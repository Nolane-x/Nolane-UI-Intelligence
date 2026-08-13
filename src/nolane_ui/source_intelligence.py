"""NUI v6 deep source-research and cross-source synthesis invariants.

This module treats repository/source links as discovery only.  Material design
or implementation influence requires evidence tied to the mechanism-bearing
artifacts appropriate to the source role.
"""
from __future__ import annotations

from collections import Counter
from typing import Any

HIGH_AMBITION = {"flagship", "exceptional", "experiential"}
MATERIAL_USAGE = {"adopt", "adapt"}
INFLUENTIAL_USAGE = {"adopt", "adapt", "inspire"}

BASE_ARTIFACTS = {
    "adopt": {"readme", "license", "implementation"},
    "adapt": {"readme", "license", "implementation"},
    "inspire": {"readme", "mechanism-bearing-evidence"},
    "build": set(),
    "reject": set(),
}

ROLE_ARTIFACTS: dict[str, set[str]] = {
    "animated-component-gallery": {
        "component-source", "demo-example", "dependency-config", "motion-behavior", "reduced-motion",
    },
    "component-distribution": {
        "component-source", "demo-example", "dependency-config", "theme-token-boundary", "interaction-behavior",
    },
    "headless-primitive": {
        "implementation", "interaction-tests", "accessibility-guidance", "keyboard-focus-behavior", "demo-example",
    },
    "design-system": {
        "component-source", "design-guidance", "interaction-tests", "accessibility-guidance", "tokens-themes", "demo-example",
    },
    "motion-engine": {
        "implementation", "api-guidance", "demo-example", "motion-behavior", "gesture-interruption", "reduced-motion", "performance-guidance",
    },
    "motion-skill-suite": {
        "guidance", "example", "motion-behavior", "reduced-motion", "performance-guidance",
    },
    "interaction-state-machine": {
        "implementation", "state-model", "interaction-tests", "keyboard-focus-behavior", "demo-example",
    },
    "positioning-engine": {
        "implementation", "collision-behavior", "interaction-tests", "demo-example", "performance-guidance",
    },
    "data-visualization": {
        "encoding-api", "data-semantics", "demo-example", "interaction-behavior", "accessibility-guidance", "performance-guidance",
    },
    "rich-text-editor": {
        "document-model", "plugin-extension-boundary", "keyboard-focus-behavior", "interaction-tests", "demo-example", "performance-guidance",
    },
    "data-grid": {
        "data-model", "virtualization-performance", "keyboard-focus-behavior", "interaction-tests", "demo-example", "accessibility-guidance",
    },
    "form-engine": {
        "state-model", "validation-model", "interaction-tests", "accessibility-guidance", "demo-example",
    },
    "drag-drop-engine": {
        "interaction-model", "keyboard-equivalent", "collision-behavior", "interaction-tests", "accessibility-guidance", "demo-example",
    },
    "canvas-sdk": {
        "scene-model", "input-model", "plugin-extension-boundary", "demo-example", "performance-guidance", "accessibility-fallback",
    },
    "canvas-library": {
        "scene-model", "input-model", "demo-example", "performance-guidance", "accessibility-fallback",
    },
    "3d-renderer": {
        "renderer-api", "scene-model", "input-model", "demo-example", "device-performance", "accessibility-fallback",
    },
    "3d-helper-library": {
        "helper-api", "demo-example", "device-performance", "input-model", "accessibility-fallback",
    },
    "creative-canvas-gallery": {
        "component-source", "demo-example", "renderer-api", "device-performance", "accessibility-fallback",
    },
    "mobile-ui-system": {
        "component-source", "platform-guidance", "interaction-tests", "accessibility-guidance", "tokens-themes", "demo-example",
    },
    "notification-system": {
        "implementation", "announcement-behavior", "interaction-tests", "demo-example", "accessibility-guidance",
    },
    "agent-skill-catalog": {
        "skill-source", "behavioral-examples", "evaluation-evidence", "license",
    },
    "design-intelligence-skill": {
        "skill-source", "behavioral-examples", "evaluation-evidence", "license",
    },
    "icon-system": {
        "icon-catalog", "symbol-conventions", "naming-tags", "framework-delivery", "license",
    },
    "typography-source": {
        "font-catalog", "script-coverage", "weights-axes", "delivery-subsetting", "license",
    },
    "design-token-tool": {
        "token-schema", "transform-pipeline", "theme-examples", "generated-output", "migration-versioning", "license",
    },
    "style-system": {
        "configuration-model", "theme-token-boundary", "responsive-state-model", "demo-example", "performance-guidance", "license",
    },
    "visual-testing-tool": {
        "testing-api", "browser-runtime", "snapshot-model", "accessibility-integration", "ci-examples", "license",
    },
    "accessibility-testing-tool": {
        "rule-model", "testing-api", "browser-runtime", "limitations", "ci-examples", "license",
    },
    "creative-renderer": {
        "renderer-api", "scene-model", "input-model", "demo-example", "device-performance", "accessibility-fallback", "license",
    },
    "diagram-graph-ui": {
        "graph-model", "interaction-model", "keyboard-focus-behavior", "demo-example", "performance-guidance", "accessibility-guidance",
    },
    "geospatial-ui": {
        "map-renderer", "projection-data-model", "interaction-model", "demo-example", "performance-guidance", "accessibility-fallback",
    },
    "code-editor": {
        "document-model", "extension-api", "keyboard-focus-behavior", "virtualization-performance", "demo-example", "accessibility-guidance",
    },
    "terminal-ui-system": {
        "layout-style-model", "input-model", "keyboard-behavior", "demo-example", "accessibility-guidance", "license",
    },
    "ai-ui-system": {
        "message-state-model", "streaming-behavior", "tool-action-model", "demo-example", "accessibility-guidance", "license",
    },
    "animation-asset-runtime": {
        "runtime-api", "asset-format", "state-interactivity", "demo-example", "performance-guidance", "accessibility-fallback", "license",
    },
}

