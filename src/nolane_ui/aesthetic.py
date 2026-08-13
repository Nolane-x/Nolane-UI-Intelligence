"""NUI v5 affective/aesthetic deterministic invariants.

This module does not pretend to calculate universal beauty. It validates whether
high-ambition UI work preserved the original experiential contract and supplied
the evidence that NUI v5 requires before an agent may treat a visual direction
as adequate or complete.
"""
from __future__ import annotations

from collections import Counter
from typing import Any

HIGH_AMBITION = {"flagship", "exceptional", "experiential"}
MAGNITUDE_DIMENSIONS = ("scope", "data", "spatial", "institutional", "temporal", "network", "visual")
BASE_HIGH_AMBITION_ROUTES = {
    "preserving-experiential-intent",
    "directing-visual-ambition",
    "exploring-aesthetic-directions",
    "researching-visual-references",
    "directing-visual-hierarchy",
    "crafting-typography",
    "crafting-color",
    "crafting-spacing-and-rhythm",
    "crafting-depth-and-surfaces",
    "directing-iconography-and-imagery",
    "designing-motion",
    "preventing-generic-ui",
    "detecting-aesthetic-attractors",
    "engineering-visual-legibility",
    "directing-visual-energy",
    "deepening-signature-mechanisms",
    "critiquing-visual-design",
    "critiquing-aesthetic-adequacy",
    "iterating-rendered-visual-design",
    "escaping-aesthetic-basins",
}


def _number(value: Any) -> float | None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    return float(value)


def _unit(value: Any, field: str, errors: list[str]) -> float | None:
    number = _number(value)
    if number is None or number < 0.0 or number > 1.0:
        errors.append(f"{field} must be a number in [0,1]")
        return None
    return number


def _nonempty_strings(value: Any) -> bool:
    return isinstance(value, list) and bool(value) and all(isinstance(x, str) and x.strip() for x in value)


def mandatory_aesthetic_routes(profile: dict[str, Any]) -> set[str]:
    """Return non-optional v5 routes implied by experiential/visual ambition."""
    if not isinstance(profile, dict):
        return set()
    ambition = str(profile.get("visual_ambition", "")).strip().lower()
    required: set[str] = set()

    if ambition in HIGH_AMBITION:
        required |= BASE_HIGH_AMBITION_ROUTES
        if profile.get("visual_freedom") in {"high", "open", "unconstrained"}:
            required |= {"exploring-aesthetic-directions", "researching-visual-references"}
        if profile.get("material_data_visualization") or profile.get("data_visualization"):
            required |= {"designing-data-visualization", "proving-visual-encoding-semantics"}
        if profile.get("aspirational_identity") or profile.get("status_fantasy") or profile.get("role_fantasy"):
            required.add("modeling-aspirational-identity")
        if profile.get("magnitude_language") or profile.get("magnitude_target"):
            required.add("composing-spatial-dramaturgy")
        if profile.get("product_wide") or profile.get("multi_screen") or profile.get("workspace_count", 0) > 1:
            required.add("evaluating-perceptual-diversity")
    elif ambition in {"distinctive"}:
        required |= {
            "directing-visual-ambition",
            "exploring-aesthetic-directions",
            "preventing-generic-ui",
            "critiquing-visual-design",
        }

    if profile.get("experiential_intent") or profile.get("desired_feelings"):
        required.add("preserving-experiential-intent")
    return required


