"""NUI v7 rendered-perception evidence gates.

The validator deliberately does not compute a universal beauty score. It asks
whether the agent observed enough of the rendered artifact, across the states
and viewports that matter, to make a falsifiable visual-quality claim.
"""
from __future__ import annotations

from typing import Any


def _text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _list_of_text(value: Any, minimum: int = 1) -> bool:
    return isinstance(value, list) and len(value) >= minimum and all(_text(x) for x in value)


def _number(value: Any) -> float | None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    return float(value)


def _unit(value: Any) -> bool:
    number = _number(value)
    return number is not None and 0.0 <= number <= 1.0


def _validate_capture_matrix(record: dict[str, Any], errors: list[str], *, high_ambition: bool) -> tuple[set[str], set[tuple[int, int]]]:
    captures = record.get("capture_matrix")
    if not isinstance(captures, list) or not captures:
        errors.append("rendered perception requires capture_matrix[]; a screenshot path alone is screenshot theater")
        return set(), set()

    states: set[str] = set()
    viewports: set[tuple[int, int]] = set()
    artifacts: set[str] = set()
    for index, capture in enumerate(captures):
        if not isinstance(capture, dict):
            errors.append(f"capture_matrix[{index}] must be an object")
            continue
        state = capture.get("state")
        artifact = capture.get("artifact")
        renderer = capture.get("renderer")
        viewport = capture.get("viewport")
        if not _text(state):
            errors.append(f"capture_matrix[{index}] requires state")
        else:
            states.add(state.strip())
        if not _text(artifact):
            errors.append(f"capture_matrix[{index}] requires artifact")
        elif artifact in artifacts:
            errors.append(f"capture_matrix reuses artifact {artifact}; each evidence capture must be traceable")
        else:
            artifacts.add(artifact)
        if not _text(renderer):
            errors.append(f"capture_matrix[{index}] requires renderer")
        if not isinstance(viewport, dict):
            errors.append(f"capture_matrix[{index}] requires viewport object")
            continue
        width = viewport.get("width")
        height = viewport.get("height")
        dpr = viewport.get("dpr")
        if not isinstance(width, int) or width <= 0 or not isinstance(height, int) or height <= 0:
            errors.append(f"capture_matrix[{index}] viewport requires positive integer width/height")
        else:
            viewports.add((width, height))
        if _number(dpr) is None or float(dpr) <= 0:
            errors.append(f"capture_matrix[{index}] viewport requires positive dpr")

    required_states = record.get("required_states", ["default"])
    if not _list_of_text(required_states):
        errors.append("required_states must be a non-empty string list")
    else:
        for state in required_states:
            if state not in states:
                errors.append(f"required rendered state not captured: {state}")

    responsive = bool(record.get("responsive_material") or record.get("multi_viewport") or high_ambition)
    if responsive and len(viewports) < 2:
        errors.append("responsive/high-ambition perception evidence requires at least two materially different viewports")
    return states, viewports


def _validate_observations(record: dict[str, Any], errors: list[str], *, high_ambition: bool) -> None:
    observations = record.get("observations")
    if not isinstance(observations, dict):
        errors.append("rendered perception requires observations object derived from the rendered artifact")
        return

    focal_order = observations.get("focal_order")
    if not _list_of_text(focal_order, 2):
        errors.append("observations.focal_order requires at least two observed attention targets")

    hierarchy = observations.get("hierarchy")
    if not isinstance(hierarchy, dict) or not _text(hierarchy.get("primary")) or not _text(hierarchy.get("secondary")):
        errors.append("observations.hierarchy requires primary and secondary observed roles")
    elif high_ambition and not _list_of_text(hierarchy.get("quiet_regions")):
        errors.append("high-ambition hierarchy evidence requires quiet_regions so visual energy is not uniformly loud")

    typography = observations.get("resolved_typography")
    if not isinstance(typography, list) or not typography:
        errors.append("observations.resolved_typography requires actual rendered font-resolution evidence")
    else:
        for index, font in enumerate(typography):
            if not isinstance(font, dict):
                errors.append(f"resolved_typography[{index}] must be an object")
                continue
            for field in ("role", "intended", "resolved"):
                if not _text(font.get(field)):
                    errors.append(f"resolved_typography[{index}] requires {field}")
            if not isinstance(font.get("loaded"), bool):
                errors.append(f"resolved_typography[{index}] requires loaded boolean")
            if font.get("resolved") != font.get("intended") and not font.get("fallback_reviewed"):
                errors.append(f"resolved_typography[{index}] fallback delta must be reviewed")

    signature = observations.get("signature_mechanism")
    if not isinstance(signature, dict):
        errors.append("observations.signature_mechanism is required")
    else:
        if not _text(signature.get("name")):
            errors.append("signature mechanism requires name")
        if not _text(signature.get("subject_link")):
            errors.append("signature mechanism must explain its subject/domain link")
        removal_cost = _number(signature.get("removal_cost"))
        if removal_cost is None or not 0 <= removal_cost <= 1:
            errors.append("signature mechanism removal_cost must be in [0,1]")
        elif high_ambition and removal_cost < 0.45:
            errors.append("high-ambition signature mechanism has too little observed removal cost")
        if not _list_of_text(signature.get("observed_in")):
            errors.append("signature mechanism must name rendered artifacts where it was observed")

    material = observations.get("material_structure")
    if not isinstance(material, dict):
        errors.append("observations.material_structure is required")
    else:
        if not _list_of_text(material.get("surface_roles"), 2):
            errors.append("material_structure.surface_roles requires at least two distinct material/surface roles")
        if not _unit(material.get("boundary_density")):
            errors.append("material_structure.boundary_density must be in [0,1]")
        if not _unit(material.get("material_variety")):
            errors.append("material_structure.material_variety must be in [0,1]")


