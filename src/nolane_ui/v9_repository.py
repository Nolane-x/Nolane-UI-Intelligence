"""Structural closure checks for NUI v9 product-completeness and perceptual craft."""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


REQUIRED = (
    "src/nolane_ui/product_v9.py",
    "src/nolane_ui/scope_v9.py",
    "src/nolane_ui/routing_v9.py",
    "src/nolane_ui/v9_repository.py",
    "knowledge/v9-design-benchmark-gallery.json",
    "knowledge/v9-domain-signatures.json",
    "knowledge/v9-render-fidelity.json",
    "evals/v9-product-completeness-adversarial.json",
    "docs/V9-PRODUCT-COMPLETENESS-TASTE-CLOSURE.md",
    "docs/superpowers/plans/2026-08-14-product-completeness-taste-v9.md",
    "tests/test_product_v9.py",
    "tests/test_v9_completion.py",
    "tests/test_v9_knowledge.py",
    "tests/test_v9_skill_protocols.py",
    "tests/test_v9_routing.py",
    "tests/test_v9_adversarial.py",
    "tests/test_v9_repository.py",
)

SKILL_ANCHORS: dict[str, tuple[str, ...]] = {
    "modeling-product-intent": ("V9 Product Envelope Discovery", "broad-before-narrow", "scope adequacy challenge"),
    "inventorying-product-capabilities": ("V9 Expected-Capability Disposition", "REQUIRED", "EXPECTED", "EXCLUDED"),
    "architecting-information": ("V9 Settings Architecture", "scope precedence", "settings search", "recovery/reset"),
    "designing-authentication-and-passkeys": ("V9 Account Continuity Boundary", "account/workspace lifecycle"),
    "modeling-users-and-tasks": ("V9 Audience Strategy Sensitivity", "trust-first", "delight-first"),
    "exploring-aesthetic-directions": ("V9 Comparative Taste Discrimination", "cheap-looking", "premium", "editorial"),
    "critiquing-visual-design": ("V9 Rendered Design-Director Court", "screenshot-based critique", "A/B"),
    "verifying-design-fidelity": ("V9 Design-to-Render Fidelity", "default chrome", "scrollbar", "visual regression"),
    "designing-editor-canvas-workspaces": ("V9 Instrument Architecture", "context inspector", "asset/resource"),
    "designing-desktop-windowed-workspaces": ("V9 Professional Workspace Completeness", "secondary panels", "status surface"),
    "designing-motion": ("V9 Motion Direction", "emotional cadence", "intentional absence", "reduced motion equivalence"),
    "engineering-rich-interactive-components": ("V9 Motion Implementation Fidelity", "semantic motion", "performance degradation"),
}


def _load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _version_at_least(version: str, minimum: tuple[int, int, int]) -> bool:
    """Accept later NUI releases while preserving the historical V9 gate."""
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", version)
    if not match:
        return False
    return tuple(int(part) for part in match.groups()) >= minimum


