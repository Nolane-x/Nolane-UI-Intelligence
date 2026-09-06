"""Evidence-bounded UX impact ranking for UX Intelligence v3."""
from __future__ import annotations

from copy import deepcopy
import math
from typing import Any, Iterable

from .v3_catalog import UX_IMPACT_SCORE_WEIGHTS, UX_PRIORITY_BANDS, UX_REQUIRED_IMPACT_COMPONENTS


_ORIGINS = frozenset({"declared", "observed", "inferred"})
_COMPONENTS = frozenset(UX_IMPACT_SCORE_WEIGHTS)


def _source_id(item: dict[str, Any], index: int) -> str:
    for field in ("finding_id", "candidate_id", "regression_id", "request_id"):
        value = item.get(field)
        if isinstance(value, str) and value.strip():
            return value.strip()
    fingerprint = item.get("finding_fingerprint")
    if isinstance(fingerprint, str) and fingerprint.strip():
        return "uxrgr:" + fingerprint.strip()
    rule_id = item.get("rule_id")
    regression_class = item.get("class")
    if isinstance(rule_id, str) and rule_id.strip() and isinstance(regression_class, str) and regression_class.strip():
        return f"uxrgr:{regression_class.strip()}:{rule_id.strip()}"
    raise ValueError(f"items[{index}] has no stable source identity")


def _value(raw: Any, label: str) -> float:
    if isinstance(raw, bool) or not isinstance(raw, (int, float)):
        raise TypeError(f"{label}.value must be numeric")
    result = float(raw)
    if not math.isfinite(result) or not 0.0 <= result <= 1.0:
        raise ValueError(f"{label}.value must be finite and within [0, 1]")
    return result


def _component(raw: Any, label: str) -> dict[str, Any]:
    if not isinstance(raw, dict):
        raise TypeError(f"{label} must be an object")
    origin = raw.get("origin")
    if origin not in _ORIGINS:
        raise ValueError(f"{label}.origin must be declared, observed, or inferred")
    refs = raw.get("evidence_refs")
    if not isinstance(refs, (tuple, list)) or not refs:
        raise ValueError(f"{label}.evidence_refs must be a non-empty sequence")
    normalized_refs = []
    for index, ref in enumerate(refs):
        if not isinstance(ref, str) or not ref.strip():
            raise ValueError(f"{label}.evidence_refs[{index}] must be a non-empty string")
        normalized_refs.append(ref.strip())
    return {"value": _value(raw.get("value"), label), "origin": origin, "evidence_refs": tuple(sorted(set(normalized_refs)))}


def _evidence_for(source_id: str, evidence: dict[str, Any]) -> dict[str, Any]:
    if set(evidence) <= _COMPONENTS:
        return evidence
    raw = evidence.get(source_id)
    if raw is None:
        return {}
    if not isinstance(raw, dict):
        raise TypeError(f"impact_evidence[{source_id!r}] must be an object")
    return raw


def _band(score: float) -> str:
    for threshold, band in UX_PRIORITY_BANDS:
        if score >= threshold:
            return band
    raise RuntimeError("UX priority bands do not cover [0, 1]")


def rank_ux_impacts(items: Iterable[dict[str, Any]], impact_evidence: dict[str, dict[str, Any]]) -> tuple[dict[str, Any], ...]:
    """Rank UX findings/regressions without changing their authority."""
    if isinstance(items, (str, bytes)):
        raise TypeError("items must be an iterable of objects")
    if not isinstance(impact_evidence, dict):
        raise TypeError("impact_evidence must be an object")

    assessments: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    for index, raw_item in enumerate(tuple(items)):
        if not isinstance(raw_item, dict):
            raise TypeError(f"items[{index}] must be an object")
        item = deepcopy(raw_item)
        source_id = _source_id(item, index)
        if source_id in seen_ids:
            raise ValueError(f"duplicate source identity {source_id!r}")
        seen_ids.add(source_id)
        evidence = _evidence_for(source_id, impact_evidence)
        unknown = set(evidence) - _COMPONENTS
        if unknown:
            raise ValueError(f"unknown impact components for {source_id}: {sorted(unknown)!r}")

        components = {name: _component(value, f"{source_id}.{name}") for name, value in evidence.items()}
        missing_required = tuple(sorted(UX_REQUIRED_IMPACT_COMPONENTS - set(components)))
        missing_optional = tuple(sorted(_COMPONENTS - set(components) - UX_REQUIRED_IMPACT_COMPONENTS))
        if missing_required:
            score = None
            band = "unknown"
            status = "insufficient-evidence"
        else:
            score = round(sum(components[name]["value"] * UX_IMPACT_SCORE_WEIGHTS[name] for name in components), 12)
            band = _band(score)
            status = "provisional" if any(value["origin"] == "inferred" for value in components.values()) else "ranked"

        assessments.append({
            "source_id": source_id,
            "source_kind": "finding" if "finding_id" in item else "regression",
            "source_rule_id": item.get("rule_id"),
            "source_severity": item.get("severity"),
            "source_enforcement": item.get("enforcement"),
            "status": status,
            "priority_score": score,
            "priority_band": band,
            "components": components,
            "missing_required_components": missing_required,
            "missing_optional_components": missing_optional,
            "authority_boundary": "ranking-does-not-change-source-authority",
        })

    assessments.sort(key=lambda value: (value["priority_score"] is None, -(value["priority_score"] or 0.0), value["source_id"]))
    return tuple(assessments)


__all__ = ["rank_ux_impacts"]
