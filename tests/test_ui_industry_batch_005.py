import difflib
import json
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
GRAPH_PATH = SKILLS_DIR / "skill-graph.json"

COURTS = {
    "design-system": [
        "governing-design-system-evolution",
        "designing-token-taxonomies",
        "designing-semantic-token-aliasing",
        "designing-token-mode-architecture",
        "designing-theme-inheritance",
        "designing-multi-brand-theming",
        "designing-density-token-systems",
        "designing-motion-token-systems",
        "designing-component-token-scopes",
        "designing-token-deprecation-migrations",
        "designing-design-system-versioning",
        "designing-component-api-governance",
        "designing-composition-boundaries",
        "designing-slot-and-part-contracts",
        "designing-variant-prop-taxonomies",
        "designing-design-system-contribution-workflows",
        "designing-design-system-documentation-portals",
        "designing-design-system-adoption-migrations",
        "measuring-design-system-adoption",
        "designing-cross-platform-component-parity",
    ],
    "responsive": [
        "engineering-responsive-composition",
        "designing-container-query-layouts",
        "designing-content-driven-breakpoints",
        "designing-responsive-region-reordering",
        "designing-responsive-priority-collapse",
        "designing-responsive-density-shifts",
        "designing-responsive-navigation-transitions",
        "designing-responsive-table-transformations",
        "designing-responsive-toolbar-overflow",
        "designing-responsive-form-layouts",
        "designing-responsive-dialog-sizing",
        "designing-responsive-panel-docking",
        "designing-responsive-sidebar-behavior",
        "designing-responsive-canvas-workspaces",
        "designing-responsive-dashboard-grids",
        "designing-responsive-media-crops",
        "designing-responsive-empty-states",
        "designing-responsive-error-recovery",
        "designing-responsive-loading-skeletons",
        "verifying-responsive-state-parity",
    ],
    "typography": [
        "engineering-typographic-systems",
        "designing-type-scale-relationships",
        "designing-line-length-and-measure",
        "designing-line-height-rhythm",
        "designing-paragraph-spacing",
        "designing-heading-hierarchy",
        "designing-optical-heading-balance",
        "designing-rag-and-line-break-quality",
        "designing-widow-and-orphan-control",
        "designing-hyphenation-behavior",
        "designing-text-truncation",
        "designing-multiline-labels",
        "designing-tabular-numerals",
        "designing-decimal-alignment",
        "designing-numeric-comparison-typography",
        "designing-code-typography",
        "designing-variable-font-controls",
        "designing-font-loading-fallback-behavior",
        "designing-legal-and-disclosure-typography",
        "verifying-typography-under-zoom",
    ],
    "agent": [
        "designing-agentic-interaction-systems",
        "designing-agent-plan-previews",
        "designing-agent-action-confirmations",
        "designing-agent-permission-escalation",
        "designing-agent-tool-selection-visibility",
        "designing-agent-action-progress",
        "designing-agent-interruption-and-cancel",
        "designing-agent-retry-and-recovery",
        "designing-agent-partial-completion",
        "designing-agent-uncertainty-disclosure",
        "designing-agent-confidence-calibration",
        "designing-agent-memory-controls",
        "designing-agent-context-inspection",
        "designing-agent-context-editing",
        "designing-agent-delegation-handoffs",
        "designing-multi-agent-coordination-views",
        "designing-agent-background-task-surfaces",
        "designing-agent-result-provenance",
        "designing-agent-side-effect-review",
        "designing-agent-reversible-actions",
    ],
    "evidence": [
        "engineering-ui-evidence-workflows",
        "designing-ui-research-repositories",
        "designing-research-question-framing",
        "designing-usability-test-protocols",
        "designing-task-success-measures",
        "designing-behavioral-observation-capture",
        "designing-interview-note-synthesis",
        "designing-affinity-analysis-workflows",
        "designing-journey-evidence-maps",
        "designing-prototype-test-fidelity",
        "designing-a-b-test-interpretation",
        "designing-experiment-guardrail-metrics",
        "designing-qualitative-quantitative-triangulation",
        "designing-design-hypothesis-ledgers",
        "designing-ui-regression-evidence",
        "designing-visual-diff-review",
        "designing-interaction-fidelity-audits",
        "designing-content-fidelity-audits",
        "designing-accessibility-evidence-packages",
        "designing-design-decision-records",
    ],
}

