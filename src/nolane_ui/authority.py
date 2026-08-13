"""NUI v7 decision-dimensional UI authority routing.

Authority is not a global prestige score. A source can be primary for one
question (for example keyboard/focus semantics) and only inspirational for
another (for example art direction). The resolver keeps those dimensions
separate and applies narrow context boosts rather than promoting one source to
universal authority.
"""
from __future__ import annotations

from collections import defaultdict
from typing import Any

SEMANTIC_DIMENSIONS = {
    "component-semantics", "accessibility-testing", "service-journey",
    "enterprise-workflow", "commerce-workflow", "platform-convention",
}
VISUAL_ONLY_KINDS = {"visual-inspiration", "animated-gallery"}
VALID_STRENGTHS = {"primary", "strong", "supporting", "inspiration", "adapter"}
STRENGTH_SCORE = {"primary": 100, "strong": 80, "supporting": 60, "inspiration": 35, "adapter": 20}


def _list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [str(v) for v in value]
    return []


def mandatory_v7_routes(profile: dict[str, Any]) -> set[str]:
    """Return v7 owners that are non-optional for concrete authority/craft work."""
    if not isinstance(profile, dict):
        return set()
    routes: set[str] = set()
    if profile.get("external_authority_used") or profile.get("authority_sensitive_decisions"):
        routes.add("routing-to-ui-authorities")
    if profile.get("institutional_knowledge_material"):
        routes |= {"routing-to-ui-authorities", "adapting-institutional-design-knowledge"}
    if profile.get("implementation_shortcut_used") or profile.get("external_implementation_authorities"):
        routes |= {"routing-to-ui-authorities", "orchestrating-implementation-authorities"}
    if profile.get("agent_readable_adapter_used"):
        routes |= {"routing-to-ui-authorities", "building-agent-readable-ui-context"}
    if profile.get("fast_path") or profile.get("concrete_packet_required"):
        routes |= {"routing-to-ui-authorities", "compiling-concrete-design-packets"}
    if profile.get("execution_brief_required"):
        routes.add("compressing-ui-decisions-for-execution")
    ambition = str(profile.get("visual_ambition", "")).strip().lower()
    if ambition in {"flagship", "exceptional", "experiential"}:
        routes |= {"validating-rendered-perception", "designing-domain-native-signatures"}
    return routes


