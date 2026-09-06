"""V13 eighth-wave independently authored rules for labresult."""
from __future__ import annotations

from ._capabilities import interaction_caps


LAB_RESULT_RULES_V13 = [{'rule_id': 'ui.labresult.units-and-reference-range-preserved',
  'domain': 'labresult',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Laboratory values must preserve units and the reference range used for that specific result',
  'statement': 'A numeric result cannot be interpreted safely without its measurement unit and '
               'applicable reference interval, which may vary by laboratory, method, population, or '
               'time.',
  'intent': 'Keep result interpretation tied to the source measurement context instead of a unitless '
            'normalized number.',
  'applies_when': ['Laboratory results display quantitative values that may have laboratory-specific '
                   'units or reference ranges.'],
  'does_not_apply_when': [],
  'failure_modes': ['A potassium value is shown in a trend after unit conversion but the old reference '
                    'interval remains attached, making an abnormal result appear normal.'],
  'user_impacts': ['Clinicians can misinterpret severity or trend because displayed numbers and '
                   'interpretation thresholds no longer share the same basis.'],
  'observables': ['Load results from laboratories with different units and intervals, then inspect '
                  'detail, trend, export, and abnormality indicators.'],
  'falsifiers': ['Every displayed value retains its applicable unit and reference interval, and '
                 'conversions update both value semantics and comparison basis coherently.'],
  'repairs': ['Bind value, unit, method context, and reference interval as one result interpretation '
              'record and avoid independent presentation transformations.'],
  'exceptions': [],
  'verification': ['Compare native and converted results across labs and verify abnormality flags and '
                   'trend labels use the correct paired unit and interval.'],
  'owner_hints': ['designing-lab-result-review'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-lab-result-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.labresult.preliminary-distinct-from-final',
  'domain': 'labresult',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Preliminary laboratory results must remain distinct from final verified results',
  'statement': 'An early value can guide care, but the interface must preserve its provisional status '
               'and later transition rather than presenting it as a final verified result.',
  'intent': 'Prevent clinicians from over-trusting values that the laboratory has not finalized.',
  'applies_when': ['Laboratory workflows can publish preliminary, partial, verified, corrected, and '
                   'final results.'],
  'does_not_apply_when': [],
  'failure_modes': ['A preliminary culture result appears in the patient summary with the same final '
                    'styling and no pending indicator, then changes substantially after verification.'],
  'user_impacts': ['Clinical decisions can be made on a value whose evidentiary status was hidden.'],
  'observables': ['Deliver preliminary and final versions of the same result and inspect chart summary, '
                  'trends, notifications, and historical detail.'],
  'falsifiers': ['Provisional state remains visible until finalization and prior preliminary values are '
                 'retained as history when clinically relevant.'],
  'repairs': ['Model result verification status explicitly and propagate it to every surface that can '
              'be used for clinical interpretation.'],
  'exceptions': [],
  'verification': ['Transition results from preliminary through final and corrected states, verifying '
                   'each state and its history remain distinguishable.'],
  'owner_hints': ['designing-lab-result-review'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-lab-result-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.labresult.corrected-result-history-preserved',
  'domain': 'labresult',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Corrected laboratory results must preserve the prior reported value and correction context',
  'statement': 'When a laboratory amends a result, the current corrected value should be authoritative '
               'while the previous value, correction time, and reason remain reviewable.',
  'intent': 'Allow clinicians to understand what changed after earlier care decisions may already have '
            'used the original report.',
  'applies_when': ['Laboratories can issue corrected or amended results after a value has already been '
                   'released.'],
  'does_not_apply_when': [],
  'failure_modes': ['A corrected result silently overwrites the original value in trends and '
                    'notifications, leaving no indication that clinicians previously saw a different '
                    'number.'],
  'user_impacts': ['Care teams cannot reconstruct whether prior decisions were reasonable given the '
                   'information available at that time.'],
  'observables': ['Publish an initial result followed by one or more corrections and inspect detail, '
                  'trend, notification history, and audit export.'],
  'falsifiers': ['The latest corrected value is clearly current while every superseded reported value '
                 'and correction event remains accessible.'],
  'repairs': ['Store corrections as versioned result events and render current plus historical values '
              'instead of destructive replacement.'],
  'exceptions': [],
  'verification': ['Apply multiple corrections and verify current displays, timelines, and exports '
                   'preserve the complete reporting lineage.'],
  'owner_hints': ['designing-lab-result-review'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-lab-result-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.labresult.specimen-time-distinct-from-result-time',
  'domain': 'labresult',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Specimen collection time must remain distinct from result publication and verification '
           'times',
  'statement': 'Clinical interpretation often depends on when the specimen was obtained, which is not '
               'interchangeable with when testing completed or the result became visible.',
  'intent': 'Keep trends and temporal reasoning aligned with the biological observation time rather '
            'than interface publication time.',
  'applies_when': ['Lab results have collection, receipt, analysis, verification, and publication '
                   'timestamps that can differ materially.'],
  'does_not_apply_when': [],
  'failure_modes': ['A delayed test is plotted at result publication time, shifting it days later in a '
                    'trend and making it appear associated with the wrong treatment period.'],
  'user_impacts': ['Clinicians can infer false temporal relationships between interventions and '
                   'measured physiology.'],
  'observables': ['Create delayed and backlogged specimens and compare timeline position, detail '
                  'timestamps, trend ordering, and exports.'],
  'falsifiers': ['Collection time and result/report times are separately labeled, and trend placement '
                 'uses the clinically intended temporal basis.'],
  'repairs': ['Preserve distinct laboratory timestamps and define which timestamp each visualization or '
              'workflow uses rather than collapsing them.'],
  'exceptions': [],
  'verification': ['Test delayed verification and late-imported results, verifying specimen chronology '
                   'and reporting chronology remain independently recoverable.'],
  'owner_hints': ['designing-lab-result-review'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-lab-result-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.labresult.abnormal-flag-source-visible',
  'domain': 'labresult',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Abnormal laboratory flags must expose the source basis used to classify the result',
  'statement': 'High, low, critical, or other abnormality labels should be traceable to the applicable '
               'laboratory reference interval, instrument flag, or clinical rule rather than inferred '
               'from generic thresholds.',
  'intent': 'Prevent attention cues from implying a stronger or different interpretation than the '
            'source supports.',
  'applies_when': ['Laboratory results can carry abnormal flags from the source lab or be classified by '
                   'local clinical rules.'],
  'does_not_apply_when': [],
  'failure_modes': ['A result receives a red critical badge from a generic application threshold even '
                    'though the source laboratory marked it only mildly high for that patient context.'],
  'user_impacts': ['Clinicians can prioritize or escalate incorrectly because the UI obscures how the '
                   'abnormal label was produced.'],
  'observables': ['Compare source flags, local rules, and displayed severity across results with '
                  'different reference intervals and methods.'],
  'falsifiers': ['The interface can identify whether a flag comes from source laboratory metadata, a '
                 'local rule, or both, and does not conflate their authority.'],
  'repairs': ['Preserve source abnormality metadata separately from application-derived interpretation '
              'and label derived classifications explicitly.'],
  'exceptions': [],
  'verification': ['Feed conflicting source and local classifications and verify the UI retains each '
                   'basis without silently substituting one for the other.'],
  'owner_hints': ['designing-lab-result-review'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-lab-result-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.labresult.patient-and-specimen-identity-bound',
  'domain': 'labresult',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Laboratory results must remain jointly bound to patient identity and specimen identity',
  'statement': 'A result should not be considered safely attributable from patient name or test name '
               'alone; the UI must preserve the specimen or accession context that produced it.',
  'intent': 'Prevent cross-patient and cross-specimen attribution errors in repeated or high-volume '
            'testing.',
  'applies_when': ['Clinical systems ingest multiple specimens and repeated tests for the same or '
                   'similar patients.'],
  'does_not_apply_when': [],
  'failure_modes': ['Two patients with similar names have identical tests and an imported result is '
                    'attached using display name matching rather than accession identity.'],
  'user_impacts': ['A value can be interpreted and acted on for the wrong patient or wrong specimen '
                   'episode.'],
  'observables': ['Import repeated same-name tests across patients and specimens and inspect result '
                  'linkage, accession detail, trends, and correction workflows.'],
  'falsifiers': ['Each result resolves through stable patient and specimen or accession identifiers, or '
                 'remains explicitly unmatched when that linkage is uncertain.'],
  'repairs': ['Use authoritative identifiers from ordering and laboratory messages and reject heuristic '
              'patient/test-name matching as final linkage authority.'],
  'exceptions': [],
  'verification': ['Test duplicate names, repeated specimens, and out-of-order imports, verifying no '
                   'result silently attaches to the wrong patient or specimen.'],
  'owner_hints': ['designing-lab-result-review'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-lab-result-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.labresult.missing-result-distinct-from-normal',
  'domain': 'labresult',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Missing or unavailable laboratory results must remain distinct from normal or negative '
           'findings',
  'statement': 'No value can mean not performed, pending, canceled, lost, unavailable, or not reported; '
               'the interface must not collapse these states into a reassuring normal result.',
  'intent': 'Prevent absence of data from being interpreted as evidence of normal physiology or '
            'negative testing.',
  'applies_when': ['Orders or panels can contain components that are pending, canceled, not resulted, '
                   'or unavailable.'],
  'does_not_apply_when': [],
  'failure_modes': ['A lab panel summary shows all unflagged rows as normal, including one component '
                    'that never produced a result.'],
  'user_impacts': ['Clinicians can overlook incomplete testing because missingness is rendered as a '
                   'benign clinical finding.'],
  'observables': ['Create panel components in pending, canceled, missing, negative, and normal states '
                  'and compare summaries, filters, trends, and exports.'],
  'falsifiers': ['Unavailable states have explicit semantics and never receive normal/negative '
                 'interpretation unless a reported result actually supports it.'],
  'repairs': ['Model missingness and result interpretation separately and require a concrete reported '
              'value or categorical result before applying normal/negative labels.'],
  'exceptions': [],
  'verification': ['Test incomplete panels and source outages, verifying normal, negative, pending, '
                   'canceled, and missing remain semantically distinct.'],
  'owner_hints': ['designing-lab-result-review'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-lab-result-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.labresult.trend-comparability-basis-visible',
  'domain': 'labresult',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Laboratory trends must disclose when values are not directly comparable across method, '
           'unit, or reference changes',
  'statement': 'Plotting values on one line can imply comparability that does not exist after '
               'laboratory method, assay, unit, specimen type, or reference population changes.',
  'intent': 'Keep longitudinal interpretation honest when measurement basis changes over time.',
  'applies_when': ['Clinical trend views combine repeated laboratory measurements from evolving '
                   'methods, sites, or specimen contexts.'],
  'does_not_apply_when': [],
  'failure_modes': ['A years-long assay trend connects values before and after a method change with no '
                    'marker even though the numerical scales are not directly comparable.'],
  'user_impacts': ['Clinicians can infer improvement or deterioration from a discontinuity caused by '
                   'measurement methodology rather than the patient.'],
  'observables': ['Load trend fixtures with method, unit, and laboratory changes and inspect chart '
                  'segments, tooltips, normalization, and comparison warnings.'],
  'falsifiers': ['The trend either uses a validated conversion or visibly marks the comparability '
                 'boundary and exposes the changed measurement basis.'],
  'repairs': ['Carry method and context metadata into trend grouping and break or annotate series when '
              'a direct comparison is not justified.'],
  'exceptions': [],
  'verification': ['Cross method and unit changes in a longitudinal fixture and verify the '
                   'visualization never silently implies unsupported continuity.'],
  'owner_hints': ['designing-lab-result-review'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-lab-result-owners-v13'],
  'status': 'active'}]


__all__ = ["LAB_RESULT_RULES_V13"]
