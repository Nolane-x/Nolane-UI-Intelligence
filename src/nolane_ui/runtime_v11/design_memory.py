"""Project-local aesthetic memory for V11 Phase 4."""
from __future__ import annotations

from copy import deepcopy
from typing import Any


def _mechanism_list(value: Any, field: str, errors: list[str]) -> None:
    if not isinstance(value, list):
        errors.append(f"{field} must be a list")
        return
    for index, item in enumerate(value):
        if not isinstance(item, dict):
            errors.append(f"{field}[{index}] must be an object")
            continue
        if not isinstance(item.get("provenance"), str) or not item["provenance"].strip():
            errors.append(f"{field}[{index}] requires provenance")


def validate_design_memory(memory: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(memory, dict):
        return {"valid": False, "errors": ["design memory must be an object"]}
    if memory.get("memory_version") != 11:
        errors.append("memory_version must equal 11")
    if not isinstance(memory.get("project_identity"), str) or not memory["project_identity"].strip():
        errors.append("project_identity must be non-empty")
    if not isinstance(memory.get("last_verified_revision"), str) or not memory["last_verified_revision"].strip():
        errors.append("last_verified_revision must be non-empty")
    digests = memory.get("source_digests")
    if not isinstance(digests, dict) or not digests:
        errors.append("source_digests must be a non-empty object")
    elif any(not isinstance(path, str) or not path or not isinstance(digest, str) or not digest for path, digest in digests.items()):
        errors.append("source_digests entries must be non-empty strings")
    for field in ("accepted_mechanisms", "rejected_mechanisms", "identity_invariants"):
        _mechanism_list(memory.get(field), field, errors)
    if "global_style" in memory or "house_style" in memory:
        errors.append("design memory must remain project-local and cannot declare a global/house style")
    if memory.get("claim_boundary") != "project-design-memory-only":
        errors.append("claim_boundary must equal project-design-memory-only")
    return {"valid": not errors, "errors": errors}


def build_design_memory(
    *,
    project_identity: str,
    revision: str,
    source_digests: dict[str, str],
    accepted_mechanisms: list[dict[str, Any]],
    rejected_mechanisms: list[dict[str, Any]],
    identity_invariants: list[dict[str, Any]],
) -> dict[str, Any]:
    memory = {
        "memory_version": 11,
        "project_identity": project_identity,
        "accepted_mechanisms": deepcopy(accepted_mechanisms),
        "rejected_mechanisms": deepcopy(rejected_mechanisms),
        "identity_invariants": deepcopy(identity_invariants),
        "visual_tokens_or_refs": [],
        "signature_history": [],
        "preserve_patterns": [],
        "known_genericity_traps": [],
        "source_digests": deepcopy(source_digests),
        "last_verified_revision": revision,
        "claim_boundary": "project-design-memory-only",
    }
    validation = validate_design_memory(memory)
    if not validation["valid"]:
        raise ValueError("invalid design memory: " + "; ".join(validation["errors"]))
    return memory


def assess_design_memory_staleness(memory: dict[str, Any], current_digests: dict[str, str]) -> dict[str, Any]:
    validation = validate_design_memory(memory)
    if not validation["valid"]:
        raise ValueError("invalid design memory: " + "; ".join(validation["errors"]))
    if not isinstance(current_digests, dict):
        raise ValueError("current_digests must be an object")
    changed: list[str] = []
    missing: list[str] = []
    for path, digest in memory["source_digests"].items():
        if path not in current_digests:
            missing.append(path)
        elif current_digests[path] != digest:
            changed.append(path)
    if missing:
        status = "UNKNOWN"
    elif changed:
        status = "STALE"
    else:
        status = "CURRENT"
    return {
        "status": status,
        "changed_paths": sorted(changed),
        "missing_paths": sorted(missing),
        "unrelated_current_paths": sorted(set(current_digests) - set(memory["source_digests"])),
        "claim_boundary": "project-design-memory-only",
    }


__all__ = ["assess_design_memory_staleness", "build_design_memory", "validate_design_memory"]
