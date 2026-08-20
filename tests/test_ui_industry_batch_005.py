import difflib
import json
import re
import unittest
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
GRAPH_PATH = SKILLS_DIR / "skill-graph.json"
PROVENANCE_PATH = ROOT / "docs" / "research" / "UI-INDUSTRY-1000-BATCH-005.md"

COURTS = {
    "mobile-native": [
        "designing-mobile-native-application-shells",
        "designing-native-navigation-stacks",
        "designing-tab-bar-state-continuity",
        "designing-mobile-safe-area-integration",
        "designing-virtual-keyboard-avoidance",
        "designing-mobile-deep-link-routing",
        "designing-app-lifecycle-state-restoration",
        "designing-native-share-sheet-intents",
        "designing-mobile-app-switcher-privacy",
        "designing-mobile-gesture-navigation-conflicts",
    ],
    "visual-builder": [
        "designing-visual-application-builders",
        "designing-canvas-hierarchy-synchronization",
        "designing-responsive-breakpoint-authoring",
        "designing-style-inheritance-inspection",
        "designing-component-instance-overrides",
        "designing-builder-component-authoring",
        "designing-builder-slot-insertion",
        "designing-builder-data-binding",
        "designing-builder-conditional-visibility",
        "designing-builder-interaction-wiring",
        "designing-builder-preview-publish-modes",
        "designing-builder-layout-constraint-editing",
    ],
    "business-intelligence": [
        "designing-business-intelligence-workspaces",
        "designing-semantic-metric-browsing",
        "designing-query-provenance-inspection",
        "designing-dashboard-edit-view-modes",
        "designing-dashboard-filter-scope",
        "designing-drill-path-continuity",
        "designing-data-freshness-communication",
        "designing-metric-definition-comparison",
        "designing-alert-to-analysis-handoffs",
        "designing-saved-analysis-workspaces",
        "designing-dashboard-permission-boundaries",
        "designing-data-lineage-exploration",
    ],
    "clinical": [
        "designing-clinical-care-workflows",
        "designing-patient-identity-banners",
        "designing-clinical-encounter-context",
        "designing-medication-order-entry",
        "designing-medication-reconciliation",
        "designing-lab-result-review",
        "designing-clinical-result-abnormality",
        "designing-clinical-order-status",
        "designing-problem-list-management",
        "designing-clinical-note-signing",
        "designing-clinical-handoff-summaries",
        "designing-radiology-study-navigation",
        "designing-medical-image-measurements",
        "designing-clinical-alert-fatigue-controls",
    ],
    "public-service": [
        "designing-public-service-experiences",
        "designing-service-eligibility-checkers",
        "designing-government-application-journeys",
        "designing-service-evidence-upload",
        "designing-save-and-return-service-flows",
        "designing-assisted-digital-handoffs",
        "designing-public-service-status-tracking",
        "designing-identity-proofing-service-flows",
        "designing-benefit-entitlement-explanations",
        "designing-public-service-change-reporting",
    ],
    "marketplace": [
        "designing-marketplace-operations",
        "designing-seller-onboarding",
        "designing-listing-moderation-workflows",
        "designing-marketplace-inventory-availability",
        "designing-order-exception-management",
        "designing-split-fulfillment-shipments",
        "designing-marketplace-dispute-resolution",
        "designing-marketplace-payout-status",
        "designing-buyer-seller-messaging-boundaries",
        "designing-marketplace-trust-signals",
    ],
    "realtime": [
        "designing-realtime-communication-systems",
        "designing-room-channel-membership",
        "designing-message-sync-gap-recovery",
        "designing-offline-message-reconciliation",
        "designing-end-to-end-encryption-state",
        "designing-key-verification-flows",
        "designing-call-join-device-checks",
        "designing-call-participant-layouts",
        "designing-screen-share-control",
        "designing-moderation-action-surfaces",
    ],
    "xr": [
        "designing-ray-pointer-interaction",
        "designing-gaze-targeting",
        "designing-hand-direct-manipulation",
        "designing-world-space-panel-placement",
        "designing-spatial-ui-distance-scaling",
        "designing-occlusion-aware-interface-placement",
        "designing-spatial-anchor-persistence",
        "designing-xr-locomotion-controls",
        "designing-xr-safety-boundaries",
        "designing-xr-dom-overlay-coordination",
    ],
    "personalization": [
        "designing-recommendation-personalization-surfaces",
        "designing-recommendation-explanations",
        "designing-personalization-controls",
        "designing-ranking-feedback-loops",
        "designing-cold-start-preference-capture",
        "designing-recommendation-diversity-controls",
    ],
    "design-to-code": [
        "designing-design-to-code-handoffs",
        "designing-component-mapping-to-code",
        "designing-token-mapping-to-code",
        "designing-responsive-intent-handoff",
        "designing-interaction-specification-handoff",
        "designing-design-code-drift-review",
    ],
}

COURT_META = {
    "mobile-native": ("mobile-native", "mobile-native-specialist", "adapting-platform-conventions"),
    "visual-builder": ("visual-builder", "visual-builder-specialist", "designing-editor-canvas-workspaces"),
    "business-intelligence": ("business-intelligence", "business-intelligence-specialist", "designing-data-dense-interfaces"),
    "clinical": ("clinical", "clinical-specialist", "designing-high-stakes-decisions"),
    "public-service": ("public-service", "public-service-specialist", "routing-ui-work"),
    "marketplace": ("marketplace", "marketplace-specialist", "designing-commerce-checkout"),
    "realtime": ("realtime-communication", "realtime-communication-specialist", "designing-collaboration-and-presence"),
    "xr": (None, "xr-specialist", "designing-spatial-xr-interfaces"),
    "personalization": ("personalization", "personalization-specialist", "routing-ui-work"),
    "design-to-code": ("design-to-code", "design-to-code-specialist", "routing-ui-work"),
}

