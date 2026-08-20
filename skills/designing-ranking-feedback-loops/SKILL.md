---
name: designing-ranking-feedback-loops
description: Use when clicks, skips, dwell, hides, ratings, saves, purchases, completions, or explicit feedback can influence future ranking and the interface must prevent ambiguous signals, runaway reinforcement, accidental feedback, and misleading immediate effects.
---

# Designing Ranking Feedback Loops

Every feedback control or inferred behavior creates a loop: the system observes an action, changes ranking, and the changed ranking alters future behavior. Interface design must distinguish explicit user intent from noisy behavioral evidence and keep the loop correctable.

## Parent Contract
**Required parent:** `designing-recommendation-personalization-surfaces`.

The parent owns recommendation presentation. This skill owns user-event semantics, feedback acknowledgement, correction, and interface safeguards around ranking reinforcement.

## Signal Semantics
Classify explicit positive/negative feedback separately from implicit behavior. A click can indicate interest, confusion, accidental activation, or need to inspect. Long dwell can mean enjoyment or difficulty. Do not present inferred signals to users as if they were deliberate preferences.

For explicit actions, make the consequence proportionate and understandable. “Not interested” may reduce similar items; “block creator” has stronger scope; “report” is a trust/safety action and should not be used merely as negative ranking feedback. Keep these intents separate in analytics and UI.

## Feedback Acknowledgement
After explicit feedback, confirm what changed and provide undo where feasible. Avoid instant full-feed reshuffle that destroys orientation unless the action explicitly asks to refresh. The model may update asynchronously; do not promise an immediate ranking effect the system cannot guarantee.

## Reinforcement Risk
Repeated exposure itself creates feedback. Popular items can collect more interactions because they were ranked highly, narrowing diversity. UI-level mitigations may include exploration slots, “see less like this,” diversity controls, or reset paths, but algorithmic policy remains outside this skill. The interface should not hide feedback loops behind claims of neutral relevance.

## Event Integrity
Deduplicate repeated clicks/retries, ignore programmatic or hidden impressions, and bind feedback to the recommendation event/item/context that produced it. When users act from search or direct navigation rather than a recommendation, avoid attributing the event to the wrong ranking surface.

## Evidence
Trace explicit hide, undo, accidental click, repeated view, purchase after recommendation, skip, and report. Compare UI acknowledgement with emitted events and downstream ranking effects. Test cross-device duplicate events and item reappearance after negative feedback.

## Failure Modes
- Every click is treated as positive preference.
- Report-abuse is reused as ordinary recommendation dislike.
- Negative feedback instantly destroys scroll position through full rerank.
- Feedback event lacks recommendation-context identity.
- Retry emits duplicate strong negative signals.
- UI says “we'll show less” but the ranking pipeline never receives the event.
- Implicit inference is displayed as user-authored preference.

## Falsification
Send explicit negative feedback, undo it, then replay the same network request. Falsify if duplicate events amplify the signal or undo does not reverse the durable preference event according to product semantics.

## Recovery
Strengthen event identity, separate intent classes, deduplicate, expose bounded effect/undo, and avoid promises until downstream acknowledgement exists. If ranking behavior cannot be observed, claim only that feedback was received—not that recommendations have changed.

## Handoff
Durable settings use `designing-personalization-controls`; diversity effects use `designing-recommendation-diversity-controls`; explanations should reflect only actual signals through `designing-recommendation-explanations`.

## Output Contract
Return a `ranking-feedback-loops-contract` with `signal_classes[]`, `explicit_vs_implicit_boundary`, `event_identity`, `acknowledgement_copy`, `undo_semantics`, `rerank_stability`, `deduplication_rules`, `reinforcement_risks[]`, `evidence_cases[]`, and `recovery_actions[]`.