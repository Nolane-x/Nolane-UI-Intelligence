import unittest
from pathlib import Path

from nolane_ui.rules_v13.catalog import load_rule_catalog_v13
from nolane_ui.rules_v13.similarity import audit_catalog_similarity


EXPECTED_FOURTH_WAVE = {
    'ui.schedule.dst-gap-invalid-local-time',
    'ui.schedule.dst-fold-disambiguates-repeated-time',
    'ui.schedule.organizer-zone-change-explicit-semantics',
    'ui.schedule.recurring-event-zone-semantics-stable',
    'ui.schedule.availability-cross-zone-date-boundary',
    'ui.schedule.all-day-event-not-shifted-by-zone',
    'ui.messaging.delivery-state-not-read-state',
    'ui.messaging.retry-does-not-duplicate-message',
    'ui.messaging.edit-race-preserves-latest-authoritative-version',
    'ui.messaging.attachment-send-waits-for-upload-authority',
    'ui.messaging.reply-target-stable-after-reorder',
    'ui.messaging.offline-send-queued-not-delivered',
    'ui.import.mapping-preview-before-commit',
    'ui.import.partial-failure-preserves-row-results',
    'ui.import.encoding-detection-reviewable',
    'ui.export.scope-matches-requested-filter',
    'ui.export.generated-file-bound-to-request-version',
    'ui.migration.resume-does-not-reapply-completed-step',
    'ui.capture.permission-denial-preserves-alternative-path',
    'ui.capture.orientation-metadata-not-double-applied',
    'ui.capture.retake-does-not-upload-rejected-capture',
    'ui.capture.document-page-order-stable',
    'ui.device.disconnect-during-action-reconciles-authority',
    'ui.device.hardware-selection-not-label-only',
    'ui.consent.preference-center-shows-effective-state',
    'ui.consent.scope-expansion-requires-renewed-choice',
    'ui.consent.optional-purpose-not-default-enabled',
    'ui.consent.essential-processing-not-fake-optional-toggle',
    'ui.consent.cross-device-preference-reconciles',
    'ui.consent.withdrawal-does-not-erase-required-record-without-policy',
    'ui.accessibility.screen-reader-order-preserves-meaning',
    'ui.accessibility.focus-return-when-origin-disappears',
    'ui.accessibility.virtualized-set-position-truthful',
    'ui.accessibility.zoom-reflow-preserves-essential-content',
    'ui.accessibility.text-spacing-does-not-clip-content',
    'ui.accessibility.single-key-shortcut-has-safeguard',
}


class RuleV13FourthWaveQualityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[1]
        cls.catalog = load_rule_catalog_v13(cls.root)
        cls.by_id = {rule['rule_id']: rule for rule in cls.catalog['rules']}

    def test_explicit_failure_classes_exist(self):
        self.assertTrue(EXPECTED_FOURTH_WAVE <= set(self.by_id))

    def test_real_owners_and_verifiers(self):
        for rid in EXPECTED_FOURTH_WAVE:
            for slug in self.by_id[rid]['owner_hints'] + self.by_id[rid]['verifier_hints']:
                self.assertTrue((self.root / 'skills' / slug / 'SKILL.md').is_file(), (rid, slug))

    def test_provenance_resolves(self):
        records = {item['provenance_id'] for item in self.catalog['provenance']['records']}
        for rid in EXPECTED_FOURTH_WAVE:
            self.assertTrue(set(self.by_id[rid]['provenance_ids']) <= records, rid)

    def test_operational_signatures_are_distinct(self):
        seen = {}
        for rid in sorted(EXPECTED_FOURTH_WAVE):
            rule = self.by_id[rid]
            signature = (tuple(rule['failure_modes']), tuple(rule['repairs']), tuple(rule['verification']))
            self.assertNotIn(signature, seen, (rid, seen.get(signature)))
            seen[signature] = rid

    def test_full_anti_duplication_court_remains_clean(self):
        audit = audit_catalog_similarity(self.catalog['rules'])
        self.assertTrue(audit['valid'], audit)
        self.assertEqual(audit['duplicate_pair_count'], 0)
        self.assertEqual(audit['boilerplate_cluster_count'], 0)


if __name__ == '__main__':
    unittest.main()
