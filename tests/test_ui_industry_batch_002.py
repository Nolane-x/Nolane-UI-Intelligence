import difflib
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
GRAPH_PATH = SKILLS_DIR / "skill-graph.json"

BATCH_002 = [
    "designing-field-validation-and-error-recovery",
    "designing-dependent-form-fields",
    "designing-multi-step-forms",
    "designing-form-autosave-and-drafts",
    "designing-address-entry",
    "designing-phone-number-entry",
    "designing-one-time-code-entry",
    "designing-password-creation-and-strength",
    "designing-monetary-input",
    "designing-measurement-and-unit-input",
    "designing-global-navigation-shells",
    "designing-sidebar-navigation",
    "designing-breadcrumb-navigation",
    "designing-mega-navigation",
    "designing-pagination",
    "designing-infinite-scroll-browsing",
    "designing-search-result-interfaces",
    "designing-faceted-search",
    "designing-saved-searches-and-views",
    "designing-recent-items-navigation",
    "designing-toast-feedback",
    "designing-inline-status-feedback",
    "designing-persistent-banner-alerts",
    "designing-notification-centers",
    "designing-background-task-progress",
    "designing-indeterminate-progress",
    "designing-skeleton-loading",
    "designing-partial-failure-states",
    "designing-retry-and-recovery-actions",
    "designing-connectivity-recovery",
    "designing-chat-interfaces",
    "designing-threaded-conversations",
    "designing-message-composers",
    "designing-message-delivery-state",
    "designing-read-receipts",
    "designing-typing-indicators",
    "designing-message-reactions",
    "designing-message-attachments",
    "designing-mentions-and-references",
    "designing-conversation-search",
    "designing-comment-systems",
    "designing-annotation-workflows",
    "designing-collaborative-cursors",
    "designing-live-presence-indicators",
    "designing-sharing-dialogs",
    "designing-invitation-flows",
    "designing-link-sharing",
    "designing-collaboration-permissions",
    "designing-review-feedback-workflows",
    "designing-collaboration-awareness",
    "designing-first-run-onboarding",
    "designing-product-tours",
    "designing-coach-marks",
    "designing-onboarding-checklists",
    "designing-contextual-help",
    "designing-help-center-navigation",
    "designing-progressive-feature-discovery",
    "designing-sample-data-experiences",
    "designing-permission-onboarding",
    "designing-migration-onboarding",
    "designing-product-catalog-browsing",
    "designing-product-detail-purchase-decisions",
    "designing-product-variant-selection",
    "designing-shopping-carts",
    "designing-checkout-step-orchestration",
    "designing-shipping-method-selection",
    "designing-promotion-code-entry",
    "designing-order-tracking",
    "designing-return-and-refund-flows",
    "designing-wishlists-and-saved-items",
    "designing-rich-text-editors",
    "designing-markdown-editors",
    "designing-content-composer-workflows",
    "designing-content-preview",
    "designing-publishing-controls",
    "designing-content-scheduling",
    "designing-editorial-status-workflows",
    "designing-content-taxonomy-management",
    "designing-media-library-interfaces",
    "designing-content-localization-workflows",
    "designing-api-explorers",
    "designing-schema-explorers",
    "designing-query-builders",
    "designing-log-viewers",
    "designing-trace-exploration",
    "designing-metrics-exploration",
    "designing-feature-flag-management",
    "designing-webhook-management",
    "designing-secret-credential-management",
    "designing-environment-management",
    "designing-consent-preference-centers",
    "designing-cookie-consent-controls",
    "designing-privacy-control-centers",
    "designing-security-centers",
    "designing-device-session-management",
    "designing-two-factor-enrollment",
    "designing-recovery-code-management",
    "designing-data-export-portability",
    "designing-account-deletion",
    "designing-account-recovery-flows",
]


