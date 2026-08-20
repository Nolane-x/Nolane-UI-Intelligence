---
name: designing-audio-automation-curves
description: Use when this specialist's decision ownership is materially in scope. Own detailed audio parameter automation envelopes across volume, pan, sends, effects, modes, breakpoints, interpolation, thinning, write passes, and safe editing against the mixer.
---
# Designing Audio Automation Curves

## Parent Contract

**Required parent:** `designing-nonlinear-media-editors`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own time-varying audio mix parameters as automation lanes/envelopes. Decide parameter selection, lane visibility, breakpoint creation, interpolation, write/read/touch/latch behavior, range/units, copy, trim/offset, thinning, and synchronization with mixer controls. Generic keyframes do not fully capture real-time automation modes.

## Inputs and evidence

Require automatable audio parameters, mixer automation modes, timebase/sample precision, parameter units/ranges, write pass behavior, smoothing/thinning, clip versus track automation, plugin parameters, and history. Identify destructive overwrite modes and existing automation coverage.

## Procedure

Persistently show automation target and mode. Writing from mixer should display the generated envelope in near-real time and clearly show where existing automation will be overwritten or touched. Lane editing exposes parameter unit/value at cursor and supports breakpoints with interpolation appropriate to audio. Trim/offset changes preserve curve shape while shifting level under explicit semantics. Thin/smooth operations preview point reduction and error tolerance. Copy/paste distinguishes clip-local, track-time, and relative-time behavior.

## Failure topology

Failures include moving a fader overwriting an entire automation pass because write mode was hidden, editing wrong parameter lane, units unclear, dense captured points making curves unusable, thinning altering audible shape excessively, and clip automation confused with track automation. Another failure is changing mixer mode without the visible lane reflecting the new write policy.

## Falsification

Reject if automation mode/target cannot be identified; if write scope is unclear before moving a control; if parameter unit/range is hidden; if thinning lacks preview/tolerance; if clip versus track envelope ownership is ambiguous; if mixer and lane disagree on current automated value; or if cancel cannot restore a write pass transaction.

## Output contract

Return an `audio-automation-curves-contract` with: target parameter/owner; time basis; unit/range; automation mode; write scope; breakpoint/interpolation; lane visibility; trim/offset; thinning/smoothing; mixer synchronization; copy/paste; and undo/write-pass boundary. Include one write-mode overwrite safeguard.

## Handoffs

Audio mixer supplies controls and modes, keyframe editing supplies generic curve mechanics, timeline snapping provides temporal alignment, and final render consumes resulting automation.