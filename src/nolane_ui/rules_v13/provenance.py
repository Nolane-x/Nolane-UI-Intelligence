"""V13 provenance ledger validation.

Provenance records why NUI considers a rule worth carrying. They never replace
operational rule text and never turn community frequency into normative authority.
"""
from __future__ import annotations

from datetime import date
from typing import Any

EVIDENCE_CLASSES = frozenset({"normative", "reproduced", "corroborated", "emerging", "internal-derived"})
_REQUIRED_FIELDS = (
    "provenance_id", "evidence_class", "source_id", "source_role", "reporter",
    "reviewed_at", "support_role", "contraindications", "transfer_boundary",
)


def _text(value: Any, minimum: int = 1) -> bool:
    return isinstance(value, str) and len(" ".join(value.split())) >= minimum


def _string_list(value: Any, minimum: int = 1) -> bool:
    return isinstance(value, list) and bool(value) and all(_text(item, minimum) for item in value)


def validate_provenance_ledger_v13(record: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(record, dict):
        return {"valid": False, "errors": ["V13 provenance ledger must be an object"], "record_count": 0}
    if record.get("version") != 13:
        errors.append("V13 provenance ledger must declare version 13")
    records = record.get("records")
    if not isinstance(records, list) or not records:
        return {"valid": False, "errors": errors + ["V13 provenance ledger requires non-empty records[]"], "record_count": 0}

    ids: set[str] = set()
    classes: set[str] = set()
    for index, item in enumerate(records):
        if not isinstance(item, dict):
            errors.append(f"provenance[{index}] must be an object")
            continue
        for field in _REQUIRED_FIELDS:
            if field not in item:
                errors.append(f"provenance[{index}] requires {field}")
        pid = str(item.get("provenance_id", "")).strip()
        label = pid or str(index)
        if not pid:
            errors.append(f"provenance[{index}] requires provenance_id")
        elif pid in ids:
            errors.append(f"duplicate V13 provenance id {pid}")
        else:
            ids.add(pid)

        evidence_class = item.get("evidence_class")
        if evidence_class not in EVIDENCE_CLASSES:
            errors.append(f"V13 provenance {label} has invalid evidence_class {evidence_class}")
        else:
            classes.add(str(evidence_class))

        for field, minimum in (("source_id", 2), ("source_role", 4), ("reporter", 6), ("support_role", 32), ("transfer_boundary", 32)):
            if not _text(item.get(field), minimum):
                errors.append(f"V13 provenance {label} {field} is missing or too weak")
        if not _string_list(item.get("contraindications"), 16):
            errors.append(f"V13 provenance {label} requires meaningful contraindications[]")

        reviewed_at = item.get("reviewed_at")
        try:
            if not isinstance(reviewed_at, str):
                raise ValueError
            date.fromisoformat(reviewed_at)
        except ValueError:
            errors.append(f"V13 provenance {label} reviewed_at must be ISO YYYY-MM-DD")

        if evidence_class == "emerging" and "normative" in str(item.get("source_role", "")).lower():
            errors.append(f"V13 provenance {label} emerging evidence cannot claim normative source role")

    return {"valid": not errors, "errors": errors, "record_count": len(ids), "evidence_classes": sorted(classes)}


__all__ = ["EVIDENCE_CLASSES", "validate_provenance_ledger_v13"]
