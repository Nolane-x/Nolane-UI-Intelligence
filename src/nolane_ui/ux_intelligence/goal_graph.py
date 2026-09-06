"""Goal-graph contracts for UX Intelligence v3.

The graph separates product facts from user-intent hypotheses. Browser/runtime
behavior can support an inference about intent, but it can never make a goal or
task an observed fact. Declared intent must come from explicit caller/product
provenance.
"""
from __future__ import annotations

from copy import deepcopy
import math
from typing import Any, Iterable

from .product_model import normalize_ux_product_model
from .provenance import UX_PROVENANCE


GRAPH_STATUSES = {"experimental", "active", "deprecated"}
NODE_KINDS = {"goal", "task", "object", "action", "state", "outcome"}
EDGE_KINDS = {
    "decomposes-to",
    "acts-on",
    "requires",
    "transitions-to",
    "succeeds-when",
    "blocked-by",
    "recovers-via",
}
ORIGINS = {"declared", "observed", "inferred"}

_REQUIRED_GRAPH_FIELDS = (
    "product_id",
    "revision",
    "nodes",
    "edges",
    "evidence_refs",
    "provenance_ids",
    "status",
)
_REQUIRED_NODE_FIELDS = (
    "node_id",
    "kind",
    "label",
    "description",
    "origin",
    "confidence",
    "evidence_refs",
)
_REQUIRED_EDGE_FIELDS = (
    "edge_id",
    "source_id",
    "relation",
    "target_id",
    "origin",
    "confidence",
    "evidence_refs",
)


