import unittest
from pathlib import Path

from nolane_ui.rules_v13.catalog import load_rule_catalog_v13
from nolane_ui.rules_v13.similarity import audit_catalog_similarity

EXPECTED_SIXTH_WAVE = {
    # roles / permissions
    'ui.roles.assignment-shows-effective-scope',
    'ui.roles.inheritance-source-visible',
    'ui.roles.change-preview-shows-capability-delta',
    'ui.roles.bulk-update-partial-failure-maps-members',
    'ui.roles.last-admin-removal-protected',
    'ui.roles.temporary-grant-expiry-visible',
    'ui.roles.revoked-action-stops-before-authoritative-commit',
    'ui.roles.resource-request-bound-to-target',
    # settings / preferences
    'ui.settings.saved-state-distinct-from-effective',
    'ui.settings.sync-bound-to-account',
    'ui.settings.device-conflict-resolution-visible',
    'ui.settings.reset-scope-preview',
    'ui.settings.dependency-disable-explains-consequence',
    'ui.settings.autosave-failure-visible',
    'ui.settings.workspace-vs-global-scope-visible',
    'ui.settings.requires-restart-state-visible',
    # commands / keyboard
    'ui.commands.shortcut-conflict-resolved-by-context',
    'ui.commands.disabled-command-explains-precondition',
    'ui.commands.target-scope-visible-before-execution',
    'ui.commands.palette-refreshes-after-context-change',
    'ui.commands.destructive-shortcut-has-recovery-boundary',
    'ui.commands.chord-timeout-does-not-trigger-partial',
    'ui.commands.remap-collision-warning',
    'ui.commands.assistive-technology-reserved-key-not-captured',
    # dashboards / monitoring
    'ui.dashboard.metric-time-window-visible',
    'ui.dashboard.stale-data-state-visible',
    'ui.dashboard.alert-threshold-context-visible',
    'ui.dashboard.drilldown-preserves-filter-context',
    'ui.dashboard.partial-aggregate-distinct-from-complete',
    'ui.dashboard.refresh-failure-not-rendered-as-zero',
    'ui.dashboard.permission-redaction-distinct-from-no-data',
    'ui.dashboard.live-pause-state-visible',
    # download / export
    'ui.download.export-snapshot-time-visible',
    'ui.download.resume-preserves-file-identity',
    'ui.download.generated-artifact-expiry-visible',
    'ui.download.partial-export-scope-visible',
    'ui.download.lossy-format-warning-before-generation',
    'ui.download.retry-reuses-logical-export-job',
    'ui.download.filename-collision-does-not-silent-overwrite',
    'ui.download.expired-link-has-regeneration-path',
    # upload / import
    'ui.upload.retry-preserves-upload-identity',
    'ui.upload.batch-partial-failure-maps-files',
    'ui.upload.duplicate-target-does-not-silent-overwrite',
    'ui.upload.mapping-missing-required-fields-visible',
    'ui.upload.preview-distinct-from-commit',
    'ui.upload.cancel-stops-or-marks-server-processing',
    'ui.upload.scan-processing-distinct-from-ready',
    'ui.upload.account-scope-revalidated-before-attach',
    # voice / audio input
    'ui.voice.listening-state-visible',
    'ui.voice.partial-transcript-distinct-from-final',
    'ui.voice.stop-recording-boundary-visible',
    'ui.voice.input-device-switch-reconciles-recording',
    'ui.voice.wake-word-active-scope-visible',
    'ui.voice.echo-playback-not-treated-as-user-speech',
    'ui.voice.recognition-language-visible',
    'ui.voice.destructive-command-requires-explicit-confirmation',
    # TV / remote
    'ui.tv.focus-visible-at-viewing-distance',
    'ui.tv.directional-navigation-no-focus-trap',
    'ui.tv.back-action-follows-navigation-hierarchy',
    'ui.tv.long-press-distinct-from-press',
    'ui.tv.remote-disconnect-recovery-visible',
    'ui.tv.critical-controls-within-safe-area',
    'ui.tv.control-timeout-does-not-hide-focused-action',
    'ui.tv.modal-close-restores-logical-focus',
    # spatial / XR
    'ui.spatial.recenter-preserves-world-target-meaning',
    'ui.spatial.safety-boundary-never-obscured',
    'ui.spatial.anchor-loss-state-visible',
    'ui.spatial.near-far-transfer-preserves-target',
    'ui.spatial.dom-overlay-input-ownership-explicit',
    'ui.spatial.locomotion-mode-disclosed-before-motion',
    'ui.spatial.gaze-hand-ambiguity-requires-confirmation',
    'ui.spatial.distance-scaling-preserves-legibility',
    # wearable / glanceable
    'ui.wearable.glance-surface-minimizes-sensitive-disclosure',
    'ui.wearable.stale-complication-state-visible',
    'ui.wearable.rotary-navigation-keeps-focus-identity',
    'ui.wearable.quick-action-confirmation-matches-consequence',
    'ui.wearable.phone-handoff-preserves-task-context',
    'ui.wearable.truncation-does-not-invert-status',
    'ui.wearable.live-session-stop-boundary-visible',
    'ui.wearable.offline-capability-visible-before-action',
    # print / output
    'ui.print.preview-matches-selected-range',
    'ui.print.current-printer-target-visible',
    'ui.print.submitted-distinct-from-printer-accepted',
    'ui.print.partial-page-failure-retryable',
    'ui.print.layout-overflow-visible-before-submit',
    'ui.print.color-mode-effective-state-visible',
    'ui.print.confidential-output-destination-warning',
    'ui.print.cancelled-distinct-from-completed',
    # multi-step workflow
    'ui.workflow.branch-change-invalidates-dependent-steps',
    'ui.workflow.prior-valid-data-survives-step-navigation',
    'ui.workflow.review-summary-matches-effective-submission',
    'ui.workflow.resume-restores-step-and-draft',
    'ui.workflow.back-navigation-does-not-repeat-side-effects',
    'ui.workflow.skipped-step-reason-visible-when-relevant',
    'ui.workflow.async-validation-blocks-only-dependent-progress',
    'ui.workflow.final-submit-idempotent',
    # queues / jobs
    'ui.jobs.queued-running-complete-distinct',
    'ui.jobs.cancel-requested-distinct-from-cancelled',
    'ui.jobs.retry-creates-attempt-under-same-job',
    'ui.jobs.priority-change-effective-state-visible',
    'ui.jobs.dependency-blocked-state-visible',
    'ui.jobs.partial-output-labelled-before-completion',
    'ui.jobs.retry-preserves-effective-parameters',
    'ui.jobs.queue-position-does-not-invent-precision',
    # realtime feeds
    'ui.realtime.reconnect-gap-visible',
    'ui.realtime.out-of-order-events-reconciled',
    'ui.realtime.duplicate-event-identity-deduplicated',
    'ui.realtime.paused-feed-not-presented-as-live',
    'ui.realtime.backfill-distinct-from-live-arrival',
    'ui.realtime.optimistic-event-rejection-reconciled',
    'ui.realtime.permission-loss-stops-authoritative-stream',
    'ui.realtime.order-not-derived-from-untrusted-client-clock',
    # design-system runtime
    'ui.design-system.invalid-token-fallback-not-silent',
    'ui.design-system.theme-switch-clears-stale-mode',
    'ui.design-system.deprecated-token-use-diagnosable',
    'ui.design-system.unsupported-component-state-rejected',
    'ui.design-system.consumer-override-scope-visible',
    'ui.design-system.version-mismatch-diagnosable',
    'ui.design-system.semantic-token-type-preserved',
    'ui.design-system.breaking-change-migration-gated',
    # localization / content truth
    'ui.locale.fallback-language-visible',
    'ui.locale.mixed-language-content-labelled',
    'ui.locale.plural-category-derived-from-locale',
    'ui.locale.dynamic-bidi-content-isolated',
    'ui.locale.locale-switch-preserves-task-state',
    'ui.locale.untranslated-placeholder-not-shipped',
    'ui.locale.translation-staleness-visible',
    'ui.locale.truncation-preserves-distinguishing-content',
}