def validate_authority_mesh(mesh: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(mesh, dict):
        return {"valid": False, "errors": ["authority mesh must be an object"], "authority_count": 0, "dimension_count": 0}
    if mesh.get("version") != 7:
        errors.append("authority mesh version must be 7")
    authorities = mesh.get("authorities")
    if not isinstance(authorities, list) or not authorities:
        return {"valid": False, "errors": errors + ["authority mesh requires authorities[]"], "authority_count": 0, "dimension_count": 0}
    ids: set[str] = set()
    dimensions: set[str] = set()
    for index, item in enumerate(authorities):
        if not isinstance(item, dict):
            errors.append(f"authority {index} must be an object")
            continue
        sid = str(item.get("source_id", "")).strip()
        if not sid:
            errors.append(f"authority {index} requires source_id")
        elif sid in ids:
            errors.append(f"duplicate authority source_id {sid}")
        ids.add(sid)
        if not str(item.get("url", "")).startswith("https://"):
            errors.append(f"authority {sid or index} requires canonical https url")
        if not item.get("verified_at"):
            errors.append(f"authority {sid or index} requires verified_at")
        dims = item.get("authority_dimensions")
        if not isinstance(dims, list) or not dims:
            errors.append(f"authority {sid or index} requires authority_dimensions")
            continue
        for d in dims:
            if not isinstance(d, dict):
                errors.append(f"authority {sid or index} dimension must be object")
                continue
            dim = str(d.get("dimension", "")).strip()
            strength = d.get("strength")
            if not dim:
                errors.append(f"authority {sid or index} dimension requires name")
            else:
                dimensions.add(dim)
            if strength not in VALID_STRENGTHS:
                errors.append(f"authority {sid or index}/{dim} invalid strength {strength}")
            if not d.get("scope") or not d.get("basis"):
                errors.append(f"authority {sid or index}/{dim} requires scope and basis")
        if not isinstance(item.get("transfer_boundary"), dict):
            errors.append(f"authority {sid or index} requires transfer_boundary")
    return {
        "valid": not errors,
        "errors": errors,
        "authority_count": len(authorities),
        "dimension_count": len(dimensions),
        "dimensions": sorted(dimensions),
    }


def _context_score(item: dict[str, Any], dimension: str, profile: dict[str, Any], base: int) -> tuple[int, list[str]]:
    score = base
    reasons: list[str] = []
    sid = str(item.get("source_id"))
    platform = str(profile.get("platform", "")).lower()
    domain = str(profile.get("domain", "")).lower()
    jurisdiction = str(profile.get("jurisdiction", "")).lower()
    stack = str(profile.get("stack", "")).lower()
    ambition = str(profile.get("visual_ambition", "")).lower()

    # Narrow applicability boosts. These do not change the authority dimension.
    if sid == "apple-hig" and platform in {"ios", "ipados", "macos", "watchos", "tvos", "visionos", "apple"}:
        score += 70; reasons.append("target is an Apple platform")
    if sid == "govuk-design-system" and (domain == "public-service" or jurisdiction in {"uk", "gb", "united-kingdom"}):
        score += 45; reasons.append("public-service / UK service context")
    if sid == "uswds" and (domain == "public-service" or jurisdiction in {"us", "usa", "united-states"}):
        score += 40; reasons.append("public-service / US accessibility-service context")
    if sid in {"react-aria", "radix-primitives"} and stack in {"react", "nextjs", "next.js", "web", "typescript", "javascript", ""}:
        score += 20; reasons.append("web component behavior fit")
    if sid in {"sap-fiori", "ant-design", "carbon"} and domain in {"enterprise", "enterprise-operations", "b2b", "business-software"}:
        score += 35; reasons.append("enterprise workflow context")
    if sid == "shopify-polaris":
        if platform in {"shopify", "shopify-admin", "shopify-app", "shopify-extension"}:
            score += 80; reasons.append("Shopify-native surface")
        else:
            score -= 120; reasons.append("Shopify-specific authority not generalized")
    if sid == "atlassian-rovo" and (domain in {"ai-collaboration", "enterprise-collaboration"} or profile.get("ai_experience") is True):
        score += 45; reasons.append("AI collaboration experience")
    if sid in {"react-bits", "magic-ui", "aceternity"} and ambition in {"flagship", "exceptional", "experiential"}:
        score += 35; reasons.append("high visual ambition")
    if sid in {"motion", "gsap"} and (profile.get("motion_material") is True or dimension == "motion-system"):
        score += 35; reasons.append("motion is material")
    if dimension == "agent-readable-access" and item.get("access_modes"):
        score += 30; reasons.append("machine-readable access available")
    return score, reasons


def resolve_authorities(profile: dict[str, Any], mesh: dict[str, Any]) -> dict[str, Any]:
    """Resolve primary/corroborating authority per requested decision dimension."""
    validation = validate_authority_mesh(mesh)
    if not validation["valid"]:
        return {"status": "BLOCKED", "errors": validation["errors"], "primary": {}, "corroborating": {}}
    requested = _list(profile.get("decision_dimensions"))
    if not requested:
        requested = _list(mesh.get("default_dimensions"))
    candidates: dict[str, list[tuple[int, str, dict[str, Any], dict[str, Any], list[str]]]] = defaultdict(list)
    for item in mesh["authorities"]:
        for dim in item["authority_dimensions"]:
            name = dim["dimension"]
            if requested and name not in requested:
                continue
            base = STRENGTH_SCORE[dim["strength"]]
            score, contextual = _context_score(item, name, profile, base)
            # Visual-only authorities cannot become primary semantic authorities.
            if name in SEMANTIC_DIMENSIONS and item.get("kind") in VISUAL_ONLY_KINDS:
                score -= 200
            candidates[name].append((score, str(item["source_id"]), item, dim, contextual))

    primary: dict[str, Any] = {}
    corroborating: dict[str, list[dict[str, Any]]] = {}
    unresolved: list[str] = []
    for dimension in requested:
        ranked = sorted(candidates.get(dimension, []), key=lambda x: (-x[0], x[1]))
        ranked = [r for r in ranked if r[0] > 0]
        if not ranked:
            unresolved.append(dimension)
            continue
        score, sid, item, dim, contextual = ranked[0]
        primary[dimension] = {
            "source_id": sid,
            "name": item["name"],
            "url": item["url"],
            "strength": dim["strength"],
            "scope": dim["scope"],
            "basis": dim["basis"],
            "score": score,
            "context_reasons": contextual,
            "live_verification_required": bool(item.get("live_verification_required")),
        }
        corroborating[dimension] = [
            {"source_id": r[1], "name": r[2]["name"], "score": r[0], "strength": r[3]["strength"]}
            for r in ranked[1:4]
        ]
    return {
        "status": "PASS" if not unresolved else "PARTIAL",
        "primary": primary,
        "corroborating": corroborating,
        "unresolved_dimensions": unresolved,
        "authority_rule": "authority is decision-dimensional; adapters and visual inspiration do not inherit semantic authority",
    }


def validate_authority_route_plan(plan: dict[str, Any], mesh: dict[str, Any] | None = None) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(plan, dict):
        return {"valid": False, "errors": ["authority route plan must be an object"]}
    decisions = plan.get("decisions")
    if not isinstance(decisions, list) or not decisions:
        errors.append("authority route plan requires decisions[]")
        decisions = []
    source_map = {}
    if mesh and isinstance(mesh, dict):
        source_map = {str(a.get("source_id")): a for a in mesh.get("authorities", []) if isinstance(a, dict)}
    for i, decision in enumerate(decisions):
        if not isinstance(decision, dict):
            errors.append(f"authority decision {i} must be an object"); continue
        dimension = str(decision.get("dimension", ""))
        sid = str(decision.get("source_id", ""))
        role = str(decision.get("role", ""))
        if not dimension or not sid or not decision.get("reason"):
            errors.append(f"authority decision {i} requires dimension, source_id and reason")
            continue
        if dimension in SEMANTIC_DIMENSIONS and role in {"visual-inspiration", "animated-gallery"}:
            errors.append(f"semantic authority dimension {dimension} cannot be assigned to visual inspiration role {sid}")
        source = source_map.get(sid)
        if source and dimension in SEMANTIC_DIMENSIONS and source.get("kind") in VISUAL_ONLY_KINDS:
            errors.append(f"authority smear: {sid} is visual-only for semantic dimension {dimension}")
        if source and not any(d.get("dimension") == dimension for d in source.get("authority_dimensions", [])):
            errors.append(f"source {sid} does not declare authority for {dimension}")
    return {"valid": not errors, "errors": errors}


def validate_agent_adapters(adapters: dict[str, Any]) -> dict[str, Any]:
    """Validate machine-readable access metadata without granting authority by protocol."""
    errors: list[str] = []
    if not isinstance(adapters, dict) or adapters.get("version") != 7:
        return {"valid": False, "errors": ["agent adapter registry must be version 7"], "adapter_count": 0}
    items = adapters.get("adapters")
    if not isinstance(items, list) or not items:
        return {"valid": False, "errors": ["agent adapter registry requires adapters[]"], "adapter_count": 0}
    seen: set[str] = set()
    for i, item in enumerate(items):
        if not isinstance(item, dict):
            errors.append(f"adapter {i} must be object"); continue
        aid = str(item.get("id", ""))
        if not aid or aid in seen:
            errors.append(f"adapter {i} requires unique id")
        seen.add(aid)
        if item.get("access_mode") not in {"mcp", "llms-txt", "agent-skill", "open-code", "ai-toolkit", "structured-docs"}:
            errors.append(f"adapter {aid} has unsupported access_mode")
        if item.get("authority_escalation") is not False:
            errors.append(f"adapter {aid} must explicitly forbid authority escalation")
        if not str(item.get("url", "")).startswith("https://"):
            errors.append(f"adapter {aid} requires canonical https url")
        if not item.get("underlying_authority"):
            errors.append(f"adapter {aid} requires underlying_authority")
        if item.get("live_verification_required") is not True:
            errors.append(f"adapter {aid} must require live verification")
    return {"valid": not errors, "errors": errors, "adapter_count": len(items)}


__all__ = [
    "resolve_authorities", "validate_authority_mesh", "validate_authority_route_plan",
    "validate_agent_adapters", "mandatory_v7_routes", "SEMANTIC_DIMENSIONS",
]
