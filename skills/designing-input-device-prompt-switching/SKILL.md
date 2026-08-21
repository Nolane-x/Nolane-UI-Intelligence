---
name: designing-input-device-prompt-switching
description: Use when keyboard, mouse, touch, gamepad, remote, or other input devices can alternate during one session and the interface must switch button glyphs, hints, control legends, and affordances without flicker, stale prompts, or misleading capability assumptions.
---

# Designing Input-Device Prompt Switching

## Prompt identity is runtime state
A control hint such as “Press A,” “Press Enter,” or “Tap” is only correct relative to the active input context. Hybrid devices, shared PCs, consoles with keyboards, and accessibility peripherals can change that context moment to moment. This skill owns how the product infers the active prompt family and when visible legends should update.

## Parent Contract
**Required parent:** `routing-ui-work`.

The routing parent activates this specialist when more than one input family can control the same surface. Default command semantics and remapping are neighboring skills; this owner handles dynamic prompt presentation.

## Active-device inference
Track recent meaningful input by device identity and input family. Ignore noisy signals that should not steal prompt ownership: pointer movement caused by controller emulation, tiny stick drift, passive touchpad events, or synthetic accessibility events that do not imply the user switched control mode. The decision owner is the hysteresis policy that decides when evidence is strong enough to change prompts.

A prompt family may depend on controller type, platform convention, locale, and user mapping. Do not infer branded glyphs from generic gamepad capability unless device identity is trustworthy. When identity is unknown, prefer neutral labels or action names over a possibly wrong glyph.

## Switching behavior
Prompt changes should be fast enough to feel responsive but stable enough to avoid flicker when devices generate interleaved events. Keep focus and task state unchanged while prompts switch. A pointer becoming active may reveal hover affordances; a gamepad becoming active may emphasize directional focus, but the product must not destroy the user’s current context merely to restyle hints.

For co-play or multiple assigned controllers, prompt ownership can be scoped by player rather than global last-input. A settings pane for player two should not switch to player one’s controller glyphs because player one moved a stick elsewhere.

## Evidence
Evidence includes raw device events, filtering/hysteresis decisions, resolved input family, mapped action labels, glyph set, and rendered prompt changes. Test rapid alternation, stick drift, mouse jitter, unknown controllers, remapped controls, and simultaneous players. Capture at least one trace proving that irrelevant background input does not steal visible prompt ownership.

## Failure modes
Characteristic Failure includes glyph flicker between keyboard and gamepad, stale prompts after a device switch, showing Xbox-style labels for an unknown layout, touch users seeing hover-only instructions, remapped controls still displaying defaults, and one player’s input changing another player’s legends. Another failure is prompt disappearance during ambiguity instead of a neutral fallback.

## Falsification
Inject noisy interleaved events, swap controller type, enable a custom mapping, switch from touch to keyboard without pointer movement, and connect two players. The contract fails if prompts change on noise, lag after meaningful input, display an unverified device glyph, or diverge from the actual action mapping.

## Recovery
When device identity is uncertain, fall back to semantic action names or neutral glyphs while preserving control. Recompute prompt bindings from the authoritative mapping rather than caching old button labels. If event noise causes oscillation, fix the input inference/hysteresis boundary rather than adding arbitrary visual delays.

## Output and Handoff
Output: `input-device-prompt-switching-contract`, containing device inference, noise filters, hysteresis, player scope, glyph resolution, mapping integration, neutral fallbacks, and evidence. Handoff customizable bindings to controller-remapping surfaces and disconnect state to controller-disconnect recovery.

## Sibling Boundary and delete-the-skill
Sibling controller remapping owns what action a button performs; this skill reflects that mapping in prompts as the active device changes. Remote navigation owns command meaning. The delete-the-skill test passes because without a prompt-switching owner, hybrid-input interfaces routinely display stale or incorrect instructions even while actual controls continue working.