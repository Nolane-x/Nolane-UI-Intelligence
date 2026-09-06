"""Authority-safe promotion from v3 journey hypotheses to v2 contracts."""
from __future__ import annotations

from copy import deepcopy
from typing import Any, Iterable

from .goal_graph import normalize_ux_goal_graph
from .journeys import validate_ux_journey_spec
from .product_model import normalize_ux_product_model
from .provenance import UX_PROVENANCE


def _gap(code: str, field: str, because: str) -> dict[str, str]:
    return {"code": code, "field": field, "because": because}


def _strings(value: Any, label: str, *, allow_empty: bool = True) -> tuple[str, ...]:
    if not isinstance(value, (tuple, list)):
        raise TypeError(f"{label} must be a sequence")
    if not allow_empty and not value:
        raise ValueError(f"{label} must not be empty")
    out: list[str] = []
    for index, item in enumerate(value):
        if not isinstance(item, str) or not item.strip():
            raise ValueError(f"{label}[{index}] must be a non-empty string")
        out.append(item.strip())
    return tuple(out)


def promote_ux_journey_candidate(
    candidate: dict[str, Any],
    product_model: dict[str, Any],
    goal_graph: dict[str, Any],
    *,
    provenance_catalog: Iterable[dict[str, Any]] = UX_PROVENANCE,
) -> dict[str, Any]:
    """Promote only evidence-complete hypotheses; otherwise return stable gaps."""
    if not isinstance(candidate, dict):
        raise TypeError("candidate must be an object")

    model = normalize_ux_product_model(product_model, provenance_catalog=provenance_catalog)
    graph = normalize_ux_goal_graph(goal_graph, provenance_catalog=provenance_catalog)
    if model["product_id"] != graph["product_id"] or model["revision"] != graph["revision"]:
        raise ValueError("product model and goal graph must describe the same product revision")
    if candidate.get("product_id") != model["product_id"] or candidate.get("revision") != model["revision"]:
        raise ValueError("candidate must describe the same product revision")

    candidate_id = candidate.get("candidate_id")
    if not isinstance(candidate_id, str) or not candidate_id.strip():
        raise ValueError("candidate_id must be a non-empty string")

    nodes = {item["node_id"]: item for item in graph["nodes"]}
    actions = {item["action_id"]: item for item in model["actions"]}
    surfaces = {item["surface_id"]: item for item in model["surfaces"]}
    outcomes = {item["outcome_id"]: item for item in model.get("outcomes", ())}
    gaps: list[dict[str, str]] = []

    goal_id = candidate.get("goal_node_id")
    goal = nodes.get(goal_id) if isinstance(goal_id, str) else None
    if goal is None or goal.get("kind") != "goal":
        gaps.append(_gap("goal-unresolved", "goal_node_id", "candidate goal must resolve to a goal node in the current graph"))
    elif goal["origin"] != "declared":
        gaps.append(_gap("goal-not-declared", "goal_node_id", "authoritative v2 promotion requires an explicitly declared goal"))

    raw_steps = candidate.get("step_hypotheses")
    if not isinstance(raw_steps, (tuple, list)) or not raw_steps:
        gaps.append(_gap("journey-steps-unproven", "step_hypotheses", "promotion requires at least one evidenced candidate step"))
        raw_steps = ()

    promoted_steps: list[dict[str, Any]] = []
    for index, raw_step in enumerate(raw_steps):
        field_prefix = f"step_hypotheses[{index}]"
        if not isinstance(raw_step, dict):
            gaps.append(_gap("step-invalid", field_prefix, "candidate step must be an object"))
            continue
        step_id = raw_step.get("candidate_step_id")
        if not isinstance(step_id, str) or not step_id.strip():
            gaps.append(_gap("step-id-unproven", field_prefix, "candidate step requires a stable non-empty id"))
            continue
        action_id = raw_step.get("action_id")
        action = actions.get(action_id) if isinstance(action_id, str) else None
        if action is None:
            gaps.append(_gap("action-unresolved", str(action_id or step_id), "promoted steps must resolve to an action in the current product model"))
            continue
        if action["origin"] not in {"declared", "observed"}:
            gaps.append(_gap("action-inferred-only", action_id, "promoted steps require declared or observed action evidence"))

        try:
            targets = _strings(raw_step.get("expected_target_surface_ids"), f"{step_id}.expected_target_surface_ids", allow_empty=False)
        except (TypeError, ValueError):
            targets = ()
            gaps.append(_gap("expected-transition-unproven", step_id, "promoted steps require explicit target-surface evidence"))
        expected_transition: dict[str, Any] = {}
        if len(targets) > 1:
            gaps.append(_gap("expected-transition-ambiguous", step_id, "v2 promotion will not guess among multiple target surfaces"))
        elif len(targets) == 1:
            target = surfaces.get(targets[0])
            locator = target.get("locator") if target else None
            if target is None or target.get("origin") not in {"declared", "observed"} or not isinstance(locator, str) or not locator.strip():
                gaps.append(_gap("expected-transition-unproven", step_id, "target surface must be declared or observed and have a locator"))
            else:
                expected_transition = {"route": locator}

        try:
            recovery_values = _strings(raw_step.get("recovery_hypotheses"), f"{step_id}.recovery_hypotheses", allow_empty=False)
        except (TypeError, ValueError):
            recovery_values = ()
            gaps.append(_gap("recovery-expectation-unproven", step_id, "v2 requires a non-empty recovery expectation and v3 may not invent one"))

        try:
            required_context = tuple(sorted(set(_strings(raw_step.get("required_context_hypotheses", ()), f"{step_id}.required_context_hypotheses"))))
            preserved_context = tuple(sorted(set(_strings(raw_step.get("preserved_context_hypotheses", ()), f"{step_id}.preserved_context_hypotheses"))))
        except (TypeError, ValueError):
            required_context = ()
            preserved_context = ()
            gaps.append(_gap("context-semantics-invalid", step_id, "context hypotheses must contain only explicit non-empty field names"))

        intent = raw_step.get("intent_hypothesis")
        if not isinstance(intent, str) or not intent.strip():
            gaps.append(_gap("step-intent-unproven", step_id, "promoted step requires an explicit candidate intent label"))

        if expected_transition and recovery_values and isinstance(intent, str) and intent.strip():
            evidence_requirements = tuple(sorted(set(expected_transition) | set(required_context) | set(preserved_context)))
            promoted_steps.append({
                "step_id": step_id,
                "intent": intent.strip(),
                "action": action_id,
                "expected_transition": expected_transition,
                "required_context": required_context,
                "preserved_context": preserved_context,
                "allowed_detours": (),
                "recovery_expectation": " | ".join(recovery_values),
                "evidence_requirements": evidence_requirements,
            })

    raw_success = candidate.get("success_hypotheses")
    success_criteria: list[str] = []
    if not isinstance(raw_success, (tuple, list)) or not raw_success:
        gaps.append(_gap("success-criteria-unproven", "success_hypotheses", "promotion requires at least one declared or observed success hypothesis"))
    else:
        for index, hypothesis in enumerate(raw_success):
            field = f"success_hypotheses[{index}]"
            if not isinstance(hypothesis, dict):
                gaps.append(_gap("success-criteria-unproven", field, "success hypothesis must be an object"))
                continue
            outcome_id = hypothesis.get("outcome_id")
            outcome = outcomes.get(outcome_id) if isinstance(outcome_id, str) else None
            if outcome is None or outcome.get("origin") not in {"declared", "observed"}:
                gaps.append(_gap("success-criteria-unproven", field, "success outcome must resolve to declared or observed product evidence"))
                continue
            if hypothesis.get("surface_id") != outcome.get("surface_id"):
                gaps.append(_gap("success-criteria-mismatch", field, "candidate success surface must match the current product outcome"))
                continue
            success_criteria.append(outcome_id)

    try:
        critical_state = tuple(sorted(set(_strings(candidate.get("critical_state_hypotheses"), "critical_state_hypotheses", allow_empty=False))))
    except (TypeError, ValueError):
        critical_state = ()
        gaps.append(_gap("critical-state-unproven", "critical_state_hypotheses", "promotion requires explicit critical-state semantics"))

    known_provenance = {item["provenance_id"] for item in provenance_catalog}
    inherited_provenance = tuple(sorted((
        set(candidate.get("provenance_ids", ()))
        | set(model.get("provenance_ids", ()))
        | set(graph.get("provenance_ids", ()))
    ) & known_provenance))
    if not inherited_provenance:
        gaps.append(_gap("provenance-unproven", "provenance_ids", "promotion must retain at least one resolved provenance record"))

    gaps.sort(key=lambda item: (item["code"], item["field"]))
    if gaps:
        return {"status": "promotion-gaps", "candidate_id": candidate_id, "journey": None, "promotion_gaps": tuple(gaps)}

    assert goal is not None
    journey = {
        "journey_id": "uxj:" + candidate_id.split(":", 1)[-1],
        "title": candidate["title"] if isinstance(candidate.get("title"), str) and candidate["title"].strip() else goal["label"],
        "user_goal": goal["label"],
        "entry_state": deepcopy(candidate.get("entry_state", {})),
        "steps": tuple(promoted_steps),
        "success_criteria": tuple(sorted(set(success_criteria))),
        "critical_state": critical_state,
        "provenance_ids": inherited_provenance,
        "status": "experimental",
    }
    validate_ux_journey_spec(journey, provenance_catalog=provenance_catalog)
    return {"status": "promoted", "candidate_id": candidate_id, "journey": journey, "promotion_gaps": ()}


__all__ = ["promote_ux_journey_candidate"]
