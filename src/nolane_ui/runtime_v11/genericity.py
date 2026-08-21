"""Dynamic genericity evidence for V11 Phase 4.

Genericity is judged from authored causality and accumulation, never from a
permanent blacklist or a scalar 'AI-looking' score. Trend tells expire unless
reviewed so contemporary model habits do not become timeless design law.
"""
from __future__ import annotations

from copy import deepcopy
from datetime import date
from typing import Any

TELL_STATUSES = {"ACTIVE", "WATCH", "RETIRED"}


def _parse_date(value: Any, field: str, errors: list[str]) -> date | None:
    if not isinstance(value, str):
        errors.append(f"{field} must be an ISO date")
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        errors.append(f"{field} must be an ISO date")
        return None


def validate_trend_registry(registry: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(registry, dict):
        return {"valid": False, "errors": ["trend registry must be an object"]}
    if registry.get("version") != 11:
        errors.append("version must equal 11")
    tells = registry.get("tells")
    if not isinstance(tells, list):
        errors.append("tells must be a list")
        return {"valid": False, "errors": errors}
    seen: set[str] = set()
    for index, tell in enumerate(tells):
        prefix = f"tells[{index}]"
        if not isinstance(tell, dict):
            errors.append(f"{prefix} must be an object")
            continue
        tell_id = tell.get("tell_id")
        if not isinstance(tell_id, str) or not tell_id.strip():
            errors.append(f"{prefix}.tell_id must be non-empty")
        elif tell_id in seen:
            errors.append(f"duplicate tell_id: {tell_id}")
        else:
            seen.add(tell_id)
        if tell.get("status") not in TELL_STATUSES:
            errors.append(f"{prefix}.status is invalid")
        if tell.get("implementation") != "independently-authored":
            errors.append(f"{prefix}.implementation must equal independently-authored")
        for field in ("observed_pattern", "falsifier"):
            if not isinstance(tell.get(field), str) or not tell[field].strip():
                errors.append(f"{prefix}.{field} must be non-empty")
        parsed = {}
        for field in ("first_observed", "last_reviewed", "review_after"):
            parsed[field] = _parse_date(tell.get(field), f"{prefix}.{field}", errors)
        if all(parsed.values()):
            if parsed["last_reviewed"] < parsed["first_observed"]:
                errors.append(f"{prefix}.last_reviewed precedes first_observed")
            if parsed["review_after"] < parsed["last_reviewed"]:
                errors.append(f"{prefix}.review_after precedes last_reviewed")
        for field in ("source_provenance", "applicable_contexts", "non_applicable_contexts"):
            value = tell.get(field)
            if not isinstance(value, list) or any(not isinstance(item, str) or not item.strip() for item in value):
                errors.append(f"{prefix}.{field} must be a list of non-empty strings")
    return {"valid": not errors, "errors": errors}


def _active_tell_ids(registry: dict[str, Any], as_of: str) -> set[str]:
    validation = validate_trend_registry(registry)
    if not validation["valid"]:
        raise ValueError("invalid trend registry: " + "; ".join(validation["errors"]))
    today = date.fromisoformat(as_of)
    active: set[str] = set()
    for tell in registry["tells"]:
        if tell["status"] == "RETIRED":
            continue
        if today > date.fromisoformat(tell["review_after"]):
            continue
        active.add(tell["tell_id"])
    return active


def _signal_debt(signal: dict[str, Any]) -> float:
    specificity = float(signal.get("subject_specificity", 0.5))
    necessity = float(signal.get("semantic_necessity", 0.5))
    frequency = max(0.0, float(signal.get("frequency", 1.0)))
    hierarchy_cost = max(0.0, float(signal.get("hierarchy_cost", 0.0)))
    removal_cost = min(1.0, max(0.0, float(signal.get("removal_cost", 0.5))))
    # The number is internal evidence aggregation, not a beauty or AI score.
    return (1.0 - specificity) + (1.0 - necessity) + min(frequency / 4.0, 2.0) + hierarchy_cost + (1.0 - removal_cost)


def assess_genericity(
    *,
    structural_signals: list[dict[str, Any]],
    trend_matches: list[dict[str, Any]],
    trend_registry: dict[str, Any],
    as_of: str,
) -> dict[str, Any]:
    if not isinstance(structural_signals, list) or not isinstance(trend_matches, list):
        raise ValueError("signals and trend matches must be lists")
    active_ids = _active_tell_ids(trend_registry, as_of)
    active_matches = [deepcopy(item) for item in trend_matches if isinstance(item, dict) and item.get("tell_id") in active_ids]
    ledger = []
    for signal in structural_signals:
        if not isinstance(signal, dict):
            continue
        item = deepcopy(signal)
        item["debt_evidence"] = round(_signal_debt(item), 4)
        ledger.append(item)
    systemic = [item for item in ledger if item["debt_evidence"] >= 3.0]
    if len(systemic) >= 2:
        verdict = "GENERICITY_DEBT"
    elif ledger or active_matches:
        verdict = "WATCH"
    else:
        verdict = "SPECIFIC"
    return {
        "verdict": verdict,
        "structural_signals": ledger,
        "active_trend_matches": active_matches,
        "expired_or_inactive_match_count": len(trend_matches) - len(active_matches),
        "accumulation": {
            "systemic_signal_count": len(systemic),
            "cross_signal_count": len(ledger),
            "active_trend_count": len(active_matches),
        },
        "claim_boundary": "genericity-evidence-only",
    }


def product_substitution_assessment(
    *,
    original_product: str,
    substitute_products: list[str],
    mechanism_fit: dict[str, float],
) -> dict[str, Any]:
    if not original_product or not isinstance(substitute_products, list) or not substitute_products:
        raise ValueError("product substitution requires original and substitute products")
    fits = [float(mechanism_fit.get(product, 0.0)) for product in substitute_products]
    high_fit = sum(value >= 0.75 for value in fits)
    verdict = "WEAK_SUBJECT_SPECIFICITY" if high_fit >= max(2, (len(fits) + 1) // 2) else "SUBJECT_SPECIFIC"
    return {
        "original_product": original_product,
        "substitute_products": deepcopy(substitute_products),
        "mechanism_fit": {key: float(value) for key, value in mechanism_fit.items()},
        "interchangeable_product_count": high_fit,
        "verdict": verdict,
        "claim_boundary": "product-substitution-evidence-only",
    }


__all__ = ["TELL_STATUSES", "assess_genericity", "product_substitution_assessment", "validate_trend_registry"]
