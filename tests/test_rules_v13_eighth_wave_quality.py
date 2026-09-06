import unittest
from pathlib import Path

from nolane_ui.rules_v13.catalog import load_rule_catalog_v13
from nolane_ui.rules_v13.similarity import audit_catalog_similarity

EXPECTED_EIGHTH_WAVE = {
    # security alert triage
    'ui.securityalert.source-event-identity-preserved',
    'ui.securityalert.status-distinct-from-resolution',
    'ui.securityalert.suppression-scope-visible',
    'ui.securityalert.severity-recalculation-history-visible',
    'ui.securityalert.dedup-preserves-contributing-evidence',
    'ui.securityalert.assignment-handoff-atomic',
    'ui.securityalert.bulk-close-scope-confirmed',
    'ui.securityalert.stale-alert-state-reconciled',
    # security case evidence
    'ui.securitycase.evidence-provenance-immutable',
    'ui.securitycase.evidence-redaction-scope-visible',
    'ui.securitycase.case-merge-lineage-preserved',
    'ui.securitycase.export-chain-of-custody-consistent',
    'ui.securitycase.relationship-links-not-rewrite-history',
    'ui.securitycase.access-revocation-effective-immediately',
    'ui.securitycase.status-transition-basis-preserved',
    'ui.securitycase.external-evidence-load-failure-explicit',
    # threat hunting
    'ui.threathunt.query-time-range-authoritative',
    'ui.threathunt.partial-backend-coverage-visible',
    'ui.threathunt.schema-version-bound-to-query',
    'ui.threathunt.result-pagination-snapshot-stable',
    'ui.threathunt.evidence-bookmark-stable',
    'ui.threathunt.query-modification-diff-visible',
    'ui.threathunt.async-query-cancel-stops-authority',
    'ui.threathunt.zero-results-distinct-from-detection-gap',
    # authentication anomaly review
    'ui.authreview.risk-signal-freshness-visible',
    'ui.authreview.session-target-identity-stable',
    'ui.authreview.reauthentication-not-dismiss-investigation',
    'ui.authreview.challenge-outcome-distinguished',
    'ui.authreview.device-trust-state-visible',
    'ui.authreview.false-positive-dismissal-scope-visible',
    'ui.authreview.lockout-bypass-authority-explicit',
    'ui.authreview.investigation-action-linked-to-audit-event',
    # clinical orders
    'ui.clinicalorder.status-source-authoritative',
    'ui.clinicalorder.discontinued-distinct-from-completed',
    'ui.clinicalorder.pending-signature-visible',
    'ui.clinicalorder.patient-context-sticky-across-action',
    'ui.clinicalorder.duplicate-orders-distinguishable',
    'ui.clinicalorder.result-linked-to-order-identity',
    'ui.clinicalorder.cross-facility-context-visible',
    'ui.clinicalorder.stale-order-refresh-before-action',
    # lab results
    'ui.labresult.units-and-reference-range-preserved',
    'ui.labresult.preliminary-distinct-from-final',
    'ui.labresult.corrected-result-history-preserved',
    'ui.labresult.specimen-time-distinct-from-result-time',
    'ui.labresult.abnormal-flag-source-visible',
    'ui.labresult.patient-and-specimen-identity-bound',
    'ui.labresult.missing-result-distinct-from-normal',
    'ui.labresult.trend-comparability-basis-visible',
    # medication order entry
    'ui.medication.identity-strength-form-unambiguous',
    'ui.medication.dose-route-frequency-coupled',
    'ui.medication.allergy-check-pending-visible',
    'ui.medication.interaction-warning-source-visible',
    'ui.medication.discontinue-effective-time-visible',
    'ui.medication.prn-condition-visible',
    'ui.medication.taper-sequence-integrity-preserved',
    'ui.medication.duplicate-therapy-distinguishable',
    # radiology
    'ui.radiology.study-patient-accession-identity-bound',
    'ui.radiology.preliminary-distinct-from-final-report',
    'ui.radiology.image-series-completeness-visible',
    'ui.radiology.measurement-unit-and-frame-preserved',
    'ui.radiology.comparison-study-identity-visible',
    'ui.radiology.hanging-protocol-fallback-visible',
    'ui.radiology.laterality-orientation-preserved',
    'ui.radiology.partial-study-load-visible',
    # assessment taking
    'ui.assessment.attempt-state-preserved-across-navigation',
    'ui.assessment.unsaved-response-protected-on-navigation',
    'ui.assessment.flagged-question-state-persistent',
    'ui.assessment.submission-distinct-from-scoring',
    'ui.assessment.time-limit-authority-visible',
    'ui.assessment.accommodation-effective-state-visible',
    'ui.assessment.randomized-item-identity-stable',
    'ui.assessment.section-lock-boundary-visible',
    # quiz authoring
    'ui.quizauthor.draft-distinct-from-published-version',
    'ui.quizauthor.answer-key-hidden-from-learner-preview',
    'ui.quizauthor.scoring-weight-total-valid',
    'ui.quizauthor.randomization-pool-configuration-valid',
    'ui.quizauthor.preview-uses-target-delivery-config',
    'ui.quizauthor.question-delete-reference-impact-visible',
    'ui.quizauthor.media-asset-availability-verified',
    'ui.quizauthor.publish-creates-versioned-assessment',
    # learning progress
    'ui.learning.completion-distinct-from-mastery',
    'ui.learning.progress-freshness-visible',
    'ui.learning.cross-device-progress-reconciled',
    'ui.learning.prerequisite-effective-state-visible',
    'ui.learning.reset-semantics-confirmed',
    'ui.learning.partial-credit-aggregation-consistent',
    'ui.learning.hidden-content-progress-impact-visible',
    'ui.learning.course-version-migration-preserves-progress',
    # instructor analytics
    'ui.instructor.cohort-scope-visible',
    'ui.instructor.denominator-and-missing-learners-visible',
    'ui.instructor.time-window-basis-visible',
    'ui.instructor.privacy-aggregation-state-visible',
    'ui.instructor.late-submission-inclusion-visible',
    'ui.instructor.gradebook-freshness-visible',
    'ui.instructor.drilldown-population-consistent',
    'ui.instructor.export-preserves-analytics-filters',
    # resource booking
    'ui.booking.timezone-basis-visible',
    'ui.booking.held-distinct-from-confirmed',
    'ui.booking.capacity-checked-at-commit',
    'ui.booking.recurrence-exception-scope-visible',
    'ui.booking.resource-dependencies-visible',
    'ui.booking.cancellation-effective-scope-visible',
    'ui.booking.waitlist-promotion-state-visible',
    'ui.booking.stale-availability-conflict-reconciled',
    # marketplace operations
    'ui.marketops.listing-moderation-state-visible',
    'ui.marketops.order-distinct-from-payout-state',
    'ui.marketops.seller-scope-visible',
    'ui.marketops.inventory-reservation-source-visible',
    'ui.marketops.bulk-operation-scope-confirmed',
    'ui.marketops.policy-hold-reason-and-state-visible',
    'ui.marketops.dispute-linkage-stable',
    'ui.marketops.search-index-lag-visible',
    # marketplace dispute
    'ui.dispute.deadline-authority-visible',
    'ui.dispute.evidence-submission-receipt-preserved',
    'ui.dispute.partial-refund-distinct-from-dispute-resolution',
    'ui.dispute.party-identity-stable',
    'ui.dispute.evidence-access-scope-visible',
    'ui.dispute.status-and-appeal-path-visible',
    'ui.dispute.provider-decision-import-reconciled',
    'ui.dispute.merge-lineage-preserved',
    # marketplace inventory
    'ui.inventory.available-onhand-reserved-distinguished',
    'ui.inventory.variant-identity-stable',
    'ui.inventory.multi-location-source-visible',
    'ui.inventory.oversell-conflict-reconciled',
    'ui.inventory.backorder-distinct-from-preorder',
    'ui.inventory.bundle-component-dependency-visible',
    'ui.inventory.freshness-visible',
    'ui.inventory.reservation-expiration-visible',
    # marketplace payout
    'ui.payout.gross-net-fee-basis-visible',
    'ui.payout.pending-available-paid-distinguished',
    'ui.payout.destination-identity-visible',
    'ui.payout.currency-conversion-basis-visible',
    'ui.payout.failed-payout-recovery-visible',
    'ui.payout.adjustment-lineage-preserved',
    'ui.payout.reserve-hold-scope-visible',
    'ui.payout.reconciliation-export-consistent',
    # trading order entry
    'ui.trading.side-symbol-venue-bound',
    'ui.trading.quantity-distinct-from-notional',
    'ui.trading.order-type-parameters-complete',
    'ui.trading.estimated-distinct-from-executable-price',
    'ui.trading.market-session-state-visible',
    'ui.trading.partial-fill-lifecycle-visible',
    'ui.trading.cancel-replace-race-reconciled',
    'ui.trading.quote-freshness-visible',
    # portfolio monitoring
    'ui.portfolio.position-quantity-and-value-source-visible',
    'ui.portfolio.price-timestamp-visible',
    'ui.portfolio.settled-distinct-from-unsettled',
    'ui.portfolio.base-currency-visible',
    'ui.portfolio.cost-basis-method-visible',
    'ui.portfolio.corporate-action-pending-state-visible',
    'ui.portfolio.rollup-drilldown-population-consistent',
    'ui.portfolio.zero-distinct-from-unavailable',
    # bank reconciliation
    'ui.reconciliation.statement-period-visible',
    'ui.reconciliation.matched-transaction-identity-stable',
    'ui.reconciliation.split-match-sum-consistent',
    'ui.reconciliation.duplicate-bank-feed-transaction-visible',
    'ui.reconciliation.opening-closing-balance-consistent',
    'ui.reconciliation.lock-state-visible',
    'ui.reconciliation.late-transaction-after-lock-visible',
    'ui.reconciliation.unreconciled-export-consistent',
    # live stream
    'ui.livestream.live-edge-distinct-from-dvr-position',
    'ui.livestream.latency-mode-visible',
    'ui.livestream.reconnect-state-visible',
    'ui.livestream.track-sync-state-visible',
    'ui.livestream.ended-distinct-from-network-failure',
    'ui.livestream.interaction-timestamps-align-with-stream-time',
    'ui.livestream.quality-downgrade-source-visible',
    'ui.livestream.live-caption-availability-visible',
    # conferencing
    'ui.conference.prejoin-device-selection-reflects-active-device',
    'ui.conference.prejoin-mute-camera-state-preserved',
    'ui.conference.participant-identity-distinguishable',
    'ui.conference.network-degradation-visible',
    'ui.conference.screen-share-source-visible',
    'ui.conference.host-cohost-authority-visible',
    'ui.conference.leave-distinct-from-end-for-all',
    'ui.conference.recording-state-visible-to-participants',
    # software delivery pipeline
    'ui.pipeline.environment-target-visible',
    'ui.pipeline.artifact-commit-identity-bound',
    'ui.pipeline.stage-dependency-state-visible',
    'ui.pipeline.approval-bound-to-artifact-version',
    'ui.pipeline.rollback-target-visible',
    'ui.pipeline.canceled-distinct-from-failed',
    'ui.pipeline.partial-rollout-state-visible',
    'ui.pipeline.retry-creates-distinct-attempt-identity',
    # build status and artifacts
    'ui.buildartifact.build-status-distinct-from-artifact-availability',
    'ui.buildartifact.log-chunk-order-stable',
    'ui.buildartifact.retention-expiry-visible',
    'ui.buildartifact.test-shard-aggregation-consistent',
    'ui.buildartifact.flaky-retry-distinguished',
    'ui.buildartifact.cache-hit-not-success-proof',
    'ui.buildartifact.download-checksum-visible',
    'ui.buildartifact.branch-commit-association-stable',
}

