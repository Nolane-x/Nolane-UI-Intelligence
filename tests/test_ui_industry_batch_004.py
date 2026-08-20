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
    "diagram": [
        "designing-diagramming-and-node-graph-editors",
        "designing-node-creation-and-placement",
        "designing-port-and-connector-authoring",
        "designing-edge-routing-and-bendpoints",
        "designing-graph-auto-layout-controls",
        "designing-subgraph-and-container-models",
        "designing-swimlane-diagrams",
        "designing-mind-map-interfaces",
        "designing-flowchart-semantics",
        "designing-uml-and-modeling-diagrams",
        "designing-dependency-graph-exploration",
        "designing-topology-map-interfaces",
        "designing-graph-search-and-navigation",
        "designing-graph-minimap-overviews",
        "designing-large-graph-virtualization",
        "designing-graph-validation-and-errors",
        "designing-graph-diff-and-history",
        "designing-collaborative-diagram-editing",
        "designing-diagram-export-and-presentation",
        "designing-executable-graph-debug-overlays",
    ],
    "project": [
        "designing-project-and-work-management",
        "designing-kanban-boards",
        "designing-backlog-grooming",
        "designing-sprint-planning",
        "designing-roadmap-timelines",
        "designing-milestone-tracking",
        "designing-task-dependency-networks",
        "designing-task-hierarchy-and-subtasks",
        "designing-workload-capacity-balancing",
        "designing-work-item-status-transitions",
        "designing-recurring-work-items",
        "designing-project-templates",
        "designing-bulk-work-item-editing",
        "designing-project-views-and-filters",
        "designing-project-health-dashboards",
        "designing-time-tracking-workflows",
        "designing-effort-estimation",
        "designing-blocker-and-risk-registers",
        "designing-portfolio-rollups",
        "designing-project-closure-and-archival",
    ],
    "incident": [
        "designing-incident-response-operations",
        "designing-alert-triage-workspaces",
        "designing-incident-severity-declaration",
        "designing-incident-timeline-capture",
        "designing-responder-role-assignment",
        "designing-war-room-collaboration",
        "designing-runbook-execution",
        "designing-service-health-overviews",
        "designing-dependency-impact-analysis",
        "designing-incident-escalation-controls",
        "designing-stakeholder-incident-communications",
        "designing-status-page-authoring",
        "designing-on-call-handoffs",
        "designing-incident-command-controls",
        "designing-mitigation-action-tracking",
        "designing-incident-hypothesis-evidence-logs",
        "designing-postmortem-authoring",
        "designing-postmortem-action-followup",
        "designing-maintenance-window-operations",
        "designing-reliability-experiment-guardrails",
    ],
    "delivery": [
        "designing-software-delivery-pipelines",
        "designing-pipeline-stage-visualization",
        "designing-build-status-and-artifacts",
        "designing-ci-job-log-navigation",
        "designing-release-approval-gates",
        "designing-deployment-target-selection",
        "designing-canary-rollouts",
        "designing-blue-green-rollouts",
        "designing-progressive-delivery-controls",
        "designing-deployment-rollback",
        "designing-artifact-promotion",
        "designing-release-note-workflows",
        "designing-environment-diff-interfaces",
        "designing-configuration-drift-review",
        "designing-deployment-locks",
        "designing-release-train-coordination",
        "designing-change-freeze-controls",
        "designing-preview-environment-lifecycle",
        "designing-software-supply-chain-provenance",
        "designing-deployment-failure-diagnosis",
    ],
    "instrumentation": [
        "designing-scientific-and-engineering-instrumentation",
        "designing-instrument-telemetry-dashboards",
        "designing-experiment-setup-workflows",
        "designing-experiment-run-control",
        "designing-instrument-calibration-workflows",
        "designing-live-signal-monitoring",
        "designing-signal-waveform-analysis",
        "designing-spectrum-analysis-interfaces",
        "designing-microscopy-measurement-workflows",
        "designing-sample-tracking-interfaces",
        "designing-microplate-layout-interfaces",
        "designing-batch-and-lot-traceability",
        "designing-process-control-trend-views",
        "designing-instrument-alarm-thresholds",
        "designing-setpoint-control-interfaces",
        "designing-experimental-provenance-capture",
        "designing-experiment-comparison",
        "designing-parameter-sweep-interfaces",
        "designing-model-fitting-controls",
        "designing-safety-interlock-interfaces",
    ],
    "cad": [
        "designing-3d-cad-authoring-workspaces",
        "designing-3d-scene-hierarchies",
        "designing-3d-viewport-navigation",
        "designing-camera-view-management",
        "designing-3d-grid-and-snapping",
        "designing-3d-layer-and-collection-management",
        "designing-mesh-selection-modes",
        "designing-extrusion-and-inset-operations",
        "designing-boolean-modeling-operations",
        "designing-dimensional-measurement-tools",
        "designing-parametric-constraint-editing",
        "designing-assembly-hierarchies",
        "designing-material-assignment-workflows",
        "designing-lighting-authoring-controls",
        "designing-uv-and-texture-mapping",
        "designing-3d-annotation-and-markup",
        "designing-section-and-cut-planes",
        "designing-clash-and-collision-inspection",
        "designing-render-preview-workflows",
        "designing-manufacturing-and-export-handoff",
    ],
    "media-editing": [
        "designing-nonlinear-media-editors",
        "designing-media-ingest-and-bins",
        "designing-editing-timelines",
        "designing-track-and-layer-management",
        "designing-clip-trimming",
        "designing-split-and-razor-editing",
        "designing-ripple-roll-slip-slide-edits",
        "designing-timeline-snapping",
        "designing-transition-authoring",
        "designing-keyframe-animation-editing",
        "designing-multicamera-editing",
        "designing-audio-mixing-workspaces",
        "designing-audio-automation-curves",
        "designing-color-grading-controls",
        "designing-video-scope-interfaces",
        "designing-subtitle-authoring-workflows",
        "designing-media-relink-and-recovery",
        "designing-proxy-media-workflows",
        "designing-edit-markers-and-review-notes",
        "designing-render-and-export-queues",
    ],
    "learning": [
        "designing-digital-learning-experiences",
        "designing-course-catalogs",
        "designing-curriculum-pathways",
        "designing-lesson-navigation",
        "designing-learning-progress-tracking",
        "designing-practice-problem-workflows",
        "designing-quiz-authoring",
        "designing-quiz-taking",
        "designing-timed-assessment-interfaces",
        "designing-assessment-question-navigation",
        "designing-answer-review-and-explanations",
        "designing-rubric-based-grading",
        "designing-gradebook-interfaces",
        "designing-assignment-submission",
        "designing-academic-integrity-review",
        "designing-spaced-repetition-systems",
        "designing-flashcard-study-interfaces",
        "designing-certificate-and-completion-flows",
        "designing-instructor-cohort-analytics",
        "designing-learning-accommodation-controls",
    ],
    "financial-ops": [
        "designing-financial-operations-workspaces",
        "designing-general-ledger-browsing",
        "designing-journal-entry-workflows",
        "designing-bank-reconciliation",
        "designing-accounts-payable-queues",
        "designing-accounts-receivable-workflows",
        "designing-expense-review-and-approval",
        "designing-budget-planning",
        "designing-cash-flow-forecasting",
        "designing-financial-statement-navigation",
        "designing-variance-analysis",
        "designing-chart-of-accounts-management",
        "designing-tax-category-mapping",
        "designing-multi-currency-exposure-views",
        "designing-portfolio-position-monitoring",
        "designing-trading-order-entry",
        "designing-market-watchlists",
        "designing-order-book-interfaces",
        "designing-trade-blotters",
        "designing-financial-risk-limit-controls",
    ],
    "security-ops": [
        "designing-security-operations-workspaces",
        "designing-security-alert-triage",
        "designing-threat-investigation-timelines",
        "designing-security-entity-investigation",
        "designing-indicator-of-compromise-search",
        "designing-security-event-correlation",
        "designing-detection-rule-authoring",
        "designing-detection-rule-testing",
        "designing-attack-path-visualization",
        "designing-vulnerability-prioritization",
        "designing-patch-exposure-review",
        "designing-endpoint-isolation-controls",
        "designing-network-session-investigation",
        "designing-authentication-anomaly-review",
        "designing-privilege-escalation-review",
        "designing-phishing-investigation",
        "designing-malware-analysis-result-views",
        "designing-security-case-evidence-management",
        "designing-threat-hunting-workspaces",
        "designing-security-operations-handoffs",
    ],
}

