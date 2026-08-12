"""Deterministic v2 validators for UI industry coverage and routing.

These validators intentionally check only machine-verifiable structure. They do
not infer usability, safety, accessibility, or legal conformance from metadata.
"""
from __future__ import annotations

from datetime import date
from typing import Any, Iterable

ALLOWED_DRIFT = {"low", "medium", "high", "very-high"}
DRIFT_MAX_AGE_DAYS = {"very-high": 45, "high": 150, "medium": 400, "low": 800}
REQUIRED_SATURATION_DIMENSIONS = {"breadth", "depth", "contradictions", "novelty", "freshness"}


def _parse_date(value: str) -> date:
    return date.fromisoformat(value[:10])


def validate_industry_atlas(atlas: dict[str, Any], graph: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    skills = graph.get("skills", {}) if isinstance(graph, dict) else {}
    axes = atlas.get("axes", {}) if isinstance(atlas, dict) else {}
    mandatory_axes = {
        "surfaces", "input_modalities", "ai_roles", "risk_classes",
        "temporal_behaviors", "social_contexts",
    }
    missing_axes = sorted(mandatory_axes - set(axes))
    if missing_axes:
        errors.append(f"industry atlas missing axes: {missing_axes}")

    cells = atlas.get("coverage_cells", [])
    if not isinstance(cells, list) or not cells:
        errors.append("industry atlas must contain coverage_cells")
        cells = []
    seen: set[str] = set()
    for cell in cells:
        if not isinstance(cell, dict):
            errors.append("industry atlas coverage cell must be an object")
            continue
        cid = cell.get("id")
        if not isinstance(cid, str) or not cid:
            errors.append("industry atlas coverage cell requires id")
            continue
        if cid in seen:
            errors.append(f"duplicate industry atlas cell {cid}")
        seen.add(cid)
        owners = cell.get("owner_skills", [])
        verifiers = cell.get("verifier_skills", [])
        if not isinstance(owners, list) or not owners:
            errors.append(f"atlas cell {cid} has no owner skills")
            owners = []
        if not isinstance(verifiers, list) or not verifiers:
            errors.append(f"atlas cell {cid} has no verifier skills")
            verifiers = []
        for owner in owners:
            if owner not in skills:
                errors.append(f"atlas cell {cid} references undeclared owner {owner}")
        for verifier in verifiers:
            if verifier not in skills:
                errors.append(f"atlas cell {cid} references undeclared verifier {verifier}")
        if set(owners) & set(verifiers):
            errors.append(f"atlas cell {cid} uses the same skill as owner and verifier")

    return {
        "valid": not errors,
        "errors": errors,
        "coverage_cell_count": len(cells),
        "axis_count": len(axes),
    }


def validate_source_ledger(ledger: dict[str, Any], as_of: str | None = None) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    allowed = set(ledger.get("authority_classes", []))
    if not allowed:
        errors.append("source ledger must declare authority_classes")
    sources = ledger.get("sources", [])
    if not isinstance(sources, list) or not sources:
        errors.append("source ledger must contain sources")
        sources = []
    ids: set[str] = set()
    now = _parse_date(as_of or ledger.get("reviewed_at") or date.today().isoformat())
    required = {"id", "title", "publisher", "url", "authority", "status", "domains", "drift", "reviewed_at", "license_note", "mechanisms_absorbed"}
    for source in sources:
        if not isinstance(source, dict):
            errors.append("source ledger record must be an object")
            continue
        sid = source.get("id", "<unknown>")
        missing = sorted(required - set(source))
        if missing:
            errors.append(f"source {sid} missing fields: {missing}")
            continue
        if sid in ids:
            errors.append(f"duplicate source id {sid}")
        ids.add(sid)
        authority = source.get("authority")
        if authority not in allowed:
            errors.append(f"source {sid} has unknown authority {authority}")
        drift = source.get("drift")
        if drift not in ALLOWED_DRIFT:
            errors.append(f"source {sid} has invalid drift {drift}")
            continue
        if not isinstance(source.get("mechanisms_absorbed"), list) or not source["mechanisms_absorbed"]:
            errors.append(f"source {sid} has no absorbed mechanism")
        try:
            reviewed = _parse_date(source["reviewed_at"])
            age = (now - reviewed).days
            if age < 0:
                errors.append(f"source {sid} reviewed_at is in the future")
            elif age > DRIFT_MAX_AGE_DAYS[drift]:
                errors.append(f"source {sid} is stale for {drift} drift: {age} days old")
            elif age > int(DRIFT_MAX_AGE_DAYS[drift] * 0.8):
                warnings.append(f"source {sid} approaches freshness limit")
        except Exception:
            errors.append(f"source {sid} has invalid reviewed_at {source.get('reviewed_at')!r}")

    return {"valid": not errors, "errors": errors, "warnings": warnings, "source_count": len(sources)}


def validate_research_saturation(
    record: dict[str, Any], ledger: dict[str, Any], atlas: dict[str, Any], as_of: str | None = None
) -> dict[str, Any]:
    errors: list[str] = []
    decision = record.get("decision")
    if decision not in {"OPEN", "SATURATED"}:
        errors.append(f"invalid research saturation decision {decision}")
    if not record.get("as_of"):
        errors.append("research saturation decision requires as_of")
    evidence = record.get("evidence", {})
    missing_dimensions = sorted(REQUIRED_SATURATION_DIMENSIONS - set(evidence)) if isinstance(evidence, dict) else sorted(REQUIRED_SATURATION_DIMENSIONS)
    if missing_dimensions:
        errors.append(f"research saturation missing evidence dimensions: {missing_dimensions}")

    if decision == "SATURATED":
        for dimension in sorted(REQUIRED_SATURATION_DIMENSIONS):
            item = evidence.get(dimension, {}) if isinstance(evidence, dict) else {}
            if item.get("status") != "PASS":
                errors.append(f"SATURATED research requires PASS {dimension} evidence")
            if not item.get("criterion") or not item.get("observed"):
                errors.append(f"SATURATED research requires falsifiable {dimension} criterion and observation")
        if not record.get("reopen_conditions"):
            errors.append("SATURATED research requires reopen_conditions")

    ledger_result = validate_source_ledger(ledger, as_of=as_of)
    if not ledger_result["valid"]:
        errors.extend(f"research source ledger: {error}" for error in ledger_result["errors"])

    cells = atlas.get("coverage_cells", []) if isinstance(atlas, dict) else []
    for cell in cells:
        if isinstance(cell, dict) and (not cell.get("owner_skills") or not cell.get("verifier_skills")):
            errors.append(f"research saturation cannot close with unowned atlas cell {cell.get('id', '<unknown>')}")

    return {"valid": not errors, "errors": errors, "decision": decision}


def mandatory_routes_for_profile(profile: dict[str, Any]) -> set[str]:
    required: set[str] = set()
    surfaces = set(profile.get("platform_surfaces", []))
    modalities = set(profile.get("input_modalities", []))
    temporal = set(profile.get("temporal_behaviors", []))
    ai_role = profile.get("ai_role", "none")
    risk = profile.get("risk_class", "routine")

    surface_routes = {
        "desktop": {"designing-desktop-windowed-workspaces"},
        "large-screen-foldable": {"designing-foldable-large-screen-interfaces"},
        "tv-ten-foot": {"designing-tv-ten-foot-interfaces", "designing-gamepad-remote-focus", "critiquing-input-modality"},
        "wearable": {"designing-wearable-glanceable-interfaces", "critiquing-cognitive-load"},
        "automotive": {"designing-automotive-interfaces", "engineering-human-factors", "critiquing-human-factors-and-safety"},
        "spatial-xr": {"designing-spatial-xr-interfaces", "designing-gaze-hand-spatial-input", "critiquing-platform-fit", "critiquing-input-modality"},
        "game-hud": {"designing-game-hud-and-menus"},
        "cli-tui": {"designing-cli-tui-interfaces", "designing-keyboard-power-user-ux"},
        "embedded-kiosk": {"designing-embedded-kiosk-interfaces", "critiquing-performance-and-resilience"},
    }
    for surface in surfaces:
        required |= surface_routes.get(surface, set())

    modality_routes = {
        "keyboard": {"designing-keyboard-power-user-ux"},
        "pen": {"designing-pointer-touch-pen-input"},
        "gamepad": {"designing-gamepad-remote-focus"},
        "remote": {"designing-gamepad-remote-focus"},
        "voice": {"designing-voice-conversational-ui"},
        "gaze": {"designing-gaze-hand-spatial-input"},
        "hand-gesture": {"designing-gaze-hand-spatial-input"},
        "alternative-input": {"designing-alternative-input", "critiquing-input-modality"},
        "haptics": {"designing-haptics-and-multisensory-feedback"},
    }
    for modality in modalities:
        required |= modality_routes.get(modality, set())

    if ai_role in {"assistive", "generative", "agentic", "multi-agent", "generative-ui"}:
        required |= {"designing-human-ai-interaction", "critiquing-ai-trust-and-agency"}
    if ai_role in {"generative", "agentic", "multi-agent", "generative-ui"}:
        required.add("designing-ai-uncertainty-and-provenance")
    if ai_role == "agentic":
        required.add("designing-agent-autonomy-and-control")
    if ai_role == "multi-agent":
        required.add("designing-multi-agent-surfaces")
    if ai_role == "generative-ui":
        required |= {"designing-generative-ui", "critiquing-security-and-privacy"}

    if risk == "privacy-sensitive":
        required |= {"designing-privacy-sensitive-interfaces", "critiquing-security-and-privacy"}
    elif risk == "security-sensitive":
        required.add("critiquing-security-and-privacy")
    elif risk == "financial":
        required |= {"designing-financial-transaction-ui", "designing-high-stakes-decisions", "critiquing-security-and-privacy"}
    elif risk == "medical":
        required |= {"designing-medical-safety-critical-ui", "engineering-human-factors", "designing-high-stakes-decisions", "critiquing-human-factors-and-safety"}
    elif risk == "safety-critical":
        required |= {"engineering-human-factors", "designing-high-stakes-decisions", "critiquing-human-factors-and-safety"}

    if "streaming" in temporal:
        required |= {"designing-latency-and-progressive-feedback", "critiquing-performance-and-resilience"}
        if ai_role != "none":
            required.add("designing-streaming-ai-responses")
    if "realtime" in temporal:
        required |= {"designing-real-time-updates", "critiquing-performance-and-resilience"}
    if "offline-degraded" in temporal:
        required |= {"designing-offline-degraded-experiences", "critiquing-performance-and-resilience"}
    if "interruption-sensitive" in temporal:
        required |= {"designing-notifications-and-interruptions", "modeling-cognitive-load-and-attention"}

    return required


def validate_mandatory_routes(profile: dict[str, Any], selected_skills: Iterable[str]) -> dict[str, Any]:
    required = mandatory_routes_for_profile(profile)
    selected = set(selected_skills)
    missing = sorted(required - selected)
    return {"valid": not missing, "required_routes": sorted(required), "missing_routes": missing}
