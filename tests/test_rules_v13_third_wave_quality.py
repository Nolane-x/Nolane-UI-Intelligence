import unittest
from pathlib import Path

from nolane_ui.rules_v13.catalog import load_rule_catalog_v13
from nolane_ui.rules_v13.similarity import audit_catalog_similarity


EXPECTED_THIRD_WAVE = {
    'ui.collaboration.presence-distinguishes-viewing-editing',
    'ui.collaboration.remote-delete-does-not-destroy-local-draft',
    'ui.collaboration.conflict-resolution-preserves-both-versions',
    'ui.collaboration.cursor-identity-stable',
    'ui.collaboration.permission-change-revokes-action',
    'ui.collaboration.offline-edits-rejoin-with-conflict-state',
    'ui.files.upload-queue-item-identity',
    'ui.files.resume-validates-source-version',
    'ui.files.rename-conflict-no-silent-overwrite',
    'ui.files.share-expiry-visible',
    'ui.files.preview-not-authoritative-download',
    'ui.files.storage-limit-before-transfer',
    'ui.notifications.read-state-cross-device-consistent',
    'ui.notifications.dismiss-does-not-mark-action-complete',
    'ui.notifications.permission-denial-not-block-core',
    'ui.background.progress-survives-navigation',
    'ui.background.completion-notifies-correct-job',
    'ui.background.cancel-state-terminal',
    'ui.sync.stale-data-labeled-with-age',
    'ui.sync.optimistic-write-reconciles-server-rejection',
    'ui.sync.partial-sync-not-global-success',
    'ui.sync.cross-device-conflict-does-not-last-write-silently',
    'ui.sync.clock-skew-not-order-authority',
    'ui.sync.reconnect-does-not-duplicate-write',
    'ui.history.undo-restores-dependent-state',
    'ui.history.redo-invalidated-after-divergent-edit',
    'ui.history.version-restore-is-new-version',
    'ui.destructive.bulk-scope-visible-before-commit',
    'ui.destructive.delete-pending-not-gone',
    'ui.destructive.archive-vs-delete-distinct',
    'ui.finance.currency-mismatch-before-commit',
    'ui.finance.pending-transaction-not-settled',
    'ui.finance.limit-breach-explains-block',
    'ui.admin.role-change-effective-scope-visible',
    'ui.admin.bulk-action-partial-failure',
    'ui.admin.audit-entry-after-authoritative-commit',
}


class RuleV13ThirdWaveQualityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[1]
        cls.catalog = load_rule_catalog_v13(cls.root)
        cls.by_id = {rule['rule_id']: rule for rule in cls.catalog['rules']}

    def test_explicit_failure_classes_exist(self):
        self.assertTrue(EXPECTED_THIRD_WAVE <= set(self.by_id))

    def test_real_owners(self):
        for rid in EXPECTED_THIRD_WAVE:
            for slug in self.by_id[rid]['owner_hints'] + self.by_id[rid]['verifier_hints']:
                self.assertTrue((self.root / 'skills' / slug / 'SKILL.md').is_file(), (rid, slug))

    def test_provenance(self):
        records = {item['provenance_id']: item for item in self.catalog['provenance']['records']}
        for rid in EXPECTED_THIRD_WAVE:
            self.assertTrue(all(pid in records for pid in self.by_id[rid]['provenance_ids']))

    def test_distinct_signatures(self):
        seen = {}
        for rid in sorted(EXPECTED_THIRD_WAVE):
            rule = self.by_id[rid]
            signature = (tuple(rule['failure_modes']), tuple(rule['repairs']), tuple(rule['verification']))
            self.assertNotIn(signature, seen, (rid, seen.get(signature)))
            seen[signature] = rid

    def test_full_anti_dup(self):
        audit = audit_catalog_similarity(self.catalog['rules'])
        self.assertTrue(audit['valid'], audit)
        self.assertEqual(audit['duplicate_pair_count'], 0)
        self.assertEqual(audit['boilerplate_cluster_count'], 0)


if __name__ == '__main__':
    unittest.main()
