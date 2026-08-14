"""NUI v8 visual-media choice, provenance, toolchain and integration invariants."""
from __future__ import annotations
from typing import Any

_HIGH_AMBITION = {"flagship", "exceptional", "experiential"}


def mandatory_v8_routes(profile: dict[str, Any]) -> set[str]:
    routes: set[str] = set()
    if not isinstance(profile, dict):
        return routes
    subject_media = bool(profile.get("subject_native_media"))
    ambition = str(profile.get("visual_ambition", "")).lower()
    if subject_media or ambition in _HIGH_AMBITION:
        routes.add("mapping-visual-media-opportunities")
    if subject_media:
        routes |= {"sourcing-rights-safe-visual-media", "replacing-shape-substitution"}
    if profile.get("custom_visual_asset") or profile.get("generated_media"):
        routes |= {"authoring-domain-native-visual-assets", "orchestrating-creative-toolchains"}
    if profile.get("external_agent_skill"):
        routes.add("governing-external-agent-skills")
    if profile.get("agent_harness"):
        routes.add("exporting-nui-to-agent-harnesses")
    if profile.get("material_media_used") or subject_media:
        routes.add("validating-visual-asset-integration")
    return routes


def validate_media_opportunity_map(record: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(record, dict):
        return {"valid": False, "errors": ["media opportunity map must be an object"]}
    opportunities = record.get("opportunities", [])
    if not isinstance(opportunities, list) or not opportunities:
        errors.append("media opportunity map requires opportunities")
    else:
        for idx, item in enumerate(opportunities):
            if not isinstance(item, dict):
                errors.append(f"opportunity[{idx}] must be an object"); continue
            for key in ("slot", "semantic_job", "preferred_media", "fallback"):
                if not item.get(key): errors.append(f"opportunity[{idx}] requires {key}")
            if not isinstance(item.get("preferred_media"), list):
                errors.append(f"opportunity[{idx}].preferred_media must be a list")
    if record.get("subject_native_media") is True and record.get("decision") not in {"USE_MEDIA", "COMMISSION_MEDIA", "GENERATE_MEDIA"}:
        errors.append("subject-native media requires an explicit media-use decision or falsified reason not to use it")
    if record.get("shape_substitution_risk") not in {"low", "medium", "high"}:
        errors.append("media opportunity map requires shape_substitution_risk low|medium|high")
    return {"valid": not errors, "errors": errors}


def validate_shape_substitution_audit(record: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    decision = str(record.get("decision", "BLOCKED")) if isinstance(record, dict) else "BLOCKED"
    if not isinstance(record, dict):
        return {"valid": False, "errors": ["shape-substitution audit must be an object"], "decision": "RE_DIVERGE"}
    native = bool(record.get("subject_native_media_available"))
    material = int(record.get("material_slots", 0) or 0)
    abstract = int(record.get("abstract_shape_slots", 0) or 0)
    justified = int(record.get("justified_abstract_slots", 0) or 0)
    replacements = record.get("replacement_actions", [])
    unjustified = max(0, abstract - justified)
    if native and material > 0 and unjustified >= max(1, material // 2):
        errors.append("abstract geometry is substituting for available subject-native media")
    examples = record.get("examples", [])
    if unjustified and not isinstance(examples, list):
        errors.append("shape-substitution audit requires concrete examples")
    if errors and not replacements:
        decision = "RE_DIVERGE"
    elif errors:
        decision = "BLOCKED"
    return {"valid": not errors, "errors": errors, "decision": decision}


def validate_asset_provenance_ledger(record: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(record, dict):
        return {"valid": False, "errors": ["asset provenance ledger must be an object"]}
    assets = record.get("assets", [])
    if not isinstance(assets, list) or not assets:
        return {"valid": False, "errors": ["asset provenance ledger requires assets[]"]}
    for idx, asset in enumerate(assets):
        if not isinstance(asset, dict):
            errors.append(f"asset[{idx}] must be an object"); continue
        aid = asset.get("id", idx)
        for key in ("origin", "source_url", "license"):
            if not asset.get(key): errors.append(f"asset {aid} requires asset-level {key}")
        if asset.get("asset_license_verified") is not True:
            errors.append(f"asset {aid} requires asset_license_verified=true; source-level license assumptions are insufficient")
        if not asset.get("verified_at"):
            errors.append(f"asset {aid} requires verified_at")
        if asset.get("license") and str(asset.get("license")).upper() not in {"CC0", "PUBLIC-DOMAIN", "OWNED", "GENERATED"}:
            if not asset.get("license_url"):
                errors.append(f"asset {aid} requires license_url")
        if asset.get("license") and str(asset.get("license")).upper().startswith("CC-BY") and not asset.get("attribution"):
            errors.append(f"asset {aid} requires attribution")
        if "modification_allowed" not in asset or "commercial_use_allowed" not in asset:
            errors.append(f"asset {aid} requires explicit modification/commercial-use rights")
        if "local_transformations" not in asset:
            errors.append(f"asset {aid} requires local_transformations ledger")
    return {"valid": not errors, "errors": errors}


def validate_creative_toolchain_plan(record: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(record, dict):
        return {"valid": False, "errors": ["creative toolchain plan must be an object"]}
    if not record.get("goal"):
        errors.append("creative toolchain plan requires goal")
    stages = record.get("stages", [])
    if not isinstance(stages, list) or not stages:
        errors.append("creative toolchain plan requires stages")
    else:
        stage_ids: list[str] = []
        for idx, stage in enumerate(stages):
            if not isinstance(stage, dict): errors.append(f"stage[{idx}] must be an object"); continue
            for key in ("stage", "tool", "authority", "output", "human_or_agent_check"):
                if not stage.get(key): errors.append(f"stage[{idx}] requires {key}")
            stage_ids.append(str(stage.get("stage", "")))
        if "generate" in stage_ids and "render" not in stage_ids:
            errors.append("generated visual assets require a render/integration stage")
    if not record.get("fallback"):
        errors.append("creative toolchain plan requires fallback")
    return {"valid": not errors, "errors": errors}


def validate_visual_asset_integration(record: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(record, dict):
        return {"valid": False, "errors": ["visual asset integration evidence must be an object"]}
    if not record.get("assets"):
        errors.append("visual asset integration requires assets")
    states = record.get("rendered_states", [])
    if not isinstance(states, list) or len(states) < 2:
        errors.append("visual asset integration requires at least two material rendered states")
    checks = record.get("checks", {})
    required = {"semantic_fit", "composition_fit", "crop_resilience", "contrast_with_ui", "responsive_recomposition", "performance_budget", "alt_or_equivalent", "rights_provenance"}
    if not isinstance(checks, dict):
        errors.append("visual asset integration requires checks")
    else:
        for check in sorted(required):
            if checks.get(check) != "PASS": errors.append(f"visual asset integration check {check} must PASS")
    failures = record.get("observed_failures", [])
    if not isinstance(failures, list):
        errors.append("observed_failures must be a list")
    else:
        for idx, item in enumerate(failures):
            if not isinstance(item, dict) or not all(item.get(k) for k in ("finding", "fix", "verified_in")):
                errors.append(f"observed_failures[{idx}] requires finding/fix/verified_in")
    if record.get("decision") != "PASS": errors.append("visual asset integration requires decision PASS")
    return {"valid": not errors, "errors": errors}
