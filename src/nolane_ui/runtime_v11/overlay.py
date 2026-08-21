"""Evidence-only live overlay view models for NUI V11 Phase 5."""
from __future__ import annotations

import copy
from typing import Any

_ALLOWED_FIELDS = frozenset({
    "version", "rendered_identity", "source_attribution_status", "selected_source",
    "preview_id", "preview_state", "capture_refs", "runtime_finding_ids",
    "capability_gaps", "reobservation", "claim_boundary",
})
_ATTRIBUTION_STATES = frozenset({"EXACT", "CANDIDATE", "AMBIGUOUS", "UNKNOWN"})
_PREVIEW_STATES = frozenset({"PREPARED", "INJECTED", "OBSERVED", "STALE", "CONFLICT", "REJECTED", "ACCEPTED"})


def _text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _strings(value: Any) -> bool:
    return isinstance(value, list) and all(_text(item) for item in value)


def validate_overlay_packet(record: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(record, dict):
        return {"valid": False, "errors": ["live overlay packet must be an object"]}
    extra = sorted(set(record) - _ALLOWED_FIELDS)
    if extra:
        errors.append("live overlay packet has unsupported fields: " + ", ".join(extra))
    if record.get("version") != 11:
        errors.append("live overlay packet must declare version 11")
    identity = record.get("rendered_identity")
    if not isinstance(identity, dict) or not _text(identity.get("locator")):
        errors.append("live overlay packet requires rendered_identity.locator")
    if record.get("source_attribution_status") not in _ATTRIBUTION_STATES:
        errors.append("live overlay source_attribution_status is invalid")
    selected = record.get("selected_source")
    if selected is not None and not isinstance(selected, dict):
        errors.append("live overlay selected_source must be null or object")
    preview_id = record.get("preview_id")
    if preview_id is not None and not _text(preview_id):
        errors.append("live overlay preview_id must be null or string")
    preview_state = record.get("preview_state")
    if preview_state is not None and preview_state not in _PREVIEW_STATES:
        errors.append("live overlay preview_state is invalid")
    if not _strings(record.get("capture_refs")):
        errors.append("live overlay capture_refs must be a list of strings")
    if not _strings(record.get("runtime_finding_ids")):
        errors.append("live overlay runtime_finding_ids must be a list of strings")
    if not _strings(record.get("capability_gaps")):
        errors.append("live overlay capability_gaps must be a list of strings")
    reobservation = record.get("reobservation")
    if reobservation is not None and not isinstance(reobservation, dict):
        errors.append("live overlay reobservation must be null or object")
    if record.get("claim_boundary") != "overlay-evidence-only":
        errors.append("live overlay claim_boundary must be overlay-evidence-only")
    if record.get("source_attribution_status") in {"UNKNOWN", "AMBIGUOUS", "CANDIDATE"} and selected is not None:
        errors.append("non-EXACT source attribution cannot be displayed as selected source")
    return {"valid": not errors, "errors": errors}


def build_overlay_packet(
    *,
    rendered_identity: dict[str, Any],
    attribution: dict[str, Any],
    preview: dict[str, Any] | None = None,
    runtime_findings: list[dict[str, Any]] | None = None,
    capability_gaps: list[str] | None = None,
    reobservation: dict[str, Any] | None = None,
) -> dict[str, Any]:
    if not isinstance(rendered_identity, dict) or not _text(rendered_identity.get("locator")):
        raise ValueError("overlay rendered_identity requires locator")
    if not isinstance(attribution, dict) or attribution.get("status") not in _ATTRIBUTION_STATES:
        raise ValueError("overlay requires a valid source attribution status")
    findings = runtime_findings or []
    if not isinstance(findings, list):
        raise TypeError("runtime_findings must be a list")
    finding_ids: list[str] = []
    for finding in findings:
        if not isinstance(finding, dict) or not _text(finding.get("finding_id")):
            raise ValueError("runtime findings must expose finding_id")
        finding_ids.append(str(finding["finding_id"]).strip())
    gaps = list(capability_gaps or [])
    if not _strings(gaps):
        raise ValueError("capability_gaps must contain non-empty strings")

    selected_source = None
    if attribution.get("status") == "EXACT" and _text(attribution.get("selected_candidate_id")):
        matches = [item for item in attribution.get("candidates", []) if isinstance(item, dict) and item.get("candidate_id") == attribution["selected_candidate_id"]]
        if len(matches) == 1:
            selected_source = {
                "candidate_id": matches[0].get("candidate_id"),
                "source_path": matches[0].get("source_path"),
                "source_digest": matches[0].get("source_digest"),
                "range": copy.deepcopy(matches[0].get("range")),
            }

    packet = {
        "version": 11,
        "rendered_identity": copy.deepcopy(rendered_identity),
        "source_attribution_status": attribution["status"],
        "selected_source": selected_source,
        "preview_id": preview.get("preview_id") if isinstance(preview, dict) else None,
        "preview_state": preview.get("state") if isinstance(preview, dict) else None,
        "capture_refs": list(preview.get("capture_refs", [])) if isinstance(preview, dict) else [],
        "runtime_finding_ids": sorted(set(finding_ids)),
        "capability_gaps": sorted(set(gaps)),
        "reobservation": copy.deepcopy(reobservation) if isinstance(reobservation, dict) else None,
        "claim_boundary": "overlay-evidence-only",
    }
    validation = validate_overlay_packet(packet)
    if not validation["valid"]:
        raise AssertionError("internal live overlay packet invalid: " + "; ".join(validation["errors"]))
    return packet


__all__ = ["build_overlay_packet", "validate_overlay_packet"]
