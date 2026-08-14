"""NUI v9 product-completeness, taste, rendered-critique and fidelity gates.

The module deliberately validates evidence structure rather than pretending that
repository-only code can decide whether a product is universally beautiful or
complete. Its purpose is to make common AI omissions falsifiable: under-scoped
product envelopes, settings/account lifecycle gaps, accidental browser chrome,
single-candidate "taste", spec-only visual critique, domain/audience mismatch,
and design intent that never survives implementation.
"""
from __future__ import annotations

from collections import Counter
from typing import Any


DISPOSITIONS = {"REQUIRED", "EXPECTED", "OPTIONAL", "EXCLUDED", "UNKNOWN"}
HIGH_AMBITION = {"production", "full-platform", "platform", "flagship", "enterprise"}
RESIDUE_TREATMENTS = {
    "native-intentional",
    "styled",
    "overlay",
    "reveal-on-interaction",
    "hidden-with-alternative",
    "custom-system",
}


def _object(value: Any, name: str) -> tuple[dict[str, Any], list[str]]:
    if not isinstance(value, dict):
        return {}, [f"{name} must be an object"]
    return value, []


def _nonempty_list(value: Any, name: str, errors: list[str]) -> list[Any]:
    if not isinstance(value, list) or not value:
        errors.append(f"{name} must be a non-empty list")
        return []
    return value


def _text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate_capability_envelope(record: dict[str, Any]) -> dict[str, Any]:
    """Validate discovery breadth and explicit capability disposition.

    This is intentionally upstream of the existing functional-closure graph.
    Closure proves that known capabilities are represented and reachable; this
    gate asks whether the known set was broad enough for the claimed product.
    """

    record, errors = _object(record, "capability envelope")
    product_class = record.get("product_class")
    ambition = str(record.get("ambition", "")).strip().lower()
    if not _text(product_class):
        errors.append("capability envelope requires product_class")
    if not ambition:
        errors.append("capability envelope requires ambition")

    actors = _nonempty_list(record.get("actors"), "capability envelope actors", errors)
    if actors and any(not _text(actor) for actor in actors):
        errors.append("capability envelope actors must be named strings")

    expected = _nonempty_list(
        record.get("expected_capability_families"),
        "expected capability families",
        errors,
    )
    expected_families = {str(x).strip() for x in expected if _text(x)}
    if len(expected_families) != len(expected):
        errors.append("expected capability families must be unique non-empty strings")
    if ambition in HIGH_AMBITION and len(expected_families) < 6:
        errors.append("high-ambition product envelope is too narrow to support a full-product claim")

    capabilities_value = record.get("capabilities")
    if not isinstance(capabilities_value, list) or not capabilities_value:
        errors.append("capability envelope requires discovered capabilities")
        capabilities: list[dict[str, Any]] = []
    else:
        capabilities = [c for c in capabilities_value if isinstance(c, dict)]
        if len(capabilities) != len(capabilities_value):
            errors.append("capabilities must be objects")

    seen_ids: set[str] = set()
    family_dispositions: dict[str, set[str]] = {}
    counts: Counter[str] = Counter()
    unknown_ids: list[str] = []
    for index, capability in enumerate(capabilities):
        cid = capability.get("id")
        if not _text(cid):
            errors.append(f"capability[{index}] requires id")
            continue
        cid = str(cid).strip()
        if cid in seen_ids:
            errors.append(f"duplicate capability id {cid}")
        seen_ids.add(cid)
        family = capability.get("family")
        family = str(family).strip() if _text(family) else cid
        disposition = capability.get("disposition")
        if disposition not in DISPOSITIONS:
            errors.append(f"capability {cid} requires disposition in {sorted(DISPOSITIONS)}")
            continue
        counts[str(disposition)] += 1
        family_dispositions.setdefault(family, set()).add(str(disposition))
        if disposition == "UNKNOWN":
            unknown_ids.append(cid)
        if disposition == "EXCLUDED":
            if not _text(capability.get("rationale")):
                errors.append(f"excluded capability {cid} requires rationale")
            if not _text(capability.get("authority")):
                errors.append(f"excluded capability {cid} requires authority")
        elif not _text(capability.get("evidence")):
            errors.append(f"capability {cid} requires discovery evidence")

    coverage_value = record.get("coverage")
    if not isinstance(coverage_value, list):
        errors.append("capability envelope requires coverage list")
        coverage: set[str] = set()
    else:
        coverage = {str(x).strip() for x in coverage_value if _text(x)}

    missing_families = sorted(expected_families - coverage)
    if missing_families:
        errors.append(f"expected capability families have no discovery coverage: {missing_families}")

    undispositioned = sorted(
        family
        for family in expected_families
        if family in coverage and family not in family_dispositions
    )
    if undispositioned:
        errors.append(f"covered expected families are undispositioned: {undispositioned}")

    # A broad family can be represented by a capability with the same canonical
    # family even when the screen/navigation name differs.
    unresolved = sorted(
        family for family in expected_families
        if family in family_dispositions and family_dispositions[family] == {"UNKNOWN"}
    )
    if ambition in HIGH_AMBITION and (unknown_ids or unresolved):
        errors.append(
            "high-ambition completion cannot retain UNKNOWN capability disposition: "
            f"{sorted(set(unknown_ids) | set(unresolved))}"
        )

    return {
        "valid": not errors,
        "errors": errors,
        "product_class": product_class,
        "ambition": ambition,
        "expected_family_count": len(expected_families),
        "covered_family_count": len(expected_families & coverage),
        "missing_families": missing_families,
        "undispositioned_families": undispositioned,
        "disposition_counts": dict(counts),
    }


