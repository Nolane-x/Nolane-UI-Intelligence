"""NUI v2 deterministic validation facade.

v1 invariants are preserved verbatim in validators_legacy. This module layers
industry coverage/freshness gates and modular emerging-domain extensions on top
instead of weakening established gates. It supports package and standalone
importlib loading used by the regression suite.
"""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
from typing import Any, Iterable


def _load_sibling(filename: str, module_name: str):
    path = Path(__file__).with_name(filename)
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


if __package__:
    from . import validators_legacy as _legacy
    from . import industry as _industry
    from . import emerging as _emerging
    from . import emerging2 as _emerging2
    from . import emerging3 as _emerging3
    from . import emerging4 as _emerging4
else:
    _legacy = _load_sibling("validators_legacy.py", "nui_validators_legacy")
    _industry = _load_sibling("industry.py", "nui_industry")
    _emerging = _load_sibling("emerging.py", "nui_emerging")
    _emerging2 = _load_sibling("emerging2.py", "nui_emerging2")
    _emerging3 = _load_sibling("emerging3.py", "nui_emerging3")
    _emerging4 = _load_sibling("emerging4.py", "nui_emerging4")

validate_completion_packet = _legacy.validate_completion_packet
validate_skill_graph = _legacy.validate_skill_graph
validate_state_matrix = _legacy.validate_state_matrix
validate_tokens = _legacy.validate_tokens
validate_industry_atlas = _industry.validate_industry_atlas
validate_source_ledger = _industry.validate_source_ledger
validate_research_saturation = _industry.validate_research_saturation


def mandatory_routes_for_profile(profile: dict[str, Any]) -> set[str]:
    return (
        _industry.mandatory_routes_for_profile(profile)
        | _emerging.mandatory_emerging_routes(profile)
        | _emerging2.mandatory_standardized_emerging_routes(profile)
        | _emerging3.mandatory_third_extension_routes(profile)
        | _emerging4.mandatory_fourth_extension_routes(profile)
    )


def validate_mandatory_routes(profile: dict[str, Any], selected_skills: Iterable[str]) -> dict[str, Any]:
    required = mandatory_routes_for_profile(profile)
    selected = set(selected_skills)
    missing = sorted(required - selected)
    return {"valid": not missing, "required_routes": sorted(required), "missing_routes": missing}


