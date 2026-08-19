---
name: designing-undo-redo-history
description: Use when interactive work supports undo and redo and the product must define command granularity, state restoration, async effects, history branching, remote changes and user-visible recovery semantics.
---

# Designing Undo and Redo History

## Parent Contract
**Required parent:** `designing-interactions`.

This faculty owns user-facing reversible history semantics. Version history and collaborative conflict resolution are siblings; backend transactional compensation may be required for external effects.

## Decision Model
Define an undoable command as a semantic user intention, not every low-level event. Typing may group characters by pause/context; dragging an object should usually be one command from start to final transform; applying a multi-field form can be one transaction if users perceive it as one action. Bad granularity makes undo either uselessly microscopic or dangerously broad.

Undo must restore all state that makes the command coherent: data, selection/focus where appropriate, hierarchy and derived view state—but not necessarily unrelated viewport position. Redo is the inverse of an undone command only while the history branch remains valid. A new edit after undo commonly truncates the redo branch unless the product exposes branching history.

Async/external effects require honesty. Sending an email, charging a card or publishing remotely may not be truly undoable; offer compensating actions such as recall/refund only when supported and label them by actual consequence. Do not add an “Undo” toast that merely changes local UI while the external effect remains.

Collaboration complicates ownership. Local undo should typically undo the user’s own compatible actions rather than rewind other collaborators’ work wholesale.

## Failure Topology
- Drag produces hundreds of history entries, so one undo moves a single pixel.
- Undoing a delete restores the object but not its parent/order/links.
- A new edit after undo leaves Redo enabled but replays onto incompatible state.
- “Undo send” hides the message locally after it was already delivered.
- Collaborative undo reverses another user’s later edits.
- History stack survives document switch and applies commands to the wrong context.

## Falsification and Recovery
Perform grouped typing, drag, multi-object edit, delete/restore, undo-then-new-edit, async action, document switch and concurrent remote update. Reapply undo/redo round trips and compare semantic state, not screenshots.

Recover by redefining command boundaries, storing sufficient inverse/context data, disabling impossible redo branches and replacing fake undo with explicit compensating actions.

## Output Contract
Return `undo-redo-history-contract` with command granularity, grouping rules, captured state, branch behavior, async/irreversible policy, collaboration ownership, context scope, UI affordances and round-trip tests.