def extend(root: Path, base: dict[str, Any]) -> dict[str, Any]:
    root = Path(root)
    errors = list(base.get("errors", []))
    warnings = list(base.get("warnings", []))
    metrics = dict(base.get("metrics", {}))

    for rel in REQUIRED:
        if not (root / rel).is_file():
            errors.append(f"missing required v9 file: {rel}")

    try:
        pyproject = (root / "pyproject.toml").read_text(encoding="utf-8")
        match = re.search(r'^version\s*=\s*"([^"]+)"', pyproject, flags=re.MULTILINE)
        version = match.group(1) if match else ""
        if not _version_at_least(version, (0, 9, 0)):
            errors.append("v9 compatibility requires package version >= 0.9.0")
        metrics["nui_major"] = 9
    except Exception as exc:
        errors.append(f"v9 package plane: {exc}")

    try:
        graph = _load(root / "skills/skill-graph.json").get("skills", {})
        if len(graph) < 174:
            errors.append(f"v9 must retain the 174-skill historical baseline; found {len(graph)}")
        metrics["skill_count"] = len(graph)
        for skill, anchors in SKILL_ANCHORS.items():
            if skill not in graph:
                errors.append(f"v9 protocol owner missing from canonical graph: {skill}")
                continue
            path = root / "skills" / skill / "SKILL.md"
            if not path.is_file():
                errors.append(f"v9 protocol owner missing SKILL.md: {skill}")
                continue
            text = path.read_text(encoding="utf-8").lower()
            for anchor in anchors:
                if anchor.lower() not in text:
                    errors.append(f"v9 protocol anchor absent from {skill}: {anchor}")
    except Exception as exc:
        errors.append(f"v9 skill protocol plane: {exc}")

    try:
        gallery = _load(root / "knowledge/v9-design-benchmark-gallery.json")
        refs = gallery.get("references", [])
        if gallery.get("version") != 9 or len(refs) < 12:
            errors.append("v9 benchmark gallery requires version 9 and at least twelve references")
        ref_ids = [x.get("id") for x in refs if isinstance(x, dict)]
        if not ref_ids or len(ref_ids) != len(set(ref_ids)) or any(not x for x in ref_ids):
            errors.append("v9 benchmark reference ids must be unique and non-empty")
        for item in refs:
            if not isinstance(item, dict) or len(item.get("mechanisms", [])) < 2 or not item.get("anti_copy") or not item.get("refresh_policy"):
                errors.append(f"v9 benchmark reference incomplete: {item.get('id') if isinstance(item, dict) else item}")
        metrics["v9_benchmark_references"] = len(refs)
    except Exception as exc:
        errors.append(f"v9 benchmark plane: {exc}")

    try:
        domains = _load(root / "knowledge/v9-domain-signatures.json")
        items = domains.get("domains", [])
        if domains.get("version") != 9 or len(items) < 8:
            errors.append("v9 domain signatures require version 9 and at least eight domains")
        required_domains = {"fintech", "medtech", "developer-tools", "creative-tools", "ai-products", "education", "commerce"}
        ids = {str(x.get("id")) for x in items if isinstance(x, dict)}
        if not required_domains.issubset(ids):
            errors.append("v9 domain signatures are missing required coverage classes")
        for item in items:
            if not isinstance(item, dict) or len(item.get("audience_variants", [])) < 2 or not item.get("anti_patterns"):
                errors.append(f"v9 domain signature incomplete: {item.get('id') if isinstance(item, dict) else item}")
        metrics["v9_domain_signatures"] = len(items)
    except Exception as exc:
        errors.append(f"v9 domain plane: {exc}")

    try:
        fidelity = _load(root / "knowledge/v9-render-fidelity.json")
        if fidelity.get("version") != 9:
            errors.append("v9 render fidelity knowledge must declare version 9")
        if len(fidelity.get("token_dimensions", [])) < 8:
            errors.append("v9 render fidelity requires at least eight token dimensions")
        if len(fidelity.get("component_constraints", [])) < 8:
            errors.append("v9 render fidelity requires at least eight component constraints")
        if len(fidelity.get("default_chrome_audit", [])) < 10:
            errors.append("v9 render fidelity requires broad default-chrome audit coverage")
        if len(fidelity.get("motion_semantics", [])) < 5:
            errors.append("v9 render fidelity requires deep motion semantics")
        metrics["v9_default_chrome_classes"] = len(fidelity.get("default_chrome_audit", []))
    except Exception as exc:
        errors.append(f"v9 render fidelity plane: {exc}")

    try:
        corpus = _load(root / "evals/v9-product-completeness-adversarial.json")
        cases = corpus.get("cases", [])
        if corpus.get("version") != 9 or len(cases) < 24:
            errors.append("v9 adversarial corpus requires version 9 and at least twenty-four cases")
        ids = [x.get("id") for x in cases if isinstance(x, dict)]
        if len(ids) != len(cases) or len(ids) != len(set(ids)) or any(not x for x in ids):
            errors.append("v9 adversarial ids must be unique and non-empty")
        verdicts = {x.get("expected_verdict") for x in cases if isinstance(x, dict)}
        if not {"BLOCK", "ALLOW"}.issubset(verdicts):
            errors.append("v9 adversarial corpus must include both blocking and anti-overcorrection allow cases")
        metrics["v9_adversarial_cases"] = len(cases)
    except Exception as exc:
        errors.append(f"v9 adversarial plane: {exc}")

    try:
        workflow = (root / ".github/workflows/verify.yml").read_text(encoding="utf-8")
        historical_artifacts = (
            "nui-v9-completion-packet" in workflow and "Nolane-UI-Intelligence-v9-complete.zip" in workflow
        )
        inherited_artifacts = (
            "nui-v10-completion-packet" in workflow and "Nolane-UI-Intelligence-v10-complete.zip" in workflow
        )
        if not (historical_artifacts or inherited_artifacts):
            errors.append("v9 release compatibility requires a V9-or-later completion packet and complete-project ZIP")

        script = (root / "scripts/nui-release-packet").read_text(encoding="utf-8")
        historical_packet = "NUI-V9-STRUCTURAL" in script and "validate_v9_completion_evidence" in script
        inherited_packet = "NUI-V10-STRUCTURAL" in script and "validate_v10_completion_evidence" in script
        if not (historical_packet or inherited_packet):
            errors.append("v9 release compatibility requires a V9-or-later structural completion packet")
    except Exception as exc:
        errors.append(f"v9 release plane: {exc}")

    return {"valid": not errors, "errors": errors, "warnings": warnings, "metrics": metrics}


__all__ = ["extend"]
