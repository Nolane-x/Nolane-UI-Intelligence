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
else:
    _legacy = _load_sibling("validators_legacy.py", "nui_validators_legacy")
    _industry = _load_sibling("industry.py", "nui_industry")
    _emerging = _load_sibling("emerging.py", "nui_emerging")

validate_completion_packet = _legacy.validate_completion_packet
validate_skill_graph = _legacy.validate_skill_graph
validate_state_matrix = _legacy.validate_state_matrix
validate_tokens = _legacy.validate_tokens
validate_industry_atlas = _industry.validate_industry_atlas
validate_source_ledger = _industry.validate_source_ledger
validate_research_saturation = _industry.validate_research_saturation


def mandatory_routes_for_profile(profile: dict[str, Any]) -> set[str]:
    return _industry.mandatory_routes_for_profile(profile) | _emerging.mandatory_emerging_routes(profile)


def validate_mandatory_routes(profile: dict[str, Any], selected_skills: Iterable[str]) -> dict[str, Any]:
    required = mandatory_routes_for_profile(profile)
    selected = set(selected_skills)
    missing = sorted(required - selected)
    return {"valid": not missing, "required_routes": sorted(required), "missing_routes": missing}


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
        "knowledge/v2-skill-manifest.json",
        "knowledge/emerging-skill-manifest.json",
        "knowledge/ui-domain-atlas-emerging.json",
        "knowledge/source-ledger-emerging.json",
        "evals/v2/coverage/required-domains.json",
        "evals/v2/coverage/emerging-domains.json",
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

        extension = _load(root / "knowledge/ui-domain-atlas-emerging.json")
        extension_result = validate_industry_atlas(extension, graph)
        errors.extend(f"emerging industry atlas: {item}" for item in extension_result["errors"])
        metrics["emerging_coverage_cells"] = extension_result["coverage_cell_count"]
    except Exception as exc:
        errors.append(f"invalid industry atlas/graph: {exc}")

    try:
        ledger = _load(root / "knowledge/source-ledger.json")
        ledger_result = validate_source_ledger(ledger)
        errors.extend(f"source ledger: {item}" for item in ledger_result["errors"])
        warnings.extend(f"source ledger: {item}" for item in ledger_result["warnings"])
        metrics["research_source_count"] = ledger_result["source_count"]

        emerging_ledger = _load(root / "knowledge/source-ledger-emerging.json")
        emerging_result = validate_source_ledger(emerging_ledger)
        errors.extend(f"emerging source ledger: {item}" for item in emerging_result["errors"])
        warnings.extend(f"emerging source ledger: {item}" for item in emerging_result["warnings"])
        metrics["emerging_research_source_count"] = emerging_result["source_count"]
    except Exception as exc:
        errors.append(f"invalid source ledger: {exc}")

    try:
        saturation = _load(root / "knowledge/research-saturation.json")
        saturation_result = validate_research_saturation(saturation, ledger, atlas)
        errors.extend(f"research saturation: {item}" for item in saturation_result["errors"])
        metrics["research_saturation"] = saturation_result.get("decision")
    except Exception as exc:
        errors.append(f"invalid research saturation record: {exc}")

    try:
        manifests = [
            _load(root / "knowledge/v2-skill-manifest.json"),
            _load(root / "knowledge/emerging-skill-manifest.json"),
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
    "validate_source_ledger", "validate_research_saturation",
    "validate_mandatory_routes", "mandatory_routes_for_profile",
]
