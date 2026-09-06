"""Validation, lookup, and deterministic read APIs for UX Intelligence v1."""

from __future__ import annotations

from collections import Counter
from copy import deepcopy
from typing import Any, Iterable

from .mechanisms import UX_MECHANISMS
from .rules import UX_RULES
from .skills import UX_SKILLS


VERSION = 1
UX_DOMAINS = {
    "goal-task",
    "mental-model",
    "information-architecture",
    "journey-flow",
    "cognitive-friction",
    "comprehension",
    "recovery",
    "evaluation",
}
RULE_DOMAINS = UX_DOMAINS | {"convergence"}
RULE_CLASSES = {"behavioral", "structural", "contextual", "convergence"}
SEVERITIES = {"critical", "major", "moderate", "observation"}
ENFORCEMENTS = {"block", "warn", "review"}
STATUSES = {"active", "deprecated", "experimental"}
NON_BLOCKING_CLASSES = {"contextual", "convergence"}
FORBIDDEN_QUOTA_FIELDS = {
    "minimum_rule_count",
    "target_rule_count",
    "rule_quota",
    "minimum_skill_count",
    "target_skill_count",
    "skill_quota",
}
OPERATIONAL_PLANES = (
    "applies_when",
    "failure_modes",
    "user_impacts",
    "observables",
    "falsifiers",
    "repairs",
    "verification",
)


def _require_non_empty_string(record: dict[str, Any], field: str, owner: str) -> None:
    value = record.get(field)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{owner}: {field} must be a non-empty string")


def _require_non_empty_text_tuple(record: dict[str, Any], field: str, owner: str) -> None:
    value = record.get(field)
    if not isinstance(value, tuple) or not value:
        raise ValueError(f"{owner}: {field} must be a non-empty tuple")
    if not all(isinstance(item, str) and item.strip() for item in value):
        raise ValueError(f"{owner}: {field} must contain only non-empty strings")


def _reject_quota_fields(record: dict[str, Any], owner: str) -> None:
    forbidden = set(record) & FORBIDDEN_QUOTA_FIELDS
    if forbidden:
        raise ValueError(f"{owner}: count quotas are forbidden: {sorted(forbidden)}")


def _unique_ids(records: Iterable[dict[str, Any]], field: str, label: str) -> set[str]:
    identifiers = [record.get(field) for record in records]
    if any(not isinstance(item, str) or not item.strip() for item in identifiers):
        raise ValueError(f"{label}: every {field} must be a non-empty string")
    if len(identifiers) != len(set(identifiers)):
        raise ValueError(f"{label}: duplicate {field} detected")
    return set(identifiers)


def _normalize_signature_text(value: str) -> str:
    return " ".join(value.casefold().split())


def _operational_signature(rule: dict[str, Any]) -> tuple[tuple[str, ...], tuple[str, ...], tuple[str, ...]]:
    return (
        tuple(_normalize_signature_text(item) for item in rule["failure_modes"]),
        tuple(_normalize_signature_text(item) for item in rule["repairs"]),
        tuple(_normalize_signature_text(item) for item in rule["verification"]),
    )


def _validate_mechanisms() -> set[str]:
    mechanism_ids = _unique_ids(UX_MECHANISMS, "mechanism_id", "UX mechanisms")
    for mechanism in UX_MECHANISMS:
        owner = mechanism["mechanism_id"]
        _reject_quota_fields(mechanism, owner)
        for field in ("title", "definition", "diagnostic_question"):
            _require_non_empty_string(mechanism, field, owner)
        for field in ("signals", "non_examples"):
            _require_non_empty_text_tuple(mechanism, field, owner)
    if [item["mechanism_id"] for item in UX_MECHANISMS] != sorted(mechanism_ids):
        raise ValueError("UX mechanisms must be canonically sorted by mechanism_id")
    return mechanism_ids


