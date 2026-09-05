"""Canonical V13 catalog composition and bounded query surface."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from ..reality_catalog_v12 import REALITY_RULES_V12
from .compat_v12 import normalize_v12_rule
from .contracts import validate_catalog_v13
from .provenance import validate_provenance_ledger_v13
from .shards import FIRST_WAVE_RULES_V13, FOUNDATION_RULES_V13, SECOND_WAVE_RULES_V13, THIRD_WAVE_RULES_V13, FOURTH_WAVE_RULES_V13, FIFTH_WAVE_RULES_V13, SIXTH_WAVE_RULES_V13
from .similarity import audit_catalog_similarity

_PROVENANCE_PATHS = (
    Path("knowledge/rule-provenance-v13.json"),
    Path("knowledge/rule-provenance-v13-normative.json"),
    Path("knowledge/rule-provenance-v13-owners.json"),
    Path("knowledge/rule-provenance-v13-wave6-owners.json"),
)


def _resolve_root(root: str | Path | None) -> Path:
    if root is None:
        return Path(__file__).resolve().parents[3]
    return Path(root).resolve()


def load_rule_catalog_v13(root: str | Path | None = None) -> dict[str, Any]:
    repository_root = _resolve_root(root)
    provenance_records: list[dict[str, Any]] = []
    reviewed_at = ""
    for relative_path in _PROVENANCE_PATHS:
        provenance_path = repository_root / relative_path
        if not provenance_path.is_file():
            raise FileNotFoundError(f"V13 provenance ledger shard missing: {provenance_path}")
        shard = json.loads(provenance_path.read_text(encoding="utf-8"))
        if shard.get("version") != 13 or not isinstance(shard.get("records"), list):
            raise ValueError(f"invalid V13 provenance ledger shard: {provenance_path}")
        reviewed_at = max(reviewed_at, str(shard.get("reviewed_at", "")))
        provenance_records.extend(shard["records"])
    provenance = {"version": 13, "reviewed_at": reviewed_at, "records": provenance_records}
    provenance_result = validate_provenance_ledger_v13(provenance)
    if not provenance_result["valid"]:
        raise ValueError(f"invalid V13 provenance ledger: {provenance_result['errors']}")

    rules = [normalize_v12_rule(rule) for rule in REALITY_RULES_V12]
    rules.extend(dict(rule) for rule in FOUNDATION_RULES_V13)
    rules.extend(dict(rule) for rule in FIRST_WAVE_RULES_V13)
    rules.extend(dict(rule) for rule in SECOND_WAVE_RULES_V13)
    rules.extend(dict(rule) for rule in THIRD_WAVE_RULES_V13)
    rules.extend(dict(rule) for rule in FOURTH_WAVE_RULES_V13)
    rules.extend(dict(rule) for rule in FIFTH_WAVE_RULES_V13)
    rules.extend(dict(rule) for rule in SIXTH_WAVE_RULES_V13)
    rules.sort(key=lambda rule: rule["rule_id"])
    catalog = {
        "version": 13,
        "rules": rules,
        "provenance": provenance,
        "composition": {
            "v12_compatibility_rule_count": len(REALITY_RULES_V12),
            "v13_foundation_rule_count": len(FOUNDATION_RULES_V13),
            "v13_first_wave_rule_count": len(FIRST_WAVE_RULES_V13),
            "v13_second_wave_rule_count": len(SECOND_WAVE_RULES_V13),
            "v13_third_wave_rule_count": len(THIRD_WAVE_RULES_V13),
            "v13_fourth_wave_rule_count": len(FOURTH_WAVE_RULES_V13),
            "v13_fifth_wave_rule_count": len(FIFTH_WAVE_RULES_V13),
            "v13_sixth_wave_rule_count": len(SIXTH_WAVE_RULES_V13),
            "rule_count_is_quality_target": False,
        },
    }
    validation = validate_catalog_v13(catalog)
    if not validation["valid"]:
        raise ValueError(f"invalid V13 rule catalog: {validation['errors']}")
    known_provenance = {item["provenance_id"] for item in provenance["records"]}
    missing = sorted({pid for rule in rules for pid in rule["provenance_ids"] if pid not in known_provenance})
    if missing:
        raise ValueError(f"V13 rules reference missing provenance ids: {missing}")
    similarity = audit_catalog_similarity(rules)
    if not similarity["valid"]:
        raise ValueError(f"V13 rule catalog fails anti-duplication court: {similarity}")
    return catalog


def get_rule_v13(rule_id: str, *, root: str | Path | None = None) -> dict[str, Any] | None:
    target = str(rule_id).strip()
    if not target:
        return None
    for rule in load_rule_catalog_v13(root)["rules"]:
        if rule["rule_id"] == target:
            return dict(rule)
    return None


def query_rules_v13(
    *,
    root: str | Path | None = None,
    domain: str | None = None,
    rule_class: str | None = None,
    status: str | None = None,
    text: str | None = None,
    limit: int = 25,
) -> list[dict[str, Any]]:
    if not isinstance(limit, int) or not 1 <= limit <= 100:
        raise ValueError("V13 rule query limit must be between 1 and 100")
    domain_value = str(domain).strip() if domain is not None else None
    class_value = str(rule_class).strip() if rule_class is not None else None
    status_value = str(status).strip() if status is not None else None
    needle = " ".join(str(text).lower().split()) if text is not None else None

    matches: list[dict[str, Any]] = []
    for rule in load_rule_catalog_v13(root)["rules"]:
        if domain_value and rule["domain"] != domain_value:
            continue
        if class_value and rule["class"] != class_value:
            continue
        if status_value and rule["status"] != status_value:
            continue
        if needle:
            haystack = " ".join(
                [rule["rule_id"], rule["title"], rule["statement"], rule["intent"]]
                + rule["failure_modes"]
                + rule["observables"]
                + rule["repairs"]
            ).lower()
            if needle not in " ".join(haystack.split()):
                continue
        matches.append(dict(rule))
        if len(matches) >= limit:
            break
    return matches


def get_rule_provenance_v13(provenance_id: str, *, root: str | Path | None = None) -> dict[str, Any] | None:
    target = str(provenance_id).strip()
    if not target:
        return None
    for record in load_rule_catalog_v13(root)["provenance"]["records"]:
        if record["provenance_id"] == target:
            return dict(record)
    return None


def explain_rule_capabilities_v13(rule_id: str, *, root: str | Path | None = None) -> dict[str, Any]:
    rule = get_rule_v13(rule_id, root=root)
    if rule is None:
        raise ValueError(f"unknown canonical V13 rule: {rule_id}")
    grouped = {"supported": [], "partial": [], "required": [], "unsupported": []}
    for mode, state in rule["capabilities"].items():
        grouped[state.lower()].append(mode)
    for values in grouped.values():
        values.sort()
    return {
        "rule_id": rule["rule_id"],
        "enforcement": rule["enforcement"],
        "supported": grouped["supported"],
        "partial": grouped["partial"],
        "required": grouped["required"],
        "unsupported": grouped["unsupported"],
        "truth_boundary": "Only evidence from available declared capabilities can support a rule finding; unsupported or missing required modes remain UNKNOWN/BLOCKED rather than PASS.",
    }


def rule_catalog_status_v13(root: str | Path | None = None) -> dict[str, Any]:
    catalog = load_rule_catalog_v13(root)
    validation = validate_catalog_v13(catalog)
    similarity = audit_catalog_similarity(catalog["rules"])
    return {
        "valid": validation["valid"] and similarity["valid"],
        "version": 13,
        "rule_count": validation["rule_count"],
        "domain_counts": validation["domain_counts"],
        "class_counts": validation["class_counts"],
        "provenance_record_count": len(catalog["provenance"]["records"]),
        "duplicate_pair_count": similarity["duplicate_pair_count"],
        "boilerplate_cluster_count": similarity["boilerplate_cluster_count"],
        "rule_count_is_quality_target": False,
    }


__all__ = [
    "explain_rule_capabilities_v13", "get_rule_provenance_v13", "get_rule_v13",
    "load_rule_catalog_v13", "query_rules_v13", "rule_catalog_status_v13",
]
