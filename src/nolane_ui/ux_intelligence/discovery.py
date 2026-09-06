"""Graph-driven autonomous journey discovery for UX Intelligence v3.

Discovery ranks hypotheses about what is worth testing. It does not emit UX
findings, mutate rule authority, or upgrade inferred user intent into truth.
"""
from __future__ import annotations

from copy import deepcopy
import hashlib
import json
import math
from typing import Any, Iterable

from .goal_graph import normalize_ux_goal_graph
from .product_model import normalize_ux_product_model
from .v3_catalog import CANDIDATE_STATUSES, UX_DISCOVERY_SCORE_WEIGHTS


_MAX_DEPTH = 32


def _validate_depth(value: Any) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError("max_depth must be an integer")
    if not 1 <= value <= _MAX_DEPTH:
        raise ValueError(f"max_depth must be within 1..{_MAX_DEPTH}")
    return value


def _validate_limit(value: Any) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError("limit must be an integer")
    if not 1 <= value <= 100:
        raise ValueError("limit must be within 1..100")
    return value


def _validate_score(value: Any, label: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{label} must be numeric")
    score = float(value)
    if not math.isfinite(score) or not 0.0 <= score <= 1.0:
        raise ValueError(f"{label} must be finite and within [0, 1]")
    return score


def _semantic_hash(payload: Any) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _surface_index(model: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {item["surface_id"]: item for item in model["surfaces"]}


def _action_index(model: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {item["action_id"]: item for item in model["actions"]}


def _outcome_index(model: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {item["outcome_id"]: item for item in model.get("outcomes", ())}


def _goal_outcomes(graph: dict[str, Any], goal_id: str) -> tuple[str, ...]:
    prefix = "outcome:"
    result = []
    for edge in graph["edges"]:
        if edge["source_id"] == goal_id and edge["relation"] == "succeeds-when":
            target = edge["target_id"]
            if target.startswith(prefix):
                result.append(target[len(prefix):])
    return tuple(sorted(set(result)))


def _root_surfaces(model: dict[str, Any]) -> tuple[str, ...]:
    actions = model["actions"]
    sources = {item["source_surface_id"] for item in actions}
    targets = {
        target
        for item in actions
        for target in item["observed_target_surface_ids"]
    }
    roots = sorted(sources - targets)
    if roots:
        return tuple(roots)
    return tuple(sorted(sources))


def _adjacency(model: dict[str, Any]) -> dict[str, tuple[dict[str, Any], ...]]:
    grouped: dict[str, list[dict[str, Any]]] = {}
    for action in model["actions"]:
        grouped.setdefault(action["source_surface_id"], []).append(action)
    return {
        source: tuple(sorted(items, key=lambda item: item["action_id"]))
        for source, items in grouped.items()
    }


def _enumerate_paths(
    model: dict[str, Any],
    success_surfaces: set[str],
    max_depth: int,
) -> tuple[tuple[dict[str, Any], ...], ...]:
    adjacency = _adjacency(model)
    paths: list[tuple[dict[str, Any], ...]] = []

    def walk(
        surface_id: str,
        path: tuple[dict[str, Any], ...],
        seen_transitions: frozenset[tuple[str, str, tuple[str, ...]]],
    ) -> None:
        if path and surface_id in success_surfaces:
            paths.append(path)
            return
        if len(path) >= max_depth:
            return
        for action in adjacency.get(surface_id, ()):
            targets = tuple(action["observed_target_surface_ids"])
            transition = (surface_id, action["action_id"], targets)
            if transition in seen_transitions:
                continue
            for target in targets:
                walk(
                    target,
                    path + (action,),
                    seen_transitions | {transition},
                )

    for root in _root_surfaces(model):
        walk(root, (), frozenset())

    unique: dict[tuple[str, ...], tuple[dict[str, Any], ...]] = {}
    for path in paths:
        key = tuple(action["action_id"] for action in path)
        unique.setdefault(key, path)
    return tuple(unique[key] for key in sorted(unique))


def _step_hypothesis(action: dict[str, Any], index: int) -> dict[str, Any]:
    return {
        "candidate_step_id": f"step-{index + 1}:{action['action_id']}",
        "intent_hypothesis": f"Use {action['label']}",
        "action_id": action["action_id"],
        "source_surface_id": action["source_surface_id"],
        "expected_target_surface_ids": tuple(action["observed_target_surface_ids"]),
        "required_context_hypotheses": (),
        "preserved_context_hypotheses": (),
        "recovery_hypotheses": (),
        "evidence_refs": tuple(action["evidence_refs"]),
        "origin": action["origin"],
        "confidence": action["confidence"],
    }


def _path_fingerprint(goal_id: str, path: tuple[dict[str, Any], ...], outcome_ids: tuple[str, ...]) -> str:
    return _semantic_hash(
        {
            "goal_node_id": goal_id,
            "actions": [
                {
                    "action_id": action["action_id"],
                    "source_surface_id": action["source_surface_id"],
                    "targets": list(action["observed_target_surface_ids"]),
                }
                for action in path
            ],
            "outcomes": list(outcome_ids),
        }
    )


def _score_components(
    goal: dict[str, Any],
    path: tuple[dict[str, Any], ...],
    outcomes: tuple[dict[str, Any], ...],
    fingerprint: str,
    verified_fingerprints: set[str],
) -> dict[str, float]:
    goal_confidence = _validate_score(goal["confidence"], "goal confidence")
    success_strength = max((_validate_score(item["confidence"], "outcome confidence") for item in outcomes), default=0.0)
    if path:
        covered = sum(
            1
            for action in path
            if action.get("evidence_refs") and action.get("observed_target_surface_ids")
        )
        path_coverage = covered / len(path)
    else:
        path_coverage = 0.0
    critical = any(
        action["commitment_level"] in {"state-changing", "destructive", "external-effect"}
        for action in path
    )
    return {
        "goal_confidence": goal_confidence,
        "success_evidence_strength": success_strength,
        "path_evidence_coverage": path_coverage,
        "critical_action_presence": 1.0 if critical else 0.0,
        "recovery_relevance": 1.0 if critical else 0.0,
        "novelty_against_verified_journeys": 0.0 if fingerprint in verified_fingerprints else 1.0,
    }


def _weighted_score(components: dict[str, float]) -> float:
    score = sum(components[key] * UX_DISCOVERY_SCORE_WEIGHTS[key] for key in UX_DISCOVERY_SCORE_WEIGHTS)
    return round(score, 12)


def discover_ux_journeys(
    product_model: dict[str, Any],
    goal_graph: dict[str, Any],
    *,
    max_depth: int = 8,
    verified_journey_fingerprints: Iterable[str] = (),
) -> list[dict[str, Any]]:
    """Return deterministic journey hypotheses ranked for future verification."""
    depth = _validate_depth(max_depth)
    model = normalize_ux_product_model(product_model)
    graph = normalize_ux_goal_graph(goal_graph)
    if model["product_id"] != graph["product_id"] or model["revision"] != graph["revision"]:
        raise ValueError("product model and goal graph must describe the same product revision")

    verified = set()
    for index, item in enumerate(tuple(verified_journey_fingerprints)):
        if not isinstance(item, str) or not item.strip():
            raise ValueError(f"verified_journey_fingerprints[{index}] must be a non-empty string")
        verified.add(item)

    outcomes_by_id = _outcome_index(model)
    surfaces = _surface_index(model)
    candidates: list[dict[str, Any]] = []

    goals = sorted(
        (node for node in graph["nodes"] if node["kind"] == "goal"),
        key=lambda item: item["node_id"],
    )
    for goal in goals:
        outcome_ids = _goal_outcomes(graph, goal["node_id"])
        resolved_outcomes = tuple(outcomes_by_id[item] for item in outcome_ids if item in outcomes_by_id)
        success_surfaces = {item["surface_id"] for item in resolved_outcomes}
        if not success_surfaces:
            continue
        for path in _enumerate_paths(model, success_surfaces, depth):
            if not path:
                continue
            last_targets = set(path[-1]["observed_target_surface_ids"])
            matched_outcomes = tuple(
                item for item in resolved_outcomes if item["surface_id"] in last_targets
            )
            if not matched_outcomes:
                continue
            matched_ids = tuple(sorted(item["outcome_id"] for item in matched_outcomes))
            fingerprint = _path_fingerprint(goal["node_id"], path, matched_ids)
            components = _score_components(goal, path, matched_outcomes, fingerprint, verified)
            score = _weighted_score(components)
            refs = set(goal["evidence_refs"])
            for action in path:
                refs.update(action["evidence_refs"])
            for outcome in matched_outcomes:
                refs.update(outcome["evidence_refs"])
            first_surface = surfaces[path[0]["source_surface_id"]]
            critical_actions = tuple(
                action["action_id"]
                for action in path
                if action["commitment_level"] in {"state-changing", "destructive", "external-effect"}
            )
            steps = tuple(_step_hypothesis(action, index) for index, action in enumerate(path))
            success_hypotheses = tuple(
                {
                    "outcome_id": outcome["outcome_id"],
                    "label": outcome["label"],
                    "surface_id": outcome["surface_id"],
                    "origin": outcome["origin"],
                    "confidence": outcome["confidence"],
                    "evidence_refs": tuple(outcome["evidence_refs"]),
                }
                for outcome in sorted(matched_outcomes, key=lambda item: item["outcome_id"])
            )
            status = "hypothesis"
            candidate = {
                "candidate_id": f"uxc:{fingerprint[:24]}",
                "candidate_fingerprint": fingerprint,
                "product_id": model["product_id"],
                "revision": model["revision"],
                "goal_node_id": goal["node_id"],
                "title": f"{goal['label']} via {first_surface['locator']}",
                "entry_state": {
                    "surface_id": first_surface["surface_id"],
                    "route": first_surface["locator"],
                },
                "step_hypotheses": steps,
                "success_hypotheses": success_hypotheses,
                "critical_state_hypotheses": critical_actions,
                "discovery_score": score,
                "score_components": components,
                "origin_summary": {
                    "goal_origin": goal["origin"],
                    "path_origins": tuple(sorted({action["origin"] for action in path})),
                    "success_origins": tuple(sorted({outcome["origin"] for outcome in matched_outcomes})),
                },
                "evidence_refs": tuple(sorted(refs)),
                "provenance_ids": tuple(sorted(set(model["provenance_ids"]) | set(graph["provenance_ids"]))),
                "status": status,
            }
            candidates.append(candidate)

    deduplicated: dict[str, dict[str, Any]] = {}
    for candidate in candidates:
        existing = deduplicated.get(candidate["candidate_fingerprint"])
        if existing is None or (
            -candidate["discovery_score"], candidate["candidate_id"]
        ) < (
            -existing["discovery_score"], existing["candidate_id"]
        ):
            deduplicated[candidate["candidate_fingerprint"]] = candidate
    return sorted(
        (deepcopy(item) for item in deduplicated.values()),
        key=lambda item: (-item["discovery_score"], item["candidate_id"]),
    )


def query_ux_journey_candidates(
    candidates: Iterable[dict[str, Any]],
    *,
    goal_node_id: str | None = None,
    status: str | None = None,
    min_score: float | None = None,
    limit: int = 25,
) -> list[dict[str, Any]]:
    bounded_limit = _validate_limit(limit)
    if goal_node_id is not None and (not isinstance(goal_node_id, str) or not goal_node_id.strip()):
        raise ValueError("goal_node_id must be a non-empty string when supplied")
    if status is not None and status not in CANDIDATE_STATUSES:
        raise ValueError(f"unknown candidate status {status!r}")
    threshold = None if min_score is None else _validate_score(min_score, "min_score")

    result = []
    for index, candidate in enumerate(tuple(candidates)):
        if not isinstance(candidate, dict):
            raise TypeError(f"candidates[{index}] must be an object")
        score = _validate_score(candidate.get("discovery_score"), f"candidates[{index}].discovery_score")
        if goal_node_id is not None and candidate.get("goal_node_id") != goal_node_id:
            continue
        if status is not None and candidate.get("status") != status:
            continue
        if threshold is not None and score < threshold:
            continue
        result.append(deepcopy(candidate))
    result.sort(key=lambda item: (-item["discovery_score"], item["candidate_id"]))
    return result[:bounded_limit]


__all__ = [
    "discover_ux_journeys",
    "query_ux_journey_candidates",
]