WHY: dict[str, str] = {
    "readme": "establish project scope and intended usage without treating marketing copy as mechanism proof",
    "license": "establish legal reuse/adaptation boundaries before material transfer",
    "implementation": "inspect the implementation that actually creates the claimed behavior",
    "mechanism-bearing-evidence": "inspect a component, demo, source file, or equivalent artifact that visibly/behaviorally carries the mechanism",
    "component-source": "inspect concrete component state, rendering and dependency behavior rather than screenshots alone",
    "demo-example": "observe the mechanism in its intended content, interaction and layout context",
    "dependency-config": "identify runtime dependencies, build assumptions and integration surface",
    "motion-behavior": "characterize timing, continuity, interruption, retargeting and information purpose",
    "reduced-motion": "determine whether the mechanism survives or degrades safely under reduced motion",
    "interaction-tests": "verify keyboard, focus, state transition and edge-case behavior beyond prose claims",
    "accessibility-guidance": "identify upstream accessibility assumptions and explicit supported behavior",
    "keyboard-focus-behavior": "understand non-pointer operation, focus ownership and restoration",
    "tokens-themes": "separate reusable semantics from the upstream visual system and theme vocabulary",
    "design-guidance": "understand why the system chooses a pattern, not merely how to import it",
    "api-guidance": "understand supported public mechanisms and lifecycle constraints",
    "gesture-interruption": "understand interruption, gesture ownership and retargeting under real input",
    "performance-guidance": "identify runtime cost, scaling limits and recommended performance boundaries",
    "icon-catalog": "inspect the actual symbol vocabulary available for product concepts",
    "symbol-conventions": "understand grid, stroke, weight, optical and family-consistency rules",
    "naming-tags": "verify semantic discoverability and concept coverage rather than choosing icons by appearance",
    "framework-delivery": "understand how symbols are delivered and customized without breaking consistency",
    "font-catalog": "inspect the actual type families/files rather than a screenshot or specimen alone",
    "script-coverage": "verify required languages/scripts and fallback behavior",
    "weights-axes": "verify available weights, styles and variable-font axes that support the intended hierarchy",
    "delivery-subsetting": "understand loading, subsetting and performance implications",
}