def validate_bounded_saturation(record: dict[str, Any], final_evidence: dict[str, Any]) -> dict[str, Any]:
    """Require falsifiable zero-novelty evidence before accepting SATURATED.

    This validator deliberately proves only that the repository carries a bounded,
    internally coherent saturation claim. It cannot prove permanent completeness
    of the UI field and therefore requires explicit reopen conditions and bounds.
    """
    errors: list[str] = []
    dimensions = ("breadth", "depth", "contradictions", "novelty", "freshness")

    if record.get("decision") != "SATURATED":
        errors.append("bounded saturation validation requires decision SATURATED")
    if not isinstance(record.get("as_of"), str) or not record["as_of"].strip():
        errors.append("SATURATED decision requires a non-empty as_of boundary")

    evidence = record.get("evidence")
    if not isinstance(evidence, dict):
        errors.append("SATURATED decision requires evidence object")
        evidence = {}
    for dimension in dimensions:
        item = evidence.get(dimension)
        if not isinstance(item, dict):
            errors.append(f"SATURATED decision missing {dimension} evidence")
            continue
        if item.get("status") != "PASS":
            errors.append(f"SATURATED decision requires PASS {dimension} evidence")
        if not isinstance(item.get("criterion"), str) or not item["criterion"].strip():
            errors.append(f"SATURATED decision requires falsifiable {dimension} criterion")
        if not isinstance(item.get("observed"), str) or not item["observed"].strip():
            errors.append(f"SATURATED decision requires observed {dimension} evidence")

    reopen = record.get("reopen_conditions")
    if not isinstance(reopen, list) or len([item for item in reopen if isinstance(item, str) and item.strip()]) < 5:
        errors.append("SATURATED decision requires at least five explicit reopen conditions")

    if not isinstance(final_evidence, dict):
        errors.append("final saturation evidence must be an object")
        final_evidence = {}
    if final_evidence.get("wave_id") != record.get("wave_id"):
        errors.append("final saturation evidence wave_id must match research saturation wave_id")
    if final_evidence.get("decision") != "NO_NEW_NONDECOMPOSABLE_OWNER":
        errors.append("final saturation evidence must declare NO_NEW_NONDECOMPOSABLE_OWNER")

    sweeps = final_evidence.get("sweeps")
    if not isinstance(sweeps, list) or len(sweeps) < 5:
        errors.append("final saturation evidence requires at least five research sweeps")
        sweeps = []
    if sweeps:
        final = sweeps[-1]
        if not isinstance(final, dict):
            errors.append("final research sweep must be an object")
        else:
            if final.get("new_owner_count") != 0:
                errors.append("final research sweep new_owner_count must be zero before SATURATED")
            checks = final.get("decomposition_checks")
            if not isinstance(checks, list) or len(checks) < 6:
                errors.append("final zero-novelty sweep requires at least six decomposition checks")
                checks = []
            seen_sources: set[str] = set()
            for index, check in enumerate(checks):
                if not isinstance(check, dict):
                    errors.append(f"decomposition check {index} must be an object")
                    continue
                source_id = check.get("source_id")
                if not isinstance(source_id, str) or not source_id.strip():
                    errors.append(f"decomposition check {index} requires source_id")
                elif source_id in seen_sources:
                    errors.append(f"duplicate decomposition source_id {source_id}")
                else:
                    seen_sources.add(source_id)
                mapped = check.get("mapped_skills")
                if not isinstance(mapped, list) or not mapped or not all(isinstance(item, str) and item for item in mapped):
                    errors.append(f"decomposition check {source_id or index} requires mapped_skills")
                reason = check.get("reason")
                if not isinstance(reason, str) or not reason.strip():
                    errors.append(f"decomposition check {source_id or index} requires reason")

    boundary = final_evidence.get("saturation_boundary")
    if not isinstance(boundary, dict):
        errors.append("final saturation evidence requires saturation_boundary")
    else:
        for key in ("included", "not_claimed", "reopen_on"):
            value = boundary.get(key)
            if not isinstance(value, list) or not value:
                errors.append(f"saturation_boundary requires non-empty {key}")
        not_claimed = " ".join(str(item).lower() for item in boundary.get("not_claimed", []))
        if "future" not in not_claimed or "superiority" not in not_claimed:
            errors.append("saturation boundary must explicitly reject permanent completeness and unsupported superiority")

    return {
        "valid": not errors,
        "errors": errors,
        "decision": record.get("decision"),
        "sweep_count": len(sweeps),
    }


def validate_research_radar(radar: dict[str, Any], ledgers: Iterable[dict[str, Any]]) -> dict[str, Any]:
    """Make high-drift research reopen policy machine-checkable.

    Every very-high-drift source in the supplied ledgers must be watched. Radar
    entries must point to real ledger sources and contain an actionable cadence,
    trigger, and reason. High-drift sources not marked very-high remain eligible
    for optional proactive watches but do not fail this minimum gate.
    """
    errors: list[str] = []
    warnings: list[str] = []
    sources: dict[str, dict[str, Any]] = {}

    for ledger_index, ledger in enumerate(ledgers):
        if not isinstance(ledger, dict):
            errors.append(f"source ledger {ledger_index} must be an object")
            continue
        for source in ledger.get("sources", []):
            if not isinstance(source, dict):
                errors.append(f"source ledger {ledger_index} contains non-object source")
                continue
            source_id = source.get("id")
            if not isinstance(source_id, str) or not source_id.strip():
                errors.append(f"source ledger {ledger_index} contains source without id")
                continue
            if source_id in sources:
                errors.append(f"duplicate source id across ledgers: {source_id}")
            sources[source_id] = source

    if not isinstance(radar, dict):
        return {
            "valid": False,
            "errors": errors + ["research radar must be an object"],
            "warnings": warnings,
            "missing_very_high_drift": [],
            "watched_count": 0,
        }
    if not isinstance(radar.get("as_of"), str) or not radar["as_of"].strip():
        errors.append("research radar requires non-empty as_of")
    if not isinstance(radar.get("policy"), str) or not radar["policy"].strip():
        errors.append("research radar requires non-empty policy")

    watch = radar.get("watch")
    if not isinstance(watch, list) or not watch:
        errors.append("research radar requires non-empty watch list")
        watch = []

    watched_ids: set[str] = set()
    for index, item in enumerate(watch):
        if not isinstance(item, dict):
            errors.append(f"research radar watch {index} must be an object")
            continue
        source_id = item.get("source_id")
        if not isinstance(source_id, str) or not source_id.strip():
            errors.append(f"research radar watch {index} requires source_id")
            continue
        if source_id in watched_ids:
            errors.append(f"duplicate research radar watch for {source_id}")
        watched_ids.add(source_id)
        if source_id not in sources:
            errors.append(f"research radar watch references unknown source {source_id}")
        for field in ("cadence", "trigger", "reason"):
            value = item.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"research radar watch {source_id} requires {field}")

    very_high = {source_id for source_id, source in sources.items() if source.get("drift") == "very-high"}
    missing_very_high = sorted(very_high - watched_ids)
    for source_id in missing_very_high:
        errors.append(f"very-high-drift source is not watched: {source_id}")

    high_unwatched = sorted(
        source_id for source_id, source in sources.items()
        if source.get("drift") == "high" and source_id not in watched_ids
    )
    if high_unwatched:
        warnings.append(f"high-drift sources not proactively watched: {high_unwatched}")

    return {
        "valid": not errors,
        "errors": errors,
        "warnings": warnings,
        "missing_very_high_drift": missing_very_high,
        "watched_count": len(watched_ids),
        "source_count": len(sources),
    }


