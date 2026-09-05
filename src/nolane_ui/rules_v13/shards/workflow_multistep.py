"""V13 sixth-wave rules; all operational prose is independently authored."""
from __future__ import annotations

WORKFLOW_MULTISTEP_RULES_V13 = [{'rule_id': 'ui.workflow.branch-change-invalidates-dependent-steps',
  'domain': 'workflow',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Changing an earlier workflow branch must invalidate dependent later-step answers explicitly',
  'statement': 'If a choice in an earlier step changes which later fields, approvals, calculations, or documents are '
               'applicable, stale answers from the previous branch must not silently remain effective.',
  'intent': 'Prevent multi-step workflows from submitting contradictory state assembled from two different branches '
            'of the decision tree.',
  'applies_when': ['A wizard or multi-step flow conditionally changes later questions, requirements, calculations, '
                   'or steps based on an earlier answer.'],
  'does_not_apply_when': [],
  'failure_modes': ['The user changes a branching answer and hidden values from the old branch remain in the final '
                    'submission without review.'],
  'user_impacts': ['The resulting request can contain invalid, contradictory, or unauthorized information that the '
                   'visible workflow no longer represents.'],
  'observables': ['Complete one branch, return to the branching step, choose another path, and inspect hidden state, '
                  'review summary, and submission payload.'],
  'falsifiers': ['Dependent stale values are cleared, marked invalid, or deliberately preserved with explicit review '
                 'when the branch changes.'],
  'repairs': ['Track dependency relationships between steps and invalidate downstream state from the changed branch '
              'before the workflow can advance.'],
  'exceptions': [],
  'verification': ['Switch among every branch after entering downstream data and confirm only values applicable to '
                   'the active branch survive into review and commit.'],
  'owner_hints': ['designing-multi-step-forms'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-workflow-multistep-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.workflow.prior-valid-data-survives-step-navigation',
  'domain': 'workflow',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Navigating between workflow steps must preserve still-valid user input',
  'statement': 'Moving backward, forward, or between completed steps must not clear valid answers merely because a '
               'component unmounted or a different step rendered.',
  'intent': 'Respect the user’s investment in multi-step entry while still allowing explicit invalidation when '
            'requirements actually change.',
  'applies_when': ['A multi-step workflow stores draft values across page, route, component, or modal transitions '
                   'before final submission.'],
  'does_not_apply_when': [],
  'failure_modes': ['Returning to a prior step shows blank or default fields even though no product rule invalidated '
                    'the previously accepted values.'],
  'user_impacts': ['Users must re-enter information and may abandon long flows or accidentally submit different '
                   'values on the second attempt.'],
  'observables': ['Enter valid values, move through several steps, navigate backward and forward, and compare '
                  'retained draft state with the original entries.'],
  'falsifiers': ['Valid values persist across navigation and are cleared only by explicit reset, branch '
                 'invalidation, expiry, or a documented security boundary.'],
  'repairs': ['Persist workflow draft state outside ephemeral step components and apply targeted invalidation rules '
              'rather than remount-based reset.'],
  'exceptions': [],
  'verification': ['Test browser Back, in-flow Back, stepper navigation, refresh recovery, and validation errors and '
                   'confirm still-valid data remains intact.'],
  'owner_hints': ['designing-multi-step-forms'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-workflow-multistep-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.workflow.review-summary-matches-effective-submission',
  'domain': 'workflow',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Final workflow review must reflect the exact values that will be submitted',
  'statement': 'A review or confirmation step must render from the same effective state used for final submission, '
               'including computed values, defaults, attachments, branch choices, and server-normalized data.',
  'intent': 'Make review a genuine decision boundary rather than a stale visual copy disconnected from the actual '
            'request payload.',
  'applies_when': ['A consequential multi-step workflow presents a summary or review screen before the authoritative '
                   'final submission.'],
  'does_not_apply_when': [],
  'failure_modes': ['The summary displays one value while the request payload uses a newer hidden, defaulted, '
                    'normalized, or branch-specific value.'],
  'user_impacts': ['Users can explicitly approve information different from what the system actually submits on '
                   'their behalf.'],
  'observables': ['Mutate state through validation, defaults, async normalization, and back-navigation and compare '
                  'review rendering with the final outgoing payload.'],
  'falsifiers': ['Review content is derived from the effective submission model and any later mutation returns the '
                 'workflow to review before commit.'],
  'repairs': ['Create one canonical submission state and render the review directly from it instead of maintaining a '
              'separate summary snapshot.'],
  'exceptions': [],
  'verification': ['Exercise server normalization, conditional defaults, attachment changes, and last-step edits and '
                   'confirm final payload exactly matches reviewed values.'],
  'owner_hints': ['designing-multi-step-forms'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-workflow-multistep-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.workflow.resume-restores-step-and-draft',
  'domain': 'workflow',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Resuming an interrupted workflow must restore both draft data and the unresolved step context',
  'statement': 'A saved or recoverable multi-step workflow should reopen at the correct unresolved point with its '
               'valid draft state, rather than restarting at step one or dropping users into a summary that assumes '
               'completion.',
  'intent': 'Make long-running flows robust to session interruption, device change, navigation away, or explicit '
            'save-and-return behavior.',
  'applies_when': ['The product supports save-and-resume, draft persistence, interruption recovery, or long-lived '
                   'workflows spanning multiple sessions.'],
  'does_not_apply_when': [],
  'failure_modes': ['Resuming restores some data but loses which step was unresolved, or restores the step but '
                    'silently drops previously valid draft values.'],
  'user_impacts': ['Users can repeat work, skip unfinished requirements, or submit a draft whose visible progress no '
                   'longer matches its stored state.'],
  'observables': ['Interrupt the workflow at several steps with partial valid data, then resume from history, link, '
                  'and another session and inspect restoration state.'],
  'falsifiers': ['Resume restores the latest valid draft plus a step position derived from unresolved requirements '
                 'and current branch rules.'],
  'repairs': ['Persist workflow draft, branch state, validation generation, and progress markers together under one '
              'durable workflow identity.'],
  'exceptions': [],
  'verification': ['Resume after logout, timeout, device switch, schema change, and ordinary navigation and confirm '
                   'stale progress is reconciled rather than blindly replayed.'],
  'owner_hints': ['designing-multi-step-forms'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-workflow-multistep-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.workflow.back-navigation-does-not-repeat-side-effects',
  'domain': 'workflow',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Revisiting workflow steps must not repeat side effects that already committed',
  'statement': 'Back-navigation and re-entry must distinguish draft step rendering from actions that already sent '
               'email, reserved inventory, charged payment, created records, or invoked other external side effects.',
  'intent': 'Prevent a user’s attempt to edit earlier answers from re-executing non-idempotent work associated with '
            'a prior step transition.',
  'applies_when': ['A multi-step flow performs side effects before final completion or on transitions between '
                   'steps.'],
  'does_not_apply_when': [],
  'failure_modes': ['Returning to and leaving a prior step causes an already completed side effect to execute again '
                    'because transition code does not track authoritative completion.'],
  'user_impacts': ['Users can create duplicate records, messages, reservations, charges, or other external '
                   'consequences while merely reviewing earlier input.'],
  'observables': ['Instrument side-effect calls, advance through the workflow, navigate backward, then advance again '
                  'without changing the relevant decision.'],
  'falsifiers': ['Committed side effects have stable identity or idempotency and step navigation alone cannot replay '
                 'them.'],
  'repairs': ['Separate render/navigation transitions from side-effect commands and persist operation identity or '
              'completion before allowing re-entry.'],
  'exceptions': [],
  'verification': ['Exercise Back, refresh, retry, browser history, and resume around every pre-final side effect '
                   'and confirm one logical consequence per user decision.'],
  'owner_hints': ['designing-multi-step-forms'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-workflow-multistep-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.workflow.skipped-step-reason-visible-when-relevant',
  'domain': 'workflow',
  'class': 'contextual',
  'severity': 'moderate',
  'enforcement': 'warn',
  'title': 'Conditionally skipped workflow steps should expose why they are unavailable when that affects '
           'understanding',
  'statement': 'When progress indicators show a step that becomes skipped or unavailable because of branch logic, '
               'permission, prior answer, or product policy, the interface should make that state understandable '
               'rather than simply removing the step without context.',
  'intent': 'Preserve the user’s mental model of progress when a workflow shape changes dynamically after earlier '
            'decisions.',
  'applies_when': ['A visible stepper, checklist, or progress model includes steps whose applicability can change '
                   'based on answers or effective policy.'],
  'does_not_apply_when': [],
  'failure_modes': ['A previously visible step disappears or becomes unreachable with no indication whether it '
                    'completed, was skipped, failed, or is no longer applicable.'],
  'user_impacts': ['Users can think required work was lost or completed incorrectly and may not understand why the '
                   'workflow now has a different path.'],
  'observables': ['Change branch-driving answers and permissions while observing the progress model and any state '
                  'associated with the affected step.'],
  'falsifiers': ['The progress surface distinguishes not-applicable or skipped state where necessary for '
                 'understanding and does not mislabel it complete.'],
  'repairs': ['Model step applicability separately from completion and surface concise reason text or state '
              'semantics in progress UI when the change is user-relevant.'],
  'exceptions': [],
  'verification': ['Exercise all branch transitions and permission variants and confirm step progress remains '
                   'interpretable without exposing hidden policy details.'],
  'owner_hints': ['designing-multi-step-forms'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-workflow-multistep-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.workflow.async-validation-blocks-only-dependent-progress',
  'domain': 'workflow',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Asynchronous validation should block only progress that depends on its unresolved result',
  'statement': 'A pending remote validation must prevent the dependent commit or branch from proceeding, but should '
               'not freeze unrelated review or editing when those actions do not rely on the validation result.',
  'intent': 'Keep multi-step flows responsive without allowing users to cross a boundary whose validity is still '
            'unknown.',
  'applies_when': ['A workflow step performs server-side or asynchronous validation whose result is required for '
                   'some later actions but not every local interaction.'],
  'does_not_apply_when': [],
  'failure_modes': ['The workflow either advances past the dependent boundary while validation is unresolved or '
                    'globally disables unrelated editing during the check.'],
  'user_impacts': ['Users can submit invalid state or experience unnecessary dead time because the validation '
                   'dependency is modeled too weakly or too broadly.'],
  'observables': ['Delay the validator and attempt dependent and independent actions while observing progress state, '
                  'editing, and eventual error reconciliation.'],
  'falsifiers': ['Only transitions requiring the unresolved validation are blocked, and a late failure attaches to '
                 'the relevant state without discarding unrelated work.'],
  'repairs': ['Represent validation dependencies explicitly and gate the exact transitions that consume the result '
              'instead of freezing the whole workflow.'],
  'exceptions': [],
  'verification': ['Test delayed success, delayed failure, cancellation, answer changes during validation, and '
                   'repeated requests and confirm dependency-scoped blocking remains correct.'],
  'owner_hints': ['designing-multi-step-forms'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-workflow-multistep-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.workflow.final-submit-idempotent',
  'domain': 'workflow',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Final multi-step submission must be idempotent across retries and uncertain responses',
  'statement': 'If the final submit request times out or the client loses the response, retrying must not create a '
               'second logical application, order, request, record, or other committed workflow result.',
  'intent': 'Protect long completed workflows from duplicate side effects at the moment network uncertainty is most '
            'costly.',
  'applies_when': ['The final submission creates or commits a consequential logical entity and the client can retry '
                   'after timeout, reconnect, or ambiguous completion.'],
  'does_not_apply_when': [],
  'failure_modes': ['A user retries after an uncertain response and the backend creates another independent '
                    'committed entity from the same completed workflow.'],
  'user_impacts': ['Users can produce duplicate applications, requests, reservations, orders, or other records and '
                   'may not know which one is authoritative.'],
  'observables': ['Drop the final response after server commit, retry from the same workflow identity, and inspect '
                  'created entities and returned identifiers.'],
  'falsifiers': ['All retries for the same finalized workflow resolve to one authoritative result or explicitly '
                 'require a new user decision to create another.'],
  'repairs': ['Bind final submission to a stable idempotency or workflow-completion identity persisted before '
              'sending the request.'],
  'exceptions': [],
  'verification': ['Test timeout, refresh, browser retry, double activation, and reconnect and confirm one logical '
                   'committed outcome per workflow completion.'],
  'owner_hints': ['designing-multi-step-forms'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-workflow-multistep-owners-v13'],
  'status': 'active'}]

__all__ = ["WORKFLOW_MULTISTEP_RULES_V13"]
