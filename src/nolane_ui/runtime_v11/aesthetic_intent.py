"""Machine-readable design intent contracts for V11 Phase 4.

This module serializes decisions already owned by NUI cognition. It does not
invent a visual direction and carries no verification or release authority.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any

MODES = {"IDENTITY_LOCKED", "BOUNDED_DEPARTURE", "NEW_DIRECTION", "IMPLEMENTATION_ONLY"}
AMBITIONS = {"UTILITY", "STANDARD", "HIGH", "FLAGSHIP"}
REQUIRED_FIELDS = (
    "intent_id", "revision", "scope", "ambition", "mode", "product_thesis",
    "user_job", "subject_anchors", "identity_invariants", "frozen_axes",
    "flexible_axes", "novelty_budget", "signature_mechanism", "quiet_system",
    "composition_principles", "typography_character", "palette_behavior",
    "surface_material_logic", "media_role", "motion_posture", "anti_references",
    "preserve", "rejection_conditions", "required_owner_outputs",
    "source_evidence_refs",
)
LIST_FIELDS = {
    "scope", "subject_anchors", "identity_invariants", "frozen_axes",
    "flexible_axes", "quiet_system", "composition_principles", "anti_references",
    "preserve", "rejection_conditions", "required_owner_outputs", "source_evidence_refs",
}


def _strings(values: Any, field: str, errors: list[str], *, allow_objects: bool = False) -> None:
    if not isinstance(values, list):
        errors.append(f"{field} must be a list")
        return
    for index, value in enumerate(values):
        if allow_objects and isinstance(value, dict):
            continue
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{field}[{index}] must be a non-empty string")


def validate_aesthetic_intent(packet: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(packet, dict):
        return {"valid": False, "errors": ["intent packet must be an object"]}
    for field in REQUIRED_FIELDS:
        if field not in packet:
            errors.append(f"missing required field: {field}")
    if packet.get("version") != 11:
        errors.append("version must equal 11")
    if packet.get("kind") != "aesthetic-generation-intent":
        errors.append("kind must equal aesthetic-generation-intent")
    if packet.get("claim_boundary") != "generation-intent-only":
        errors.append("claim_boundary must equal generation-intent-only")
    if packet.get("mode") not in MODES:
        errors.append("mode is invalid")
    if packet.get("ambition") not in AMBITIONS:
        errors.append("ambition is invalid")
    for field in LIST_FIELDS:
        if field in packet:
            _strings(packet[field], field, errors, allow_objects=field == "identity_invariants")
    frozen = packet.get("frozen_axes", [])
    flexible = packet.get("flexible_axes", [])
    if isinstance(frozen, list) and isinstance(flexible, list):
        overlap = sorted(set(x for x in frozen if isinstance(x, str)) & set(x for x in flexible if isinstance(x, str)))
        if overlap:
            errors.append("frozen_axes and flexible_axes overlap: " + ", ".join(overlap))
    if packet.get("established_identity") is True and packet.get("mode") == "NEW_DIRECTION" and packet.get("departure_authorized") is not True:
        errors.append("established identity cannot enter NEW_DIRECTION without explicit departure authority")
    return {"valid": not errors, "errors": errors}


def compile_aesthetic_intent(inputs: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(inputs, dict):
        raise ValueError("aesthetic intent inputs must be an object")
    packet = deepcopy(inputs)
    packet["version"] = 11
    packet["kind"] = "aesthetic-generation-intent"
    packet["claim_boundary"] = "generation-intent-only"
    validation = validate_aesthetic_intent(packet)
    if not validation["valid"]:
        raise ValueError("invalid aesthetic intent: " + "; ".join(validation["errors"]))
    return packet


__all__ = ["AMBITIONS", "MODES", "compile_aesthetic_intent", "validate_aesthetic_intent"]