COURT_META = {
    "design-system": ("design-system-evolution", "design-system-specialist", "governing-design-systems"),
    "responsive": ("responsive-composition", "responsive-specialist", "adapting-responsive-layouts"),
    "typography": ("typographic-system", "typography-specialist", "crafting-typography"),
    "agent": ("agentic-interaction", "agentic-interaction-specialist", "designing-agent-autonomy-and-control"),
    "evidence": ("ui-evidence", "ui-evidence-specialist", "challenging-ui-designs"),
}


def _output_for(slug: str) -> str:
    prefixes = ("designing-", "engineering-", "governing-", "measuring-", "verifying-")
    stem = slug
    for prefix in prefixes:
        if stem.startswith(prefix):
            stem = stem.removeprefix(prefix)
            break
    return stem + "-contract"


def _records():
    records = []
    for court, slugs in COURTS.items():
        root_family, child_family, root_parent = COURT_META[court]
        root = slugs[0]
        for index, slug in enumerate(slugs):
            records.append(
                {
                    "slug": slug,
                    "court": court,
                    "family": root_family if index == 0 else child_family,
                    "parent": root_parent if index == 0 else root,
                    "output": _output_for(slug),
                }
            )
    return records


BATCH_005 = _records()
SLUGS = [record["slug"] for record in BATCH_005]
EXPECTED = {record["slug"]: record for record in BATCH_005}


def _normalized_body(text: str) -> str:
    text = re.sub(r"^---.*?---\s*", "", text, flags=re.DOTALL)
    text = re.sub(r"^#.*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"(?:designing|engineering|governing|measuring|verifying)-[a-z0-9-]+", "<skill>", text.lower())
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return " ".join(text.split())


class UIIndustryBatch005Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph = json.loads(GRAPH_PATH.read_text(encoding="utf-8"))
        cls.graph_skills = cls.graph["skills"]

    def test_batch_has_exactly_one_hundred_unique_slugs(self):
        self.assertEqual(100, len(BATCH_005))
        self.assertEqual(100, len(set(SLUGS)))

    def test_each_court_has_exactly_twenty_skills(self):
        counts = Counter(record["court"] for record in BATCH_005)
        self.assertEqual(set(COURTS), set(counts))
        self.assertEqual({20}, set(counts.values()))

    def test_batch_slugs_do_not_preexist_as_prior_graph_nodes(self):
        # Before implementation this is the intentional red-state guard. After graph
        # insertion, all Batch 005 nodes must be present and the exact metadata tests
        # below become authoritative.
        prior_count = len(self.graph_skills)
        if prior_count == 674:
            collisions = sorted(set(SLUGS) & set(self.graph_skills))
            self.assertEqual([], collisions)

    def test_each_skill_exists_and_frontmatter_name_matches_slug(self):
        for slug in SLUGS:
            path = SKILLS_DIR / slug / "SKILL.md"
            self.assertTrue(path.is_file(), slug)
            text = path.read_text(encoding="utf-8")
            match = re.match(r"^---\nname:\s*([^\n]+)\n", text)
            self.assertIsNotNone(match, slug)
            self.assertEqual(slug, match.group(1).strip())

    def test_each_skill_has_required_behavioral_sections_and_depth(self):
        sections = (
            "## Decision ownership",
            "## Inputs and evidence",
            "## Procedure",
            "## Failure topology",
            "## Falsification",
            "## Output contract",
            "## Handoffs",
        )
        for slug in SLUGS:
            path = SKILLS_DIR / slug / "SKILL.md"
            self.assertTrue(path.is_file(), slug)
            text = path.read_text(encoding="utf-8")
            self.assertGreaterEqual(len(text), 2200, slug)
            for section in sections:
                self.assertIn(section, text, f"{slug}: missing {section}")

    def test_each_skill_is_registered_with_exact_locked_metadata(self):
        for slug, expected in EXPECTED.items():
            self.assertIn(slug, self.graph_skills)
            node = self.graph_skills[slug]
            self.assertEqual(expected["family"], node.get("family"), slug)
            self.assertEqual(expected["parent"], node.get("parent"), slug)
            self.assertEqual(expected["output"], node.get("output"), slug)

    def test_batch_outputs_are_unique_and_do_not_collide_with_prior_graph(self):
        outputs = [record["output"] for record in BATCH_005]
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

    def test_final_graph_count_is_exactly_774(self):
        self.assertEqual(774, len(self.graph_skills))

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
        for i, left in enumerate(SLUGS):
            for right in SLUGS[i + 1 :]:
                ratio = difflib.SequenceMatcher(None, bodies[left], bodies[right]).ratio()
                self.assertLess(ratio, 0.92, f"trivial rename risk: {left} / {right}: {ratio:.3f}")


if __name__ == "__main__":
    unittest.main()
