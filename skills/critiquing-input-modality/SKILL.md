---
name: critiquing-input-modality
description: Use when a UI depends on keyboard, pointer, touch, pen, drag, remote, gamepad, voice, gaze, gestures, haptics, switch control, or mixed inputs and complete reachability must be independently verified.
---

# Critiquing Input Modality

## Overview
Verify the complete task across every modality promised or required. Do not equate focusability with operability or pointer success with interaction parity.

## Parent Contract
**Required parent:** `challenging-ui-designs`.

**May modify:** false. Consume applicable modality contracts, action vocabulary, focus graph, platform scope, and accessibility obligations. Test rendered/runtime behavior whenever the evidence method requires it.

## Decision Model
Build an action inventory from real task flows: navigate, select, activate, adjust, move/reorder, reveal information, dismiss, submit, cancel, undo, and recover. For each applicable modality, prove a reachable path. Differences in mechanics are acceptable; missing functionality is not.

Inspect target and focus behavior. Keyboard/switch paths need logical grouping and no dead ends. Remote/gamepad paths need deterministic directional edges and Back/Escape. Pointer/touch needs adequate geometry, cancellation, and no hover-only essentials. Dragging needs an equivalent non-drag route when required. Voice needs stable names and ambiguity repair. Gaze requires separation of attention from intent. Haptics/audio cannot be the only critical carrier.

Test modality switching. Selection, current object, mode, and task state should not unexpectedly reset when users move from touch to keyboard, pen to pointer, or voice to screen. Custom canvas/editor controls are frequent failure points because semantic alternatives are omitted.

Assess efficiency as well as binary reachability. A switch user forced through 500 stops technically can operate the UI but may not have practical parity. Report excessive traversal as a usability/accessibility defect with evidence.

## Evidence
Use actual devices/emulators and assistive technologies appropriate to the claim; record input method, platform, workflow, action counts, focus path, target geometry, alternative path, failures, and recovery. Automated DOM checks alone cannot prove remote, switch, voice, or gaze operation.

## Output Contract
Return a `finding-set` with `may_modify:false`, `artifact_revision`, `modality_matrix`, `findings[] {finding_id, severity, modality, task_action, evidence, user_impact, falsifier, recommended_repair, required_reverification}`, `unreachable_actions[]`, `inefficient_paths[]`, and `release_recommendation`.

## Failure Traps
- Tab can reach a canvas but cannot manipulate it.
- D-pad focus jumps unpredictably yet mouse tests pass.
- “Alternative” reorder path cannot reach all positions.
- Essential tooltip available only on hover.
- Modality switching silently changes active tool.
- Reviewer assumes hardware behavior from documentation without testing.
- One modality’s success averaged into an overall score.

A required modality with an unreachable critical action is a hard gate, not a small quality deduction.