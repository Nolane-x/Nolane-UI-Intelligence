"""V13 eighth-wave independently authored rules for clinicalorder."""
from __future__ import annotations

from ._capabilities import interaction_caps


CLINICAL_ORDER_RULES_V13 = [{'rule_id': 'ui.clinicalorder.status-source-authoritative',
  'domain': 'clinicalorder',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Clinical order status must identify the authoritative workflow source behind the displayed '
           'state',
  'statement': 'Order labels such as pending, active, collected, in progress, completed, or canceled '
               'must reflect the system or service that owns that transition rather than a locally '
               'guessed presentation state.',
  'intent': 'Keep care decisions aligned with the actual execution state of an order across integrated '
            'clinical systems.',
  'applies_when': ['Clinical orders can be created in one system and executed, collected, resulted, or '
                   'canceled by another service or facility.'],
  'does_not_apply_when': [],
  'failure_modes': ['The ordering screen marks a lab order completed when the outbound message was sent '
                    'even though the laboratory never acknowledged or performed it.'],
  'user_impacts': ['Clinicians can assume care was delivered and fail to follow up on an order that '
                   'never reached or completed execution.'],
  'observables': ['Simulate acknowledgements, downstream rejection, completion, and integration delay '
                  'while comparing the displayed status to source messages.'],
  'falsifiers': ['The UI states both the current effective order status and, where material, the '
                 'authoritative source or last confirmed transition behind it.'],
  'repairs': ['Derive displayed lifecycle from acknowledged domain events and distinguish local '
              'submission from downstream execution state.'],
  'exceptions': [],
  'verification': ['Run accepted, rejected, delayed, canceled, and completed orders through integration '
                   'fixtures and verify each surface converges on the authoritative status.'],
  'owner_hints': ['designing-clinical-order-status'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-clinical-order-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.clinicalorder.discontinued-distinct-from-completed',
  'domain': 'clinicalorder',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Discontinued clinical orders must remain distinct from orders that completed their intended '
           'course',
  'statement': 'Stopping an order before or after partial execution carries different clinical meaning '
               'from successful completion and must not be represented by the same terminal state.',
  'intent': 'Preserve whether care ended because it was fulfilled or because a clinician intentionally '
            'stopped further execution.',
  'applies_when': ['Orders can be discontinued, canceled, completed, partially performed, or '
                   'superseded.'],
  'does_not_apply_when': [],
  'failure_modes': ['A medication or diagnostic order is discontinued after one partial execution and '
                    'the timeline labels it completed, hiding that future execution was intentionally '
                    'stopped.'],
  'user_impacts': ['Clinicians reviewing history can infer a full planned course occurred when it was '
                   'actually interrupted.'],
  'observables': ['Discontinue orders at several lifecycle points and inspect order history, summaries, '
                  'handoff views, and downstream reconciliation.'],
  'falsifiers': ['Completed, canceled, and discontinued states stay distinct, and partial execution '
                 'before discontinuation remains visible when applicable.'],
  'repairs': ['Model terminal lifecycle reasons separately from execution quantity and preserve the '
              'transition that stopped future work.'],
  'exceptions': [],
  'verification': ['Test discontinuation before execution, after partial execution, and after '
                   'completion and verify the historical meaning remains unambiguous.'],
  'owner_hints': ['designing-clinical-order-status'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-clinical-order-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.clinicalorder.pending-signature-visible',
  'domain': 'clinicalorder',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Unsigned or cosign-pending clinical orders must be visibly non-final where signature '
           'authority is required',
  'statement': 'If policy requires author signature, cosign, or attestation before an order is '
               'executable or legally final, the interface must not present the draft as an equivalent '
               'active order.',
  'intent': 'Prevent clinicians from assuming an order has authoritative effect before required '
            'sign-off exists.',
  'applies_when': ['Clinical workflows allow orders that require author signature, supervising cosign, '
                   'or later attestation.'],
  'does_not_apply_when': [],
  'failure_modes': ['A resident enters an order that still needs cosign, but patient-summary and task '
                    'views render it with the same active styling as signed executable orders.'],
  'user_impacts': ['Care teams can act on an order whose required authorization is not complete or '
                   'overlook a blocking signature task.'],
  'observables': ['Create orders under different signing policies and inspect order lists, task queues, '
                  'execution eligibility, and handoff summaries.'],
  'falsifiers': ['Pending-signature state is explicit and the UI distinguishes whether the order is '
                 'draft, executable pending cosign, or blocked until signature.'],
  'repairs': ['Model signature authority as a first-class order state and propagate it to every surface '
              'that represents order readiness.'],
  'exceptions': [],
  'verification': ['Exercise unsigned, signed, cosigned, rejected, and revoked signatures and verify '
                   'execution and display follow the actual policy state.'],
  'owner_hints': ['designing-clinical-order-status'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-clinical-order-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.clinicalorder.patient-context-sticky-across-action',
  'domain': 'clinicalorder',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Clinical order actions must remain bound to the patient context the clinician reviewed',
  'statement': 'Opening another patient, changing encounter, or receiving workspace updates must not '
               'retarget an in-progress order action to a different patient without explicit '
               'confirmation.',
  'intent': 'Prevent cross-patient ordering caused by context drift in dense clinical workflows.',
  'applies_when': ['Clinicians can switch rapidly between patients or encounters while order dialogs, '
                   'side panels, or drafts remain open.'],
  'does_not_apply_when': [],
  'failure_modes': ['A clinician opens an order for patient A, switches the chart to patient B, and the '
                    'still-open submit control sends the draft under patient B because it follows '
                    'global context.'],
  'user_impacts': ['A cross-patient order can create direct clinical harm and corrupt the medical '
                   'record.'],
  'observables': ['Open order composers while switching patient and encounter context from another '
                  'navigation surface, then inspect target identity at commit.'],
  'falsifiers': ['The order keeps an explicit patient and encounter binding, and any context mismatch '
                 'blocks or requires deliberate rebinding before submission.'],
  'repairs': ['Capture patient and encounter identity when order authoring begins and validate that '
              'binding again at commit rather than inheriting mutable global context.'],
  'exceptions': [],
  'verification': ['Race patient navigation with order signing and verify no order can silently migrate '
                   'to a different patient or encounter.'],
  'owner_hints': ['designing-clinical-order-status'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-clinical-order-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.clinicalorder.duplicate-orders-distinguishable',
  'domain': 'clinicalorder',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Potentially duplicate clinical orders must expose the distinctions that make them separate '
           'or redundant',
  'statement': 'When similar orders coexist, the interface should show ordering time, indication, dose '
               'or protocol, destination, and lifecycle so clinicians can judge whether the duplication '
               'is intentional.',
  'intent': 'Reduce accidental repeat ordering without incorrectly collapsing clinically distinct '
            'requests.',
  'applies_when': ['A patient may have multiple orders with similar names that differ by timing, '
                   'specimen, indication, protocol, or facility.'],
  'does_not_apply_when': [],
  'failure_modes': ['Two imaging orders with the same display name appear identical, so a clinician '
                    'cancels the wrong one or submits an unnecessary third order.'],
  'user_impacts': ['Patients can receive duplicate interventions or lose a needed order because the '
                   'interface hid material distinctions.'],
  'observables': ['Create same-name orders with different timing, indications, and destinations and '
                  'inspect list, search, cancellation, and duplicate-warning surfaces.'],
  'falsifiers': ['Each order remains uniquely identifiable and duplicate warnings expose the fields '
                 'that justify comparison rather than relying on name alone.'],
  'repairs': ['Present stable order identity plus clinically relevant differentiators and make '
              'duplicate detection advisory to those explicit facts.'],
  'exceptions': [],
  'verification': ['Compare and act on near-duplicate orders, verifying the clinician can identify '
                   'exactly which order will be canceled, changed, or retained.'],
  'owner_hints': ['designing-clinical-order-status'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-clinical-order-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.clinicalorder.result-linked-to-order-identity',
  'domain': 'clinicalorder',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Results must remain linked to the exact clinical order that produced them',
  'statement': 'When several similar tests or procedures exist, a result should identify its '
               'originating order, specimen or accession context, and execution episode rather than '
               'being matched by display name alone.',
  'intent': 'Prevent clinicians from attributing a result to the wrong diagnostic request or treatment '
            'episode.',
  'applies_when': ['Clinical records can contain repeat orders for the same test across different '
                   'times, specimens, facilities, or encounters.'],
  'does_not_apply_when': [],
  'failure_modes': ['A result is attached to the most recent same-name order even though its accession '
                    'belongs to an earlier request.'],
  'user_impacts': ['Clinical interpretation and follow-up can be based on the wrong specimen, time, or '
                   'episode of care.'],
  'observables': ['Create repeated orders and out-of-order results, then inspect result details, order '
                  'history, trends, and notification links.'],
  'falsifiers': ['Every result exposes a stable link to the originating order or explicit unmatched '
                 'state when the relationship cannot be established.'],
  'repairs': ['Use authoritative order/accession relationships from the source workflow and never infer '
              'linkage from name or recency alone.'],
  'exceptions': [],
  'verification': ['Deliver results out of order for repeated tests and verify each result resolves to '
                   'the correct originating order and encounter.'],
  'owner_hints': ['designing-clinical-order-status'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-clinical-order-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.clinicalorder.cross-facility-context-visible',
  'domain': 'clinicalorder',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Cross-facility clinical orders must make the ordering and performing context visible',
  'statement': 'If an order crosses organizations, departments, laboratories, imaging centers, or '
               'pharmacies, the UI should expose where it was placed and where execution is expected or '
               'occurred.',
  'intent': 'Prevent clinicians from assuming local execution semantics for an order owned by another '
            'facility or service.',
  'applies_when': ['Orders may be routed to external facilities or transferred between care locations.'],
  'does_not_apply_when': [],
  'failure_modes': ['An external laboratory order appears in a local list without destination context, '
                    'so staff search the local lab for a specimen that was never expected there.'],
  'user_impacts': ['Care coordination can be delayed and duplicate orders may be created because '
                   'execution ownership is unclear.'],
  'observables': ['Place local and external orders with identical test names and compare list, detail, '
                  'handoff, and cancellation surfaces.'],
  'falsifiers': ['Ordering facility, performing destination, and any transfer state are visible '
                 'wherever that distinction changes action or interpretation.'],
  'repairs': ['Carry facility and destination identity as order metadata and surface it in lifecycle, '
              'status, and action controls rather than only in hidden details.'],
  'exceptions': [],
  'verification': ['Route orders across multiple facilities and verify staff can identify which '
                   'organization currently owns execution and cancellation.'],
  'owner_hints': ['designing-clinical-order-status'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-clinical-order-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.clinicalorder.stale-order-refresh-before-action',
  'domain': 'clinicalorder',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Stale clinical order state must be reconciled before cancel, discontinue, modify, or sign '
           'actions commit',
  'statement': 'Because downstream execution can change while a clinician keeps a chart open, '
               'state-dependent order actions must revalidate the current authoritative lifecycle '
               'before mutation.',
  'intent': 'Prevent old chart state from overriding execution or authorization changes that occurred '
            'elsewhere.',
  'applies_when': ['Orders can be updated concurrently by clinicians, downstream services, or external '
                   'facilities.'],
  'does_not_apply_when': [],
  'failure_modes': ['A clinician tries to cancel an order shown as pending, but it was already '
                    'performed elsewhere; the stale action rewrites it as simply canceled with no '
                    'performed state.'],
  'user_impacts': ['Clinical history can become false and subsequent care decisions can be based on an '
                   'impossible lifecycle.'],
  'observables': ['Open the same order in two sessions, advance it downstream in one, then attempt '
                  'state-dependent actions from the stale session.'],
  'falsifiers': ['The stale action refreshes, conflicts, or reconciles against current order state '
                 'before any mutation is accepted.'],
  'repairs': ['Use versioned order commands and require the server to reject incompatible transitions '
              'while the client presents a safe reconciliation path.'],
  'exceptions': [],
  'verification': ['Race performance, cancellation, discontinuation, and signing transitions and verify '
                   'no stale client can overwrite a newer authoritative order state.'],
  'owner_hints': ['designing-clinical-order-status'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-clinical-order-owners-v13'],
  'status': 'active'}]


__all__ = ["CLINICAL_ORDER_RULES_V13"]