def _validate_skills(mechanism_ids: set[str]) -> set[str]:
    skill_ids = _unique_ids(UX_SKILLS, "skill_id", "UX skills")
    for skill in UX_SKILLS:
        owner = skill["skill_id"]
        _reject_quota_fields(skill, owner)
        if skill.get("domain") not in UX_DOMAINS:
            raise ValueError(f"{owner}: unknown UX domain {skill.get('domain')!r}")
        for field in ("title", "purpose"):
            _require_non_empty_string(skill, field, owner)
        for field in ("questions", "outputs", "anti_patterns", "related_mechanisms"):
            _require_non_empty_text_tuple(skill, field, owner)
        unknown = set(skill["related_mechanisms"]) - mechanism_ids
        if unknown:
            raise ValueError(f"{owner}: unknown related mechanisms {sorted(unknown)}")
    if [item["skill_id"] for item in UX_SKILLS] != sorted(skill_ids):
        raise ValueError("UX skills must be canonically sorted by skill_id")
    return skill_ids


def _validate_rules(mechanism_ids: set[str], skill_ids: set[str]) -> set[str]:
    rule_ids = _unique_ids(UX_RULES, "rule_id", "UX rules")
    skill_mechanisms = {
        skill["skill_id"]: set(skill["related_mechanisms"])
        for skill in UX_SKILLS
    }
    seen_signatures: dict[tuple[tuple[str, ...], tuple[str, ...], tuple[str, ...]], str] = {}
    for rule in UX_RULES:
        owner = rule["rule_id"]
        _reject_quota_fields(rule, owner)
        if rule.get("domain") not in RULE_DOMAINS:
            raise ValueError(f"{owner}: unknown rule domain {rule.get('domain')!r}")
        if rule.get("mechanism_id") not in mechanism_ids:
            raise ValueError(f"{owner}: unknown mechanism {rule.get('mechanism_id')!r}")
        if rule.get("class") not in RULE_CLASSES:
            raise ValueError(f"{owner}: unknown rule class {rule.get('class')!r}")
        if rule.get("severity") not in SEVERITIES:
            raise ValueError(f"{owner}: unknown severity {rule.get('severity')!r}")
        if rule.get("enforcement") not in ENFORCEMENTS:
            raise ValueError(f"{owner}: unknown enforcement {rule.get('enforcement')!r}")
        if rule.get("status") not in STATUSES:
            raise ValueError(f"{owner}: unknown status {rule.get('status')!r}")
        if rule["class"] in NON_BLOCKING_CLASSES and rule["enforcement"] == "block":
            raise ValueError(f"{owner}: {rule['class']} rules must not block")
        if rule["severity"] == "observation" and rule["enforcement"] == "block":
            raise ValueError(f"{owner}: observation rules must not block")
        for field in ("title", "statement"):
            _require_non_empty_string(rule, field, owner)
        for field in OPERATIONAL_PLANES + ("owner_skill_ids",):
            _require_non_empty_text_tuple(rule, field, owner)
        unknown_owners = set(rule["owner_skill_ids"]) - skill_ids
        if unknown_owners:
            raise ValueError(f"{owner}: unknown owner skills {sorted(unknown_owners)}")
        if not any(
            rule["mechanism_id"] in skill_mechanisms[skill_id]
            for skill_id in rule["owner_skill_ids"]
        ):
            raise ValueError(f"{owner}: rule requires at least one mechanism-compatible owner skill")
        signature = _operational_signature(rule)
        if signature in seen_signatures:
            raise ValueError(
                f"{owner}: duplicate operational signature with {seen_signatures[signature]}"
            )
        seen_signatures[signature] = owner
    if [item["rule_id"] for item in UX_RULES] != sorted(rule_ids):
        raise ValueError("UX rules must be canonically sorted by rule_id")
    return rule_ids


def _validate_catalogs() -> None:
    mechanism_ids = _validate_mechanisms()
    skill_ids = _validate_skills(mechanism_ids)
    _validate_rules(mechanism_ids, skill_ids)


_validate_catalogs()

_MECHANISM_INDEX = {item["mechanism_id"]: item for item in UX_MECHANISMS}
_SKILL_INDEX = {item["skill_id"]: item for item in UX_SKILLS}
_RULE_INDEX = {item["rule_id"]: item for item in UX_RULES}


def _validate_limit(limit: int) -> int:
    if isinstance(limit, bool) or not isinstance(limit, int):
        raise TypeError("limit must be an integer")
    if not 1 <= limit <= 100:
        raise ValueError("limit must be between 1 and 100")
    return limit


