import difflib
import json
import re
import unittest
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
GRAPH_PATH = SKILLS_DIR / "skill-graph.json"
PROVENANCE_PATH = ROOT / "docs" / "research" / "UI-INDUSTRY-1000-BATCH-006.md"

COURTS = {
    "design-system-governance": [
        "governing-token-resolution-contexts",
        "governing-token-reference-integrity",
        "governing-token-type-conformance",
        "governing-token-extension-boundaries",
        "governing-token-mode-inheritance",
        "governing-semantic-token-layering",
        "auditing-token-migration-impact",
        "governing-token-deprecation-lifecycles",
        "governing-design-system-version-compatibility",
        "governing-component-anatomy-contracts",
        "governing-component-slot-contracts",
        "governing-component-state-contracts",
        "governing-component-variant-taxonomies",
        "governing-design-system-exceptions",
        "governing-design-system-contribution-workflows",
        "governing-cross-platform-component-parity",
        "governing-design-system-adoption-migrations",
        "governing-design-system-breaking-change-rollouts",
    ],
    "adaptive-composition": [
        "designing-container-query-composition",
        "designing-content-pressure-breakpoints",
        "designing-region-priority-collapse",
        "designing-responsive-region-reordering",
        "designing-adaptive-navigation-mode-transitions",
        "designing-responsive-toolbar-overflow",
        "designing-responsive-table-mode-transitions",
        "designing-responsive-form-reflow",
        "designing-pointer-to-touch-density-transitions",
        "designing-hover-to-nonhover-affordance-transitions",
        "designing-foldable-hinge-aware-layouts",
        "preserving-responsive-state-continuity",
    ],
    "typography-engineering": [
        "engineering-webfont-loading-transitions",
        "engineering-font-fallback-metric-compatibility",
        "designing-variable-font-axis-behavior",
        "engineering-font-subsetting-and-glyph-coverage",
        "designing-readable-line-measure",
        "designing-line-breaking-and-hyphenation",
        "designing-truncation-and-overflow-truth",
        "designing-numeric-tabular-alignment",
        "designing-decimal-and-financial-type-alignment",
        "designing-code-and-monospace-typography",
        "designing-mixed-font-baseline-alignment",
        "diagnosing-runtime-text-rendering-drift",
    ],
    "agentic-execution": [
        "designing-agent-shared-state-reconciliation",
        "designing-agent-tool-call-lifecycles",
        "designing-tool-result-presentation-lifecycles",
        "designing-agent-plan-preview-surfaces",
        "designing-agent-approval-scope-boundaries",
        "detecting-agent-approval-scope-drift",
        "designing-agent-interruption-and-resume",
        "designing-agent-partial-completion-recovery",
        "designing-agent-retry-and-replay-controls",
        "designing-agent-run-branching",
        "designing-agent-side-effect-ledgers",
        "designing-agent-reversible-action-surfaces",
        "designing-agent-background-run-surfaces",
        "designing-agent-tool-permission-escalation",
        "designing-agent-generated-component-authority",
        "designing-generative-ui-schema-fallbacks",
        "designing-human-correction-of-agent-state",
        "designing-multi-agent-handoff-visibility",
    ],
    "ui-evidence": [
        "designing-component-state-evidence-matrices",
        "designing-interaction-regression-evidence",
        "designing-visual-regression-baselines",
        "designing-responsive-regression-matrices",
        "designing-browser-and-device-evidence-matrices",
        "designing-accessibility-evidence-packets",
        "designing-manual-review-evidence-contracts",
        "detecting-rendered-environment-drift",
        "designing-design-system-consumer-regression-tests",
        "designing-story-state-fixture-coverage",
        "triaging-visual-diff-noise",
        "governing-regression-baseline-updates",
    ],
    "game-ten-foot": [
        "designing-directional-focus-graphs",
        "designing-remote-control-navigation",
        "designing-controller-disconnect-recovery",
        "designing-input-device-prompt-switching",
        "designing-controller-remapping-surfaces",
        "designing-multiplayer-ui-focus-ownership",
        "designing-ten-foot-readable-density",
        "designing-game-hud-information-priority",
        "designing-pause-and-game-state-overlays",
        "designing-split-screen-safe-interface-regions",
        "designing-game-menu-stack-recovery",
        "designing-gameplay-to-menu-input-handoffs",
    ],
    "automotive-hmi": [
        "designing-driving-state-interaction-lockouts",
        "designing-vehicle-warning-priority-surfaces",
        "designing-driver-distraction-aware-information-density",
        "designing-rotary-controller-focus-navigation",
        "designing-instrument-cluster-information-priority",
        "designing-driver-passenger-authority-splits",
        "designing-vehicle-state-dependent-controls",
        "designing-automotive-modality-fallbacks",
    ],
    "multi-surface-continuity": [
        "designing-cross-device-session-handoffs",
        "designing-companion-surface-authority",
        "designing-second-screen-control-continuity",
        "designing-notification-to-app-continuation",
        "designing-cross-device-capability-negotiation",
        "preserving-task-state-across-device-switches",
        "resolving-cross-device-state-conflicts",
        "designing-device-proximity-handoff-cues",
    ],
}

