"""NUI v12 external UI implementation-intelligence routing.

This layer is deterministic and deliberately does not confer authority from a
link. It resolves bounded reference packets, prefers permissive implementations
when capability is comparable, and keeps source/license obligations alive until
runtime verification and provenance are closed.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable

PERMISSIVE_LICENSES = frozenset({
    "MIT", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause", "ISC", "0BSD", "CC0-1.0"
})
RECONSULT_STAGES = (
    "intent", "design", "implementation-selection", "license-gate",
    "critique", "runtime-verification", "provenance",
)
_LICENSE_PENALTY = {
    "green": 0.0, "unverified": 0.18, "consent": 0.28,
    "restricted": 0.28, "mixed": 0.28, "reference-only": 0.55,
}
_HEALTH_BONUS = {"active": 0.06, "maintenance": 0.02, "unmaintained": -0.08, "archived": -0.16}
_COMPACT_FIELDS = (
    "id", "name", "repo", "family", "role", "mechanism", "license_status",
    "license_id", "adoption_mode", "health", "drift", "stacks", "fallbacks",
)


def _license_status(candidate: dict[str, Any]) -> str:
    data = candidate.get("license", {})
    return str(data.get("status", "unverified")) if isinstance(data, dict) else "unverified"


def _normalize_candidate(candidate: dict[str, Any]) -> dict[str, Any]:
    result = dict(candidate)
    status = _license_status(result)
    result["requires_user_consent"] = status in {"consent", "restricted", "mixed"}
    result["direct_adoption_allowed"] = status == "green" and result.get("adoption_mode") not in {
        "reference-only", "discovery-only"
    }
    return result


def _expand_compact_row(row: list[Any]) -> dict[str, Any]:
    if len(row) != len(_COMPACT_FIELDS):
        raise ValueError(f"external UI source row has {len(row)} fields; expected {len(_COMPACT_FIELDS)}")
    item = dict(zip(_COMPACT_FIELDS, row))
    repo = str(item.pop("repo"))
    mechanism = str(item.pop("mechanism"))
    status = str(item.pop("license_status"))
    license_id = str(item.pop("license_id"))
    item["url"] = f"https://github.com/{repo}"
    item["mechanisms"] = [mechanism]
    item["license"] = {
        "status": status,
        "id": license_id,
        "scope": "re-verify exact code/package/component/example/asset/font/trademark scope at point of material use",
    }
    item["reconsult_at"] = list(RECONSULT_STAGES)
    return _normalize_candidate(item)


def load_external_ui_network(root: str | Path) -> dict[str, Any]:
    """Load and normalize the sharded v12 external-source manifest."""
    root_path = Path(root)
    manifest_path = root_path / "knowledge" / "external-ui-intelligence-network-v12.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    sources: list[dict[str, Any]] = []
    for relative in manifest.get("shards", []):
        shard = json.loads((root_path / relative).read_text(encoding="utf-8"))
        for row in shard.get("sources", []):
            sources.append(_expand_compact_row(row))
    return {
        "version": manifest.get("version", 12),
        "as_of": manifest.get("as_of"),
        "policy": manifest.get("policy", {}),
        "sources": sources,
    }


def rank_reference_candidates(candidates: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    """Prefer permissive sources when capability is comparable.

    Capability remains primary. A restrictive source can win only when its
    unique-requirement fit is materially stronger; a small aesthetic/quality
    edge cannot defeat an otherwise suitable permissive implementation.
    """
    ranked: list[tuple[float, str, dict[str, Any]]] = []
    for raw in candidates:
        item = _normalize_candidate(raw)
        capability_fit = float(item.get("capability_fit", 0.75))
        unique_fit = float(item.get("unique_requirement_fit", 0.0))
        stack_fit = float(item.get("stack_fit", 0.0))
        evidence_fit = float(item.get("evidence_fit", 0.0))
        status = _license_status(item)
        score = (
            capability_fit + 0.45 * unique_fit + 0.08 * stack_fit + 0.05 * evidence_fit
            + _HEALTH_BONUS.get(str(item.get("health", "maintenance")), 0.0)
            - _LICENSE_PENALTY.get(status, 0.22)
        )
        item["selection_score"] = round(score, 6)
        ranked.append((score, str(item.get("id", "")), item))
    ranked.sort(key=lambda row: (-row[0], row[1]))
    return [row[2] for row in ranked]


def _source_map(network: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {str(s["id"]): s for s in network.get("sources", []) if isinstance(s, dict) and s.get("id")}


def resolve_reference_pack(
    pack_id: str,
    network: dict[str, Any],
    packs: dict[str, Any],
    *,
    stack: str | None = None,
    max_sources: int = 8,
) -> dict[str, Any]:
    if max_sources < 1:
        raise ValueError("max_sources must be positive")
    pack = next((p for p in packs.get("packs", []) if p.get("id") == pack_id), None)
    if not isinstance(pack, dict):
        raise KeyError(f"unknown reference pack: {pack_id}")
    sources = _source_map(network)
    ordered_ids = list(dict.fromkeys(pack.get("preferred_sources", []) + pack.get("fallback_sources", [])))
    candidates: list[dict[str, Any]] = []
    preferred_count = len(pack.get("preferred_sources", []))
    for index, source_id in enumerate(ordered_ids):
        source = sources.get(str(source_id))
        if source is None:
            continue
        candidate = dict(source)
        candidate["capability_fit"] = max(0.55, 1.0 - index * 0.035)
        # Explicitly allow a pack to record a unique reason a non-GREEN source matters.
        unique = pack.get("unique_requirement_sources", {})
        candidate["unique_requirement_fit"] = float(unique.get(source_id, 0.0)) if isinstance(unique, dict) else 0.0
        stacks = candidate.get("stacks", [])
        candidate["stack_fit"] = 1.0 if stack and (stack in stacks or "framework-agnostic" in stacks) else 0.0
        candidate["preferred_by_pack"] = index < preferred_count
        candidates.append(candidate)
    selected = rank_reference_candidates(candidates)[:max_sources]
    consent_sources = [item["id"] for item in selected if item.get("requires_user_consent")]
    unresolved_sources = [item["id"] for item in selected if _license_status(item) == "unverified"]
    return {
        "pack_id": pack_id,
        "sources": selected,
        "reconsult_at": list(RECONSULT_STAGES),
        "license_gate": {
            "policy": "permissive-first",
            "requires_user_consent": bool(consent_sources),
            "consent_sources": consent_sources,
            "live_verification_required": unresolved_sources,
            "decline_behavior": "select strongest GREEN fallback or synthesize the mechanism independently",
        },
    }


def validate_external_ui_network(
    network: dict[str, Any], packs: dict[str, Any], license_policy: dict[str, Any]
) -> dict[str, Any]:
    errors: list[str] = []
    sources = network.get("sources", []) if isinstance(network, dict) else []
    pack_items = packs.get("packs", []) if isinstance(packs, dict) else []
    if len(sources) < 140:
        errors.append("external UI network must contain at least 140 typed sources")
    if len(pack_items) < 30:
        errors.append("external UI network must contain at least 30 task-shaped reference packs")

    required = {
        "id", "name", "url", "family", "role", "mechanisms", "adoption_mode",
        "license", "health", "drift", "fallbacks", "reconsult_at",
    }
    by_id: dict[str, dict[str, Any]] = {}
    for index, source in enumerate(sources):
        if not isinstance(source, dict):
            errors.append(f"source {index} must be an object")
            continue
        missing = required - set(source)
        if missing:
            errors.append(f"source {source.get('id', index)} missing {sorted(missing)}")
            continue
        source_id = str(source["id"])
        if source_id in by_id:
            errors.append(f"duplicate source id: {source_id}")
        by_id[source_id] = source
        if not source.get("mechanisms"):
            errors.append(f"source {source_id} requires mechanisms")
        if source.get("reconsult_at") != list(RECONSULT_STAGES):
            errors.append(f"source {source_id} must persist through all reconsult stages")
        status = _license_status(source)
        if status in {"consent", "restricted", "mixed"} and source.get("requires_user_consent") is not True:
            errors.append(f"source {source_id} restrictive scope must require user consent")
        if source.get("adoption_mode") in {"reference-only", "discovery-only"} and source.get("direct_adoption_allowed") is True:
            errors.append(f"source {source_id} cannot direct-adopt from {source.get('adoption_mode')}")
        if status == "green" and source.get("license", {}).get("id") not in PERMISSIVE_LICENSES:
            errors.append(f"source {source_id} marks non-permissive license as green")

    pack_ids: set[str] = set()
    for index, pack in enumerate(pack_items):
        if not isinstance(pack, dict) or not pack.get("id"):
            errors.append(f"pack {index} requires id")
            continue
        pack_id = str(pack["id"])
        if pack_id in pack_ids:
            errors.append(f"duplicate pack id: {pack_id}")
        pack_ids.add(pack_id)
        if pack.get("reconsult_at") != list(RECONSULT_STAGES):
            errors.append(f"pack {pack_id} must persist through all reconsult stages")
        referenced = list(pack.get("preferred_sources", [])) + list(pack.get("fallback_sources", []))
        unknown = sorted({str(source_id) for source_id in referenced} - set(by_id))
        if unknown:
            errors.append(f"pack {pack_id} references unknown sources {unknown}")
        preferred = [by_id[sid] for sid in pack.get("preferred_sources", []) if sid in by_id]
        has_green = any(_license_status(s) == "green" and s.get("license", {}).get("id") in PERMISSIVE_LICENSES for s in preferred)
        if not has_green and not pack.get("restricted_only_reason"):
            errors.append(f"pack {pack_id} requires a permissive preferred route or restricted_only_reason")

    policy = license_policy.get("policy", {}) if isinstance(license_policy, dict) else {}
    if policy.get("selection_default") != "permissive-first":
        errors.append("license policy must default to permissive-first")
    if policy.get("awesome_lists_are") != "discovery-only":
        errors.append("awesome lists must remain discovery-only")
    if policy.get("reverify_at_point_of_use") is not True:
        errors.append("license policy must reverify exact upstream scope at point of use")

    return {"valid": not errors, "errors": errors, "source_count": len(sources), "pack_count": len(pack_items)}
