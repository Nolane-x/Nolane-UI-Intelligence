"""Compatibility bridge from the V12 reality catalog into the V13 rule contract.

This adapter does not reinterpret V12 authority. It preserves rule id, class,
severity and enforcement, then adds the richer V13 operational planes required
for provenance, falsifiability, ownership and capability honesty.
"""
from __future__ import annotations

from typing import Any


_DOMAIN_OWNERS = {
    "accessibility": "designing-accessible-interfaces",
    "pointer": "critiquing-input-modality",
    "forms": "designing-forms",
    "navigation": "architecting-information",
    "state": "designing-empty-loading-error-states",
    "recovery": "designing-error-recovery",
    "performance": "designing-perceived-performance",
    "motion": "designing-motion",
    "layout": "designing-responsive-layouts",
    "content": "designing-content-taxonomy-management",
    "data": "proving-visual-encoding-semantics",
    "modal": "designing-dialog-systems",
    "drag": "designing-direct-manipulation",
    "selection": "designing-bulk-selection-and-actions",
    "privacy": "designing-privacy-controls",
}


def _as_list(value: Any) -> list[str]:
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    if isinstance(value, str) and value.strip():
        return [value.strip()]
    return []


def _capabilities_for(domain: str) -> dict[str, str]:
    # Compatibility defaults are intentionally conservative. They describe what
    # evidence may contribute; they do not claim an implemented detector exists.
    modes = {
        "static": "PARTIAL",
        "dom": "PARTIAL",
        "computed-style": "PARTIAL",
        "browser-runtime": "PARTIAL",
        "interaction": "PARTIAL",
        "accessibility-tree": "UNSUPPORTED",
        "visual-render": "PARTIAL",
        "semantic-product": "PARTIAL",
        "cross-generation": "UNSUPPORTED",
        "human-review": "REQUIRED",
    }
    if domain == "accessibility":
        modes["accessibility-tree"] = "REQUIRED"
        modes["interaction"] = "REQUIRED"
    elif domain in {"pointer", "forms", "navigation", "state", "recovery", "modal", "drag", "selection"}:
        modes["interaction"] = "REQUIRED"
    elif domain == "performance":
        modes["browser-runtime"] = "REQUIRED"
    elif domain in {"layout", "motion"}:
        modes["visual-render"] = "REQUIRED"
    elif domain in {"content", "data", "privacy"}:
        modes["semantic-product"] = "REQUIRED"
    return modes


def normalize_v12_rule(rule: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(rule, dict):
        raise ValueError("V12 compatibility requires a rule object")
    rule_id = str(rule.get("rule_id", "")).strip()
    domain = str(rule.get("domain", "")).strip()
    title = str(rule.get("title", "")).strip()
    failure = str(rule.get("failure_mode", "")).strip()
    if not rule_id.startswith("ui.") or not domain or not title or not failure:
        raise ValueError("V12 compatibility requires rule_id, domain, title and failure_mode")

    observables = _as_list(rule.get("observables")) or [failure]
    repairs = _as_list(rule.get("repair"))
    verification = _as_list(rule.get("verification"))
    exceptions = _as_list(rule.get("exceptions"))
    applies = _as_list(rule.get("applies_when"))

    statement = (
        f"{title}. The interface must preserve the user-visible product truth described by this rule "
        f"and must not permit the documented failure state: {failure}"
    )
    intent = (
        f"Carry the V12 operational guarantee for {title.lower()} into the richer V13 evidence model "
        "without weakening its existing enforcement, consequence, or verification boundary."
    )
    verification_probe = verification[0] if verification else f"Reproduce {rule_id} against the affected scope."
    falsifier = f"{verification_probe} [{rule_id}] {failure}"
    user_impact = (
        f"If this failure occurs, the affected user can receive an inoperable, misleading, lossy, "
        f"or otherwise unreliable product outcome: {failure}"
    )

    return {
        "rule_id": rule_id,
        "domain": domain,
        "class": rule.get("class"),
        "severity": rule.get("severity"),
        "enforcement": rule.get("enforcement"),
        "title": title,
        "statement": statement,
        "intent": intent,
        "applies_when": applies,
        "does_not_apply_when": exceptions,
        "failure_modes": [failure],
        "user_impacts": [user_impact],
        "observables": observables,
        "falsifiers": [falsifier],
        "repairs": repairs,
        "exceptions": exceptions,
        "verification": verification,
        "owner_hints": [_DOMAIN_OWNERS.get(domain, "critiquing-user-experience")],
        "verifier_hints": ["critiquing-user-experience"],
        "capabilities": _capabilities_for(domain),
        "provenance_ids": ["nui-v12-reality-catalog"],
        "status": "active",
        "legacy_contract_version": 12,
    }


__all__ = ["normalize_v12_rule"]