def validate_settings_architecture(record: dict[str, Any]) -> dict[str, Any]:
    record, errors = _object(record, "settings architecture")
    scopes = _nonempty_list(record.get("scopes"), "settings scopes", errors)
    scopes_set = {str(x).strip() for x in scopes if _text(x)}
    if len(scopes_set) != len(scopes):
        errors.append("settings scopes must be unique named strings")

    settings_value = record.get("settings")
    if not isinstance(settings_value, list) or not settings_value:
        errors.append("settings architecture requires settings inventory")
        settings: list[dict[str, Any]] = []
    else:
        settings = [s for s in settings_value if isinstance(s, dict)]
        if len(settings) != len(settings_value):
            errors.append("settings inventory entries must be objects")

    ids: set[str] = set()
    for index, setting in enumerate(settings):
        sid = setting.get("id")
        scope = setting.get("scope")
        if not _text(sid):
            errors.append(f"setting[{index}] requires id")
            continue
        sid = str(sid).strip()
        if sid in ids:
            errors.append(f"duplicate setting id {sid}")
        ids.add(sid)
        if scope not in scopes_set:
            errors.append(f"setting {sid} references unknown scope {scope}")
        if setting.get("dangerous") is True and not _text(setting.get("confirmation_or_recovery")):
            errors.append(f"dangerous setting {sid} requires confirmation_or_recovery")
        if setting.get("reversible", True) is False and not _text(setting.get("consequence")):
            errors.append(f"irreversible setting {sid} requires explicit consequence")

    inheritance = record.get("inheritance")
    if not (_text(inheritance) or isinstance(inheritance, dict)):
        errors.append("settings architecture requires scope inheritance/precedence contract")
    if not (_text(record.get("persistence")) or isinstance(record.get("persistence"), dict)):
        errors.append("settings architecture requires persistence/sync contract")
    if not (_text(record.get("recovery")) or isinstance(record.get("recovery"), dict)):
        errors.append("settings architecture requires recovery/reset contract")

    search = record.get("search")
    if len(settings) >= 12 and search not in {True} and not isinstance(search, dict):
        errors.append("large settings systems require searchable discovery")

    taxonomy = record.get("taxonomy")
    if len(settings) >= 8 and not isinstance(taxonomy, (list, dict)):
        errors.append("large settings systems require an explicit taxonomy")

    return {
        "valid": not errors,
        "errors": errors,
        "setting_count": len(settings),
        "scopes": sorted(scopes_set),
    }