def _text_matches(record: dict[str, Any], text: str | None) -> bool:
    if text is None:
        return True
    if not isinstance(text, str):
        raise TypeError("text must be a string or None")
    needle = text.strip().casefold()
    if not needle:
        return True

    def flatten(value: Any) -> Iterable[str]:
        if isinstance(value, str):
            yield value
        elif isinstance(value, (tuple, list, set)):
            for item in value:
                yield from flatten(item)
        elif isinstance(value, dict):
            for item in value.values():
                yield from flatten(item)

    haystack = " ".join(flatten(record)).casefold()
    return needle in haystack


def get_ux_mechanism(mechanism_id: str) -> dict[str, Any] | None:
    record = _MECHANISM_INDEX.get(mechanism_id)
    return deepcopy(record) if record is not None else None


def get_ux_skill(skill_id: str) -> dict[str, Any] | None:
    record = _SKILL_INDEX.get(skill_id)
    return deepcopy(record) if record is not None else None


def get_ux_rule(rule_id: str) -> dict[str, Any] | None:
    record = _RULE_INDEX.get(rule_id)
    return deepcopy(record) if record is not None else None


def query_ux_mechanisms(*, text: str | None = None, limit: int = 20) -> list[dict[str, Any]]:
    _validate_limit(limit)
    records = [item for item in UX_MECHANISMS if _text_matches(item, text)]
    return deepcopy(records[:limit])


def query_ux_skills(*, domain: str | None = None, mechanism_id: str | None = None,
                    text: str | None = None, limit: int = 20) -> list[dict[str, Any]]:
    _validate_limit(limit)
    records = [
        item for item in UX_SKILLS
        if (domain is None or item["domain"] == domain)
        and (mechanism_id is None or mechanism_id in item["related_mechanisms"])
        and _text_matches(item, text)
    ]
    return deepcopy(records[:limit])


def query_ux_rules(*, domain: str | None = None, mechanism_id: str | None = None,
                   rule_class: str | None = None, status: str | None = None,
                   text: str | None = None, limit: int = 20) -> list[dict[str, Any]]:
    _validate_limit(limit)
    records = [
        item for item in UX_RULES
        if (domain is None or item["domain"] == domain)
        and (mechanism_id is None or item["mechanism_id"] == mechanism_id)
        and (rule_class is None or item["class"] == rule_class)
        and (status is None or item["status"] == status)
        and _text_matches(item, text)
    ]
    return deepcopy(records[:limit])


def ux_intelligence_status() -> dict[str, Any]:
    skill_domains = Counter(item["domain"] for item in UX_SKILLS)
    rule_classes = Counter(item["class"] for item in UX_RULES)
    rule_mechanisms = Counter(item["mechanism_id"] for item in UX_RULES)
    skill_mechanisms = Counter(
        mechanism_id
        for skill in UX_SKILLS
        for mechanism_id in skill["related_mechanisms"]
    )
    referenced = set(rule_mechanisms) | set(skill_mechanisms)
    orphan_mechanisms = sorted(set(_MECHANISM_INDEX) - referenced)
    return {
        "valid": True,
        "version": VERSION,
        "mechanism_count": len(UX_MECHANISMS),
        "skill_count": len(UX_SKILLS),
        "rule_count": len(UX_RULES),
        "domain_counts": dict(sorted(skill_domains.items())),
        "rule_class_counts": dict(sorted(rule_classes.items())),
        "mechanism_coverage": {
            mechanism_id: {
                "skill_count": skill_mechanisms.get(mechanism_id, 0),
                "rule_count": rule_mechanisms.get(mechanism_id, 0),
            }
            for mechanism_id in sorted(_MECHANISM_INDEX)
        },
        "orphan_mechanisms": orphan_mechanisms,
        "rule_count_is_quality_target": False,
        "skill_count_is_quality_target": False,
    }


__all__ = [
    "get_ux_mechanism",
    "get_ux_rule",
    "get_ux_skill",
    "query_ux_mechanisms",
    "query_ux_rules",
    "query_ux_skills",
    "ux_intelligence_status",
]
