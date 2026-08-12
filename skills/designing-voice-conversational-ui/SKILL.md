---
name: designing-voice-conversational-ui
description: Use when users issue spoken commands, dictate content, converse with an assistant, control a hands-busy interface, or need voice as a primary or alternative input channel.
---

# Designing Voice and Conversational UI

## Overview
Voice is probabilistic input with transient output and social/privacy constraints. Design for ambiguity, repair, interruption, and multimodal continuity rather than pretending speech is a keyboard with no screen.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require task consequence, environment/noise, privacy context, supported languages, whether a screen is present, and how other input modalities coexist. Route consequential actions to `designing-high-stakes-decisions`.

## Decision Model
Model a turn as capture → interpretation → grounding → action or clarification → feedback. Decide which commands can execute immediately and which require disambiguation or confirmation. Confirmation should be semantic and risk-proportional: “Play jazz” can execute and be corrected; “Send it” when two drafts or recipients are plausible needs clarification before an irreversible action.

Make system state speakable. The user needs to know whether the interface is listening, processing, waiting for clarification, executing, or done. Provide interruption/barge-in policy and a reliable cancel phrase or physical control. If speech recognition fails, preserve what was understood and invite correction rather than restarting the entire task.

Avoid long audio menus. Offer a few meaningful choices, allow open language where the model supports it, and use a screen to externalize options when available. In multimodal interfaces, spoken and visible state must refer to the same objects with stable names. Privacy matters: do not unexpectedly read sensitive content aloud in shared environments; allow text/keyboard alternative.

Localization includes pronunciation, grammar, names, accents, code-switching, and domain vocabulary — not text translation alone.

## Evidence
Test realistic noise, accents/languages in scope, ambiguous referents, delayed network/model response, interruption, correction, screen-off/hands-busy contexts, privacy-sensitive content, and fallback input. Record recognition uncertainty separately from task design errors.

## Output Contract
Return a `voice-contract` with `intents[]`, `entities_and_referents`, `turn_states`, `clarification_policy`, `confirmation_policy`, `barge_in_and_cancel`, `repair_paths[]`, `multimodal_sync`, `privacy_rules[]`, `localization_needs[]`, and `voice_tests[]`.

## Failure Traps
- Executing ambiguous pronouns or deictic phrases with high consequence.
- Confirmation after every low-risk command until voice becomes unusably slow.
- No visible/listening state, so users repeat commands.
- Voice-only error recovery that requires remembering a long menu.
- Reading private content aloud by default.
- Treating one English recognition test as multilingual validation.
- Screen and voice using different names for the same object.

Conversation succeeds when misunderstanding is cheap to repair and consequential ambiguity is caught before action.