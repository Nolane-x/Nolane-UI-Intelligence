"""Selective bridge from UX cognition records to existing canonical NUI skills.

The v1 UX registry and the repository skill graph have different purposes.  The
registry names fine-grained reasoning operations; the canonical graph names
agent-executable skill contracts.  V2 links the two explicitly instead of
silently cloning every cognition record into another SKILL.md node.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any, Iterable

from .skills import UX_SKILLS


FORBIDDEN_QUOTA_FIELDS = {
    "minimum_rule_count",
    "target_rule_count",
    "rule_quota",
    "minimum_skill_count",
    "target_skill_count",
    "skill_quota",
}


UX_CANONICAL_SKILL_BRIDGE = tuple(sorted((
    {
        "skill_id": "assessing-recovery-completeness",
        "canonical_slug": "critiquing-user-experience",
        "canonical_path": "skills/critiquing-user-experience/SKILL.md",
        "reason_for_canonicalization": "Recovery completeness is an evidence-backed UX critique operation, so the existing independent UX critic is the canonical execution surface rather than a duplicate recovery-only skill node.",
        "required_outputs": ("recovery-completeness-assessment", "evidence-backed-finding-set"),
        "supported_mechanisms": ("context-loss", "cross-step-inconsistency", "state-without-explanation"),
        "verification_dependencies": ("failure-state-observation", "restored-context-observation", "freshness-evidence"),
    },
    {
        "skill_id": "conducting-cognitive-walkthroughs",
        "canonical_slug": "critiquing-user-experience",
        "canonical_path": "skills/critiquing-user-experience/SKILL.md",
        "reason_for_canonicalization": "The canonical UX critic already walks critical jobs through entry, orientation, decision, action, feedback, recovery, and completion; v2 binds the cognitive-walkthrough operation to that execution contract.",
        "required_outputs": ("step-level-learnability-findings", "uncertainty-and-falsifier-notes"),
        "supported_mechanisms": ("mental-model-mismatch", "navigation-disorientation", "workflow-fragmentation"),
        "verification_dependencies": ("user-task-model", "task-flow-model", "observed-interface-behavior"),
    },
    {
        "skill_id": "evaluating-task-success",
        "canonical_slug": "evaluating-usability-evidence",
        "canonical_path": "skills/evaluating-usability-evidence/SKILL.md",
        "reason_for_canonicalization": "Task success is an evidence judgment about authoritative completion, correctness, error and recovery rather than a new interaction-design surface.",
        "required_outputs": ("task-success-evidence", "bounded-quality-claim"),
        "supported_mechanisms": ("cross-step-inconsistency", "false-completion"),
        "verification_dependencies": ("task-outcome-observation", "completion-authority-evidence", "error-and-recovery-evidence"),
    },
    {
        "skill_id": "identifying-user-goals",
        "canonical_slug": "modeling-users-and-tasks",
        "canonical_path": "skills/modeling-users-and-tasks/SKILL.md",
        "reason_for_canonicalization": "User-goal extraction is a component of the existing canonical user/task model and should strengthen that model instead of creating a parallel goal taxonomy.",
        "required_outputs": ("goal-statement", "goal-success-evidence"),
        "supported_mechanisms": ("goal-displacement",),
        "verification_dependencies": ("product-intent", "representative-task-context", "success-evidence"),
    },
    {
        "skill_id": "mapping-critical-user-journeys",
        "canonical_slug": "designing-task-flows",
        "canonical_path": "skills/designing-task-flows/SKILL.md",
        "reason_for_canonicalization": "Critical journeys are the stateful end-to-end form of the canonical task-flow model; the bridge adds UX-v2 journey semantics without duplicating the graph node.",
        "required_outputs": ("stateful-critical-journey", "normal-interrupted-failed-and-recovery-paths"),
        "supported_mechanisms": ("false-completion", "unrecoverable-progress-loss", "workflow-fragmentation"),
        "verification_dependencies": ("user-goal", "task-state-model", "runtime-observation-plan"),
    },
    {
        "skill_id": "testing-mental-model-alignment",
        "canonical_slug": "critiquing-user-experience",
        "canonical_path": "skills/critiquing-user-experience/SKILL.md",
        "reason_for_canonicalization": "Mental-model alignment becomes actionable when an independent UX critique compares predicted and observed behavior; the existing critic is therefore the canonical execution surface.",
        "required_outputs": ("prediction-mismatch-findings", "observable-consequence-evidence"),
        "supported_mechanisms": ("ambiguous-consequence", "mental-model-mismatch"),
        "verification_dependencies": ("established-user-concepts", "prediction-evidence", "observed-interaction-outcome"),
    },
), key=lambda item: item["skill_id"]))


def _validate_limit(limit: int) -> int:
    if isinstance(limit, bool) or not isinstance(limit, int):
        raise TypeError("limit must be an integer")
    if not 1 <= limit <= 100:
        raise ValueError("limit must be between 1 and 100")
    return limit


def _text_matches(record: dict[str, Any], text: str | None) -> bool:
    if text is None:
        return True
    if not isinstance(text, str):
        raise TypeError("text must be a string or None")
    needle = text.strip().casefold()
    if not needle:
        return True
    values: list[str] = []
    for value in record.values():
        if isinstance(value, str):
            values.append(value)
        elif isinstance(value, (tuple, list)):
            values.extend(str(item) for item in value)
    return needle in " ".join(values).casefold()


def validate_ux_canonical_skill_bridge(
    records: Iterable[dict[str, Any]],
    *,
    skill_registry: Iterable[dict[str, Any]] = UX_SKILLS,
) -> dict[str, Any]:
    records = list(records)
    skills = {item["skill_id"]: item for item in skill_registry}
    seen: set[str] = set()
    errors: list[str] = []
    for index, record in enumerate(records):
        if not isinstance(record, dict):
            raise TypeError(f"UX canonical bridge record {index} must be an object")
        skill_id = record.get("skill_id")
        if not isinstance(skill_id, str) or not skill_id.strip():
            raise ValueError(f"UX canonical bridge record {index}: skill_id must be a non-empty string")
        if skill_id in seen:
            raise ValueError(f"UX canonical bridge: duplicate skill_id {skill_id}")
        seen.add(skill_id)
        if skill_id not in skills:
            raise ValueError(f"UX canonical bridge: unknown UX skill {skill_id}")
        forbidden = set(record) & FORBIDDEN_QUOTA_FIELDS
        if forbidden:
            raise ValueError(f"{skill_id}: count quotas are forbidden: {sorted(forbidden)}")
        for field in ("canonical_slug", "canonical_path", "reason_for_canonicalization"):
            value = record.get(field)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{skill_id}: {field} must be a non-empty string")
        expected_path = f"skills/{record['canonical_slug']}/SKILL.md"
        if record["canonical_path"] != expected_path:
            raise ValueError(f"{skill_id}: canonical_path must equal {expected_path}")
        for field in ("required_outputs", "supported_mechanisms", "verification_dependencies"):
            value = record.get(field)
            if not isinstance(value, (tuple, list)) or not value:
                raise ValueError(f"{skill_id}: {field} must be a non-empty sequence")
            if not all(isinstance(item, str) and item.strip() for item in value):
                raise ValueError(f"{skill_id}: {field} must contain non-empty strings")
        unknown = set(record["supported_mechanisms"]) - set(skills[skill_id]["related_mechanisms"])
        if unknown:
            raise ValueError(f"{skill_id}: unsupported mechanisms {sorted(unknown)}")
    identifiers = [record["skill_id"] for record in records]
    if identifiers != sorted(identifiers):
        raise ValueError("UX canonical bridge must be canonically sorted by skill_id")
    return {"valid": True, "record_count": len(records), "errors": errors}


validate_ux_canonical_skill_bridge(UX_CANONICAL_SKILL_BRIDGE)
_BRIDGE_INDEX = {item["skill_id"]: item for item in UX_CANONICAL_SKILL_BRIDGE}


def get_ux_canonical_skill_bridge(skill_id: str) -> dict[str, Any] | None:
    record = _BRIDGE_INDEX.get(skill_id)
    return deepcopy(record) if record is not None else None


def query_ux_canonical_skill_bridge(
    *,
    mechanism_id: str | None = None,
    canonical_slug: str | None = None,
    text: str | None = None,
    limit: int = 20,
) -> list[dict[str, Any]]:
    _validate_limit(limit)
    records = [
        item
        for item in UX_CANONICAL_SKILL_BRIDGE
        if (mechanism_id is None or mechanism_id in item["supported_mechanisms"])
        and (canonical_slug is None or canonical_slug == item["canonical_slug"])
        and _text_matches(item, text)
    ]
    return deepcopy(records[:limit])


__all__ = [
    "UX_CANONICAL_SKILL_BRIDGE",
    "get_ux_canonical_skill_bridge",
    "query_ux_canonical_skill_bridge",
    "validate_ux_canonical_skill_bridge",
]
