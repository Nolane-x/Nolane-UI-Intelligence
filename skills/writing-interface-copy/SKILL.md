---
name: writing-interface-copy
description: Use when labels, controls, onboarding, help, status, validation, errors, empty states, confirmations, or other interface text materially affects comprehension and action.
---

# Writing Interface Copy

## Overview
Words are interaction material. UI copy should help users identify objects, predict actions, understand state, and recover—without sounding like marketing filler inside operational controls.

## Parent Contract
**Required parent:** `routing-ui-work`.

Use product vocabulary, user expertise, task flow, state model, brand voice, and localization constraints.

## Vocabulary system
Create a small lexicon of key product nouns and verbs. Use one concept consistently across navigation, headings, controls, status, docs hints, and feedback. Backend/service names are not user vocabulary unless users genuinely work with them.

## Action labels
Label buttons/menu items by the result they cause: `Save changes`, `Invite members`, `Archive project`. Avoid vague `Submit`, `Continue`, or `Yes` when the consequence can be named.

For destructive actions, identify the target and consequence. Confirmation copy should not use cleverness or emotional pressure.

## Labels, help, examples
Each string has one job:
- label identifies
- description explains purpose/consequence
- example demonstrates format/content
- placeholder hints at input only when helpful
- tooltip supplements; it does not host essential instructions

Remove duplicate prose that restates visible controls.

## Status and system voice
State what happened, what is happening, or what the user can do next. Avoid pretending the system has human feelings. Keep action vocabulary consistent: `Publish` → `Published`, not `Publish` → `Successfully deployed your content!` unless deploy is genuinely the same product concept.

## Errors
A useful error answers:
1. what failed, in user terms
2. what data/state was preserved
3. what the user can do now
4. whether retry may duplicate an effect

Do not blame the user or expose irrelevant infrastructure detail.

## Empty states
Explain why the space is empty only when ambiguity exists. Offer the next valuable action when one exists. Avoid decorative motivational copy that delays orientation.

## Expert interfaces
Favor compact, precise language and stable terminology. Repeated explanatory text can become friction; use contextual help/disclosure where needed.

## Localization readiness
Avoid strings constructed by concatenating fragments whose order may change across languages. Expect length expansion and grammatical variation. Keep text out of raster/generated imagery when it must be localized or interactive.

## Output: `content-contract`
Return `lexicon`, `voice_rules`, `action_labels`, `status_patterns`, `error_patterns`, `empty_state_rules`, `help_rules`, `localization_constraints`, and `copy_invariants`.

## Generic-copy detector
Challenge words such as seamless, powerful, supercharge, unlock, next-generation, effortless, intelligent, revolutionary when they do not describe a concrete user outcome. Specificity is usually more credible than hype.
