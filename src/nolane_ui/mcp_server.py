"""Optional MCP exposure for current Nolane UI Intelligence.

The module remains importable without the MCP SDK. When installed with the
``mcp`` extra, :func:`run_server` exposes bounded local read/analysis tools.
It deliberately contains no arbitrary shell executor, remote URL fetcher, or
third-party installer; those permissions remain with the host agent.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .interop import build_agent_install_plan
from .rules_v13.catalog import (
    get_rule_provenance_v13,
    get_rule_v13,
    query_rules_v13,
    rule_catalog_status_v13,
)
from .runtime_v11.doctor import diagnose_runtime_state
from .ux_intelligence import (
    get_ux_canonical_skill_bridge,
    get_ux_mechanism,
    get_ux_provenance,
    get_ux_rule,
    get_ux_skill,
    build_ux_product_model,
    build_ux_goal_graph,
    discover_ux_journeys,
    query_ux_journey_candidates,
    promote_ux_journey_candidate,
    plan_ux_discovery,
    create_ux_evidence_snapshot,
    compare_ux_snapshots,
    rank_ux_impacts,
    query_ux_canonical_skill_bridge,
    query_ux_mechanisms,
    query_ux_provenance,
    query_ux_rules,
    query_ux_skills,
    ux_intelligence_status,
    ux_v2_status,
    ux_v3_status,
    verify_ux_journey,
)
from .validators import validate_repository


def _load(root: Path, relative: str) -> Any:
    return json.loads((root / relative).read_text(encoding="utf-8"))


def get_status(root: Path | str) -> dict[str, Any]:
    root = Path(root).resolve()
    result = validate_repository(root)
    return {
        "name": "Nolane UI Intelligence",
        "version": _load(root, "nui.config.json").get("version"),
        "valid": result.get("valid", False),
        "metrics": result.get("metrics", {}),
        "errors": result.get("errors", [])[:20],
        "root": str(root),
    }


def get_media_sources(root: Path | str) -> dict[str, Any]:
    root = Path(root).resolve()
    data = _load(root, "knowledge/visual-media-sources-v8.json")
    return {"version": data.get("version"), "principle": data.get("principle"), "sources": data.get("sources", [])}


def get_creative_tools(root: Path | str) -> dict[str, Any]:
    root = Path(root).resolve()
    data = _load(root, "knowledge/creative-toolchain-v8.json")
    return {"version": data.get("version"), "principle": data.get("principle"), "tools": data.get("tools", [])}


def get_skill(root: Path | str, skill_name: str) -> dict[str, Any]:
    root = Path(root).resolve()
    graph = _load(root, "skills/skill-graph.json").get("skills", {})
    if skill_name not in graph:
        raise ValueError(f"unknown canonical NUI skill: {skill_name}")
    path = (root / "skills" / skill_name / "SKILL.md").resolve()
    skill_root = (root / "skills").resolve()
    if skill_root not in path.parents:
        raise ValueError("skill path escaped canonical skill root")
    return {"name": skill_name, "metadata": graph[skill_name], "content": path.read_text(encoding="utf-8")}


def get_rule_record(root: Path | str, rule_id: str) -> dict[str, Any]:
    rule = get_rule_v13(rule_id, root=Path(root).resolve())
    if rule is None:
        raise ValueError(f"unknown canonical V13 rule: {rule_id}")
    return rule


def query_rule_records(
    root: Path | str,
    *,
    domain: str | None = None,
    rule_class: str | None = None,
    status: str | None = None,
    text: str | None = None,
    limit: int = 25,
) -> dict[str, Any]:
    rules = query_rules_v13(
        root=Path(root).resolve(),
        domain=domain,
        rule_class=rule_class,
        status=status,
        text=text,
        limit=limit,
    )
    return {"count": len(rules), "rules": rules, "limit": limit}


def get_rule_provenance(root: Path | str, provenance_id: str) -> dict[str, Any]:
    record = get_rule_provenance_v13(provenance_id, root=Path(root).resolve())
    if record is None:
        raise ValueError(f"unknown V13 provenance id: {provenance_id}")
    return record


def get_rule_status(root: Path | str) -> dict[str, Any]:
    return rule_catalog_status_v13(Path(root).resolve())


def get_ux_mechanism_record(root: Path | str, mechanism_id: str) -> dict[str, Any]:
    _ = Path(root).resolve()
    record = get_ux_mechanism(mechanism_id)
    if record is None:
        raise ValueError(f"unknown UX mechanism: {mechanism_id}")
    return record


def query_ux_mechanism_records(
    root: Path | str,
    *,
    text: str | None = None,
    limit: int = 25,
) -> dict[str, Any]:
    _ = Path(root).resolve()
    mechanisms = query_ux_mechanisms(text=text, limit=limit)
    return {"count": len(mechanisms), "mechanisms": mechanisms, "limit": limit}


def get_ux_skill_record(root: Path | str, skill_id: str) -> dict[str, Any]:
    _ = Path(root).resolve()
    record = get_ux_skill(skill_id)
    if record is None:
        raise ValueError(f"unknown UX cognitive skill: {skill_id}")
    return record


def query_ux_skill_records(
    root: Path | str,
    *,
    domain: str | None = None,
    mechanism_id: str | None = None,
    text: str | None = None,
    limit: int = 25,
) -> dict[str, Any]:
    _ = Path(root).resolve()
    skills = query_ux_skills(
        domain=domain,
        mechanism_id=mechanism_id,
        text=text,
        limit=limit,
    )
    return {"count": len(skills), "skills": skills, "limit": limit}


def get_ux_rule_record(root: Path | str, rule_id: str) -> dict[str, Any]:
    _ = Path(root).resolve()
    record = get_ux_rule(rule_id)
    if record is None:
        raise ValueError(f"unknown UX rule: {rule_id}")
    return record


def query_ux_rule_records(
    root: Path | str,
    *,
    domain: str | None = None,
    mechanism_id: str | None = None,
    rule_class: str | None = None,
    status: str | None = None,
    text: str | None = None,
    limit: int = 25,
) -> dict[str, Any]:
    _ = Path(root).resolve()
    rules = query_ux_rules(
        domain=domain,
        mechanism_id=mechanism_id,
        rule_class=rule_class,
        status=status,
        text=text,
        limit=limit,
    )
    return {"count": len(rules), "rules": rules, "limit": limit}


def get_ux_status(root: Path | str) -> dict[str, Any]:
    _ = Path(root).resolve()
    return ux_intelligence_status()


def get_ux_provenance_record(provenance_id: str, root: Path | str | None = None) -> dict[str, Any]:
    if root is not None:
        _ = Path(root).resolve()
    record = get_ux_provenance(provenance_id)
    if record is None:
        raise ValueError(f"unknown UX provenance id: {provenance_id}")
    return record


def query_ux_provenance_records(
    root: Path | str | None = None,
    *,
    source_kind: str | None = None,
    verification_mode: str | None = None,
    text: str | None = None,
    limit: int = 25,
) -> dict[str, Any]:
    if root is not None:
        _ = Path(root).resolve()
    records = query_ux_provenance(
        source_kind=source_kind,
        verification_mode=verification_mode,
        text=text,
        limit=limit,
    )
    return {"count": len(records), "provenance": records, "limit": limit}


def get_ux_canonical_skill_bridge_record(skill_id: str, root: Path | str | None = None) -> dict[str, Any]:
    if root is not None:
        _ = Path(root).resolve()
    record = get_ux_canonical_skill_bridge(skill_id)
    if record is None:
        raise ValueError(f"unknown UX canonical bridge skill id: {skill_id}")
    return record


def query_ux_canonical_skill_bridge_records(
    root: Path | str | None = None,
    *,
    mechanism_id: str | None = None,
    canonical_slug: str | None = None,
    text: str | None = None,
    limit: int = 25,
) -> dict[str, Any]:
    if root is not None:
        _ = Path(root).resolve()
    records = query_ux_canonical_skill_bridge(
        mechanism_id=mechanism_id,
        canonical_slug=canonical_slug,
        text=text,
        limit=limit,
    )
    return {"count": len(records), "bridge": records, "limit": limit}


def get_ux_v2_status(root: Path | str | None = None) -> dict[str, Any]:
    if root is not None:
        _ = Path(root).resolve()
    return ux_v2_status()


def verify_ux_journey_record(
    journey: dict[str, Any],
    observations: dict[str, Any],
    root: Path | str | None = None,
) -> dict[str, Any]:
    if root is not None:
        _ = Path(root).resolve()
    return verify_ux_journey(journey, observations)


def get_ux_v3_status(root: Path | str | None = None) -> dict[str, Any]:
    if root is not None:
        _ = Path(root).resolve()
    return ux_v3_status()


def build_ux_product_model_record(packet: dict[str, Any], root: Path | str | None = None) -> dict[str, Any]:
    if root is not None:
        _ = Path(root).resolve()
    return build_ux_product_model(packet)


def build_ux_goal_graph_record(
    product_model: dict[str, Any],
    *,
    declared_goals: list[dict[str, Any]] | tuple[dict[str, Any], ...] = (),
    inferred_goals: list[dict[str, Any]] | tuple[dict[str, Any], ...] = (),
    root: Path | str | None = None,
) -> dict[str, Any]:
    if root is not None:
        _ = Path(root).resolve()
    return build_ux_goal_graph(product_model, declared_goals=declared_goals, inferred_goals=inferred_goals)


def discover_ux_journey_records(
    product_model: dict[str, Any],
    goal_graph: dict[str, Any],
    *,
    max_depth: int = 8,
    root: Path | str | None = None,
) -> dict[str, Any]:
    if root is not None:
        _ = Path(root).resolve()
    candidates = discover_ux_journeys(product_model, goal_graph, max_depth=max_depth)
    return {"count": len(candidates), "candidates": candidates}


def query_ux_journey_candidate_records(
    candidates: list[dict[str, Any]] | tuple[dict[str, Any], ...],
    *,
    goal_node_id: str | None = None,
    status: str | None = None,
    min_score: float | None = None,
    limit: int = 25,
    root: Path | str | None = None,
) -> dict[str, Any]:
    if root is not None:
        _ = Path(root).resolve()
    records = query_ux_journey_candidates(
        candidates, goal_node_id=goal_node_id, status=status, min_score=min_score, limit=limit
    )
    return {"count": len(records), "candidates": records, "limit": limit}


def promote_ux_journey_candidate_record(
    candidate: dict[str, Any],
    product_model: dict[str, Any],
    goal_graph: dict[str, Any],
    root: Path | str | None = None,
) -> dict[str, Any]:
    if root is not None:
        _ = Path(root).resolve()
    return promote_ux_journey_candidate(candidate, product_model, goal_graph)


def plan_ux_discovery_record(
    subject: dict[str, Any],
    available_capabilities: list[str] | tuple[str, ...],
    *,
    limit: int = 25,
    root: Path | str | None = None,
) -> dict[str, Any]:
    if root is not None:
        _ = Path(root).resolve()
    requests = plan_ux_discovery(subject, available_capabilities, limit=limit)
    return {"count": len(requests), "requests": requests, "limit": limit}


def create_ux_evidence_snapshot_record(
    product_id: str,
    revision: str,
    journey: dict[str, Any],
    verification: dict[str, Any],
    *,
    created_from: str,
    provenance_ids: list[str] | tuple[str, ...] = (),
    root: Path | str | None = None,
) -> dict[str, Any]:
    if root is not None:
        _ = Path(root).resolve()
    return create_ux_evidence_snapshot(
        product_id, revision, journey, verification, created_from=created_from, provenance_ids=provenance_ids
    )


def compare_ux_snapshot_records(
    baseline: dict[str, Any],
    candidate: dict[str, Any],
    *,
    history: list[dict[str, Any]] | tuple[dict[str, Any], ...] = (),
    root: Path | str | None = None,
) -> dict[str, Any]:
    if root is not None:
        _ = Path(root).resolve()
    return compare_ux_snapshots(baseline, candidate, history=history)


def rank_ux_impact_records(
    items: list[dict[str, Any]] | tuple[dict[str, Any], ...],
    impact_evidence: dict[str, dict[str, Any]],
    root: Path | str | None = None,
) -> dict[str, Any]:
    if root is not None:
        _ = Path(root).resolve()
    assessments = rank_ux_impacts(items, impact_evidence)
    return {"count": len(assessments), "assessments": assessments}


def get_runtime_doctor(root: Path | str) -> dict[str, Any]:
    return diagnose_runtime_state(Path(root).resolve())


def tool_catalog(root: Path | str | None = None) -> list[dict[str, str]]:
    if root is not None:
        _ = Path(root)
    return [
        {"name": "nui_status", "description": "Validate the local NUI repository and return bounded current-head structural metrics."},
        {"name": "nui_install_plan", "description": "Return a permission-preserving adapter plan for a supported agent harness."},
        {"name": "nui_get_skill", "description": "Read one canonical NUI skill by exact graph name."},
        {"name": "nui_media_sources", "description": "List rights-aware visual-media discovery sources and their caveats."},
        {"name": "nui_creative_tools", "description": "List creative production tools by stage authority and policy boundary."},
        {"name": "nui_rule_status", "description": "Return V13 rule-catalog, provenance, and anti-duplication status without mutating source."},
        {"name": "nui_get_rule", "description": "Read one canonical V13 rule by exact rule id."},
        {"name": "nui_query_rules", "description": "Query at most 100 V13 rules by bounded domain, class, status, or text filters."},
        {"name": "nui_rule_provenance", "description": "Read one exact V13 provenance record and its evidence boundary."},
        {"name": "nui_ux_status", "description": "Return read-only UX Intelligence v1 mechanism, cognitive-skill, rule, and coverage status."},
        {"name": "nui_get_ux_mechanism", "description": "Read one UX semantic failure mechanism by exact id."},
        {"name": "nui_query_ux_mechanisms", "description": "Query at most 100 UX semantic mechanisms by bounded text filter."},
        {"name": "nui_get_ux_skill", "description": "Read one UX cognitive skill registry entry by exact id."},
        {"name": "nui_query_ux_skills", "description": "Query at most 100 UX cognitive skills by bounded domain, mechanism, or text filters."},
        {"name": "nui_get_ux_rule", "description": "Read one UX operational rule by exact id without changing V13 rule authority."},
        {"name": "nui_query_ux_rules", "description": "Query at most 100 UX operational rules by bounded domain, mechanism, class, status, or text filters."},
        {"name": "nui_ux_v2_status", "description": "Return UX v2 bridge, provenance, deterministic evaluator, and authority-boundary integrity status."},
        {"name": "nui_get_ux_provenance", "description": "Read one bounded UX v2 provenance record by exact id."},
        {"name": "nui_query_ux_provenance", "description": "Query at most 100 UX v2 provenance records by source kind, verification mode, or text."},
        {"name": "nui_get_ux_canonical_skill_bridge", "description": "Read one explicit bridge from a UX cognition record to an existing canonical NUI skill."},
        {"name": "nui_query_ux_canonical_skill_bridge", "description": "Query at most 100 UX-to-canonical skill bridge records without modifying the canonical graph."},
        {"name": "nui_verify_ux_journey", "description": "Verify a structured UX journey against provider-neutral runtime observations and return evidence-bounded findings."},
        {"name": "nui_ux_v3_status", "description": "Return UX v3 autonomous-discovery integrity and authority-boundary status."},
        {"name": "nui_build_ux_product_model", "description": "Build an evidence-bounded UX product model from explicit discovery evidence."},
        {"name": "nui_build_ux_goal_graph", "description": "Build a declared/inferred UX goal graph without promoting browser traversal into user intent."},
        {"name": "nui_discover_ux_journeys", "description": "Discover and rank bounded UX journey hypotheses without creating findings."},
        {"name": "nui_query_ux_journey_candidates", "description": "Query bounded UX journey hypotheses by goal, status, and score."},
        {"name": "nui_promote_ux_journey_candidate", "description": "Promote a sufficiently evidenced candidate into the unchanged UX v2 journey contract."},
        {"name": "nui_plan_ux_discovery", "description": "Plan evidence requests only; does not execute a browser or claim observations."},
        {"name": "nui_create_ux_evidence_snapshot", "description": "Create a defensive temporal UX evidence snapshot in memory."},
        {"name": "nui_compare_ux_snapshots", "description": "Compare same-product temporal UX snapshots without escalating finding authority."},
        {"name": "nui_rank_ux_impacts", "description": "Rank verified UX findings/regressions without changing severity or enforcement."},
        {"name": "nui_runtime_doctor", "description": "Run the read-only V11 runtime installation and evidence doctor."},
    ]


def run_server(root: Path | str | None = None) -> None:
    root_path = Path(root).resolve() if root else Path(__file__).resolve().parents[2]
    try:
        from mcp.server.fastmcp import FastMCP  # type: ignore
    except ImportError as exc:
        raise RuntimeError("MCP SDK is optional. Install NUI with the 'mcp' extra: pip install -e '.[mcp]'") from exc
    mcp = FastMCP("nolane-ui-intelligence")

    @mcp.tool()
    def nui_status() -> dict[str, Any]:
        return get_status(root_path)

    @mcp.tool()
    def nui_install_plan(agent_id: str) -> dict[str, Any]:
        return build_agent_install_plan(agent_id, root_path)

    @mcp.tool()
    def nui_get_skill(skill_name: str) -> dict[str, Any]:
        return get_skill(root_path, skill_name)

    @mcp.tool()
    def nui_media_sources() -> dict[str, Any]:
        return get_media_sources(root_path)

    @mcp.tool()
    def nui_creative_tools() -> dict[str, Any]:
        return get_creative_tools(root_path)

    @mcp.tool()
    def nui_rule_status() -> dict[str, Any]:
        return get_rule_status(root_path)

    @mcp.tool()
    def nui_get_rule(rule_id: str) -> dict[str, Any]:
        return get_rule_record(root_path, rule_id)

    @mcp.tool()
    def nui_query_rules(
        domain: str | None = None,
        rule_class: str | None = None,
        status: str | None = None,
        text: str | None = None,
        limit: int = 25,
    ) -> dict[str, Any]:
        return query_rule_records(root_path, domain=domain, rule_class=rule_class, status=status, text=text, limit=limit)

    @mcp.tool()
    def nui_rule_provenance(provenance_id: str) -> dict[str, Any]:
        return get_rule_provenance(root_path, provenance_id)

    @mcp.tool()
    def nui_ux_status() -> dict[str, Any]:
        return get_ux_status(root_path)

    @mcp.tool()
    def nui_get_ux_mechanism(mechanism_id: str) -> dict[str, Any]:
        return get_ux_mechanism_record(root_path, mechanism_id)

    @mcp.tool()
    def nui_query_ux_mechanisms(text: str | None = None, limit: int = 25) -> dict[str, Any]:
        return query_ux_mechanism_records(root_path, text=text, limit=limit)

    @mcp.tool()
    def nui_get_ux_skill(skill_id: str) -> dict[str, Any]:
        return get_ux_skill_record(root_path, skill_id)

    @mcp.tool()
    def nui_query_ux_skills(
        domain: str | None = None,
        mechanism_id: str | None = None,
        text: str | None = None,
        limit: int = 25,
    ) -> dict[str, Any]:
        return query_ux_skill_records(root_path, domain=domain, mechanism_id=mechanism_id, text=text, limit=limit)

    @mcp.tool()
    def nui_get_ux_rule(rule_id: str) -> dict[str, Any]:
        return get_ux_rule_record(root_path, rule_id)

    @mcp.tool()
    def nui_query_ux_rules(
        domain: str | None = None,
        mechanism_id: str | None = None,
        rule_class: str | None = None,
        status: str | None = None,
        text: str | None = None,
        limit: int = 25,
    ) -> dict[str, Any]:
        return query_ux_rule_records(
            root_path, domain=domain, mechanism_id=mechanism_id, rule_class=rule_class,
            status=status, text=text, limit=limit,
        )

    @mcp.tool()
    def nui_ux_v2_status() -> dict[str, Any]:
        return get_ux_v2_status(root_path)

    @mcp.tool()
    def nui_get_ux_provenance(provenance_id: str) -> dict[str, Any]:
        return get_ux_provenance_record(provenance_id, root_path)

    @mcp.tool()
    def nui_query_ux_provenance(
        source_kind: str | None = None,
        verification_mode: str | None = None,
        text: str | None = None,
        limit: int = 25,
    ) -> dict[str, Any]:
        return query_ux_provenance_records(
            root_path, source_kind=source_kind, verification_mode=verification_mode, text=text, limit=limit
        )

    @mcp.tool()
    def nui_get_ux_canonical_skill_bridge(skill_id: str) -> dict[str, Any]:
        return get_ux_canonical_skill_bridge_record(skill_id, root_path)

    @mcp.tool()
    def nui_query_ux_canonical_skill_bridge(
        mechanism_id: str | None = None,
        canonical_slug: str | None = None,
        text: str | None = None,
        limit: int = 25,
    ) -> dict[str, Any]:
        return query_ux_canonical_skill_bridge_records(
            root_path, mechanism_id=mechanism_id, canonical_slug=canonical_slug, text=text, limit=limit
        )

    @mcp.tool()
    def nui_verify_ux_journey(journey: dict[str, Any], observations: dict[str, Any]) -> dict[str, Any]:
        return verify_ux_journey_record(journey, observations, root_path)

    @mcp.tool()
    def nui_ux_v3_status() -> dict[str, Any]:
        return get_ux_v3_status(root_path)

    @mcp.tool()
    def nui_build_ux_product_model(packet: dict[str, Any]) -> dict[str, Any]:
        return build_ux_product_model_record(packet, root_path)

    @mcp.tool()
    def nui_build_ux_goal_graph(
        product_model: dict[str, Any],
        declared_goals: list[dict[str, Any]] = [],
        inferred_goals: list[dict[str, Any]] = [],
    ) -> dict[str, Any]:
        return build_ux_goal_graph_record(
            product_model, declared_goals=declared_goals, inferred_goals=inferred_goals, root=root_path
        )

    @mcp.tool()
    def nui_discover_ux_journeys(
        product_model: dict[str, Any], goal_graph: dict[str, Any], max_depth: int = 8
    ) -> dict[str, Any]:
        return discover_ux_journey_records(product_model, goal_graph, max_depth=max_depth, root=root_path)

    @mcp.tool()
    def nui_query_ux_journey_candidates(
        candidates: list[dict[str, Any]],
        goal_node_id: str | None = None, status: str | None = None, min_score: float | None = None, limit: int = 25,
    ) -> dict[str, Any]:
        return query_ux_journey_candidate_records(
            candidates, goal_node_id=goal_node_id, status=status, min_score=min_score, limit=limit, root=root_path
        )

    @mcp.tool()
    def nui_promote_ux_journey_candidate(
        candidate: dict[str, Any], product_model: dict[str, Any], goal_graph: dict[str, Any]
    ) -> dict[str, Any]:
        return promote_ux_journey_candidate_record(candidate, product_model, goal_graph, root_path)

    @mcp.tool()
    def nui_plan_ux_discovery(
        subject: dict[str, Any], available_capabilities: list[str], limit: int = 25
    ) -> dict[str, Any]:
        return plan_ux_discovery_record(subject, available_capabilities, limit=limit, root=root_path)

    @mcp.tool()
    def nui_create_ux_evidence_snapshot(
        product_id: str, revision: str, journey: dict[str, Any], verification: dict[str, Any],
        created_from: str, provenance_ids: list[str] = [],
    ) -> dict[str, Any]:
        return create_ux_evidence_snapshot_record(
            product_id, revision, journey, verification, created_from=created_from,
            provenance_ids=provenance_ids, root=root_path,
        )

    @mcp.tool()
    def nui_compare_ux_snapshots(
        baseline: dict[str, Any], candidate: dict[str, Any], history: list[dict[str, Any]] = []
    ) -> dict[str, Any]:
        return compare_ux_snapshot_records(baseline, candidate, history=history, root=root_path)

    @mcp.tool()
    def nui_rank_ux_impacts(
        items: list[dict[str, Any]], impact_evidence: dict[str, dict[str, Any]]
    ) -> dict[str, Any]:
        return rank_ux_impact_records(items, impact_evidence, root_path)

    @mcp.tool()
    def nui_runtime_doctor() -> dict[str, Any]:
        return get_runtime_doctor(root_path)

    mcp.run()
