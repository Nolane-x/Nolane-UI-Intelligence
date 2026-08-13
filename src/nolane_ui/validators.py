"""NUI v6 validation overlay.

v1-v4 behavior lives in :mod:`validators_v4`; v5 affective/aesthetic policy remains
here and v6 adds deep-source, industry-ontology, semantic-depth and causal-eval
gates while preserving prior public APIs.
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
    from . import aesthetic as _aesthetic
    from . import validators_v4 as _v4
    from . import source_intelligence as _source_v6
    from . import depth as _depth_v6
else:
    _aesthetic = _load_sibling("aesthetic.py", "nui_aesthetic_v5")
    _v4 = _load_sibling("validators_v4.py", "nui_validators_v4")
    _source_v6 = _load_sibling("source_intelligence.py", "nui_source_intelligence_v6")
    _depth_v6 = _load_sibling("depth.py", "nui_depth_v6")

validate_completion_packet = _v4.validate_completion_packet
validate_skill_graph = _v4.validate_skill_graph
validate_state_matrix = _v4.validate_state_matrix
validate_tokens = _v4.validate_tokens
validate_industry_atlas = _v4.validate_industry_atlas
validate_source_ledger = _v4.validate_source_ledger
validate_research_saturation = _v4.validate_research_saturation
validate_bounded_saturation = _v4.validate_bounded_saturation
validate_research_radar = _v4.validate_research_radar
validate_v3_completion_evidence = _v4.validate_v3_completion_evidence
validate_v4_completion_evidence = _v4.validate_v4_completion_evidence

REQUIRED_V5 = (
    "knowledge/v5-skill-manifest.json",
    "evals/v5/manifest.json",
    "evals/v5/affective-aesthetic/cases.json",
    "evals/v5/semantic-mutations/cases.json",
    "evals/v5/skill-interactions/cases.json",
    "evals/v5/craft-distribution/cases.json",
    "src/nolane_ui/aesthetic.py",
    "schemas/experiential-intent.schema.json",
    "schemas/visual-ambition-contract.schema.json",
    "schemas/aesthetic-quality-evidence.schema.json",
    "schemas/encoding-provenance.schema.json",
    "schemas/workspace-visual-matrix.schema.json",
    "schemas/skill-interaction-evidence.schema.json",
    "artifacts/v5-completion-packet.example.json",
    "docs/V5-ATLAS-FINDINGS-CLOSURE.md",
)

REQUIRED_V6 = (
    "knowledge/v6-skill-manifest.json",
    "knowledge/ui-source-intelligence-v6.json",
    "knowledge/ui-industry-ontology-v6.json",
    "knowledge/skill-depth-constitution-v6.json",
    "knowledge/v6-depth-focus-obligations.json",
    "evals/v6/manifest.json",
    "evals/v6/source-depth/cases.json",
    "evals/v6/synthesis/cases.json",
    "evals/v6/ontology/cases.json",
    "evals/v6/skill-effect/cases.json",
    "src/nolane_ui/source_intelligence.py",
    "src/nolane_ui/depth.py",
    "schemas/ui-source-research-dossier.schema.json",
    "schemas/ui-cross-source-synthesis.schema.json",
    "artifacts/v6-completion-packet.example.json",
    "docs/research/UI-SOURCE-INTELLIGENCE-V6.md",
)


def _load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def mandatory_routes_for_profile(profile: dict[str, Any]) -> set[str]:
    return _v4.mandatory_routes_for_profile(profile) | _aesthetic.mandatory_aesthetic_routes(profile) | _source_v6.mandatory_v6_source_routes(profile)


def validate_mandatory_routes(profile: dict[str, Any], selected_skills: Iterable[str]) -> dict[str, Any]:
    required = mandatory_routes_for_profile(profile)
    missing = sorted(required - set(selected_skills))
    return {"valid": not missing, "required_routes": sorted(required), "missing_routes": missing}


def validate_v5_completion_evidence(record: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(record, dict):
        return {"decision": "BLOCKED", "errors": ["v5 completion evidence must be an object"]}
    errors.extend(validate_v4_completion_evidence(record).get("errors", []))
    ambition = str(record.get("visual_ambition", "")).strip().lower()
    if ambition in _aesthetic.HIGH_AMBITION:
        required = (
            ("experiential_intent", "experiential intent"),
            ("visual_ambition_contract", "visual ambition contract"),
            ("reference_frontier", "reference frontier"),
            ("visual_legibility_evidence", "visual legibility evidence"),
            ("aesthetic_attractor_audit", "aesthetic attractor audit"),
            ("signature_depth_contract", "signature depth contract"),
            ("visual_energy_evidence", "visual energy evidence"),
            ("aesthetic_adequacy", "aesthetic adequacy"),
        )
        for key, label in required:
            value = record.get(key)
            if not isinstance(value, dict) or value.get("status") != "PASS":
                errors.append(f"{ambition} completion requires {label} PASS")
        divergence = record.get("divergence_evidence")
        if not isinstance(divergence, dict) or divergence.get("status") != "PASS":
            errors.append(f"{ambition} completion requires divergence evidence PASS")
        elif record.get("visual_freedom") in {"high", "open", "unconstrained"}:
            if divergence.get("candidate_count", 0) < 3:
                errors.append("high visual freedom requires at least three materially different visual candidates")
            if divergence.get("materially_distinct") is not True:
                errors.append("high visual freedom requires materially distinct candidate directions")
            if divergence.get("rendered_evidence") is not True:
                errors.append("high visual freedom requires rendered candidate evidence when claiming completion")
        basin = record.get("aesthetic_basin_decision")
        if not isinstance(basin, dict):
            errors.append(f"{ambition} completion requires aesthetic basin decision")
        elif basin.get("decision") == "RE_DIVERGE":
            errors.append("aesthetic basin decision requires re-divergence before release")
        elif basin.get("decision") not in {"REFINE", "KEEP", "PASS"}:
            errors.append("aesthetic basin decision must explicitly permit refinement/keep before release")
        if record.get("material_data_visualization") or record.get("data_visualization"):
            encoding = record.get("encoding_provenance")
            if not isinstance(encoding, dict) or encoding.get("status") != "PASS":
                errors.append("material data visualization requires encoding provenance PASS")
        if record.get("product_wide") or record.get("multi_screen") or record.get("workspace_count", 0) > 1:
            diversity = record.get("perceptual_diversity")
            if not isinstance(diversity, dict) or diversity.get("status") != "PASS":
                errors.append("product-wide high-ambition completion requires perceptual diversity PASS")
    return {"decision": "BLOCKED" if errors else "PASS", "errors": errors}



def validate_v6_completion_evidence(record: dict[str, Any]) -> dict[str, Any]:
    """Gate task completion through v5 plus v6 deep-research/causal obligations."""
    errors: list[str] = []
    if not isinstance(record, dict):
        return {"decision": "BLOCKED", "errors": ["v6 completion evidence must be an object"]}
    errors.extend(validate_v5_completion_evidence(record).get("errors", []))
    usage = str(record.get("external_source_usage", ""))
    count = int(record.get("external_source_count", 0) or 0)
    material = usage in _source_v6.INFLUENTIAL_USAGE or record.get("external_sources_material") is True
    if material:
        source_research = record.get("source_research")
        if not isinstance(source_research, dict) or source_research.get("status") != "PASS":
            errors.append("material external-source completion requires source research PASS")
        research_depth = record.get("research_depth_audit")
        if not isinstance(research_depth, dict) or research_depth.get("status") != "PASS":
            errors.append("material external-source completion requires research depth audit PASS")
        source_mix = record.get("source_mix")
        if count > 1 or str(record.get("visual_ambition", "")) in {"exceptional", "experiential"}:
            if not isinstance(source_mix, dict) or source_mix.get("status") != "PASS":
                errors.append("material multi/high-ambition source work requires source mix PASS")
        if count > 1:
            synthesis = record.get("cross_source_synthesis")
            if not isinstance(synthesis, dict) or synthesis.get("status") != "PASS":
                errors.append("multiple material sources require cross-source synthesis PASS")
    if record.get("high_risk_interaction_cell") is True or record.get("cross_axis_high_risk") is True:
        coverage = record.get("industry_ontology_coverage")
        if not isinstance(coverage, dict) or coverage.get("status") != "PASS":
            errors.append("high-risk cross-axis work requires industry ontology coverage PASS")
    if record.get("claim_skill_effect") is True or record.get("causal_skill_quality_claim") is True:
        benchmark = record.get("skill_effect_benchmark")
        if not isinstance(benchmark, dict) or benchmark.get("status") not in {"SUPPORTED", "MIXED"}:
            errors.append("causal skill-effect claim requires a supported or mixed bounded benchmark")
        elif not all(benchmark.get(k) is True for k in ("lineage_recorded", "controls_present", "falsifiers_declared")):
            errors.append("skill-effect benchmark requires lineage, controls and falsifiers")
    return {"decision": "BLOCKED" if errors else "PASS", "errors": errors}

def validate_repository(root: Path | str) -> dict[str, Any]:
    root = Path(root)
    base = _v4.validate_repository(root)
    errors = list(base.get("errors", []))
    warnings = list(base.get("warnings", []))
    metrics = dict(base.get("metrics", {}))
    for relative in REQUIRED_V5:
        if not (root / relative).is_file():
            errors.append(f"missing required v5 repository file: {relative}")
    try:
        graph = _load(root / "skills/skill-graph.json")
        declared = graph.get("skills", {})
        v5 = _load(root / "knowledge/v5-skill-manifest.json")
        if v5.get("version") != 5:
            errors.append("v5 skill manifest must declare version 5")
        items = v5.get("skills", [])
        if len(items) != 13:
            errors.append(f"v5 skill manifest must contain exactly 13 skills, found {len(items)}")
        owners: set[str] = set()
        for item in items:
            name = item.get("name")
            node = declared.get(name)
            if not node:
                errors.append(f"v5 manifest skill {name} is not declared in skill graph")
                continue
            for field in ("family", "parent", "output"):
                if node.get(field) != item.get(field):
                    errors.append(f"v5 manifest/graph mismatch for {name}.{field}")
            owner = str(item.get("ownership", "")).strip().lower()
            if not owner:
                errors.append(f"v5 manifest skill {name} requires ownership")
            elif owner in owners:
                errors.append(f"duplicate v5 ownership sentence for {name}")
            owners.add(owner)
        metrics["v5_skill_count"] = len(items)
    except Exception as exc:
        errors.append(f"invalid v5 skill manifest: {exc}")
        declared = {}
    try:
        manifest = _load(root / "evals/v5/manifest.json")
        if manifest.get("version") != 5:
            errors.append("v5 eval manifest must declare version 5")
        assets = manifest.get("assets", [])
        if not isinstance(assets, list) or len(assets) != 4:
            errors.append("v5 eval manifest must declare exactly four behavior planes")
            assets = [] if not isinstance(assets, list) else assets
        total = 0
        ids: set[str] = set()
        semantic_mutations = 0
        interaction_cases = 0
        declared_names = set(declared)
        for path in assets:
            if not isinstance(path, str) or not path:
                errors.append("v5 eval manifest asset requires path")
                continue
            doc = _load(root / path)
            if doc.get("version") != 5:
                errors.append(f"v5 eval asset {path} must declare version 5")
            cases = doc.get("cases", [])
            if not isinstance(cases, list):
                errors.append(f"v5 eval asset {path} requires cases[]")
                continue
            if "semantic-mutations" in path:
                semantic_mutations += len(cases)
            if "skill-interactions" in path:
                interaction_cases += len(cases)
            for case in cases:
                total += 1
                cid = case.get("id") if isinstance(case, dict) else None
                if not isinstance(cid, str) or not cid:
                    errors.append(f"v5 eval asset {path} contains case without id")
                    continue
                if cid in ids:
                    errors.append(f"duplicate v5 eval case id {cid}")
                ids.add(cid)
                required = case.get("required_skills", [])
                if not isinstance(required, list) or not required:
                    errors.append(f"v5 eval case {cid} requires required_skills")
                else:
                    unknown = sorted(set(required) - declared_names)
                    if unknown:
                        errors.append(f"v5 eval case {cid} references unknown skills {unknown}")
                if not isinstance(case.get("must_find"), list) or len(case.get("must_find", [])) < 2:
                    errors.append(f"v5 eval case {cid} requires at least two must_find findings")
                if "skill-interactions" in path:
                    if len(set(required)) < 2:
                        errors.append(f"v5 interaction case {cid} must combine at least two skills")
                    if not case.get("objective_delta_reviewed") or "baseline" not in case or "combined" not in case:
                        errors.append(f"v5 interaction case {cid} lacks factorial comparison evidence")
                if "semantic-mutations" in path:
                    if case.get("expected") != "FAIL" or not case.get("target_skill") or not case.get("detected_by"):
                        errors.append(f"v5 semantic mutation {cid} lacks executable detection mapping")
        if manifest.get("case_count") != total:
            errors.append(f"v5 eval manifest case_count {manifest.get('case_count')} does not match discovered {total}")
        if total < 28:
            errors.append(f"v5 eval corpus requires at least 28 cases, found {total}")
        if "v5-atlas-green-runtime-affective-fail" not in ids:
            errors.append("v5 eval corpus must contain ATLAS green-runtime/failed-affect regression")
        metrics["v5_adversarial_cases"] = total
        metrics["v5_semantic_mutations"] = semantic_mutations
        metrics["v5_skill_interactions"] = interaction_cases
    except Exception as exc:
        errors.append(f"invalid v5 eval corpus: {exc}")
    # v6 deep research, industry ontology, skill depth and causal evaluation planes.
    for relative in REQUIRED_V6:
        if not (root / relative).is_file():
            errors.append(f"missing required v6 repository file: {relative}")
    try:
        graph = _load(root / "skills/skill-graph.json")
        declared = graph.get("skills", {})
        manifest6 = _load(root / "knowledge/v6-skill-manifest.json")
        if manifest6.get("version") != 6:
            errors.append("v6 skill manifest must declare version 6")
        items6 = manifest6.get("skills", [])
        if not isinstance(items6, list) or len(items6) != 4:
            errors.append(f"v6 skill manifest must contain exactly 4 new decision owners, found {len(items6) if isinstance(items6,list) else 0}")
            items6 = items6 if isinstance(items6, list) else []
        for item in items6:
            name = item.get("name")
            node = declared.get(name)
            if not node:
                errors.append(f"v6 manifest skill {name} is not declared in skill graph")
                continue
            for field in ("family", "parent", "output", "ownership"):
                if node.get(field) != item.get(field):
                    errors.append(f"v6 manifest/graph mismatch for {name}.{field}")
        metrics["v6_skill_count"] = len(items6)
    except Exception as exc:
        errors.append(f"invalid v6 skill manifest: {exc}")
        declared = declared if 'declared' in locals() else {}
    try:
        source_registry = _load(root / "knowledge/ui-source-intelligence-v6.json")
        source_result = _source_v6.validate_source_intelligence_registry(source_registry)
        errors.extend(f"v6 source intelligence: {e}" for e in source_result.get("errors", []))
        metrics["v6_source_count"] = source_result.get("source_count", 0)
        metrics["v6_source_domain_count"] = len(source_result.get("domains", []))
        metrics["v6_source_role_count"] = len(source_result.get("roles", []))
        metrics["v6_source_anchor_count"] = source_result.get("anchor_count", 0)
    except Exception as exc:
        errors.append(f"invalid v6 source intelligence registry: {exc}")
    try:
        ontology = _load(root / "knowledge/ui-industry-ontology-v6.json")
        ontology_result = _depth_v6.validate_industry_ontology(ontology, set(declared))
        errors.extend(f"v6 industry ontology: {e}" for e in ontology_result.get("errors", []))
        metrics["v6_ontology_axes"] = ontology_result.get("axis_count", 0)
        metrics["v6_ontology_values"] = ontology_result.get("axis_value_count", 0)
        metrics["v6_interaction_cells"] = ontology_result.get("interaction_cell_count", 0)
    except Exception as exc:
        errors.append(f"invalid v6 industry ontology: {exc}")
    try:
        constitution = _load(root / "knowledge/skill-depth-constitution-v6.json")
        dims = constitution.get("dimensions", {}) if isinstance(constitution, dict) else {}
        if constitution.get("version") != 6 or set(dims) != set(_depth_v6.SKILL_DEPTH_DIMENSIONS):
            errors.append("v6 skill-depth constitution must declare all ten behavioral dimensions")
        forbidden = set(constitution.get("forbidden_proxies", []))
        if not {"word_count", "token_count"}.issubset(forbidden):
            errors.append("v6 skill-depth constitution must forbid word/token-count depth proxies")
        metrics["v6_depth_dimensions"] = len(dims)
        focus = _load(root / "knowledge/v6-depth-focus-obligations.json")
        focus_skills = focus.get("skills", {}) if isinstance(focus, dict) else {}
        focus_names = set(focus_skills)
        declared_names = set(declared)
        if focus_names != declared_names:
            missing = sorted(declared_names - focus_names)
            unexpected = sorted(focus_names - declared_names)
            errors.append(
                "v6 depth focus must exactly cover the canonical skill graph"
                + (f"; missing {missing}" if missing else "")
                + (f"; unexpected {unexpected}" if unexpected else "")
            )
        global_terms: list[str] = []
        for skill, terms in focus_skills.items():
            path = root / "skills" / skill / "SKILL.md"
            if not path.is_file():
                errors.append(f"v6 depth focus references missing skill {skill}")
                continue
            if not isinstance(terms, list) or len(terms) != 5:
                errors.append(f"v6 depth focus skill {skill} requires exactly five bespoke semantic obligations")
                terms = terms if isinstance(terms, list) else []
            normalized_terms = [str(term).strip().lower() for term in terms]
            if len(normalized_terms) != len(set(normalized_terms)):
                errors.append(f"v6 depth focus skill {skill} contains duplicate semantic obligations")
            global_terms.extend(normalized_terms)
            text = path.read_text(encoding="utf-8").lower()
            for term in terms:
                if str(term).lower() not in text:
                    errors.append(f"v6 depth focus skill {skill} missing semantic obligation: {term}")
            if "falsif" not in text or "recovery" not in text:
                errors.append(f"v6 depth focus skill {skill} requires falsification and recovery behavior")
        if len(global_terms) != len(set(global_terms)):
            errors.append("v6 depth focus semantic obligations must be globally unique to resist templated depth")
        metrics["v6_depth_focus_skill_count"] = len(focus_skills)
    except Exception as exc:
        errors.append(f"invalid v6 skill-depth plane: {exc}")
    try:
        eval_manifest = _load(root / "evals/v6/manifest.json")
        if eval_manifest.get("version") != 6:
            errors.append("v6 eval manifest must declare version 6")
        assets = eval_manifest.get("assets", [])
        if not isinstance(assets, list) or len(assets) != 4:
            errors.append("v6 eval manifest must declare exactly four planes")
            assets = assets if isinstance(assets, list) else []
        total = 0
        ids: set[str] = set()
        for rel in assets:
            doc = _load(root / rel)
            if doc.get("version") != 6:
                errors.append(f"v6 eval asset {rel} must declare version 6")
            cases = doc.get("cases", [])
            if not isinstance(cases, list):
                errors.append(f"v6 eval asset {rel} requires cases[]")
                continue
            for case in cases:
                total += 1
                if not isinstance(case, dict):
                    errors.append(f"v6 eval asset {rel} contains non-object case"); continue
                cid = case.get("id")
                if not isinstance(cid, str) or not cid:
                    errors.append(f"v6 eval asset {rel} contains case without id"); continue
                if cid in ids: errors.append(f"duplicate v6 eval case id {cid}")
                ids.add(cid)
                for field in ("required_skills", "setup", "pressure", "expected_decision", "evidence_requirements", "evaluator_owner"):
                    if not case.get(field): errors.append(f"v6 eval case {cid} requires {field}")
                required = case.get("required_skills", [])
                if isinstance(required, list):
                    unknown = sorted(set(required)-set(declared))
                    if unknown: errors.append(f"v6 eval case {cid} references unknown skills {unknown}")
                evaluator = case.get("evaluator_owner")
                if evaluator and evaluator not in declared:
                    errors.append(f"v6 eval case {cid} evaluator_owner references unknown skill {evaluator}")
        if eval_manifest.get("case_count") != total:
            errors.append(f"v6 eval manifest case_count {eval_manifest.get('case_count')} does not match discovered {total}")
        if total < 32: errors.append(f"v6 eval corpus requires at least 32 cases, found {total}")
        metrics["v6_adversarial_cases"] = total
    except Exception as exc:
        errors.append(f"invalid v6 eval corpus: {exc}")
    return {"valid": not errors, "errors": errors, "warnings": warnings, "metrics": metrics}


__all__ = [
    "validate_completion_packet", "validate_repository", "validate_skill_graph",
    "validate_state_matrix", "validate_tokens", "validate_industry_atlas",
    "validate_source_ledger", "validate_research_saturation", "validate_bounded_saturation",
    "validate_research_radar", "validate_mandatory_routes", "mandatory_routes_for_profile",
    "validate_v3_completion_evidence", "validate_v4_completion_evidence", "validate_v5_completion_evidence", "validate_v6_completion_evidence",
]
