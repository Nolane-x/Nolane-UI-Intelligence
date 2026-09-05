import unittest
from pathlib import Path

from nolane_ui.rules_v13.catalog import load_rule_catalog_v13
from nolane_ui.rules_v13.similarity import audit_catalog_similarity

EXPECTED_SEVENTH_WAVE = {
    # audit logs
    'ui.audit.event-actor-identity-preserved',
    'ui.audit.event-target-scope-visible',
    'ui.audit.timestamp-timezone-and-ordering-visible',
    'ui.audit.before-after-value-diff-preserved',
    'ui.audit.filter-export-scope-consistent',
    'ui.audit.pagination-does-not-drop-events',
    'ui.audit.redaction-preserves-event-meaning',
    'ui.audit.correlation-identity-stable-across-views',
    # approvals
    'ui.approval.decision-bound-to-request-version',
    'ui.approval.approver-authority-current-at-decision',
    'ui.approval.delegation-source-visible',
    'ui.approval.rejection-reason-preserved',
    'ui.approval.multi-stage-order-and-gate-state-visible',
    'ui.approval.concurrent-decisions-reconciled',
    'ui.approval.withdrawal-invalidates-pending-actions',
    'ui.approval.bulk-mixed-outcomes-map-requests',
    # sharing
    'ui.sharing.link-scope-visible-before-copy',
    'ui.sharing.expiration-effective-state-visible',
    'ui.sharing.revoked-link-not-presented-active',
    'ui.sharing.audience-preview-resolves-groups',
    'ui.sharing.public-vs-organization-boundary-explicit',
    'ui.sharing.download-permission-distinct-from-view',
    'ui.sharing.reshare-inheritance-visible',
    'ui.sharing.native-handoff-result-reconciled',
    # versioning / restore
    'ui.versioning.restore-target-version-previewed',
    'ui.versioning.restore-preserves-newer-history',
    'ui.versioning.concurrent-edit-version-conflict-visible',
    'ui.versioning.rename-move-preserves-history-continuity',
    'ui.versioning.lock-owner-and-expiry-visible',
    'ui.versioning.trash-retention-and-deletion-state-visible',
    'ui.versioning.compare-version-identities-stable',
    'ui.versioning.autosave-vs-published-boundary-explicit',
    # diffs / review
    'ui.diff.baseline-and-head-identities-visible',
    'ui.diff.moved-content-not-double-counted',
    'ui.diff.whitespace-normalization-declared',
    'ui.diff.collapsed-sections-still-count-changes',
    'ui.diff.binary-unrenderable-change-disclosed',
    'ui.diff.hunk-context-stable-across-navigation',
    'ui.diff.review-stale-after-base-update',
    'ui.diff.applied-change-result-reconciled',
    # operational inbox
    'ui.inbox.unread-state-authority-consistent',
    'ui.inbox.assignment-owner-visible',
    'ui.inbox.snooze-wake-time-visible',
    'ui.inbox.filter-count-consistent-with-items',
    'ui.inbox.bulk-action-partial-result-maps-items',
    'ui.inbox.duplicate-items-deduplicated-by-identity',
    'ui.inbox.priority-sort-basis-visible',
    'ui.inbox.resolution-retention-policy-visible',
    # tree navigation
    'ui.tree.expansion-state-distinct-from-selection',
    'ui.tree.keyboard-hierarchy-navigation-complete',
    'ui.tree.lazy-child-loading-state-visible',
    'ui.tree.moved-node-preserves-focus-identity',
    'ui.tree.invalid-parent-cycle-prevented',
    'ui.tree.breadcrumb-and-tree-path-consistent',
    'ui.tree.virtualized-node-position-semantic',
    'ui.tree.parent-child-selection-scope-explicit',
    # list / pagination
    'ui.list.pagination-stable-under-concurrent-insert',
    'ui.list.page-size-change-preserves-context',
    'ui.list.sort-key-and-direction-visible',
    'ui.list.filter-reset-state-explicit',
    'ui.list.infinite-scroll-end-and-retry-visible',
    'ui.list.selection-across-pages-scope-explicit',
    'ui.list.filtered-empty-distinct-from-dataset-empty',
    'ui.list.deep-link-restores-list-context',
    # loading / error / feedback states
    'ui.feedback.loading-preserves-known-content-truth',
    'ui.feedback.skeleton-does-not-imply-false-data',
    'ui.feedback.progress-determinate-only-with-measured-total',
    'ui.feedback.retry-does-not-duplicate-operation',
    'ui.feedback.error-bound-to-failed-operation',
    'ui.feedback.optimistic-pending-state-visible',
    'ui.feedback.background-completion-reconciles-view',
    'ui.feedback.toast-not-sole-consequential-record',
    # overlays / menus / tooltips
    'ui.overlay.trigger-anchor-relationship-preserved',
    'ui.overlay.focus-returns-to-logical-trigger',
    'ui.overlay.escape-closes-topmost-layer-only',
    'ui.overlay.nested-layer-order-preserves-ownership',
    'ui.overlay.viewport-collision-does-not-hide-content',
    'ui.overlay.tooltip-keyboard-parity',
    'ui.overlay.context-menu-target-remains-stable',
    'ui.overlay.cascading-menu-intent-tolerates-pointer-path',
    # charts / time series
    'ui.chart.axis-scale-and-baseline-visible',
    'ui.chart.legend-series-mapping-stable',
    'ui.chart.missing-data-gap-not-rendered-as-zero',
    'ui.chart.aggregation-window-visible',
    'ui.chart.cross-filter-source-and-scope-visible',
    'ui.chart.tooltip-value-time-basis-visible',
    'ui.chart.zoom-selection-reset-state-visible',
    'ui.chart.nonvisual-equivalent-uses-same-data',
    # calendar / date-time
    'ui.calendar.all-day-distinct-from-timed-event',
    'ui.calendar.calendar-system-visible-when-non-gregorian',
    'ui.calendar.disabled-date-reason-available',
    'ui.calendar.range-end-inclusion-semantics-visible',
    'ui.calendar.recurring-instance-distinct-from-series-edit',
    'ui.calendar.availability-slot-staleness-visible',
    'ui.calendar.week-start-and-week-number-follow-locale',
    'ui.calendar.date-time-picker-preserves-entered-zone-context',
    # address / contact entry
    'ui.contact.country-selection-drives-address-schema',
    'ui.contact.postal-code-not-universally-required',
    'ui.contact.phone-country-code-distinct-from-national-number',
    'ui.contact.phone-extension-preserved',
    'ui.contact.person-name-order-not-hardcoded',
    'ui.contact.single-name-person-supported',
    'ui.contact.autofill-review-before-consequential-submit',
    'ui.contact.normalization-does-not-destroy-user-meaning',
    # verification / recovery codes
    'ui.verification.code-expiry-state-visible',
    'ui.verification.resend-challenge-replacement-semantics-visible',
    'ui.verification.code-entry-supports-paste-and-autofill',
    'ui.verification.attempt-lock-state-visible-without-false-countdown',
    'ui.verification.recovery-code-consumption-one-time-visible',
    'ui.verification.recovery-code-export-confirmation',
    'ui.verification.device-switch-preserves-challenge-context',
    'ui.verification.multiple-active-challenges-bound-to-purpose',
    # scanning
    'ui.scanning.camera-permission-recovery-path',
    'ui.scanning.symbology-mismatch-explained',
    'ui.scanning.duplicate-scan-debounced-by-result-identity',
    'ui.scanning.scan-result-reviewed-before-consequential-action',
    'ui.scanning.document-crop-preview-before-save',
    'ui.scanning.multi-page-order-preserved',
    'ui.scanning.low-quality-capture-recapture-path',
    'ui.scanning.sensitive-capture-retention-visible',
    # document signing
    'ui.signing.signer-identity-and-document-version-visible',
    'ui.signing.required-signature-fields-complete-before-submit',
    'ui.signing.signing-order-and-next-signer-visible',
    'ui.signing.decline-state-finality-visible',
    'ui.signing.expired-signing-link-recovery',
    'ui.signing.document-change-invalidates-prior-signatures',
    'ui.signing.signed-artifact-download-integrity-visible',
    'ui.signing.witness-and-counterparty-roles-distinct',
    # links / deep links
    'ui.link.deep-link-target-scope-visible',
    'ui.link.broken-link-has-context-preserving-fallback',
    'ui.link.external-destination-disclosed-before-context-loss',
    'ui.link.single-use-link-consumption-visible',
    'ui.link.signed-link-expiry-state-visible',
    'ui.link.copy-uses-canonical-shareable-url',
    'ui.link.mobile-app-web-fallback-preserves-task',
    'ui.link.fragment-navigation-focuses-logical-target',
    # file browser
    'ui.filebrowser.current-directory-identity-visible',
    'ui.filebrowser.selection-survives-benign-sort-change',
    'ui.filebrowser.inline-rename-validation-preserves-name',
    'ui.filebrowser.move-conflict-resolution-explicit',
    'ui.filebrowser.preview-bound-to-current-version',
    'ui.filebrowser.hidden-item-state-visible-when-enabled',
    'ui.filebrowser.permission-denied-folder-distinct-from-empty',
    'ui.filebrowser.multi-select-command-scope-visible',
    # incident response
    'ui.incident.severity-current-state-visible',
    'ui.incident.responder-role-handoff-visible',
    'ui.incident.timeline-event-source-and-time-visible',
    'ui.incident.hypothesis-distinct-from-confirmed-finding',
    'ui.incident.acknowledged-alert-owner-visible',
    'ui.incident.runbook-step-execution-state-visible',
    'ui.incident.merged-incident-identity-preserved',
    'ui.incident.postmortem-linked-to-closed-incident',
    # preview / publish
    'ui.preview.preview-bound-to-source-revision',
    'ui.preview.draft-distinct-from-published-state',
    'ui.preview.environment-expiry-visible',
    'ui.preview.preview-data-isolation-visible',
    'ui.preview.publish-diff-visible-before-commit',
    'ui.preview.stale-after-source-change-visible',
    'ui.preview.failed-publish-retains-draft',
    'ui.preview.rollback-target-release-visible',
}

