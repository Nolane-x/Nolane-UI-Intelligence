"""Deterministic closure comparison for bounded runtime re-observation.

This module answers a narrow question: did the same observed runtime finding
persist after repair, disappear under adequate observation, or become
unjudgeable because the observation capability was incomplete? It does not
produce NUI release authority.
"""
from __future__ import annotations

from collections import defaultdict, deque
from typing import Any


def _runtime_scope(finding: dict[str, Any]) -> tuple[str, str, str, str]:
    if not isinstance(finding, dict):
        raise ValueError("runtime finding must be an object")
    finding_id = finding.get("finding_id")
    if not isinstance(finding_id, str) or not finding_id.strip():
        raise ValueError("runtime finding requires finding_id")
    runtime = finding.get("runtime")
    if not isinstance(runtime, dict):
        raise ValueError(f"runtime finding {finding_id} requires runtime object")
    rule_id = runtime.get("rule_id")
    if not isinstance(rule_id, str) or not rule_id.strip():
        raise ValueError(f"runtime finding {finding_id} requires runtime.rule_id")

    source = runtime.get("path")
    if source is None:
        source = runtime.get("url")
    source_text = str(source).strip() if source is not None else ""

    line = runtime.get("line")
    line_text = str(line) if line is not None else ""
    locator = runtime.get("locator")
    locator_text = str(locator).strip() if locator is not None else ""
    return rule_id.strip(), source_text, line_text, locator_text


def _finding_id(finding: dict[str, Any]) -> str:
    value = finding.get("finding_id")
    if not isinstance(value, str) or not value.strip():
        raise ValueError("runtime finding requires finding_id")
    return value.strip()


def _scope_record(scope: tuple[str, str, str, str]) -> dict[str, Any]:
    rule_id, source, line, locator = scope
    record: dict[str, Any] = {"rule_id": rule_id}
    if source:
        record["source"] = source
    if line:
        try:
            record["line"] = int(line)
        except ValueError:
            record["line"] = line
    if locator:
        record["locator"] = locator
    return record


def _normalize_capabilities_by_rule(value: dict[str, bool] | None) -> dict[str, bool]:
    if value is None:
        return {}
    if not isinstance(value, dict):
        raise ValueError("capabilities_by_rule must be an object when supplied")
    normalized: dict[str, bool] = {}
    for rule_id, complete in value.items():
        if not isinstance(rule_id, str) or not rule_id.strip():
            raise ValueError("capabilities_by_rule keys must be non-empty rule IDs")
        if not isinstance(complete, bool):
            raise ValueError("capabilities_by_rule values must be boolean")
        normalized[rule_id.strip()] = complete
    return dict(sorted(normalized.items()))


def compare_runtime_observations(
    before_findings: list[dict[str, Any]],
    after_findings: list[dict[str, Any]],
    *,
    capabilities_complete: bool = True,
    capabilities_by_rule: dict[str, bool] | None = None,
) -> dict[str, Any]:
    """Compare two bounded runtime observations without self-certifying release.

    Findings are matched as a multiset by rule + source + line + locator. An
    unmatched prior finding may be called RESOLVED only when observation is
    complete for that rule. ``capabilities_by_rule`` refines the legacy global
    boolean while preserving the previous behavior for callers that omit it.
    """
    if not isinstance(before_findings, list) or not isinstance(after_findings, list):
        raise ValueError("before_findings and after_findings must be lists")
    if not isinstance(capabilities_complete, bool):
        raise ValueError("capabilities_complete must be boolean")
    scoped_capabilities = _normalize_capabilities_by_rule(capabilities_by_rule)

    before = sorted(before_findings, key=lambda item: (_finding_id(item), _runtime_scope(item)))
    after = sorted(after_findings, key=lambda item: (_finding_id(item), _runtime_scope(item)))

    after_buckets: dict[tuple[str, str, str, str], deque[dict[str, Any]]] = defaultdict(deque)
    for item in after:
        after_buckets[_runtime_scope(item)].append(item)

    closures: list[dict[str, Any]] = []
    for prior in before:
        scope = _runtime_scope(prior)
        prior_id = _finding_id(prior)
        rule_id = scope[0]
        bucket = after_buckets.get(scope)
        if bucket:
            matched = bucket.popleft()
            closures.append(
                {
                    "finding_id": prior_id,
                    "status": "PERSISTED",
                    "scope": _scope_record(scope),
                    "matched_finding_id": _finding_id(matched),
                }
            )
        else:
            capability_complete = scoped_capabilities.get(rule_id, capabilities_complete)
            closures.append(
                {
                    "finding_id": prior_id,
                    "status": "RESOLVED" if capability_complete else "UNKNOWN",
                    "scope": _scope_record(scope),
                    "matched_finding_id": None,
                }
            )

    regressions: list[dict[str, Any]] = []
    for scope in sorted(after_buckets):
        bucket = after_buckets[scope]
        while bucket:
            item = bucket.popleft()
            regressions.append(
                {
                    "finding_id": _finding_id(item),
                    "scope": _scope_record(scope),
                }
            )
    regressions.sort(key=lambda item: (item["finding_id"], str(item["scope"])))

    counts = {
        "resolved": sum(item["status"] == "RESOLVED" for item in closures),
        "persisted": sum(item["status"] == "PERSISTED" for item in closures),
        "unknown": sum(item["status"] == "UNKNOWN" for item in closures),
        "regression": len(regressions),
    }
    if counts["unknown"]:
        decision = "UNKNOWN"
    elif counts["persisted"] or counts["regression"]:
        decision = "OPEN"
    else:
        decision = "CLEAN"

    return {
        "closures": closures,
        "regressions": regressions,
        "counts": counts,
        "decision": decision,
        "capabilities_complete": capabilities_complete,
        "capabilities_by_rule": scoped_capabilities,
        "claim_boundary": "runtime-closure-only",
    }


__all__ = ["compare_runtime_observations"]
