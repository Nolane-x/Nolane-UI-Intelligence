"""Controlled experiment and run-provenance contracts for NUI V10."""
from __future__ import annotations

import hashlib
import json
from typing import Any

VALID_STATUSES = {"success", "failed", "timeout", "excluded"}
EXCLUSION_REASONS = {"provider-outage", "infrastructure-corruption", "artifact-corruption", "protocol-violation", "duplicate-run"}


def _text(v: Any) -> bool:
    return isinstance(v, str) and bool(v.strip())


def _sha(v: Any) -> bool:
    if not _text(v) or len(str(v)) != 64:
        return False
    try:
        int(str(v), 16)
        return True
    except ValueError:
        return False


def _ids(source: Any, key: str) -> set[str]:
    if isinstance(source, dict) and isinstance(source.get(key), list):
        return {str(x).strip() for x in source[key] if _text(x)}
    return set()


def validate_experiment_manifest(record: dict[str, Any], corpus: dict[str, Any], mutations: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(record, dict) or record.get("version") != 10:
        errors.append("experiment manifest must declare version 10")
        record = record if isinstance(record, dict) else {}
    for field in ("experiment_id", "nui_revision"):
        if not _text(record.get(field)):
            errors.append(f"experiment manifest requires {field}")
    tasks = record.get("tasks")
    if not isinstance(tasks, list) or not tasks:
        errors.append("experiment manifest requires tasks")
        tasks = []
    known_tasks = _ids(corpus, "task_ids")
    if known_tasks:
        unknown = {str(x) for x in tasks} - known_tasks
        if unknown:
            errors.append(f"experiment references unknown tasks: {sorted(unknown)}")
    models = record.get("models")
    if not isinstance(models, list) or not models:
        errors.append("experiment manifest requires models")
        models = []
    for i, model in enumerate(models):
        if not isinstance(model, dict):
            errors.append(f"model[{i}] must be an object")
            continue
        # A model name alone is not reproducible evidence. Provider and runtime
        # are part of the experimental identity because the same nominal model
        # can behave differently across serving stacks and execution harnesses.
        for field in ("family", "name", "snapshot", "provider", "runtime"):
            if not _text(model.get(field)):
                errors.append(f"model[{i}] requires {field}")
    treatments = record.get("treatments")
    if not isinstance(treatments, list) or not treatments:
        errors.append("experiment manifest requires treatments")
        treatments = []
    treatment_set = {str(x) for x in treatments}
    if "baseline" not in treatment_set:
        errors.append("experiment requires matched baseline treatment")
    if "nui_full" not in treatment_set:
        errors.append("experiment requires nui_full treatment")
    known_ablations = _ids(mutations, "ablation_ids")
    ablation_treatments = {x.split(":", 1)[1] for x in treatment_set if x.startswith("nui_ablation:") and ":" in x}
    if known_ablations and not ablation_treatments:
        errors.append("experiment requires at least one targeted ablation treatment")
    unknown_ablations = ablation_treatments - known_ablations
    if known_ablations and unknown_ablations:
        errors.append(f"experiment references unknown ablations: {sorted(unknown_ablations)}")
    known_mutations = _ids(mutations, "mutation_ids")
    mutation_treatments = {x.split(":", 1)[1] for x in treatment_set if x.startswith("nui_mutation:") and ":" in x}
    unknown_mutations = mutation_treatments - known_mutations
    if known_mutations and unknown_mutations:
        errors.append(f"experiment references unknown mutations: {sorted(unknown_mutations)}")
    if not isinstance(record.get("replicates"), int) or int(record.get("replicates", 0)) < 1:
        errors.append("experiment replicates must be a positive integer")
    if not isinstance(record.get("tool_budget"), dict) or not record.get("tool_budget"):
        errors.append("experiment requires explicit tool_budget")
    return {"valid": not errors, "errors": errors, "treatments": sorted(treatment_set), "task_count": len(tasks), "model_count": len(models)}


def validate_run_record(record: dict[str, Any], manifest: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(record, dict):
        return {"valid": False, "errors": ["run record must be an object"]}
    for field in ("run_id", "experiment_id", "task_id", "treatment", "provider", "model_family", "model_name", "model_snapshot", "runtime", "nui_revision"):
        if not _text(record.get(field)):
            errors.append(f"run record requires {field}")
    if _text(manifest.get("experiment_id")) and record.get("experiment_id") != manifest.get("experiment_id"):
        errors.append("run experiment_id does not match manifest")
    if _text(manifest.get("nui_revision")) and record.get("nui_revision") != manifest.get("nui_revision"):
        errors.append("run nui_revision does not match manifest")
    status = record.get("status")
    if status not in VALID_STATUSES:
        errors.append(f"run status must be one of {sorted(VALID_STATUSES)}")
    if status == "excluded" and record.get("exclusion_reason") not in EXCLUSION_REASONS:
        errors.append(f"excluded run requires exclusion_reason in {sorted(EXCLUSION_REASONS)}")
    if status != "excluded" and record.get("exclusion_reason") is not None:
        errors.append("non-excluded run cannot carry exclusion_reason")
    if not isinstance(record.get("seed"), int):
        errors.append("run requires integer seed")
    if not isinstance(record.get("temperature"), (int, float)):
        errors.append("run requires numeric temperature")
    for field in ("prompt_sha256", "context_sha256", "tool_budget_hash"):
        if not _sha(record.get(field)):
            errors.append(f"run requires 64-hex {field}")
    digests = record.get("artifact_digests")
    if not isinstance(digests, list):
        errors.append("run artifact_digests must be a list")
        digests = []
    for digest in digests:
        if not _sha(digest):
            errors.append("artifact digests must be 64-hex SHA-256 values")
    if status == "success" and not digests:
        errors.append("successful run requires at least one artifact digest")
    for optional_numeric in ("input_tokens", "output_tokens", "cost_usd", "wall_time_seconds"):
        if optional_numeric in record and not isinstance(record.get(optional_numeric), (int, float)):
            errors.append(f"{optional_numeric} must be numeric when present")
    return {"valid": not errors, "errors": errors, "pairing_key": pairing_key(record) if not errors else None}


def pairing_key(run: dict[str, Any]) -> tuple[Any, ...]:
    return (
        run.get("experiment_id"), run.get("task_id"), run.get("model_family"), run.get("model_name"),
        run.get("model_snapshot"), run.get("runtime"), run.get("seed"), run.get("temperature"), run.get("tool_budget_hash"),
    )


def stable_hash_jsonish(value: Any) -> str:
    """Hash JSON-like data canonically rather than by Python insertion order."""
    payload = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


__all__ = ["validate_experiment_manifest", "validate_run_record", "pairing_key", "stable_hash_jsonish", "EXCLUSION_REASONS"]
