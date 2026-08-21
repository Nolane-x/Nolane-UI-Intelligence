"""Provider-neutral orchestration primitives for NUI V11 Phase 5 Live Visual Runtime.

This coordinator composes source attribution, immutable preview preparation,
preview freshness, and the existing conflict-safe source mutation boundary. It
deliberately does not own browser transport internals, taste decisions, or
release authority.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

from .live import transactional_replace
from .preview import (
    assess_preview_freshness,
    build_preview_candidate,
    prepare_preview_application,
    validate_preview_candidate,
)
from .source_attribution import resolve_source_attribution, select_source_candidate


def _text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def assess_visual_observation_capabilities(
    requirements: dict[str, list[str]],
    available: dict[str, bool],
) -> dict[str, Any]:
    """Evaluate capability completeness per assertion instead of globally.

    Missing capability for one assertion leaves only that assertion UNKNOWN.
    This function is evidence bookkeeping and cannot grant product authority.
    """
    if not isinstance(requirements, dict):
        raise TypeError("visual capability requirements must be an object")
    if not isinstance(available, dict):
        raise TypeError("visual capability availability must be an object")

    normalized_available: dict[str, bool] = {}
    for name, value in available.items():
        if not _text(name) or not isinstance(value, bool):
            raise ValueError("available visual capabilities must map non-empty names to booleans")
        normalized_available[str(name).strip()] = value

    assertions: dict[str, str] = {}
    missing_by_assertion: dict[str, list[str]] = {}
    for assertion in sorted(requirements):
        required = requirements[assertion]
        if not _text(assertion):
            raise ValueError("visual capability assertion names must be non-empty strings")
        if not isinstance(required, list) or any(not _text(item) for item in required):
            raise ValueError(f"visual capability requirements for {assertion} must be a list of non-empty strings")
        required_names = sorted(set(str(item).strip() for item in required))
        missing = [name for name in required_names if normalized_available.get(name) is not True]
        assertions[str(assertion)] = "UNKNOWN" if missing else "READY"
        missing_by_assertion[str(assertion)] = missing

    overall = "READY" if all(value == "READY" for value in assertions.values()) else "UNKNOWN"
    return {
        "status": overall,
        "assertions": assertions,
        "missing_by_assertion": missing_by_assertion,
        "claim_boundary": "live-visual-closure-only",
    }


def prepare_live_visual_selection(
    rendered_identity: dict[str, Any],
    candidates: list[dict[str, Any]],
    *,
    repository_root: str | Path,
    candidate_id: str | None = None,
) -> dict[str, Any]:
    """Resolve a rendered target to a mutation-safe source selection.

    Ambiguous/candidate states remain blocked unless an explicit candidate ID is
    supplied. UNKNOWN never becomes mutation authority.
    """
    attribution = resolve_source_attribution(
        rendered_identity,
        candidates,
        repository_root=repository_root,
    )

    status = attribution["status"]
    if status == "UNKNOWN":
        return {
            "status": "BLOCKED",
            "failure": "ATTRIBUTION_UNKNOWN",
            "attribution": attribution,
            "claim_boundary": "live-visual-closure-only",
        }

    if status in {"CANDIDATE", "AMBIGUOUS"}:
        if candidate_id is None:
            failure = (
                "ATTRIBUTION_AMBIGUOUS"
                if status == "AMBIGUOUS"
                else "ATTRIBUTION_CANDIDATE_SELECTION_REQUIRED"
            )
            return {
                "status": "BLOCKED",
                "failure": failure,
                "attribution": attribution,
                "claim_boundary": "live-visual-closure-only",
            }
        attribution = select_source_candidate(attribution, candidate_id)
    elif candidate_id is not None and candidate_id != attribution.get("selected_candidate_id"):
        attribution = select_source_candidate(attribution, candidate_id)

    selected_id = attribution.get("selected_candidate_id")
    selected = next(
        (item for item in attribution["candidates"] if item.get("candidate_id") == selected_id),
        None,
    )
    if selected is None or attribution.get("mutation_authorized") is not True:
        return {
            "status": "BLOCKED",
            "failure": "ATTRIBUTION_UNKNOWN",
            "attribution": attribution,
            "claim_boundary": "live-visual-closure-only",
        }

    return {
        "status": "READY",
        "failure": None,
        "attribution": attribution,
        "source_candidate": selected,
        "claim_boundary": "live-visual-closure-only",
    }


def prepare_live_visual_preview(
    selection: dict[str, Any],
    *,
    preview_id: str,
    session_id: str,
    replacement: str,
    transport_capability: dict[str, Any],
    repository_root: str | Path,
    preserve_constraints: list[str] | None = None,
    direction_id: str | None = None,
    provenance: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Prepare a non-destructive preview and negotiate transport capability.

    The function never invokes a provider or mutates canonical source. READY
    means the immutable preview record may be handed to a compatible adapter;
    actual browser injection and refresh evidence are separate operations.
    """
    if not isinstance(selection, dict) or selection.get("status") != "READY":
        raise ValueError("live visual preview preparation requires a READY source selection")
    source_candidate = selection.get("source_candidate")
    if not isinstance(source_candidate, dict):
        raise ValueError("live visual preview preparation requires source_candidate")

    preview = build_preview_candidate(
        preview_id=preview_id,
        session_id=session_id,
        source_candidate=source_candidate,
        replacement=replacement,
        preserve_constraints=preserve_constraints,
        direction_id=direction_id,
        provenance=provenance,
    )
    freshness = assess_preview_freshness(preview, repository_root)
    if freshness["status"] != "CURRENT":
        return {
            "status": "UNKNOWN" if freshness["status"] == "STALE" else "BLOCKED",
            "failure": freshness.get("failure"),
            "preview": preview,
            "freshness": freshness,
            "claim_boundary": "live-visual-closure-only",
        }

    application = prepare_preview_application(preview, transport_capability)
    if application["status"] != "READY":
        return {
            "status": "UNKNOWN",
            "failure": "TRANSPORT_CAPABILITY_INCOMPLETE",
            "missing_capabilities": list(application.get("missing_capabilities", [])),
            "preview": application["preview"],
            "freshness": freshness,
            "claim_boundary": "live-visual-closure-only",
        }

    return {
        "status": "READY",
        "failure": None,
        "missing_capabilities": [],
        "preview": application["preview"],
        "provider": application["provider"],
        "freshness": freshness,
        "claim_boundary": "live-visual-closure-only",
    }


