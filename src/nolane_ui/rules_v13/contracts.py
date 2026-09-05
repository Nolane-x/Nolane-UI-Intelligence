"""V13 canonical rule contracts for Nolane UI Intelligence.

The validator is intentionally dependency-free and treats rule count as descriptive.
Operational strength, authority coherence, falsifiability, and capability honesty are
validated before a rule can enter the canonical catalog.
"""
from __future__ import annotations

from collections import Counter
from typing import Any

RULE_CLASSES = frozenset({"mechanical", "behavioral", "contextual", "advisory", "aesthetic", "convergence"})
RULE_SEVERITIES = frozenset({"critical", "major", "moderate", "minor", "observation"})
RULE_ENFORCEMENTS = frozenset({"block", "warn", "review"})
NON_BLOCKING_CLASSES = frozenset({"advisory", "aesthetic", "convergence"})
CAPABILITY_MODES = (
    "static", "dom", "computed-style", "browser-runtime", "interaction",
    "accessibility-tree", "visual-render", "semantic-product", "cross-generation", "human-review",
)
CAPABILITY_STATES = frozenset({"SUPPORTED", "PARTIAL", "REQUIRED", "UNSUPPORTED"})
RULE_STATUSES = frozenset({"active", "rising", "fading", "mostly-fixed", "emerging", "deprecated", "retired"})

_REQUIRED_FIELDS = (
    "rule_id", "domain", "class", "severity", "enforcement", "title", "statement", "intent",
    "applies_when", "does_not_apply_when", "failure_modes", "user_impacts", "observables",
    "falsifiers", "repairs", "exceptions", "verification", "owner_hints", "verifier_hints",
    "capabilities", "provenance_ids", "status",
)
_TEXT_MINIMUMS = {"title": 18, "statement": 56, "intent": 48}
_LIST_MINIMUMS = {
    "applies_when": 28,
    "does_not_apply_when": 20,
    "failure_modes": 28,
    "user_impacts": 24,
    "observables": 24,
    "falsifiers": 24,
    "repairs": 28,
    "exceptions": 16,
    "verification": 28,
}
_OPTIONALLY_EMPTY_LISTS = frozenset({"does_not_apply_when", "exceptions", "verifier_hints"})


def _text(value: Any, minimum: int = 1) -> bool:
    return isinstance(value, str) and len(" ".join(value.split())) >= minimum


def _string_list(value: Any, *, minimum: int = 1, allow_empty: bool = False) -> bool:
    return (
        isinstance(value, list)
        and (allow_empty or bool(value))
        and all(_text(item, minimum) for item in value)
    )


