"""Treatment-blind judging and contamination controls for NUI V10."""
from __future__ import annotations

import hashlib
from typing import Any

_ALLOWED_JUDGE_FIELDS = {"task_id", "artifact_refs", "output_text", "render_refs", "interaction_trace", "runtime_observations"}


def _text(v: Any) -> bool:
    return isinstance(v, str) and bool(v.strip())


def blind_run_for_judge(run: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(run, dict):
        raise TypeError("run must be an object")
    raw_id = str(run.get("run_id", ""))
    blind_id = hashlib.sha256(raw_id.encode("utf-8")).hexdigest()[:20]
    payload = {"blind_id": blind_id}
    for key in _ALLOWED_JUDGE_FIELDS:
        if key in run:
            payload[key] = run[key]
    return payload


def pair_orientation(experiment_id: str, task_id: str, replicate: int) -> tuple[str, str]:
    material = f"{experiment_id}\0{task_id}\0{replicate}".encode("utf-8")
    bit = hashlib.sha256(material).digest()[0] & 1
    return ("LEFT", "RIGHT") if bit == 0 else ("RIGHT", "LEFT")


def detect_leakage(text: str, hidden_task: dict[str, Any]) -> list[str]:
    haystack = str(text).casefold()
    hits: list[str] = []
    phrases = hidden_task.get("leakage_sensitive_phrases", []) if isinstance(hidden_task, dict) else []
    if not isinstance(phrases, list):
        return []
    for phrase in phrases:
        if _text(phrase) and str(phrase).casefold() in haystack:
            hits.append(str(phrase))
    return hits


def validate_judgment(record: dict[str, Any], hidden_task: dict[str, Any], run_index: dict[str, dict[str, Any]]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(record, dict):
        return {"valid": False, "errors": ["judgment must be an object"]}
    verdict = record.get("verdict")
    if verdict not in {"LEFT", "RIGHT", "TIE", "UNJUDGABLE"}:
        errors.append("judgment verdict must be LEFT, RIGHT, TIE or UNJUDGABLE")
    if not isinstance(record.get("confidence"), (int, float)) or not 0 <= float(record.get("confidence", -1)) <= 1:
        errors.append("judgment confidence must be within 0..1")
    pair = record.get("blind_pair")
    if not isinstance(pair, list) or len(pair) != 2 or any(not _text(x) for x in pair):
        errors.append("judgment requires two blind pair ids")
    evidence = record.get("dimension_evidence")
    required_dimensions = hidden_task.get("judge_dimensions", []) if isinstance(hidden_task, dict) else []
    if not isinstance(evidence, list):
        errors.append("judgment requires dimension_evidence")
        evidence = []
    seen_dims = set()
    for i, item in enumerate(evidence):
        if not isinstance(item, dict):
            errors.append(f"dimension_evidence[{i}] must be an object")
            continue
        dimension = item.get("dimension")
        if not _text(dimension):
            errors.append(f"dimension_evidence[{i}] requires dimension")
        else:
            seen_dims.add(str(dimension))
        refs = item.get("evidence_refs")
        if not isinstance(refs, list) or not refs or any(not _text(x) for x in refs):
            errors.append(f"dimension_evidence[{i}] requires raw evidence_refs")
        if not _text(item.get("observation")):
            errors.append(f"dimension_evidence[{i}] requires observation")
    missing = {str(x) for x in required_dimensions} - seen_dims
    if missing:
        errors.append(f"judgment missing required dimensions: {sorted(missing)}")
    treatment_words = ("nui_full", "nui_ablation", "nui_mutation", "baseline")
    serialized = repr(record).lower()
    if any(word in serialized for word in treatment_words):
        errors.append("judgment payload leaks treatment identity")
    return {"valid": not errors, "errors": errors, "dimensions": sorted(seen_dims)}


__all__ = ["blind_run_for_judge", "pair_orientation", "detect_leakage", "validate_judgment"]
