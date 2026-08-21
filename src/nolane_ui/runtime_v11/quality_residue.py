"""Bounded quality-residue loop for V11 Phase 4."""
from __future__ import annotations

from copy import deepcopy
from typing import Any


def plan_quality_residue_pass(
    *,
    findings: list[dict[str, Any]],
    pass_index: int,
    max_passes: int,
    preserve: list[str] | None = None,
) -> dict[str, Any]:
    if not isinstance(findings, list):
        raise ValueError("findings must be a list")
    if not isinstance(pass_index, int) or pass_index < 0:
        raise ValueError("pass_index must be a non-negative integer")
    if not isinstance(max_passes, int) or max_passes < 1:
        raise ValueError("max_passes must be positive")
    thesis_failures = [item for item in findings if isinstance(item, dict) and item.get("kind") == "thesis"]
    if thesis_failures:
        decision = "RE_DIVERGE"
        reason = "thesis-level failure is outside bounded residue repair authority"
    elif findings and pass_index >= max_passes:
        decision = "RE_DIVERGE"
        reason = "quality residue pass budget exhausted with open findings"
    elif findings:
        decision = "REPAIR"
        reason = "bounded causal residue findings remain"
    else:
        decision = "CLEAN"
        reason = "no quality residue finding remains in this scope"
    repairable = [] if decision == "RE_DIVERGE" else deepcopy(findings)
    return {
        "decision": decision,
        "reason": reason,
        "pass_index": pass_index,
        "max_passes": max_passes,
        "repairable_findings": repairable,
        "preserve": deepcopy(preserve or []),
        "claim_boundary": "quality-residue-only",
    }


def assess_quality_residue_closure(*, resolved: int, persisted: int, unknown: int, regressions: int) -> dict[str, Any]:
    counts = {"resolved": resolved, "persisted": persisted, "unknown": unknown, "regressions": regressions}
    if any(not isinstance(value, int) or value < 0 for value in counts.values()):
        raise ValueError("quality residue counts must be non-negative integers")
    if unknown:
        status = "UNKNOWN"
    elif persisted or regressions:
        status = "OPEN"
    else:
        status = "CLEAN"
    return {
        "status": status,
        **counts,
        "claim_boundary": "quality-residue-only",
    }


__all__ = ["assess_quality_residue_closure", "plan_quality_residue_pass"]
