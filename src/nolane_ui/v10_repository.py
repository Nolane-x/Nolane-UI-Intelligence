"""Structural and cross-link closure for NUI V10 behavioral empirical proof.

This validator intentionally reports a STRUCTURAL_ONLY claim ceiling.  It proves
that the repository contains a coherent, falsifiable evaluation system; it does
not manufacture real-model efficacy evidence from files or synthetic tests.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from .behavior_v10 import validate_hypothesis_registry
from .benchmark_v10 import validate_task_corpus
from .mutation_v10 import validate_mutation_registry

REQUIRED = (
    "src/nolane_ui/behavior_v10.py",
    "src/nolane_ui/benchmark_v10.py",
    "src/nolane_ui/mutation_v10.py",
    "src/nolane_ui/experiment_v10.py",
    "src/nolane_ui/judging_v10.py",
    "src/nolane_ui/stats_v10.py",
    "src/nolane_ui/claims_v10.py",
    "src/nolane_ui/v10_repository.py",
    "knowledge/v10-behavioral-hypotheses.json",
    "knowledge/v10-empirical-evaluation-sources.json",
    "benchmarks/v10/tasks-public.json",
    "benchmarks/v10/tasks-hidden.json",
    "benchmarks/v10/mutations.json",
    "schemas/v10-experiment.schema.json",
    "schemas/v10-run-record.schema.json",
    "schemas/v10-claim.schema.json",
    "docs/V10-EMPIRICAL-RUN-PROTOCOL.md",
    "docs/superpowers/specs/2026-08-14-v10-behavioral-design-intelligence-design.md",
    "docs/superpowers/plans/2026-08-14-v10-behavioral-empirical-proof.md",
    "evals/v10-behavioral-empirical-adversarial.json",
    "scripts/nui-v10-build-run-matrix",
    "scripts/nui-v10-validate-run-bundle",
    "scripts/nui-v10-aggregate",
    "examples/v10/experiment.example.json",
    "examples/v10/run-record.example.jsonl",
    "tests/test_v10_hypotheses.py",
    "tests/test_v10_benchmark_tasks.py",
    "tests/test_v10_mutations.py",
    "tests/test_v10_experiments.py",
    "tests/test_v10_judging.py",
    "tests/test_v10_stats.py",
    "tests/test_v10_claims.py",
    "tests/test_v10_knowledge.py",
    "tests/test_v10_skill_protocols.py",
    "tests/test_v10_cli_protocol.py",
    "tests/test_v10_repository.py",
    "tests/test_v10_adversarial.py",
)

SKILL_ANCHORS: dict[str, tuple[str, ...]] = {
    "modeling-product-intent": ("V10 Empirical Scope Hypothesis", "H-SCOPE-BREADTH", "scope-compress"),
    "inventorying-product-capabilities": ("V10 Disposition Attribution Protocol", "H-CAPABILITY-DISPOSITION", "drop-expected-disposition"),
    "architecting-information": ("V10 Settings-Architecture Identification", "H-SETTINGS-ARCH", "settings-flat-misc"),
    "designing-authentication-and-passkeys": ("V10 Account-Lifecycle Empirical Boundary", "H-ACCOUNT-CONTINUITY", "account-login-only"),
    "designing-editor-canvas-workspaces": ("V10 Instrument Adequacy Experiment", "H-WORKSPACE-INSTRUMENTS", "workspace-all-tools-visible"),
    "designing-desktop-windowed-workspaces": ("V10 Desktop Workspace Persistence & Zoning Evidence", "workspace-all-tools-visible"),
    "modeling-users-and-tasks": ("V10 Cross-Audience Behavioral Test", "H-DOMAIN-AUDIENCE", "domain-theme-stereotype"),
    "exploring-aesthetic-directions": ("V10 Comparative Taste Identification", "H-TASTE-COMPARATIVE", "pairwise blinded evidence"),
    "critiquing-visual-design": ("V10 Causal Render-Critique Experiment", "H-RENDER-CRITIQUE-CAUSAL", "repair effectiveness"),
    "verifying-design-fidelity": ("V10 Runtime Fidelity Attribution", "H-RENDER-FIDELITY", "artifact evidence is not efficacy evidence"),
    "designing-motion": ("V10 Semantic Motion Identification", "H-MOTION-SEMANTIC", "motion-decoration-priority"),
    "engineering-rich-interactive-components": ("V10 Temporal Runtime Realization Test", "H-MOTION-SEMANTIC"),
    "using-nolane-ui": ("V10 Generation/Evaluation Isolation", "hidden evaluator rubric", "EMPIRICAL_EVAL"),
    "nolane-ui": ("V10 Empirical Claim Lifecycle", "EMPIRICAL_TRANSFER", "STRUCTURAL_ONLY"),
    "routing-ui-work": ("V10 Empirical-Evaluation Routing", "empirical-evaluation", "ablation"),
}

REQUIRED_SOURCE_IDS = {
    "webcoderbench-acl-2026",
    "artifactsbench-2025",
    "vision2web-2026",
    "webgen-bench-2025",
    "design2code-2024",
}

REQUIRED_ADVERSARIAL_PLANES = {
    "provenance", "blindness", "pairing", "statistics", "ablation", "holdout",
    "missingness", "cost", "claims", "contamination", "placebo", "hard-blockers",
}


def _load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _nonempty_strings(value: Any, minimum: int = 1) -> bool:
    return (
        isinstance(value, list)
        and len(value) >= minimum
        and all(isinstance(x, str) and bool(x.strip()) for x in value)
    )


def extend(root: Path, base: dict[str, Any]) -> dict[str, Any]:
    root = Path(root)
    errors = list(base.get("errors", []))
    warnings = list(base.get("warnings", []))
    metrics = dict(base.get("metrics", {}))

    for rel in REQUIRED:
        if not (root / rel).is_file():
            errors.append(f"missing required v10 file: {rel}")

    # Version and preserved ownership topology.
    try:
        pyproject = (root / "pyproject.toml").read_text(encoding="utf-8")
        match = re.search(r'^version\s*=\s*"([^"]+)"', pyproject, flags=re.MULTILINE)
        if not match or match.group(1) != "0.10.0":
            errors.append("v10 package version must be 0.10.0")
        metrics["nui_major"] = 10
        graph = _load(root / "skills/skill-graph.json").get("skills", {})
        if len(graph) < 174:
            errors.append(f"v10 must retain the 174-skill historical baseline; found {len(graph)}")
        metrics["skill_count"] = len(graph)
    except Exception as exc:
        errors.append(f"v10 version/ownership plane: {exc}")
        graph = {}

    # Falsifiable hypotheses.
    hypothesis_result: dict[str, Any] = {"hypothesis_ids": []}
    try:
        hypotheses = _load(root / "knowledge/v10-behavioral-hypotheses.json")
        hypothesis_result = validate_hypothesis_registry(hypotheses)
        errors.extend(f"v10 hypothesis registry: {e}" for e in hypothesis_result.get("errors", []))
        if hypothesis_result.get("hypothesis_count", 0) < 12:
            errors.append("v10 requires at least twelve falsifiable behavioral hypotheses")
        metrics["v10_hypotheses"] = int(hypothesis_result.get("hypothesis_count", 0))
        metrics["v10_dimensions"] = len(hypothesis_result.get("dimensions", []))
    except Exception as exc:
        errors.append(f"v10 hypothesis plane: {exc}")

    # Original public/hidden corpus with strict split and cross-links.
    task_result: dict[str, Any] = {"task_ids": []}
    try:
        public = _load(root / "benchmarks/v10/tasks-public.json")
        hidden = _load(root / "benchmarks/v10/tasks-hidden.json")
        task_result = validate_task_corpus(public, hidden, hypothesis_result)
        errors.extend(f"v10 task corpus: {e}" for e in task_result.get("errors", []))
        tasks = public.get("tasks", [])
        if len(tasks) != 48:
            errors.append(f"v10 benchmark corpus must contain exactly 48 original tasks; found {len(tasks)}")
        families = {x.get("family") for x in tasks if isinstance(x, dict)}
        holdouts = [x for x in tasks if isinstance(x, dict) and x.get("split") == "holdout"]
        if len(families) != 12:
            errors.append(f"v10 benchmark corpus must contain exactly 12 task families; found {len(families)}")
        if len(holdouts) != 12:
            errors.append(f"v10 benchmark corpus must contain exactly 12 holdout tasks; found {len(holdouts)}")
        for family in families:
            family_tasks = [x for x in tasks if isinstance(x, dict) and x.get("family") == family]
            if len(family_tasks) != 4:
                errors.append(f"v10 task family {family} must contain four tasks")
            if sum(x.get("split") == "holdout" for x in family_tasks) != 1:
                errors.append(f"v10 task family {family} must contain exactly one holdout")
            if {x.get("complexity") for x in family_tasks} != {"low", "medium", "high"}:
                errors.append(f"v10 task family {family} must exercise low/medium/high complexity")
        metrics["v10_benchmark_tasks"] = len(tasks)
        metrics["v10_task_families"] = len(families)
        metrics["v10_holdout_tasks"] = len(holdouts)
    except Exception as exc:
        errors.append(f"v10 benchmark plane: {exc}")

    # Mutation/ablation sensitivity and negative controls.
    try:
        mutation_data = _load(root / "benchmarks/v10/mutations.json")
        mutation_result = validate_mutation_registry(mutation_data, hypothesis_result, task_result)
        errors.extend(f"v10 mutation registry: {e}" for e in mutation_result.get("errors", []))
        items = mutation_data.get("mutations", [])
        if len(items) < 16:
            errors.append("v10 mutation registry requires at least sixteen perturbations")
        kinds = {x.get("kind") for x in items if isinstance(x, dict)}
        if "placebo" not in kinds or not ({"semantic", "interaction"} & kinds):
            errors.append("v10 mutations require targeted semantic/interaction perturbations plus placebo controls")
        hypothesis_mutations = set(hypothesis_result.get("mutation_ids", []))
        registered = set(mutation_result.get("mutation_ids", []))
        if not hypothesis_mutations.issubset(registered):
            errors.append(f"v10 hypotheses reference unregistered mutations: {sorted(hypothesis_mutations - registered)}")
        hypothesis_ablations = set(hypothesis_result.get("ablation_ids", []))
        registered_ablations = set(mutation_result.get("ablation_ids", []))
        if not hypothesis_ablations.issubset(registered_ablations):
            errors.append(f"v10 hypotheses reference unregistered ablations: {sorted(hypothesis_ablations - registered_ablations)}")
        metrics["v10_mutations"] = len(items)
        metrics["v10_placebos"] = sum(x.get("kind") == "placebo" for x in items if isinstance(x, dict))
        metrics["v10_ablations"] = len(registered_ablations)
    except Exception as exc:
        errors.append(f"v10 mutation plane: {exc}")

    # Source-depth ledger: mechanisms + limitations, never global authority.
    try:
        ledger = _load(root / "knowledge/v10-empirical-evaluation-sources.json")
        sources = ledger.get("sources", [])
        if ledger.get("version") != 10 or len(sources) < 5:
            errors.append("v10 empirical source ledger requires version 10 and at least five primary sources")
        ids = {x.get("id") for x in sources if isinstance(x, dict)}
        if not REQUIRED_SOURCE_IDS.issubset(ids):
            errors.append(f"v10 source ledger missing required methodology anchors: {sorted(REQUIRED_SOURCE_IDS - ids)}")
        for item in sources:
            if not isinstance(item, dict):
                errors.append("v10 source entries must be objects")
                continue
            sid = item.get("id", "<unknown>")
            for field in ("primary_url", "source_type", "authority_role", "transfer_boundary", "drift_posture"):
                if not isinstance(item.get(field), str) or not item.get(field).strip():
                    errors.append(f"v10 source {sid} missing {field}")
            for field in ("inspected_mechanisms", "contraindications", "v10_uses"):
                if not _nonempty_strings(item.get(field)):
                    errors.append(f"v10 source {sid} missing deep {field}")
            if item.get("authority_role") == "global-design-authority":
                errors.append(f"v10 source {sid} illegally escalates benchmark methodology to global design authority")
        metrics["v10_empirical_sources"] = len(sources)
    except Exception as exc:
        errors.append(f"v10 empirical source plane: {exc}")

    # Skill integration: semantic anchors live on canonical owners rather than new duplicate skills.
    try:
        for skill, anchors in SKILL_ANCHORS.items():
            if skill not in graph:
                errors.append(f"v10 protocol owner missing from canonical graph: {skill}")
                continue
            path = root / "skills" / skill / "SKILL.md"
            if not path.is_file():
                errors.append(f"v10 protocol owner missing SKILL.md: {skill}")
                continue
            text = path.read_text(encoding="utf-8").lower()
            for anchor in anchors:
                if anchor.lower() not in text:
                    errors.append(f"v10 protocol anchor absent from {skill}: {anchor}")
    except Exception as exc:
        errors.append(f"v10 skill integration plane: {exc}")

    # Adversarial anti-gaming court.
    try:
        corpus = _load(root / "evals/v10-behavioral-empirical-adversarial.json")
        cases = corpus.get("cases", [])
        if corpus.get("version") != 10 or len(cases) < 48:
            errors.append("v10 adversarial corpus requires version 10 and at least 48 cases")
        ids = [x.get("id") for x in cases if isinstance(x, dict)]
        if len(ids) != len(cases) or len(ids) != len(set(ids)) or any(not x for x in ids):
            errors.append("v10 adversarial case ids must be unique and non-empty")
        if {x.get("expected_verdict") for x in cases if isinstance(x, dict)} != {"BLOCK", "ALLOW"}:
            errors.append("v10 adversarial court must contain both BLOCK and ALLOW controls")
        planes = {x.get("plane") for x in cases if isinstance(x, dict)}
        if not REQUIRED_ADVERSARIAL_PLANES.issubset(planes):
            errors.append(f"v10 adversarial court missing planes: {sorted(REQUIRED_ADVERSARIAL_PLANES - planes)}")
        for item in cases:
            if isinstance(item, dict) and not all(isinstance(item.get(k), str) and item.get(k).strip() for k in ("stimulus", "expected_failure", "detector", "rationale")):
                errors.append(f"v10 adversarial case incomplete: {item.get('id')}")
        metrics["v10_adversarial_cases"] = len(cases)
        metrics["v10_adversarial_planes"] = len(planes)
    except Exception as exc:
        errors.append(f"v10 adversarial plane: {exc}")

    # Schemas/protocols must be JSON-valid and clearly bounded.
    try:
        for rel in ("schemas/v10-experiment.schema.json", "schemas/v10-run-record.schema.json", "schemas/v10-claim.schema.json"):
            schema = _load(root / rel)
            if schema.get("type") != "object" or not schema.get("required"):
                errors.append(f"v10 schema lacks typed object contract: {rel}")
        protocol = (root / "docs/V10-EMPIRICAL-RUN-PROTOCOL.md").read_text(encoding="utf-8")
        for phrase in ("artifact quality ≠ NUI efficacy", "hidden evaluator", "EMPIRICAL_TRANSFER", "Failures, timeouts"):
            if phrase.lower() not in protocol.lower():
                errors.append(f"v10 empirical protocol missing invariant: {phrase}")
        for rel in ("scripts/nui-v10-build-run-matrix", "scripts/nui-v10-validate-run-bundle", "scripts/nui-v10-aggregate"):
            text = (root / rel).read_text(encoding="utf-8")
            if "json" not in text.lower() or "v10" not in text.lower():
                errors.append(f"v10 CLI protocol incomplete: {rel}")
    except Exception as exc:
        errors.append(f"v10 protocol/schema plane: {exc}")

    # Ordinary repository verification may only certify the framework.
    metrics["v10_claim_ceiling"] = "STRUCTURAL_ONLY"

    return {"valid": not errors, "errors": errors, "warnings": warnings, "metrics": metrics}


__all__ = ["extend"]