def validate_account_workspace_lifecycle(record: dict[str, Any]) -> dict[str, Any]:
    record, errors = _object(record, "account/workspace lifecycle")
    states = _nonempty_list(record.get("states"), "account/workspace lifecycle states", errors)
    states_set = {str(x).strip().lower() for x in states if _text(x)}
    workspace_model = str(record.get("workspace_model", "personal")).strip().lower()

    required_any = {
        "account creation": {"sign-up", "account-created", "created"},
        "authenticated session": {"signed-in", "active-session", "authenticated"},
        "recovery": {"recovery", "recovering", "credential-recovery", "account-recovery"},
        "deactivation or deletion": {"deactivated", "deleted", "delete-pending", "deactivation"},
    }
    if workspace_model in {"organization", "workspace", "team", "multi-tenant"}:
        required_any.update({
            "membership": {"invited", "member", "joined", "membership-pending", "membership-revoked"},
            "workspace switching": {"workspace-switch", "workspace-active", "tenant-switch"},
        })

    missing = []
    for label, aliases in required_any.items():
        if not states_set.intersection(aliases):
            missing.append(label)
            errors.append(f"account/workspace lifecycle missing {label} state")

    if workspace_model in {"organization", "workspace", "team", "multi-tenant"}:
        if not (_text(record.get("membership_authority")) or isinstance(record.get("membership_authority"), dict)):
            errors.append("organization/workspace lifecycle requires membership authority model")
        if not (_text(record.get("ownership_transfer")) or isinstance(record.get("ownership_transfer"), dict)):
            errors.append("organization/workspace lifecycle requires ownership-transfer disposition")

    if not isinstance(record.get("recovery_paths"), list) or not record.get("recovery_paths"):
        errors.append("account/workspace lifecycle requires explicit recovery paths")
    if not (_text(record.get("session_device_model")) or isinstance(record.get("session_device_model"), dict)):
        errors.append("account/workspace lifecycle requires session/device continuity model")

    return {"valid": not errors, "errors": errors, "missing_lifecycle_classes": missing}


def validate_interface_residue_audit(record: dict[str, Any]) -> dict[str, Any]:
    record, errors = _object(record, "interface residue audit")
    surfaces = record.get("surfaces")
    if not isinstance(surfaces, list) or not surfaces:
        return {"valid": False, "errors": errors + ["interface residue audit requires audited surfaces"], "findings": []}

    findings: list[str] = []
    seen: set[str] = set()
    for index, item in enumerate(surfaces):
        if not isinstance(item, dict):
            errors.append(f"residue surface[{index}] must be an object")
            continue
        sid = item.get("id")
        kind = item.get("kind")
        if not _text(sid) or not _text(kind):
            errors.append(f"residue surface[{index}] requires id and kind")
            continue
        sid = str(sid).strip()
        if sid in seen:
            errors.append(f"duplicate residue surface {sid}")
        seen.add(sid)
        appearance = str(item.get("appearance", "")).strip().lower()
        treatment = item.get("treatment")
        intentional = item.get("intentional") is True
        platform_fit = str(item.get("platform_fit", "unknown")).strip().lower()

        if ("default" in appearance or appearance in {"unstyled", "legacy", "classic"}) and not intentional:
            msg = f"unintentional default/legacy residue on {sid} ({kind})"
            errors.append(msg)
            findings.append(msg)
        if treatment is not None and treatment not in RESIDUE_TREATMENTS:
            errors.append(f"residue surface {sid} has invalid treatment {treatment}")
        if not intentional and treatment is None:
            errors.append(f"residue surface {sid} requires intentional treatment decision")
        if platform_fit in {"mismatch", "broken", "unknown"}:
            errors.append(f"residue surface {sid} has unresolved platform fit {platform_fit}")

        kind_norm = str(kind).strip().lower()
        if kind_norm in {"scrollbar", "scrollbars"}:
            if treatment == "hidden-with-alternative" and item.get("operable_alternative") is not True:
                errors.append(f"hidden scrollbar {sid} requires operable alternative")
            if treatment == "reveal-on-interaction" and not isinstance(item.get("reveal_triggers"), list):
                errors.append(f"reveal-on-interaction scrollbar {sid} requires reveal_triggers")

        if item.get("essential_state_cue") is True and item.get("decorative_only") is True:
            errors.append(f"residue surface {sid} cannot mark an essential state cue decorative-only")

    return {"valid": not errors, "errors": errors, "findings": findings, "surface_count": len(surfaces)}


