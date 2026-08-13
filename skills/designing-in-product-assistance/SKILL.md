---
name: designing-in-product-assistance
description: Use when users need contextual help, explanations, guidance, coaching, troubleshooting, examples, recovery assistance, or escalation while operating an interactive system beyond initial onboarding.
---

# Designing In Product Assistance

## Overview
User assistance is a support layer for moments when the interface, task, domain, failure state, or user knowledge leaves a meaningful gap. It is not a license to leave primary interaction unclear and attach tooltips everywhere. Good assistance appears at the point of need, answers the actual question, preserves task context, and disappears when competence grows. It also distinguishes explanation from instruction, instruction from automated action, and automated action from support escalation.

## Parent Contract
**Required parent:** `routing-ui-work`.

Consume the task model, user expertise, information architecture, error/recovery states, terminology, accessibility/localization requirements, product support boundaries, and evidence about where users actually fail or seek help. If the underlying control can be made self-explanatory without adding cognitive cost, fix the interface first. Route assistance only where a legitimate knowledge, procedural, diagnostic, or recovery gap remains.

## Decision Model
### 1. Classify the assistance need
Separate orientation, conceptual explanation, procedural guidance, field-level help, examples, error diagnosis, troubleshooting, feature discovery, policy explanation, and human-support escalation. Each need has different timing and depth. A tooltip is rarely an appropriate troubleshooting system; a long article is rarely appropriate for a single ambiguous field.

### 2. Choose trigger and timing
Assistance can be user-invoked, contextually suggested, event-triggered, or proactively surfaced. Prefer user control for interruptive or lengthy guidance. Proactive assistance requires strong evidence of need and should not repeatedly interrupt competent users. Never infer confusion solely from hesitation and then hijack the workflow.

### 3. Preserve task context
Keep the object, state, data, and user progress visible when possible. Deep help can open a separate surface, but returning must restore context. If guidance asks the user to perform steps, reflect completion and changed state rather than forcing memorization across windows.

### 4. Make help layered and searchable
Start with the smallest answer that resolves the likely question, then offer deeper rationale, examples, edge cases, and references. Use the same terminology as the product. Connect search synonyms to canonical concepts. Avoid duplicate documentation that contradicts the live interface because one copy was not updated.

### 5. Design assistance for failure and uncertainty
For errors, state what happened, what remains safe, what the user can do next, and whether retry changes anything. Troubleshooting should narrow causes through observable evidence rather than blame. When the system does not know, say so and provide an escalation path instead of fabricating certainty.

### 6. Bound automation inside assistance
A helper may suggest or execute actions, especially when AI is present. Suggestions must identify scope and consequence; execution inherits normal permission, confirmation, target-binding, provenance, and undo rules. “Fix it for me” does not bypass `designing-agent-autonomy-and-control` or security gates.

### 7. Support accessibility, localization, and learning
Assistance must work with keyboard, screen readers, zoom/reflow, alternative input, captions/media alternatives where relevant, and localized content expansion. Do not place essential instructions only in hover content. Preserve user choice between concise and detailed guidance where cognitive needs differ.

### 8. Measure whether assistance reduces friction
Track task recovery, repeated help invocation, abandonment, support escalation, successful search, and whether assistance causes new errors. High help usage can indicate valuable support or a broken primary UI; interpret it with task evidence rather than celebrating engagement.

## Evidence
ISO/FDIS 9241-130 is in the Final Draft approval stage in 2026 and addresses user assistance within interactive systems, including selection, usage, dependencies, and platform-independent guidance. Its draft status means it is a research signal, not a released normative requirement. The older ISO 9241-13:1998 remains the publication being replaced. Combine standards status with support logs, usability research, search queries, error telemetry, observed task breakdowns, accessibility evaluation, and content governance evidence.

## Output Contract
Produce a `user-assistance-contract` containing: assistance need taxonomy; user segments/expertise; trigger rules; proactive-surfacing threshold; contextual anchor; layer/depth model; terminology/source-of-truth; help search and synonym strategy; task-state preservation; procedural progress behavior; error/troubleshooting decision tree; uncertainty language; escalation path; automated-action boundaries; accessibility/localization obligations; stale-content ownership and versioning; analytics/evaluation plan; retirement criteria for assistance made unnecessary by UI improvements; and unresolved evidence gaps.

## Failure Traps
- Using tooltips to compensate for labels or controls that can simply be clearer.
- Showing a product tour every time instead of learning whether the user needs it.
- Opening help that destroys the exact task state the user was trying to understand.
- Writing different terminology in help and in the interface.
- Treating repeated help clicks as proof the assistance is successful.
- Giving troubleshooting steps without explaining what state is safe or whether retry is idempotent.
- Letting an AI helper execute privileged actions because the interaction began as “help.”
- Hiding essential instructions in hover-only or inaccessible overlays.
- Keeping documentation after behavior changed, creating a second contradictory product.
- Treating a Final Draft standard as already published.

The assistance succeeds when users recover knowledge or control with minimal interruption, remain in command of the task, and need progressively less help as the interface and their understanding improve.

## V6 In-Product Assistance Protocol
Trigger help from **help-trigger context**—user goal, current object/state, error, permission, expertise, and action—not just the screen name. Store a **task-resume anchor** so opening docs, walkthrough, support, or assistant does not lose the user's place or entered state.

Design **progressive help depth** from inline cue → short explanation → worked example → reference → human/support where appropriate. Add **stale-help detection** tied to product version, permissions, platform, and feature flags. Run an **assistance dependency test**: frequent successful users should not require repeating a tutorial because the core interface is unclear.

### Falsification
Change product state/version, open help mid-error, leave/return, and attempt the task after assistance is removed. Misleading/stale guidance falsifies the help system.

### Recovery
Update contextual linkage/content, preserve resume state, and fix the underlying interaction where help is compensating for avoidable ambiguity.
