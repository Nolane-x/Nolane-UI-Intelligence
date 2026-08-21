"""Evidence-only routing from runtime findings to existing NUI skill owners.

The runtime layer never creates ownership. It may only resolve rule owner hints
against a supplied canonical skill graph and report unresolved hints explicitly.
"""
from __future__ import annotations

from typing import Any

from .registry import validate_rule_registry


def _unique_strings(values: list[Any]) -> list[str]:
    result: list[str] = []
    seen: set[str] = set()
    for value in values:
        if not isinstance(value, str):
            continue
        item = value.strip()
        if not item or item in seen:
            continue
        seen.add(item)
        result.append(item)
    return result


def _graph_skills(skill_graph: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(skill_graph, dict):
        raise ValueError("skill graph must be an object")
    skills = skill_graph.get("skills")
    if not isinstance(skills, dict):
        raise ValueError("skill graph requires skills object")
    return skills


def _finding_identity(finding: dict[str, Any]) -> tuple[str, str]:
    if not isinstance(finding, dict):
        raise ValueError("runtime finding must be an object")
    finding_id = finding.get("finding_id")
    if not isinstance(finding_id, str) or not finding_id.strip():
        raise ValueError("runtime finding requires finding_id")
    runtime = finding.get("runtime")
    if not isinstance(runtime, dict):
        raise ValueError(f"runtime finding {finding_id} requires runtime object")
    rule_id = runtime.get("rule_id")
    if not isinstance(rule_id, str) or not rule_id.strip():
        raise ValueError(f"runtime finding {finding_id} requires runtime.rule_id")
    return finding_id.strip(), rule_id.strip()


def route_runtime_finding(
    finding: dict[str, Any],
    registry: dict[str, Any],
    skill_graph: dict[str, Any],
) -> dict[str, Any]:
    """Resolve one runtime finding to already-declared NUI owners.

    `owner_hints` are suggestions owned by the runtime rule. They acquire no
    authority from appearing there: only slugs already present in the supplied
    skill graph can become resolved owners.
    """
    finding_id, rule_id = _finding_identity(finding)
    validation = validate_rule_registry(registry)
    if not validation["valid"]:
        raise ValueError("invalid runtime rule registry: " + "; ".join(validation["errors"]))
    skills = _graph_skills(skill_graph)

    rule = next((item for item in registry["rules"] if item.get("rule_id") == rule_id), None)
    if rule is None:
        return {
            "finding_id": finding_id,
            "rule_id": rule_id,
            "status": "UNKNOWN_RULE",
            "owners": [],
            "unresolved_owner_hints": [],
            "evidence_only": True,
            "reason": "Finding rule_id is not present in the supplied runtime registry; no owner was inferred.",
        }

    hints = _unique_strings(rule.get("owner_hints", []))
    owners = [hint for hint in hints if hint in skills]
    unresolved = [hint for hint in hints if hint not in skills]

    if owners:
        status = "ROUTED"
        reason = "Resolved only owner hints already declared in the supplied canonical skill graph."
    else:
        status = "UNRESOLVED"
        reason = "No runtime owner hint resolves to an existing canonical skill; ownership was not invented."

    return {
        "finding_id": finding_id,
        "rule_id": rule_id,
        "status": status,
        "owners": owners,
        "unresolved_owner_hints": unresolved,
        "evidence_only": True,
        "reason": reason,
    }


def route_runtime_findings(
    findings: list[dict[str, Any]],
    registry: dict[str, Any],
    skill_graph: dict[str, Any],
) -> dict[str, Any]:
    """Route a batch deterministically without turning routing into authority."""
    if not isinstance(findings, list):
        raise ValueError("runtime findings must be a list")
    routes = [route_runtime_finding(finding, registry, skill_graph) for finding in findings]
    routes.sort(key=lambda item: (item["finding_id"], item["rule_id"]))
    return {
        "routes": routes,
        "route_count": len(routes),
        "unresolved_route_count": sum(item["status"] != "ROUTED" for item in routes),
        "unresolved_hint_count": sum(len(item["unresolved_owner_hints"]) for item in routes),
        "evidence_only": True,
    }


__all__ = ["route_runtime_finding", "route_runtime_findings"]
