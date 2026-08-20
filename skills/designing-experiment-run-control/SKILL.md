---
name: designing-experiment-run-control
description: Use when this specialist's decision ownership is materially in scope. Own start, pause, resume, stop, abort, phase progression, live run status, operator authority, and outcome distinction for active scientific or engineering experiments.
---
# Designing Experiment Run Control

## Parent Contract

**Required parent:** `designing-scientific-and-engineering-instrumentation`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the lifecycle of an active experiment run. Decide start authorization, phase/state model, elapsed and remaining progress, pause/resume, graceful stop versus emergency abort, operator ownership, mid-run annotations, parameter-change boundaries, and terminal outcome classification. This owner does not design instrument-specific control algorithms.

## Inputs and evidence

Require frozen run manifest, phase sequence, start prerequisites, control commands, safe pause/stop/abort capabilities, operator roles, timing model, live measurement dependencies, allowed mid-run edits, storage state, and recovery after disconnect. Identify actions with irreversible sample or equipment consequences.

## Procedure

Show one authoritative run state and current phase with start time, operator, setup version, and relevant control authority. Start should recheck volatile prerequisites. Distinguish pause, stop, abort, failed, completed, and interrupted—these outcomes carry different scientific meaning. Any allowed mid-run parameter change must record old/new value, time, actor, and applicable phase. If the UI loses connection, do not assume the run stopped; show control uncertainty and recover actual device state before enabling commands. Terminal completion requires both execution state and data-finalization status.

## Failure topology

Failures include duplicate starts from latency, a disconnect making a running experiment appear stopped, stop and abort presented as equivalent, mid-run changes hidden from results, elapsed time continuing after terminal state, and data write failure while UI reports completed. Another failure is a single operator control bar remaining enabled after authority transfers.

## Falsification

Reject if run state can diverge from device/runtime with no uncertainty cue; if stop versus abort consequences are unclear; if a parameter can change without provenance; if reconnect enables controls before authoritative state is recovered; if completed can be shown while required data is not finalized; or if an irreversible abort lacks an appropriate consequence boundary.

## Output contract

Return an `experiment-run-control-contract` with: run states/phases; start preflight; operator/authority; command semantics; duplicate-action protection; pause/stop/abort consequences; connection uncertainty; mid-run change provenance; timing; annotations; terminal outcome; and data-finalization gate. Include one disconnect-during-run scenario.

## Handoffs

Setup provides the run manifest, live signal monitoring provides evidence, setpoint/interlock owners govern allowed control changes, and provenance captures all state transitions.