UMBRELLA_ONLY = {'nui-internal-product-truth-v13'}


class RuleV13EighthWaveQualityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[1]
        cls.catalog = load_rule_catalog_v13(cls.root)
        cls.by_id = {rule['rule_id']: rule for rule in cls.catalog['rules']}
        cls.provenance = {record['provenance_id']: record for record in cls.catalog['provenance']['records']}

    def test_explicit_failure_classes_exist_without_quota(self):
        self.assertEqual(len(EXPECTED_EIGHTH_WAVE), 192)
        self.assertTrue(EXPECTED_EIGHTH_WAVE <= set(self.by_id), sorted(EXPECTED_EIGHTH_WAVE - set(self.by_id)))
        self.assertFalse(self.catalog['composition']['rule_count_is_quality_target'])
        self.assertFalse({'minimum_rule_count', 'required_rule_count', 'rule_quota'} & set(self.catalog))

    def test_owner_and_verifier_hints_resolve_to_real_skills(self):
        for rid in sorted(EXPECTED_EIGHTH_WAVE & set(self.by_id)):
            rule = self.by_id[rid]
            for slug in rule['owner_hints'] + rule['verifier_hints']:
                self.assertTrue((self.root / 'skills' / slug / 'SKILL.md').is_file(), (rid, slug))

    def test_provenance_is_specific_resolved_and_not_emerging_only(self):
        for rid in sorted(EXPECTED_EIGHTH_WAVE & set(self.by_id)):
            pids = set(self.by_id[rid]['provenance_ids'])
            self.assertTrue(pids <= set(self.provenance), (rid, pids - set(self.provenance)))
            self.assertNotEqual(pids, UMBRELLA_ONLY, rid)
            evidence_classes = {self.provenance[pid]['evidence_class'] for pid in pids}
            self.assertNotEqual(evidence_classes, {'emerging'}, rid)

    def test_operational_signatures_are_distinct(self):
        seen = {}
        for rid in sorted(EXPECTED_EIGHTH_WAVE & set(self.by_id)):
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