def validate_taste_comparison(record: dict[str, Any]) -> dict[str, Any]:
    record, errors = _object(record, "taste comparison")
    candidates_value = record.get("candidates")
    if not isinstance(candidates_value, list) or len(candidates_value) < 2:
        errors.append("taste comparison requires at least two rendered candidates")
        candidates: list[dict[str, Any]] = []
    else:
        candidates = [c for c in candidates_value if isinstance(c, dict)]
        if len(candidates) != len(candidates_value):
            errors.append("taste candidates must be objects")

    ids: set[str] = set()
    for index, candidate in enumerate(candidates):
        cid = candidate.get("id")
        if not _text(cid):
            errors.append(f"taste candidate[{index}] requires id")
            continue
        cid = str(cid).strip()
        ids.add(cid)
        if not _text(candidate.get("render_ref")):
            errors.append(f"taste candidate {cid} requires render_ref")

    dimensions = record.get("dimensions")
    if not isinstance(dimensions, list) or len({str(x).strip() for x in dimensions if _text(x)}) < 3:
        errors.append("taste comparison requires at least three named discrimination dimensions")

    comparisons = record.get("comparisons")
    if not isinstance(comparisons, list) or not comparisons:
        errors.append("taste comparison requires evidence-bearing pairwise comparisons")
    else:
        for index, comparison in enumerate(comparisons):
            if not isinstance(comparison, dict):
                errors.append(f"taste comparison[{index}] must be an object")
                continue
            if not _text(comparison.get("dimension")):
                errors.append(f"taste comparison[{index}] requires dimension")
            preferred = comparison.get("preferred")
            if preferred not in ids:
                errors.append(f"taste comparison[{index}] preferred candidate must exist")
            if not _text(comparison.get("rationale")):
                errors.append(f"taste comparison[{index}] requires rationale")
            if not _text(comparison.get("evidence_ref")):
                errors.append(f"taste comparison[{index}] requires evidence_ref")

    verdict = record.get("verdict")
    if ids and verdict not in ids and verdict not in {"tie", "re-diverge", "RE_DIVERGE"}:
        errors.append("taste verdict must name a candidate, tie, or re-diverge")

    return {"valid": not errors, "errors": errors, "candidate_count": len(candidates)}


def validate_render_critique(record: dict[str, Any]) -> dict[str, Any]:
    record, errors = _object(record, "render critique")
    render_refs = _nonempty_list(record.get("render_refs"), "render critique render_refs", errors)
    render_set = {str(x).strip() for x in render_refs if _text(x)}
    viewports = _nonempty_list(record.get("viewports"), "render critique viewports", errors)
    if record.get("responsive") is True:
        normalized = {str(x).strip().lower() for x in viewports if _text(x)}
        if not normalized.intersection({"mobile", "small", "phone"}):
            errors.append("responsive render critique requires a mobile/small rendered viewport")
        if not normalized.intersection({"desktop", "large", "wide"}):
            errors.append("responsive render critique requires a desktop/large rendered viewport")

    observations = record.get("observations")
    if not isinstance(observations, list) or not observations:
        errors.append("render critique requires visual observations")
        observations = []
    observed_dimensions: set[str] = set()
    for index, observation in enumerate(observations):
        if not isinstance(observation, dict):
            errors.append(f"render observation[{index}] must be an object")
            continue
        dimension = observation.get("dimension")
        finding = observation.get("finding")
        if not _text(dimension) or not _text(finding):
            errors.append(f"render observation[{index}] requires dimension and finding")
            continue
        observed_dimensions.add(str(dimension).strip().lower())
        evidence_ref = observation.get("evidence_ref")
        if render_set and evidence_ref not in render_set:
            errors.append(f"render observation[{index}] must point to a render_ref")

    critical_dimensions = {"hierarchy", "rhythm", "density", "typography", "spacing"}
    if len(observed_dimensions & critical_dimensions) < 3:
        errors.append("render critique must cover at least three core visual dimensions: hierarchy/rhythm/density/typography/spacing")

    revisions = record.get("revision_decisions")
    if not isinstance(revisions, list) or not revisions:
        errors.append("render critique requires revision decisions")

    return {
        "valid": not errors,
        "errors": errors,
        "render_count": len(render_refs),
        "observed_dimensions": sorted(observed_dimensions),
    }


