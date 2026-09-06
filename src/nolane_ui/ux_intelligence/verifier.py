"""End-to-end deterministic UX journey verification.

The verifier accepts plain provider-neutral mappings.  Browser transport stays
owned by V11; this module binds supplied observations to explicit journey
expectations and UX rules without importing Playwright or a browser adapter.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any, Iterable

from .evaluators import UX_JOURNEY_EVALUATORS, evaluate_ux_journey_rule
from .journeys import normalize_ux_journey_spec
from .provenance import UX_PROVENANCE
from .rules import UX_RULES


def _step_observations(packet: dict[str, Any]) -> dict[str, dict[str, Any]]:
    raw = packet.get("steps", {})
    if isinstance(raw, dict):
        result: dict[str, dict[str, Any]] = {}
        for key, value in raw.items():
            if not isinstance(key, str) or not isinstance(value, dict):
                raise TypeError("observations.steps must map step ids to objects")
            result[key] = deepcopy(value)
        return result
    if isinstance(raw, (tuple, list)):
        result = {}
        for index, value in enumerate(raw):
            if not isinstance(value, dict):
                raise TypeError(f"observations.steps[{index}] must be an object")
            step_id = value.get("step_id")
            if not isinstance(step_id, str) or not step_id.strip():
                raise ValueError(f"observations.steps[{index}] requires step_id")
            if step_id in result:
                raise ValueError(f"duplicate observation step_id {step_id}")
            result[step_id] = {key: deepcopy(item) for key, item in value.items() if key != "step_id"}
        return result
    raise TypeError("observations.steps must be an object or sequence")


def _finding(
    *,
    journey_id: str,
    step_id: str,
    rule: dict[str, Any],
    observed: Any,
    expected: Any,
    evidence_refs: Iterable[str],
    provenance_ids: Iterable[str],
    verification_mode: str,
) -> dict[str, Any]:
    return {
        "finding_id": f"uxf:{journey_id}:{step_id}:{rule['rule_id']}",
        "journey_id": journey_id,
        "step_id": step_id,
        "rule_id": rule["rule_id"],
        "mechanism_id": rule["mechanism_id"],
        "summary": rule["title"],
        "observed": deepcopy(observed),
        "expected": deepcopy(expected),
        "evidence_refs": tuple(sorted(set(evidence_refs))),
        "provenance_ids": tuple(sorted(set(provenance_ids))),
        "severity": rule["severity"],
        "enforcement": rule["enforcement"],
        "verification_mode": verification_mode,
    }


def _gap(journey_id: str, step_id: str | None, field: str, reason: str) -> dict[str, Any]:
    return {
        "journey_id": journey_id,
        "step_id": step_id,
        "field": field,
        "reason": reason,
    }


def verify_ux_journey(
    journey: dict[str, Any],
    observations: dict[str, Any],
    *,
    rule_catalog: Iterable[dict[str, Any]] = UX_RULES,
    provenance_catalog: Iterable[dict[str, Any]] = UX_PROVENANCE,
) -> dict[str, Any]:
    if not isinstance(observations, dict):
        raise TypeError("UX observations must be an object")
    normalized = normalize_ux_journey_spec(journey, provenance_catalog=provenance_catalog)
    rules = {item["rule_id"]: item for item in rule_catalog}
    provenance_ids = {item["provenance_id"] for item in provenance_catalog}
    required_runtime_provenance = "uxp.v11-runtime-observation"
    if required_runtime_provenance not in provenance_ids:
        raise ValueError("UX verifier requires uxp.v11-runtime-observation provenance")

    step_observations = _step_observations(observations)
    findings: list[dict[str, Any]] = []
    evidence_gaps: list[dict[str, Any]] = []
    step_results: list[dict[str, Any]] = []
    current_context = deepcopy(normalized["entry_state"])

    for step in normalized["steps"]:
        step_id = step["step_id"]
        observation = step_observations.get(step_id)
        contract_failures: list[dict[str, Any]] = []
        evaluator_results: list[dict[str, Any]] = []
        step_findings: list[str] = []

        if observation is None:
            for field in sorted(set(step["evidence_requirements"]) | set(step["expected_transition"]) | set(step["preserved_context"])):
                evidence_gaps.append(_gap(normalized["journey_id"], step_id, field, "step was not executed or observed"))
            step_results.append({
                "step_id": step_id,
                "status": "not-executed",
                "contract_failures": (),
                "finding_ids": (),
                "evaluator_results": (),
            })
            continue

        missing_fields = sorted(
            field
            for field in (set(step["evidence_requirements"]) | set(step["expected_transition"]) | set(step["preserved_context"]))
            if field not in observation
        )
        for field in missing_fields:
            evidence_gaps.append(_gap(normalized["journey_id"], step_id, field, "required step evidence is absent"))

        for field in step["required_context"]:
            if field not in current_context:
                evidence_gaps.append(_gap(normalized["journey_id"], step_id, field, "required incoming context is not evidenced"))

        for field, expected_value in step["expected_transition"].items():
            if field not in observation:
                continue
            observed_value = observation[field]
            allowed_detour = field == "route" and observed_value in set(step["allowed_detours"])
            if observed_value != expected_value and not allowed_detour:
                contract_failures.append({
                    "kind": "expected-transition-mismatch",
                    "field": field,
                    "expected": deepcopy(expected_value),
                    "observed": deepcopy(observed_value),
                })

        for field in step["preserved_context"]:
            if field not in observation or field not in current_context:
                continue
            if observation[field] != current_context[field]:
                contract_failures.append({
                    "kind": "preserved-context-mismatch",
                    "field": field,
                    "expected": deepcopy(current_context[field]),
                    "observed": deepcopy(observation[field]),
                })
                rule = rules.get("ux.task.same-goal-navigation-preserves-context")
                if rule is not None:
                    finding = _finding(
                        journey_id=normalized["journey_id"],
                        step_id=step_id,
                        rule=rule,
                        observed={field: observation[field]},
                        expected={field: current_context[field]},
                        evidence_refs=(field,),
                        provenance_ids=tuple(normalized["provenance_ids"]) + (
                            "uxp.product-journey-contract",
                            "uxp.rule-authority-inheritance",
                            required_runtime_provenance,
                        ),
                        verification_mode="runtime-observation",
                    )
                    findings.append(finding)
                    step_findings.append(finding["finding_id"])

        for evaluator in UX_JOURNEY_EVALUATORS:
            if evaluator["rule_id"] not in rules:
                raise ValueError(f"UX verifier evaluator references unavailable rule {evaluator['rule_id']}")
            result = evaluate_ux_journey_rule(evaluator, step, observation)
            evaluator_results.append({"evaluator_id": evaluator["evaluator_id"], **result})
            if result["status"] == "insufficient-evidence":
                for field in result["missing_evidence"]:
                    evidence_gaps.append(
                        _gap(normalized["journey_id"], step_id, field, f"{evaluator['evaluator_id']} activated without required evidence")
                    )
            elif result["status"] == "fail":
                rule = rules[evaluator["rule_id"]]
                finding = _finding(
                    journey_id=normalized["journey_id"],
                    step_id=step_id,
                    rule=rule,
                    observed=result["observed"],
                    expected=result["expected"],
                    evidence_refs=(field for field in evaluator["required_evidence"] if field in observation),
                    provenance_ids=tuple(normalized["provenance_ids"]) + tuple(evaluator["provenance_ids"]),
                    verification_mode=evaluator["verification_mode"],
                )
                findings.append(finding)
                step_findings.append(finding["finding_id"])

        has_eval_failure = any(item["status"] == "fail" for item in evaluator_results)
        has_eval_gap = any(item["status"] == "insufficient-evidence" for item in evaluator_results)
        if contract_failures or has_eval_failure:
            status = "fail"
        elif missing_fields or has_eval_gap or any(field not in current_context for field in step["required_context"]):
            status = "insufficient-evidence"
        else:
            status = "pass"

        step_results.append({
            "step_id": step_id,
            "status": status,
            "contract_failures": tuple(contract_failures),
            "finding_ids": tuple(step_findings),
            "evaluator_results": tuple(evaluator_results),
        })
        for key, value in observation.items():
            current_context[key] = deepcopy(value)

    success_packet = observations.get("success", {})
    if success_packet is None:
        success_packet = {}
    if not isinstance(success_packet, dict):
        raise TypeError("observations.success must be an object")
    success_results: list[dict[str, Any]] = []
    for criterion in normalized["success_criteria"]:
        if criterion not in success_packet:
            evidence_gaps.append(_gap(normalized["journey_id"], None, criterion, "success criterion evidence is absent"))
            success_results.append({"criterion": criterion, "status": "insufficient-evidence", "observed": None})
        elif success_packet[criterion] is True:
            success_results.append({"criterion": criterion, "status": "pass", "observed": True})
        else:
            success_results.append({"criterion": criterion, "status": "fail", "observed": deepcopy(success_packet[criterion])})

    any_failure = any(item["status"] == "fail" for item in step_results) or any(
        item["status"] == "fail" for item in success_results
    )
    any_gap = any(item["status"] in {"insufficient-evidence", "not-executed"} for item in step_results) or any(
        item["status"] == "insufficient-evidence" for item in success_results
    )
    status = "failed" if any_failure else "insufficient-evidence" if any_gap else "passed"

    return {
        "journey_id": normalized["journey_id"],
        "status": status,
        "step_results": tuple(step_results),
        "findings": tuple(findings),
        "evidence_gaps": tuple(evidence_gaps),
        "success_criteria_results": tuple(success_results),
        "provenance_ids": tuple(sorted(set(normalized["provenance_ids"]) | {required_runtime_provenance})),
    }


__all__ = ["verify_ux_journey"]
