import unittest
from pathlib import Path

from nolane_ui.rules_v13.catalog import load_rule_catalog_v13
from nolane_ui.rules_v13.similarity import audit_catalog_similarity


EXPECTED_SECOND_WAVE = {
    "ui.accessibility.focus-visible-under-overlays",
    "ui.accessibility.name-updates-with-state",
    "ui.accessibility.pointer-cancel-before-commit",
    "ui.accessibility.drag-has-nondrag-path",
    "ui.accessibility.reduced-motion-removes-trigger",
    "ui.accessibility.live-region-does-not-spam",
    "ui.navigation.back-restores-context",
    "ui.navigation.deep-link-resolves-valid-state",
    "ui.navigation.retry-preserves-user-work",
    "ui.navigation.offline-state-not-empty-success",
    "ui.navigation.notification-continuation-preserves-target",
    "ui.navigation.stale-route-resource-recovery",
    "ui.privacy.permission-purpose-matches-use",
    "ui.privacy.denied-permission-recovery",
    "ui.privacy.session-revocation-visible",
    "ui.privacy.shared-device-secret-redaction",
    "ui.privacy.consent-revocation-propagates",
    "ui.privacy.permission-escalation-requires-new-consent",
    "ui.mobile.safe-area-protects-primary-actions",
    "ui.mobile.virtual-keyboard-keeps-active-field-visible",
    "ui.mobile.orientation-preserves-task-state",
    "ui.mobile.gesture-conflict-has-alternative",
    "ui.mobile.responsive-reflow-preserves-reading-order",
    "ui.mobile.breakpoint-does-not-drop-active-controls",
    "ui.performance.loading-state-matches-progress",
    "ui.performance.skeleton-does-not-fake-final-content",
    "ui.performance.input-remains-responsive-under-background-work",
    "ui.media.buffering-distinct-from-paused",
    "ui.media.quality-fallback-preserves-timeline",
    "ui.media.download-retry-preserves-completed-work",
    "ui.locale.number-format-matches-locale-and-unit",
    "ui.locale.datetime-disambiguates-zone",
    "ui.locale.rtl-mirrors-directional-meaning-not-content",
    "ui.locale.translation-expansion-does-not-hide-action",
    "ui.search.filter-state-visible-in-results",
    "ui.search.saved-view-does-not-silently-drift",
}


class RuleV13SecondWaveQualityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[1]
        cls.catalog = load_rule_catalog_v13(cls.root)
        cls.by_id = {rule["rule_id"]: rule for rule in cls.catalog["rules"]}

    def test_expected_failure_classes_exist_without_count_quota(self):
        self.assertTrue(EXPECTED_SECOND_WAVE <= set(self.by_id))
        self.assertNotIn("minimum_rule_count", self.catalog)
        self.assertFalse(self.catalog["composition"]["rule_count_is_quality_target"])

    def test_owner_and_verifier_hints_resolve_to_real_skills(self):
        for rule_id in sorted(EXPECTED_SECOND_WAVE):
            rule = self.by_id[rule_id]
            for slug in rule["owner_hints"] + rule["verifier_hints"]:
                self.assertTrue((self.root / "skills" / slug / "SKILL.md").is_file(), (rule_id, slug))

    def test_provenance_resolves_and_is_not_emerging_only(self):
        records = {item["provenance_id"]: item for item in self.catalog["provenance"]["records"]}
        for rule_id in sorted(EXPECTED_SECOND_WAVE):
            rule = self.by_id[rule_id]
            evidence_classes = {records[pid]["evidence_class"] for pid in rule["provenance_ids"]}
            self.assertNotEqual(evidence_classes, {"emerging"}, rule_id)

    def test_second_wave_operational_signatures_are_distinct(self):
        signatures = {}
        for rule_id in sorted(EXPECTED_SECOND_WAVE):
            rule = self.by_id[rule_id]
            signature = (tuple(rule["failure_modes"]), tuple(rule["repairs"]), tuple(rule["verification"]))
            self.assertNotIn(signature, signatures, (rule_id, signatures.get(signature)))
            signatures[signature] = rule_id

    def test_full_catalog_still_passes_anti_duplication_court(self):
        similarity = audit_catalog_similarity(self.catalog["rules"])
        self.assertTrue(similarity["valid"], similarity)
        self.assertEqual(similarity["duplicate_pair_count"], 0, similarity)
        self.assertEqual(similarity["boilerplate_cluster_count"], 0, similarity)


if __name__ == "__main__":
    unittest.main()
