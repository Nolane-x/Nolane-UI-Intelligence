"""Bounded provenance records for UX Intelligence v2.

These records describe why a verifier expectation may be used and where that
basis stops transferring.  They are not universal UX laws and do not elevate UX
findings into V13 canonical-rule authority.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any, Iterable


SOURCE_KINDS = {
    "internal-empirical",
    "runtime-observation",
    "standards",
    "research",
    "product-contract",
    "expert-review",
}
STATUSES = {"active", "deprecated", "experimental"}
FORBIDDEN_QUOTA_FIELDS = {
    "minimum_rule_count",
    "target_rule_count",
    "rule_quota",
    "minimum_skill_count",
    "target_skill_count",
    "skill_quota",
}


UX_PROVENANCE = tuple(sorted((
    {
        "provenance_id": "uxp.product-journey-contract",
        "title": "Declared product journey contract",
        "source_kind": "product-contract",
        "source_reference": "UXJourneySpec supplied by the product/task owner",
        "claim": "Explicitly declared journey transitions, preserved context and success criteria may be evaluated as product-local expectations for that journey.",
        "supports": ("journey-transition-expectation", "context-preservation-expectation", "success-criteria-evaluation"),
        "transfer_boundaries": ("Applies only to the supplied product/task journey and does not establish a universal UX requirement for unrelated products.",),
        "contraindications": ("Do not treat an underspecified or stale journey declaration as proof that observed behavior is defective; revalidate the product contract first.",),
        "verification_modes": ("product-contract", "interaction"),
        "status": "active",
    },
    {
        "provenance_id": "uxp.rule-authority-inheritance",
        "title": "UX rule authority inheritance contract",
        "source_kind": "product-contract",
        "source_reference": "src/nolane_ui/ux_intelligence/rules.py",
        "claim": "A runtime UX finding may inherit mechanism, severity and enforcement only from the explicit UX rule it proves.",
        "supports": ("finding-authority-inheritance", "deterministic-rule-evaluation"),
        "transfer_boundaries": ("This inheritance is limited to the UX Intelligence rule catalog and does not confer V13 canonical-rule authority.",),
        "contraindications": ("Do not synthesize a new severity or enforcement level from evaluator confidence, wording, or missing evidence.",),
        "verification_modes": ("product-contract", "runtime-observation"),
        "status": "active",
    },
    {
        "provenance_id": "uxp.v11-runtime-observation",
        "title": "V11 provider-neutral runtime observation boundary",
        "source_kind": "runtime-observation",
        "source_reference": "src/nolane_ui/runtime_v11",
        "claim": "Provider-neutral browser/runtime observations can evidence rendered state, interaction outcome, context markers and completion signals without requiring Playwright-specific objects at the UX boundary.",
        "supports": ("runtime-state-evidence", "interaction-outcome-evidence", "completion-evidence", "recovery-affordance-evidence"),
        "transfer_boundaries": ("Runtime observation can prove observable interface state but cannot by itself prove user comprehension, preference, intent or causal usability improvement.",),
        "contraindications": ("Do not infer a UX failure when the observation packet lacks a field required to falsify the applicable expectation.",),
        "verification_modes": ("runtime-observation", "interaction"),
        "status": "active",
    },
), key=lambda item: item["provenance_id"]))


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
    parts: list[str] = []
    for value in record.values():
        if isinstance(value, str):
            parts.append(value)
        elif isinstance(value, (tuple, list)):
            parts.extend(str(item) for item in value)
    return needle in " ".join(parts).casefold()


def validate_ux_provenance(records: Iterable[dict[str, Any]]) -> dict[str, Any]:
    records = list(records)
    seen: set[str] = set()
    for index, record in enumerate(records):
        if not isinstance(record, dict):
            raise TypeError(f"UX provenance record {index} must be an object")
        provenance_id = record.get("provenance_id")
        if not isinstance(provenance_id, str) or not provenance_id.strip():
            raise ValueError(f"UX provenance record {index}: provenance_id must be non-empty")
        if provenance_id in seen:
            raise ValueError(f"UX provenance: duplicate provenance_id {provenance_id}")
        seen.add(provenance_id)
        forbidden = set(record) & FORBIDDEN_QUOTA_FIELDS
        if forbidden:
            raise ValueError(f"{provenance_id}: count quotas are forbidden: {sorted(forbidden)}")
        if record.get("source_kind") not in SOURCE_KINDS:
            raise ValueError(f"{provenance_id}: unknown source_kind {record.get('source_kind')!r}")
        if record.get("status") not in STATUSES:
            raise ValueError(f"{provenance_id}: unknown status {record.get('status')!r}")
        for field in ("title", "source_reference", "claim"):
            value = record.get(field)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{provenance_id}: {field} must be a non-empty string")
        for field in ("supports", "transfer_boundaries", "contraindications", "verification_modes"):
            value = record.get(field)
            if not isinstance(value, (tuple, list)) or not value:
                raise ValueError(f"{provenance_id}: {field} must be a non-empty sequence")
            if not all(isinstance(item, str) and item.strip() for item in value):
                raise ValueError(f"{provenance_id}: {field} must contain non-empty strings")
    identifiers = [record["provenance_id"] for record in records]
    if identifiers != sorted(identifiers):
        raise ValueError("UX provenance must be canonically sorted by provenance_id")
    return {"valid": True, "record_count": len(records), "errors": []}


validate_ux_provenance(UX_PROVENANCE)
_PROVENANCE_INDEX = {item["provenance_id"]: item for item in UX_PROVENANCE}


def get_ux_provenance(provenance_id: str) -> dict[str, Any] | None:
    record = _PROVENANCE_INDEX.get(provenance_id)
    return deepcopy(record) if record is not None else None


def query_ux_provenance(
    *,
    source_kind: str | None = None,
    verification_mode: str | None = None,
    text: str | None = None,
    limit: int = 20,
) -> list[dict[str, Any]]:
    _validate_limit(limit)
    records = [
        item
        for item in UX_PROVENANCE
        if (source_kind is None or item["source_kind"] == source_kind)
        and (verification_mode is None or verification_mode in item["verification_modes"])
        and _text_matches(item, text)
    ]
    return deepcopy(records[:limit])


__all__ = [
    "SOURCE_KINDS",
    "UX_PROVENANCE",
    "get_ux_provenance",
    "query_ux_provenance",
    "validate_ux_provenance",
]