COURT_META = {
    "diagram": ("diagram", "diagram-specialist", "designing-editor-canvas-workspaces"),
    "project": ("project", "project-specialist", "designing-task-flows"),
    "incident": ("incident", "incident-specialist", "designing-high-stakes-decisions"),
    "delivery": ("delivery", "delivery-specialist", "designing-environment-management"),
    "instrumentation": ("instrumentation", "instrumentation-specialist", "designing-high-stakes-decisions"),
    "cad": ("cad", "cad-specialist", "designing-editor-canvas-workspaces"),
    "media-editing": ("media-editing", "media-editing-specialist", "designing-editor-canvas-workspaces"),
    "learning": ("learning", "learning-specialist", "routing-ui-work"),
    "financial-ops": ("financial-ops", "financial-ops-specialist", "designing-financial-transaction-ui"),
    "security-ops": ("security-ops", "security-ops-specialist", "designing-security-centers"),
}


def _output_for(slug: str) -> str:
    return slug.removeprefix("designing-") + "-contract"


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


BATCH_004 = _records()
SLUGS = [record["slug"] for record in BATCH_004]
EXPECTED = {record["slug"]: record for record in BATCH_004}


def _normalized_body(text: str) -> str:
    text = re.sub(r"^---.*?---\s*", "", text, flags=re.DOTALL)
    text = re.sub(r"^#.*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"designing-[a-z0-9-]+", "<skill>", text.lower())
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return " ".join(text.split())


class UIIndustryBatch004Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph = json.loads(GRAPH_PATH.read_text(encoding="utf-8"))
        cls.graph_skills = cls.graph["skills"]

    def test_batch_has_exactly_two_hundred_unique_slugs(self):
        self.assertEqual(200, len(BATCH_004))
        self.assertEqual(200, len(set(SLUGS)))

    def test_each_court_has_exactly_twenty_skills(self):
        counts = Counter(record["court"] for record in BATCH_004)
        self.assertEqual(set(COURTS), set(counts))
        self.assertEqual({20}, set(counts.values()))

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
        outputs = [record["output"] for record in BATCH_004]
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

    def test_graph_preserves_batch_004_baseline_at_or_above_674(self):
        self.assertGreaterEqual(len(self.graph_skills), 674)

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
        suspicious = []
        for index, left in enumerate(slugs):
            for right in slugs[index + 1 :]:
                ratio = difflib.SequenceMatcher(None, bodies[left].split(), bodies[right].split(), autojunk=False).ratio()
                if ratio >= 0.82:
                    suspicious.append((left, right, round(ratio, 3)))
        self.assertEqual([], suspicious)

    def test_no_placeholder_corpus_text(self):
        banned = ("TBD", "TODO", "fill this in", "same as above", "lorem ipsum")
        for slug in SLUGS:
            path = SKILLS_DIR / slug / "SKILL.md"
            self.assertTrue(path.is_file(), slug)
            text = path.read_text(encoding="utf-8")
            for token in banned:
                self.assertNotIn(token.lower(), text.lower(), f"{slug}: placeholder {token}")


if __name__ == "__main__":
    unittest.main()
