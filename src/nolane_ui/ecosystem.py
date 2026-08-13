"""Typed UI ecosystem intelligence for NUI v4.

The registry is retrieval evidence, not an authority to install or copy code.
Selection remains bounded by product fit, current source inspection, license
posture, accessibility, integration cost, runtime proof and exit strategy.
"""
from __future__ import annotations

from typing import Any

ALLOWED_ROLES = {
    "animated-component-gallery", "motion-engine", "motion-skill-suite",
    "headless-primitive", "interaction-state-machine", "design-system",
    "component-distribution", "positioning-engine", "data-visualization",
    "rich-text-editor", "data-grid", "form-engine", "drag-drop-engine",
    "canvas-sdk", "canvas-library", "3d-renderer", "3d-helper-library",
    "mobile-ui-system", "notification-system", "agent-skill-catalog",
    "design-intelligence-skill", "creative-canvas-gallery",
}
ALLOWED_LICENSE_STATUS = {"verified-compatible", "restricted", "live-check-required", "unknown"}
ALLOWED_DRIFT = {"low", "medium", "high", "very-high"}
ALLOWED_INTENTS = {"adopt", "adapt", "inspire", "build", "reject"}
MATERIAL_INTENTS = {"adopt", "adapt"}


def validate_ui_ecosystem_registry(registry: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    if not isinstance(registry, dict):
        return {"valid": False, "errors": ["UI ecosystem registry must be an object"], "warnings": [], "source_count": 0, "category_count": 0}
    if registry.get("version") != 4:
        errors.append("UI ecosystem registry must declare version 4")
    sources = registry.get("sources")
    if not isinstance(sources, list) or not sources:
        return {"valid": False, "errors": errors + ["UI ecosystem registry requires sources"], "warnings": [], "source_count": 0, "category_count": 0}
    ids: set[str] = set(); urls: set[str] = set(); categories: set[str] = set()
    for index, source in enumerate(sources):
        if not isinstance(source, dict):
            errors.append(f"registry source {index} must be an object"); continue
        sid = source.get("id"); url = source.get("url")
        if not isinstance(sid, str) or not sid.strip(): errors.append(f"registry source {index} requires id"); continue
        if sid in ids: errors.append(f"duplicate ecosystem source id {sid}")
        ids.add(sid)
        if not isinstance(url, str) or not url.startswith("https://"):
            errors.append(f"ecosystem source {sid} requires canonical https url")
        elif url in urls: errors.append(f"duplicate ecosystem source url {url}")
        else: urls.add(url)
        role = source.get("role")
        if role not in ALLOWED_ROLES: errors.append(f"ecosystem source {sid} has invalid role {role}")
        cats = source.get("categories")
        if not isinstance(cats, list) or not cats or not all(isinstance(x, str) and x for x in cats):
            errors.append(f"ecosystem source {sid} requires categories")
        else: categories.update(cats)
        caps = source.get("capabilities")
        if not isinstance(caps, list) or not caps: errors.append(f"ecosystem source {sid} requires capabilities")
        stacks = source.get("stacks")
        if not isinstance(stacks, list) or not stacks: errors.append(f"ecosystem source {sid} requires stacks")
        modes = source.get("allowed_intents")
        if not isinstance(modes, list) or not modes or not set(modes).issubset(ALLOWED_INTENTS):
            errors.append(f"ecosystem source {sid} has invalid allowed_intents")
        license_data = source.get("license")
        if not isinstance(license_data, dict):
            errors.append(f"ecosystem source {sid} requires license object")
        else:
            if license_data.get("status") not in ALLOWED_LICENSE_STATUS: errors.append(f"ecosystem source {sid} has invalid license status")
            if license_data.get("status") == "verified-compatible" and not license_data.get("evidence_url"):
                errors.append(f"ecosystem source {sid} verified license requires evidence_url")
        provenance = source.get("provenance")
        if not isinstance(provenance, dict) or not provenance.get("inspected") or not provenance.get("verified_at"):
            errors.append(f"ecosystem source {sid} requires inspected provenance and verified_at")
        drift = source.get("drift")
        if drift not in ALLOWED_DRIFT: errors.append(f"ecosystem source {sid} has invalid drift {drift}")
        if drift in {"high", "very-high"} and source.get("verify_live_before_use") is not True:
            errors.append(f"high-drift ecosystem source {sid} must require live verification")
        if not isinstance(source.get("when_to_use"), list) or not source.get("when_to_use"):
            errors.append(f"ecosystem source {sid} requires when_to_use")
        if not isinstance(source.get("when_not_to_use"), list) or not source.get("when_not_to_use"):
            errors.append(f"ecosystem source {sid} requires when_not_to_use")
        if source.get("popularity") is not None:
            warnings.append(f"ecosystem source {sid} contains popularity metadata; ranking must ignore it")
    return {"valid": not errors, "errors": errors, "warnings": warnings, "source_count": len(ids), "category_count": len(categories)}


def query_ui_ecosystem(registry: dict[str, Any], query: dict[str, Any]) -> dict[str, Any]:
    """Deterministic candidate retrieval. Popularity is deliberately absent."""
    requested_caps = set(query.get("capabilities", []))
    requested_stacks = set(query.get("stacks", []))
    requested_categories = set(query.get("categories", []))
    intent = query.get("intent", "inspire")
    matches = []
    for source in registry.get("sources", []):
        if not isinstance(source, dict): continue
        allowed = set(source.get("allowed_intents", []))
        if intent not in allowed: continue
        caps = set(source.get("capabilities", [])); stacks = set(source.get("stacks", [])); cats = set(source.get("categories", []))
        cap_hits = len(requested_caps & caps) if requested_caps else 0
        stack_fit = (not requested_stacks) or bool(requested_stacks & stacks) or "framework-agnostic" in stacks or "web" in stacks
        cat_hits = len(requested_categories & cats) if requested_categories else 0
        if requested_caps and not cap_hits: continue
        if not stack_fit: continue
        if requested_categories and not cat_hits: continue
        a11y = source.get("accessibility_posture", "unknown")
        role_bonus = 2 if source.get("role") in {"headless-primitive", "interaction-state-machine", "motion-engine"} else 1
        score = cap_hits * 5 + cat_hits * 3 + (3 if requested_stacks & stacks else 1) + role_bonus + (2 if a11y in {"strong", "explicit"} else 0)
        matches.append({"id": source.get("id"), "url": source.get("url"), "role": source.get("role"), "score": score, "license_status": source.get("license", {}).get("status"), "verify_live_before_use": source.get("verify_live_before_use", False)})
    matches.sort(key=lambda x: (-x["score"], x["id"] or ""))
    return {
        "matches": matches,
        "ranking_factors": ["capability-fit", "stack-fit", "category-fit", "source-role-fit", "accessibility-posture"],
        "live_search_required": not matches or all(m.get("verify_live_before_use") for m in matches[:3]),
    }


def validate_reference_ledger(ledger: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    refs = ledger.get("references") if isinstance(ledger, dict) else None
    if not isinstance(refs, list) or not refs:
        return {"valid": False, "errors": ["reference ledger requires references"]}
    seen: set[tuple[str, str]] = set()
    for index, ref in enumerate(refs):
        if not isinstance(ref, dict): errors.append(f"reference {index} must be an object"); continue
        sid, url, usage = ref.get("source_id"), ref.get("url"), ref.get("usage")
        if not isinstance(sid, str) or not sid: errors.append(f"reference {index} requires source_id")
        if not isinstance(url, str) or not url.startswith("https://"): errors.append(f"reference {sid} requires canonical URL citation")
        if usage not in ALLOWED_INTENTS: errors.append(f"reference {sid} has invalid usage {usage}")
        if not isinstance(ref.get("mechanism"), str) or len(ref.get("mechanism", "").split()) < 2: errors.append(f"reference {sid} requires extracted mechanism")
        if not isinstance(ref.get("inspected"), list) or not ref.get("inspected"): errors.append(f"reference {sid} requires inspected paths or documents")
        if usage in {"adapt", "adopt", "inspire"} and (not isinstance(ref.get("adaptation_boundary"), str) or not ref.get("adaptation_boundary", "").strip()):
            errors.append(f"reference {sid} requires adaptation boundary")
        key = (str(sid), str(url))
        if key in seen: errors.append(f"duplicate material reference {sid}")
        seen.add(key)
    return {"valid": not errors, "errors": errors, "reference_count": len(refs)}


def validate_source_selection(selection: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(selection, dict): return {"valid": False, "errors": ["source selection must be an object"]}
    decision = selection.get("decision")
    if decision not in ALLOWED_INTENTS: errors.append(f"invalid source decision {decision}")
    if not isinstance(selection.get("source_id"), str) or not selection.get("source_id"): errors.append("source selection requires source_id")
    rationale = selection.get("rationale")
    if not isinstance(rationale, list) or not rationale: errors.append("source selection requires rationale")
    else:
        normalized = " ".join(map(str, rationale)).lower()
        semantic = [x for x in ("capability", "stack", "role", "accessibility", "license", "dependency", "performance", "product", "mechanism") if x in normalized]
        if not semantic and any(x in normalized for x in ("star", "popular", "trend", "github")):
            errors.append("popularity-only source selection is forbidden")
    citations = selection.get("citations")
    if decision in {"adopt", "adapt", "inspire"} and (not isinstance(citations, list) or not citations or not all(isinstance(x, str) and x.startswith("https://") for x in citations)):
        errors.append("material source decision requires URL citation")
    if decision in MATERIAL_INTENTS:
        if selection.get("license_posture") != "verified-compatible": errors.append(f"{decision} requires verified compatible license posture")
        inspected = set(selection.get("inspected", []))
        for required in ("readme", "license", "implementation"):
            if required not in inspected: errors.append(f"{decision} requires {required} inspection")
        if selection.get("source_role_fit") is False: errors.append(f"{decision} forbidden when source role does not fit the decision")
    return {"valid": not errors, "errors": errors}


def validate_rich_interaction_contract(record: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(record, dict): return {"valid": False, "errors": ["rich interaction contract must be an object"]}
    states = record.get("states")
    if not isinstance(states, list) or not {"idle", "active"}.issubset(set(states)): errors.append("rich interaction requires explicit idle and active states")
    modalities = record.get("modalities")
    if not isinstance(modalities, list) or not modalities: errors.append("rich interaction requires modalities")
    elif "pointer" in modalities and "keyboard" not in modalities: errors.append("pointer-rich interaction requires keyboard-equivalent path")
    for field in ("reduced_motion", "focus_behavior", "performance_budget", "ssr_strategy", "exit_strategy"):
        if not isinstance(record.get(field), str) or not record.get(field, "").strip(): errors.append(f"rich interaction requires {field}")
    if record.get("interruptible") is not True: errors.append("rich interaction must declare interruptible behavior")
    if record.get("retargetable") is not True: errors.append("rich interaction must declare retargetable behavior")
    return {"valid": not errors, "errors": errors}


def validate_ui_integration_audit(record: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(record, dict): return {"valid": False, "errors": ["integration audit must be an object"]}
    required = ("license", "dependency", "accessibility", "reduced_motion", "ssr_hydration", "performance", "api_drift", "security", "exit_strategy", "local_runtime")
    checks = record.get("checks")
    if not isinstance(checks, dict): checks = {}; errors.append("integration audit requires checks")
    for key in required:
        item = checks.get(key)
        if not isinstance(item, dict) or item.get("status") not in {"PASS", "N/A"} or not item.get("evidence"):
            errors.append(f"integration audit requires evidence-backed PASS or N/A for {key}")
    return {"valid": not errors, "errors": errors}


__all__ = [
    "validate_ui_ecosystem_registry", "query_ui_ecosystem", "validate_reference_ledger",
    "validate_source_selection", "validate_rich_interaction_contract", "validate_ui_integration_audit",
]
