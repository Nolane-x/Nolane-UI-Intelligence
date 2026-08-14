"""Behavioral hypothesis contracts for NUI V10.

V10 treats a design rule as an efficacy hypothesis only when it exposes an
observable decision change, controls, falsifiers and benchmark surfaces.  This
module validates that evidence topology; it does not claim that the hypothesis
has already been empirically confirmed.
"""
from __future__ import annotations

from collections import defaultdict
from typing import Any


def _text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _strings(value: Any, field: str, errors: list[str], *, minimum: int = 1) -> list[str]:
    if not isinstance(value, list):
        errors.append(f"{field} must be a list")
        return []
    result = [str(x).strip() for x in value if _text(x)]
    if len(result) != len(value):
        errors.append(f"{field} must contain only non-empty strings")
    if len(result) < minimum:
        errors.append(f"{field} requires at least {minimum} item(s)")
    if len(result) != len(set(result)):
        errors.append(f"{field} must not contain duplicates")
    return result


def validate_hypothesis_registry(record: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(record, dict):
        return {"valid": False, "errors": ["hypothesis registry must be an object"]}
    if record.get("version") != 10:
        errors.append("hypothesis registry must declare version 10")

    raw = record.get("hypotheses")
    if not isinstance(raw, list) or not raw:
        return {"valid": False, "errors": errors + ["hypothesis registry requires hypotheses"], "hypothesis_ids": []}

    hypotheses = [x for x in raw if isinstance(x, dict)]
    if len(hypotheses) != len(raw):
        errors.append("every hypothesis must be an object")

    ids: list[str] = []
    observable_to_ids: dict[str, list[str]] = defaultdict(list)
    interactions: dict[str, set[str]] = {}
    dimensions: set[str] = set()
    tasks: set[str] = set()
    mutations: set[str] = set()
    ablations: set[str] = set()

    required_text = ("hypothesis_id", "decision_boundary", "observable_behavior", "baseline_failure")
    required_lists = (
        "owners", "positive_controls", "negative_controls", "evidence_channels", "falsifiers",
        "dimensions", "tasks", "mutations", "ablations", "prohibited_overclaims",
    )

    for index, item in enumerate(hypotheses):
        for field in required_text:
            if not _text(item.get(field)):
                errors.append(f"hypothesis[{index}] requires {field}")
        hid = str(item.get("hypothesis_id", "")).strip()
        if hid:
            ids.append(hid)

        parsed: dict[str, list[str]] = {}
        for field in required_lists:
            parsed[field] = _strings(item.get(field), f"hypothesis {hid or index} {field}", errors)

        if hid:
            observable = str(item.get("observable_behavior", "")).strip().lower()
            if observable:
                observable_to_ids[observable].append(hid)
            interactions[hid] = set(_strings(item.get("interaction_with", []), f"hypothesis {hid} interaction_with", errors, minimum=0))

        dimensions.update(parsed["dimensions"])
        tasks.update(parsed["tasks"])
        mutations.update(parsed["mutations"])
        ablations.update(parsed["ablations"])

        if set(parsed["positive_controls"]) & set(parsed["negative_controls"]):
            errors.append(f"hypothesis {hid or index} cannot reuse the same positive and negative control")
        if set(parsed["falsifiers"]) & set(parsed["prohibited_overclaims"]):
            errors.append(f"hypothesis {hid or index} falsifiers and overclaim boundaries must be distinct")

    duplicates = sorted({x for x in ids if ids.count(x) > 1})
    if duplicates:
        errors.append(f"duplicate hypothesis ids: {duplicates}")

    for observable, linked in observable_to_ids.items():
        if len(linked) < 2:
            continue
        for i, left in enumerate(linked):
            for right in linked[i + 1:]:
                if right not in interactions.get(left, set()) and left not in interactions.get(right, set()):
                    errors.append(
                        f"observable-behavior overlap between {left} and {right} requires an explicit interaction declaration: {observable}"
                    )

    return {
        "valid": not errors,
        "errors": errors,
        "hypothesis_ids": ids,
        "hypothesis_count": len(hypotheses),
        "dimensions": sorted(dimensions),
        "task_ids": sorted(tasks),
        "mutation_ids": sorted(mutations),
        "ablation_ids": sorted(ablations),
    }


__all__ = ["validate_hypothesis_registry"]
