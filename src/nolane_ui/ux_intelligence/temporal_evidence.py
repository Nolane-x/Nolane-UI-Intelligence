"""Immutable semantic evidence snapshots for UX Intelligence v3."""
from __future__ import annotations

from copy import deepcopy
import hashlib
import json
from typing import Any, Iterable

from .journeys import normalize_ux_journey_spec


_TRANSIENT_KEYS = frozenset({
    "evidence_refs",
    "_evidence_refs",
    "runtime_evidence_refs",
    "capture_ref",
    "timestamp",
    "created_at",
    "observed_at",
    "captured_at",
})
_VERIFICATION_STATUSES = frozenset({"passed", "failed", "insufficient-evidence"})


def _text(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be a non-empty string")
    return value.strip()


def _semantic_normalize(value: Any) -> Any:
    if isinstance(value, dict):
        return {
            str(key): _semantic_normalize(item)
            for key, item in sorted(value.items(), key=lambda pair: str(pair[0]))
            if str(key) not in _TRANSIENT_KEYS
        }
    if isinstance(value, (tuple, list)):
        return [_semantic_normalize(item) for item in value]
    if isinstance(value, set):
        return sorted((_semantic_normalize(item) for item in value), key=lambda item: json.dumps(item, sort_keys=True, ensure_ascii=False))
    return value


def ux_semantic_fingerprint(value: Any) -> str:
    payload = json.dumps(
        _semantic_normalize(value),
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _verification_copy(verification: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(verification, dict):
        raise TypeError("verification must be an object")
    journey_id = _text(verification.get("journey_id"), "verification.journey_id")
    status = verification.get("status")
    if status not in _VERIFICATION_STATUSES:
        raise ValueError(f"{journey_id}: unknown verification status {status!r}")
    out = deepcopy(verification)
    for field in ("step_results", "findings", "evidence_gaps", "success_criteria_results", "provenance_ids"):
        value = out.get(field)
        if not isinstance(value, (tuple, list)):
            raise TypeError(f"verification.{field} must be a sequence")
        out[field] = tuple(value)
    runtime_evidence = out.get("runtime_evidence")
    if runtime_evidence is not None and not isinstance(runtime_evidence, dict):
        raise TypeError("verification.runtime_evidence must be an object or None")
    return out


def create_ux_evidence_snapshot(
    product_id: str,
    revision: str,
    journey: dict[str, Any],
    verification: dict[str, Any],
    *,
    created_from: str,
    provenance_ids: Iterable[str] = (),
) -> dict[str, Any]:
    product = _text(product_id, "product_id")
    rev = _text(revision, "revision")
    source = _text(created_from, "created_from")
    normalized_journey = normalize_ux_journey_spec(journey)
    verified = _verification_copy(verification)
    if verified["journey_id"] != normalized_journey["journey_id"]:
        raise ValueError("verification journey_id must match journey")

    extra_provenance = []
    for index, item in enumerate(tuple(provenance_ids)):
        extra_provenance.append(_text(item, f"provenance_ids[{index}]"))
    inherited = set(normalized_journey["provenance_ids"]) | set(verified["provenance_ids"]) | set(extra_provenance)

    findings = tuple(deepcopy(item) for item in verified["findings"])
    finding_fingerprints = tuple(sorted(ux_semantic_fingerprint(item) for item in findings))
    verification_semantics = {
        "journey_id": verified["journey_id"],
        "status": verified["status"],
        "step_results": verified["step_results"],
        "findings": findings,
        "evidence_gaps": verified["evidence_gaps"],
        "success_criteria_results": verified["success_criteria_results"],
        "runtime_evidence": deepcopy(verified.get("runtime_evidence")),
    }

    snapshot = {
        "version": 3,
        "product_id": product,
        "revision": rev,
        "journey_id": normalized_journey["journey_id"],
        "journey": deepcopy(normalized_journey),
        "journey_fingerprint": ux_semantic_fingerprint(normalized_journey),
        "verification_status": verified["status"],
        "verification": verified,
        "verification_fingerprint": ux_semantic_fingerprint(verification_semantics),
        "finding_fingerprints": finding_fingerprints,
        "created_from": source,
        "provenance_ids": tuple(sorted(inherited)),
    }
    validate_ux_evidence_snapshot(snapshot)
    return snapshot


def validate_ux_evidence_snapshot(snapshot: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(snapshot, dict):
        raise TypeError("UX evidence snapshot must be an object")
    if snapshot.get("version") != 3:
        raise ValueError("UX evidence snapshot must declare version 3")
    product_id = _text(snapshot.get("product_id"), "product_id")
    _text(snapshot.get("revision"), "revision")
    journey_id = _text(snapshot.get("journey_id"), "journey_id")
    _text(snapshot.get("created_from"), "created_from")

    journey = normalize_ux_journey_spec(snapshot.get("journey"))
    if journey["journey_id"] != journey_id:
        raise ValueError("snapshot journey_id does not match stored journey")
    expected_journey_fingerprint = ux_semantic_fingerprint(journey)
    if snapshot.get("journey_fingerprint") != expected_journey_fingerprint:
        raise ValueError("snapshot journey_fingerprint does not match stored journey semantics")

    verification = _verification_copy(snapshot.get("verification"))
    if verification["journey_id"] != journey_id:
        raise ValueError("snapshot verification journey_id does not match journey_id")
    if snapshot.get("verification_status") != verification["status"]:
        raise ValueError("snapshot verification_status does not match verification")

    findings = tuple(verification["findings"])
    expected_findings = tuple(sorted(ux_semantic_fingerprint(item) for item in findings))
    raw_fingerprints = snapshot.get("finding_fingerprints")
    if not isinstance(raw_fingerprints, (tuple, list)) or tuple(raw_fingerprints) != expected_findings:
        raise ValueError("snapshot finding_fingerprints do not match stored findings")

    verification_semantics = {
        "journey_id": verification["journey_id"],
        "status": verification["status"],
        "step_results": verification["step_results"],
        "findings": findings,
        "evidence_gaps": verification["evidence_gaps"],
        "success_criteria_results": verification["success_criteria_results"],
        "runtime_evidence": deepcopy(verification.get("runtime_evidence")),
    }
    if snapshot.get("verification_fingerprint") != ux_semantic_fingerprint(verification_semantics):
        raise ValueError("snapshot verification_fingerprint does not match stored verification semantics")

    provenance = snapshot.get("provenance_ids")
    if not isinstance(provenance, (tuple, list)) or not provenance:
        raise ValueError("snapshot provenance_ids must be a non-empty sequence")
    for index, item in enumerate(provenance):
        _text(item, f"provenance_ids[{index}]")

    return {
        "valid": True,
        "product_id": product_id,
        "journey_id": journey_id,
        "verification_status": verification["status"],
        "finding_count": len(findings),
        "errors": [],
    }


__all__ = [
    "create_ux_evidence_snapshot",
    "ux_semantic_fingerprint",
    "validate_ux_evidence_snapshot",
]
