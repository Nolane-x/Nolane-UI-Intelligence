"""V8 flagship visual-synthesis invariants.

This module does not score beauty. It rejects high-ambition visual claims that
lack the observable decisions which make authored visual quality falsifiable:
real divergence, product specificity, hierarchy, craft systems, responsive
recomposition, and closed render/critique loops.
"""
from __future__ import annotations

from typing import Any

_HIGH_AMBITION = {"flagship", "exceptional", "experiential"}
_DIRECTION_FIELDS = (
    "id",
    "composition",
    "type_system",
    "material_system",
    "signature_mechanism",
)
_REQUIRED_TYPOGRAPHY = (
    "roles",
    "measure_strategy",
    "optical_hierarchy",
    "fallback_behavior",
)
_REQUIRED_COMPOSITION = (
    "grid_logic",
    "density_rhythm",
    "edge_logic",
    "responsive_transform",
)
_REQUIRED_COLOR_MATERIAL = (
    "semantic_palette",
    "chroma_budget",
    "depth_model",
    "surface_rule",
    "dark_mode_behavior",
)
_REQUIRED_MOTION = (
    "purpose",
    "timing_model",
    "gesture_relation",
    "reduced_motion",
)
_REQUIRED_SIGNATURE = (
    "mechanism",
    "subject_link",
    "memory_hook",
    "restraint_rule",
)


def _missing(record: Any, fields: tuple[str, ...]) -> list[str]:
    if not isinstance(record, dict):
        return list(fields)
    return [field for field in fields if not record.get(field)]


def _text(value: Any) -> str:
    return str(value or "").strip()


