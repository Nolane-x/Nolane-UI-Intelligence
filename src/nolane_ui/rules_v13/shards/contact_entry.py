"""V13 seventh-wave independently authored rules for contact entry."""
from __future__ import annotations

from ._capabilities import interaction_caps


CONTACT_ENTRY_RULES_V13 = [{'rule_id': 'ui.contact.country-selection-drives-address-schema',
  'domain': 'contact',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Address entry must adapt fields and labels from the selected country rather than one global '
           'schema',
  'statement': 'Country choice should determine relevant administrative-area labels, field order, postal '
               'conventions, and requiredness instead of forcing one country’s address grammar on all users.',
  'intent': 'Accept valid addresses without inventing universally required components.',
  'applies_when': ['The product accepts postal addresses from more than one country or territory.'],
  'does_not_apply_when': [],
  'failure_modes': ['Every address requires a US-style state and ZIP field even for countries that do not '
                    'use those concepts or place them differently.'],
  'user_impacts': ['Users can be blocked from submitting valid addresses or enter fabricated data to satisfy '
                   'an irrelevant schema.'],
  'observables': ['Switch among supported countries with materially different address formats and inspect '
                  'fields, labels, ordering, and validation.'],
  'falsifiers': ['The form changes according to a locale/country address model and does not require '
                 'inapplicable components.'],
  'repairs': ['Drive address structure from country-aware metadata and preserve already entered compatible '
              'values when the country changes.'],
  'exceptions': [],
  'verification': ['Test representative countries with and without postal codes, states, and multiple '
                   'locality lines, verifying valid real-world examples can be entered without fake data.'],
  'owner_hints': ['designing-address-entry'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-contact-entry-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.contact.postal-code-not-universally-required',
  'domain': 'contact',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Postal code validation must allow countries and territories where postal codes are absent or '
           'optional',
  'statement': 'A contact form must not make postal code universally mandatory when the selected country '
               'legitimately has no postal-code requirement.',
  'intent': 'Avoid excluding users because a locally common field was promoted into a global invariant.',
  'applies_when': ['The product accepts addresses internationally and some supported jurisdictions lack '
                   'universal postal codes.'],
  'does_not_apply_when': [],
  'failure_modes': ['The form refuses submission until users invent a ZIP or postal value for an address '
                    'that has none.'],
  'user_impacts': ['Valid customers or recipients cannot complete onboarding, checkout, or profile flows '
                   'without entering false location data.'],
  'observables': ['Select supported no-postal-code jurisdictions and submit representative valid addresses '
                  'with the field empty or absent.'],
  'falsifiers': ['Validation follows the selected country model and never demands a fabricated code solely '
                 'to satisfy a global schema.'],
  'repairs': ['Make postal requiredness country-dependent and separate carrier-specific requirements from '
              'general address validity.'],
  'exceptions': [],
  'verification': ['Exercise country changes and saved addresses, verifying requiredness updates without '
                   'corrupting previously valid data.'],
  'owner_hints': ['designing-address-entry'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-contact-entry-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.contact.phone-country-code-distinct-from-national-number',
  'domain': 'contact',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Phone entry must keep calling code selection distinct from the national subscriber number',
  'statement': 'A phone input should not silently prepend, strip, or reinterpret country calling codes based '
               'only on locale or flag presentation when storing a canonical international number.',
  'intent': 'Prevent the same visible digits from being normalized into the wrong destination.',
  'applies_when': ['Users can enter phone numbers from multiple countries and the UI provides country or '
                   'calling-code context.'],
  'does_not_apply_when': [],
  'failure_modes': ['The input stores “020…” under the wrong country because the selected flag and typed '
                    '+code disagree, or duplicates the calling code during normalization.'],
  'user_impacts': ['Verification calls or messages can be sent to the wrong person or fail despite an '
                   'apparently valid number.'],
  'observables': ['Enter national and international forms while changing the selected country and inspect '
                  'canonical stored values plus confirmation summaries.'],
  'falsifiers': ['Country calling code and national number resolve unambiguously, with conflicts surfaced '
                 'rather than silently guessed.'],
  'repairs': ['Parse phone input using explicit calling-code context and show the normalized destination for '
              'review before consequential use.'],
  'exceptions': [],
  'verification': ['Test pasted +numbers, national prefixes, and country changes, verifying round trips '
                   'preserve the intended dialable identity.'],
  'owner_hints': ['designing-phone-number-entry'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-contact-entry-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.contact.phone-extension-preserved',
  'domain': 'contact',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Phone extensions must remain separate from the base number through save, display, and dialing '
           'handoff',
  'statement': 'If the product supports extensions, it must not discard them during normalization or '
               'concatenate them into a base number that external dialers interpret incorrectly.',
  'intent': 'Preserve business contact reachability across contact storage and handoff.',
  'applies_when': ['Users can enter telephone extensions or internal routing digits with a primary number.'],
  'does_not_apply_when': [],
  'failure_modes': ['The edit form accepts an extension but the saved contact loses it, or a tap-to-call URI '
                    'sends malformed digits as part of the subscriber number.'],
  'user_impacts': ['Users can call the wrong endpoint or lose essential routing information after saving a '
                   'seemingly complete contact.'],
  'observables': ['Enter several extension syntaxes, save, reopen, export, and invoke supported dialing '
                  'handoffs.'],
  'falsifiers': ['The extension remains a distinct preserved field and every handoff uses a '
                 'platform-appropriate representation without changing the base number.'],
  'repairs': ['Store canonical base number and extension separately and format them for each output channel '
              'at the boundary.'],
  'exceptions': [],
  'verification': ['Round-trip contacts through edit, import/export, and call handoff, confirming extension '
                   'identity is never dropped or duplicated.'],
  'owner_hints': ['designing-phone-number-entry'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-contact-entry-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.contact.person-name-order-not-hardcoded',
  'domain': 'contact',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Person-name displays must not hardcode given-name then family-name order across locales',
  'statement': 'Name rendering and entry should respect locale or user-provided ordering instead of assuming '
               'one Western two-part structure.',
  'intent': 'Avoid changing identity presentation or producing awkward forms for users with different naming '
            'conventions.',
  'applies_when': ['The product stores or displays personal names for users across multiple cultures and '
                   'locales.'],
  'does_not_apply_when': [],
  'failure_modes': ['The UI always renders Firstname Lastname and sorts or addresses users from those fields '
                    'even when the locale convention is family-name first.'],
  'user_impacts': ['People can be misidentified, addressed disrespectfully, or have records sorted under the '
                   'wrong name component.'],
  'observables': ['Create profiles with supported naming structures and switch display locale, then inspect '
                  'lists, detail, greetings, and exported text.'],
  'falsifiers': ['Display order follows locale/user metadata and does not destroy the original entered name '
                 'components.'],
  'repairs': ['Use name-aware formatting rather than string concatenation and preserve structured components '
              'plus user-preferred display name.'],
  'exceptions': [],
  'verification': ['Test East Asian order, multi-part surnames, patronymics, and preferred names, verifying '
                   'output remains culturally and semantically correct.'],
  'owner_hints': ['designing-person-name-localization'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-contact-entry-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.contact.single-name-person-supported',
  'domain': 'contact',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Name validation must support people who legitimately use a single name',
  'statement': 'Identity and contact forms must not require users to invent a family or given name when the '
               'person’s valid name is mononymous.',
  'intent': 'Prevent schema convenience from forcing false identity data.',
  'applies_when': ['A product collects personal names without a legal or domain-specific requirement for two '
                   'separate name components.'],
  'does_not_apply_when': [],
  'failure_modes': ['Submission requires nonempty first and last name fields and rejects a valid person who '
                    'has only one name.'],
  'user_impacts': ['Users must fabricate data that later appears on communications, records, or verification '
                   'workflows.'],
  'observables': ['Attempt to create and edit a contact with one valid name string and inspect downstream '
                  'display and export.'],
  'falsifiers': ['The product can represent a single-name person without duplicating or inventing another '
                 'component.'],
  'repairs': ['Allow flexible name structure or provide a single full-name path while preserving structured '
              'fields only when truly applicable.'],
  'exceptions': [],
  'verification': ['Round-trip mononymous profiles through forms, lists, sorting, and exports, verifying no '
                   'artificial name component appears.'],
  'owner_hints': ['designing-person-name-localization'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-contact-entry-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.contact.autofill-review-before-consequential-submit',
  'domain': 'contact',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Autofilled contact data must remain reviewable before it is used for a consequential destination',
  'statement': 'Browser, device, or account autofill should populate fields visibly but must not bypass the '
               'user’s opportunity to review the actual address, phone, or recipient used for a '
               'consequential action.',
  'intent': 'Prevent stale autofill from silently redirecting shipments, invitations, or identity '
            'verification.',
  'applies_when': ['Contact data can be autofilled and later used for shipping, payment, account recovery, '
                   'or communication.'],
  'does_not_apply_when': [],
  'failure_modes': ['Autofill inserts an old address or phone value and the flow submits immediately or '
                    'hides the completed fields behind a collapsed summary.'],
  'user_impacts': ['Sensitive information or physical goods can be sent to an unintended destination.'],
  'observables': ['Configure several stored autofill profiles, populate the form, and inspect the review '
                  'boundary before final submission.'],
  'falsifiers': ['The exact effective contact data is visible and editable before commit, regardless of '
                 'whether it originated from autofill.'],
  'repairs': ['Treat autofill as field input rather than trusted confirmation and include effective values '
              'in the final review summary.'],
  'exceptions': [],
  'verification': ['Test stale and partial autofill plus manual overrides, verifying submission always uses '
                   'the values last shown to the user.'],
  'owner_hints': ['designing-address-entry'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-contact-entry-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.contact.normalization-does-not-destroy-user-meaning',
  'domain': 'contact',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Contact normalization must preserve meaningful user-entered information that the canonical model '
           'cannot safely infer',
  'statement': 'Whitespace, punctuation, casing, transliteration, or abbreviation cleanup must not discard '
               'apartment, building, extension, diacritic, or local addressing information merely because it '
               'is unfamiliar to a normalizer.',
  'intent': 'Keep normalization from becoming silent data loss in international contact records.',
  'applies_when': ['The system normalizes names, addresses, or phone fields before storage or transmission.'],
  'does_not_apply_when': [],
  'failure_modes': ['A normalizer removes diacritics, secondary address text, local punctuation, or script '
                    'information and the original value cannot be recovered.'],
  'user_impacts': ['Deliveries, identity matching, or respectful name display can fail because the canonical '
                   'form destroyed meaningful input.'],
  'observables': ['Enter contact data containing diacritics, local scripts, secondary units, and uncommon '
                  'punctuation, then compare input, stored model, and output.'],
  'falsifiers': ['Any normalized representation remains traceable to the original user meaning and fields '
                 'with uncertain semantics are preserved rather than erased.'],
  'repairs': ['Store canonical and display/original forms where normalization is lossy, and restrict '
              'destructive cleanup to well-defined transformations.'],
  'exceptions': [],
  'verification': ['Round-trip diverse real examples through save, edit, export, and downstream handoffs, '
                   'verifying no meaningful component disappears.'],
  'owner_hints': ['designing-person-name-localization'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-contact-entry-owners-v13'],
  'status': 'active'}]

__all__ = ["CONTACT_ENTRY_RULES_V13"]
