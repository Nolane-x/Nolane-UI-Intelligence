---
name: designing-subtitle-authoring-workflows
description: Own subtitle/caption creation and editing across cues, timing, text, speaker/style metadata, reading speed, overlaps, track/language, import/export, and playback verification.
---
# Designing Subtitle Authoring Workflows

## Decision ownership

Own authored timed text in a media sequence. Decide cue identity, in/out timing, text editing, line breaks, speaker/position/style where supported, language/track, reading-speed/length checks, overlap rules, import/export, and linkage to transcript/source. Playback subtitle selection is separate; this owner changes caption content.

## Inputs and evidence

Require sequence timebase, subtitle format capabilities, language, text, cue timings, speaker info, style/position constraints, reading-speed rules if used, accessibility/legal standards, transcript sources, and target delivery formats. Identify generated speech-to-text cues and their confidence/provenance.

## Procedure

Represent each cue in both timeline and text/list editor with synchronized selection. Editing time or text updates one stable cue identity. Provide timecode and duration, plus reading-speed or line-length warnings as guidance/requirements according to domain. Overlaps should be explicit and validated against format constraints. Generated transcript captions need confidence/review state distinct from approved authored cues. Track language and hearing-impaired metadata remain visible. Import preserves source metadata; export previews unsupported styling/features and validates target format.

## Failure topology

Failures include text list and timeline cues desynchronized, cues too short to read with no warning, generated captions presented as reviewed, language metadata missing, overlapping cues silently dropped on export, line breaks changing unexpectedly, and edit timing slipping audio alignment. Another failure is authoring styles that playback/delivery format cannot represent.

## Falsification

Reject if cue identity differs between text/timeline; if generated/unreviewed state is hidden; if target export will discard material fields without warning; if language/track is unknown; if timing cannot be edited at sequence precision; if overlaps violate format silently; or if playback preview cannot verify the authored cue at its time.

## Output contract

Return a `subtitle-authoring-workflows-contract` with: track/language; cue identity; text/timing; speaker/style/position; reading-speed/line checks; generated-review state; overlap policy; timeline/text sync; import provenance; export compatibility; and playback verification. Include one generated-unreviewed and one unsupported-export case.

## Handoffs

Subtitle track selection handles playback, synchronized transcript playback can provide transcript context, timeline supplies timing, and content localization may create language variants.