def required_artifact_classes(
    source_role: str,
    usage: str,
    visual_ambition: str = "polished",
    risk_class: str = "routine",
) -> set[str]:
    """Return evidence classes needed to let a source materially influence work."""
    required = set(BASE_ARTIFACTS.get(usage, set()))
    if usage in INFLUENTIAL_USAGE:
        required |= ROLE_ARTIFACTS.get(source_role, {"mechanism-bearing-evidence"})
    # Role evidence can satisfy the generic implementation/mechanism placeholder.
    if source_role in ROLE_ARTIFACTS:
        if "component-source" in required or any(k.endswith("-model") or k.endswith("-api") for k in required):
            required.discard("implementation")
        if len(required - {"readme", "license"}) >= 2:
            required.discard("mechanism-bearing-evidence")
    if visual_ambition in HIGH_AMBITION and source_role in {
        "animated-component-gallery", "component-distribution", "motion-engine", "3d-renderer",
        "3d-helper-library", "creative-canvas-gallery", "animation-asset-runtime",
    }:
        required.add("performance-guidance")
        required.add("accessibility-fallback")
    if risk_class in {"medical", "financial", "safety-critical", "privacy-sensitive", "security-sensitive"}:
        if source_role in {"headless-primitive", "design-system", "mobile-ui-system", "ai-ui-system"}:
            required.add("interaction-tests")
            required.add("accessibility-guidance")
    return required


def plan_source_research(source: dict[str, Any], task_profile: dict[str, Any], usage: str) -> dict[str, Any]:
    role = str(source.get("role", ""))
    ambition = str(task_profile.get("visual_ambition", "polished"))
    risk = str(task_profile.get("risk_class", "routine"))
    required = sorted(required_artifact_classes(role, usage, ambition, risk))
    snapshot_required = bool(source.get("verify_live_before_use")) or source.get("drift") in {"high", "very-high"} or usage in MATERIAL_USAGE
    obligations = [{"artifact_class": kind, "why": WHY.get(kind, f"inspect {kind} because it can materially change the source decision")} for kind in required]
    return {
        "source_id": source.get("id"),
        "source_role": role,
        "usage": usage,
        "snapshot_required": snapshot_required,
        "obligations": obligations,
        "stop_condition": "stop only when every material mechanism is tied to inspected evidence, contradictions/hazards are recorded, and unread material cannot plausibly overturn the current decision",
    }


def _artifact_kind_set(dossier: dict[str, Any]) -> set[str]:
    items = dossier.get("inspected_artifacts", []) if isinstance(dossier, dict) else []
    return {str(item.get("kind")) for item in items if isinstance(item, dict) and item.get("kind")}