def _load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_repository(root: Path | str) -> dict[str, Any]:
    root = Path(root)
    base = _legacy.validate_repository(root)
    errors = list(base.get("errors", []))
    warnings = list(base.get("warnings", []))
    metrics = dict(base.get("metrics", {}))

    required_v2 = [
        "knowledge/ui-domain-atlas.json",
        "knowledge/source-ledger.json",
        "knowledge/research-radar.json",
        "knowledge/research-saturation.json",
        "knowledge/final-saturation-evidence.json",
        "knowledge/v2-skill-manifest.json",
        "knowledge/emerging-skill-manifest.json",
        "knowledge/ui-domain-atlas-emerging.json",
        "knowledge/source-ledger-emerging.json",
        "evals/v2/coverage/required-domains.json",
        "evals/v2/coverage/emerging-domains.json",
        "knowledge/emerging-skill-manifest-2.json",
        "knowledge/ui-domain-atlas-emerging-2.json",
        "knowledge/source-ledger-emerging-2.json",
        "evals/v2/coverage/standardized-emerging-domains-2.json",
        "knowledge/emerging-skill-manifest-3.json",
        "knowledge/ui-domain-atlas-emerging-3.json",
        "knowledge/source-ledger-emerging-3.json",
        "evals/v2/coverage/standardized-emerging-domains-3.json",
        "knowledge/emerging-skill-manifest-4.json",
        "knowledge/ui-domain-atlas-emerging-4.json",
        "knowledge/source-ledger-emerging-4.json",
        "evals/v2/coverage/standardized-emerging-domains-4.json",
    ]
    for relative in required_v2:
        if not (root / relative).is_file():
            errors.append(f"missing required v2 repository file: {relative}")

    graph: dict[str, Any] = {}
    atlas: dict[str, Any] = {}
    ledger: dict[str, Any] = {}
    try:
        graph = _load(root / "skills/skill-graph.json")
        atlas = _load(root / "knowledge/ui-domain-atlas.json")
        atlas_result = validate_industry_atlas(atlas, graph)
        errors.extend(f"industry atlas: {item}" for item in atlas_result["errors"])
        metrics["industry_coverage_cells"] = atlas_result["coverage_cell_count"]
        for suffix, label, metric in [
            ("", "emerging industry atlas", "emerging_coverage_cells"),
            ("-2", "standardized emerging atlas", "standardized_emerging_coverage_cells"),
            ("-3", "third emerging atlas", "third_emerging_coverage_cells"),
            ("-4", "fourth emerging atlas", "fourth_emerging_coverage_cells"),
        ]:
            path = root / f"knowledge/ui-domain-atlas-emerging{suffix}.json"
            result = validate_industry_atlas(_load(path), graph)
            errors.extend(f"{label}: {item}" for item in result["errors"])
            metrics[metric] = result["coverage_cell_count"]
    except Exception as exc:
        errors.append(f"invalid industry atlas/graph: {exc}")

    all_ledgers: list[dict[str, Any]] = []
    try:
        ledger = _load(root / "knowledge/source-ledger.json")
        all_ledgers.append(ledger)
        ledger_result = validate_source_ledger(ledger)
        errors.extend(f"source ledger: {item}" for item in ledger_result["errors"])
        warnings.extend(f"source ledger: {item}" for item in ledger_result["warnings"])
        metrics["research_source_count"] = ledger_result["source_count"]
        for suffix, label, metric in [
            ("", "emerging source ledger", "emerging_research_source_count"),
            ("-2", "standardized emerging source ledger", "standardized_emerging_research_source_count"),
            ("-3", "third emerging source ledger", "third_emerging_research_source_count"),
            ("-4", "fourth emerging source ledger", "fourth_emerging_research_source_count"),
        ]:
            path = root / f"knowledge/source-ledger-emerging{suffix}.json"
            extension_ledger = _load(path)
            all_ledgers.append(extension_ledger)
            result = validate_source_ledger(extension_ledger)
            errors.extend(f"{label}: {item}" for item in result["errors"])
            warnings.extend(f"{label}: {item}" for item in result["warnings"])
            metrics[metric] = result["source_count"]

        radar = _load(root / "knowledge/research-radar.json")
        radar_result = validate_research_radar(radar, all_ledgers)
        errors.extend(f"research radar: {item}" for item in radar_result["errors"])
        warnings.extend(f"research radar: {item}" for item in radar_result["warnings"])
        metrics["research_radar_watches"] = radar_result["watched_count"]
        metrics["research_radar_source_count"] = radar_result["source_count"]
    except Exception as exc:
        errors.append(f"invalid source ledger or research radar: {exc}")

    try:
        saturation = _load(root / "knowledge/research-saturation.json")
        saturation_result = validate_research_saturation(saturation, ledger, atlas)
        errors.extend(f"research saturation: {item}" for item in saturation_result["errors"])
        metrics["research_saturation"] = saturation_result.get("decision")
        if saturation.get("decision") == "SATURATED":
            final_evidence = _load(root / "knowledge/final-saturation-evidence.json")
            bounded_result = validate_bounded_saturation(saturation, final_evidence)
            errors.extend(f"bounded saturation: {item}" for item in bounded_result["errors"])
            metrics["final_saturation_sweeps"] = bounded_result["sweep_count"]
    except Exception as exc:
        errors.append(f"invalid research saturation record: {exc}")

    try:
        manifests = [
            _load(root / "knowledge/v2-skill-manifest.json"),
            _load(root / "knowledge/emerging-skill-manifest.json"),
            _load(root / "knowledge/emerging-skill-manifest-2.json"),
            _load(root / "knowledge/emerging-skill-manifest-3.json"),
            _load(root / "knowledge/emerging-skill-manifest-4.json"),
        ]
        all_items = [item for manifest in manifests for item in manifest.get("skills", [])]
        metrics["v2_skill_count"] = len(all_items)
        declared = graph.get("skills", {}) if graph else {}
        for item in all_items:
            name = item.get("name")
            node = declared.get(name)
            if not node:
                errors.append(f"v2 manifest skill {name} is not declared in skill graph")
                continue
            for field in ("family", "parent", "output"):
                if node.get(field) != item.get(field):
                    errors.append(f"v2 manifest/graph mismatch for {name}.{field}")
    except Exception as exc:
        errors.append(f"invalid v2 skill manifest: {exc}")

    return {"valid": not errors, "errors": errors, "warnings": warnings, "metrics": metrics}


__all__ = [
    "validate_completion_packet", "validate_repository", "validate_skill_graph",
    "validate_state_matrix", "validate_tokens", "validate_industry_atlas",
    "validate_source_ledger", "validate_research_saturation", "validate_bounded_saturation",
    "validate_research_radar", "validate_mandatory_routes", "mandatory_routes_for_profile",
]
