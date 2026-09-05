"""V13 seventh-wave independently authored rules for feedback states."""
from __future__ import annotations

from ._capabilities import interaction_caps


FEEDBACK_STATE_RULES_V13 = [{'rule_id': 'ui.feedback.loading-preserves-known-content-truth',
  'domain': 'feedback',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Loading refreshes must preserve known content without presenting it as freshly confirmed',
  'statement': 'When previously loaded content remains visible during a refresh, the interface should '
               'distinguish that cached or prior state from the still-pending updated result.',
  'intent': 'Avoid replacing useful context with blankness while also avoiding the false implication that '
            'old data has just been revalidated.',
  'applies_when': ['A screen refreshes data that was already loaded successfully and can safely continue '
                   'showing the prior value during the request.'],
  'does_not_apply_when': [],
  'failure_modes': ['The screen either clears known content unnecessarily or leaves old values unchanged '
                    'with no pending/stale indicator while a consequential refresh is underway.'],
  'user_impacts': ['Users lose context or make decisions assuming stale values are current.'],
  'observables': ['Load data, trigger a delayed refresh after changing server state, and inspect content '
                  'plus status before the response arrives.'],
  'falsifiers': ['Prior content may remain readable but the UI communicates refresh/pending status until '
                 'authoritative new state succeeds or fails.'],
  'repairs': ['Separate data value state from fetch lifecycle so cached content can coexist with explicit '
              'refreshing or stale metadata.'],
  'exceptions': [],
  'verification': ['Test successful, failed, and cancelled refreshes, verifying known data and freshness '
                   'state reconcile independently.'],
  'owner_hints': ['designing-empty-loading-error-states'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-feedback-state-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.feedback.skeleton-does-not-imply-false-data',
  'domain': 'feedback',
  'class': 'mechanical',
  'severity': 'moderate',
  'enforcement': 'warn',
  'title': 'Skeleton placeholders must not encode misleading values or structure that users can mistake for '
           'real content',
  'statement': 'Loading skeletons should communicate layout occupancy without showing realistic numbers, '
               'status colors, names, or chart shapes that imply data already known to the product.',
  'intent': 'Keep placeholders perceptually distinct from authoritative business or personal information.',
  'applies_when': ['A loading surface uses skeletons or shimmer placeholders before content arrives.'],
  'does_not_apply_when': [],
  'failure_modes': ['The placeholder includes realistic monetary values, avatar initials, success colors, or '
                    'chart trends that can be interpreted as actual state for a moment.'],
  'user_impacts': ['Users can briefly act on invented status or experience jarring reversals that undermine '
                   'trust in high-stakes data.'],
  'observables': ['Throttle loading on dashboards and records and inspect the placeholder at normal zoom, '
                  'reduced motion, and screen capture.'],
  'falsifiers': ['The placeholder remains clearly non-data-bearing and does not assign semantic status or '
                 'plausible values before the source resolves.'],
  'repairs': ['Use neutral geometry tied to layout needs rather than fabricated domain values or meaningful '
              'semantic colors.'],
  'exceptions': [],
  'verification': ['Test long loading delays and error transitions, verifying no placeholder content can '
                   'reasonably be read as a confirmed record.'],
  'owner_hints': ['designing-skeleton-loading'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-feedback-state-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.feedback.progress-determinate-only-with-measured-total',
  'domain': 'feedback',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Determinate progress must be used only when a meaningful total or completion estimate is '
           'available',
  'statement': 'A percentage or bounded progress bar should represent measured work against a credible '
               'total; unknown-duration work must not invent precise percentages merely to appear '
               'responsive.',
  'intent': 'Prevent false precision from distorting user expectations about completion time or remaining '
            'work.',
  'applies_when': ['Long-running operations expose progress feedback while the backend may or may not know '
                   'total work.'],
  'does_not_apply_when': [],
  'failure_modes': ['The UI advances through arbitrary percentages or stalls at 99% because the displayed '
                    'progress is disconnected from measurable completed units.'],
  'user_impacts': ['Users may wait based on a misleading estimate, abandon healthy work, or suspect the '
                   'process is frozen.'],
  'observables': ['Compare displayed progress with backend completed/total units for operations with known '
                  'and unknown workload sizes.'],
  'falsifiers': ['Determinate progress has a documented measurable basis; otherwise the UI uses '
                 'indeterminate or milestone-based feedback without fabricated precision.'],
  'repairs': ['Expose real unit or phase progress from the operation and choose the visual progress model '
              'from that capability.'],
  'exceptions': [],
  'verification': ['Run operations with varying sizes and unknown totals, verifying progress remains '
                   'monotonic only when the underlying measurement supports it.'],
  'owner_hints': ['designing-latency-and-progressive-feedback'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-feedback-state-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.feedback.retry-does-not-duplicate-operation',
  'domain': 'feedback',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Retry controls must not create duplicate authoritative operations after ambiguous network '
           'failure',
  'statement': 'When the client cannot tell whether an operation committed before a connection failed, retry '
               'must reconcile or reuse an idempotent operation identity instead of blindly submitting a '
               'second action.',
  'intent': 'Keep recovery from turning one intended purchase, message, job, or mutation into two.',
  'applies_when': ['A consequential action can time out or lose its response after the server may already '
                   'have accepted it.'],
  'does_not_apply_when': [],
  'failure_modes': ['The error UI offers Retry that posts a new mutation with no idempotency or status '
                    'check, producing duplicate authoritative results.'],
  'user_impacts': ['Users can be charged twice, send duplicate communications, or create duplicate work '
                   'because they followed the offered recovery path.'],
  'observables': ['Delay or drop the success response after server commit, invoke retry, and inspect '
                  'authoritative operation identities and final records.'],
  'falsifiers': ['Retry either resolves the original operation or safely reuses its logical identity so one '
                 'user intent cannot commit twice.'],
  'repairs': ['Persist an idempotency or operation key across ambiguous retries and reconcile final server '
              'state before creating a new intent.'],
  'exceptions': [],
  'verification': ['Inject failures before and after commit boundaries, verifying repeated retry clicks '
                   'never multiply the authoritative operation.'],
  'owner_hints': ['designing-empty-loading-error-states'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-feedback-state-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.feedback.error-bound-to-failed-operation',
  'domain': 'feedback',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Error feedback must identify which operation failed when several actions are in flight',
  'statement': 'When concurrent saves, uploads, refreshes, or commands can fail independently, each error '
               'must stay associated with the affected operation or resource instead of appearing as an '
               'ambiguous global failure.',
  'intent': 'Give users a correct recovery target in interfaces with overlapping asynchronous work.',
  'applies_when': ['The screen can launch multiple independent async operations before earlier ones finish.'],
  'does_not_apply_when': [],
  'failure_modes': ['A generic banner says “Something went wrong” after one of several requests fails and '
                    'provides a retry that may rerun the wrong operation.'],
  'user_impacts': ['Users can repeat successful work, lose failed changes, or misunderstand which resource '
                   'remains stale.'],
  'observables': ['Start several operations, force only one to fail, and inspect error placement, '
                  'identifiers, and retry behavior.'],
  'falsifiers': ['The failed operation or resource is identifiable, successful siblings retain their state, '
                 'and recovery targets only the affected intent.'],
  'repairs': ['Track errors by logical operation identity and render local or aggregated feedback that '
              'preserves that mapping.'],
  'exceptions': [],
  'verification': ['Force different subsets of concurrent work to fail, verifying retries and dismissals '
                   'never alter successful sibling outcomes.'],
  'owner_hints': ['designing-empty-loading-error-states'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-feedback-state-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.feedback.optimistic-pending-state-visible',
  'domain': 'feedback',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Optimistic updates must remain visibly pending until authoritative acceptance',
  'statement': 'When the UI applies an optimistic result before the server confirms it, the pending state '
               'must remain distinguishable from committed state wherever the distinction changes user '
               'decisions.',
  'intent': 'Preserve the speed benefit of optimism without misrepresenting provisional state as final '
            'truth.',
  'applies_when': ['A mutation is reflected immediately in the interface before the authoritative service '
                   'accepts or rejects it.'],
  'does_not_apply_when': [],
  'failure_modes': ['The optimistic value looks fully committed with no pending marker, then silently snaps '
                    'back after rejection or conflict.'],
  'user_impacts': ['Users can act on a state that never became authoritative and may not notice rollback.'],
  'observables': ['Delay and reject optimistic mutations while opening related views or navigating away and '
                  'back.'],
  'falsifiers': ['Pending optimistic state is identifiable until confirmation and rejection produces an '
                 'explicit reconciliation rather than an unexplained reversal.'],
  'repairs': ['Track optimistic records with operation identity and pending/error lifecycle separate from '
              'committed server state.'],
  'exceptions': [],
  'verification': ['Exercise success, validation rejection, conflict, and timeout, verifying provisional '
                   'state is never indistinguishable from final authority during uncertainty.'],
  'owner_hints': ['designing-inline-status-feedback'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-feedback-state-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.feedback.background-completion-reconciles-view',
  'domain': 'feedback',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Background completion must reconcile stale foreground views without requiring users to '
           'rediscover the result',
  'statement': 'When work finishes outside the currently active interaction, returning to a related surface '
               'must reflect the completed outcome or clearly indicate that a refresh is required.',
  'intent': 'Close the gap between background jobs and foreground state so users do not repeat work that '
            'already finished.',
  'applies_when': ['An upload, export, analysis, sync, or other operation can complete while the user is on '
                   'another route, tab, or device state.'],
  'does_not_apply_when': [],
  'failure_modes': ['The original screen still shows “processing” indefinitely after background completion '
                    'and allows a duplicate start action.'],
  'user_impacts': ['Users can create redundant work or assume a successful operation failed because the '
                   'foreground view never reconciles.'],
  'observables': ['Start work, leave the route until it completes, then return through history, deep link, '
                  'and notification continuation.'],
  'falsifiers': ['The surface resolves the latest authoritative job state and disables or reframes actions '
                 'that would duplicate completed work.'],
  'repairs': ['Subscribe to or refetch durable operation state on relevant route activation and map '
              'completion back to its originating resource.'],
  'exceptions': [],
  'verification': ['Complete jobs while clients are suspended or offline, then resume and verify all '
                   'relevant views converge without manual cache clearing.'],
  'owner_hints': ['designing-latency-and-progressive-feedback'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-feedback-state-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.feedback.toast-not-sole-consequential-record',
  'domain': 'feedback',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Consequential outcomes must not exist only in transient toast notifications',
  'statement': 'Success, failure, or warning information that affects money, access, data loss, or required '
               'next steps must remain discoverable after the toast disappears.',
  'intent': 'Prevent critical outcome evidence from vanishing before users can read or act on it.',
  'applies_when': ['A consequential action uses toast feedback and the result matters beyond a momentary '
                   'acknowledgement.'],
  'does_not_apply_when': [],
  'failure_modes': ['The only indication that a payment failed, access was denied, or deletion was partial '
                    'disappears automatically with no durable state in the affected surface.'],
  'user_impacts': ['Users can miss required recovery, assume success, or have no way to review what happened '
                   'after distraction.'],
  'observables': ['Trigger consequential success and failure, allow toasts to time out, navigate away and '
                  'back, then search for the outcome in the affected workflow.'],
  'falsifiers': ['The final state or durable activity/history remains available independently of the '
                 'transient toast and carries the necessary next action.'],
  'repairs': ['Use toasts as supplemental interruption feedback while persisting consequential outcome state '
              'in the resource, workflow, or activity surface.'],
  'exceptions': [],
  'verification': ['Test screen-reader timing, background tab delivery, and missed toasts, confirming users '
                   'can still recover the full outcome later.'],
  'owner_hints': ['designing-toast-feedback'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-feedback-state-owners-v13'],
  'status': 'active'}]

__all__ = ["FEEDBACK_STATE_RULES_V13"]
