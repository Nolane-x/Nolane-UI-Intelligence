"""Structural checks for the NUI v8 agent/media and flagship synthesis plane."""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any
from . import interop

REQUIRED = (
    "knowledge/v8-skill-manifest.json", "knowledge/v8-depth-obligations.json",
    "knowledge/agent-interop-v8.json", "knowledge/external-skill-trust-v8.json",
    "knowledge/tool-learning-sources-v8.json", "knowledge/tool-learning-sources-v8-extension.json",
    "knowledge/visual-media-sources-v8.json", "knowledge/visual-media-sources-v8-extension.json",
    "knowledge/creative-toolchain-v8.json", "knowledge/creative-toolchain-v8-extension.json",
    "knowledge/shape-substitution-v8.json", "knowledge/flagship-visual-synthesis-v8.json",
    "src/nolane_ui/interop.py", "src/nolane_ui/media.py", "src/nolane_ui/flagship.py",
    "src/nolane_ui/mcp_server.py", ".agents/skills/nolane-ui/SKILL.md", ".claude/skills/nolane-ui/SKILL.md",
    "scripts/nui-agent-export", "scripts/nui-mcp-server",
    "schemas/agent-interop.schema.json", "schemas/asset-provenance-ledger.schema.json",
    "schemas/external-skill-trust.schema.json", "schemas/visual-media-plan.schema.json",
    "schemas/creative-toolchain.schema.json", "schemas/visual-asset-integration.schema.json",
    "schemas/flagship-visual-synthesis.schema.json", "docs/V8-FLAGSHIP-VISUAL-SYNTHESIS-CLOSURE.md",
    "evals/v8/manifest.json", "evals/v8/agent-interop/cases.json",
    "evals/v8/external-skill-trust/cases.json", "evals/v8/visual-media/cases.json",
    "evals/v8/creative-toolchain/cases.json", "artifacts/v8-completion-packet.example.json"
)


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def merge_ids(a: list[dict[str, Any]], b: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], bool]:
    items = list(a) + list(b)
    ids = [str(x.get("id", "")) for x in items if isinstance(x, dict)]
    return items, bool(ids) and len(ids) == len(set(ids)) and all(ids)