def validate_source_research_dossier(dossier: dict[str, Any], source: dict[str, Any] | None = None) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(dossier, dict):
        return {"valid": False, "errors": ["source research dossier must be an object"], "artifact_class_count": 0, "mechanism_count": 0}
    usage = str(dossier.get("usage", ""))
    role = str(dossier.get("source_role") or (source or {}).get("role") or "")
    if usage not in {"adopt", "adapt", "inspire", "build", "reject"}:
        errors.append(f"invalid dossier usage {usage}")
    if not dossier.get("source_id"):
        errors.append("source research dossier requires source_id")
    snapshot = dossier.get("snapshot")
    snapshot = snapshot if isinstance(snapshot, dict) else {}
    if usage in INFLUENTIAL_USAGE:
        if not str(snapshot.get("canonical_url", "")).startswith("https://"):
            errors.append("influential source dossier requires canonical_url")
        if not snapshot.get("ref"):
            errors.append("influential source dossier requires snapshot ref")
        if not snapshot.get("retrieved_at"):
            errors.append("influential source dossier requires retrieved_at")
    source_data = source or {}
    snapshot_required = (
        usage in MATERIAL_USAGE
        or source_data.get("verify_live_before_use") is True
        or source_data.get("drift") in {"high", "very-high"}
    )
    if snapshot_required:
        commit = str(snapshot.get("commit_sha", ""))
        if len(commit) < 7:
            errors.append("material/high-drift source dossier requires pinned commit_sha")

    task_fit = dossier.get("task_fit")
    if usage in INFLUENTIAL_USAGE:
        if not isinstance(task_fit, dict) or task_fit.get("source_role_fit") is not True:
            errors.append("influential source dossier requires explicit source-role fit")
        else:
            for key in ("need", "why_this_source"):
                if not str(task_fit.get(key, "")).strip():
                    errors.append(f"source task_fit requires {key}")

    artifacts = dossier.get("inspected_artifacts")
    if not isinstance(artifacts, list) or not artifacts:
        artifacts = []
        errors.append("source research dossier requires inspected_artifacts")
    kinds = _artifact_kind_set(dossier)
    for index, item in enumerate(artifacts):
        if not isinstance(item, dict):
            errors.append(f"inspected artifact {index} must be an object")
            continue
        for field in ("kind", "path", "finding", "evidence_ref"):
            if not str(item.get(field, "")).strip():
                errors.append(f"inspected artifact {index} requires {field}")

    required = required_artifact_classes(role, usage, str(dossier.get("visual_ambition", "exceptional" if role == "animated-component-gallery" else "polished")), str(dossier.get("risk_class", "routine")))
    missing = sorted(required - kinds)
    for kind in missing:
        errors.append(f"source research dossier missing required artifact class: {kind}")
    if usage in INFLUENTIAL_USAGE and kinds and kinds.issubset({"readme", "license"}):
        errors.append("README-only source research cannot authorize material or visual influence")

    mechanisms = dossier.get("mechanisms")
    if usage in INFLUENTIAL_USAGE and (not isinstance(mechanisms, list) or not mechanisms):
        errors.append("influential source dossier requires extracted mechanisms")
        mechanisms = []
    mechanisms = mechanisms if isinstance(mechanisms, list) else []
    artifact_paths = {str(item.get("path")) for item in artifacts if isinstance(item, dict)}
    for index, mechanism in enumerate(mechanisms):
        if not isinstance(mechanism, dict):
            errors.append(f"mechanism {index} must be an object")
            continue
        for field in ("name", "transfer_boundary", "product_fit"):
            if not str(mechanism.get(field, "")).strip():
                errors.append(f"mechanism {index} requires {field}")
        evidence_paths = mechanism.get("evidence_artifact_paths")
        if not isinstance(evidence_paths, list) or not evidence_paths:
            errors.append(f"mechanism {index} requires evidence_artifact_paths")
        else:
            unknown = sorted(set(map(str, evidence_paths)) - artifact_paths)
            if unknown:
                errors.append(f"mechanism {index} cites uninspected artifact paths: {unknown}")

    if usage in MATERIAL_USAGE:
        license_data = dossier.get("license")
        if not isinstance(license_data, dict) or not license_data.get("evidence_refs"):
            errors.append("material source dossier requires license evidence")
        for field in ("accessibility", "performance"):
            section = dossier.get(field)
            if not isinstance(section, dict) or not section.get("evidence_refs"):
                errors.append(f"material source dossier requires {field} evidence or explicit limitation")

    if usage in INFLUENTIAL_USAGE and not str(dossier.get("stop_reason", "")).strip():
        errors.append("influential source dossier requires explicit stop_reason")
    if usage in INFLUENTIAL_USAGE and not isinstance(dossier.get("unread_material"), list):
        errors.append("influential source dossier requires unread_material list, even when empty")

    return {
        "valid": not errors,
        "errors": errors,
        "required_artifact_classes": sorted(required),
        "artifact_class_count": len(kinds),
        "mechanism_count": len(mechanisms),
    }