def _validate_temporal(record: dict[str, Any], errors: list[str]) -> None:
    if not record.get("motion_material"):
        return
    evidence = record.get("temporal_evidence")
    if not isinstance(evidence, dict):
        errors.append("material motion requires temporal_evidence with a rendered sequence")
        errors.append("material motion requires reduced-motion equivalent")
        return
    sequence = evidence.get("sequence")
    if not isinstance(sequence, list) or len(sequence) < 3:
        errors.append("temporal_evidence.sequence requires at least before, transition, and settled observations")
    else:
        times: list[float] = []
        for index, frame in enumerate(sequence):
            if not isinstance(frame, dict):
                errors.append(f"temporal sequence frame {index} must be an object")
                continue
            if not _text(frame.get("state")) or not _text(frame.get("artifact")):
                errors.append(f"temporal sequence frame {index} requires state and artifact")
            time_ms = _number(frame.get("time_ms"))
            if time_ms is None or time_ms < 0:
                errors.append(f"temporal sequence frame {index} requires non-negative time_ms")
            else:
                times.append(time_ms)
        if times and times != sorted(times):
            errors.append("temporal sequence time_ms must be monotonic")
    if not _text(evidence.get("semantic_purpose")):
        errors.append("temporal evidence requires semantic_purpose; effects alone are insufficient")
    if not _text(evidence.get("reduced_motion_equivalent")):
        errors.append("temporal evidence requires reduced_motion_equivalent")


def _validate_pixel_diff(record: dict[str, Any], errors: list[str]) -> None:
    pixel_diff = record.get("pixel_diff")
    if pixel_diff is None:
        return
    if not isinstance(pixel_diff, dict):
        errors.append("pixel_diff must be an object when provided")
        return
    required_text = ("renderer", "environment", "rationale", "baseline", "candidate")
    if any(not _text(pixel_diff.get(field)) for field in required_text):
        errors.append("pixel_diff requires renderer, environment, rationale, baseline and candidate")
    delta = _number(pixel_diff.get("delta"))
    tolerance = _number(pixel_diff.get("tolerance"))
    if delta is None or delta < 0 or tolerance is None or tolerance < 0:
        errors.append("pixel_diff delta and tolerance must be non-negative numbers")
    elif delta > tolerance:
        errors.append(f"pixel_diff delta {delta:g} exceeds calibrated tolerance {tolerance:g}")


def _validate_high_ambition_loop(record: dict[str, Any], errors: list[str]) -> None:
    comparison = record.get("reference_comparison")
    if not isinstance(comparison, dict):
        errors.append("high-ambition rendered evidence requires reference_comparison")
    else:
        if not _list_of_text(comparison.get("references"), 2):
            errors.append("reference_comparison requires at least two concrete references")
        if not _list_of_text(comparison.get("dimensions"), 2):
            errors.append("reference_comparison requires explicit comparison dimensions")
        if not _text(comparison.get("result")):
            errors.append("reference_comparison requires a rendered-result conclusion")

    critique = record.get("critique_cycle")
    if not isinstance(critique, dict):
        errors.append("high-ambition rendered evidence requires critique_cycle")
        return
    weaknesses = critique.get("weaknesses")
    adequacy = critique.get("adequacy")
    if adequacy not in {"PASS", "RE_DIVERGE", "BLOCKED"}:
        errors.append("critique_cycle.adequacy must be PASS, RE_DIVERGE or BLOCKED")
    if adequacy == "PASS":
        if not isinstance(weaknesses, list) or not weaknesses:
            errors.append("critique cycle cannot claim PASS without at least one observed weakness/fix trace")
        else:
            for index, finding in enumerate(weaknesses):
                if not isinstance(finding, dict) or any(not _text(finding.get(field)) for field in ("finding", "fix", "verified_in")):
                    errors.append(f"critique weakness {index} requires finding, fix and verified_in")


def validate_rendered_perception(record: dict[str, Any], high_ambition: bool = False) -> dict[str, Any]:
    """Validate evidence that an agent actually inspected rendered UI output.

    Pixel deltas are optional and treated as calibrated regression evidence, not
    as a beauty score. High-ambition work additionally requires reference
    comparison and an observe/fix/re-observe trace.
    """
    if not isinstance(record, dict):
        return {"valid": False, "decision": "BLOCKED", "errors": ["rendered perception evidence must be an object"]}

    errors: list[str] = []
    _validate_capture_matrix(record, errors, high_ambition=high_ambition)
    _validate_observations(record, errors, high_ambition=high_ambition)
    _validate_temporal(record, errors)
    _validate_pixel_diff(record, errors)
    if high_ambition:
        _validate_high_ambition_loop(record, errors)

    if record.get("status") not in {None, "PASS", "BLOCKED", "RE_DIVERGE"}:
        errors.append("status must be PASS, BLOCKED or RE_DIVERGE when provided")
    if record.get("status") in {"BLOCKED", "RE_DIVERGE"}:
        errors.append(f"rendered perception status is {record['status']}")

    return {
        "valid": not errors,
        "decision": "PASS" if not errors else "BLOCKED",
        "errors": errors,
        "evidence_kind": "rendered-perception-v7",
    }
