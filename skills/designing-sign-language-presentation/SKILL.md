---
name: designing-sign-language-presentation
description: Use when audiovisual or interactive content presents, overlays, streams, records, translates, interprets, or generates a sign-language access channel for users who prefer or require a natural sign language.
---

# Designing Sign Language Presentation

## Overview
A sign language is a natural language with its own grammar, spatial structure, facial expression, timing, and community conventions. It is not a sequence of pictograms and it is not automatically equivalent to captions. The UI must preserve linguistic intelligibility while integrating a signer or signing avatar with source media, controls, multiple languages, responsive layouts, and other accessibility channels. Presentation quality can change meaning, so framing and timing are semantic decisions rather than visual polish.

## Parent Contract
**Required parent:** `designing-accessible-media-alternatives`.

Consume the accessible-media information inventory, source language, requested sign language, live/recorded status, human interpreter versus recorded signer versus generated avatar, target screens, media controls, latency constraints, and user preferences. If sign-language interpretation quality itself is outside available expertise, record the domain-evidence gap; do not fabricate linguistic rules from spoken-language structure.

## Decision Model
### 1. Identify the language and production model
Name the actual sign language; never use “sign language” as if there were one universal system. Record whether content is live-interpreted, pre-recorded, authored directly in sign, machine-translated, or avatar-generated. Expose provenance when users could reasonably confuse these modes.

### 2. Preserve the full signing space
Frame enough upper body, hands, face, and relevant spatial area for the language and content. Do not crop hands during responsive resize, hide facial grammar under UI chrome, or reduce the signer to a thumbnail that is technically visible but linguistically unreadable. Define minimum useful size from evidence rather than arbitrary percentages.

### 3. Synchronize meaning, not just timestamps
For interpreted content, allow the temporal relationship needed for complete phrases and concepts rather than forcing word-for-word alignment with speech. Keep the signer associated with the correct source segment and speaker context. Live delay must be disclosed when it can affect turn-taking, questions, warnings, or interactive participation.

### 4. Support user-controlled presentation
Provide clear language selection and, where feasible, size/position controls that preserve critical source content. Remember preferences at the appropriate scope. Ensure controls remain usable by keyboard, remote, touch, screen reader, and other relevant modalities even though the media channel itself is visual.

### 5. Preserve identity and attribution
When a human interpreter or signer is shown, distinguish interpreter identity from source speaker identity. When an avatar or synthetic signer is used, route to `designing-avatar-embodied-representation` and disclose automation. Do not imply that a synthetic embodiment is a real interpreter or that smooth animation establishes linguistic correctness.

### 6. Coordinate with captions and other alternatives
Users may want sign language plus captions, source video, transcript, or audio. Layout rules must handle simultaneous channels without mutual occlusion. Do not force a choice between two accessibility modes merely because the design did not reserve space.

### 7. Verify with language users
Linguistic and presentation verification requires fluent sign-language users and qualified expertise appropriate to the context. Test framing, contrast against background, motion clarity, signer/source association, delay, language switching, responsive behavior, and high-motion scenes. Automated visual tests can catch cropping but cannot certify linguistic adequacy.

## Evidence
ISO/IEC DIS 20071-24 is currently under development in 2026 and addresses visual presentation of audio information in sign languages. Its draft status must remain explicit; it is evidence that this is a distinct accessibility UI domain, not a released universal conformance rule. Pair it with current published accessible-media guidance, platform-specific accessibility guidance, and direct research with users of the sign language in scope. For synthetic signing, require avatar provenance and linguistic evaluation separately.

## Output Contract
Produce a `sign-language-presentation-contract` containing: target sign language; human/recorded/generated production model; provenance disclosure; signer/interpreter attribution; framing and minimum readable presentation; responsive safe area; synchronization/delay policy; source-speaker association; language selection; size/position preferences; coexistence with captions/transcripts/source video; generated-avatar delegation when applicable; failure/degraded state; and required fluent-user or qualified linguistic verification.

## Failure Traps
- Treating sign language as a universal language or as AAC pictograms.
- Translating spoken words one by one and calling the result sign-language UI.
- Cropping hands or facial expression to fit a decorative video layout.
- Shrinking the signer until the channel is nominally present but unreadable.
- Hiding whether a signer is human, recorded, interpreted, translated, or synthetic.
- Using a photorealistic signing avatar as evidence that the signing is linguistically correct.
- Forcing users to choose between captions and sign presentation when both are needed.
- Ignoring live delay in an interactive or safety-relevant conversation.
- Certifying linguistic quality with screenshot tests alone.

The presentation succeeds when the sign-language channel remains a readable, attributable, user-controlled language experience rather than a decorative accessibility overlay.