def _text(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be a non-empty string")
    return value.strip()


def _sequence(value: Any, label: str) -> tuple[Any, ...]:
    if not isinstance(value, (tuple, list)):
        raise TypeError(f"{label} must be a sequence")
    return tuple(value)


def _strings(value: Any, label: str, *, allow_empty: bool = True) -> tuple[str, ...]:
    values = _sequence(value, label)
    if not allow_empty and not values:
        raise ValueError(f"{label} must not be empty")
    return tuple(_text(item, f"{label}[{index}]") for index, item in enumerate(values))


def _dedupe_strings(value: Any, label: str, *, allow_empty: bool = True) -> tuple[str, ...]:
    return tuple(sorted(set(_strings(value, label, allow_empty=allow_empty))))


def _confidence(value: Any, label: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{label} must be numeric")
    result = float(value)
    if not math.isfinite(result) or not 0.0 <= result <= 1.0:
        raise ValueError(f"{label} must be finite and within [0, 1]")
    return result


def _known_provenance(provenance_catalog: Iterable[dict[str, Any]]) -> set[str]:
    return {str(item["provenance_id"]) for item in provenance_catalog}


def _validate_provenance_ids(
    value: Any,
    label: str,
    provenance_catalog: Iterable[dict[str, Any]],
) -> tuple[str, ...]:
    ids = _dedupe_strings(value, label)
    unknown = set(ids) - _known_provenance(provenance_catalog)
    if unknown:
        raise ValueError(f"{label} contains unknown provenance ids: {sorted(unknown)}")
    return ids


def _require_fields(record: dict[str, Any], fields: tuple[str, ...], label: str) -> None:
    missing = [field for field in fields if field not in record]
    if missing:
        raise ValueError(f"{label} missing required fields: {missing}")


def _validate_origin(
    record: dict[str, Any],
    label: str,
    *,
    intent: bool = False,
) -> None:
    origin = record.get("origin")
    if origin not in ORIGINS:
        raise ValueError(f"{label}.origin must be one of {sorted(ORIGINS)}")
    if intent and origin == "observed":
        raise ValueError(f"{label}: intent nodes cannot use observed origin")
    _confidence(record.get("confidence"), f"{label}.confidence")
    evidence_refs = _strings(record.get("evidence_refs"), f"{label}.evidence_refs")
    if origin in {"observed", "inferred"} and not evidence_refs:
        raise ValueError(f"{label}: {origin} records require evidence_refs")


def validate_ux_goal_graph(
    graph: dict[str, Any],
    *,
    provenance_catalog: Iterable[dict[str, Any]] = UX_PROVENANCE,
) -> dict[str, Any]:
    if not isinstance(graph, dict):
        raise TypeError("UX goal graph must be an object")
    missing = [field for field in _REQUIRED_GRAPH_FIELDS if field not in graph]
    if missing:
        raise ValueError(f"UX goal graph missing required fields: {missing}")

    product_id = _text(graph.get("product_id"), "product_id")
    _text(graph.get("revision"), "revision")
    if graph.get("status") not in GRAPH_STATUSES:
        raise ValueError(f"unknown UX goal graph status {graph.get('status')!r}")
    _strings(graph.get("evidence_refs"), "evidence_refs")
    _validate_provenance_ids(graph.get("provenance_ids"), "provenance_ids", provenance_catalog)

    nodes = _sequence(graph.get("nodes"), "nodes")
    node_ids: set[str] = set()
    for index, raw in enumerate(nodes):
        if not isinstance(raw, dict):
            raise TypeError(f"nodes[{index}] must be an object")
        _require_fields(raw, _REQUIRED_NODE_FIELDS, f"nodes[{index}]")
        node_id = _text(raw.get("node_id"), f"nodes[{index}].node_id")
        if node_id in node_ids:
            raise ValueError(f"duplicate node_id {node_id}")
        node_ids.add(node_id)
        kind = raw.get("kind")
        if kind not in NODE_KINDS:
            raise ValueError(f"{node_id}: unknown node kind {kind!r}")
        _text(raw.get("label"), f"{node_id}.label")
        _text(raw.get("description"), f"{node_id}.description")
        _validate_origin(raw, node_id, intent=kind in {"goal", "task"})

    edges = _sequence(graph.get("edges"), "edges")
    edge_ids: set[str] = set()
    for index, raw in enumerate(edges):
        if not isinstance(raw, dict):
            raise TypeError(f"edges[{index}] must be an object")
        _require_fields(raw, _REQUIRED_EDGE_FIELDS, f"edges[{index}]")
        edge_id = _text(raw.get("edge_id"), f"edges[{index}].edge_id")
        if edge_id in edge_ids:
            raise ValueError(f"duplicate edge_id {edge_id}")
        edge_ids.add(edge_id)
        source_id = _text(raw.get("source_id"), f"{edge_id}.source_id")
        target_id = _text(raw.get("target_id"), f"{edge_id}.target_id")
        if source_id not in node_ids:
            raise ValueError(f"{edge_id}: unresolved source node {source_id!r}")
        if target_id not in node_ids:
            raise ValueError(f"{edge_id}: unresolved target node {target_id!r}")
        relation = raw.get("relation")
        if relation not in EDGE_KINDS:
            raise ValueError(f"{edge_id}: unknown edge relation {relation!r}")
        if relation == "decomposes-to" and source_id == target_id:
            raise ValueError(f"{edge_id}: self-decomposition is invalid")
        _validate_origin(raw, edge_id)

    return {
        "valid": True,
        "product_id": product_id,
        "node_count": len(nodes),
        "edge_count": len(edges),
        "declared_goal_count": sum(
            1 for node in nodes if node["kind"] == "goal" and node["origin"] == "declared"
        ),
        "inferred_goal_count": sum(
            1 for node in nodes if node["kind"] == "goal" and node["origin"] == "inferred"
        ),
        "errors": [],
    }


def normalize_ux_goal_graph(
    graph: dict[str, Any],
    *,
    provenance_catalog: Iterable[dict[str, Any]] = UX_PROVENANCE,
) -> dict[str, Any]:
    validate_ux_goal_graph(graph, provenance_catalog=provenance_catalog)
    out = deepcopy(graph)
    out["evidence_refs"] = _dedupe_strings(out["evidence_refs"], "evidence_refs")
    out["provenance_ids"] = _dedupe_strings(out["provenance_ids"], "provenance_ids")
    normalized_nodes = []
    for node in out["nodes"]:
        item = deepcopy(node)
        item["evidence_refs"] = _dedupe_strings(item["evidence_refs"], f"{item['node_id']}.evidence_refs")
        normalized_nodes.append(item)
    normalized_edges = []
    for edge in out["edges"]:
        item = deepcopy(edge)
        item["evidence_refs"] = _dedupe_strings(item["evidence_refs"], f"{item['edge_id']}.evidence_refs")
        normalized_edges.append(item)
    out["nodes"] = tuple(sorted(normalized_nodes, key=lambda item: item["node_id"]))
    out["edges"] = tuple(sorted(normalized_edges, key=lambda item: item["edge_id"]))
    return out


def _node_id(kind: str, local_id: str) -> str:
    return f"{kind}:{_text(local_id, f'{kind}_id')}"


def _edge_id(source_id: str, relation: str, target_id: str) -> str:
    return f"uxe:{source_id}:{relation}:{target_id}"


def _display_label(record: dict[str, Any], fallback: str) -> str:
    labels = record.get("labels", ())
    if isinstance(labels, (tuple, list)) and labels:
        first = labels[0]
        if isinstance(first, str) and first.strip():
            return first.strip()
    label = record.get("label")
    if isinstance(label, str) and label.strip():
        return label.strip()
    return fallback


def _product_nodes(product_model: dict[str, Any]) -> list[dict[str, Any]]:
    nodes: list[dict[str, Any]] = []
    for record in product_model["objects"]:
        nodes.append(
            {
                "node_id": _node_id("object", record["object_id"]),
                "kind": "object",
                "label": _display_label(record, record["object_id"]),
                "description": f"Product object {record['object_type']}",
                "origin": record["origin"],
                "confidence": record["confidence"],
                "evidence_refs": tuple(record["evidence_refs"]),
            }
        )
    for record in product_model["actions"]:
        nodes.append(
            {
                "node_id": _node_id("action", record["action_id"]),
                "kind": "action",
                "label": record["label"],
                "description": f"Product action {record['action_id']}",
                "origin": record["origin"],
                "confidence": record["confidence"],
                "evidence_refs": tuple(record["evidence_refs"]),
            }
        )
    for record in product_model["states"]:
        nodes.append(
            {
                "node_id": _node_id("state", record["state_id"]),
                "kind": "state",
                "label": record["state_id"],
                "description": "Observed product state",
                "origin": record["origin"],
                "confidence": record["confidence"],
                "evidence_refs": tuple(record["evidence_refs"]),
            }
        )
    for record in product_model.get("outcomes", ()):
        nodes.append(
            {
                "node_id": _node_id("outcome", record["outcome_id"]),
                "kind": "outcome",
                "label": record["label"],
                "description": "Observed product outcome",
                "origin": record["origin"],
                "confidence": record["confidence"],
                "evidence_refs": tuple(record["evidence_refs"]),
            }
        )
    return nodes


def _seed_goal(
    seed: dict[str, Any],
    *,
    origin: str,
    node_store: dict[str, dict[str, Any]],
    edge_store: dict[str, dict[str, Any]],
    provenance_ids: set[str],
    evidence_refs: set[str],
    known_provenance: set[str],
) -> None:
    if not isinstance(seed, dict):
        raise TypeError("goal seeds must be objects")
    goal_id = _node_id("goal", seed.get("goal_id"))
    label = _text(seed.get("label"), f"{goal_id}.label")
    description = _text(seed.get("description"), f"{goal_id}.description")
    if origin == "declared":
        seed_provenance = _dedupe_strings(seed.get("provenance_ids", ()), f"{goal_id}.provenance_ids", allow_empty=False)
        unknown = set(seed_provenance) - known_provenance
        if unknown:
            raise ValueError(f"{goal_id}: unknown provenance ids {sorted(unknown)}")
        provenance_ids.update(seed_provenance)
        confidence = 1.0
        seed_evidence: tuple[str, ...] = ()
    else:
        seed_evidence = _dedupe_strings(seed.get("evidence_refs", ()), f"{goal_id}.evidence_refs", allow_empty=False)
        confidence = _confidence(seed.get("confidence"), f"{goal_id}.confidence")
        evidence_refs.update(seed_evidence)

    node_store[goal_id] = {
        "node_id": goal_id,
        "kind": "goal",
        "label": label,
        "description": description,
        "origin": origin,
        "confidence": confidence,
        "evidence_refs": seed_evidence,
    }

    for local_task_id in _dedupe_strings(seed.get("task_ids", ()), f"{goal_id}.task_ids"):
        task_id = _node_id("task", local_task_id)
        task = node_store.get(task_id)
        if task is None:
            task = {
                "node_id": task_id,
                "kind": "task",
                "label": local_task_id.replace("-", " ").strip().title(),
                "description": f"{origin.title()} task for goal {label}",
                "origin": origin,
                "confidence": confidence,
                "evidence_refs": seed_evidence,
            }
            node_store[task_id] = task
        elif task["origin"] != origin:
            raise ValueError(f"{task_id}: conflicting declared/inferred task origins")
        edge_id = _edge_id(goal_id, "decomposes-to", task_id)
        edge_store[edge_id] = {
            "edge_id": edge_id,
            "source_id": goal_id,
            "relation": "decomposes-to",
            "target_id": task_id,
            "origin": origin,
            "confidence": confidence,
            "evidence_refs": seed_evidence,
        }

    for local_outcome_id in _dedupe_strings(seed.get("outcome_ids", ()), f"{goal_id}.outcome_ids"):
        outcome_id = _node_id("outcome", local_outcome_id)
        if outcome_id not in node_store:
            raise ValueError(f"{goal_id}: unresolved outcome {outcome_id!r}")
        edge_id = _edge_id(goal_id, "succeeds-when", outcome_id)
        edge_store[edge_id] = {
            "edge_id": edge_id,
            "source_id": goal_id,
            "relation": "succeeds-when",
            "target_id": outcome_id,
            "origin": origin,
            "confidence": confidence,
            "evidence_refs": seed_evidence,
        }


def build_ux_goal_graph(
    product_model: dict[str, Any],
    *,
    declared_goals: Iterable[dict[str, Any]] = (),
    inferred_goals: Iterable[dict[str, Any]] = (),
    provenance_catalog: Iterable[dict[str, Any]] = UX_PROVENANCE,
) -> dict[str, Any]:
    model = normalize_ux_product_model(product_model, provenance_catalog=provenance_catalog)
    node_store = {node["node_id"]: node for node in _product_nodes(model)}
    edge_store: dict[str, dict[str, Any]] = {}
    provenance_ids = set(model["provenance_ids"])
    evidence_refs = set(model["evidence_refs"])
    known_provenance = _known_provenance(provenance_catalog)

    declared = tuple(declared_goals)
    inferred = tuple(inferred_goals)
    for seed in sorted(declared, key=lambda item: str(item.get("goal_id", ""))):
        _seed_goal(
            seed,
            origin="declared",
            node_store=node_store,
            edge_store=edge_store,
            provenance_ids=provenance_ids,
            evidence_refs=evidence_refs,
            known_provenance=known_provenance,
        )
    for seed in sorted(inferred, key=lambda item: str(item.get("goal_id", ""))):
        candidate_id = _node_id("goal", seed.get("goal_id"))
        if candidate_id in node_store:
            raise ValueError(f"{candidate_id}: inferred goal conflicts with existing declared/product node")
        _seed_goal(
            seed,
            origin="inferred",
            node_store=node_store,
            edge_store=edge_store,
            provenance_ids=provenance_ids,
            evidence_refs=evidence_refs,
            known_provenance=known_provenance,
        )

    graph = {
        "product_id": model["product_id"],
        "revision": model["revision"],
        "nodes": tuple(sorted(node_store.values(), key=lambda item: item["node_id"])),
        "edges": tuple(sorted(edge_store.values(), key=lambda item: item["edge_id"])),
        "evidence_refs": tuple(sorted(evidence_refs)),
        "provenance_ids": tuple(sorted(provenance_ids)),
        "status": "active",
    }
    validate_ux_goal_graph(graph, provenance_catalog=provenance_catalog)
    return normalize_ux_goal_graph(graph, provenance_catalog=provenance_catalog)


__all__ = [
    "EDGE_KINDS",
    "GRAPH_STATUSES",
    "NODE_KINDS",
    "build_ux_goal_graph",
    "normalize_ux_goal_graph",
    "validate_ux_goal_graph",
]
