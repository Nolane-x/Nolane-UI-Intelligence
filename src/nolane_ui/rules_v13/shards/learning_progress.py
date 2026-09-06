"""V13 eighth-wave independently authored rules for learning."""
from __future__ import annotations

from ._capabilities import interaction_caps


LEARNING_PROGRESS_RULES_V13 = [{'rule_id': 'ui.learning.completion-distinct-from-mastery',
  'domain': 'learning',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Learning completion must remain distinct from demonstrated mastery or proficiency',
  'statement': 'Finishing content, viewing a lesson, or submitting an activity does not necessarily '
               'prove mastery, so the interface should not collapse these concepts into one progress '
               'state.',
  'intent': 'Keep learner and instructor decisions aligned with what each progress indicator actually '
            'measures.',
  'applies_when': ['Learning products track both content completion and outcomes such as mastery, '
                   'passing, or proficiency.'],
  'does_not_apply_when': [],
  'failure_modes': ['A learner watches every lesson and the dashboard marks the course mastered even '
                    'though required assessments remain below the proficiency threshold.'],
  'user_impacts': ['Learners and instructors can misread engagement completion as evidence that '
                   'learning objectives were achieved.'],
  'observables': ['Complete content with varying assessment outcomes and compare progress bars, '
                  'certificates, prerequisites, and instructor analytics.'],
  'falsifiers': ['Completion and mastery have separate definitions, can diverge, and are labeled '
                 'consistently across learner and instructor surfaces.'],
  'repairs': ['Model activity completion and mastery evidence as distinct state dimensions and derive '
              'aggregate indicators from explicit rules.'],
  'exceptions': [],
  'verification': ['Test high-completion/low-mastery and low-completion/high-mastery cases, verifying '
                   'neither state overwrites the other.'],
  'owner_hints': ['designing-learning-progress-tracking'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-learning-progress-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.learning.progress-freshness-visible',
  'domain': 'learning',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Learning progress summaries must expose when their data are delayed or not yet reconciled',
  'statement': 'Progress can lag behind activity events, grading, or external learning tools, so '
               'dashboards should not present stale percentages as current without a freshness '
               'boundary.',
  'intent': 'Prevent learners and instructors from acting on progress that silently excludes recent '
            'work.',
  'applies_when': ['Learning progress aggregates events from lessons, assessments, external tools, or '
                   'batch calculations.'],
  'does_not_apply_when': [],
  'failure_modes': ['A learner completes a module but the dashboard remains at 60% for hours with no '
                    'indication that synchronization is pending.'],
  'user_impacts': ['Learners can repeat work or instructors can intervene unnecessarily because the '
                   'stale state looks authoritative.'],
  'observables': ['Delay progress aggregation and external tool sync while observing timestamps, '
                  'pending indicators, and recalculation behavior.'],
  'falsifiers': ['The interface reveals pending or stale aggregation when recent activity has not yet '
                 'been incorporated and converges when processing completes.'],
  'repairs': ['Carry aggregation watermark or freshness metadata with progress summaries and expose '
              'background reconciliation state.'],
  'exceptions': [],
  'verification': ['Inject delayed completion and grading events, verifying the dashboard never '
                   'presents an outdated rollup as freshly authoritative.'],
  'owner_hints': ['designing-learning-progress-tracking'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-learning-progress-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.learning.cross-device-progress-reconciled',
  'domain': 'learning',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Cross-device learning progress must reconcile concurrent activity without silently losing '
           'either device history',
  'statement': 'Learners can switch phones, browsers, and offline sessions, so conflicting completion '
               'and position updates require stable event identity and reconciliation.',
  'intent': 'Preserve learning history when multiple devices report progress out of order.',
  'applies_when': ['Learning products sync reading position, lesson completion, notes, or quiz progress '
                   'across devices.'],
  'does_not_apply_when': [],
  'failure_modes': ['A phone reports lesson completion after a laptop sends an older in-progress '
                    'checkpoint, and the late stale event rolls the learner backward to incomplete.'],
  'user_impacts': ['Learners can lose earned progress or resume at the wrong location because '
                   'last-arriving data was treated as authoritative.'],
  'observables': ['Generate ordered and out-of-order progress events from two devices and inspect '
                  'timeline, completion state, and resume position.'],
  'falsifiers': ['Reconciliation preserves monotonic completion where appropriate and applies explicit '
                 'conflict rules to non-monotonic state such as position or reset.'],
  'repairs': ['Use event identity, logical ordering, and domain-specific merge rules instead of blind '
              'last-write-wins for progress synchronization.'],
  'exceptions': [],
  'verification': ['Race offline and online device updates, verifying completion and resume state '
                   'converge according to the documented reconciliation contract.'],
  'owner_hints': ['designing-learning-progress-tracking'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-learning-progress-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.learning.prerequisite-effective-state-visible',
  'domain': 'learning',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Prerequisite gates must show the effective requirement and why content is currently locked '
           'or unlocked',
  'statement': 'Learners should be able to distinguish missing completion, missing mastery, schedule '
               'restrictions, enrollment policy, or stale sync from a generic disabled lesson.',
  'intent': 'Make progression rules understandable and debuggable without exposing hidden '
            'implementation details.',
  'applies_when': ['Courses can lock activities based on completion, mastery, dates, enrollment, or '
                   'other prerequisite conditions.'],
  'does_not_apply_when': [],
  'failure_modes': ['A lesson is grayed out with no explanation even though the learner completed the '
                    'stated prerequisite and the real blocker is a pending grade sync.'],
  'user_impacts': ['Learners can waste time repeating work or seek support because the true gate '
                   'condition is invisible.'],
  'observables': ['Configure different prerequisite types and partially satisfied states, then inspect '
                  'learner lock messaging and instructor diagnostics.'],
  'falsifiers': ['The UI identifies the effective prerequisite condition and current satisfaction state '
                 'without implying a different requirement.'],
  'repairs': ['Compile prerequisite policy into inspectable gate reasons and separate evaluation errors '
              'or stale data from genuinely unmet requirements.'],
  'exceptions': [],
  'verification': ['Test every prerequisite type plus sync failure, verifying locked and unlocked '
                   'states match the disclosed effective conditions.'],
  'owner_hints': ['designing-learning-progress-tracking'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-learning-progress-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.learning.reset-semantics-confirmed',
  'domain': 'learning',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Resetting learner progress must confirm exactly which history, mastery, attempts, and '
           'completion state will change',
  'statement': 'A reset can mean restart one activity, clear a course, reopen attempts, or erase '
               'mastery evidence; the interface must disclose that scope before destructive commitment.',
  'intent': 'Prevent support or instructors from erasing more learning history than intended.',
  'applies_when': ['Learning products allow users or administrators to reset progress at several '
                   'scopes.'],
  'does_not_apply_when': [],
  'failure_modes': ['An administrator clicks Reset Course intending to reopen content, but the '
                    'operation also deletes assessment attempts and mastery evidence without warning.'],
  'user_impacts': ['Learner history, grades, or certification eligibility can be irreversibly altered '
                   'beyond the requested recovery action.'],
  'observables': ['Preview and execute resets at activity, module, and course scope while inspecting '
                  'history, attempts, mastery, certificates, and audit records.'],
  'falsifiers': ['The confirmation enumerates affected state dimensions and committed changes match '
                 'that disclosed scope exactly.'],
  'repairs': ['Separate reset operations by state dimension or compile a precise mutation plan for '
              'explicit confirmation before execution.'],
  'exceptions': [],
  'verification': ['Run narrow and broad resets, verifying unaffected history remains intact and every '
                   'changed dimension was named before commit.'],
  'owner_hints': ['designing-learning-progress-tracking'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-learning-progress-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.learning.partial-credit-aggregation-consistent',
  'domain': 'learning',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Learning progress aggregation must apply partial credit consistently across item, activity, '
           'and course rollups',
  'statement': 'When partial credit contributes to mastery or completion, the learner and instructor '
               'views should use the same documented aggregation basis instead of independent rounding '
               'or thresholds.',
  'intent': 'Prevent contradictory progress and mastery outcomes from inconsistent score aggregation.',
  'applies_when': ['Courses aggregate scores with partial credit, weighted activities, mastery '
                   'thresholds, or dropped items.'],
  'does_not_apply_when': [],
  'failure_modes': ['A learner sees 80% mastery in the activity while the course rollup shows 70% '
                    'because one surface rounds item credit before weighting and the other rounds '
                    'after.'],
  'user_impacts': ['Learners and instructors cannot explain progression or eligibility decisions from '
                   'inconsistent calculations.'],
  'observables': ['Construct edge-case partial scores and compare item totals, activity grade, mastery '
                  'state, course rollup, and export.'],
  'falsifiers': ['All surfaces derive from one score aggregation contract and any rounding occurs at '
                 'documented boundaries.'],
  'repairs': ['Centralize scoring aggregation semantics and expose enough basis for downstream progress '
              'calculations to reproduce the result.'],
  'exceptions': [],
  'verification': ['Test fractional scores, weights, thresholds, and rounding boundaries, verifying '
                   'every rollup agrees on the same source values.'],
  'owner_hints': ['designing-learning-progress-tracking'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-learning-progress-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.learning.hidden-content-progress-impact-visible',
  'domain': 'learning',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Hiding or unpublishing learning content must expose its impact on existing learner progress '
           'and completion rules',
  'statement': 'Content visibility changes can alter denominator, prerequisites, or completion '
               'requirements, so authors should know how historical and future progress will be '
               'interpreted.',
  'intent': 'Prevent course edits from silently changing learner completion percentages or eligibility.',
  'applies_when': ['Instructors can hide, archive, or unpublish activities after learners have already '
                   'interacted with them.'],
  'does_not_apply_when': [],
  'failure_modes': ['A completed required activity is hidden and instantly removed from the '
                    'denominator, causing some learners to jump to 100% and others to lose prerequisite '
                    'evidence.'],
  'user_impacts': ['Progress can change without learner action because course structure edits rewrote '
                   'the aggregation basis invisibly.'],
  'observables': ['Hide completed and incomplete required activities and compare learner rollups, '
                  'prerequisites, historical completion, and instructor analytics.'],
  'falsifiers': ['The product defines and exposes whether hidden content still counts historically, is '
                 'excluded prospectively, or triggers a version boundary.'],
  'repairs': ['Version progress requirements or apply explicit historical-content rules instead of '
              'recomputing old progress from the mutable current course tree.'],
  'exceptions': [],
  'verification': ['Change visibility after mixed learner completion and verify rollups follow the '
                   'disclosed policy without unexplained retroactive shifts.'],
  'owner_hints': ['designing-learning-progress-tracking'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-learning-progress-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.learning.course-version-migration-preserves-progress',
  'domain': 'learning',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Migrating learners to a new course version must preserve or explicitly transform existing '
           'progress',
  'statement': 'When content structure changes, prior completion, mastery, and position should map '
               'through a reviewed migration rather than being silently discarded or attached to the '
               'wrong new activity.',
  'intent': 'Keep learner history coherent across curriculum revisions.',
  'applies_when': ['Courses can publish new versions with renamed, split, merged, added, or removed '
                   'activities.'],
  'does_not_apply_when': [],
  'failure_modes': ['A completed old lesson is replaced by two new lessons and migration marks both '
                    'complete without a mapping rule or resets the learner to zero with no '
                    'explanation.'],
  'user_impacts': ['Learners can receive unearned completion or lose legitimate progress when '
                   'curriculum structure changes.'],
  'observables': ['Create version migrations with one-to-one, split, merge, added, and removed content '
                  'and inspect before/after learner state.'],
  'falsifiers': ['Every migrated progress state is explainable by an explicit mapping or policy, and '
                 'unmapped history remains visible instead of disappearing.'],
  'repairs': ['Use versioned content identities plus declared migration mappings and keep historical '
              'progress attached to the source version.'],
  'exceptions': [],
  'verification': ['Migrate representative learner histories and verify completion, mastery, and audit '
                   'records match the reviewed mapping plan.'],
  'owner_hints': ['designing-learning-progress-tracking'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-learning-progress-owners-v13'],
  'status': 'active'}]


__all__ = ["LEARNING_PROGRESS_RULES_V13"]
