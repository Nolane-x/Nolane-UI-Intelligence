"""V13 sixth-wave rules; all operational prose is independently authored."""
from __future__ import annotations

LOCALIZATION_CONTENT_RULES_V13 = [{'rule_id': 'ui.locale.fallback-language-visible',
  'domain': 'locale',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Fallback language must be discoverable when content is not available in the selected locale',
  'statement': 'If localized content falls back to another language, the interface should expose that fallback when '
               'language identity affects comprehension, trust, or the user’s ability to request the missing '
               'translation.',
  'intent': 'Prevent users from interpreting unexpected language as a broken preference, incorrect account state, or '
            'fully localized experience.',
  'applies_when': ['The product supports language negotiation and can display source or fallback language content '
                   'when a preferred translation is unavailable.'],
  'does_not_apply_when': [],
  'failure_modes': ['A page silently switches portions of content to another language with no indication that '
                    'fallback occurred or which language is being shown.'],
  'user_impacts': ['Users can misunderstand content, question whether their locale setting applied, or miss that '
                   'only part of the experience is translated.'],
  'observables': ['Remove selected-locale translations at page, component, and content-record levels and inspect '
                  'visible language identity and fallback behavior.'],
  'falsifiers': ['Fallback content is labelled or otherwise understandable in context and the product does not '
                 'falsely claim complete selected-language coverage.'],
  'repairs': ['Carry resolved content language alongside localized strings and expose fallback state where the '
              'language change is material to the task.'],
  'exceptions': [],
  'verification': ['Test primary, regional, chained, and source-language fallbacks and confirm displayed language '
                   'identity matches the actual resolved content.'],
  'owner_hints': ['designing-language-negotiation-and-fallback'],
  'verifier_hints': ['critiquing-localization'],
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
  'provenance_ids': ['nui-localization-content-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.locale.mixed-language-content-labelled',
  'domain': 'locale',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Mixed-language records must preserve language labels for content whose interpretation depends on '
           'language',
  'statement': 'When a single interface intentionally contains user-generated, translated, quoted, or source text in '
               'multiple languages, language metadata should remain available instead of assuming the surrounding UI '
               'locale applies to every segment.',
  'intent': 'Support correct pronunciation, translation, assistive-technology behavior, and user interpretation for '
            'multilingual content.',
  'applies_when': ['Content records can carry language different from the application chrome or from neighboring '
                   'records in the same view.'],
  'does_not_apply_when': [],
  'failure_modes': ['All text inherits one interface language even though individual segments are known to be '
                    'authored or translated in different languages.'],
  'user_impacts': ['Screen readers can pronounce text incorrectly and users can misidentify source versus '
                   'translation or original versus localized content.'],
  'observables': ['Render known multilingual records and inspect language metadata, translation labels, '
                  'accessibility tree, and visual distinctions.'],
  'falsifiers': ['Each materially distinct language segment retains accurate language identity or the product '
                 'explicitly states that language metadata is unknown.'],
  'repairs': ['Persist language metadata with content and apply it to semantic markup and translation presentation '
              'rather than only to interface chrome.'],
  'exceptions': [],
  'verification': ['Test mixed-language paragraphs, comments, names, quotations, and translations and confirm '
                   'language identity survives rendering and copy/export.'],
  'owner_hints': ['designing-multilingual-content-language-labeling'],
  'verifier_hints': ['critiquing-localization'],
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
  'provenance_ids': ['nui-localization-content-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.locale.plural-category-derived-from-locale',
  'domain': 'locale',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Pluralized content must use locale rules rather than English-style singular and plural assumptions',
  'statement': 'User-visible counts and messages must select plural categories from the active content locale rather '
               'than hard-coding only one-versus-many grammar that fails in languages with different plural systems.',
  'intent': 'Preserve grammatical meaning in localized interfaces where count-sensitive forms vary beyond English '
            'singular and plural.',
  'applies_when': ['The interface interpolates numeric counts into localized phrases or labels whose grammar depends '
                   'on quantity.'],
  'does_not_apply_when': [],
  'failure_modes': ['Localized copy chooses forms using a hard-coded count equals one rule even though the target '
                    'locale requires zero, dual, paucal, fractional, or other categories.'],
  'user_impacts': ['Users encounter ungrammatical or misleading messages in core status, commerce, notification, or '
                   'data interfaces.'],
  'observables': ['Render representative counts including zero, one, two, fractions, and locale-specific category '
                  'boundaries across supported locales.'],
  'falsifiers': ['Plural selection uses locale-aware message rules and all supported categories have intentional '
                 'translations or documented fallback.'],
  'repairs': ['Move plural logic into the localization message system and keep numeric formatting plus grammatical '
              'category tied to the resolved locale.'],
  'exceptions': [],
  'verification': ['Run plural-category test vectors for each supported locale and confirm dynamic counts select the '
                   'expected localized message form.'],
  'owner_hints': ['designing-localized-interfaces'],
  'verifier_hints': ['critiquing-localization'],
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
  'provenance_ids': ['nui-localization-content-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.locale.dynamic-bidi-content-isolated',
  'domain': 'locale',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Dynamic bidirectional text must be isolated so user content cannot reorder surrounding UI meaning',
  'statement': 'Names, identifiers, messages, and other dynamic text with unknown directionality must be isolated '
               'from surrounding labels so right-to-left and left-to-right runs cannot visually reorder punctuation '
               'or adjacent controls.',
  'intent': 'Protect semantic reading order and target identity when untrusted or mixed-direction text appears '
            'inside localized interfaces.',
  'applies_when': ['The interface interpolates dynamic content whose writing direction may differ from the '
                   'surrounding UI or may contain mixed bidirectional characters.'],
  'does_not_apply_when': [],
  'failure_modes': ['A right-to-left or mixed-direction value causes surrounding punctuation, labels, timestamps, or '
                    'action context to render in a misleading visual order.'],
  'user_impacts': ['Users can misread identifiers, message attribution, amounts, or action targets and may activate '
                   'controls associated with the wrong visible text.'],
  'observables': ['Inject representative RTL, LTR, mixed-script, numeric, punctuation-heavy, and isolate-control '
                  'strings into dynamic content positions.'],
  'falsifiers': ['Dynamic directional runs are isolated or semantically marked so surrounding UI order remains '
                 'stable across supported writing directions.'],
  'repairs': ['Use appropriate language and direction metadata plus bidirectional isolation at dynamic interpolation '
              'boundaries instead of concatenating raw strings.'],
  'exceptions': [],
  'verification': ['Test names, IDs, timestamps, amounts, links, and button-adjacent text under LTR and RTL UI '
                   'locales and confirm visual association remains correct.'],
  'owner_hints': ['designing-localized-interfaces'],
  'verifier_hints': ['critiquing-localization'],
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
  'provenance_ids': ['nui-localization-content-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.locale.locale-switch-preserves-task-state',
  'domain': 'locale',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Switching interface locale must preserve the current task and valid draft state',
  'statement': 'Changing language or locale during an active workflow should re-render localized presentation '
               'without discarding user input, selected records, navigation context, or unsaved draft state unless a '
               'documented boundary requires reset.',
  'intent': 'Treat locale as presentation and formatting context rather than as a reason to restart the user’s task '
            'from scratch.',
  'applies_when': ['Users can change interface language or locale without signing out and may do so while editing, '
                   'filtering, filling forms, or navigating deep product state.'],
  'does_not_apply_when': [],
  'failure_modes': ['The locale switch returns the user to a home screen, clears a valid draft, or changes the '
                    'active record even though those states are language-independent.'],
  'user_impacts': ['Multilingual users can lose work or avoid switching to a more comfortable language because doing '
                   'so disrupts the task.'],
  'observables': ['Change locale while editing, filtering, selecting, and navigating and compare stable task '
                  'identifiers and draft state before and after rerender.'],
  'falsifiers': ['The task and valid draft persist while labels, formatting, direction, and locale-dependent derived '
                 'presentation update appropriately.'],
  'repairs': ['Separate locale context from task identity and store draft/navigation state independently of '
              'localized route or component instances.'],
  'exceptions': [],
  'verification': ['Switch among supported locales during forms, editors, searches, and details and confirm only '
                   'locale-dependent presentation changes.'],
  'owner_hints': ['designing-localized-interfaces'],
  'verifier_hints': ['critiquing-localization'],
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
  'provenance_ids': ['nui-localization-content-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.locale.untranslated-placeholder-not-shipped',
  'domain': 'locale',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Unresolved translation keys and localization placeholders must not reach production UI',
  'statement': 'Production interfaces must not expose raw message keys, template placeholders, pseudo-localization '
               'markers, or developer fallback strings as if they were user-facing translated content.',
  'intent': 'Catch localization pipeline failures that are mechanically detectable and erode comprehension '
            'immediately.',
  'applies_when': ['The application resolves user-facing strings through translation keys, templates, message '
                   'catalogs, or runtime localization bundles.'],
  'does_not_apply_when': [],
  'failure_modes': ['A missing resource renders text such as a key path, placeholder token, pseudo-localized marker, '
                    'or internal developer fallback in the production surface.'],
  'user_impacts': ['Users can encounter incomprehensible controls, errors, or instructions and may be unable to '
                   'complete the task.'],
  'observables': ['Remove representative translations and inspect production-mode rendering, logs, bundle fallback, '
                  'and all user-visible text surfaces.'],
  'falsifiers': ['Missing translations fail closed to an intentional human-readable fallback or are blocked before '
                 'release rather than exposing implementation tokens.'],
  'repairs': ['Validate translation coverage in build/release gates and reserve explicit human-readable fallback '
              'content for genuinely supported fallback behavior.'],
  'exceptions': [],
  'verification': ['Scan representative production builds for unresolved keys and intentionally remove resources to '
                   'confirm missing translations cannot silently ship as placeholders.'],
  'owner_hints': ['designing-pseudolocalization-stress-testing'],
  'verifier_hints': ['critiquing-localization'],
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
  'provenance_ids': ['nui-localization-content-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.locale.translation-staleness-visible',
  'domain': 'locale',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Translated content must not silently present an outdated source revision as current',
  'statement': 'When source content changes after a translation was produced, systems that can detect the revision '
               'mismatch should mark the translation stale or require revalidation instead of treating it as current '
               'equivalence.',
  'intent': 'Preserve content truth in products where translated policy, instructions, help, or operational text can '
            'lag behind an updated source.',
  'applies_when': ['The product stores source and translated content with revision identity or enough metadata to '
                   'know that the source changed after translation.'],
  'does_not_apply_when': [],
  'failure_modes': ['A translation from an older source revision remains published with no stale indication after '
                    'materially different source content replaces the original.'],
  'user_impacts': ['Users in one language can receive outdated instructions, policy, status, or safety information '
                   'while other locales show the current version.'],
  'observables': ['Publish a translation, modify the source revision without retranslating, and inspect translation '
                  'workflow state plus public rendering.'],
  'falsifiers': ['Revision mismatch moves translation into stale, review-needed, fallback, or explicitly accepted '
                 'state before it is represented as current.'],
  'repairs': ['Track translation provenance to source revision and invalidate current-equivalence status when the '
              'source changes materially.'],
  'exceptions': [],
  'verification': ['Test minor and major source edits, approved exceptions, fallback behavior, and retranslation and '
                   'confirm stale status follows revision provenance.'],
  'owner_hints': ['designing-content-localization-workflows'],
  'verifier_hints': ['critiquing-localization'],
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
  'provenance_ids': ['nui-localization-content-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.locale.truncation-preserves-distinguishing-content',
  'domain': 'locale',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Localized truncation must preserve the content needed to distinguish nearby choices',
  'statement': 'When labels expand in translation, truncation or compression must not remove the distinguishing '
               'noun, qualifier, amount, destination, or state that separates one actionable option from another.',
  'intent': 'Keep localized interfaces operable when translated strings exceed layouts designed around shorter '
            'source-language copy.',
  'applies_when': ['Multiple actionable labels or records can become visually similar after localization expansion '
                   'and the layout truncates or clamps their text.'],
  'does_not_apply_when': [],
  'failure_modes': ['Two different actions or records render with identical visible prefixes because the differing '
                    'semantic fragment is clipped.'],
  'user_impacts': ['Users can activate the wrong option or be unable to distinguish destinations, plans, files, or '
                   'statuses in the localized UI.'],
  'observables': ['Apply long translated labels and text-size expansion to adjacent choices and compare full strings '
                  'with visible differentiated content.'],
  'falsifiers': ['Layout, wrapping, alternate wording, tooltip/detail, or prioritized truncation preserves enough '
                 'visible context to distinguish each choice.'],
  'repairs': ['Design for translation expansion and prioritize semantically distinguishing segments rather than '
              'applying uniform end truncation to all labels.'],
  'exceptions': [],
  'verification': ['Stress-test supported locales, long names, dynamic values, and larger text and confirm '
                   'actionable choices never collapse to the same visible meaning.'],
  'owner_hints': ['designing-translation-expansion-resilience'],
  'verifier_hints': ['critiquing-localization'],
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
  'provenance_ids': ['nui-localization-content-owners-v13'],
  'status': 'active'}]

__all__ = ["LOCALIZATION_CONTENT_RULES_V13"]