def validate_flagship_visual_synthesis(record: dict[str, Any]) -> dict[str, Any]:
    """Validate an evidence packet for flagship/exceptional visual synthesis.

    The validator deliberately avoids a numeric beauty score. A PASS means the
    claimed direction survived structural anti-generic and rendered-evidence
    gates; it never means that beauty is objectively proven.
    """
    if not isinstance(record, dict):
        return {
            "valid": False,
            "errors": ["flagship visual synthesis must be an object"],
            "metrics": {},
        }

    errors: list[str] = []
    ambition = _text(record.get("ambition")).lower()
    if ambition not in _HIGH_AMBITION:
        errors.append("flagship visual synthesis requires flagship|exceptional|experiential ambition")
    if not _text(record.get("visual_thesis")):
        errors.append("flagship visual synthesis requires a concrete visual_thesis")

    candidates = record.get("direction_candidates", [])
    candidate_count = len(candidates) if isinstance(candidates, list) else 0
    if not isinstance(candidates, list) or candidate_count < 3:
        errors.append("high-ambition visual synthesis requires at least three direction candidates")
        candidates = []

    ids: list[str] = []
    fingerprints: list[tuple[str, str, str, str]] = []
    dimension_values: dict[str, set[str]] = {
        "composition": set(),
        "type_system": set(),
        "material_system": set(),
        "signature_mechanism": set(),
    }
    for index, candidate in enumerate(candidates):
        if not isinstance(candidate, dict):
            errors.append(f"direction candidate[{index}] must be an object")
            continue
        missing = _missing(candidate, _DIRECTION_FIELDS)
        for field in missing:
            errors.append(f"direction candidate[{index}] requires {field}")
        cid = _text(candidate.get("id"))
        if cid:
            ids.append(cid)
        fp = tuple(_text(candidate.get(field)).lower() for field in _DIRECTION_FIELDS[1:])
        fingerprints.append(fp)  # type: ignore[arg-type]
        for field in dimension_values:
            value = _text(candidate.get(field)).lower()
            if value:
                dimension_values[field].add(value)

    if ids and len(ids) != len(set(ids)):
        errors.append("direction candidate ids must be unique")
    if len(fingerprints) >= 3:
        if len(set(fingerprints)) == 1:
            errors.append("direction candidates converged on the same solution instead of materially diverging")
        static_dimensions = [name for name, values in dimension_values.items() if len(values) < 2]
        if static_dimensions:
            errors.append(
                "direction candidates must materially diverge across composition/type/material/signature; "
                f"static dimensions: {', '.join(static_dimensions)}"
            )

    selected = _text(record.get("selected_direction_id"))
    if not selected or selected not in set(ids):
        errors.append("selected_direction_id must reference a declared direction candidate")
    if not _text(record.get("selection_rationale")):
        errors.append("flagship visual synthesis requires a selection_rationale tied to product value")

    hierarchy = record.get("attention_hierarchy", [])
    if not isinstance(hierarchy, list) or len(hierarchy) < 3:
        errors.append("attention_hierarchy requires at least three ranked roles")
    else:
        ranks: list[int] = []
        roles: list[str] = []
        for index, item in enumerate(hierarchy):
            if not isinstance(item, dict):
                errors.append(f"attention_hierarchy[{index}] must be an object")
                continue
            if not item.get("rank") or not item.get("role") or not item.get("visual_mechanism"):
                errors.append(f"attention_hierarchy[{index}] requires rank/role/visual_mechanism")
                continue
            try:
                ranks.append(int(item["rank"]))
            except (TypeError, ValueError):
                errors.append(f"attention_hierarchy[{index}].rank must be an integer")
            roles.append(_text(item.get("role")))
        if ranks and (1 not in ranks or len(ranks) != len(set(ranks))):
            errors.append("attention_hierarchy requires one unique primary rank and unique ranking")
        if roles and len(roles) != len(set(roles)):
            errors.append("attention_hierarchy roles must not collapse into equal repeated roles")

    typography = record.get("typography")
    for field in _missing(typography, _REQUIRED_TYPOGRAPHY):
        errors.append(f"typography requires {field}")
    if isinstance(typography, dict):
        roles = typography.get("roles", [])
        if not isinstance(roles, list) or len({str(x) for x in roles if x}) < 3:
            errors.append("typography requires at least three distinct functional roles")

    composition = record.get("composition")
    for field in _missing(composition, _REQUIRED_COMPOSITION):
        errors.append(f"composition requires {field}")

    color_material = record.get("color_material")
    for field in _missing(color_material, _REQUIRED_COLOR_MATERIAL):
        errors.append(f"color_material requires {field}")

    motion = record.get("motion")
    for field in _missing(motion, _REQUIRED_MOTION):
        errors.append(f"motion requires {field}")

    signature = record.get("signature")
    for field in _missing(signature, _REQUIRED_SIGNATURE):
        errors.append(f"signature requires {field}")

    frontier = record.get("reference_frontier", [])
    if not isinstance(frontier, list) or len(frontier) < 3:
        errors.append("reference_frontier requires at least three mechanism-level references")
    else:
        reference_ids: list[str] = []
        reference_mechanisms: list[str] = []
        for index, item in enumerate(frontier):
            if not isinstance(item, dict) or not all(item.get(k) for k in ("id", "mechanism", "transfer_boundary")):
                errors.append(f"reference_frontier[{index}] requires id/mechanism/transfer_boundary")
                continue
            reference_ids.append(_text(item.get("id")))
            reference_mechanisms.append(_text(item.get("mechanism")).lower())
        if reference_ids and len(reference_ids) != len(set(reference_ids)):
            errors.append("reference_frontier ids must be unique")
        if reference_mechanisms and len(set(reference_mechanisms)) < 3:
            errors.append("reference_frontier requires three distinct mechanism-level learnings")

    transfer = record.get("generic_transfer_test")
    if not isinstance(transfer, dict) or transfer.get("verdict") != "FAILS_TRANSFER" or not transfer.get("reason"):
        errors.append("high-ambition product specificity requires a documented generic transfer test that FAILS_TRANSFER")

    states = record.get("rendered_states", [])
    required_states = 3 if ambition in {"exceptional", "experiential"} else 2
    if not isinstance(states, list) or len(states) < required_states:
        errors.append(f"{ambition or 'high-ambition'} synthesis requires at least {required_states} rendered states")
        states = []
    viewports: set[str] = set()
    state_ids: set[str] = set()
    duplicate_state_ids: set[str] = set()
    for index, state in enumerate(states):
        if not isinstance(state, dict):
            errors.append(f"rendered_states[{index}] must be an object")
            continue
        if not all(state.get(k) for k in ("id", "viewport")):
            errors.append(f"rendered_states[{index}] requires id/viewport")
        sid = _text(state.get("id"))
        if sid:
            if sid in state_ids:
                duplicate_state_ids.add(sid)
            state_ids.add(sid)
        changes = state.get("structural_changes", [])
        if not isinstance(changes, list) or not [x for x in changes if _text(x)]:
            errors.append(f"rendered_states[{index}] requires observed structural_changes; shrink-only evidence is insufficient")
        viewport = _text(state.get("viewport"))
        if viewport:
            viewports.add(viewport)
    if duplicate_state_ids:
        errors.append(f"rendered state ids must be unique: {', '.join(sorted(duplicate_state_ids))}")
    if states and len(viewports) < 2:
        errors.append("rendered evidence requires at least two materially different viewport classes")

    cycles = record.get("critique_cycles", [])
    if not isinstance(cycles, list) or len(cycles) < 2:
        errors.append("flagship visual synthesis requires at least two closed critique cycles")
        cycles = []
    categories: set[str] = set()
    for index, cycle in enumerate(cycles):
        if not isinstance(cycle, dict) or not all(cycle.get(k) for k in ("category", "finding", "correction", "verified_in")):
            errors.append(f"critique_cycles[{index}] requires category/finding/correction/verified_in")
            continue
        categories.add(_text(cycle.get("category")).lower())
        verified_in = _text(cycle.get("verified_in"))
        if verified_in not in state_ids:
            errors.append(f"critique_cycles[{index}].verified_in must reference a declared rendered state")
    if len(cycles) >= 2 and len(categories) < 2:
        errors.append("critique cycles must attack at least two distinct failure dimensions")

    audit = record.get("anti_generic_audit")
    if not isinstance(audit, dict):
        errors.append("flagship visual synthesis requires anti_generic_audit")
    else:
        rejected = audit.get("rejected_attractors", [])
        replacements = audit.get("replacement_mechanisms", [])
        if not isinstance(rejected, list) or len([x for x in rejected if _text(x)]) < 3:
            errors.append("anti_generic_audit requires at least three concrete rejected attractors")
        if not isinstance(replacements, list) or len([x for x in replacements if _text(x)]) < 2:
            errors.append("anti_generic_audit requires concrete product-native replacement mechanisms")
        if not _text(audit.get("silhouette_observation")):
            errors.append("anti_generic_audit requires a silhouette_observation")

    if record.get("decision") != "PASS":
        errors.append("flagship visual synthesis requires explicit decision PASS")

    return {
        "valid": not errors,
        "errors": errors,
        "metrics": {
            "ambition": ambition,
            "direction_candidate_count": candidate_count,
            "reference_count": len(frontier) if isinstance(frontier, list) else 0,
            "rendered_state_count": len(states),
            "critique_cycle_count": len(cycles),
            "viewport_class_count": len(viewports),
        },
    }
