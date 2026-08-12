"""NUI v2 deterministic validation facade.

v1 invariants are preserved verbatim in validators_legacy. This module layers
industry coverage/freshness gates on top instead of weakening established gates.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .validators_legacy import (
    validate_completion_packet,
    validate_repository as _validate_repository_v1,
    validate_skill_graph,
    validate_state_matrix,
    validate_tokens,
)
from .industry import (
    mandatory_routes_for_profile,
    validate_industry_atlas,
    validate_mandatory_routes,
    validate_research_saturation,
    validate_source_ledger,
)


def _load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_repository(root: Path | str) -> dict[str, Any]:
    root = Path(root)
    base = _validate_repository_v1(root)
    errors = list(base.get("errors", []))
    warnings = list(base.get("warnings", []))
    metrics = dict(base.get("metrics", {}))

    required_v2 = [
        "knowledge/ui-domain-atlas.json",
        "knowledge/source-ledger.json",
        "knowledge/research-radar.json",
        "knowledge/research-saturation.json",
        "knowledge/v2-skill-manifest.json",
        "evals/v2/coverage/required-domains.json",
    ]
    for relative in required_v2:
        if not (root / relative).is_file():
            errors.append(f"missing required v2 repository file: {relative}")

    graph: dict[str, Any] = {}
    atlas: dict[str, Any] = {}
    ledger: dict[str, Any] = {}
    saturation: dict[str, Any] = {}
    try:
        graph = _load(root / "skills/skill-graph.json")
        atlas = _load(root / "knowledge/ui-domain-atlas.json")
        atlas_result = validate_industry_atlas(atlas, graph)
        errors.extend(f"industry atlas: {item}" for item in atlas_result["errors"])
        metrics["industry_coverage_cells"] = atlas_result["coverage_cell_count"]
    except Exception as exc:
        errors.append(f"invalid industry atlas/graph: {exc}")

    try:
        ledger = _load(root / "knowledge/source-ledger.json")
        ledger_result = validate_source_ledger(ledger)
        errors.extend(f"source ledger: {item}" for item in ledger_result["errors"])
        warnings.extend(f"source ledger: {item}" for item in ledger_result["warnings"])
        metrics["research_source_count"] = ledger_result["source_count"]
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
        manifest = _load(root / "knowledge/v2-skill-manifest.json")
        metrics["v2_skill_count"] = len(manifest.get("skills", []))
        declared = graph.get("skills", {}) if graph else {}
        for item in manifest.get("skills", []):
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
