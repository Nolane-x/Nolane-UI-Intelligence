---
name: designing-waveform-navigation
description: Use when an audio waveform is an interactive temporal map and users need to seek, inspect, zoom, select, or orient through sound without the waveform becoming an inaccessible decorative canvas.
---

# Designing Waveform Navigation

## Parent Contract
**Required parent:** `designing-media-playback-experiences`.

This faculty owns waveform-as-navigation. A waveform may visually encode amplitude across time, but it must have explicit temporal semantics and alternative controls. It does not own audio editing envelopes or clip-range selection itself.

## Decision Boundary
Decide whether the waveform is decorative, a seek surface, a zoomable timeline, or a detailed analysis surface. If interactive, map x-position to canonical media time and maintain the playhead separately from hover/preview. Long recordings may require zoom and horizontal navigation; define how scale changes preserve the current anchor and how overview context remains available.

Amplitude should not be implied to represent loudness or semantic events unless the data actually supports that claim. Provide timestamps, chapters, markers, or transcript connections for users who cannot perceive waveform shape. Keyboard interaction needs temporal increments and marker navigation; screen readers should receive the same seek/marker functions without hearing thousands of amplitude samples.

## Failure Topology
- Waveform looks seekable but clicks do nothing.
- Canvas consumes pointer events but has no keyboard or nonvisual alternative.
- Zoom jumps to the start instead of preserving the user's current time anchor.
- Hover position is mistaken for actual playhead and labels show contradictory times.
- Downsampled amplitude is described as exact acoustic analysis.
- A six-hour waveform renders millions of points and blocks the main thread.

## Falsification and Recovery
Test decorative versus interactive affordance, seek, hover preview, keyboard movement, zoom/pan, markers, long-file performance, screen-reader alternative, and resize. The design fails if visual waveform interaction exposes a materially faster navigation path with no equivalent or if temporal mapping shifts under zoom.

Recover by explicitly classifying the waveform, binding all interaction to canonical time, adding structured marker/time controls, virtualizing/downsampling visual data responsibly, and maintaining zoom anchor. Keep exact acoustic claims out unless supported by the signal pipeline.

## Output Contract
Return `waveform-navigation-contract` with waveform role, time mapping, playhead/preview states, seek input modes, zoom/pan anchor, marker/alternative navigation, performance strategy, and temporal mapping verification cases.
