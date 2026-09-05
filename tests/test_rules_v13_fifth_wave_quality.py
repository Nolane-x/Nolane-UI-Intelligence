import unittest
from pathlib import Path

from nolane_ui.rules_v13.catalog import load_rule_catalog_v13
from nolane_ui.rules_v13.similarity import audit_catalog_similarity

EXPECTED_FIFTH_WAVE = {
    # identity/session
    'ui.identity.session-revocation-blocks-protected-commit',
    'ui.identity.reauthentication-returns-to-intended-action',
    'ui.identity.current-session-distinguished-in-device-list',
    'ui.identity.recovery-channel-change-requires-fresh-auth',
    'ui.identity.passkey-registration-exposes-account-and-device-context',
    'ui.identity.account-switch-clears-prior-account-authority',
    'ui.identity.shared-device-signout-clears-sensitive-residue',
    'ui.identity.auth-step-retry-does-not-reset-valid-progress',
    # tables/grids
    'ui.table.grid-focus-survives-virtualization',
    'ui.table.edit-cancel-restores-authoritative-cell',
    'ui.table.sort-state-announced-with-active-column',
    'ui.table.group-selection-scope-visible',
    'ui.table.bulk-edit-partial-failure-maps-to-records',
    'ui.table.pinned-columns-do-not-cover-row-actions',
    'ui.table.column-visibility-preserves-header-association',
    'ui.table.treegrid-collapse-restores-logical-focus',
    # maps/location
    'ui.map.position-accuracy-bound-visible',
    'ui.map.position-freshness-visible',
    'ui.map.map-list-selection-synchronized',
    'ui.map.cluster-expansion-preserves-selected-place',
    'ui.map.denied-location-has-manual-location-path',
    'ui.map.background-location-active-state-visible',
    'ui.map.route-recalculation-does-not-change-destination',
    'ui.map.location-unavailable-distinct-from-no-results',
    # media
    'ui.media.captions-available-not-equal-enabled',
    'ui.media.audio-description-track-state-visible',
    'ui.media.playback-speed-preserves-caption-sync',
    'ui.media.seek-preview-not-committed-until-seek',
    'ui.media.live-edge-distinct-from-current-playback',
    'ui.media.cast-state-distinct-from-local-playback',
    'ui.media.picture-in-picture-return-preserves-state',
    'ui.media.entitlement-failure-distinct-from-network-failure',
    # comments/moderation
    'ui.comments.retry-does-not-duplicate-comment',
    'ui.comments.mention-resolves-stable-identity',
    'ui.comments.edited-state-visible-after-change',
    'ui.comments.deleted-parent-preserves-thread-context',
    'ui.comments.moderation-action-scope-visible',
    'ui.comments.moderation-reversal-restores-prior-state',
    'ui.comments.hidden-state-distinct-from-deleted',
    'ui.comments.unread-marker-survives-thread-reorder',
    # search/recommendation
    'ui.search.query-and-filter-state-distinct',
    'ui.search.saved-search-definition-change-visible',
    'ui.search.zero-results-distinct-from-search-failure',
    'ui.search.pagination-does-not-repeat-result-identity',
    'ui.recommendation.personalization-toggle-changes-effective-ranking-input',
    'ui.recommendation.feedback-target-bound-to-item',
    'ui.recommendation.explanation-does-not-invent-ranking-precision',
    'ui.recommendation.dismissed-item-does-not-immediately-reappear-with-same-identity',
    # offline/connectivity
    'ui.offline.queued-mutation-bound-to-account',
    'ui.offline.cached-data-shows-last-authoritative-sync',
    'ui.offline.update-activation-preserves-unsaved-work',
    'ui.offline.expired-auth-pauses-sync-with-local-work-preserved',
    'ui.offline.capability-boundary-visible-before-action',
    'ui.offline.retry-queue-preserves-operation-order',
    'ui.offline.background-sync-result-reconciles-visible-state',
    'ui.offline.local-delete-conflict-does-not-silently-resurrect',
    # onboarding/permissions
    'ui.onboarding.skip-keeps-settings-reentry-path',
    'ui.onboarding.checklist-completion-derived-from-real-state',
    'ui.onboarding.permission-primer-matches-requested-capability',
    'ui.onboarding.denied-permission-does-not-loop-prompt',
    'ui.onboarding.one-time-permission-expiry-reconciles-ui',
    'ui.onboarding.resume-returns-to-unresolved-step',
    'ui.onboarding.optional-personalization-does-not-block-core',
    'ui.onboarding.permission-scope-expansion-explains-delta',
    # commerce lifecycle
    'ui.commerce.estimated-tax-shipping-distinct-from-final',
    'ui.commerce.promotion-removal-explains-total-change',
    'ui.commerce.payment-retry-reuses-order-identity',
    'ui.commerce.partial-fulfillment-state-per-item',
    'ui.commerce.return-eligibility-basis-visible',
    'ui.commerce.plan-downgrade-effective-date-visible',
    'ui.commerce.credit-allocation-visible-before-charge',
    'ui.commerce.dispute-state-distinct-from-refund',
    # agent runtime
    'ui.ai.retry-shows-reused-and-changed-inputs',
    'ui.ai.partial-completion-separates-committed-from-planned',
    'ui.ai.tool-timeout-distinct-from-tool-failure',
    'ui.ai.permission-elevation-expiry-visible',
    'ui.ai.run-branch-identity-visible',
    'ui.ai.human-correction-invalidates-stale-downstream-plan',
    'ui.ai.multi-agent-handoff-current-actor-visible',
    'ui.ai.side-effect-ledger-matches-authoritative-actions',
    # notifications
    'ui.notifications.cross-channel-duplicates-collapse-by-event',
    'ui.notifications.badge-count-scope-visible',
    'ui.notifications.snooze-mute-effective-state-visible',
    'ui.notifications.action-failure-remains-recoverable',
    'ui.notifications.timestamp-distinguishes-event-from-delivery',
    'ui.notifications.channel-disable-does-not-imply-event-deletion',
    'ui.notifications.archive-distinct-from-read',
    'ui.notifications.grouped-summary-does-not-hide-actionable-child',
    # native/device
    'ui.native.bluetooth-pairing-target-identity-stable',
    'ui.native.share-cancel-does-not-report-success',
    'ui.native.handoff-confirms-target-account-and-device',
    'ui.native.input-prompt-switch-does-not-steal-active-operation',
    'ui.native.navigation-restoration-preserves-task-state',
    'ui.native.external-display-disconnect-restores-primary-controls',
    'ui.native.capability-negotiation-does-not-offer-unsupported-action',
    'ui.native.device-discovery-expiry-removes-stale-target',
}

