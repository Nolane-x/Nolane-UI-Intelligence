import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
GRAPH_PATH = SKILLS_DIR / "skill-graph.json"

BATCH_001 = [
    "designing-press-feedback-motion",
    "designing-hover-response-motion",
    "designing-focus-transition-motion",
    "designing-toggle-state-motion",
    "designing-menu-entry-exit-motion",
    "designing-popover-origin-motion",
    "designing-modal-presentation-motion",
    "designing-drawer-and-sheet-motion",
    "designing-accordion-expansion-motion",
    "designing-tab-transition-motion",
    "designing-list-insertion-removal-motion",
    "designing-layout-reflow-motion",
    "designing-shared-element-continuity",
    "designing-drag-inertia-and-snap",
    "designing-scroll-linked-motion",
    "designing-staggered-reveal-motion",
    "designing-numeric-change-motion",
    "designing-data-update-motion",
    "designing-animation-interruption-and-retargeting",
    "designing-motion-performance-fallbacks",
    "designing-command-palettes",
    "designing-comboboxes-and-autocomplete",
    "designing-multiselect-token-inputs",
    "designing-cascading-menus",
    "designing-context-menus",
    "designing-tooltip-systems",
    "designing-popover-systems",
    "designing-dialog-systems",
    "designing-drawer-and-sheet-components",
    "designing-tree-views",
    "designing-split-pane-layouts",
    "designing-resizable-panels",
    "designing-docking-workspaces",
    "designing-property-inspectors",
    "designing-bulk-action-toolbars",
    "designing-inline-editing",
    "designing-editable-data-grids",
    "designing-date-time-pickers",
    "designing-file-uploaders",
    "designing-search-filter-builders",
    "designing-multi-selection-models",
    "designing-range-selection",
    "designing-marquee-and-lasso-selection",
    "designing-drag-reordering",
    "designing-resize-handles",
    "designing-transform-gizmos",
    "designing-snapping-and-guides",
    "designing-pan-zoom-navigation",
    "designing-object-grouping-and-locking",
    "designing-undo-redo-history",
    "designing-spreadsheet-interfaces",
    "designing-cell-editing",
    "designing-formula-authoring",
    "designing-frozen-panes",
    "designing-column-pinning",
    "designing-table-sorting",
    "designing-table-filtering",
    "designing-table-grouping",
    "designing-tree-grids",
    "designing-virtualized-grids",
    "designing-pivot-table-interfaces",
    "designing-dashboard-drilldown",
    "designing-cross-filtering",
    "designing-time-series-exploration",
    "designing-uncertainty-visualization",
    "designing-operational-inboxes",
    "designing-work-queues",
    "designing-triage-surfaces",
    "designing-approval-workflows",
    "designing-multi-stage-approval",
    "designing-case-management",
    "designing-assignment-and-ownership",
    "designing-escalation-workflows",
    "designing-sla-aware-interfaces",
    "designing-audit-log-interfaces",
    "designing-role-management",
    "designing-rbac-matrices",
    "designing-policy-inheritance",
    "designing-organization-administration",
    "designing-bulk-administration",
    "designing-subscription-management",
    "designing-pricing-plan-comparison",
    "designing-usage-metering",
    "designing-quota-and-limit-ux",
    "designing-payment-failure-recovery",
    "designing-invoice-history",
    "designing-calendar-interfaces",
    "designing-time-slot-selection",
    "designing-timezone-aware-scheduling",
    "designing-recurring-events",
    "designing-resource-booking",
    "designing-scheduling-conflicts",
    "designing-geospatial-interfaces",
    "designing-map-marker-clustering",
    "designing-map-layer-management",
    "designing-map-list-coordination",
    "designing-route-comparison",
    "designing-version-history",
    "designing-diff-interfaces",
    "designing-conflict-resolution",
]


class UIIndustryBatch001Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph = json.loads(GRAPH_PATH.read_text(encoding="utf-8"))
        cls.graph_skills = cls.graph["skills"]

    def test_batch_has_exactly_one_hundred_unique_slugs(self):
        self.assertEqual(100, len(BATCH_001))
        self.assertEqual(100, len(set(BATCH_001)))
        self.assertGreaterEqual(len(self.graph_skills), 274)

    def test_each_skill_exists_and_frontmatter_name_matches_slug(self):
        for slug in BATCH_001:
            path = SKILLS_DIR / slug / "SKILL.md"
            self.assertTrue(path.is_file(), slug)
            text = path.read_text(encoding="utf-8")
            match = re.match(r"^---\nname:\s*([^\n]+)\n", text)
            self.assertIsNotNone(match, slug)
            self.assertEqual(slug, match.group(1).strip())

    def test_each_skill_has_substantive_decision_and_failure_content(self):
        required_signals = ("Decision", "Failure", "Falsif", "Output")
        for slug in BATCH_001:
            text = (SKILLS_DIR / slug / "SKILL.md").read_text(encoding="utf-8")
            self.assertGreaterEqual(len(text), 1800, slug)
            for signal in required_signals:
                self.assertIn(signal, text, f"{slug}: missing {signal}")

    def test_each_skill_is_registered_in_graph(self):
        for slug in BATCH_001:
            self.assertIn(slug, self.graph_skills)
            node = self.graph_skills[slug]
            self.assertIn("family", node, slug)
            self.assertIn("parent", node, slug)
            self.assertIn("output", node, slug)
            self.assertIn(node["parent"], self.graph_skills, slug)

    def test_batch_has_no_self_parent_or_duplicate_output(self):
        outputs = []
        for slug in BATCH_001:
            node = self.graph_skills[slug]
            self.assertNotEqual(slug, node["parent"])
            outputs.append(node["output"])
        self.assertEqual(len(outputs), len(set(outputs)))

    def test_parent_chain_reaches_nui_root(self):
        for slug in BATCH_001:
            seen = set()
            current = slug
            while current is not None:
                self.assertNotIn(current, seen, f"cycle from {slug}")
                seen.add(current)
                current = self.graph_skills[current]["parent"]
            self.assertIn("using-nolane-ui", seen, slug)


if __name__ == "__main__":
    unittest.main()