def validate_experiential_intent(record: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(record, dict):
        return {"valid": False, "decision": "BLOCKED", "errors": ["experiential intent must be an object"]}
    for field in ("desired_feelings", "forbidden_feelings", "source_language"):
        if not _nonempty_strings(record.get(field)):
            errors.append(f"experiential intent requires non-empty {field}")
    if not isinstance(record.get("identity_projection"), str) or not record.get("identity_projection", "").strip():
        errors.append("experiential intent requires identity_projection")
    _unit(record.get("emotional_intensity"), "emotional_intensity", errors)
    _unit(record.get("memorability_target"), "memorability_target", errors)
    magnitude = record.get("magnitude_target")
    if not isinstance(magnitude, dict):
        errors.append("experiential intent requires magnitude_target object")
    else:
        missing = [key for key in MAGNITUDE_DIMENSIONS if key not in magnitude]
        if missing:
            errors.append(f"magnitude_target missing dimensions {missing}")
    proxies = record.get("operational_proxies")
    if proxies is not None and not _nonempty_strings(proxies):
        errors.append("operational_proxies must be a non-empty string list when provided")
    return {"valid": not errors, "decision": "PASS" if not errors else "BLOCKED", "errors": errors}


def validate_aesthetic_attractor_audit(record: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    probable: list[str] = []
    mechanisms = record.get("mechanisms") if isinstance(record, dict) else None
    if not isinstance(mechanisms, list):
        return {"valid": False, "decision": "BLOCKED", "errors": ["attractor audit requires mechanisms[]"], "probable_tropes": []}
    for index, item in enumerate(mechanisms):
        if not isinstance(item, dict):
            errors.append(f"mechanism {index} must be an object")
            continue
        name = str(item.get("name") or f"mechanism-{index}")
        frequency = _number(item.get("frequency"))
        specificity = _number(item.get("subject_specificity"))
        removal = _number(item.get("removal_cost"))
        necessity = _number(item.get("semantic_necessity"))
        for field in ("semantic_necessity", "subject_specificity", "information_gain", "emotional_contribution", "removal_cost"):
            v = _number(item.get(field))
            if v is None or not 0 <= v <= 1:
                errors.append(f"{name}.{field} must be in [0,1]")
        if frequency is None or frequency < 0:
            errors.append(f"{name}.frequency must be non-negative")
        elif frequency >= 12 and specificity is not None and removal is not None and necessity is not None:
            if specificity <= 0.35 and removal <= 0.35 and necessity <= 0.45:
                probable.append(name)
    global_metrics = record.get("global_metrics", {}) if isinstance(record, dict) else {}
    required_metrics = ("boundary_density", "edge_density", "surface_entropy", "boundary_repetition", "material_variety", "quiet_region_ratio")
    if not isinstance(global_metrics, dict):
        errors.append("attractor audit requires global_metrics object")
        global_metrics = {}
    for field in required_metrics:
        _unit(global_metrics.get(field), f"global_metrics.{field}", errors)
    if probable:
        errors.append(f"probable aesthetic trope accumulation: {sorted(probable)}")
    bd = _number(global_metrics.get("boundary_density"))
    br = _number(global_metrics.get("boundary_repetition"))
    mv = _number(global_metrics.get("material_variety"))
    qr = _number(global_metrics.get("quiet_region_ratio"))
    if all(v is not None for v in (bd, br, mv, qr)) and bd >= 0.70 and br >= 0.75 and mv <= 0.25 and qr <= 0.12:
        errors.append("global boundary/material accumulation indicates border or pane soup")
    return {"valid": not errors, "decision": "PASS" if not errors else "BLOCKED", "errors": errors, "probable_tropes": sorted(probable)}


def validate_visual_legibility_evidence(record: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(record, dict):
        return {"valid": False, "decision": "BLOCKED", "errors": ["visual legibility evidence must be an object"]}
    samples = record.get("samples")
    if not isinstance(samples, list) or not samples:
        errors.append("visual legibility evidence requires computed style samples")
        samples = []
    for index, sample in enumerate(samples):
        if not isinstance(sample, dict):
            errors.append(f"legibility sample {index} must be an object")
            continue
        sid = sample.get("id", index)
        px = _number(sample.get("computed_px"))
        if px is None or px <= 0:
            errors.append(f"sample {sid} requires positive computed_px")
            continue
        if px < 11 and not isinstance(sample.get("semantic_reason"), str):
            errors.append(f"sample {sid} below 11px requires semantic reason")
        if px < 10 and sample.get("required_information"):
            errors.append(f"sample {sid} below 10px cannot contain required information")
        if px < 9 and not sample.get("decorative", False):
            errors.append(f"sample {sid} below 9px must be decorative/auxiliary")
        compound = sum(bool(sample.get(key)) for key in ("low_contrast", "uppercase", "tracked"))
        if px < 11 and compound >= 2:
            errors.append(f"sample {sid} has compound microtext legibility risk")
    fonts = record.get("resolved_fonts")
    if not isinstance(fonts, list) or not fonts:
        errors.append("visual legibility evidence requires resolved_fonts[]")
        fonts = []
    for index, font in enumerate(fonts):
        if not isinstance(font, dict):
            errors.append(f"resolved font {index} must be an object")
            continue
        role = font.get("role", index)
        if not all(isinstance(font.get(key), str) and font.get(key).strip() for key in ("intended", "resolved", "loading")):
            errors.append(f"resolved font {role} requires intended, resolved and loading")
            continue
        if font.get("resolved") != font.get("intended") and not font.get("fallback_delta_reviewed"):
            errors.append(f"resolved font {role} fallback delta is unreviewed")
    return {"valid": not errors, "decision": "PASS" if not errors else "BLOCKED", "errors": errors}


def validate_encoding_provenance_table(record: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    channels = record.get("channels") if isinstance(record, dict) else None
    if not isinstance(channels, list) or not channels:
        return {"valid": False, "decision": "BLOCKED", "errors": ["encoding provenance requires channels[]"]}
    seen: set[str] = set()
    for index, item in enumerate(channels):
        if not isinstance(item, dict):
            errors.append(f"channel {index} must be an object")
            continue
        channel = item.get("channel")
        if not isinstance(channel, str) or not channel.strip():
            errors.append(f"channel {index} requires channel name")
            continue
        if channel in seen:
            errors.append(f"duplicate visual channel {channel}")
        seen.add(channel)
        decorative = item.get("decorative") is True
        meaning = item.get("meaning")
        if not decorative and (not isinstance(meaning, str) or not meaning.strip()):
            errors.append(f"non-decorative channel {channel} requires semantic meaning")
    return {"valid": not errors, "decision": "PASS" if not errors else "BLOCKED", "errors": errors}


def validate_signature_depth_contract(record: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(record, dict):
        return {"valid": False, "decision": "BLOCKED", "errors": ["signature depth contract must be an object"]}
    dimensions = ("semantic_depth", "interaction_depth", "visual_depth", "information_gain", "product_specificity", "reusability", "memorability", "failure_if_removed")
    values: dict[str, float] = {}
    for field in dimensions:
        value = _unit(record.get(field), field, errors)
        if value is not None:
            values[field] = value
    required_level = record.get("required_level", "standard")
    floor = {"standard": 0.35, "medium": 0.45, "high": 0.60, "exceptional": 0.72}.get(str(required_level), 0.60)
    depth_fields = ("semantic_depth", "interaction_depth", "information_gain", "product_specificity", "failure_if_removed")
    if not errors and sum(values[x] for x in depth_fields) / len(depth_fields) < floor:
        errors.append(f"signature semantic/interaction depth is below {required_level} floor")
    if values.get("visual_depth", 0) >= 0.75 and values.get("semantic_depth", 1) <= 0.25 and values.get("information_gain", 1) <= 0.25:
        errors.append("signature is visually deep but semantically decorative")
    return {"valid": not errors, "decision": "PASS" if not errors else "BLOCKED", "errors": errors}


def validate_workspace_visual_matrix(record: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    screens = record.get("screens") if isinstance(record, dict) else None
    if not isinstance(screens, list) or len(screens) < 2:
        return {"valid": False, "decision": "BLOCKED", "errors": ["workspace visual matrix requires at least two screens"]}
    dimensions = ("signature", "dominant_geometry", "density", "main_visualization", "surface_pattern", "typographic_gesture", "color_mass", "interaction_signature")
    for index, screen in enumerate(screens):
        if not isinstance(screen, dict):
            errors.append(f"screen {index} must be an object")
            continue
        if not isinstance(screen.get("screen"), str) or not screen.get("screen", "").strip():
            errors.append(f"screen {index} requires screen name")
        for field in dimensions:
            if not isinstance(screen.get(field), str) or not screen.get(field, "").strip():
                errors.append(f"screen {screen.get('screen', index)} requires {field}")
    if not errors:
        unique_ratios = []
        for field in dimensions:
            counts = Counter(str(s[field]).strip().lower() for s in screens)
            unique_ratios.append(len(counts) / len(screens))
        diversity = sum(unique_ratios) / len(unique_ratios)
        if len(screens) >= 4 and diversity < 0.28:
            errors.append("cross-surface template repetition: perceptual diversity is too low")
    return {"valid": not errors, "decision": "PASS" if not errors else "BLOCKED", "errors": errors}


def decide_aesthetic_basin(record: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(record, dict):
        return {"decision": "RE_DIVERGE", "reasons": ["missing basin evidence"]}
    reasons: list[str] = []
    fit = _number(record.get("affective_fit")); fit_target = _number(record.get("affective_target"))
    distinct = _number(record.get("distinctiveness")); distinct_target = _number(record.get("distinctiveness_target"))
    if fit is None or fit_target is None or fit < fit_target:
        reasons.append("affective fit remains below target")
    if distinct is None or distinct_target is None or distinct < distinct_target:
        reasons.append("distinctiveness remains below target")
    losses = record.get("reference_losses")
    if not isinstance(losses, int) or isinstance(losses, bool) or losses >= 2:
        reasons.append("repeated reference-frontier loss")
    if record.get("signature_depth_pass") is not True:
        reasons.append("signature depth has not passed")
    if record.get("adequacy_status") not in {"PASS", "ADEQUATE"}:
        reasons.append("aesthetic adequacy critic has not passed the direction")
    return {"decision": "RE_DIVERGE" if reasons else "REFINE", "reasons": reasons}


def validate_skill_interaction_evidence(record: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(record, dict):
        return {"valid": False, "decision": "BLOCKED", "errors": ["skill interaction evidence must be an object"]}
    factorial = record.get("factorial_cases")
    mutations = record.get("semantic_mutations")
    if not isinstance(factorial, list) or not factorial:
        errors.append("skill interaction evidence requires factorial_cases[]")
        factorial = []
    if not isinstance(mutations, list) or not mutations:
        errors.append("skill interaction evidence requires semantic_mutations[]")
        mutations = []
    for index, case in enumerate(factorial):
        if not isinstance(case, dict):
            errors.append(f"factorial case {index} must be an object")
            continue
        skills = case.get("skills")
        if not isinstance(skills, list) or len(set(skills)) < 2:
            errors.append(f"factorial case {case.get('id', index)} requires at least two skills")
        if not case.get("objective_delta_reviewed"):
            errors.append(f"factorial case {case.get('id', index)} requires reviewed objective delta")
        if "baseline" not in case or "combined" not in case:
            errors.append(f"factorial case {case.get('id', index)} requires baseline and combined evidence")
    for index, mutation in enumerate(mutations):
        if not isinstance(mutation, dict):
            errors.append(f"semantic mutation {index} must be an object")
            continue
        for field in ("mutation", "target_skill", "expected"):
            if not isinstance(mutation.get(field), str) or not mutation.get(field, "").strip():
                errors.append(f"semantic mutation {mutation.get('id', index)} requires {field}")
        if not _nonempty_strings(mutation.get("detected_by")):
            errors.append(f"semantic mutation {mutation.get('id', index)} requires detected_by cases")
    return {"valid": not errors, "decision": "PASS" if not errors else "BLOCKED", "errors": errors}
