---
name: designing-accessible-media-alternatives
description: Use when video, audio, live media, recorded media, presentations, streams, or time-based content require captions, subtitles, transcripts, audio description, spoken on-screen text, or equivalent selectable information channels.
---

# Designing Accessible Media Alternatives

## Overview
Accessible media is not a checkbox that says “captions available.” Time-based information may exist simultaneously in speech, music, sound effects, on-screen text, action, diagrams, speaker identity, and spatial context. A useful alternative channel must preserve the information needed to understand and act, remain synchronized enough for the task, and be selectable and perceivable under the user’s real environment. Different alternatives serve different needs; one transcript does not replace every time-synchronized access mode.

## Parent Contract
**Required parent:** `designing-accessible-interfaces`.

Consume media type, live versus recorded status, languages, information carried only in audio or only visually, interaction around the media, latency tolerance, target surfaces, user preferences, and any legal or platform obligations. If the product cannot identify what information is unavailable through each sensory channel, perform an information inventory before choosing an alternative.

## Decision Model
### 1. Inventory meaningful information by channel
Separate dialogue, speaker identity, non-speech audio, music cues, warnings, visual action, gestures, diagrams, on-screen labels, and text overlays. Mark which items are essential to comprehension, navigation, safety, humor, instruction, or task completion.

### 2. Choose alternatives by information need
Captions/subtitles provide time-aligned visual alternatives to audio. Transcripts support search, review, copying, and asynchronous reading. Audio description can convey meaningful visual information. Spoken presentation of on-screen text may help users who cannot read it visually. Sign-language presentation is a separate natural-language channel and routes to its specialist skill. Do not claim one mode is a universal substitute.

### 3. Design synchronization and live degradation
For live media, specify acceptable delay, correction behavior, partial text, speaker attribution, and what happens when service quality falls below the threshold. Avoid captions that lag so far behind that a user cannot associate them with the current speaker or event. Recorded media should support seeking while preserving alternative-channel alignment.

### 4. Make alternatives controllable
Users need clear controls to turn alternatives on, select language, adjust supported presentation properties, and understand whether a track is human-authored, automatic, translated, or generated. The control itself must be keyboard, screen-reader, remote, and touch accessible according to the surface.

### 5. Preserve readability without covering content
Caption placement, line length, contrast, background treatment, scaling, safe areas, and collision with other overlays require responsive behavior. User customization should outrank decorative composition when the alternative channel is essential. When moving captions is necessary, preserve reading order and stable association.

### 6. Treat generated accessibility output as fallible
Automatic captioning, translation, or audio description requires provenance, correction, and quality monitoring appropriate to consequence. Safety instructions, names, numbers, medical content, and financial content may require stronger evidence or human review. Never label generated output as verified merely because it is fluent.

## Evidence
ISO/IEC 20071-23:2018 provides current guidance for visual presentation of audio information including captions and subtitles. ISO/IEC TS 20071-25:2017 provides current guidance for audio presentation of captions, subtitles, and other on-screen text. Use authoritative platform accessibility guidance for concrete controls and rendering behavior, and validate live/recorded alternatives with representative users. Track standard review status because older published standards may be under systematic review without being withdrawn.

## Output Contract
Produce an `accessible-media-contract` containing: sensory information inventory; required alternative channels; language tracks; caption/subtitle rules; transcript behavior; audio-description or spoken-text behavior; live latency/correction policy; speaker attribution; generated-versus-authored provenance; media-control accessibility; responsive placement; customization; seek/synchronization semantics; failure/degraded-state communication; high-risk content review rules; and independent accessibility verification scenarios.

## Failure Traps
- Treating a transcript as an adequate substitute for synchronized captions in every task.
- Omitting meaningful non-speech sounds or speaker changes from captions.
- Overlaying captions on critical visual content with no adaptive placement.
- Making the caption button inaccessible before captions are enabled.
- Hiding whether captions or translations are automatic and potentially wrong.
- Allowing live caption lag to destroy speaker/event association without warning.
- Assuming subtitles for language translation satisfy accessibility captions automatically.
- Providing audio description that talks over essential dialogue with no mixing strategy.
- Removing user presentation preferences to preserve a branded video layout.

The media experience succeeds when users can obtain equivalent task-relevant information through channels they can perceive, with truthful quality and synchronization rather than nominal feature presence.