UMBRELLA_ONLY = {'nui-internal-product-truth-v13'}


class RuleV13FifthWaveQualityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[1]
        cls.catalog = load_rule_catalog_v13(cls.root)
        cls.by_id = {rule['rule_id']: rule for rule in cls.catalog['rules']}
        cls.provenance = {record['provenance_id']: record for record in cls.catalog['provenance']['records']}

    def test_explicit_failure_classes_exist_without_quota(self):
        self.assertEqual(len(EXPECTED_FIFTH_WAVE), 96)
        self.assertTrue(EXPECTED_FIFTH_WAVE <= set(self.by_id))
        self.assertFalse(self.catalog['composition']['rule_count_is_quality_target'])
        self.assertFalse({'minimum_rule_count', 'required_rule_count', 'rule_quota'} & set(self.catalog))

    def test_owner_and_verifier_hints_resolve_to_real_skills(self):
        for rid in sorted(EXPECTED_FIFTH_WAVE):
            rule = self.by_id[rid]
            for slug in rule['owner_hints'] + rule['verifier_hints']:
                self.assertTrue((self.root / 'skills' / slug / 'SKILL.md').is_file(), (rid, slug))

    def test_provenance_is_specific_resolved_and_not_emerging_only(self):
        for rid in sorted(EXPECTED_FIFTH_WAVE):
            pids = set(self.by_id[rid]['provenance_ids'])
            self.assertTrue(pids <= set(self.provenance), (rid, pids - set(self.provenance)))
            self.assertNotEqual(pids, UMBRELLA_ONLY, rid)
            evidence_classes = {self.provenance[pid]['evidence_class'] for pid in pids}
            self.assertNotEqual(evidence_classes, {'emerging'}, rid)

    def test_operational_signatures_are_distinct(self):
        seen = {}
        for rid in sorted(EXPECTED_FIFTH_WAVE):
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