EXPECTED_COUNTS = {
    "design-system-governance": 18,
    "adaptive-composition": 12,
    "typography-engineering": 12,
    "agentic-execution": 18,
    "ui-evidence": 12,
    "game-ten-foot": 12,
    "automotive-hmi": 8,
    "multi-surface-continuity": 8,
}

TOKEN_SLUGS = set(COURTS["design-system-governance"][:8])
COMPONENT_CONTRACT_SLUGS = set(COURTS["design-system-governance"][9:13])
HUMAN_AI_SLUGS = {
    "designing-agent-shared-state-reconciliation",
    "designing-agent-tool-call-lifecycles",
    "designing-human-correction-of-agent-state",
}
GENERATIVE_UI_SLUGS = {
    "designing-tool-result-presentation-lifecycles",
    "designing-agent-generated-component-authority",
    "designing-generative-ui-schema-fallbacks",
}
MULTI_AGENT_SLUGS = {"designing-multi-agent-handoff-visibility"}


def _output_for(slug: str) -> str:
    for prefix in (
        "designing-",
        "engineering-",
        "governing-",
        "auditing-",
        "detecting-",
        "diagnosing-",
        "preserving-",
        "resolving-",
        "triaging-",
    ):
        if slug.startswith(prefix):
            return slug.removeprefix(prefix) + "-contract"
    return slug + "-contract"


def _metadata(court: str, slug: str):
    if court == "design-system-governance":
        if slug in TOKEN_SLUGS:
            return "design-token-governance-specialist", "architecting-design-tokens"
        if slug in COMPONENT_CONTRACT_SLUGS:
            return "component-contract-governance-specialist", "architecting-component-systems"
        return "design-system-governance-specialist", "architecting-component-systems"
    if court == "adaptive-composition":
        return "adaptive-composition-specialist", "adapting-responsive-layouts"
    if court == "typography-engineering":
        return "typography-engineering-specialist", "crafting-typography"
    if court == "agentic-execution":
        if slug in HUMAN_AI_SLUGS:
            return "human-ai-execution-specialist", "designing-human-ai-interaction"
        if slug in GENERATIVE_UI_SLUGS:
            return "generative-ui-execution-specialist", "designing-generative-ui"
        if slug in MULTI_AGENT_SLUGS:
            return "multi-agent-handoff-specialist", "designing-multi-agent-surfaces"
        return "agent-autonomy-execution-specialist", "designing-agent-autonomy-and-control"
    if court == "ui-evidence":
        return "ui-evidence-specialist", "binding-ui-evidence"
    if court == "game-ten-foot":
        return "game-interface-specialist", "routing-ui-work"
    if court == "automotive-hmi":
        return "automotive-hmi-specialist", "designing-high-stakes-decisions"
    if court == "multi-surface-continuity":
        return "multi-surface-continuity-specialist", "routing-ui-work"
    raise AssertionError(court)


def _records():
    records = []
    for court, slugs in COURTS.items():
        for slug in slugs:
            family, parent = _metadata(court, slug)
            records.append(
                {
                    "slug": slug,
                    "court": court,
                    "family": family,
                    "parent": parent,
                    "output": _output_for(slug),
                }
            )
    return records


