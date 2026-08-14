"""NUI v8 compatibility validator facade.

Package imports receive the v8 overlay. Historical standalone imports keep the
frozen v7 API so older kernel tests and direct file loaders remain compatible.
"""
from __future__ import annotations

import importlib.util
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


if not __package__:
    _v7 = _load_sibling("validators_v7.py", "nui_validators_v7_compat")
    for _name in dir(_v7):
        if not _name.startswith("_"):
            globals()[_name] = getattr(_v7, _name)
else:
    from .validators_v7 import *  # noqa: F401,F403
    from . import validators_v7 as _v7
    from . import v8_repository as _repo8
    from . import interop as _interop8
    from . import media as _media8

    def mandatory_routes_for_profile(profile: dict[str, Any]) -> set[str]:
        return _v7.mandatory_routes_for_profile(profile) | _media8.mandatory_v8_routes(profile)

    def validate_mandatory_routes(profile: dict[str, Any], selected_skills: Iterable[str]) -> dict[str, Any]:
        required = mandatory_routes_for_profile(profile)
        missing = sorted(required - set(selected_skills))
        return {"valid": not missing, "required_routes": sorted(required), "missing_routes": missing}

    def _pass(value: Any) -> bool:
        return isinstance(value, dict) and value.get("status") in {"PASS", "READY", "SUPPORTED"}

    def validate_v8_completion_evidence(record: dict[str, Any]) -> dict[str, Any]:
        if not isinstance(record, dict):
            return {"decision": "BLOCKED", "errors": ["v8 completion evidence must be an object"]}
        errors = list(_v7.validate_v7_completion_evidence(record).get("errors", []))
        if record.get("external_agent_skill") or record.get("external_agent_skills_material"):
            review = record.get("external_skill_trust")
            if not _pass(review):
                checked = _interop8.validate_external_skill_trust(review) if isinstance(review, dict) else {"errors": ["missing reviewed external-skill evidence"]}
                errors.extend(checked.get("errors", []))
        if record.get("agent_harness") or record.get("agent_harness_export"):
            evidence = record.get("agent_interop_evidence")
            if not _pass(evidence) or evidence.get("authority_escalation") is not False:
                errors.append("agent harness requires PASS interoperability evidence with bounded authority")
        if record.get("external_media_used") or record.get("external_visual_assets"):
            value = record.get("asset_provenance_ledger")
            checked = _media8.validate_asset_provenance_ledger(value) if isinstance(value, dict) else {"errors": ["missing asset provenance ledger"]}
            errors.extend(checked.get("errors", []))
        subject_native = bool(record.get("subject_native_media"))
        if subject_native:
            value = record.get("media_opportunity_map")
            checked = _media8.validate_media_opportunity_map(value) if isinstance(value, dict) else {"errors": ["missing media opportunity map"]}
            errors.extend(checked.get("errors", []))
            value = record.get("shape_substitution_audit")
            checked = _media8.validate_shape_substitution_audit(value) if isinstance(value, dict) else {"errors": ["missing representation audit"], "decision": "RE_DIVERGE"}
            errors.extend(checked.get("errors", []))
            if checked.get("decision") == "RE_DIVERGE":
                errors.append("material representation requires re-divergence before release")
        if record.get("custom_visual_asset") or record.get("generated_media"):
            value = record.get("creative_toolchain_plan")
            checked = _media8.validate_creative_toolchain_plan(value) if isinstance(value, dict) else {"errors": ["missing creative toolchain plan"]}
            errors.extend(checked.get("errors", []))
            if not _pass(record.get("domain_native_asset_brief")):
                errors.append("custom material media requires domain-native asset brief PASS")
        if record.get("material_media_used") or subject_native:
            value = record.get("visual_asset_integration")
            checked = _media8.validate_visual_asset_integration(value) if isinstance(value, dict) else {"errors": ["missing visual asset integration evidence"]}
            errors.extend(checked.get("errors", []))
        return {"decision": "BLOCKED" if errors else "PASS", "errors": errors}

    def validate_repository(root: Path | str) -> dict[str, Any]:
        root = Path(root)
        base = dict(_v7.validate_repository(root))
        prefix = "v6 depth focus must exactly cover the canonical skill graph"
        base["errors"] = [e for e in base.get("errors", []) if not str(e).startswith(prefix)]
        base["valid"] = not base["errors"]
        return _repo8.extend(root, base)
