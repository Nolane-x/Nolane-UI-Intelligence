---
name: designing-forms
description: Use when users must enter, edit, validate, review, submit, or recover structured data and form behavior can affect comprehension, errors, permissions, or task completion.
---

# Designing Forms

## Overview
Forms are conversations with constraints. Optimize for accurate completion and recovery, not visual compactness alone.

## Parent Contract
**Required parent:** `routing-ui-work`.

Consume the task flow, field semantics, validation rules, and permission model. Do not invent required fields to make the layout symmetrical.

## Field necessity
For each field ask:
- is this needed to complete the current user goal?
- can the system derive it safely?
- can it be deferred until it is actually needed?
- does the user understand the requested concept in product vocabulary?

Remove administrative data collection from the primary flow unless it has a real dependency.

## Grouping and order
Order fields by the user’s decision process, not database schema. Group fields that share meaning or dependency. Separate risky/advanced configuration when it would distract from the main task.

## Labels and help
Persistent labels identify the field. Placeholders may demonstrate format but must not carry the only label. Help text explains a non-obvious requirement; do not repeat the label in prose.

## Validation strategy
Classify validation:
- syntactic and safe to validate locally
- semantic and requires server/domain knowledge
- cross-field dependency
- warning that permits continuation
- blocking error

Validate at the earliest moment that provides useful feedback without interrupting normal typing. Do not produce error states for incomplete input while the user is still entering a value unless immediate constraint feedback is genuinely helpful.

Error messages identify the problem and next action. Preserve user-entered data after failure unless security/product policy forbids it.

## Submission/async behavior
On submit define accepted, pending, success, partial, duplicate, failure, timeout/unknown, and retry behavior where applicable. Prevent duplicate effects, but do not freeze the entire page when only one operation is pending.

## Multi-step forms
Split only when steps have meaningful dependency, cognitive boundaries, or save/resume value. Show progress when it helps orientation, not as decorative ceremony. Preserve data across back/forward navigation.

## Dangerous changes
For settings with large consequences, expose scope and downstream effects near the decision. Confirmation should reference the specific changed value/target, not generic “Are you sure?” text.

## Output: `form-contract`
Return `fields`, `grouping`, `order`, `dependencies`, `validation_map`, `error_copy_requirements`, `async_states`, `submission_policy`, `persistence_policy`, `accessibility_requirements`, and `stress_cases`.

## Stress cases
Empty optional section, all fields invalid, one server error, slow validation, long translated labels, autofill, password manager, keyboard-only completion, paste of formatted data, and return to a saved draft when relevant.

## V6 Form Behavior Engineering
Model dependencies before layout with a **field-dependency graph**: visibility, requiredness, defaults, validation, computed values, and option sets that change when another field changes. Cycles and hidden dependencies require explicit resolution, especially when edits can invalidate later answers.

Choose a **validation-timing policy** per rule. Syntax may validate on blur or after meaningful input; cross-field/business rules may require submit or server evidence; destructive or expensive validation should not fire on every keystroke. Prevent premature error noise while ensuring the user sees failures before a costly commit. For long or consequential forms, define a **draft-persistence contract** covering autosave cadence, device/account scope, conflict handling, privacy-sensitive fields, expiry, and recovery after interruption.

For multi-error submission, design an **error-summary focus path**: summary placement, first-invalid focus strategy, inline linkage, preserved entered values, and announcement. Audit browser/platform behavior with an **autofill-and-input-mode audit**—correct input type, autocomplete tokens, password manager semantics, numeric/date keyboards, paste, IME composition, and locale-specific formats.

### Falsification
Change an upstream dependency after filling downstream fields, submit with several errors, navigate away mid-edit, autofill the form, paste localized values, and retry under slow server validation. Data loss, hidden invalid values, or focus stranded from errors falsifies the form contract.

### Recovery
Repair data/dependency semantics first, restore lost draft paths, then adjust presentation. Never disable paste/autofill merely to make validation simpler.