def validate_rule_v13(rule: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(rule, dict):
        return {"valid": False, "errors": ["V13 rule must be an object"]}

    for field in _REQUIRED_FIELDS:
        if field not in rule:
            errors.append(f"V13 rule requires {field}")

    rule_id = str(rule.get("rule_id", "")).strip()
    if not rule_id or not rule_id.startswith("ui.") or len(rule_id.split(".")) < 3:
        errors.append("V13 rule_id must use ui.<domain>.<name> form")

    domain = str(rule.get("domain", "")).strip()
    if not domain:
        errors.append("V13 rule requires non-empty domain")
    elif rule_id.startswith("ui.") and len(rule_id.split(".")) >= 3 and domain != rule_id.split(".")[1]:
        errors.append(f"V13 rule {rule_id} domain must match rule_id domain segment")

    rule_class = rule.get("class")
    severity = rule.get("severity")
    enforcement = rule.get("enforcement")
    if rule_class not in RULE_CLASSES:
        errors.append(f"V13 rule {rule_id or '<unknown>'} has invalid class {rule_class}")
    if severity not in RULE_SEVERITIES:
        errors.append(f"V13 rule {rule_id or '<unknown>'} has invalid severity {severity}")
    if enforcement not in RULE_ENFORCEMENTS:
        errors.append(f"V13 rule {rule_id or '<unknown>'} has invalid enforcement {enforcement}")
    if rule_class in NON_BLOCKING_CLASSES and enforcement == "block":
        errors.append(f"V13 rule {rule_id or '<unknown>'} class {rule_class} cannot block")
    if enforcement == "block" and severity in {"minor", "observation"}:
        errors.append(f"V13 rule {rule_id or '<unknown>'} cannot block at severity {severity}")

    for field, minimum in _TEXT_MINIMUMS.items():
        if not _text(rule.get(field), minimum):
            errors.append(f"V13 rule {rule_id or '<unknown>'} {field} must contain operational prose of at least {minimum} characters")

    for field, minimum in _LIST_MINIMUMS.items():
        if not _string_list(rule.get(field), minimum=minimum, allow_empty=field in _OPTIONALLY_EMPTY_LISTS):
            errors.append(f"V13 rule {rule_id or '<unknown>'} {field} must be a {'possibly empty ' if field in _OPTIONALLY_EMPTY_LISTS else ''}list of operational strings")

    for field in ("owner_hints", "verifier_hints", "provenance_ids"):
        if not _string_list(rule.get(field), allow_empty=field in _OPTIONALLY_EMPTY_LISTS):
            errors.append(f"V13 rule {rule_id or '<unknown>'} {field} must be a list of non-empty strings")

    capabilities = rule.get("capabilities")
    if not isinstance(capabilities, dict):
        errors.append(f"V13 rule {rule_id or '<unknown>'} capabilities must be an object")
    else:
        missing = [mode for mode in CAPABILITY_MODES if mode not in capabilities]
        extra = sorted(set(capabilities) - set(CAPABILITY_MODES))
        if missing:
            errors.append(f"V13 rule {rule_id or '<unknown>'} capabilities missing modes {missing}")
        if extra:
            errors.append(f"V13 rule {rule_id or '<unknown>'} capabilities contain unknown modes {extra}")
        for mode in CAPABILITY_MODES:
            state = capabilities.get(mode)
            if state not in CAPABILITY_STATES:
                errors.append(f"V13 rule {rule_id or '<unknown>'} capability {mode} has invalid state {state}")

    status = rule.get("status")
    if status not in RULE_STATUSES:
        errors.append(f"V13 rule {rule_id or '<unknown>'} has invalid status {status}")

    for relation in ("distinct_from", "supersedes", "complements", "conflicts_with"):
        if relation in rule and not _string_list(rule.get(relation), allow_empty=True):
            errors.append(f"V13 rule {rule_id or '<unknown>'} {relation} must be a list of rule ids")

    return {"valid": not errors, "errors": errors, "rule_id": rule_id}


def validate_catalog_v13(record: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(record, dict):
        return {"valid": False, "errors": ["V13 rule catalog must be an object"], "rule_count": 0}
    if record.get("version") != 13:
        errors.append("V13 rule catalog must declare version 13")
    quota_fields = sorted(key for key in record if key in {"minimum_rule_count", "required_rule_count", "rule_quota", "minimum_rules_per_shard"})
    if quota_fields:
        errors.append(f"V13 rule catalog forbids rule-count quota fields: {quota_fields}")
    rules = record.get("rules")
    if not isinstance(rules, list) or not rules:
        return {"valid": False, "errors": errors + ["V13 rule catalog requires non-empty rules[]"], "rule_count": 0}

    ids: list[str] = []
    class_counts: Counter[str] = Counter()
    domain_counts: Counter[str] = Counter()
    for index, rule in enumerate(rules):
        result = validate_rule_v13(rule)
        errors.extend(f"rule[{index}]: {error}" for error in result["errors"])
        rid = result.get("rule_id")
        if rid:
            ids.append(rid)
        if isinstance(rule, dict):
            if rule.get("class") in RULE_CLASSES:
                class_counts[str(rule["class"])] += 1
            if isinstance(rule.get("domain"), str) and rule["domain"].strip():
                domain_counts[rule["domain"].strip()] += 1

    duplicates = sorted(rid for rid, count in Counter(ids).items() if count > 1)
    if duplicates:
        errors.append(f"V13 rule catalog contains duplicate rule ids: {duplicates}")

    return {
        "valid": not errors,
        "errors": errors,
        "rule_count": len(ids),
        "domains": sorted(domain_counts),
        "domain_counts": dict(sorted(domain_counts.items())),
        "class_counts": dict(sorted(class_counts.items())),
    }


__all__ = [
    "CAPABILITY_MODES", "CAPABILITY_STATES", "NON_BLOCKING_CLASSES", "RULE_CLASSES",
    "RULE_ENFORCEMENTS", "RULE_SEVERITIES", "RULE_STATUSES", "validate_catalog_v13", "validate_rule_v13",
]
