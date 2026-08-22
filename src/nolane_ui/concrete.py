"""NUI v7 concrete design knowledge and immediate synthesis.

This module intentionally stores narrow decision cards rather than a giant
style cookbook. Cards preserve provenance, contraindications, and validation
obligations so fast recommendations do not become untraceable defaults.

V12.1 additionally binds material UI fast-path generation to an evaluated
external reference-execution contract and carries a prompt-ready directive so
host/coding agents cannot silently drop the active reference capsule.
Historical non-material callers remain backward compatible.
"""
from __future__ import annotations

from typing import Any


def validate_pattern_kb(kb: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(kb, dict) or kb.get("version") != 7:
        return {"valid": False, "errors": ["concrete pattern knowledge must be version 7"], "pattern_count": 0, "domain_count": 0}
    patterns = kb.get("patterns")
    if not isinstance(patterns, list) or not patterns:
        return {"valid": False, "errors": ["concrete pattern knowledge requires patterns[]"], "pattern_count": 0, "domain_count": 0}
    ids: set[str] = set(); domains: set[str] = set()
    for i, card in enumerate(patterns):
        if not isinstance(card, dict): errors.append(f"pattern {i} must be object"); continue
        pid = str(card.get("id", ""))
        if not pid or pid in ids: errors.append(f"pattern {i} requires unique id")
        ids.add(pid)
        for field in ("problem", "decision", "rationale", "source_refs", "contraindications", "validation", "transfer_boundary", "domains", "dimensions"):
            value = card.get(field)
            if field in {"source_refs", "contraindications", "validation", "domains", "dimensions"}:
                if not isinstance(value, list) or not value: errors.append(f"pattern {pid} requires non-empty {field}")
            elif not value:
                errors.append(f"pattern {pid} requires {field}")
        domains.update(str(d) for d in card.get("domains", []))
        if not all(isinstance(r, dict) and r.get("source_id") and r.get("url") and r.get("claim") for r in card.get("source_refs", [])):
            errors.append(f"pattern {pid} source_refs require source_id, url and claim")
        if not isinstance(card.get("priority"), int) or not 1 <= card.get("priority", 0) <= 100:
            errors.append(f"pattern {pid} priority must be 1..100")
    return {"valid": not errors, "errors": errors, "pattern_count": len(patterns), "domain_count": len(domains), "domains": sorted(domains)}


def _tokens(profile: dict[str, Any]) -> set[str]:
    values: list[str] = []
    for key in ("task", "domain", "platform", "stack", "risk_class", "visual_ambition"):
        values.append(str(profile.get(key, "")))
    for key in ("roles", "user_needs", "requirements", "decision_dimensions"):
        v = profile.get(key, [])
        if isinstance(v, list): values.extend(map(str, v))
    text = " ".join(values).lower().replace("/", " ").replace("-", " ")
    return {t for t in text.split() if len(t) > 2}


def _eligible(card: dict[str, Any], profile: dict[str, Any]) -> bool:
    platform = str(profile.get("platform", "")).lower()
    required_platforms = [str(x).lower() for x in card.get("platforms", [])]
    if required_platforms and platform not in required_platforms:
        return False
    if card.get("requires_ai") is True and profile.get("ai_experience") is not True:
        return False
    if card.get("shopify_only") is True and platform not in {"shopify", "shopify-admin", "shopify-app", "shopify-extension"}:
        return False
    return True


def _score(card: dict[str, Any], profile: dict[str, Any], tokens: set[str]) -> int:
    score = int(card.get("priority", 50))
    domain = str(profile.get("domain", "generic")).lower()
    domains = [str(x).lower() for x in card.get("domains", [])]
    if domain in domains: score += 45
    elif "generic" in domains: score += 18
    dims = {str(x) for x in profile.get("decision_dimensions", []) if isinstance(profile.get("decision_dimensions"), list)}
    score += 12 * len(dims.intersection(set(card.get("dimensions", []))))
    tags = {str(x).lower() for x in card.get("tags", [])}
    score += min(24, 4 * len(tags.intersection(tokens)))
    platform = str(profile.get("platform", "")).lower()
    if platform and platform in [str(x).lower() for x in card.get("platforms", [])]: score += 55
    if profile.get("visual_ambition") in {"flagship", "exceptional", "experiential"} and "high-ambition" in tags: score += 25
    return score


def _reference_generation_blockers(profile: dict[str, Any], contract: dict[str, Any] | None) -> list[str]:
    """Check V12.1 facts locally without re-running the routing algorithm."""
    if profile.get("material_ui") is not True:
        return []
    if not isinstance(contract, dict):
        return ["missing V12.1 reference execution contract for material UI generation"]

    from .external_ui_execution import task_profile_fingerprint

    errors: list[str] = []
    if contract.get("routing_evaluated") is not True:
        errors.append("V12.1 reference routing was not explicitly evaluated")
    if contract.get("task_fingerprint") != task_profile_fingerprint(profile):
        errors.append("V12.1 reference execution fingerprint does not match the current material UI task")
    posture = contract.get("posture")
    if posture not in {"ACTIVE", "EVALUATED_NO_MATCH"}:
        errors.append("V12.1 material UI reference posture must be ACTIVE or EVALUATED_NO_MATCH")
    required = [str(item) for item in contract.get("required_pack_ids", [])]
    resolved = contract.get("resolved_packs", [])
    resolved_ids = {
        str(item.get("pack_id")) for item in resolved
        if isinstance(item, dict) and item.get("pack_id")
    } if isinstance(resolved, list) else set()
    missing = [pack_id for pack_id in required if pack_id not in resolved_ids]
    if missing:
        errors.append(f"V12.1 reference execution dropped required packs before generation: {missing}")
    if posture == "ACTIVE":
        if not required:
            errors.append("V12.1 ACTIVE reference execution requires at least one task-shaped pack")
        if not contract.get("must_preserve_source_ids"):
            errors.append("V12.1 ACTIVE reference execution requires persistent source ids")
    if posture == "EVALUATED_NO_MATCH" and not str(contract.get("no_match_reason", "")).strip():
        errors.append("V12.1 EVALUATED_NO_MATCH requires an explicit reason")
    return errors


def _reference_generation_directive(profile: dict[str, Any], contract: dict[str, Any] | None) -> str:
    if profile.get("material_ui") is not True or not isinstance(contract, dict):
        return ""
    from .external_ui_execution import build_reference_generation_directive
    return build_reference_generation_directive(contract)


def compile_concrete_design_packet(
    profile: dict[str, Any],
    authority_result: dict[str, Any],
    pattern_kb: dict[str, Any],
    grammar: dict[str, Any],
    reference_execution_contract: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Compile a bounded fast-path packet from source-bound concrete cards."""
    reference_directive = _reference_generation_directive(profile, reference_execution_contract)
    kb_validation = validate_pattern_kb(pattern_kb)
    if not kb_validation["valid"]:
        return {
            "status": "BLOCKED",
            "errors": kb_validation["errors"],
            "task_thesis": "",
            "authority_stack": [],
            "decisions": [],
            "implementation_shortcuts": [],
            "validation_obligations": [],
            "unresolved_blockers": ["invalid pattern knowledge"],
            "material_ui": profile.get("material_ui") is True,
            "reference_execution": reference_execution_contract,
            "reference_generation_directive": reference_directive,
        }
    tokens = _tokens(profile)
    ranked = []
    for card in pattern_kb["patterns"]:
        if _eligible(card, profile):
            ranked.append((_score(card, profile, tokens), card["id"], card))
    ranked.sort(key=lambda x: (-x[0], x[1]))
    min_decisions = int(grammar.get("decision_budget", {}).get("min", 5))
    max_decisions = int(grammar.get("decision_budget", {}).get("max", 9))
    selected = [r[2] for r in ranked[:max_decisions]]
    if len(selected) < min_decisions:
        used = {c["id"] for c in selected}
        for _, _, card in ranked:
            if card["id"] in used: continue
            selected.append(card); used.add(card["id"])
            if len(selected) >= min_decisions: break

    decisions = []
    validations: list[str] = []
    for card in selected:
        primary_source = card["source_refs"][0]
        decisions.append({
            "pattern_id": card["id"],
            "decision": card["decision"],
            "rationale": card["rationale"],
            "decision_type": card.get("decision_type", "pattern"),
            "source_id": primary_source["source_id"],
            "provenance": card["source_refs"],
            "contraindications": card["contraindications"],
            "transfer_boundary": card["transfer_boundary"],
        })
        for v in card["validation"]:
            if v not in validations: validations.append(v)

    primary = authority_result.get("primary", {}) if isinstance(authority_result, dict) else {}
    authority_stack = [
        {"dimension": dim, "source_id": data.get("source_id"), "url": data.get("url"), "scope": data.get("scope")}
        for dim, data in primary.items()
    ]
    unresolved = [f"unresolved authority dimension: {x}" for x in authority_result.get("unresolved_dimensions", [])] if isinstance(authority_result, dict) else ["authority resolution unavailable"]
    unresolved.extend(_reference_generation_blockers(profile, reference_execution_contract))
    shortcuts: list[str] = []
    for rule in grammar.get("implementation_shortcuts", []):
        if not isinstance(rule, dict): continue
        when = rule.get("when", {})
        matches = True
        for key, accepted in when.items():
            accepted = accepted if isinstance(accepted, list) else [accepted]
            if str(profile.get(key, "")).lower() not in {str(x).lower() for x in accepted}:
                matches = False; break
        if matches and rule.get("instruction"):
            shortcuts.append(str(rule["instruction"]))
    if not shortcuts:
        shortcuts.append("Prefer an existing behaviorally-correct primitive or local component path before inventing a new interaction contract; keep visual adaptation separate from semantics.")

    thesis = str(profile.get("task", "")).strip() or f"Design a {profile.get('domain','product')} interface that preserves task, domain, platform and evidence constraints."
    return {
        "status": "READY" if not unresolved and len(decisions) >= min_decisions else "NEEDS_RESEARCH",
        "task_thesis": thesis,
        "authority_stack": authority_stack,
        "decisions": decisions,
        "implementation_shortcuts": shortcuts[:5],
        "validation_obligations": validations[:16],
        "unresolved_blockers": unresolved,
        "compression_rule": "fast path may compress explanation, never hard obligations, provenance, contraindications, unresolved authority, the V12.1 reference execution contract, or its prompt-ready generation directive",
        "material_ui": profile.get("material_ui") is True,
        "reference_execution": reference_execution_contract,
        "reference_generation_directive": reference_directive,
    }


def validate_concrete_design_packet(packet: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(packet, dict): return {"valid": False, "errors": ["concrete design packet must be object"]}
    if packet.get("status") not in {"READY", "NEEDS_RESEARCH", "BLOCKED"}: errors.append("packet requires valid status")
    for field in ("task_thesis", "authority_stack", "decisions", "implementation_shortcuts", "validation_obligations", "unresolved_blockers"):
        if field not in packet: errors.append(f"packet requires {field}")
    decisions = packet.get("decisions", [])
    if not isinstance(decisions, list): errors.append("packet decisions must be list"); decisions=[]
    if len(decisions) > 9: errors.append("immediate concrete packet must contain at most nine decisions")
    for i, d in enumerate(decisions):
        if not isinstance(d, dict): errors.append(f"decision {i} must be object"); continue
        for field in ("pattern_id", "decision", "rationale", "provenance", "contraindications", "transfer_boundary"):
            if not d.get(field): errors.append(f"decision {i} requires {field}")
    if packet.get("material_ui") is True:
        refs = packet.get("reference_execution")
        if not isinstance(refs, dict) or refs.get("posture") not in {"ACTIVE", "EVALUATED_NO_MATCH"}:
            errors.append("material concrete packet requires V12.1 reference execution")
        directive = packet.get("reference_generation_directive")
        if not isinstance(directive, str) or not directive.strip():
            errors.append("material concrete packet requires prompt-ready V12.1 reference generation directive")
        else:
            if "REFERENCE EXECUTION:" not in directive or "DO NOT DROP" not in directive:
                errors.append("material concrete packet reference directive is incomplete")
    if packet.get("status") == "READY" and packet.get("unresolved_blockers"):
        errors.append("READY packet cannot contain unresolved blockers")
    return {"valid": not errors, "errors": errors}


__all__ = ["compile_concrete_design_packet", "validate_pattern_kb", "validate_concrete_design_packet"]
