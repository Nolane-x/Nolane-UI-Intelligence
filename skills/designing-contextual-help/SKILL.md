---
name: designing-contextual-help
description: Use when users need explanation at the point of uncertainty and the product must connect help to the current task, state, terminology, or error without replacing usable interface design with walls of instruction.
---

# Designing Contextual Help

## Parent Contract
**Required parent:** `designing-onboarding`.

This faculty owns help that appears because of the current product context: field-level explanation, “learn more” for a concept, a task-specific help drawer, error-linked guidance, or a lightweight explainer beside an unfamiliar domain term. It does not own the global help-center architecture or a proactive coach mark.

## Decision Boundary
Place help where uncertainty arises, but require a reason for every explanatory affordance. If a label can simply be made clearer, fix the label rather than attaching a tooltip that restates it. Contextual help is appropriate for domain concepts, irreversible consequences, complex configuration, rare workflows, or a failure whose remedy requires more than one sentence.

Bind help to the current state. A generic article about “permissions” is weak when the user is blocked because inherited workspace policy disables one control. Pass enough safe context to select the relevant section without leaking secrets or private object data into external documentation systems. If help opens a drawer or side panel, preserve the user's current task and focus origin so they can compare guidance with the interface rather than abandoning it.

Help content has version and ownership. A renamed setting or changed workflow can make contextual guidance actively harmful. Prefer canonical documentation identifiers and deep anchors over copied prose embedded in many components. When offline or help content fails to load, essential instructions for a blocking state must still have a local fallback.

## Failure Topology
- Every ambiguous label gains a question-mark icon instead of being rewritten clearly.
- Help link opens a generic homepage and users must search again for the exact issue.
- Support URL contains raw customer IDs, secret tokens, or form contents as query parameters.
- Side-panel help steals navigation state and closing it returns focus to the page top.
- Embedded guidance describes an old control name after product redesign.
- Critical recovery instructions disappear because the external docs service is unavailable.

## Falsification and Recovery
Falsify with permission-blocked controls, validation errors, renamed product terminology, offline mode, docs version drift, keyboard/screen-reader activation, mobile viewport, and external-help load failure. The design fails if help requires the user to reconstruct the context they already had in the product or if opening help destroys the task state they are trying to understand.

Recover by first improving interface clarity, binding help links to semantic topic IDs and current state, minimizing transmitted context, preserving task/focus state, versioning documentation targets, and keeping essential blocking guidance locally available.

## Output Contract
Return `contextual-help-contract` with help-eligible uncertainty classes, placement, context binding, topic identifiers, privacy-safe parameters, task/focus preservation, documentation versioning, offline/failure fallback, accessibility behavior, and falsification cases.