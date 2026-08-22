"""NUI v12.1 generation-time external UI reference enforcement.

This module binds V12 reference intelligence to a concrete material UI task.
It does not grant authority or copy upstream work. It ensures reference routing
is explicitly evaluated before generation and remains present through the NUI
lifecycle until verification and provenance are closed.
"""
from __future__ import annotations

from copy import deepcopy
import hashlib
import json
from typing import Any

from .external_ui_intelligence import RECONSULT_STAGES, resolve_reference_pack


FINGERPRINT_FIELDS = (
    "material_ui",
    "task",
    "domain",
    "platform",
    "stack",
    "requirements",
    "roles",
    "user_needs",
    "decision_dimensions",
    "visual_ambition",
    "risk_class",
    "ai_experience",
)

PHASE_STAGE_REQUIREMENTS: dict[str, tuple[str, ...]] = {
    "INTAKE": (),
    "CONTRACTED": (),
    "ROUTED": ("intent",),
    "DISCOVERED": ("intent",),
    "ARCHITECTED": ("intent", "design"),
    "DIVERGED": ("intent", "design"),
    "DESIGN_SELECTED": ("intent", "design"),
    "SYSTEMIZED": ("intent", "design"),
    "SPECIFIED": ("intent", "design"),
    "IMPLEMENTABLE": ("intent", "design", "implementation-selection", "license-gate"),
    "RENDERED": ("intent", "design", "implementation-selection", "license-gate"),
    "CRITIQUED": ("intent", "design", "implementation-selection", "license-gate", "critique"),
    "VERIFIED": (
        "intent", "design", "implementation-selection", "license-gate", "critique", "runtime-verification"
    ),
    "RELEASED": RECONSULT_STAGES,
}


def _canonical(value: Any) -> Any:
    if isinstance(value, dict):
        return {str(key): _canonical(value[key]) for key in sorted(value, key=lambda item: str(item))}
    if isinstance(value, list):
        return [_canonical(item) for item in value]
    if isinstance(value, tuple):
        return [_canonical(item) for item in value]
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    return str(value)