def extend(root: Path, base: dict[str, Any]) -> dict[str, Any]:
    errors = list(base.get("errors", [])); warnings = list(base.get("warnings", [])); metrics = dict(base.get("metrics", {}))
    for rel in REQUIRED:
        if not (root / rel).is_file(): errors.append(f"missing required v8 file: {rel}")
    try:
        graph = load(root / "skills/skill-graph.json").get("skills", {})
        manifest = load(root / "knowledge/v8-skill-manifest.json")
        items = manifest.get("skills", [])
        if len(graph) < 174: errors.append(f"v8 graph must retain at least the 174-skill historical baseline, found {len(graph)}")
        if manifest.get("version") != 8 or len(items) != 8: errors.append("v8 manifest requires version 8 and eight owners")
        for item in items:
            name = item.get("name"); node = graph.get(name, {})
            if not node: errors.append(f"v8 owner missing from graph: {name}"); continue
            for key in ("family", "parent", "output"):
                if node.get(key) != item.get(key): errors.append(f"v8 graph mismatch: {name}.{key}")
            if not (root / "skills" / str(name) / "SKILL.md").is_file(): errors.append(f"v8 owner missing SKILL.md: {name}")
        metrics["skill_count"] = len(graph); metrics["v8_skill_count"] = len(items)
    except Exception as exc: errors.append(f"v8 skill plane: {exc}"); graph = {}
    try:
        old = load(root / "knowledge/v6-depth-focus-obligations.json").get("skills", {})
        new = load(root / "knowledge/v8-depth-obligations.json").get("skills", {})
        if set(old) & set(new): errors.append("v8 depth extension overlaps earlier owner keys")
        union = dict(old); union.update(new)
        if len(union) != 174: errors.append(f"v8 combined depth baseline must retain 174 historical skills, found {len(union)}")
        missing_baseline = sorted(set(union) - set(graph))
        if missing_baseline: errors.append(f"v8 combined depth baseline missing from canonical graph: {missing_baseline}")
        terms: list[str] = []
        for name, anchors in union.items():
            if not isinstance(anchors, list) or len(anchors) != 5: errors.append(f"depth owner requires five anchors: {name}"); continue
            norm = [str(x).strip().lower() for x in anchors]; terms.extend(norm)
            path = root / "skills" / name / "SKILL.md"
            if path.is_file():
                text = path.read_text(encoding="utf-8").lower()
                for anchor in norm:
                    if anchor not in text: errors.append(f"depth anchor absent from {name}: {anchor}")
                if "falsif" not in text or "recovery" not in text: errors.append(f"depth owner needs falsification/recovery: {name}")
        if len(terms) != len(set(terms)): errors.append("combined depth anchors must be globally unique")
        metrics["depth_locked_skill_count"] = len(union); metrics["v8_depth_extension_count"] = len(new)
    except Exception as exc: errors.append(f"v8 depth plane: {exc}")
    try:
        r = interop.validate_agent_interop_registry(load(root / "knowledge/agent-interop-v8.json"))
        errors.extend(f"v8 interop: {x}" for x in r.get("errors", []))
        if r.get("adapter_count") != 9: errors.append("v8 requires nine adapter records")
        metrics["v8_agent_adapter_count"] = r.get("adapter_count", 0)
    except Exception as exc: errors.append(f"v8 interop plane: {exc}")
    try:
        tools, ok1 = merge_ids(load(root/"knowledge/tool-learning-sources-v8.json").get("sources", []), load(root/"knowledge/tool-learning-sources-v8-extension.json").get("sources", []))
        media, ok2 = merge_ids(load(root/"knowledge/visual-media-sources-v8.json").get("sources", []), load(root/"knowledge/visual-media-sources-v8-extension.json").get("sources", []))
        creative, ok3 = merge_ids(load(root/"knowledge/creative-toolchain-v8.json").get("tools", []), load(root/"knowledge/creative-toolchain-v8-extension.json").get("tools", []))
        if not (ok1 and ok2 and ok3): errors.append("v8 registry ids must be non-empty and unique")
        if len(tools) < 14 or len(media) < 14 or len(creative) < 14: errors.append("v8 registry breadth requires 14 tool-learning, 14 media, and 14 creative entries")
        classes = {str(x.get("kind") or x.get("class") or "") for x in media if isinstance(x, dict)} - {""}
        if len(classes) < 8: errors.append("v8 media coverage requires at least eight source classes")
        metrics.update(v8_tool_learning_sources=len(tools), v8_visual_media_sources=len(media), v8_media_source_classes=len(classes), v8_creative_tools=len(creative))
    except Exception as exc: errors.append(f"v8 registry plane: {exc}")
    try:
        synthesis = load(root / "knowledge/flagship-visual-synthesis-v8.json")
        planes = synthesis.get("planes", [])
        attractors = synthesis.get("anti_generic_attractors", [])
        tests = synthesis.get("perceptual_tests", [])
        if synthesis.get("version") != 8: errors.append("flagship synthesis knowledge must declare version 8")
        if len(planes) != 12: errors.append(f"flagship synthesis requires twelve distinct decision planes, found {len(planes)}")
        plane_ids = [str(x.get("id", "")) for x in planes if isinstance(x, dict)]
        if not plane_ids or len(plane_ids) != len(set(plane_ids)) or any(not x for x in plane_ids):
            errors.append("flagship synthesis plane ids must be unique and non-empty")
        for item in planes:
            if not isinstance(item, dict) or not all(item.get(k) for k in ("name", "owns", "rejects", "evidence")):
                errors.append(f"flagship synthesis plane is incomplete: {item.get('id') if isinstance(item, dict) else item}")
        if len(attractors) < 6: errors.append("flagship synthesis requires at least six anti-generic diagnostic attractors")
        if len(tests) < 7: errors.append("flagship synthesis requires at least seven perceptual falsification tests")
        metrics.update(v8_flagship_synthesis_planes=len(planes), v8_anti_generic_attractors=len(attractors), v8_perceptual_tests=len(tests))
    except Exception as exc: errors.append(f"v8 flagship synthesis plane: {exc}")
    try:
        m = load(root / "evals/v8/manifest.json"); assets = m.get("assets", []); total = 0; ids: set[str] = set()
        if m.get("version") != 8 or len(assets) != 4: errors.append("v8 eval manifest requires four planes")
        for rel in assets:
            d = load(root / rel); cases = d.get("cases", [])
            if d.get("version") != 8 or len(cases) != 8: errors.append(f"v8 eval plane requires eight cases: {rel}")
            for c in cases:
                total += 1; cid = c.get("id") if isinstance(c, dict) else None
                if not cid or cid in ids: errors.append(f"v8 eval id invalid: {cid}")
                if cid: ids.add(cid)
                if not isinstance(c, dict) or not c.get("expected_decision") or not c.get("evaluator_owner") or len(c.get("must_find", [])) < 2: errors.append(f"v8 eval case incomplete: {cid}")
        if total != 32 or m.get("case_count") != 32: errors.append(f"v8 eval corpus requires 32 cases, found {total}")
        metrics["v8_adversarial_cases"] = total
    except Exception as exc: errors.append(f"v8 eval plane: {exc}")
    return {"valid": not errors, "errors": errors, "warnings": warnings, "metrics": metrics}
