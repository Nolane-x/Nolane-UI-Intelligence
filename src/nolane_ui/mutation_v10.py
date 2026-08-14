"""Semantic mutation and ablation contracts for NUI V10."""
from __future__ import annotations

from typing import Any


def _text(v: Any) -> bool:
    return isinstance(v, str) and bool(v.strip())


def _ids(source: Any, key: str) -> set[str]:
    if isinstance(source, dict) and isinstance(source.get(key), list):
        return {str(x).strip() for x in source[key] if _text(x)}
    return set()


def validate_mutation_registry(record: dict[str, Any], hypotheses: dict[str, Any], tasks: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(record, dict) or record.get("version") != 10:
        errors.append("mutation registry must declare version 10")
    raw = record.get("mutations", []) if isinstance(record, dict) else []
    if not isinstance(raw, list) or not raw:
        return {"valid": False, "errors": errors + ["mutation registry requires mutations"], "mutation_ids": [], "ablation_ids": []}

    known_h = _ids(hypotheses, "hypothesis_ids")
    known_t = _ids(tasks, "task_ids")
    seen: set[str] = set()
    ablations: set[str] = set()

    for i, item in enumerate(raw):
        if not isinstance(item, dict):
            errors.append(f"mutation[{i}] must be an object")
            continue
        mid = str(item.get("id", "")).strip()
        if not mid:
            errors.append(f"mutation[{i}] requires id")
            continue
        if mid in seen:
            errors.append(f"duplicate mutation id {mid}")
        seen.add(mid)
        kind = item.get("kind")
        if kind not in {"semantic", "placebo", "interaction", "ablation"}:
            errors.append(f"mutation {mid} has invalid kind {kind}")
        hid = str(item.get("target_hypothesis", "")).strip()
        if not hid:
            errors.append(f"mutation {mid} requires target_hypothesis")
        elif known_h and hid not in known_h:
            errors.append(f"mutation {mid} references unknown hypothesis {hid}")
        if not _text(item.get("target_owner")):
            errors.append(f"mutation {mid} requires target_owner")
        dimensions = item.get("target_dimensions")
        if not isinstance(dimensions, list) or not dimensions or any(not _text(x) for x in dimensions):
            errors.append(f"mutation {mid} requires target_dimensions")
        exposed = item.get("exposed_tasks")
        if not isinstance(exposed, list) or not exposed:
            errors.append(f"mutation {mid} requires exposed_tasks")
        elif known_t:
            unknown = {str(x) for x in exposed} - known_t
            if unknown:
                errors.append(f"mutation {mid} references unknown tasks: {sorted(unknown)}")
        if not _text(item.get("operation")):
            errors.append(f"mutation {mid} requires operation")
        effect = item.get("expected_effect")
        if not isinstance(effect, dict):
            errors.append(f"mutation {mid} requires expected_effect")
            effect = {}
        direction = effect.get("direction")
        if kind in {"semantic", "ablation", "interaction"}:
            if direction not in {"decrease", "targeted-degradation", "interaction-degradation"}:
                errors.append(f"mutation {mid} must declare expected targeted degradation")
            if not _text(effect.get("causal_rationale")):
                errors.append(f"mutation {mid} expected degradation requires causal_rationale")
        if kind == "placebo":
            if direction != "no-material-change":
                errors.append(f"placebo mutation {mid} must expect no-material-change")
            stable = item.get("stable_dimensions")
            if not isinstance(stable, list) or not stable or any(not _text(x) for x in stable):
                errors.append(f"placebo mutation {mid} requires stable_dimensions")
        ablation_id = item.get("ablation_id")
        if kind == "ablation" or _text(ablation_id):
            ablations.add(str(ablation_id or mid))

    return {"valid": not errors, "errors": errors, "mutation_ids": sorted(seen), "ablation_ids": sorted(ablations), "mutation_count": len(seen)}


def expected_mutation_effects(record: dict[str, Any]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for item in record.get("mutations", []) if isinstance(record, dict) else []:
        if isinstance(item, dict) and _text(item.get("id")):
            out[str(item["id"])] = dict(item.get("expected_effect", {}))
    return out


__all__ = ["validate_mutation_registry", "expected_mutation_effects"]