def task_profile_fingerprint(profile: dict[str, Any]) -> str:
    payload = {field: profile.get(field) for field in FINGERPRINT_FIELDS if field in profile}
    encoded = json.dumps(_canonical(payload), ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def _profile_text(profile: dict[str, Any]) -> str:
    parts: list[str] = []

    def visit(value: Any) -> None:
        if isinstance(value, str):
            parts.append(value.lower())
        elif isinstance(value, dict):
            for item in value.values():
                visit(item)
        elif isinstance(value, (list, tuple, set)):
            for item in value:
                visit(item)

    visit(profile)
    return " ".join(parts).replace("_", " ").replace("-", " ")


def _append_unique(target: list[str], values: list[Any]) -> None:
    for value in values:
        item = str(value)
        if item and item not in target:
            target.append(item)


def infer_reference_pack_ids(profile: dict[str, Any], routing: dict[str, Any]) -> list[str]:
    """Infer a bounded set of V12 reference packs from observable task signals."""
    if not isinstance(profile, dict) or not isinstance(routing, dict):
        return []
    if profile.get("material_ui") is not True:
        return []

    policy = routing.get("policy", {}) if isinstance(routing.get("policy"), dict) else {}
    maximum = max(1, int(policy.get("max_active_packs", 8)))
    selected: list[str] = []
    _append_unique(selected, list(policy.get("material_ui_baseline_packs", [])))

    stack_baselines = policy.get("stack_baselines", {})
    stack_baselines = stack_baselines if isinstance(stack_baselines, dict) else {}
    for key in ("stack", "platform"):
        value = str(profile.get(key, "")).strip().lower().replace("_", "-")
        if value:
            _append_unique(selected, list(stack_baselines.get(value, [])))

    text = _profile_text(profile)
    rules = routing.get("rules", []) if isinstance(routing.get("rules"), list) else []
    ranked_rules = sorted(
        (rule for rule in rules if isinstance(rule, dict)),
        key=lambda rule: (-int(rule.get("priority", 0)), str(rule.get("id", ""))),
    )
    for rule in ranked_rules:
        phrases = [str(item).lower().replace("-", " ") for item in rule.get("match_any", [])]
        if phrases and any(phrase in text for phrase in phrases):
            _append_unique(selected, list(rule.get("packs", [])))
        if len(selected) >= maximum:
            break
    return selected[:maximum]


def _compact_pack(packet: dict[str, Any]) -> dict[str, Any]:
    sources = []
    for source in packet.get("sources", []):
        if not isinstance(source, dict):
            continue
        license_data = source.get("license", {}) if isinstance(source.get("license"), dict) else {}
        sources.append({
            "id": source.get("id"),
            "mechanisms": list(source.get("mechanisms", [])),
            "license": {"status": license_data.get("status"), "id": license_data.get("id")},
            "recommendation_mode": source.get("recommendation_mode"),
            "fallbacks": list(source.get("fallbacks", [])),
        })
    gate = packet.get("license_gate", {}) if isinstance(packet.get("license_gate"), dict) else {}
    return {
        "pack_id": packet.get("pack_id"),
        "sources": sources,
        "license_gate": {
            "policy": gate.get("policy"),
            "adoption_candidate": gate.get("adoption_candidate"),
            "requires_user_consent": gate.get("requires_user_consent") is True,
            "consent_sources": list(gate.get("consent_sources", [])),
            "green_fallback": gate.get("green_fallback"),
            "live_verification_required": list(gate.get("live_verification_required", [])),
        },
        "reconsult_at": list(packet.get("reconsult_at", [])),
    }


def compile_reference_execution_contract(
    profile: dict[str, Any],
    network: dict[str, Any],
    packs: dict[str, Any],
    routing: dict[str, Any],
    *,
    stack: str | None = None,
) -> dict[str, Any]:
    """Compile the compact reference context that must survive UI generation."""
    material = profile.get("material_ui") is True
    pack_ids = infer_reference_pack_ids(profile, routing) if material else []
    policy = routing.get("policy", {}) if isinstance(routing.get("policy"), dict) else {}
    per_pack = max(1, int(policy.get("max_sources_per_pack", 3)))
    max_sources = max(1, int(policy.get("max_active_source_ids", 12)))

    resolved: list[dict[str, Any]] = []
    for pack_id in pack_ids:
        packet = resolve_reference_pack(
            pack_id,
            network,
            packs,
            stack=stack or str(profile.get("stack", "")) or None,
            max_sources=per_pack,
        )
        resolved.append(_compact_pack(packet))

    preserve: list[str] = []
    # First preserve every actual adoption candidate so implementation selection
    # cannot silently forget the chosen route.
    for packet in resolved:
        candidate = packet.get("license_gate", {}).get("adoption_candidate")
        if candidate:
            _append_unique(preserve, [candidate])
    # Then preserve the strongest compact research alternatives up to the bound.
    for packet in resolved:
        for source in packet.get("sources", []):
            if len(preserve) >= max_sources:
                break
            if source.get("id"):
                _append_unique(preserve, [source["id"]])
        if len(preserve) >= max_sources:
            break

    consent_ids: list[str] = []
    research_verification_ids: list[str] = []
    for packet in resolved:
        gate = packet.get("license_gate", {})
        if gate.get("requires_user_consent") is True:
            _append_unique(consent_ids, list(gate.get("consent_sources", [])))
        _append_unique(research_verification_ids, list(gate.get("live_verification_required", [])))

    posture = "ACTIVE" if pack_ids else ("EVALUATED_NO_MATCH" if material else "NOT_REQUIRED")
    return {
        "version": 12,
        "contract_type": "external-ui-reference-execution",
        "material_ui": material,
        "posture": posture,
        "routing_evaluated": True,
        "task_fingerprint": task_profile_fingerprint(profile),
        "required_pack_ids": pack_ids,
        "resolved_packs": resolved,
        "must_preserve_source_ids": preserve,
        "license_gate": {
            "policy": "permissive-first",
            "requires_user_consent": bool(consent_ids),
            "consent_source_ids": consent_ids,
            "research_verification_source_ids": research_verification_ids,
        },
        "stage_checkpoints": {},
        "no_match_reason": "no task-shaped V12 pack materially matched after deterministic routing" if material and not pack_ids else "",
    }


def validate_reference_execution_contract(
    contract: dict[str, Any], profile: dict[str, Any], routing: dict[str, Any]
) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(contract, dict):
        return {"valid": False, "errors": ["reference execution contract must be an object"]}
    if contract.get("version") != 12:
        errors.append("reference execution contract requires version 12")
    if contract.get("routing_evaluated") is not True:
        errors.append("material UI reference routing must be explicitly evaluated")
    if contract.get("task_fingerprint") != task_profile_fingerprint(profile):
        errors.append("reference execution task fingerprint does not match current task profile")

    expected = infer_reference_pack_ids(profile, routing) if profile.get("material_ui") is True else []
    declared = [str(item) for item in contract.get("required_pack_ids", [])]
    missing_required = [pack_id for pack_id in expected if pack_id not in declared]
    for pack_id in missing_required:
        errors.append(f"reference execution contract missing inferred required pack {pack_id}")

    resolved = contract.get("resolved_packs")
    if not isinstance(resolved, list):
        resolved = []
        errors.append("reference execution contract requires resolved_packs list")
    resolved_ids = [str(item.get("pack_id")) for item in resolved if isinstance(item, dict) and item.get("pack_id")]
    for pack_id in declared:
        if pack_id not in resolved_ids:
            errors.append(f"reference execution contract required pack {pack_id} is not resolved")
    for pack_id in resolved_ids:
        if pack_id not in declared:
            errors.append(f"reference execution contract contains undeclared resolved pack {pack_id}")

    posture = contract.get("posture")
    if profile.get("material_ui") is True:
        if expected and posture != "ACTIVE":
            errors.append("material UI with inferred references must use ACTIVE posture")
        if not expected and posture != "EVALUATED_NO_MATCH":
            errors.append("material UI without inferred references must use EVALUATED_NO_MATCH posture")
        if posture == "EVALUATED_NO_MATCH" and not str(contract.get("no_match_reason", "")).strip():
            errors.append("EVALUATED_NO_MATCH requires explicit no_match_reason")
    elif posture != "NOT_REQUIRED":
        errors.append("non-material UI reference posture must be NOT_REQUIRED")

    preserve = contract.get("must_preserve_source_ids")
    if not isinstance(preserve, list):
        preserve = []
        errors.append("reference execution contract requires must_preserve_source_ids list")
    if len(preserve) != len(set(map(str, preserve))):
        errors.append("must_preserve_source_ids contains duplicates")
    all_source_ids = {
        str(source.get("id"))
        for packet in resolved if isinstance(packet, dict)
        for source in packet.get("sources", []) if isinstance(source, dict) and source.get("id")
    }
    if posture == "ACTIVE" and not preserve:
        errors.append("ACTIVE reference execution contract requires persistent source ids")
    unknown_preserved = sorted(set(map(str, preserve)) - all_source_ids)
    if unknown_preserved:
        errors.append(f"persistent reference source ids are absent from resolved packets: {unknown_preserved}")

    gate = contract.get("license_gate")
    gate = gate if isinstance(gate, dict) else {}
    consent_ids = gate.get("consent_source_ids", [])
    if not isinstance(consent_ids, list):
        errors.append("license_gate consent_source_ids must be a list")
        consent_ids = []
    if gate.get("requires_user_consent") is not bool(consent_ids):
        errors.append("license_gate requires_user_consent must reflect selected restrictive adoption candidates only")

    return {"valid": not errors, "errors": errors, "expected_pack_ids": expected}


def record_reference_checkpoint(
    contract: dict[str, Any],
    stage: str,
    evidence_ref: str,
    *,
    active_source_ids: list[str] | None = None,
    active_pack_ids: list[str] | None = None,
    consent_evidence: dict[str, Any] | None = None,
    provenance: dict[str, Any] | None = None,
    mutate: bool = False,
) -> dict[str, Any]:
    """Record one lifecycle re-consult without allowing context dropout."""
    checkpoint = {
        "stage": stage,
        "task_fingerprint": contract.get("task_fingerprint"),
        "active_pack_ids": list(active_pack_ids if active_pack_ids is not None else contract.get("required_pack_ids", [])),
        "active_source_ids": list(active_source_ids if active_source_ids is not None else contract.get("must_preserve_source_ids", [])),
        "evidence_ref": evidence_ref,
        "consent_evidence": deepcopy(consent_evidence or {}),
        "provenance": deepcopy(provenance or {}),
    }
    if mutate:
        checkpoints = contract.setdefault("stage_checkpoints", {})
        if isinstance(checkpoints, dict):
            checkpoints[stage] = checkpoint
    return checkpoint


def validate_reference_stage_checkpoint(contract: dict[str, Any], checkpoint: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(checkpoint, dict):
        return {"valid": False, "errors": ["reference checkpoint must be an object"]}
    stage = str(checkpoint.get("stage", ""))
    if stage not in RECONSULT_STAGES:
        errors.append(f"invalid reference checkpoint stage {stage}")
    if checkpoint.get("task_fingerprint") != contract.get("task_fingerprint"):
        errors.append("reference checkpoint task fingerprint drifted from generation contract")
    required_packs = set(map(str, contract.get("required_pack_ids", [])))
    checkpoint_packs = set(map(str, checkpoint.get("active_pack_ids", [])))
    dropped_packs = sorted(required_packs - checkpoint_packs)
    if dropped_packs:
        errors.append(f"reference checkpoint dropped active pack ids {dropped_packs}")
    persistent_sources = set(map(str, contract.get("must_preserve_source_ids", [])))
    checkpoint_sources = set(map(str, checkpoint.get("active_source_ids", [])))
    dropped_sources = sorted(persistent_sources - checkpoint_sources)
    if dropped_sources:
        errors.append(f"reference checkpoint dropped persistent source ids {dropped_sources}")
    if not str(checkpoint.get("evidence_ref", "")).strip():
        errors.append("reference checkpoint requires evidence_ref")

    gate = contract.get("license_gate", {}) if isinstance(contract.get("license_gate"), dict) else {}
    consent_ids = set(map(str, gate.get("consent_source_ids", [])))
    if stage == "license-gate" and consent_ids:
        evidence = checkpoint.get("consent_evidence", {})
        evidence = evidence if isinstance(evidence, dict) else {}
        missing = sorted(source_id for source_id in consent_ids if not evidence.get(source_id))
        if missing:
            errors.append(f"license-gate checkpoint lacks explicit consent evidence for {missing}")

    if stage == "provenance" and persistent_sources:
        provenance = checkpoint.get("provenance", {})
        provenance = provenance if isinstance(provenance, dict) else {}
        missing = sorted(source_id for source_id in persistent_sources if not str(provenance.get(source_id, "")).strip())
        if missing:
            errors.append(f"provenance checkpoint does not account for persistent source ids {missing}")
    return {"valid": not errors, "errors": errors}


def validate_reference_completion(contract: dict[str, Any], phase: str) -> dict[str, Any]:
    """Block NUI phase advancement when mandatory reference re-consults are absent."""
    errors: list[str] = []
    phase = str(phase).upper()
    if phase not in PHASE_STAGE_REQUIREMENTS:
        return {"valid": False, "errors": [f"unknown NUI phase {phase}"], "missing_stages": []}
    if contract.get("material_ui") is not True:
        return {"valid": True, "errors": [], "missing_stages": []}
    if contract.get("routing_evaluated") is not True:
        errors.append("material UI reference execution was not evaluated")
    if contract.get("posture") not in {"ACTIVE", "EVALUATED_NO_MATCH"}:
        errors.append("material UI requires ACTIVE or EVALUATED_NO_MATCH reference posture")

    checkpoints = contract.get("stage_checkpoints", {})
    checkpoints = checkpoints if isinstance(checkpoints, dict) else {}
    required = list(PHASE_STAGE_REQUIREMENTS[phase])
    missing = [stage for stage in required if stage not in checkpoints]
    for stage in missing:
        errors.append(f"phase {phase} missing required reference checkpoint {stage}")
    for stage in required:
        checkpoint = checkpoints.get(stage)
        if checkpoint is None:
            continue
        result = validate_reference_stage_checkpoint(contract, checkpoint)
        errors.extend(f"{stage}: {error}" for error in result["errors"])

    return {"valid": not errors, "errors": errors, "missing_stages": missing, "required_stages": required}


__all__ = [
    "FINGERPRINT_FIELDS",
    "PHASE_STAGE_REQUIREMENTS",
    "task_profile_fingerprint",
    "infer_reference_pack_ids",
    "compile_reference_execution_contract",
    "record_reference_checkpoint",
    "validate_reference_execution_contract",
    "validate_reference_stage_checkpoint",
    "validate_reference_completion",
]
