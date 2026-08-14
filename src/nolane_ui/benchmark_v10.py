"""Original benchmark corpus contracts for NUI V10.

Generation tasks and evaluator answer keys are deliberately stored in separate
records.  The validator rejects leakage, missing holdouts and broken references.
"""
from __future__ import annotations

from typing import Any


def _text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _list(value: Any, field: str, errors: list[str], minimum: int = 1) -> list[Any]:
    if not isinstance(value, list) or len(value) < minimum:
        errors.append(f"{field} requires at least {minimum} item(s)")
        return []
    return value


def _ids(source: Any, key: str) -> set[str]:
    if isinstance(source, dict):
        value = source.get(key, [])
        if isinstance(value, list):
            return {str(x).strip() for x in value if _text(x)}
    return set()


def validate_task_corpus(public: dict[str, Any], hidden: dict[str, Any], hypotheses: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(public, dict) or public.get("version") != 10:
        errors.append("public task corpus must declare version 10")
    if not isinstance(hidden, dict) or hidden.get("version") != 10:
        errors.append("hidden task corpus must declare version 10")

    pub_items = public.get("tasks", []) if isinstance(public, dict) else []
    hid_items = hidden.get("tasks", []) if isinstance(hidden, dict) else []
    if not isinstance(pub_items, list) or not pub_items:
        errors.append("public task corpus requires tasks")
        pub_items = []
    if not isinstance(hid_items, list) or not hid_items:
        errors.append("hidden task corpus requires tasks")
        hid_items = []

    pub_map: dict[str, dict[str, Any]] = {}
    hid_map: dict[str, dict[str, Any]] = {}
    splits: set[str] = set()
    families: set[str] = set()
    complexities: set[str] = set()
    hypothesis_ids = _ids(hypotheses, "hypothesis_ids")
    forbidden_public = {"checklist", "expected_failure_traps", "hard_blockers", "judge_dimensions", "leakage_sensitive_phrases", "treatment", "answer_key"}

    for index, item in enumerate(pub_items):
        if not isinstance(item, dict):
            errors.append(f"public task[{index}] must be an object")
            continue
        tid = str(item.get("id", "")).strip()
        if not tid:
            errors.append(f"public task[{index}] requires id")
            continue
        if tid in pub_map:
            errors.append(f"duplicate public task id {tid}")
        pub_map[tid] = item
        for field in ("family", "split", "complexity", "prompt"):
            if not _text(item.get(field)):
                errors.append(f"public task {tid} requires {field}")
        if item.get("split") not in {"dev", "holdout"}:
            errors.append(f"public task {tid} split must be dev or holdout")
        if item.get("complexity") not in {"low", "medium", "high"}:
            errors.append(f"public task {tid} complexity must be low, medium or high")
        if item.get("split"):
            splits.add(str(item.get("split")))
        if _text(item.get("family")):
            families.add(str(item.get("family")))
        if _text(item.get("complexity")):
            complexities.add(str(item.get("complexity")))
        _list(item.get("artifact_requirements"), f"public task {tid} artifact_requirements", errors)
        leaked_fields = forbidden_public.intersection(item)
        if leaked_fields:
            errors.append(f"public task {tid} leaks evaluator-only fields: {sorted(leaked_fields)}")

    for index, item in enumerate(hid_items):
        if not isinstance(item, dict):
            errors.append(f"hidden task[{index}] must be an object")
            continue
        tid = str(item.get("id", "")).strip()
        if not tid:
            errors.append(f"hidden task[{index}] requires id")
            continue
        if tid in hid_map:
            errors.append(f"duplicate hidden task id {tid}")
        hid_map[tid] = item
        for field in ("expected_failure_traps", "judge_dimensions", "checklist", "leakage_sensitive_phrases", "hypotheses", "ablations"):
            _list(item.get(field), f"hidden task {tid} {field}", errors)
        if not isinstance(item.get("hard_blockers", []), list):
            errors.append(f"hidden task {tid} hard_blockers must be a list")
        if hypothesis_ids:
            unknown = {str(x) for x in item.get("hypotheses", [])} - hypothesis_ids
            if unknown:
                errors.append(f"hidden task {tid} references unknown hypotheses: {sorted(unknown)}")

    if set(pub_map) != set(hid_map):
        errors.append(
            f"public/hidden task ids must match exactly; public-only={sorted(set(pub_map)-set(hid_map))}, hidden-only={sorted(set(hid_map)-set(pub_map))}"
        )

    for tid in sorted(set(pub_map) & set(hid_map)):
        prompt = str(pub_map[tid].get("prompt", "")).lower()
        hidden_item = hid_map[tid]
        sensitive = list(hidden_item.get("leakage_sensitive_phrases", [])) + list(hidden_item.get("checklist", []))
        leaked = sorted({str(p) for p in sensitive if _text(p) and str(p).strip().lower() in prompt})
        if leaked:
            errors.append(f"public task {tid} leaks hidden evaluator language: {leaked}")

    if pub_items and "holdout" not in splits:
        errors.append("benchmark corpus requires a holdout split before transfer claims are possible")
    if pub_items and "dev" not in splits:
        errors.append("benchmark corpus requires a dev split")
    if len(pub_items) >= 12 and len(families) < 8:
        errors.append("large V10 corpus must span at least eight task families")
    if len(pub_items) >= 12 and not {"low", "medium", "high"}.issubset(complexities):
        errors.append("large V10 corpus must include low, medium and high complexity tasks")

    return {
        "valid": not errors,
        "errors": errors,
        "task_ids": sorted(pub_map),
        "task_count": len(pub_map),
        "families": sorted(families),
        "splits": sorted(splits),
    }


def materialize_task_for_generation(public: dict[str, Any], task_id: str) -> dict[str, Any]:
    for item in public.get("tasks", []) if isinstance(public, dict) else []:
        if isinstance(item, dict) and item.get("id") == task_id:
            allowed = {"id", "family", "split", "complexity", "prompt", "artifact_requirements", "constraints", "platform", "modalities"}
            return {k: v for k, v in item.items() if k in allowed}
    raise KeyError(task_id)


def materialize_task_for_judge(public: dict[str, Any], hidden: dict[str, Any], task_id: str) -> dict[str, Any]:
    public_task = materialize_task_for_generation(public, task_id)
    for item in hidden.get("tasks", []) if isinstance(hidden, dict) else []:
        if isinstance(item, dict) and item.get("id") == task_id:
            return {"task": public_task, "rubric": dict(item)}
    raise KeyError(task_id)


__all__ = ["validate_task_corpus", "materialize_task_for_generation", "materialize_task_for_judge"]
