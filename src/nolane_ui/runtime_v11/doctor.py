"""Maintenance diagnostics for NUI V11 runtime design intelligence.

Doctor reports installation/schema/evidence/capability drift. It never infers
product/design truth from repository churn and it never mutates as a side effect.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

from .evidence import assess_evidence_staleness, validate_evidence_binding
from .registry import load_rule_registry

_REQUIRED_ARTIFACTS = (
    "scripts/nui-detect",
    "knowledge/runtime-detector-rules-v11.json",
    "schemas/runtime-browser-observation-v11.schema.json",
    "schemas/runtime-evidence-binding-v11.schema.json",
    "src/nolane_ui/runtime_v11/contracts.py",
    "src/nolane_ui/runtime_v11/registry.py",
    "src/nolane_ui/runtime_v11/detector.py",
    "src/nolane_ui/runtime_v11/adjudication.py",
    "src/nolane_ui/runtime_v11/browser.py",
    "src/nolane_ui/runtime_v11/hooks.py",
)


def _finding(
    finding_id: str,
    category: str,
    severity: str,
    action: str,
    summary: str,
    details: dict[str, Any] | None = None,
) -> dict[str, Any]:
    return {
        "id": finding_id,
        "category": category,
        "severity": severity,
        "action": action,
        "summary": summary,
        "details": details or {},
    }


def diagnose_runtime_state(
    root: Path | str,
    *,
    evidence_bindings: list[dict[str, Any]] | None = None,
    current_digests: dict[str, str] | None = None,
    required_capabilities: list[str] | None = None,
    available_capabilities: list[str] | None = None,
    commit_count: int | None = None,
) -> dict[str, Any]:
    root_path = Path(root)
    findings: list[dict[str, Any]] = []

    missing_artifacts = [path for path in _REQUIRED_ARTIFACTS if not (root_path / path).exists()]
    if missing_artifacts:
        findings.append(_finding(
            "runtime-installation.missing-artifact",
            "schema-projection",
            "blocking",
            "route",
            "Canonical V11 runtime artifacts are missing; runtime claims cannot be trusted until the installation is repaired.",
            {"missing": missing_artifacts},
        ))
    else:
        try:
            registry = load_rule_registry(root_path)
            findings.append(_finding(
                "runtime-installation.registry-valid",
                "schema-projection",
                "info",
                "mention",
                "V11 runtime detector registry is structurally valid.",
                {"rule_count": len(registry["rules"])},
            ))
        except ValueError as exc:
            findings.append(_finding(
                "runtime-installation.registry-invalid",
                "schema-projection",
                "blocking",
                "route",
                "V11 runtime detector registry is unreadable or structurally invalid.",
                {"error": str(exc)},
            ))

    bindings = evidence_bindings or []
    digests = current_digests or {}
    for index, binding in enumerate(bindings):
        validation = validate_evidence_binding(binding)
        if not validation["valid"]:
            findings.append(_finding(
                "runtime-evidence.binding-invalid",
                "evidence",
                "blocking",
                "route",
                "A runtime evidence binding is malformed and cannot support a release-relevant claim.",
                {"index": index, "errors": validation["errors"]},
            ))
            continue
        status = assess_evidence_staleness(binding, digests)
        if status["status"] == "STALE":
            findings.append(_finding(
                "runtime-evidence.stale",
                "evidence",
                "blocking",
                "route",
                "Evidence overlaps changed source and must be re-observed before it can support the same claim.",
                status,
            ))
        elif status["status"] == "UNKNOWN":
            findings.append(_finding(
                "runtime-evidence.current-state-unknown",
                "evidence",
                "blocking",
                "route",
                "Current source evidence is incomplete; the binding cannot be treated as current.",
                status,
            ))

    required = {str(item).strip() for item in (required_capabilities or []) if str(item).strip()}
    available = {str(item).strip() for item in (available_capabilities or []) if str(item).strip()}
    missing_caps = sorted(required - available)
    if missing_caps:
        findings.append(_finding(
            "runtime-capability.missing",
            "capability",
            "blocking",
            "route",
            "Required runtime evidence capabilities are unavailable; affected evidence remains UNKNOWN/BLOCKED.",
            {"required": sorted(required), "available": sorted(available), "missing": missing_caps},
        ))

    blocking = [item for item in findings if item["severity"] == "blocking"]
    return {
        "valid": not blocking,
        "root": root_path.as_posix(),
        "findings": findings,
        "blocking_count": len(blocking),
        "commit_count_note": "informational-only" if commit_count is not None else "not-supplied",
        "truth_drift_policy": "Repository churn or commit count alone never proves PRODUCT/DESIGN truth drift.",
        "mutation_policy": "Doctor is read-only; repairs require an explicit follow-up command/owner.",
    }


__all__ = ["diagnose_runtime_state"]