EXPECTED_COUNTS = {
    "mobile-native": 10,
    "visual-builder": 12,
    "business-intelligence": 12,
    "clinical": 14,
    "public-service": 10,
    "marketplace": 10,
    "realtime": 10,
    "xr": 10,
    "personalization": 6,
    "design-to-code": 6,
}


def _output_for(slug: str) -> str:
    return slug.removeprefix("designing-") + "-contract"


def _records():
    records = []
    for court, slugs in COURTS.items():
        root_family, child_family, root_parent = COURT_META[court]
        root = slugs[0]
        for index, slug in enumerate(slugs):
            if root_family is None:
                family = child_family
                parent = root_parent
            else:
                family = root_family if index == 0 else child_family
                parent = root_parent if index == 0 else root
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


BATCH_005 = _records()
SLUGS = [record["slug"] for record in BATCH_005]
EXPECTED = {record["slug"]: record for record in BATCH_005}


def _normalized_body(text: str) -> str:
    text = re.sub(r"^---.*?---\s*", "", text, flags=re.DOTALL)
    text = re.sub(r"^#{1,6}.*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"designing-[a-z0-9-]+", "<skill>", text.lower())
    text = re.sub(r"`[^`]+`", "<token>", text)
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return " ".join(text.split())


def _substantive_paragraphs(text: str):
    text = re.sub(r"^---.*?---\s*", "", text, flags=re.DOTALL)
    paragraphs = []
    for paragraph in re.split(r"\n\s*\n", text):
        p = " ".join(paragraph.split())
        if p.startswith("#") or len(p) < 120:
            continue
        p = re.sub(r"designing-[a-z0-9-]+", "<skill>", p.lower())
        paragraphs.append(p)
    return paragraphs


class UIIndustryBatch005Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph = json.loads(GRAPH_PATH.read_text(encoding="utf-8"))
        cls.graph_skills = cls.graph["skills"]

    def test_batch_has_exactly_one_hundred_unique_slugs(self):
        self.assertEqual(100, len(BATCH_005))
        self.assertEqual(100, len(set(SLUGS)))

    def test_court_counts_are_explicit_and_exact(self):
        counts = Counter(record["court"] for record in BATCH_005)
        self.assertEqual(EXPECTED_COUNTS, dict(counts))

    def test_each_skill_exists_and_frontmatter_name_matches_slug(self):
        for slug in SLUGS:
            path = SKILLS_DIR / slug / "SKILL.md"
            self.assertTrue(path.is_file(), slug)
            text = path.read_text(encoding="utf-8")
            match = re.match(r"^---\nname:\s*([^\n]+)\n", text)
            self.assertIsNotNone(match, slug)
            self.assertEqual(slug, match.group(1).strip())

    def test_each_skill_has_substantive_individually_authored_depth(self):
        required_concepts = (
            "Decision",
            "evidence",
            "Failure",
            "Falsification",
            "Recovery",
            "Output",
            "Handoff",
        )
        for slug in SLUGS:
            path = SKILLS_DIR / slug / "SKILL.md"
            self.assertTrue(path.is_file(), slug)
            text = path.read_text(encoding="utf-8")
            self.assertGreaterEqual(len(text), 2800, slug)
            lowered = text.lower()
            for concept in required_concepts:
                self.assertIn(concept.lower(), lowered, f"{slug}: missing {concept}")

    def test_each_skill_is_registered_with_exact_locked_metadata(self):
        for slug, expected in EXPECTED.items():
            self.assertIn(slug, self.graph_skills)
            node = self.graph_skills[slug]
            self.assertEqual(expected["family"], node.get("family"), slug)
            self.assertEqual(expected["parent"], node.get("parent"), slug)
            self.assertEqual(expected["output"], node.get("output"), slug)

    def test_outputs_are_unique_and_do_not_collide_with_prior_graph(self):
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

    def test_provenance_ledger_covers_every_admitted_slug(self):
        self.assertTrue(PROVENANCE_PATH.is_file())
        text = PROVENANCE_PATH.read_text(encoding="utf-8")
        for slug in SLUGS:
            self.assertIn(f"`{slug}`", text, slug)

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
        for i, left in enumerate(slugs):
            for right in slugs[i + 1 :]:
                ratio = difflib.SequenceMatcher(None, bodies[left], bodies[right], autojunk=False).ratio()
                self.assertLess(ratio, 0.84, f"trivial rename risk: {left} vs {right} = {ratio:.3f}")

    def test_no_long_substantive_paragraph_is_mass_reused(self):
        owners = defaultdict(set)
        for slug in SLUGS:
            path = SKILLS_DIR / slug / "SKILL.md"
            self.assertTrue(path.is_file(), slug)
            for paragraph in set(_substantive_paragraphs(path.read_text(encoding="utf-8"))):
                owners[paragraph].add(slug)
        repeated = {paragraph: slugs for paragraph, slugs in owners.items() if len(slugs) >= 3}
        self.assertFalse(repeated, f"mass-reused substantive paragraphs: {repeated}")

    def test_closed_pr_19_inventory_is_not_silently_reintroduced_as_batch_shape(self):
        forbidden_roots = {
            "governing-design-system-evolution",
            "engineering-responsive-composition",
            "engineering-typographic-systems",
            "designing-agentic-interaction-systems",
            "engineering-ui-evidence-workflows",
        }
        self.assertFalse(forbidden_roots & set(SLUGS))


if __name__ == "__main__":
    unittest.main()