def validate_source_mix(record: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(record, dict):
        return {"valid": False, "errors": ["source mix must be an object"]}
    sources = record.get("sources")
    if not isinstance(sources, list):
        sources = []
        errors.append("source mix requires sources")
    ambition = str(record.get("visual_ambition", "polished"))
    if record.get("source_required") and not sources:
        errors.append("source-required work requires at least one researched source")
    roles = [str(s.get("role")) for s in sources if isinstance(s, dict) and s.get("role")]
    if ambition in {"exceptional", "experiential"} and len(sources) >= 2:
        counts = Counter(roles)
        if len(counts) == 1 and not str(record.get("monoculture_justification", "")).strip():
            errors.append("exceptional source research cannot use a single-role source monoculture without a product-specific justification")
        total_weight = sum(float(s.get("influence", 1.0)) for s in sources if isinstance(s, dict)) or 1.0
        role_weight: Counter[str] = Counter()
        for s in sources:
            if isinstance(s, dict) and s.get("role"):
                role_weight[str(s["role"])] += float(s.get("influence", 1.0))
        if role_weight and max(role_weight.values()) / total_weight > 0.8 and not str(record.get("dominance_justification", "")).strip():
            errors.append("one source role dominates more than 80% of declared influence without justification")
    return {"valid": not errors, "errors": errors, "source_count": len(sources), "role_count": len(set(roles))}


def validate_cross_source_synthesis(record: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(record, dict):
        return {"valid": False, "errors": ["cross-source synthesis must be an object"]}
    sources = record.get("sources")
    if not isinstance(sources, list) or not sources:
        errors.append("cross-source synthesis requires sources")
        sources = []
    layers = record.get("layers")
    if not isinstance(layers, dict) or not layers:
        errors.append("cross-source synthesis requires layer ownership")
        layers = {}
    if len(sources) > 1:
        required_layers = {"semantics", "interaction", "visual"}
        missing_layers = sorted(required_layers - set(layers))
        if missing_layers:
            errors.append(f"multi-source synthesis requires local ownership decisions for layers: {missing_layers}")
    for name, spec in layers.items():
        if not isinstance(spec, dict) or not str(spec.get("owner", "")).strip():
            errors.append(f"synthesis layer {name} requires owner")
            continue
        owner = spec.get("owner")
        if owner != "local" and owner not in sources:
            errors.append(f"synthesis layer {name} owner {owner} is not a declared source or local")
        if len(sources) > 1 and not str(spec.get("local_override", "")).strip():
            errors.append(f"synthesis layer {name} requires local_override defining product-system authority")
    conflicts = record.get("conflicts")
    if len(sources) > 1:
        if not isinstance(conflicts, list):
            errors.append("multi-source synthesis requires conflicts list, even when empty")
            conflicts = []
        for index, conflict in enumerate(conflicts):
            if not isinstance(conflict, dict) or not str(conflict.get("dimension", "")).strip():
                errors.append(f"synthesis conflict {index} requires dimension")
            elif not str(conflict.get("resolution", "")).strip():
                errors.append(f"synthesis conflict {index} requires explicit resolution")
    local = record.get("local_system")
    if len(sources) > 1:
        required_local = {"tokens", "actions", "states", "accessibility"}
        if not isinstance(local, dict):
            errors.append("multi-source synthesis requires local_system authority")
        else:
            missing_local = sorted(k for k in required_local if not str(local.get(k, "")).strip())
            if missing_local:
                errors.append(f"local_system missing authorities: {missing_local}")
        removed = record.get("foreign_defaults_removed")
        if not isinstance(removed, list) or not removed:
            errors.append("multi-source synthesis requires foreign_defaults_removed evidence")
    return {"valid": not errors, "errors": errors, "source_count": len(sources), "layer_count": len(layers)}


__all__ = [
    "required_artifact_classes", "plan_source_research", "validate_source_research_dossier",
    "validate_source_mix", "validate_cross_source_synthesis", "ROLE_ARTIFACTS",
]

VALID_SOURCE_TIERS = {"anchor", "specialist", "discovery"}

REQUIRED_ANCHOR_ROLES = {
    "animated-component-gallery",
    "icon-system",
    "design-token-tool",
    "design-system",
    "accessibility-testing-tool",
    "diagram-graph-ui",
    "visual-testing-tool",
    "typography-source",
}


def validate_source_intelligence_registry(registry: dict[str, Any]) -> dict[str, Any]:
    """Validate the v6 source registry without turning source count into authority."""
    errors: list[str] = []
    if not isinstance(registry, dict):
        return {"valid": False, "errors": ["source intelligence registry must be an object"], "source_count": 0, "domains": []}
    if registry.get("version") != 6:
        errors.append("source intelligence registry version must be 6")
    sources = registry.get("sources")
    if not isinstance(sources, list) or not sources:
        sources = []
        errors.append("source intelligence registry requires sources")
    seen_ids: set[str] = set()
    seen_urls: set[str] = set()
    domains: set[str] = set()
    roles: set[str] = set()
    for index, source in enumerate(sources):
        if not isinstance(source, dict):
            errors.append(f"source {index} must be an object")
            continue
        sid = str(source.get("id", "")).strip()
        url = str(source.get("url", "")).strip()
        role = str(source.get("role", "")).strip()
        if not sid:
            errors.append(f"source {index} requires id")
        elif sid in seen_ids:
            errors.append(f"duplicate source id: {sid}")
        seen_ids.add(sid)
        if not url.startswith("https://"):
            errors.append(f"source {sid or index} requires canonical https url")
        elif url in seen_urls:
            errors.append(f"duplicate source url: {url}")
        seen_urls.add(url)
        tier = source.get("tier")
        if tier not in VALID_SOURCE_TIERS:
            errors.append(f"source {sid or index} has invalid tier {tier}")
        if not role:
            errors.append(f"source {sid or index} requires role")
        roles.add(role)
        for field in ("domains", "capabilities", "stacks", "mechanism_families"):
            value = source.get(field)
            if not isinstance(value, list) or not value:
                errors.append(f"source {sid or index} requires non-empty {field}")
        domains.update(map(str, source.get("domains", []) if isinstance(source.get("domains"), list) else []))
        if source.get("drift") not in {"low", "medium", "high", "very-high"}:
            errors.append(f"source {sid or index} requires valid drift")
        license_data = source.get("license")
        if not isinstance(license_data, dict) or not license_data.get("status"):
            errors.append(f"source {sid or index} requires license status")
        research_map = source.get("research_map")
        if not isinstance(research_map, dict):
            errors.append(f"source {sid or index} requires research_map")
        else:
            for key in ("required_for_inspire", "required_for_adapt", "questions"):
                if not isinstance(research_map.get(key), list) or not research_map.get(key):
                    errors.append(f"source {sid or index} research_map requires non-empty {key}")
        boundary = source.get("adaptation_boundary")
        if not isinstance(boundary, dict):
            errors.append(f"source {sid or index} requires adaptation_boundary")
        else:
            for key in ("may_transfer", "must_reconcile", "must_not_assume"):
                if not isinstance(boundary.get(key), list) or not boundary.get(key):
                    errors.append(f"source {sid or index} adaptation_boundary requires non-empty {key}")
        provenance = source.get("provenance")
        if not isinstance(provenance, dict) or not provenance.get("verified_at"):
            errors.append(f"source {sid or index} requires provenance verified_at")
            provenance = provenance if isinstance(provenance, dict) else {}
        if tier == "anchor":
            artifacts = provenance.get("inspected_artifacts")
            if not isinstance(artifacts, list) or len(artifacts) < 3 or not all(isinstance(a, dict) and a.get("path") and a.get("finding") for a in artifacts):
                errors.append(f"anchor source {sid or index} requires artifact-level provenance with at least three inspected artifacts")
            if not provenance.get("snapshot_ref"):
                errors.append(f"anchor source {sid or index} requires provenance snapshot_ref")
        if tier in {"specialist", "discovery"} and source.get("live_verification_required") is not True:
            errors.append(f"non-anchor source {sid or index} must require live verification before material influence")
    anchor_roles = {str(s.get("role")) for s in sources if isinstance(s, dict) and s.get("tier") == "anchor"}
    missing_anchor_roles = sorted(REQUIRED_ANCHOR_ROLES - anchor_roles)
    if missing_anchor_roles:
        errors.append(f"source intelligence anchor role coverage missing: {missing_anchor_roles}")
    if sum(1 for s in sources if isinstance(s, dict) and s.get("tier") == "anchor") < len(REQUIRED_ANCHOR_ROLES):
        errors.append(f"source intelligence requires at least {len(REQUIRED_ANCHOR_ROLES)} artifact-level anchors")
    return {
        "valid": not errors,
        "errors": errors,
        "source_count": len(sources),
        "domains": sorted(domains),
        "roles": sorted(roles),
        "anchor_count": sum(1 for s in sources if isinstance(s, dict) and s.get("tier") == "anchor"),
    }


def mandatory_v6_source_routes(profile: dict[str, Any]) -> set[str]:
    """Return v6 source-intelligence owners that cannot be skipped by routing."""
    if not isinstance(profile, dict):
        return set()
    routes: set[str] = set()
    usage = str(profile.get("external_source_usage", ""))
    count = int(profile.get("external_source_count", 0) or 0)
    material = usage in INFLUENTIAL_USAGE or profile.get("external_sources_material") is True
    if material:
        routes |= {"performing-ui-repository-archaeology", "auditing-ui-research-depth"}
    if material and count > 1:
        routes.add("synthesizing-cross-source-ui-language")
    if profile.get("skill_effect_evaluation") is True or profile.get("causal_skill_benchmark") is True:
        routes.add("benchmarking-ui-skill-effect")
    return routes
