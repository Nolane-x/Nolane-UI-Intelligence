---
name: designing-interaction-regression-evidence
description: Use when a UI change could preserve static appearance while breaking event order, focus movement, async behavior, keyboard paths, cancellation, or multi-step task semantics and verification needs evidence of interaction sequences across revisions.
---

# Designing Interaction Regression Evidence

## What static diffs cannot prove
A UI can be pixel-identical and still regress: Enter submits twice, focus jumps behind a modal, a drag drops on the wrong target, optimistic state never rolls back, or a cancellation races with success. This skill owns the evidence model for proving behavior across meaningful event sequences, not merely final screenshots.

## Parent Contract
**Required parent:** `binding-ui-evidence`.

The parent binds claims to artifacts. This specialist is invoked when the claim concerns temporal interaction behavior and regression risk between a known baseline and a changed implementation.

## Sequence contract
Represent a regression case as `(initial_state, input_sequence, expected_intermediate_states, terminal_invariant, environment, revision)`. Inputs include pointer, keyboard, touch, assistive technology commands, timers, network responses, or programmatic events where those matter. Intermediate states are first-class because many defects are transient and disappear by the final frame.

The decision owner is which sequences deserve durable evidence. Preserve paths that cross modal boundaries, mutate data, depend on async response order, exercise undo/cancel, change focus ownership, or represent high-frequency/high-consequence tasks. Avoid recording every trivial click if its semantics are already covered by a stronger sequence.

## Event-order truth
Capture ordering whenever behavior depends on it: pointerdown before focus, validation before submit, cancellation before terminal acknowledgement, optimistic update before server reconciliation. Tests that simply wait for the final state can miss illegal intermediate behavior. Where timing is nondeterministic, assert causal constraints rather than brittle millisecond values.

User-visible feedback belongs in the sequence contract. If an action is intentionally delayed, evidence should prove that the interface communicates pending state and blocks unsafe duplicate input during that interval.

## Evidence forms
Useful evidence includes automated interaction traces, browser event logs, focus traces, state transition logs, recorded accessibility-tree changes, and targeted video when motion/order must be inspected manually. Attach revision identity and fixture data. A video without machine-checkable state may aid review but should not be the sole proof for deterministic invariants.

## Characteristic Failure
Failure includes tests that jump directly to target state, event recordings tied to unstable selectors, hidden race conditions masked by generous waits, snapshots after the bug has already self-corrected, and suites that cover mouse but not the keyboard path sharing the same feature. Another failure is false regression confidence from asserting implementation details rather than user-observable behavior.

## Falsification strategy
Deliberately reorder async responses, slow network acknowledgement, inject duplicate input, move focusable elements, cancel at boundary moments, and run the same sequence with keyboard and pointer where both are supported. The contract fails if a materially wrong intermediate state is invisible to evidence, if tests pass after breaking a user-observable invariant, or if sequence evidence cannot be replayed from a defined initial state.

## Recovery
When a sequence becomes flaky, first determine whether the product behavior is nondeterministic or the evidence harness is. Replace arbitrary sleeps with event/state synchronization, stabilize fixture identity, and narrow assertions to semantic invariants. If the interaction contract legitimately changed, version the baseline and preserve the prior expected sequence in change evidence rather than simply updating tests.

## Output
Output: `interaction-regression-evidence-contract`, containing selected sequences, initial states, causal ordering, intermediate invariants, terminal expectations, replay environment, and artifact bindings.

## Handoff and Sibling boundary
Handoff visual appearance changes to visual-regression baselines, responsive variants to responsive regression matrices, and per-state coverage to component-state evidence matrices. Sibling story-state fixture coverage supplies deterministic starting states but does not own the temporal sequence itself.

The delete-the-skill test passes because removing this owner leaves a verification gap where regressions that occur only during interaction can pass every static screenshot and final-state assertion.