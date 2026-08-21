"""Context-aware adjudication for deterministic V11 observations."""
from __future__ import annotations

from fnmatch import fnmatch
from typing import Any

from .registry import validate_rule_registry

_DISPOSITIONS = frozenset({"finding", "accepted-exception", "unknown"})


def _text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _validate_exception(record: Any) -> list[str]:
    if not isinstance(record, dict):
        return ["runtime detector exception must be an object"]
    errors: list[str] = []
    for field in ("rule_id", "file", "authority", "reason", "created_revision"):
        if not _text(record.get(field)):
            errors.append(f"runtime detector exception requires {field}")
    file_scope = str(record.get("file", "")).strip()
    if file_scope in {"*", "**", "**/*"}:
        errors.append("runtime detector exception file scope must be narrower than the entire project")
    return errors


def _matching_exception(
    finding: dict[str, Any],
    exceptions: list[dict[str, Any]] | None,
) -> tuple[dict[str, Any] | None, list[str]]:
    if not exceptions:
        return None, []
    runtime = finding.get("runtime", {}) if isinstance(finding, dict) else {}
    rule_id = str(runtime.get("rule_id", ""))
    path = str(runtime.get("path", ""))
    snippet = str(runtime.get("snippet", ""))
    errors: list[str] = []
    for candidate in exceptions:
        candidate_errors = _validate_exception(candidate)
        if candidate_errors:
            if isinstance(candidate, dict) and candidate.get("rule_id") == rule_id:
                errors.extend(candidate_errors)
            continue
        if candidate.get("rule_id") != rule_id:
            continue
        file_scope = str(candidate["file"])
        if not fnmatch(path, file_scope):
            continue
        value = candidate.get("value")
        if value is not None and str(value) not in snippet:
            continue
        return dict(candidate), errors
    return None, errors


def adjudicate_match(
    finding: dict[str, Any],
    rule: dict[str, Any],
    context: dict[str, Any] | None = None,
    exceptions: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    """Adjudicate one observation without silently inventing design intent."""
    if not isinstance(finding, dict):
        raise ValueError("runtime finding must be an object")
    if not isinstance(rule, dict):
        raise ValueError("runtime rule must be an object")
    runtime = finding.get("runtime")
    if not isinstance(runtime, dict):
        raise ValueError("runtime finding requires runtime metadata")
    rule_id = str(rule.get("rule_id", ""))
    if runtime.get("rule_id") != rule_id:
        raise ValueError("runtime finding rule_id does not match adjudication rule")

    exception, exception_errors = _matching_exception(finding, exceptions)
    if exception is not None:
        return {
            "disposition": "accepted-exception",
            "reason": f"Explicit scoped authority accepted {rule_id} for this source location.",
            "finding": finding,
            "exception": exception,
            "exception_errors": exception_errors,
        }

    rule_class = str(rule.get("class", ""))
    context = context if isinstance(context, dict) else {}
    confirmed = context.get("confirmed_violations", [])
    confirmed_ids = {str(item) for item in confirmed} if isinstance(confirmed, list) else set()

    if rule_class == "contextual" and rule_id not in confirmed_ids:
        result = {
            "disposition": "unknown",
            "reason": "Contextual runtime signal needs product/design authority or rendered falsification evidence before it becomes a violation.",
            "finding": finding,
            "exception": None,
            "exception_errors": exception_errors,
        }
    else:
        result = {
            "disposition": "finding",
            "reason": (
                "Context explicitly confirms this contextual violation."
                if rule_class == "contextual"
                else "The rule class permits this deterministic observation to remain an open finding."
            ),
            "finding": finding,
            "exception": None,
            "exception_errors": exception_errors,
        }
    assert result["disposition"] in _DISPOSITIONS
    return result


def adjudicate_findings(
    findings: list[dict[str, Any]],
    registry: dict[str, Any],
    *,
    context: dict[str, Any] | None = None,
    exceptions: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    validation = validate_rule_registry(registry)
    if not validation["valid"]:
        raise ValueError("invalid runtime rule registry: " + "; ".join(validation["errors"]))
    rules = {str(rule["rule_id"]): rule for rule in registry["rules"]}
    buckets: dict[str, list[dict[str, Any]]] = {
        "findings": [],
        "unknowns": [],
        "accepted_exceptions": [],
    }
    exception_errors: list[str] = []
    for finding in findings:
        runtime = finding.get("runtime", {}) if isinstance(finding, dict) else {}
        rule_id = str(runtime.get("rule_id", ""))
        rule = rules.get(rule_id)
        if rule is None:
            raise ValueError(f"runtime finding references unknown registry rule: {rule_id}")
        decision = adjudicate_match(finding, rule, context=context, exceptions=exceptions)
        exception_errors.extend(decision["exception_errors"])
        if decision["disposition"] == "finding":
            buckets["findings"].append(finding)
        elif decision["disposition"] == "unknown":
            buckets["unknowns"].append(decision)
        else:
            buckets["accepted_exceptions"].append(decision)
    return {**buckets, "exception_errors": sorted(set(exception_errors))}


__all__ = ["adjudicate_findings", "adjudicate_match"]
