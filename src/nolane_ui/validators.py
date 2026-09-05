"""NUI compatibility validator facade.

Package imports receive the current overlay. Historical standalone imports keep
the frozen v7 API so older kernel tests and direct file loaders remain compatible.
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


if not __package__:
    _v7 = _load_sibling("validators_v7.py", "nui_validators_v7_compat")
    for _name in dir(_v7):
        if not _name.startswith("_"):
            globals()[_name] = getattr(_v7, _name)
else:
    from .validators_v7 import *  # noqa: F401,F403
    from . import validators_v7 as _v7
    from . import v8_repository as _repo8
    from . import v9_repository as _repo9
    from . import v10_repository as _repo10
    from . import interop as _interop8
    from . import media as _media8
    from . import flagship as _flagship8
    from . import product_v9 as _product9
    from . import scope_v9 as _scope9
    from . import routing_v9 as _routing9
    from . import external_ui_execution as _external_ref_v12
    from . import external_ui_intelligence as _external_ui_v12
    from . import reality_rules as _reality_v12
    from .runtime_v11.doctor import REQUIRED_RUNTIME_ARTIFACTS as _RUNTIME_V11_ARTIFACTS
    from .runtime_v11.doctor import diagnose_runtime_state as _diagnose_runtime_v11
    from .rules_v13.catalog import load_rule_catalog_v13 as _load_rules_v13
    from .rules_v13.similarity import audit_catalog_similarity as _audit_rules_v13

    def mandatory_routes_for_profile(profile: dict[str, Any]) -> set[str]:
        return (
            _v7.mandatory_routes_for_profile(profile)
            | _media8.mandatory_v8_routes(profile)
            | _routing9.mandatory_v9_routes(profile)
        )

    def validate_mandatory_routes(profile: dict[str, Any], selected_skills: Iterable[str]) -> dict[str, Any]:
        required = mandatory_routes_for_profile(profile)
        missing = sorted(required - set(selected_skills))
        return {"valid": not missing, "required_routes": sorted(required), "missing_routes": missing}

    def validate_completion_packet(
        packet: dict[str, Any], root: Path | str, expected_revision: str | None = None
    ) -> dict[str, Any]:
        """Apply historical completion semantics plus V12 material-reference lineage.

        Standalone/direct-file consumers keep the frozen V7 facade above. Package
        consumers get the current overlay: material UI completion cannot PASS when
        its task-bound external reference execution contract is missing, stale, or
        has dropped required packs/sources/checkpoints. Because this validator is
        the release court, V12.1 requires the full RELEASED lineage, including
        provenance, rather than stopping at the VERIFIED observation stage.
        """
        base = dict(_v7.validate_completion_packet(packet, root, expected_revision))
        profile = packet.get("task_profile") if isinstance(packet, dict) else None
        if not isinstance(profile, dict) or profile.get("material_ui") is not True:
            return base

        errors = list(base.get("errors", []))
        contract = packet.get("reference_execution")
        if not isinstance(contract, dict):
            errors.append("material UI completion requires V12.1 reference execution contract")
        else:
            routing_path = Path(root) / "knowledge" / "external-ui-generation-routing-v12.json"
            try:
                routing = json.loads(routing_path.read_text(encoding="utf-8"))
            except Exception as exc:
                errors.append(f"V12.1 reference execution routing unavailable: {exc}")
            else:
                contract_result = _external_ref_v12.validate_reference_execution_contract(
                    contract, profile, routing
                )
                errors.extend(
                    f"reference execution: {error}" for error in contract_result.get("errors", [])
                )
                lineage_result = _external_ref_v12.validate_reference_completion(contract, "RELEASED")
                errors.extend(
                    f"reference execution: {error}" for error in lineage_result.get("errors", [])
                )

        if errors:
            return {**base, "decision": "BLOCKED", "errors": errors}
        return base

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

        ambition = str(record.get("visual_ambition", "")).strip().lower()
        if ambition in {"flagship", "exceptional", "experiential"}:
            value = record.get("flagship_visual_synthesis")
            if isinstance(value, dict):
                checked = _flagship8.validate_flagship_visual_synthesis(value)
                errors.extend(f"flagship visual synthesis: {error}" for error in checked.get("errors", []))
            else:
                errors.append("flagship visual synthesis evidence is required for flagship, exceptional, or experiential completion")

        return {"decision": "BLOCKED" if errors else "PASS", "errors": errors}

    def _extend_checked(errors: list[str], label: str, validator, value: Any) -> None:
        if not isinstance(value, dict):
            errors.append(f"{label} evidence is required")
            return
        checked = validator(value)
        errors.extend(f"{label}: {error}" for error in checked.get("errors", []))

    def validate_v9_completion_evidence(record: dict[str, Any]) -> dict[str, Any]:
        """Gate product-wide and high-ambition visual completion claims.

        V8 remains authoritative for inherited media, research, safety and flagship
        synthesis obligations. V9 adds *scope adequacy* before closure and a
        perceptual/render chain after implementation. No score can compensate for
        a failed inherited hard gate.
        """
        if not isinstance(record, dict):
            return {"decision": "BLOCKED", "errors": ["v9 completion evidence must be an object"]}

        errors = list(validate_v8_completion_evidence(record).get("errors", []))
        product_ambition = str(record.get("product_ambition", record.get("product_scope", ""))).strip().lower()
        product_wide = product_ambition in {
            "production", "full-platform", "platform", "enterprise", "production-platform", "full-product"
        } or bool(record.get("product_wide_completion"))

        if product_wide:
            _extend_checked(errors, "capability envelope", _product9.validate_capability_envelope, record.get("capability_envelope"))
            _extend_checked(errors, "scope adequacy", _scope9.validate_scope_adequacy, record.get("scope_adequacy"))

        if record.get("settings_material") or record.get("settings_system"):
            _extend_checked(errors, "settings architecture", _product9.validate_settings_architecture, record.get("settings_architecture"))

        if record.get("account_workspace_material") or record.get("multi_account_workspace"):
            _extend_checked(errors, "account/workspace lifecycle", _product9.validate_account_workspace_lifecycle, record.get("account_workspace_lifecycle"))

        visual_ambition = str(record.get("visual_ambition", "")).strip().lower()
        high_visual = visual_ambition in {"flagship", "exceptional", "experiential"}
        rendered = bool(record.get("material_rendered_ui")) or high_visual
        if rendered:
            _extend_checked(errors, "interface residue audit", _product9.validate_interface_residue_audit, record.get("interface_residue_audit"))

        if high_visual:
            _extend_checked(errors, "taste comparison", _product9.validate_taste_comparison, record.get("taste_comparison"))
            _extend_checked(errors, "render critique", _product9.validate_render_critique, record.get("render_critique"))
            _extend_checked(errors, "domain/audience fit", _product9.validate_domain_audience_fit, record.get("domain_audience_fit"))
            _extend_checked(errors, "render fidelity", _product9.validate_render_fidelity, record.get("render_fidelity"))

        return {"decision": "BLOCKED" if errors else "PASS", "errors": errors}

    def _read_current_package_version(root: Path) -> str | None:
        try:
            pyproject = (root / "pyproject.toml").read_text(encoding="utf-8")
        except OSError:
            return None
        import re
        match = re.search(r'^version\s*=\s*"([^"]+)"', pyproject, flags=re.MULTILINE)
        return match.group(1) if match else None

    def _current_version_coherence(root: Path) -> dict[str, Any]:
        package_version = _read_current_package_version(root)
        try:
            config = json.loads((root / "nui.config.json").read_text(encoding="utf-8"))
            config_version = str(config.get("version", "")).strip() or None
        except Exception:
            config_version = None
        errors: list[str] = []
        expected = "0.13.0"
        if package_version != expected or config_version != expected:
            errors.append(
                f"version coherence: current package/config version must both be {expected}; "
                f"package={package_version!r}, config={config_version!r}"
            )
        return {
            "valid": not errors,
            "errors": errors,
            "package_version": package_version,
            "config_version": config_version,
        }

    def validate_repository(root: Path | str) -> dict[str, Any]:
        root = Path(root)
        base = dict(_v7.validate_repository(root))
        prefix = "v6 depth focus must exactly cover the canonical skill graph"
        base["errors"] = [e for e in base.get("errors", []) if not str(e).startswith(prefix)]
        base["valid"] = not base["errors"]
        v8 = _repo8.extend(root, base)
        v9 = _repo9.extend(root, v8)
        result = dict(_repo10.extend(root, v9))
        errors = list(result.get("errors", []))
        warnings = list(result.get("warnings", []))
        metrics = dict(result.get("metrics", {}))

        version = _current_version_coherence(root)
        errors.extend(version["errors"])
        metrics["package_version"] = version["package_version"]
        metrics["config_version"] = version["config_version"]

        runtime = _diagnose_runtime_v11(root)
        metrics["v11_runtime_artifact_count"] = len(_RUNTIME_V11_ARTIFACTS)
        metrics["v11_runtime_blocking_count"] = int(runtime.get("blocking_count", 0))
        for finding in runtime.get("findings", []):
            if finding.get("severity") == "blocking":
                errors.append(f"v11 runtime: {finding.get('summary', finding.get('id', 'blocking finding'))}")

        try:
            reality = _reality_v12.load_reality_rule_catalog(root)
            reality_result = _reality_v12.validate_reality_rule_catalog(reality)
            metrics["v12_reality_rule_count"] = int(reality_result.get("rule_count", 0))
            errors.extend(f"v12 reality: {error}" for error in reality_result.get("errors", []))
        except Exception as exc:
            errors.append(f"v12 reality: {exc}")

        try:
            network = _external_ui_v12.load_external_ui_network(root)
            packs = json.loads((root / "knowledge" / "external-ui-reference-packs-v12.json").read_text(encoding="utf-8"))
            license_policy = json.loads((root / "knowledge" / "external-ui-license-policy-v12.json").read_text(encoding="utf-8"))
            external_result = _external_ui_v12.validate_external_ui_network(network, packs, license_policy)
            metrics["v12_external_ui_source_count"] = len(network.get("sources", []))
            metrics["v12_external_ui_pack_count"] = len(packs.get("packs", []))
            errors.extend(f"v12 external UI: {error}" for error in external_result.get("errors", []))
        except Exception as exc:
            errors.append(f"v12 external UI: {exc}")

        try:
            catalog = _load_rules_v13(root)
            similarity = _audit_rules_v13(catalog["rules"])
            metrics["v13_rule_count"] = len(catalog["rules"])
            metrics["v13_provenance_record_count"] = len(catalog["provenance"]["records"])
            metrics["v13_duplicate_pair_count"] = int(similarity.get("duplicate_pair_count", 0))
            metrics["v13_boilerplate_cluster_count"] = int(similarity.get("boilerplate_cluster_count", 0))
        except Exception as exc:
            errors.append(f"v13 provenance/catalog: {exc}")

        return {**result, "valid": not errors, "errors": errors, "warnings": warnings, "metrics": metrics}
