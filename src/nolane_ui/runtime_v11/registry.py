"""Rule-registry loading and structural validation for NUI V11."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .contracts import (
    EDIT_FORBIDDEN_CLASSES,
    FINDING_SEVERITIES,
    RULE_CLASSES,
    RULE_ENGINES,
    RULE_TIERS,
)

REGISTRY_RELATIVE_PATH = Path("knowledge/runtime-detector-rules-v11.json")
_REQUIRED_RULE_FIELDS = (
    "rule_id",
    "domain",
    "class",
    "tier",
    "severity",
    "engines",
    "description",
    "falsifier",
    "source_provenance",
)


def _text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate_rule_registry(record: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(record, dict):
        return {"valid": False, "errors": ["runtime rule registry must be an object"], "rule_count": 0}
    if record.get("version") != 11:
        errors.append("runtime rule registry must declare version 11")
    rules_value = record.get("rules")
    if not isinstance(rules_value, list) or not rules_value:
        return {
            "valid": False,
            "errors": errors + ["runtime rule registry requires non-empty rules[]"],
            "rule_count": 0,
        }

    ids: set[str] = set()
    domains: set[str] = set()
    for index, rule in enumerate(rules_value):
        if not isinstance(rule, dict):
            errors.append(f"rule[{index}] must be an object")
            continue
        for field in _REQUIRED_RULE_FIELDS:
            if field not in rule:
                errors.append(f"rule[{index}] requires {field}")

        rule_id = str(rule.get("rule_id", "")).strip()
        if not rule_id:
            errors.append(f"rule[{index}] requires non-empty rule_id")
        elif rule_id in ids:
            errors.append(f"duplicate runtime rule id {rule_id}")
        else:
            ids.add(rule_id)
        if rule_id and not rule_id.startswith("runtime."):
            errors.append(f"runtime rule id must start with runtime.: {rule_id}")

        domain = rule.get("domain")
        if not _text(domain):
            errors.append(f"runtime rule {rule_id or index} requires domain")
        else:
            domains.add(str(domain).strip())

        rule_class = rule.get("class")
        tier = rule.get("tier")
        severity = rule.get("severity")
        if rule_class not in RULE_CLASSES:
            errors.append(f"runtime rule {rule_id or index} has invalid class {rule_class}")
        if tier not in RULE_TIERS:
            errors.append(f"runtime rule {rule_id or index} has invalid tier {tier}")
        if severity not in FINDING_SEVERITIES:
            errors.append(f"runtime rule {rule_id or index} has invalid severity {severity}")
        if rule_class in EDIT_FORBIDDEN_CLASSES and tier == "edit":
            errors.append(f"runtime rule {rule_id or index} class {rule_class} cannot run in edit tier")

        engines = rule.get("engines")
        if not isinstance(engines, list) or not engines:
            errors.append(f"runtime rule {rule_id or index} requires engines[]")
        else:
            invalid_engines = sorted({str(engine) for engine in engines} - RULE_ENGINES)
            if invalid_engines:
                errors.append(f"runtime rule {rule_id or index} has invalid engine(s) {invalid_engines}")
            if len({str(engine) for engine in engines}) != len(engines):
                errors.append(f"runtime rule {rule_id or index} engines must be unique")

        if not _text(rule.get("description")):
            errors.append(f"runtime rule {rule_id or index} requires description")
        if not _text(rule.get("falsifier")):
            errors.append(f"runtime rule {rule_id or index} requires falsifier")

        provenance = rule.get("source_provenance")
        if not isinstance(provenance, dict):
            errors.append(f"runtime rule {rule_id or index} requires source provenance object")
        else:
            if not _text(provenance.get("kind")):
                errors.append(f"runtime rule {rule_id or index} provenance requires kind")
            if provenance.get("implementation") != "independently-authored":
                errors.append(
                    f"runtime rule {rule_id or index} provenance must mark implementation independently-authored"
                )
            if "mechanism_sources" in provenance:
                errors.append(
                    f"runtime rule {rule_id or index} provenance mechanism_sources is legacy; use research_inspiration"
                )
            inspiration = provenance.get("research_inspiration")
            if inspiration is not None and (
                not isinstance(inspiration, list)
                or any(not _text(item) for item in inspiration)
            ):
                errors.append(
                    f"runtime rule {rule_id or index} provenance research_inspiration must be a list of non-empty strings"
                )

        owner_hints = rule.get("owner_hints", [])
        if not isinstance(owner_hints, list) or any(not _text(owner) for owner in owner_hints):
            errors.append(f"runtime rule {rule_id or index} owner_hints must be a list of non-empty strings")

    return {
        "valid": not errors,
        "errors": errors,
        "rule_count": len(ids),
        "domains": sorted(domains),
    }


def load_rule_registry(root: Path | str) -> dict[str, Any]:
    path = Path(root) / REGISTRY_RELATIVE_PATH
    try:
        record = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"runtime rule registry not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"runtime rule registry is invalid JSON: {path}: {exc}") from exc
    result = validate_rule_registry(record)
    if not result["valid"]:
        raise ValueError("invalid runtime rule registry: " + "; ".join(result["errors"]))
    return record


__all__ = ["REGISTRY_RELATIVE_PATH", "load_rule_registry", "validate_rule_registry"]