def validate_domain_audience_fit(record: dict[str, Any]) -> dict[str, Any]:
    record, errors = _object(record, "domain/audience fit")
    if not _text(record.get("domain")):
        errors.append("domain/audience fit requires domain")
    signature = record.get("domain_signature")
    if not isinstance(signature, dict) or not signature:
        errors.append("domain/audience fit requires domain_signature")
    else:
        for key in ("trust", "density"):
            if key not in signature:
                errors.append(f"domain signature requires {key}")

    audience = record.get("audience_profile")
    if not isinstance(audience, dict) or not audience:
        errors.append("domain/audience fit requires audience_profile")
    else:
        for key in ("expertise", "primary_intent", "decision_mode"):
            if not _text(audience.get(key)):
                errors.append(f"audience profile requires {key}")

    fit_decisions = record.get("fit_decisions")
    if not isinstance(fit_decisions, list) or not fit_decisions:
        errors.append("domain/audience fit requires explicit fit_decisions")
    else:
        for index, decision in enumerate(fit_decisions):
            if not isinstance(decision, dict):
                errors.append(f"fit_decision[{index}] must be an object")
                continue
            if not _text(decision.get("dimension")) or not _text(decision.get("consequence")):
                errors.append(f"fit_decision[{index}] requires dimension and consequence")

    return {"valid": not errors, "errors": errors}


def validate_render_fidelity(record: dict[str, Any]) -> dict[str, Any]:
    record, errors = _object(record, "render fidelity")
    tokens = record.get("token_contract")
    if not isinstance(tokens, dict) or not tokens:
        errors.append("render fidelity requires token_contract")
    else:
        for key in ("spacing", "type"):
            if not tokens.get(key):
                errors.append(f"render fidelity token_contract requires {key}")

    components = record.get("component_constraints")
    if not isinstance(components, dict) or not components:
        errors.append("render fidelity requires component quality constraints")

    if not isinstance(record.get("responsive_rules"), (list, dict)) or not record.get("responsive_rules"):
        errors.append("render fidelity requires responsive implementation rules")
    if not isinstance(record.get("motion_rules"), (list, dict)) or not record.get("motion_rules"):
        errors.append("render fidelity requires motion implementation rules")
    if not (_text(record.get("native_control_strategy")) or isinstance(record.get("native_control_strategy"), dict)):
        errors.append("render fidelity requires native/default control strategy")

    runtime = record.get("runtime_evidence")
    if not isinstance(runtime, list) or not runtime:
        errors.append("render fidelity requires runtime rendered evidence")
    else:
        for index, evidence in enumerate(runtime):
            if not isinstance(evidence, dict) or evidence.get("status") not in {"PASS", "FAIL", "UNKNOWN"}:
                errors.append(f"runtime fidelity evidence[{index}] requires PASS/FAIL/UNKNOWN status")

    regression = record.get("visual_regression")
    if not isinstance(regression, dict) or regression.get("status") not in {"PASS", "ACCEPTED_DELTA"}:
        errors.append("render fidelity requires visual regression PASS or ACCEPTED_DELTA evidence")

    return {"valid": not errors, "errors": errors}


def validate_v9_product_system(record: dict[str, Any]) -> dict[str, Any]:
    record, top_errors = _object(record, "v9 product system")
    validators = {
        "capability_envelope": validate_capability_envelope,
        "settings_architecture": validate_settings_architecture,
        "account_workspace_lifecycle": validate_account_workspace_lifecycle,
        "interface_residue_audit": validate_interface_residue_audit,
        "taste_comparison": validate_taste_comparison,
        "render_critique": validate_render_critique,
        "domain_audience_fit": validate_domain_audience_fit,
        "render_fidelity": validate_render_fidelity,
    }
    errors = list(top_errors)
    results: dict[str, dict[str, Any]] = {}
    for key, validator in validators.items():
        value = record.get(key)
        if not isinstance(value, dict):
            result = {"valid": False, "errors": [f"missing {key} evidence"]}
        else:
            result = validator(value)
        results[key] = result
        errors.extend(f"{key}: {error}" for error in result.get("errors", []))
    return {"decision": "BLOCKED" if errors else "PASS", "errors": errors, "checks": results}


__all__ = [
    "validate_account_workspace_lifecycle",
    "validate_capability_envelope",
    "validate_domain_audience_fit",
    "validate_interface_residue_audit",
    "validate_render_critique",
    "validate_render_fidelity",
    "validate_settings_architecture",
    "validate_taste_comparison",
    "validate_v9_product_system",
]
