"""Semantic UX regression comparison for v3 evidence snapshots."""
from __future__ import annotations

from copy import deepcopy
from typing import Any, Iterable

from .temporal_evidence import ux_semantic_fingerprint, validate_ux_evidence_snapshot
from .v3_catalog import UX_RULE_REGRESSION_CLASSES


def _validated(snapshot: dict[str, Any]) -> dict[str, Any]:
    validate_ux_evidence_snapshot(snapshot)
    return deepcopy(snapshot)


def _finding_map(snapshot: dict[str, Any]) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for finding in snapshot["verification"]["findings"]:
        fingerprint = ux_semantic_fingerprint(finding)
        result.setdefault(fingerprint, deepcopy(finding))
    return result


def _history_fingerprints(
    history: Iterable[dict[str, Any]],
    *,
    product_id: str,
    journey_id: str,
) -> set[str]:
    seen: set[str] = set()
    for index, raw in enumerate(tuple(history)):
        snapshot = _validated(raw)
        if snapshot["product_id"] != product_id or snapshot["journey_id"] != journey_id:
            raise ValueError(f"history[{index}] snapshot identity differs from comparison identity")
        seen.update(_finding_map(snapshot))
    return seen


def compare_ux_snapshots(
    baseline: dict[str, Any],
    candidate: dict[str, Any],
    *,
    history: Iterable[dict[str, Any]] = (),
) -> dict[str, Any]:
    """Compare same-product/same-journey snapshots without increasing finding authority."""
    before = _validated(baseline)
    after = _validated(candidate)
    if before["product_id"] != after["product_id"]:
        raise ValueError("snapshot products differ")
    if before["journey_id"] != after["journey_id"]:
        raise ValueError("snapshot journeys differ")

    historical = _history_fingerprints(
        history,
        product_id=before["product_id"],
        journey_id=before["journey_id"],
    )
    baseline_findings = _finding_map(before)
    candidate_findings = _finding_map(after)
    regressions: list[dict[str, Any]] = []

    if before["verification_status"] == "passed" and after["verification_status"] == "insufficient-evidence":
        regressions.append({
            "class": "journey-pass-to-insufficient-evidence",
            "rule_id": None,
            "finding_id": None,
            "finding_fingerprint": None,
            "severity": None,
            "enforcement": None,
            "proven_failure": False,
            "baseline_status": "passed",
            "candidate_status": "insufficient-evidence",
            "because": "previously passing journey no longer has sufficient evidence; this is not proof of UX failure",
        })

    for fingerprint in sorted(set(candidate_findings) - set(baseline_findings)):
        finding = candidate_findings[fingerprint]
        rule_id = finding.get("rule_id")
        regression_class = (
            "reintroduced-rule-finding"
            if fingerprint in historical
            else UX_RULE_REGRESSION_CLASSES.get(rule_id, "new-rule-finding")
        )
        regressions.append({
            "class": regression_class,
            "rule_id": rule_id,
            "finding_id": finding.get("finding_id"),
            "finding_fingerprint": fingerprint,
            "severity": finding.get("severity"),
            "enforcement": finding.get("enforcement"),
            "proven_failure": True,
            "baseline_status": before["verification_status"],
            "candidate_status": after["verification_status"],
            "because": "candidate contains a v2-derived finding absent from the immediate baseline",
        })

    regressions.sort(key=lambda item: (
        0 if item["proven_failure"] else 1,
        item["class"],
        item.get("rule_id") or "",
        item.get("finding_fingerprint") or "",
    ))
    if any(item["proven_failure"] for item in regressions):
        status = "regressed"
    elif regressions:
        status = "insufficient-evidence"
    else:
        status = "no-regression"

    return {
        "product_id": before["product_id"],
        "journey_id": before["journey_id"],
        "baseline_revision": before["revision"],
        "candidate_revision": after["revision"],
        "status": status,
        "regressions": tuple(regressions),
        "baseline_verification_status": before["verification_status"],
        "candidate_verification_status": after["verification_status"],
    }


__all__ = ["compare_ux_snapshots"]
