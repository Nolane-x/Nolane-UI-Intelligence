"""V13 eighth-wave independently authored rules for medication."""
from __future__ import annotations

from ._capabilities import interaction_caps


MEDICATION_RULES_V13 = [{'rule_id': 'ui.medication.identity-strength-form-unambiguous',
  'domain': 'medication',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Medication identity must present product, strength, concentration, and dosage form without '
           'ambiguity',
  'statement': 'Names that look similar can represent materially different products, so order entry '
               'must expose the attributes needed to identify the intended medication before '
               'commitment.',
  'intent': 'Prevent clinicians from selecting a same-name or look-alike medication whose strength or '
            'form differs from the intended therapy.',
  'applies_when': ['Medication search and order entry include products with multiple strengths, '
                   'concentrations, formulations, and package forms.'],
  'does_not_apply_when': [],
  'failure_modes': ['A search result shows only “metoprolol 50” and hides whether the item is '
                    'immediate-release or extended-release until after signing.'],
  'user_impacts': ['Patients can receive the wrong formulation or strength even though the visible '
                   'medication name appeared familiar.'],
  'observables': ['Search for products with overlapping names and compare result rows, selected-order '
                  'summary, signing view, and print/export surfaces.'],
  'falsifiers': ['The selected product exposes stable medication identity plus strength, concentration '
                 'when relevant, and dosage form before the order becomes final.'],
  'repairs': ['Carry structured medication attributes from the formulary into every selection and '
              'confirmation surface instead of relying on a display label alone.'],
  'exceptions': [],
  'verification': ['Order several look-alike products and verify each can be distinguished before '
                   'signing and remains distinguishable in history.'],
  'owner_hints': ['designing-medication-order-entry'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-medication-order-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.medication.dose-route-frequency-coupled',
  'domain': 'medication',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Dose, route, and frequency must be reviewed as one coupled medication instruction',
  'statement': 'A medication instruction can become unsafe when one component changes independently, so '
               'order entry should present dose, route, and timing together wherever the clinician '
               'confirms therapy.',
  'intent': 'Keep medication administration meaning intact across edits, templates, and copied orders.',
  'applies_when': ['Medication orders are assembled from separate dose, unit, route, frequency, and '
                   'schedule controls.'],
  'does_not_apply_when': [],
  'failure_modes': ['A clinician changes a route from oral to intravenous while an old oral dose and '
                    'frequency remain silently reused from the template.'],
  'user_impacts': ['The order can be syntactically valid but clinically inconsistent because related '
                   'instruction fields drifted apart.'],
  'observables': ['Change route, dose unit, and frequency in different sequences and inspect dependent '
                  'fields, warnings, summary text, and final payload.'],
  'falsifiers': ['The final instruction shows all coupled components together and any incompatible '
                 'stale value is cleared, recalculated, or requires deliberate confirmation.'],
  'repairs': ['Model the administration instruction as one validated object and revalidate dependent '
              'fields whenever route, formulation, dose basis, or timing changes.'],
  'exceptions': [],
  'verification': ['Exercise route and dose transitions across templates and copies, verifying no '
                   'hidden stale component survives into the signed order.'],
  'owner_hints': ['designing-medication-order-entry'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-medication-order-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.medication.allergy-check-pending-visible',
  'domain': 'medication',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Pending or unavailable allergy checking must remain visible before medication commitment',
  'statement': 'If allergy data has not loaded or the checking service is unavailable, the interface '
               'must not present a clean allergy state as though screening completed successfully.',
  'intent': 'Prevent missing safety evidence from being mistaken for an affirmative absence of allergy '
            'risk.',
  'applies_when': ['Medication order entry depends on patient allergy data or an external '
                   'allergy-checking service.'],
  'does_not_apply_when': [],
  'failure_modes': ['The allergy service times out and the UI removes the loading indicator, leaving an '
                    'empty “no allergies” region beside the order.'],
  'user_impacts': ['Clinicians can sign medication orders believing allergy screening was completed '
                   'when the safety check never returned.'],
  'observables': ['Delay, fail, and partially load allergy sources while opening medication orders and '
                  'inspect signing gates and safety summaries.'],
  'falsifiers': ['Pending, unavailable, incomplete, and completed allergy checks remain distinct, and a '
                 'clean result appears only after successful evaluation.'],
  'repairs': ['Carry allergy-check execution state separately from the findings and block or require '
              'explicit policy-governed acknowledgement when evidence is unavailable.'],
  'exceptions': [],
  'verification': ['Run known-allergy and no-allergy fixtures under service success and failure, '
                   'verifying the interface never converts unavailable evidence into a clean state.'],
  'owner_hints': ['designing-medication-order-entry'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-medication-order-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.medication.interaction-warning-source-visible',
  'domain': 'medication',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Medication interaction warnings must expose the rule source and the medications involved',
  'statement': 'A warning should identify which ordered or active therapies produced the interaction '
               'and enough source context to distinguish evidence-based checking from generic caution '
               'text.',
  'intent': 'Help clinicians evaluate alerts without obscuring what combination actually triggered '
            'them.',
  'applies_when': ['Order entry performs drug-drug, drug-condition, or other medication interaction '
                   'checks.'],
  'does_not_apply_when': [],
  'failure_modes': ['A severe interaction banner appears without naming the existing medication that '
                    'triggered it, so the clinician cannot determine whether the alert still applies '
                    'after a medication change.'],
  'user_impacts': ['Important warnings can be ignored or misinterpreted because their basis cannot be '
                   'inspected.'],
  'observables': ['Add and remove interacting therapies and compare alert membership, source details, '
                  'severity, and dismissal behavior.'],
  'falsifiers': ['Each warning identifies the implicated therapies or conditions and remains traceable '
                 'to the checking source or rule set used.'],
  'repairs': ['Preserve interaction rule identifiers and contributing medication identities in the '
              'evaluation result and expose them in the review surface.'],
  'exceptions': [],
  'verification': ['Create several overlapping interactions and verify each alert updates only when its '
                   'contributing evidence changes.'],
  'owner_hints': ['designing-medication-order-entry'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-medication-order-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.medication.discontinue-effective-time-visible',
  'domain': 'medication',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Medication discontinuation must expose when the stop becomes clinically effective',
  'statement': 'Stopping future doses now, after the current dose, at a scheduled time, or at transfer '
               'are different instructions and must not collapse into one undifferentiated discontinued '
               'badge.',
  'intent': 'Keep administration teams aligned with the intended stop boundary of a medication order.',
  'applies_when': ['Medication workflows support immediate, scheduled, conditional, or encounter-bound '
                   'discontinuation.'],
  'does_not_apply_when': [],
  'failure_modes': ['A clinician schedules discontinuation for midnight but the medication list '
                    'immediately renders the drug inactive, hiding that doses remain authorized until '
                    'then.'],
  'user_impacts': ['Care teams can omit or administer doses incorrectly because the interface '
                   'misrepresents the effective stop time.'],
  'observables': ['Discontinue medications with immediate and future effective times and inspect active '
                  'lists, MAR-like views, history, and handoff summaries.'],
  'falsifiers': ['Current activity and future stop intent are both visible until the effective time, '
                 'after which the medication transitions consistently to discontinued.'],
  'repairs': ['Store discontinuation request time separately from effective stop time and derive '
              'activity from the latter.'],
  'exceptions': [],
  'verification': ['Test immediate, scheduled, and canceled discontinuations, verifying list status and '
                   'administration eligibility converge at the correct boundary.'],
  'owner_hints': ['designing-medication-order-entry'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-medication-order-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.medication.prn-condition-visible',
  'domain': 'medication',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'As-needed medication orders must keep the administration condition visible with dose '
           'instructions',
  'statement': 'A PRN frequency without the indication or triggering condition is incomplete '
               'operational guidance and should not be presented as though timing alone defines use.',
  'intent': 'Preserve the clinician’s conditional intent when orders move into administration and '
            'handoff contexts.',
  'applies_when': ['Medications can be ordered for use only when a symptom, threshold, or other '
                   'condition is present.'],
  'does_not_apply_when': [],
  'failure_modes': ['An order summary shows “every 6 hours PRN” but omits that it is only for severe '
                    'nausea, making the instruction look broadly discretionary.'],
  'user_impacts': ['Administration can occur for the wrong indication or without the intended decision '
                   'boundary.'],
  'observables': ['Create PRN orders with different indications and inspect medication list, '
                  'administration view, printout, handoff, and history.'],
  'falsifiers': ['The PRN condition remains paired with dose and frequency wherever someone could '
                 'decide whether to administer the medication.'],
  'repairs': ['Treat indication or condition as a required part of the PRN instruction and propagate it '
              'through downstream medication representations.'],
  'exceptions': [],
  'verification': ['Edit and copy PRN orders, verifying the conditional indication cannot disappear '
                   'while the timing instruction remains.'],
  'owner_hints': ['designing-medication-order-entry'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-medication-order-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.medication.taper-sequence-integrity-preserved',
  'domain': 'medication',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Medication taper schedules must preserve ordered sequence, duration, and transition '
           'boundaries',
  'statement': 'A taper is a multi-step therapeutic plan rather than independent dose rows, so the '
               'interface must maintain the order and timing relationship among its steps.',
  'intent': 'Prevent dose reductions or increases from being reordered, skipped, or duplicated during '
            'editing and execution.',
  'applies_when': ['Medication orders can define staged dose changes over days, weeks, or event-driven '
                   'transitions.'],
  'does_not_apply_when': [],
  'failure_modes': ['A user edits the second taper step and the UI re-sorts rows by dose amount, '
                    'causing the plan to administer a later lower dose before the intended intermediate '
                    'phase.'],
  'user_impacts': ['Patients can receive an unsafe dosing trajectory because sequence semantics were '
                   'treated as ordinary list order.'],
  'observables': ['Create, reorder, copy, and edit taper steps while inspecting effective dates, '
                  'sequence numbering, summaries, and downstream instructions.'],
  'falsifiers': ['Every step retains a stable sequence and explicit transition boundary, and edits '
                 'cannot create overlaps or gaps without visible validation.'],
  'repairs': ['Model taper steps as an ordered schedule with validated temporal continuity rather than '
              'a bag of medication instructions.'],
  'exceptions': [],
  'verification': ['Test insertion, deletion, date shifts, and copy operations, verifying the final '
                   'administered sequence matches the clinician-reviewed taper.'],
  'owner_hints': ['designing-medication-order-entry'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-medication-order-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.medication.duplicate-therapy-distinguishable',
  'domain': 'medication',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Potential duplicate medication therapy must expose why orders are equivalent or '
           'intentionally distinct',
  'statement': 'When two active orders share an ingredient or therapeutic class, the interface should '
               'show formulation, route, schedule, indication, and lifecycle before asking the '
               'clinician to resolve duplication.',
  'intent': 'Reduce accidental duplicate therapy without forcing clinically distinct treatments into '
            'one false equivalence.',
  'applies_when': ['A patient can have multiple same-ingredient or same-class medications for different '
                   'routes, indications, or transition plans.'],
  'does_not_apply_when': [],
  'failure_modes': ['A duplicate warning shows only two medication names and a clinician cancels a '
                    'topical or rescue order that was intentionally separate from the scheduled '
                    'therapy.'],
  'user_impacts': ['Necessary therapy can be removed, or true duplicates can remain, because the '
                   'comparison hid material differences.'],
  'observables': ['Create exact duplicates and clinically distinct near-duplicates, then inspect '
                  'warnings, medication list context, and resolution actions.'],
  'falsifiers': ['Duplicate review exposes the fields that define equivalence and lets the clinician '
                 'identify exactly which order will be retained, changed, or stopped.'],
  'repairs': ['Compare structured medication instructions and present their meaningful differences '
              'instead of relying on name or therapeutic class alone.'],
  'exceptions': [],
  'verification': ['Resolve several duplicate scenarios and verify only the intended order changes '
                   'while distinct therapies remain clearly differentiated.'],
  'owner_hints': ['designing-medication-order-entry'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-medication-order-owners-v13'],
  'status': 'active'}]


__all__ = ["MEDICATION_RULES_V13"]
