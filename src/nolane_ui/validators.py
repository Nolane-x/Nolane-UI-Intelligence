"""Small deterministic validators for NUI contracts.

These functions intentionally validate only machine-checkable invariants. They do
not pretend to score beauty, usability, or accessibility from JSON alone.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Iterable

ALLOWED_TOKEN_TIERS = {"primitive", "semantic", "component", "context"}
RELEASE_OBLIGATION_STATUSES = {"PASS", "ACCEPTED_RISK"}
RESOLVED_FINDING_STATUSES = {"repaired", "accepted-risk", "not-reproducible"}
BANNED_PLACEHOLDERS = re.compile(r"\b(TODO|TBD|fill this in|implement later)\b", re.I)


def _load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    meta: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip().strip('"').strip("'")
    return meta


def validate_skill_graph(graph: dict[str, Any], skill_names: Iterable[str]) -> list[str]:
    errors: list[str] = []
    declared = graph.get("skills")
    if not isinstance(declared, dict) or not declared:
        return ["skill graph must declare a non-empty skills object"]

    actual = set(skill_names)
    for name, node in declared.items():
        if name not in actual:
            errors.append(f"skill {name} is declared but its implementation is missing")
        if not isinstance(node, dict):
            errors.append(f"skill {name} node must be an object")
            continue
        parent = node.get("parent")
        if parent is not None and parent not in declared:
            errors.append(f"skill {name} references unknown parent {parent}")

    undeclared = actual - set(declared)
    for name in sorted(undeclared):
        errors.append(f"skill {name} exists on disk but is not declared in graph")

    # Parent graph must be acyclic.
    for start in declared:
        seen: set[str] = set()
        current: str | None = start
        while current is not None and current in declared:
            if current in seen:
                errors.append(f"parent cycle detected from skill {start} through {current}")
                break
            seen.add(current)
            parent = declared[current].get("parent") if isinstance(declared[current], dict) else None
            current = parent

    lifecycle = graph.get("lifecycle", [])
    if len(lifecycle) != len(set(lifecycle)):
        errors.append("lifecycle contains duplicate states")
    if lifecycle and (lifecycle[0] != "INTAKE" or lifecycle[-1] != "RELEASED"):
        errors.append("lifecycle must begin at INTAKE and end at RELEASED")
    if "RECOVERY" not in graph.get("exception_states", []):
        errors.append("exception states must include RECOVERY")
    return errors


def validate_state_matrix(matrix: dict[str, Any]) -> dict[str, Any]:
    required = set(matrix.get("required_states", []))
    applicable = set(matrix.get("applicable_states", []))
    inapplicable = set(matrix.get("explicitly_inapplicable", []))
    accounted = applicable | inapplicable
    unaccounted = sorted(required - accounted)
    contradictions = sorted(applicable & inapplicable)
    errors: list[str] = []
    if unaccounted:
        errors.append(f"required states are unaccounted: {unaccounted}")
    if contradictions:
        errors.append(f"states cannot be both applicable and inapplicable: {contradictions}")

    known = required | applicable | inapplicable
    for transition in matrix.get("transitions", []):
        if not isinstance(transition, dict):
            errors.append("transition must be an object")
            continue
        for key in ("from", "to"):
            state = transition.get(key)
            if state not in known:
                errors.append(f"transition references undeclared state {state!r}")

    return {
        "valid": not errors,
        "errors": errors,
        "unaccounted_states": unaccounted,
        "contradictory_states": contradictions,
    }


def validate_tokens(model: dict[str, Any]) -> dict[str, Any]:
    tokens = model.get("tokens", {})
    if not isinstance(tokens, dict):
        return {"valid": False, "errors": ["tokens must be an object"], "invalid_tiers": [], "cycles": []}

    invalid_tiers: list[str] = []
    errors: list[str] = []
    for name, token in tokens.items():
        if not isinstance(token, dict):
            errors.append(f"token {name} must be an object")
            continue
        if token.get("tier") not in ALLOWED_TOKEN_TIERS:
            invalid_tiers.append(name)
        alias = token.get("alias")
        if alias is not None and alias not in tokens:
            errors.append(f"token {name} aliases missing token {alias}")

    cycles: list[list[str]] = []
    for start in tokens:
        order: list[str] = []
        index: dict[str, int] = {}
        current: str | None = start
        while current is not None and current in tokens:
            if current in index:
                cycle = order[index[current] :] + [current]
                canonical = tuple(cycle)
                if not any(set(c) == set(cycle) for c in cycles):
                    cycles.append(list(canonical))
                break
            index[current] = len(order)
            order.append(current)
            token = tokens[current]
            current = token.get("alias") if isinstance(token, dict) else None

    if invalid_tiers:
        errors.append(f"invalid token tiers: {sorted(invalid_tiers)}")
    if cycles:
        errors.append(f"token alias cycles detected: {cycles}")
    return {"valid": not errors, "errors": errors, "invalid_tiers": sorted(invalid_tiers), "cycles": cycles}


def validate_completion_packet(packet: dict[str, Any], root: Path | str) -> dict[str, Any]:
    errors: list[str] = []
    required = {
        "packet_id", "phase", "task_profile", "obligations", "evidence",
        "findings", "checks", "claim", "bounds", "unknowns",
    }
    missing = sorted(required - set(packet))
    if missing:
        errors.append(f"completion packet missing fields: {missing}")

    if packet.get("phase") != "VERIFIED":
        errors.append("completion packet phase must be VERIFIED")

    for obligation in packet.get("obligations", []):
        status = obligation.get("status") if isinstance(obligation, dict) else None
        if status not in RELEASE_OBLIGATION_STATUSES:
            oid = obligation.get("id", "<unknown>") if isinstance(obligation, dict) else "<invalid>"
            errors.append(f"obligation {oid} is unresolved with status {status}")

    for evidence in packet.get("evidence", []):
        result = evidence.get("result") if isinstance(evidence, dict) else None
        eid = evidence.get("evidence_id", "<unknown>") if isinstance(evidence, dict) else "<invalid>"
        if result == "UNKNOWN":
            errors.append(f"evidence {eid} is UNKNOWN and cannot close a release obligation")
        elif result != "PASS":
            errors.append(f"evidence {eid} is not PASS: {result}")

    for finding in packet.get("findings", []):
        if not isinstance(finding, dict):
            errors.append("finding record must be an object")
            continue
        severity = finding.get("severity")
        status = finding.get("status")
        if severity in {"critical", "major"} and status not in RESOLVED_FINDING_STATUSES:
            errors.append(
                f"{severity} finding {finding.get('finding_id', '<unknown>')} remains unresolved with status {status}"
            )

    bounds = packet.get("bounds")
    if not isinstance(bounds, list) or not any(str(item).strip() for item in bounds):
        errors.append("completion claim must include at least one explicit bound")

    checks = packet.get("checks")
    if not isinstance(checks, dict) or any(value != "PASS" for value in checks.values()):
        errors.append("all declared deterministic checks must be PASS")

    accepted_risk = any(
        isinstance(item, dict) and item.get("status") == "ACCEPTED_RISK"
        for item in packet.get("obligations", [])
    )
    decision = "BLOCKED" if errors else ("PASS_WITH_ACCEPTED_RISK" if accepted_risk else "PASS")
    return {"decision": decision, "errors": errors, "root": str(Path(root))}


def validate_repository(root: Path | str) -> dict[str, Any]:
    root = Path(root)
    errors: list[str] = []
    warnings: list[str] = []

    required_paths = [
        "README.md", "AGENTS.md", "nui.config.json", "skills/skill-graph.json",
        "schemas/ui-task-profile.schema.json", "schemas/finding.schema.json",
        "schemas/evidence.schema.json", "schemas/completion-packet.schema.json",
    ]
    for relative in required_paths:
        if not (root / relative).is_file():
            errors.append(f"missing required repository file: {relative}")

    graph_path = root / "skills/skill-graph.json"
    graph: dict[str, Any] = {}
    if graph_path.is_file():
        try:
            graph = _load_json(graph_path)
        except Exception as exc:
            errors.append(f"invalid skill graph JSON: {exc}")

    disk_skills: set[str] = set()
    skill_root = root / "skills"
    if skill_root.is_dir():
        for child in skill_root.iterdir():
            if child.is_dir() and (child / "SKILL.md").is_file():
                disk_skills.add(child.name)

    if graph:
        errors.extend(validate_skill_graph(graph, disk_skills))
        for name, node in graph.get("skills", {}).items():
            path = root / "skills" / name / "SKILL.md"
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8")
            meta = _parse_frontmatter(text)
            if meta.get("name") != name:
                errors.append(f"skill {name} frontmatter name mismatch")
            description = meta.get("description", "")
            if not description.startswith("Use when"):
                errors.append(f"skill {name} description must start with 'Use when'")
            if len(description) > 500:
                errors.append(f"skill {name} description exceeds 500 characters")
            parent = node.get("parent") if isinstance(node, dict) else None
            if parent is not None:
                if "## Parent Contract" not in text:
                    errors.append(f"skill {name} is missing Parent Contract section")
                if parent not in text:
                    errors.append(f"skill {name} does not name parent {parent}")
            if BANNED_PLACEHOLDERS.search(text):
                errors.append(f"skill {name} contains placeholder language")

    for path in sorted((root / "schemas").glob("*.json")) if (root / "schemas").is_dir() else []:
        try:
            _load_json(path)
        except Exception as exc:
            errors.append(f"invalid schema JSON {path.relative_to(root)}: {exc}")

    eval_count = 0
    if (root / "evals").is_dir():
        for path in sorted((root / "evals").rglob("*.json")):
            eval_count += 1
            try:
                _load_json(path)
            except Exception as exc:
                errors.append(f"invalid eval JSON {path.relative_to(root)}: {exc}")

    if not disk_skills:
        warnings.append("no skill implementations were found")

    return {
        "valid": not errors,
        "errors": errors,
        "warnings": warnings,
        "metrics": {
            "skill_count": len(disk_skills),
            "declared_skill_count": len(graph.get("skills", {})) if graph else 0,
            "eval_json_files": eval_count,
        },
    }
