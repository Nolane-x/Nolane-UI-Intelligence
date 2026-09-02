"""Reality-grounded UI rule catalog for NUI V12.

The catalog is intentionally broader than the V11 runtime detector registry.
A reality rule may require browser observation, interaction testing, product
context, or human review; it must not pretend a text heuristic can prove more
than it actually observes.

External provenance is optional. Operational truth is not: every rule must say
when it applies, what concrete failure it prevents, what can be observed, how to
repair it, what exceptions exist, and how the repair is verified.
"""
from __future__ import annotations

import copy
from collections import Counter
from pathlib import Path
from typing import Any

from .reality_catalog_v12 import REALITY_RULE_CATALOG_V12

CATALOG_RELATIVE_PATH = Path("src/nolane_ui/reality_catalog_v12.py")
RULE_CLASSES = frozenset({"mechanical", "behavioral", "contextual", "advisory", "aesthetic"})
RULE_SEVERITIES = frozenset({"critical", "major", "moderate", "minor", "observation"})
RULE_ENFORCEMENTS = frozenset({"block", "warn", "review"})
NON_BLOCKING_CLASSES = frozenset({"advisory", "aesthetic"})
_REQUIRED_FIELDS = (
    "rule_id",
    "domain",
    "class",
    "severity",
    "enforcement",
    "title",
    "statement",
    "applies_when",
    "failure_mode",
    "observables",
    "repair",
    "exceptions",
    "verification",
)


def _text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _string_list(value: Any, *, allow_empty: bool = False) -> bool:
    return (
        isinstance(value, list)
        and (allow_empty or bool(value))
        and all(_text(item) for item in value)
    )


def validate_reality_rule_catalog(record: dict[str, Any]) -> dict[str, Any]:
    """Validate the V12 rule contract without requiring external citations."""
    errors: list[str] = []
    if not isinstance(record, dict):
        return {"valid": False, "errors": ["reality rule catalog must be an object"], "rule_count": 0, "domains": []}
    if record.get("version") != 12:
        errors.append("reality rule catalog must declare version 12")
    rules = record.get("rules")
    if not isinstance(rules, list) or not rules:
        return {"valid": False, "errors": errors + ["reality rule catalog requires non-empty rules[]"], "rule_count": 0, "domains": []}

    ids: set[str] = set()
    domains: set[str] = set()
    class_counts: Counter[str] = Counter()
    enforcement_counts: Counter[str] = Counter()

    for index, rule in enumerate(rules):
        if not isinstance(rule, dict):
            errors.append(f"rule[{index}] must be an object")
            continue
        for field in _REQUIRED_FIELDS:
            if field not in rule:
                errors.append(f"rule[{index}] requires {field}")

        rule_id = str(rule.get("rule_id", "")).strip()
        label = rule_id or str(index)
        if not rule_id:
            errors.append(f"rule[{index}] requires non-empty rule_id")
        elif not rule_id.startswith("ui."):
            errors.append(f"reality rule id must start with ui.: {rule_id}")
        elif rule_id in ids:
            errors.append(f"duplicate reality rule id {rule_id}")
        else:
            ids.add(rule_id)

        domain = rule.get("domain")
        if not _text(domain):
            errors.append(f"reality rule {label} requires domain")
        else:
            domains.add(str(domain).strip())

        rule_class = rule.get("class")
        severity = rule.get("severity")
        enforcement = rule.get("enforcement")
        if rule_class not in RULE_CLASSES:
            errors.append(f"reality rule {label} has invalid class {rule_class}")
        else:
            class_counts[str(rule_class)] += 1
        if severity not in RULE_SEVERITIES:
            errors.append(f"reality rule {label} has invalid severity {severity}")
        if enforcement not in RULE_ENFORCEMENTS:
            errors.append(f"reality rule {label} has invalid enforcement {enforcement}")
        else:
            enforcement_counts[str(enforcement)] += 1
        if rule_class in NON_BLOCKING_CLASSES and enforcement == "block":
            errors.append(f"reality rule {label} class {rule_class} cannot block delivery")
        if enforcement == "block" and severity in {"minor", "observation"}:
            errors.append(f"reality rule {label} cannot block at severity {severity}")

        for field in ("title", "statement", "applies_when", "failure_mode"):
            if not _text(rule.get(field)):
                errors.append(f"reality rule {label} requires non-empty {field}")
        for field in ("observables", "repair", "verification"):
            if not _string_list(rule.get(field)):
                errors.append(f"reality rule {label} requires non-empty {field}[]")
        if not _string_list(rule.get("exceptions"), allow_empty=True):
            errors.append(f"reality rule {label} exceptions must be a string list")

        provenance = rule.get("source_provenance")
        if provenance is not None:
            if not isinstance(provenance, dict):
                errors.append(f"reality rule {label} source_provenance must be an object when provided")
            else:
                kind = provenance.get("kind")
                if kind is not None and not _text(kind):
                    errors.append(f"reality rule {label} provenance kind must be non-empty when provided")
                refs = provenance.get("references")
                if refs is not None and not _string_list(refs):
                    errors.append(f"reality rule {label} provenance references must be non-empty strings when provided")

    return {
        "valid": not errors,
        "errors": errors,
        "rule_count": len(ids),
        "domains": sorted(domains),
        "class_counts": dict(sorted(class_counts.items())),
        "enforcement_counts": dict(sorted(enforcement_counts.items())),
    }


def load_reality_rule_catalog(root: Path | str) -> dict[str, Any]:
    """Return a validated defensive copy of the built-in V12 reality catalog."""
    # Keep root in the API so callers can use the same repository-root calling
    # convention as other NUI loaders. The V12 catalog is Python data rather
    # than an enormous JSON blob so it stays reviewable and typed beside code.
    Path(root)
    record = copy.deepcopy(REALITY_RULE_CATALOG_V12)
    result = validate_reality_rule_catalog(record)
    if not result["valid"]:
        raise ValueError("invalid built-in reality rule catalog: " + "; ".join(result["errors"]))
    return record


__all__ = [
    "CATALOG_RELATIVE_PATH",
    "NON_BLOCKING_CLASSES",
    "RULE_CLASSES",
    "RULE_ENFORCEMENTS",
    "RULE_SEVERITIES",
    "load_reality_rule_catalog",
    "validate_reality_rule_catalog",
]
