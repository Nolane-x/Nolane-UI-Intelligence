---
name: designing-press-feedback-motion
description: Use when a pressable control needs temporal feedback that distinguishes contact, commitment, cancellation and release without adding latency or implying an action before it is accepted.
---

# Designing Press Feedback Motion

## Parent Contract
**Required parent:** `designing-motion`.

This specialist owns the few hundred milliseconds around a press: the visible or tactile acknowledgment that a pointer, finger, pen, key-equivalent or remote activation has contacted a control and the transition back to rest after commitment or cancellation. It does not decide whether the control is a button, what action it performs, or whether destructive confirmation is required.

## Decision Boundary
Press feedback is not decoration and is not the same as hover. Its job is to answer three questions quickly: **did the system receive contact, is the control still eligible to activate, and did release commit or cancel the action?** The motion must therefore follow the interaction state machine rather than a prewritten animation timeline.

Model at least `rest → contact → armed → committed|cancelled → rest`. A pointer that leaves the activation region while held may become disarmed; a touch gesture may cross a movement threshold and become scroll instead; a disabled control never enters an armed visual state. If the platform activates on key-up, do not visually claim completion on key-down.

Use amplitude proportional to the physical metaphor and visual weight. A compact toolbar icon can use a tiny scale, fill, opacity or surface compression; a large tactile control may justify more displacement. Avoid large scale shrinkage that changes hit geometry or makes adjacent controls appear to move. Feedback should begin fast enough to feel causally attached to contact, but it must not delay the action while waiting for an animation to finish.

For asynchronous actions, separate **press acknowledgment** from **pending/progress state**. A spinner that appears after network latency cannot substitute for immediate contact feedback. Likewise, a success flourish must not be fused into the press animation when the operation can fail.

Keyboard and switch activation need an equivalent state signal even when there is no literal pointer-down event. Reduced-motion mode may replace scale or translation with instantaneous tone/border/elevation changes; the information that contact was received must remain.

## Failure Topology
- A button animates only after the server responds, making the control feel dead during latency.
- Scale-down moves labels or nearby layout because transform isolation was not preserved.
- A pressed visual remains stuck after pointer cancellation, lost capture, modal interruption or route change.
- Touch scrolling accidentally triggers a press animation that reads as commitment.
- Press and selected/toggled states use the same appearance, so users cannot tell transient contact from persistent state.
- The animation is beautiful at 60 fps but becomes a delayed, queued echo under main-thread load.

## Falsification and Recovery
Falsify the design with rapid repeated presses, press-drag-out-release, touch scroll initiation, keyboard activation, disabled transition during hold, route interruption and low-performance throttling. If the control can visually claim a committed action that did not occur, or fail to acknowledge a valid contact promptly, the contract fails.

Recover by simplifying the temporal grammar: first guarantee state-correct immediate acknowledgment, then add only motion that survives cancellation and degraded performance. Prefer state-derived rendering over imperative animation queues.

## Output Contract
Return `press-feedback-motion-contract` containing activation modalities, press state machine, visual/tactile channels, contact and release timing, cancellation behavior, async handoff, reduced-motion equivalent, performance fallback and runtime tests.