def accept_live_visual_preview(
    preview: dict[str, Any],
    *,
    repository_root: str | Path,
) -> dict[str, Any]:
    """Apply an explicitly observed preview through the existing mutation guard.

    This is intentionally not visual closure: callers still need fresh browser
    observation and runtime re-observation after a successful apply.
    """
    validation = validate_preview_candidate(preview)
    if not validation["valid"]:
        raise ValueError("invalid live visual preview: " + "; ".join(validation["errors"]))
    if preview.get("state") != "OBSERVED":
        raise ValueError("live visual accept requires an OBSERVED preview")

    freshness = assess_preview_freshness(preview, repository_root)
    if freshness["status"] != "CURRENT":
        failure = "SOURCE_STALE" if freshness["status"] == "STALE" else str(freshness.get("failure") or "APPLY_CONFLICT")
        return {
            "status": "APPLY_CONFLICT",
            "failure": failure,
            "freshness": freshness,
            "claim_boundary": "live-visual-closure-only",
        }

    root = Path(repository_root).resolve(strict=True)
    candidate = preview["source_candidate"]
    source_range = candidate.get("range")
    if not isinstance(source_range, dict):
        raise ValueError("live visual accept requires a bounded source candidate range")
    target = (root / candidate["source_path"]).resolve(strict=True)
    try:
        target.relative_to(root)
    except ValueError as exc:
        raise ValueError("live visual source target escapes repository root") from exc

    transaction = transactional_replace(
        target,
        preview["base_source_digest"],
        source_range["start"],
        source_range["end"],
        preview["replacement"],
    )
    if transaction.get("status") != "APPLIED":
        return {
            "status": "APPLY_CONFLICT",
            "failure": "APPLY_CONFLICT",
            "transaction": transaction,
            "claim_boundary": "live-visual-closure-only",
        }

    return {
        "status": "APPLIED",
        "failure": None,
        "transaction": transaction,
        "requires_fresh_observation": True,
        "claim_boundary": "live-visual-closure-only",
    }


__all__ = [
    "accept_live_visual_preview",
    "assess_visual_observation_capabilities",
    "prepare_live_visual_preview",
    "prepare_live_visual_selection",
]