def _normalized_body(text: str) -> str:
    text = re.sub(r"^---.*?---\s*", "", text, flags=re.DOTALL)
    text = re.sub(r"^#.*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"designing-[a-z0-9-]+", "<skill>", text.lower())
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return " ".join(text.split())


class UIIndustryBatch002Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph = json.loads(GRAPH_PATH.read_text(encoding="utf-8"))
        cls.graph_skills = cls.graph["skills"]

    def test_batch_has_exactly_one_hundred_unique_slugs(self):
        self.assertEqual(100, len(BATCH_002))
        self.assertEqual(100, len(set(BATCH_002)))

    def test_each_skill_exists_and_frontmatter_name_matches_slug(self):
        for slug in BATCH_002:
            path = SKILLS_DIR / slug / "SKILL.md"
            self.assertTrue(path.is_file(), slug)
            text = path.read_text(encoding="utf-8")
            match = re.match(r"^---\nname:\s*([^\n]+)\n", text)
            self.assertIsNotNone(match, slug)
            self.assertEqual(slug, match.group(1).strip())

    def test_each_skill_has_behavioral_depth_signals(self):
        signals = ("Decision", "Failure", "Falsif", "Output")
        for slug in BATCH_002:
            text = (SKILLS_DIR / slug / "SKILL.md").read_text(encoding="utf-8")
            self.assertGreaterEqual(len(text), 1800, slug)
            for signal in signals:
                self.assertIn(signal, text, f"{slug}: missing {signal}")

    def test_each_skill_is_registered_with_valid_metadata(self):
        for slug in BATCH_002:
            self.assertIn(slug, self.graph_skills)
            node = self.graph_skills[slug]
            self.assertTrue(node.get("family"), slug)
            self.assertTrue(node.get("parent"), slug)
            self.assertTrue(node.get("output"), slug)
            self.assertIn(node["parent"], self.graph_skills, slug)

    def test_batch_outputs_are_unique_and_do_not_collide_with_prior_graph(self):
        batch_outputs = [self.graph_skills[slug]["output"] for slug in BATCH_002 if slug in self.graph_skills]
        self.assertEqual(len(batch_outputs), len(set(batch_outputs)))
        prior_outputs = {
            node.get("output")
            for slug, node in self.graph_skills.items()
            if slug not in BATCH_002 and isinstance(node, dict)
        }
        self.assertFalse(set(batch_outputs) & prior_outputs)

    def test_parent_chain_reaches_nui_root_without_cycles(self):
        for slug in BATCH_002:
            self.assertIn(slug, self.graph_skills)
            seen = set()
            current = slug
            while current is not None:
                self.assertNotIn(current, seen, f"cycle from {slug}")
                seen.add(current)
                current = self.graph_skills[current]["parent"]
            self.assertIn("using-nolane-ui", seen, slug)

    def test_final_graph_count_is_exactly_374(self):
        self.assertEqual(374, len(self.graph_skills))

    def test_no_exact_normalized_body_duplicates(self):
        seen = {}
        for slug in BATCH_002:
            path = SKILLS_DIR / slug / "SKILL.md"
            self.assertTrue(path.is_file(), slug)
            norm = _normalized_body(path.read_text(encoding="utf-8"))
            self.assertNotIn(norm, seen, f"{slug} duplicates {seen.get(norm)}")
            seen[norm] = slug

    def test_no_pair_is_a_trivial_rename(self):
        bodies = {}
        for slug in BATCH_002:
            path = SKILLS_DIR / slug / "SKILL.md"
            self.assertTrue(path.is_file(), slug)
            bodies[slug] = _normalized_body(path.read_text(encoding="utf-8"))
        slugs = list(bodies)
        suspicious = []
        for index, left in enumerate(slugs):
            for right in slugs[index + 1 :]:
                ratio = difflib.SequenceMatcher(None, bodies[left], bodies[right]).ratio()
                if ratio >= 0.86:
                    suspicious.append((left, right, round(ratio, 3)))
        self.assertEqual([], suspicious)


if __name__ == "__main__":
    unittest.main()