UMBRELLA_ONLY = {'nui-internal-product-truth-v13'}


class RuleV13SeventhWaveQualityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[1]
        cls.catalog = load_rule_catalog_v13(cls.root)
        cls.by_id = {rule['rule_id']: rule for rule in cls.catalog['rules']}
        cls.provenance = {record['provenance_id']: record for record in cls.catalog['provenance']['records']}

    def test_explicit_failure_classes_exist_without_quota(self):
        self.assertEqual(len(EXPECTED_SEVENTH_WAVE), 160)
        self.assertTrue(EXPECTED_SEVENTH_WAVE <= set(self.by_id), sorted(EXPECTED_SEVENTH_WAVE - set(self.by_id)))
        self.assertFalse(self.catalog['composition']['rule_count_is_quality_target'])
        self.assertFalse({'minimum_rule_count', 'required_rule_count', 'rule_quota'} & set(self.catalog))

    def test_owner_and_verifier_hints_resolve_to_real_skills(self):
        for rid in sorted(EXPECTED_SEVENTH_WAVE):
            rule = self.by_id[rid]
            for slug in rule['owner_hints'] + rule['verifier_hints']:
                self.assertTrue((self.root / 'skills' / slug / 'SKILL.md').is_file(), (rid, slug))

    def test_provenance_is_specific_resolved_and_not_emerging_only(self):
        for rid in sorted(EXPECTED_SEVENTH_WAVE):
            pids = set(self.by_id[rid]['provenance_ids'])
            self.assertTrue(pids <= set(self.provenance), (rid, pids - set(self.provenance)))
            self.assertNotEqual(pids, UMBRELLA_ONLY, rid)
            evidence_classes = {self.provenance[pid]['evidence_class'] for pid in pids}
            self.assertNotEqual(evidence_classes, {'emerging'}, rid)

    def test_operational_signatures_are_distinct(self):
        seen = {}
        for rid in sorted(EXPECTED_SEVENTH_WAVE):
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