UMBRELLA_ONLY = {'nui-internal-product-truth-v13'}


class RuleV13SixthWaveQualityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[1]
        cls.catalog = load_rule_catalog_v13(cls.root)
        cls.by_id = {rule['rule_id']: rule for rule in cls.catalog['rules']}
        cls.provenance = {record['provenance_id']: record for record in cls.catalog['provenance']['records']}

    def test_explicit_failure_classes_exist_without_quota(self):
        self.assertEqual(len(EXPECTED_SIXTH_WAVE), 128)
        self.assertTrue(EXPECTED_SIXTH_WAVE <= set(self.by_id), sorted(EXPECTED_SIXTH_WAVE - set(self.by_id)))
        self.assertFalse(self.catalog['composition']['rule_count_is_quality_target'])
        self.assertFalse({'minimum_rule_count', 'required_rule_count', 'rule_quota'} & set(self.catalog))

    def test_owner_and_verifier_hints_resolve_to_real_skills(self):
        for rid in sorted(EXPECTED_SIXTH_WAVE):
            rule = self.by_id[rid]
            for slug in rule['owner_hints'] + rule['verifier_hints']:
                self.assertTrue((self.root / 'skills' / slug / 'SKILL.md').is_file(), (rid, slug))

    def test_provenance_is_specific_resolved_and_not_emerging_only(self):
        for rid in sorted(EXPECTED_SIXTH_WAVE):
            pids = set(self.by_id[rid]['provenance_ids'])
            self.assertTrue(pids <= set(self.provenance), (rid, pids - set(self.provenance)))
            self.assertNotEqual(pids, UMBRELLA_ONLY, rid)
            evidence_classes = {self.provenance[pid]['evidence_class'] for pid in pids}
            self.assertNotEqual(evidence_classes, {'emerging'}, rid)

    def test_operational_signatures_are_distinct(self):
        seen = {}
        for rid in sorted(EXPECTED_SIXTH_WAVE):
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
