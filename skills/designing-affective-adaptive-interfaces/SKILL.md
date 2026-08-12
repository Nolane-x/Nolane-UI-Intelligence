---
name: designing-affective-adaptive-interfaces
description: Use when an interface senses, infers, represents, or adapts to a person’s affective state, emotion-related signals, stress, engagement, or other inferred internal condition.
---

# Designing Affective Adaptive Interfaces

## Overview
Affective adaptation is not a decorative personalization feature. It creates an inference loop in which a system observes imperfect signals about a person, assigns meaning to those signals, and changes the interface or behavior in response. Every link in that loop can be wrong, culturally narrow, privacy-invasive, manipulative, or difficult for the user to notice. The design objective is therefore not “detect emotion accurately.” It is to make the inference boundary, adaptation authority, uncertainty, consent, reversibility, and user control explicit enough that a wrong inference cannot silently become a wrong decision.

## Parent Contract
**Required parent:** `routing-ui-work`.

Consume a `ui-task-profile` that identifies the purpose of affective sensing or adaptation, affected users, signal sources, risk class, privacy context, and whether adaptation is assistive, cosmetic, persuasive, safety-related, or consequential. If the product cannot name a legitimate user benefit that requires affect inference rather than ordinary explicit preference, return a scope finding instead of inventing an emotion model.

## Decision Model
### 1. Separate observation from interpretation
Record each input channel such as explicit self-report, interaction pace, voice prosody, facial features, physiological signal, or contextual state. Do not collapse a sensor event into an emotion label. Model `signal -> feature -> inference -> confidence -> temporal validity -> proposed adaptation` so the user-facing behavior remains traceable.

### 2. Classify adaptation authority
Place every adaptation in one of four levels: presentation-only, reversible assistance, workflow steering, or consequential action. Presentation-only changes may be automatic when they are harmless and stable. Assistance should remain easy to undo. Workflow steering needs visible rationale and a non-adaptive path. Consequential action must not be authorized solely by an affect inference; route it to the applicable safety, consent, or high-stakes faculty.

### 3. Treat affect as uncertain and person-dependent
Do not assume a universal mapping from expression, physiology, language, disability, culture, or behavior to a single internal state. Preserve confidence, ambiguity, recency, baseline, and person-specific calibration. A low-confidence state should usually reduce adaptation strength rather than trigger a dramatic mode shift. Do not infer clinical diagnosis from an interface-level affect signal.

### 4. Make adaptation legible and stoppable
When adaptation materially changes content, priority, tone, difficulty, recommendation, or interaction, provide an understandable cue, a way to inspect why it changed, a stable manual override, and a way to pause or disable adaptation without losing the underlying task. Avoid interfaces that continuously move controls or rewrite structure based on transient inference.

### 5. Protect consent and privacy
Define what is sensed, where inference occurs, retention, sharing, secondary use, and deletion. Route sensitive sensing through `designing-permissions-and-consent`, `designing-privacy-sensitive-interfaces`, and independent security/privacy critique. Consent for one signal or purpose does not imply permission for another. Do not use emotional vulnerability to intensify coercive sales, engagement, or urgency patterns.

### 6. Test population and context variance
Validate with representative users and environments. Test false positives, false negatives, conflicting channels, inaccessible signals, atypical expression, assistive technology, noisy environments, and users who intentionally mask or exaggerate expression. Adaptation must degrade to a coherent non-affective interface when sensing is unavailable or refused.

## Evidence
Prefer published standards and primary empirical evidence over vendor emotion labels. ISO/IEC 30150-1:2022 establishes a model for affective-computing user interfaces; later 30150 parts under development must be labeled as drafts rather than treated as released requirements. Product evidence should include signal provenance, validation population, error characteristics, calibration method, consent record, and observed user outcomes. A classifier accuracy number without population, class balance, context, or consequence analysis is insufficient evidence for interface authority.

## Output Contract
Produce an `affective-adaptation-contract` containing: purpose; signal inventory; inference chain; confidence and freshness rules; adaptation authority levels; automatic versus confirm-required behaviors; user-visible explanation; pause/override/reset controls; consent and retention boundaries; fallback non-affective experience; protected or vulnerable-use exclusions; representative validation plan; cross-cultural and accessibility risks; and mandatory independent critics. Mark every consequential behavior that cannot be justified without stronger evidence as `BLOCKED`, not “best effort.”

## Failure Traps
- Treating an emotion label as ground truth rather than an inference.
- Assuming facial, vocal, behavioral, or physiological signals have universal meaning.
- Quietly changing prices, permissions, safety decisions, or irreversible actions because the system thinks the user is stressed or receptive.
- Asking for broad consent once and reusing affect data for unrelated purposes.
- Making controls move, disappear, or change semantics continuously as inferred state fluctuates.
- Hiding the non-adaptive path so refusal becomes a degraded punishment.
- Calling an affect model unbiased because aggregate accuracy is high.
- Using emotional vulnerability to increase pressure, scarcity, or persuasive manipulation.
- Presenting a draft standard as a published normative requirement.

The interface succeeds when affective intelligence remains subordinate to user agency: useful when right, bounded when uncertain, obvious when material, and safe when wrong.