BATCH_006 = _records()
SLUGS = [record["slug"] for record in BATCH_006]
EXPECTED = {record["slug"]: record for record in BATCH_006}


def _normalized_body(text: str) -> str:
    text = re.sub(r"^---.*?---\s*", "", text, flags=re.DOTALL)
    text = re.sub(r"^#{1,6}.*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"(?:designing|engineering|governing|auditing|detecting|diagnosing|preserving|resolving|triaging)-[a-z0-9-]+", "<skill>", text.lower())
    text = re.sub(r"`[^`]+`", "<token>", text)
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return " ".join(text.split())


def _substantive_paragraphs(text: str):
    text = re.sub(r"^---.*?---\s*", "", text, flags=re.DOTALL)
    paragraphs = []
    for paragraph in re.split(r"\n\s*\n", text):
        p = " ".join(paragraph.split())
        if p.startswith("#") or len(p) < 140:
            continue
        p = re.sub(r"(?:designing|engineering|governing|auditing|detecting|diagnosing|preserving|resolving|triaging)-[a-z0-9-]+", "<skill>", p.lower())
        paragraphs.append(p)
    return paragraphs


def _section_skeleton(text: str):
    return tuple(
        re.sub(r"[^a-z0-9]+", "-", heading.lower()).strip("-")
        for heading in re.findall(r"^##+\s+(.+)$", text, flags=re.MULTILINE)
    )


def _has_decision_ownership(text: str) -> bool:
    lowered = text.lower()
    return bool(
        re.search(r"\bdecision(?:s)?\b|\bdecid(?:e|es|ed|ing)\b", lowered)
        or re.search(r"\bthis skill owns\b|\bowns the\b", lowered)
    )


class UIIndustryBatch006Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph = json.loads(GRAPH_PATH.read_text(encoding="utf-8"))
        cls.graph_skills = cls.graph["skills"]

    def test_batch_has_exactly_one_hundred_unique_slugs(self):
        self.assertEqual(100, len(BATCH_006))
        self.assertEqual(100, len(set(SLUGS)))

    def test_court_counts_are_explicit_and_exact(self):
        counts = Counter(record["court"] for record in BATCH_006)
        self.assertEqual(EXPECTED_COUNTS, dict(counts))

    def test_each_skill_exists_and_frontmatter_name_matches_slug(self):
        for slug in SLUGS:
            path = SKILLS_DIR / slug / "SKILL.md"
            self.assertTrue(path.is_file(), slug)
            text = path.read_text(encoding="utf-8")
            match = re.match(r"^---\nname:\s*([^\n]+)\n", text)
            self.assertIsNotNone(match, slug)
            self.assertEqual(slug, match.group(1).strip())

    def test_each_skill_has_independent_cognitive_contract(self):
        required_concepts = (
            "Evidence",
            "Failure",
            "Falsification",
            "Recovery",
            "Output",
            "Handoff",
            "Sibling",
        )
        violations = []
        for slug in SLUGS:
            path = SKILLS_DIR / slug / "SKILL.md"
            self.assertTrue(path.is_file(), slug)
            text = path.read_text(encoding="utf-8")
            if len(text) < 2800:
                violations.append(f"{slug}: length {len(text)} < 2800")
            if not _has_decision_ownership(text):
                violations.append(f"{slug}: missing decision ownership semantics")
            lowered = text.lower()
            for concept in required_concepts:
                if concept.lower() not in lowered:
                    violations.append(f"{slug}: missing {concept}")
            if "delete-the-skill" not in lowered:
                violations.append(f"{slug}: missing delete-the-skill rationale")
        self.assertEqual([], violations, "\n" + "\n".join(violations))

    def test_each_skill_is_registered_with_locked_metadata(self):
        for slug, expected in EXPECTED.items():
            self.assertIn(slug, self.graph_skills)
            node = self.graph_skills[slug]
            self.assertEqual(expected["family"], node.get("family"), slug)
            self.assertEqual(expected["parent"], node.get("parent"), slug)
            self.assertEqual(expected["output"], node.get("output"), slug)

    def test_outputs_are_unique_and_do_not_collide_with_prior_graph(self):
        outputs = [record["output"] for record in BATCH_006]
        self.assertEqual(len(outputs), len(set(outputs)))
        prior_outputs = {
            node.get("output")
            for slug, node in self.graph_skills.items()
            if slug not in SLUGS and isinstance(node, dict)
        }
        self.assertFalse(set(outputs) & prior_outputs)

    def test_parent_chain_reaches_nui_root_without_cycles(self):
        for slug in SLUGS:
            self.assertIn(slug, self.graph_skills)
            seen = set()
            current = slug
            while current is not None:
                self.assertNotIn(current, seen, f"cycle from {slug}")
                seen.add(current)
                self.assertIn(current, self.graph_skills, f"missing graph node from {slug}: {current}")
                current = self.graph_skills[current]["parent"]
            self.assertIn("using-nolane-ui", seen, slug)

    def test_final_graph_count_is_exactly_874(self):
        self.assertEqual(874, len(self.graph_skills))

    def test_provenance_ledger_covers_every_admitted_slug_and_decision_boundary(self):
        self.assertTrue(PROVENANCE_PATH.is_file())
        text = PROVENANCE_PATH.read_text(encoding="utf-8")
        for slug in SLUGS:
            self.assertIn(f"### `{slug}`", text, slug)
        for field in (
            "Parent:",
            "Trigger:",
            "Decision owned:",
            "Sibling exclusion:",
            "Failure class:",
            "Falsifier:",
            "Output:",
            "Evidence role:",
            "Delete-the-skill:",
        ):
            self.assertGreaterEqual(text.count(field), 100, field)

    def test_no_exact_normalized_body_duplicates(self):
        seen = {}
        for slug in SLUGS:
            path = SKILLS_DIR / slug / "SKILL.md"
            self.assertTrue(path.is_file(), slug)
            norm = _normalized_body(path.read_text(encoding="utf-8"))
            self.assertNotIn(norm, seen, f"{slug} duplicates {seen.get(norm)}")
            seen[norm] = slug

    def test_no_pair_is_a_trivial_rename(self):
        bodies = {}
        for slug in SLUGS:
            path = SKILLS_DIR / slug / "SKILL.md"
            self.assertTrue(path.is_file(), slug)
            bodies[slug] = _normalized_body(path.read_text(encoding="utf-8"))
        slugs = list(bodies)
        for index, left in enumerate(slugs):
            for right in slugs[index + 1 :]:
                ratio = difflib.SequenceMatcher(
                    None,
                    bodies[left].split(),
                    bodies[right].split(),
                    autojunk=False,
                ).ratio()
                self.assertLess(ratio, 0.84, f"trivial rename risk: {left} vs {right} = {ratio:.3f}")

    def test_no_long_substantive_paragraph_is_mass_reused(self):
        owners = defaultdict(set)
        for slug in SLUGS:
            path = SKILLS_DIR / slug / "SKILL.md"
            for paragraph in set(_substantive_paragraphs(path.read_text(encoding="utf-8"))):
                owners[paragraph].add(slug)
        repeated = {paragraph: slugs for paragraph, slugs in owners.items() if len(slugs) >= 3}
        self.assertFalse(repeated, f"mass-reused substantive paragraphs: {repeated}")

    def test_section_skeletons_are_not_mass_cloned(self):
        owners = defaultdict(set)
        for slug in SLUGS:
            path = SKILLS_DIR / slug / "SKILL.md"
            skeleton = _section_skeleton(path.read_text(encoding="utf-8"))
            owners[skeleton].add(slug)
        repeated = {
            skeleton: slugs
            for skeleton, slugs in owners.items()
            if skeleton and len(slugs) >= 12
        }
        self.assertFalse(repeated, f"mass-cloned section skeletons: {repeated}")

    def test_no_batch006_skill_prose_generator_was_added(self):
        suspicious = []
        for path in (ROOT / "scripts").glob("**/*"):
            if not path.is_file():
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            lowered = text.lower()
            if "batch-006" in lowered and "skill.md" in lowered and any(
                marker in lowered for marker in ("write_text", "open(", "create_file", "template")
            ):
                suspicious.append(str(path.relative_to(ROOT)))
        self.assertEqual([], suspicious)


if __name__ == "__main__":
    unittest.main()
