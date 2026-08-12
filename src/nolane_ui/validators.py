"""NUI v2 deterministic validation facade.

v1 invariants remain in validators_legacy. This facade adds v2 industry routing,
research authority/freshness, bounded-saturation provenance, and repository
aggregation without changing v1 completion semantics.
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
    from . import contracts as _contracts
else:
    _legacy = _load_sibling("validators_legacy.py", "nui_validators_legacy")
    _industry = _load_sibling("industry.py", "nui_industry")
    _emerging = _load_sibling("emerging.py", "nui_emerging")
    _emerging2 = _load_sibling("emerging2.py", "nui_emerging2")
    _emerging3 = _load_sibling("emerging3.py", "nui_emerging3")
    _emerging4 = _load_sibling("emerging4.py", "nui_emerging4")
    _contracts = _load_sibling("contracts.py", "nui_contracts")

validate_completion_packet = _legacy.validate_completion_packet
validate_skill_graph = _legacy.validate_skill_graph
validate_state_matrix = _legacy.validate_state_matrix
validate_tokens = _legacy.validate_tokens
validate_industry_atlas = _industry.validate_industry_atlas
validate_source_ledger = _industry.validate_source_ledger
validate_research_saturation = _industry.validate_research_saturation

ATLAS_EXTENSIONS = (
    ("knowledge/ui-domain-atlas-emerging.json", "emerging industry atlas", "emerging_coverage_cells"),
    ("knowledge/ui-domain-atlas-emerging-2.json", "standardized emerging atlas", "standardized_emerging_coverage_cells"),
    ("knowledge/ui-domain-atlas-emerging-3.json", "third emerging atlas", "third_emerging_coverage_cells"),
    ("knowledge/ui-domain-atlas-emerging-4.json", "fourth emerging atlas", "fourth_emerging_coverage_cells"),
)

SOURCE_LEDGERS = (
    ("knowledge/source-ledger.json", "source ledger", "research_source_count"),
    ("knowledge/source-ledger-emerging.json", "emerging source ledger", "emerging_research_source_count"),
    ("knowledge/source-ledger-emerging-2.json", "standardized emerging source ledger", "standardized_emerging_research_source_count"),
    ("knowledge/source-ledger-emerging-3.json", "third emerging source ledger", "third_emerging_research_source_count"),
    ("knowledge/source-ledger-emerging-4.json", "fourth emerging source ledger", "fourth_emerging_research_source_count"),
    ("knowledge/source-ledger-final-sweep.json", "final sweep source ledger", "final_sweep_research_source_count"),
)

MANIFESTS = (
    "knowledge/v2-skill-manifest.json",
    "knowledge/emerging-skill-manifest.json",
    "knowledge/emerging-skill-manifest-2.json",
    "knowledge/emerging-skill-manifest-3.json",
    "knowledge/emerging-skill-manifest-4.json",
)

REQUIRED_V2 = (
    "knowledge/ui-domain-atlas.json",
    "knowledge/research-radar.json",
    "knowledge/research-saturation.json",
    "knowledge/final-saturation-evidence.json",
    *[item[0] for item in SOURCE_LEDGERS],
    *[item[0] for item in ATLAS_EXTENSIONS],
    *MANIFESTS,
    "evals/v2/coverage/required-domains.json",
    "evals/v2/coverage/emerging-domains.json",
    "evals/v2/coverage/standardized-emerging-domains-2.json",
    "evals/v2/coverage/standardized-emerging-domains-3.json",
    "evals/v2/coverage/standardized-emerging-domains-4.json",
    "evals/v2/rubric.json",
)

REQUIRED_V3 = (
    "knowledge/v3-skill-manifest.json",
    "evals/v3/manifest.json",
    "evals/v3/functional-closure/cases.json",
    "src/nolane_ui/contracts.py",
    "src/nolane_ui/closure.py",
)



def _load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _mandatory_v3_routes(profile: dict[str, Any]) -> set[str]:
    required: set[str] = set()
    scope = profile.get("scope")
    if profile.get("product_wide") or scope in {"multi-feature-product", "system", "product-wide"}:
        required |= {
            "inventorying-product-capabilities",
            "registering-ui-actions",
            "proving-interface-reachability",
            "covering-product-scenarios",
            "compiling-ui-implementation-specifications",
            "critiquing-functional-completeness",
        }
        if profile.get("delivery_stage") in {"implement", "verify", "release"} or profile.get("claims_runtime_behavior"):
            required.add("verifying-runtime-ui-behavior")
    if profile.get("visual_evidence_iteration"):
        required |= {
            "researching-visual-references",
            "iterating-rendered-visual-design",
            "maintaining-project-design-memory",
        }
    return required


def mandatory_routes_for_profile(profile: dict[str, Any]) -> set[str]:
    return (
        _industry.mandatory_routes_for_profile(profile)
        | _emerging.mandatory_emerging_routes(profile)
        | _emerging2.mandatory_standardized_emerging_routes(profile)
        | _emerging3.mandatory_third_extension_routes(profile)
        | _emerging4.mandatory_fourth_extension_routes(profile)
        | _mandatory_v3_routes(profile)
    )


def validate_v3_completion_evidence(record: dict[str, Any]) -> dict[str, Any]:
    """Block product-wide completion when closure/spec/runtime/visual evidence is absent."""
    errors: list[str] = []
    if not isinstance(record, dict):
        return {"decision": "BLOCKED", "errors": ["v3 completion evidence must be an object"]}
    if record.get("product_wide"):
        closure = record.get("functional_closure")
        if not isinstance(closure, dict) or closure.get("status") != "PASS":
            errors.append("product-wide completion requires functional closure PASS")
        spec = record.get("ui_specification")
        if not isinstance(spec, dict) or spec.get("status") != "IMPLEMENTABLE":
            errors.append("product-wide completion requires IMPLEMENTABLE ui specification")
    if record.get("claims_runtime_behavior"):
        runtime = record.get("behavior_verification")
        if not isinstance(runtime, dict) or runtime.get("status") != "PASS":
            errors.append("runtime behavior claim requires behavior verification PASS")
    if record.get("visual_evidence_iteration"):
        visual = record.get("visual_iteration_evidence")
        if not isinstance(visual, dict) or visual.get("status") != "PASS":
            errors.append("visual evidence iteration requires visual iteration evidence PASS")
    return {"decision": "BLOCKED" if errors else "PASS", "errors": errors}


def validate_mandatory_routes(profile: dict[str, Any], selected_skills: Iterable[str]) -> dict[str, Any]:
    required = mandatory_routes_for_profile(profile)
    missing = sorted(required - set(selected_skills))
    return {"valid": not missing, "required_routes": sorted(required), "missing_routes": missing}


def validate_bounded_saturation(
    record: dict[str, Any],
    final_evidence: dict[str, Any],
    *,
    source_ids: Iterable[str] | None = None,
    skill_names: Iterable[str] | None = None,
) -> dict[str, Any]:
    """Validate a bounded SATURATED claim and, when supplied, its references."""
    errors: list[str] = []
    dimensions = ("breadth", "depth", "contradictions", "novelty", "freshness")
    known_sources = set(source_ids) if source_ids is not None else None
    known_skills = set(skill_names) if skill_names is not None else None

    if record.get("decision") != "SATURATED":
        errors.append("bounded saturation validation requires decision SATURATED")
    if not isinstance(record.get("as_of"), str) or not record.get("as_of", "").strip():
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
        if not isinstance(item.get("criterion"), str) or not item.get("criterion", "").strip():
            errors.append(f"SATURATED decision requires falsifiable {dimension} criterion")
        if not isinstance(item.get("observed"), str) or not item.get("observed", "").strip():
            errors.append(f"SATURATED decision requires observed {dimension} evidence")

    reopen = record.get("reopen_conditions")
    if not isinstance(reopen, list) or len([x for x in reopen if isinstance(x, str) and x.strip()]) < 5:
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
                else:
                    if source_id in seen_sources:
                        errors.append(f"duplicate decomposition source_id {source_id}")
                    seen_sources.add(source_id)
                    if known_sources is not None and source_id not in known_sources:
                        errors.append(f"decomposition check references unknown source {source_id}")

                mapped = check.get("mapped_skills")
                if not isinstance(mapped, list) or not mapped or not all(isinstance(x, str) and x for x in mapped):
                    errors.append(f"decomposition check {source_id or index} requires mapped_skills")
                elif known_skills is not None:
                    unknown = sorted(set(mapped) - known_skills)
                    if unknown:
                        errors.append(f"decomposition check {source_id or index} references unknown skills {unknown}")
                if not isinstance(check.get("reason"), str) or not check.get("reason", "").strip():
                    errors.append(f"decomposition check {source_id or index} requires reason")

    boundary = final_evidence.get("saturation_boundary")
    if not isinstance(boundary, dict):
        errors.append("final saturation evidence requires saturation_boundary")
    else:
        for key in ("included", "not_claimed", "reopen_on"):
            if not isinstance(boundary.get(key), list) or not boundary.get(key):
                errors.append(f"saturation_boundary requires non-empty {key}")
        not_claimed = " ".join(str(x).lower() for x in boundary.get("not_claimed", []))
        if "future" not in not_claimed or "superiority" not in not_claimed:
            errors.append("saturation boundary must explicitly reject permanent completeness and unsupported superiority")

    return {"valid": not errors, "errors": errors, "decision": record.get("decision"), "sweep_count": len(sweeps)}


def validate_research_radar(radar: dict[str, Any], ledgers: Iterable[dict[str, Any]]) -> dict[str, Any]:
    """Validate source references and proactive coverage for high-drift research."""
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
        return {"valid": False, "errors": errors + ["research radar must be an object"], "warnings": warnings, "missing_very_high_drift": [], "watched_count": 0, "source_count": len(sources)}
    if not isinstance(radar.get("as_of"), str) or not radar.get("as_of", "").strip():
        errors.append("research radar requires non-empty as_of")
    if not isinstance(radar.get("policy"), str) or not radar.get("policy", "").strip():
        errors.append("research radar requires non-empty policy")

    watch = radar.get("watch")
    if not isinstance(watch, list) or not watch:
        errors.append("research radar requires non-empty watch list")
        watch = []
    watched: set[str] = set()
    for index, item in enumerate(watch):
        if not isinstance(item, dict):
            errors.append(f"research radar watch {index} must be an object")
            continue
        source_id = item.get("source_id")
        if not isinstance(source_id, str) or not source_id.strip():
            errors.append(f"research radar watch {index} requires source_id")
            continue
        if source_id in watched:
            errors.append(f"duplicate research radar watch for {source_id}")
        watched.add(source_id)
        if source_id not in sources:
            errors.append(f"research radar watch references unknown source {source_id}")
        for field in ("cadence", "trigger", "reason"):
            if not isinstance(item.get(field), str) or not item.get(field, "").strip():
                errors.append(f"research radar watch {source_id} requires {field}")

    very_high = {sid for sid, source in sources.items() if source.get("drift") == "very-high"}
    missing = sorted(very_high - watched)
    errors.extend(f"very-high-drift source is not watched: {sid}" for sid in missing)
    high_unwatched = sorted(sid for sid, source in sources.items() if source.get("drift") == "high" and sid not in watched)
    if high_unwatched:
        warnings.append(f"high-drift sources not proactively watched: {high_unwatched}")
    return {"valid": not errors, "errors": errors, "warnings": warnings, "missing_very_high_drift": missing, "watched_count": len(watched), "source_count": len(sources)}


def validate_repository(root: Path | str) -> dict[str, Any]:
    root = Path(root)
    base = _legacy.validate_repository(root)
    errors = list(base.get("errors", []))
    warnings = list(base.get("warnings", []))
    metrics = dict(base.get("metrics", {}))

    for relative in REQUIRED_V2:
        if not (root / relative).is_file():
            errors.append(f"missing required v2 repository file: {relative}")
    for relative in REQUIRED_V3:
        if not (root / relative).is_file():
            errors.append(f"missing required v3 repository file: {relative}")

    graph: dict[str, Any] = {}
    atlas: dict[str, Any] = {}
    try:
        graph = _load(root / "skills/skill-graph.json")
        atlas = _load(root / "knowledge/ui-domain-atlas.json")
        result = validate_industry_atlas(atlas, graph)
        errors.extend(f"industry atlas: {x}" for x in result["errors"])
        metrics["industry_coverage_cells"] = result["coverage_cell_count"]
        for relative, label, metric in ATLAS_EXTENSIONS:
            result = validate_industry_atlas(_load(root / relative), graph)
            errors.extend(f"{label}: {x}" for x in result["errors"])
            metrics[metric] = result["coverage_cell_count"]
    except Exception as exc:
        errors.append(f"invalid industry atlas/graph: {exc}")

    all_ledgers: list[dict[str, Any]] = []
    all_source_ids: set[str] = set()
    primary_ledger: dict[str, Any] = {}
    try:
        for index, (relative, label, metric) in enumerate(SOURCE_LEDGERS):
            ledger = _load(root / relative)
            if index == 0:
                primary_ledger = ledger
            all_ledgers.append(ledger)
            result = validate_source_ledger(ledger)
            errors.extend(f"{label}: {x}" for x in result["errors"])
            warnings.extend(f"{label}: {x}" for x in result["warnings"])
            metrics[metric] = result["source_count"]
            all_source_ids.update(source.get("id") for source in ledger.get("sources", []) if isinstance(source, dict) and isinstance(source.get("id"), str))

        radar_result = validate_research_radar(_load(root / "knowledge/research-radar.json"), all_ledgers)
        errors.extend(f"research radar: {x}" for x in radar_result["errors"])
        warnings.extend(f"research radar: {x}" for x in radar_result["warnings"])
        metrics["research_radar_watches"] = radar_result["watched_count"]
        metrics["research_radar_source_count"] = radar_result["source_count"]
    except Exception as exc:
        errors.append(f"invalid source ledger or research radar: {exc}")

    try:
        saturation = _load(root / "knowledge/research-saturation.json")
        result = validate_research_saturation(saturation, primary_ledger, atlas)
        errors.extend(f"research saturation: {x}" for x in result["errors"])
        metrics["research_saturation"] = result.get("decision")
        if saturation.get("decision") == "SATURATED":
            bounded = validate_bounded_saturation(
                saturation,
                _load(root / "knowledge/final-saturation-evidence.json"),
                source_ids=all_source_ids,
                skill_names=set(graph.get("skills", {})),
            )
            errors.extend(f"bounded saturation: {x}" for x in bounded["errors"])
            metrics["final_saturation_sweeps"] = bounded["sweep_count"]
    except Exception as exc:
        errors.append(f"invalid research saturation record: {exc}")

    try:
        declared = graph.get("skills", {}) if graph else {}
        items = [item for relative in MANIFESTS for item in _load(root / relative).get("skills", [])]
        metrics["v2_skill_count"] = len(items)
        for item in items:
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

    try:
        contract_result = _contracts.validate_skill_contract_integrity(root, graph)
        errors.extend(f"skill contract integrity: {x}" for x in contract_result["errors"])
        metrics["skill_contracts_checked"] = contract_result["checked"]
    except Exception as exc:
        errors.append(f"invalid v3 skill contract integrity: {exc}")

    try:
        v3 = _load(root / "knowledge/v3-skill-manifest.json")
        v3_items = v3.get("skills", [])
        if len(v3_items) != 10:
            errors.append(f"v3 skill manifest must contain exactly 10 skills, found {len(v3_items)}")
        declared = graph.get("skills", {}) if graph else {}
        for item in v3_items:
            name = item.get("name")
            node = declared.get(name)
            if not node:
                errors.append(f"v3 manifest skill {name} is not declared in skill graph")
                continue
            for field in ("family", "parent", "output"):
                if node.get(field) != item.get(field):
                    errors.append(f"v3 manifest/graph mismatch for {name}.{field}")
        metrics["v3_skill_count"] = len(v3_items)
    except Exception as exc:
        errors.append(f"invalid v3 skill manifest: {exc}")

    try:
        manifest = _load(root / "evals/v3/manifest.json")
        assets = manifest.get("assets", [])
        total = 0
        case_ids: set[str] = set()
        declared = set(graph.get("skills", {})) if graph else set()
        for asset in assets:
            path = asset.get("path") if isinstance(asset, dict) else None
            if not isinstance(path, str) or not path:
                errors.append("v3 eval manifest asset requires path")
                continue
            doc = _load(root / path)
            if doc.get("version") != 3:
                errors.append(f"v3 eval asset {path} must declare version 3")
            for case in doc.get("cases", []):
                total += 1
                cid = case.get("id")
                if not isinstance(cid, str) or not cid:
                    errors.append(f"v3 eval asset {path} contains case without id")
                elif cid in case_ids:
                    errors.append(f"duplicate v3 eval case id {cid}")
                else:
                    case_ids.add(cid)
                if len(str(case.get("failure", "")).split()) < 6:
                    errors.append(f"v3 eval case {cid} has weak failure scenario")
                required = case.get("required_skills", [])
                if not isinstance(required, list) or not required:
                    errors.append(f"v3 eval case {cid} requires required_skills")
                else:
                    unknown = sorted(set(required) - declared)
                    if unknown:
                        errors.append(f"v3 eval case {cid} references unknown skills {unknown}")
                must_find = case.get("must_find", [])
                if not isinstance(must_find, list) or len(must_find) < 2:
                    errors.append(f"v3 eval case {cid} requires at least two must_find findings")
        if total < 17:
            errors.append(f"v3 eval corpus requires at least 17 cases, found {total}")
        metrics["v3_adversarial_cases"] = total
    except Exception as exc:
        errors.append(f"invalid v3 eval corpus: {exc}")

    return {"valid": not errors, "errors": errors, "warnings": warnings, "metrics": metrics}


__all__ = [
    "validate_completion_packet", "validate_repository", "validate_skill_graph",
    "validate_state_matrix", "validate_tokens", "validate_industry_atlas",
    "validate_source_ledger", "validate_research_saturation", "validate_bounded_saturation",
    "validate_research_radar", "validate_mandatory_routes", "mandatory_routes_for_profile",
    "validate_v3_completion_evidence",
]
