"""V13 eighth-wave independently authored rules for quizauthor."""
from __future__ import annotations

from ._capabilities import interaction_caps


QUIZ_AUTHOR_RULES_V13 = [{'rule_id': 'ui.quizauthor.draft-distinct-from-published-version',
  'domain': 'quizauthor',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Quiz drafts must remain distinct from the version currently delivered to learners',
  'statement': 'Editing questions after publication should not silently mutate the assessment already '
               'assigned or in progress unless the product explicitly supports live version '
               'replacement.',
  'intent': 'Preserve delivery stability while instructors continue authoring future changes.',
  'applies_when': ['Quiz authoring allows instructors to edit content that may already have a published '
                   'learner-facing version.'],
  'does_not_apply_when': [],
  'failure_modes': ['An instructor fixes wording in a draft and active learner attempts immediately '
                    'receive the edited question without a new publication boundary.'],
  'user_impacts': ['Learners can be assessed on different content under what appears to be the same '
                   'quiz version.'],
  'observables': ['Publish a quiz, start learner attempts, edit the draft, and compare learner '
                  'delivery, preview, version history, and publish state.'],
  'falsifiers': ['Draft edits remain isolated until explicit publication and active attempts stay bound '
                 'to their assigned version according to product policy.'],
  'repairs': ['Version published assessment content and make authoring operate on a separate draft '
              'lineage with a deliberate release transition.'],
  'exceptions': [],
  'verification': ['Edit during active attempts and verify learner content changes only at the '
                   'documented publication and assignment boundary.'],
  'owner_hints': ['designing-quiz-authoring'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-quiz-author-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.quizauthor.answer-key-hidden-from-learner-preview',
  'domain': 'quizauthor',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Learner preview must not expose answer keys, scoring metadata, or instructor-only '
           'rationales',
  'statement': 'Previewing the learner experience should render only content that the target learner '
               'role is authorized to see, even though the author workspace has answer and scoring data '
               'loaded.',
  'intent': 'Prevent accidental disclosure of correct answers through author preview mode.',
  'applies_when': ['Quiz authors can switch between instructor editing and learner-facing preview '
                   'within the same session.'],
  'does_not_apply_when': [],
  'failure_modes': ['A learner preview hides the answer-key panel but leaves correct-option classes or '
                    'rationale data in accessible DOM attributes and tooltips.'],
  'user_impacts': ['Assessment integrity can be compromised because privileged authoring metadata leaks '
                   'into the learner surface.'],
  'observables': ['Open learner preview with answer keys and rationales present in the author model and '
                  'inspect visible UI, DOM, accessibility tree, and network payloads.'],
  'falsifiers': ['Learner preview exposes only data authorized for the learner role and no hidden '
                 'presentation artifact reveals correct-answer metadata.'],
  'repairs': ['Use role-scoped preview data and render from the learner contract rather than merely '
              'hiding instructor controls with CSS.'],
  'exceptions': [],
  'verification': ['Test multiple question types and rationales, verifying learner preview contains no '
                   'answer-key or scoring metadata beyond the configured release policy.'],
  'owner_hints': ['designing-quiz-authoring'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-quiz-author-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.quizauthor.scoring-weight-total-valid',
  'domain': 'quizauthor',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Quiz scoring weights must be validated against the intended total before publication',
  'statement': 'Point values, weighted sections, bonus items, and partial-credit settings can interact, '
               'so the authoring UI must surface inconsistent totals rather than publishing an '
               'unintended grade model.',
  'intent': 'Prevent assessment scores from being distorted by configuration arithmetic the author did '
            'not review.',
  'applies_when': ['Quiz authors can assign points or weights at item, section, category, or bonus '
                   'levels.'],
  'does_not_apply_when': [],
  'failure_modes': ['Editing a section weight leaves the overall configuration at 115% but publish '
                    'succeeds and learner grades are normalized unpredictably.'],
  'user_impacts': ['Learner grades can be mathematically inconsistent with the assessment design and '
                   'difficult to explain or correct.'],
  'observables': ['Configure edge-case scoring totals and inspect validation, previewed grade examples, '
                  'publication, and exported configuration.'],
  'falsifiers': ['The effective scoring model reconciles to the documented total or explicitly supports '
                 'and explains the alternative calculation.'],
  'repairs': ['Compute the score model from structured weights and block publication on contradictory '
              'totals unless a deliberate supported mode applies.'],
  'exceptions': [],
  'verification': ['Test zero, overfull, underfull, bonus, and mixed point/weight configurations, '
                   'verifying the published scoring basis matches author review.'],
  'owner_hints': ['designing-quiz-authoring'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-quiz-author-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.quizauthor.randomization-pool-configuration-valid',
  'domain': 'quizauthor',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Randomized quiz pools must expose whether they can satisfy the requested draw without '
           'duplication or omission',
  'statement': 'Pool size, draw count, exclusions, categories, and reuse policy should be validated '
               'together so authors know the delivered assessment can actually meet its randomization '
               'contract.',
  'intent': 'Prevent runtime assessment generation from failing or silently changing distribution '
            'because the pool is underspecified.',
  'applies_when': ['Quiz authoring supports drawing random items or variants from configured pools and '
                   'constraints.'],
  'does_not_apply_when': [],
  'failure_modes': ['An author requests ten unique questions from a filtered pool that currently '
                    'contains eight, but the builder publishes without warning and later repeats '
                    'items.'],
  'user_impacts': ['Learners can receive invalid or inconsistent assessments because the authoring tool '
                   'accepted an impossible randomization plan.'],
  'observables': ['Create pools with changing membership, exclusions, and draw counts and inspect '
                  'validation, preview samples, and publication behavior.'],
  'falsifiers': ['The builder evaluates the effective eligible pool and discloses any shortage or reuse '
                 'policy before publication.'],
  'repairs': ['Validate randomization constraints against current pool membership and version the pool '
              'configuration used by published assessments.'],
  'exceptions': [],
  'verification': ['Shrink and expand pools around the requested draw size, verifying publication and '
                   'learner generation follow the disclosed uniqueness rules.'],
  'owner_hints': ['designing-quiz-authoring'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-quiz-author-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.quizauthor.preview-uses-target-delivery-config',
  'domain': 'quizauthor',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Quiz preview must use the target learner delivery configuration rather than generic author '
           'defaults',
  'statement': 'Navigation rules, timing, feedback visibility, randomization, attempts, and '
               'accommodations can materially change the learner experience and should be represented '
               'in preview.',
  'intent': 'Let authors review the assessment they will actually deliver instead of a simplified '
            'editor simulation.',
  'applies_when': ['Quiz settings control learner-facing delivery behavior beyond the question content '
                   'itself.'],
  'does_not_apply_when': [],
  'failure_modes': ['The author preview always allows back navigation even though the published quiz is '
                    'configured as sequential no-return.'],
  'user_impacts': ['Authors can approve a flow that differs from the real learner experience and '
                   'discover problems only after launch.'],
  'observables': ['Configure varied delivery policies and compare preview behavior with a real learner '
                  'test attempt under the same version.'],
  'falsifiers': ['Preview declares the target role and effective delivery configuration and reproduces '
                 'the relevant learner interaction constraints.'],
  'repairs': ['Instantiate preview from the same versioned delivery contract used to create learner '
              'attempts rather than hardcoded author-mode defaults.'],
  'exceptions': [],
  'verification': ['Compare previews and learner attempts across timing, navigation, feedback, and '
                   'randomization settings, verifying behavioral parity where promised.'],
  'owner_hints': ['designing-quiz-authoring'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-quiz-author-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.quizauthor.question-delete-reference-impact-visible',
  'domain': 'quizauthor',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Deleting a quiz question must reveal references that will break or change across pools and '
           'published content',
  'statement': 'Questions can be reused by pools, sections, prerequisites, analytics, or prior '
               'versions, so deletion should distinguish removing a draft reference from destroying a '
               'shared item.',
  'intent': 'Prevent authors from unintentionally invalidating other assessments or historical '
            'references.',
  'applies_when': ['Question banks allow one item to be referenced by multiple quizzes, pools, or '
                   'versions.'],
  'does_not_apply_when': [],
  'failure_modes': ['An author deletes a question from one quiz and the shared bank item is destroyed, '
                    'causing another published assessment to lose its reference.'],
  'user_impacts': ['Other assessments can break or historical interpretation can change because '
                   'reference scope was hidden.'],
  'observables': ['Create shared and unshared question references, then test remove-from-quiz, archive, '
                  'and destructive-delete actions while inspecting dependents.'],
  'falsifiers': ['Each destructive action discloses the affected references and distinguishes unlinking '
                 'from global deletion or archival.'],
  'repairs': ['Model content identity separately from assessment membership and perform dependency '
              'analysis before destructive item deletion.'],
  'exceptions': [],
  'verification': ['Delete and unlink questions with several reference patterns, verifying only the '
                   'confirmed dependency scope changes.'],
  'owner_hints': ['designing-quiz-authoring'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-quiz-author-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.quizauthor.media-asset-availability-verified',
  'domain': 'quizauthor',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Quiz publication must verify required media assets are available to the learner audience',
  'statement': 'Images, audio, video, documents, and external embeds can exist in the author session '
               'while still being inaccessible to learners because of permissions, expiry, or '
               'processing state.',
  'intent': 'Prevent publishing questions whose essential media cannot be delivered to the target '
            'audience.',
  'applies_when': ['Quiz questions can depend on uploaded, linked, transcoded, or access-controlled '
                   'media assets.'],
  'does_not_apply_when': [],
  'failure_modes': ['An instructor can play an authenticated video in the editor, but learners receive '
                    'a permission error because the asset was never shared to the course scope.'],
  'user_impacts': ['Learners can be unable to answer questions whose essential prompt material is '
                   'unavailable.'],
  'observables': ['Publish with pending, private, expired, and broken media and test access using the '
                  'learner delivery identity.'],
  'falsifiers': ['Required media has a verified learner-accessible readiness state or publication '
                 'surfaces a blocking dependency instead of assuming author access is sufficient.'],
  'repairs': ['Validate asset processing and audience authorization against the target delivery context '
              'before publication.'],
  'exceptions': [],
  'verification': ['Test each supported media type under author-only and learner-accessible '
                   'permissions, verifying publication reflects actual delivery readiness.'],
  'owner_hints': ['designing-quiz-authoring'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-quiz-author-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.quizauthor.publish-creates-versioned-assessment',
  'domain': 'quizauthor',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Publishing a quiz must create an identifiable assessment version rather than mutating an '
           'anonymous current state',
  'statement': 'A published assessment should have a stable version identity so attempts, analytics, '
               'grading, and later edits can refer to the exact configuration learners received.',
  'intent': 'Preserve reproducibility and historical interpretation across repeated quiz releases.',
  'applies_when': ['Authors can publish, edit, republish, and assign quizzes over time.'],
  'does_not_apply_when': [],
  'failure_modes': ['The builder has only a “published” boolean; republishing overwrites question text '
                    'and settings for every historical attempt with no version boundary.'],
  'user_impacts': ['Grades and learner experiences become impossible to reconstruct after later author '
                   'edits.'],
  'observables': ['Publish several revisions and inspect attempt metadata, gradebook, analytics, '
                  'preview links, and version history.'],
  'falsifiers': ['Each published release has stable identity and historical attempts remain bound to '
                 'the version delivered at attempt creation.'],
  'repairs': ['Create immutable publication snapshots or equivalent version records and make '
              'assignments reference those versions explicitly.'],
  'exceptions': [],
  'verification': ['Republish with question and setting changes, verifying old attempts retain their '
                   'original content and scoring configuration.'],
  'owner_hints': ['designing-quiz-authoring'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-quiz-author-owners-v13'],
  'status': 'active'}]


__all__ = ["QUIZ_AUTHOR_RULES_V13"]
