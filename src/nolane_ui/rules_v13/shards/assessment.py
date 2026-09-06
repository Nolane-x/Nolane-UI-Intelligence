"""V13 eighth-wave independently authored rules for assessment."""
from __future__ import annotations

from ._capabilities import interaction_caps


ASSESSMENT_RULES_V13 = [{'rule_id': 'ui.assessment.attempt-state-preserved-across-navigation',
  'domain': 'assessment',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Assessment attempt state must remain stable while learners navigate among questions and '
           'sections',
  'statement': 'Navigation should not create a new attempt, reset answered state, or detach progress '
               'from the current attempt identity unless the assessment explicitly starts a new '
               'attempt.',
  'intent': 'Preserve learner work and scoring context across ordinary movement through an assessment.',
  'applies_when': ['Learners can move between questions, sections, review pages, and reconnect to an '
                   'in-progress assessment.'],
  'does_not_apply_when': [],
  'failure_modes': ['Returning to an earlier section silently initializes a new attempt token and '
                    'previously answered questions appear unanswered.'],
  'user_impacts': ['Learners can lose work or submit a fragmented attempt that does not match the '
                   'questions they actually completed.'],
  'observables': ['Navigate forward, backward, refresh, and reconnect while checking attempt '
                  'identifier, answers, flags, timer, and completion state.'],
  'falsifiers': ['All ordinary navigation remains bound to one attempt identity and existing attempt '
                 'state rehydrates consistently.'],
  'repairs': ['Keep attempt identity above page-level routes and require an explicit start-over '
              'transition to create a new attempt.'],
  'exceptions': [],
  'verification': ['Exercise navigation, refresh, and reconnect across multiple sections and verify one '
                   'attempt state remains authoritative until submission or reset.'],
  'owner_hints': ['designing-assessment-question-navigation'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-assessment-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.assessment.unsaved-response-protected-on-navigation',
  'domain': 'assessment',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Unsaved assessment responses must be protected before navigation can discard them',
  'statement': 'When response persistence is delayed or explicit, moving away from a question must not '
               'silently lose learner input or imply that it was saved when it was not.',
  'intent': 'Prevent navigation from destroying assessment work during latency or connectivity gaps.',
  'applies_when': ['Assessment answers can remain locally edited while autosave or explicit save is '
                   'still pending.'],
  'does_not_apply_when': [],
  'failure_modes': ['A learner types a long response and immediately opens the next question; the route '
                    'changes before autosave completes and the answer disappears.'],
  'user_impacts': ['Learners lose scored work and may not realize the submitted attempt is incomplete.'],
  'observables': ['Introduce slow and failed persistence while navigating away from edited questions '
                  'and inspect save indicators and restored state.'],
  'falsifiers': ['Navigation waits, preserves local work, or explicitly warns about unsaved state, and '
                 'returning to the question never fabricates a saved response.'],
  'repairs': ['Bind navigation to response persistence state and retain local drafts until server '
              'acknowledgement or deliberate discard.'],
  'exceptions': [],
  'verification': ['Race autosave with next, previous, section jump, refresh, and timeout actions, '
                   'verifying unsaved content is never silently lost.'],
  'owner_hints': ['designing-assessment-question-navigation'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-assessment-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.assessment.flagged-question-state-persistent',
  'domain': 'assessment',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Learner question flags must persist as attempt state rather than transient page decoration',
  'statement': 'Marking an item for review should survive navigation, refresh, and resume so the review '
               'queue reflects the learner’s actual decisions within the attempt.',
  'intent': 'Keep review workflows dependable during long or interrupted assessments.',
  'applies_when': ['Assessment interfaces allow learners to flag questions for later review before '
                   'final submission.'],
  'does_not_apply_when': [],
  'failure_modes': ['A flag appears in the question header but disappears after refresh while the '
                    'review summary still shows an inconsistent count.'],
  'user_impacts': ['Learners can unintentionally submit questions they meant to revisit because review '
                   'markers are not durable.'],
  'observables': ['Flag and unflag several questions, then navigate, refresh, reconnect, and inspect '
                  'question map plus final review page.'],
  'falsifiers': ['Flag state remains consistent across every representation of the same attempt until '
                 'the learner changes it or the attempt ends.'],
  'repairs': ['Persist review flags in attempt state using stable question identity and update all '
              'navigation summaries from that source.'],
  'exceptions': [],
  'verification': ['Interrupt and resume flagged assessments, verifying question-level markers and '
                   'aggregate review counts always agree.'],
  'owner_hints': ['designing-assessment-question-navigation'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-assessment-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.assessment.submission-distinct-from-scoring',
  'domain': 'assessment',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Assessment submission must remain distinct from scoring, grading, and result publication',
  'statement': 'Successfully submitting an attempt means responses were accepted, not necessarily that '
               'all items were scored or that results are ready for the learner.',
  'intent': 'Prevent completion feedback from overstating grading state in mixed automatic and manual '
            'assessments.',
  'applies_when': ['Assessments can include auto-scored, manually graded, moderated, or delayed-result '
                   'items.'],
  'does_not_apply_when': [],
  'failure_modes': ['A submitted essay assessment immediately shows “100% complete” using only '
                    'auto-scored items, implying final grading is finished.'],
  'user_impacts': ['Learners and instructors can act on incomplete or provisional grades as if they '
                   'were final.'],
  'observables': ['Submit attempts containing automatic and manual items and inspect confirmation, '
                  'gradebook, learner results, and notification states.'],
  'falsifiers': ['Submission receipt, scoring progress, grading completion, and result publication are '
                 'separate lifecycle states.'],
  'repairs': ['Model submission and grading pipelines independently and render each state according to '
              'its own authority.'],
  'exceptions': [],
  'verification': ['Exercise all-auto, mixed, delayed, and rescored attempts and verify submission '
                   'success never masquerades as final grade availability.'],
  'owner_hints': ['designing-assessment-question-navigation'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-assessment-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.assessment.time-limit-authority-visible',
  'domain': 'assessment',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Assessment time limits must show the authoritative clock basis and remaining time semantics',
  'statement': 'Learners need to know whether the timer is server-based, section-based, paused by '
               'accommodation, or affected by connectivity, because visual countdown alone is not '
               'enough authority.',
  'intent': 'Prevent client clock drift or hidden pause rules from changing the effective assessment '
            'deadline.',
  'applies_when': ['Assessments impose attempt or section time limits that can interact with reconnect, '
                   'pause, or accommodations.'],
  'does_not_apply_when': [],
  'failure_modes': ['A browser timer pauses while offline even though the server deadline continues, so '
                    'the learner sees five minutes remaining after the attempt has already expired.'],
  'user_impacts': ['Learners can lose responses or receive inconsistent time treatment because the '
                   'visible timer did not represent the real deadline.'],
  'observables': ['Change client clocks, disconnect, resume, switch sections, and apply accommodations '
                  'while comparing visible timer to authoritative deadline.'],
  'falsifiers': ['The UI exposes the effective remaining time from the authoritative timing policy and '
                 'represents pauses or extensions explicitly.'],
  'repairs': ['Derive countdown from a server or policy-owned deadline and reconcile client display '
              'after connectivity or accommodation changes.'],
  'exceptions': [],
  'verification': ['Run clock-skew and reconnect tests across standard and accommodated attempts, '
                   'verifying expiration occurs exactly at the disclosed authority boundary.'],
  'owner_hints': ['designing-assessment-question-navigation'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-assessment-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.assessment.accommodation-effective-state-visible',
  'domain': 'assessment',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Assessment accommodations must show the effective attempt configuration before the learner '
           'begins or resumes',
  'statement': 'Extended time, extra attempts, breaks, navigation changes, or other accommodations '
               'should be visible as effective state rather than hidden administrative metadata.',
  'intent': 'Ensure the learner and proctor can verify that approved accommodations actually apply to '
            'the current attempt.',
  'applies_when': ['Assessments support learner-specific accommodations that alter timing, attempts, or '
                   'interaction policy.'],
  'does_not_apply_when': [],
  'failure_modes': ['An accommodation exists in the profile but the current assessment launches with '
                    'the default time limit and no warning.'],
  'user_impacts': ['Learners can be unfairly constrained because approved conditions were not applied '
                   'to the active attempt.'],
  'observables': ['Configure accommodations before and after attempt creation and inspect launch '
                  'summary, timer, navigation, and attempt limits.'],
  'falsifiers': ['The attempt exposes the effective accommodation configuration and conflicts are '
                 'resolved before assessment work begins.'],
  'repairs': ['Compile accommodations into the attempt configuration at a defined boundary and surface '
              'the effective values to authorized users.'],
  'exceptions': [],
  'verification': ['Test supported accommodations across fresh and resumed attempts, verifying the live '
                   'attempt behavior matches the disclosed effective state.'],
  'owner_hints': ['designing-assessment-question-navigation'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-assessment-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.assessment.randomized-item-identity-stable',
  'domain': 'assessment',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Randomized assessment items must keep stable attempt-local identity after delivery',
  'statement': 'Randomization can choose or reorder questions, but once an attempt receives an item, '
               'answers, flags, scoring, and review must continue referencing that same delivered item '
               'identity.',
  'intent': 'Prevent rerender or resume from attaching learner responses to a different randomized '
            'question.',
  'applies_when': ['Assessments randomize item order, variants, pools, or parameterized questions per '
                   'attempt.'],
  'does_not_apply_when': [],
  'failure_modes': ['A refresh reruns random selection and item slot 5 now contains a different '
                    'question while the prior answer is still attached to slot 5.'],
  'user_impacts': ['Learner responses can be scored against questions they never answered or review '
                   'history can become incoherent.'],
  'observables': ['Start randomized attempts, answer and flag items, then refresh, resume on another '
                  'device, and inspect the delivered item set.'],
  'falsifiers': ['The attempt’s delivered item identities and variants remain fixed after selection '
                 'even if presentation order changes intentionally.'],
  'repairs': ['Persist the randomized delivery plan with the attempt and bind answers to item identity '
              'rather than ordinal position.'],
  'exceptions': [],
  'verification': ['Reconnect and resume randomized attempts repeatedly, verifying each response, flag, '
                   'and score stays attached to the originally delivered item.'],
  'owner_hints': ['designing-assessment-question-navigation'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-assessment-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.assessment.section-lock-boundary-visible',
  'domain': 'assessment',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Locked assessment sections must disclose the irreversible navigation boundary before the '
           'learner crosses it',
  'statement': 'If advancing prevents return to earlier questions, the interface must make that policy '
               'and affected section explicit before committing the transition.',
  'intent': 'Prevent learners from losing review access because a normal-looking next action secretly '
            'crosses a lock boundary.',
  'applies_when': ['Assessments can enforce sequential sections or no-return policies for security or '
                   'test design reasons.'],
  'does_not_apply_when': [],
  'failure_modes': ['A learner clicks Next from the final question of a section and only afterward '
                    'discovers the entire section is permanently locked.'],
  'user_impacts': ['Learners can lose the chance to review unanswered or flagged items without informed '
                   'consent to the boundary.'],
  'observables': ['Approach section transitions with unanswered and flagged items and inspect '
                  'pre-transition messaging, review access, and back navigation.'],
  'falsifiers': ['The interface identifies the affected section and no-return consequence before the '
                 'lock commits and accurately reflects locked state afterward.'],
  'repairs': ['Treat section advancement as a consequential workflow transition with explicit '
              'confirmation when it changes future navigation rights.'],
  'exceptions': [],
  'verification': ['Test lock boundaries with incomplete and complete sections, verifying no-return '
                   'behavior matches the pre-commit disclosure exactly.'],
  'owner_hints': ['designing-assessment-question-navigation'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-assessment-owners-v13'],
  'status': 'active'}]


__all__ = ["ASSESSMENT_RULES_V13"]
