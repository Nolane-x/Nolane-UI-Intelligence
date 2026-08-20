---
name: designing-caption-presentation
description: Use when synchronized captions exist and their placement, readability, speaker/sound information, user preferences, and collision behavior must make spoken and meaningful audio content usable without hearing.
---

# Designing Caption Presentation

## Parent Contract
**Required parent:** `designing-accessible-interfaces`.

This faculty owns the presentation layer of captions once caption content and timing exist. It does not choose subtitle tracks or media transport. It decides how caption text remains readable, distinguishable from the video, attributable to speakers where needed, and movable or styleable enough to avoid covering essential visual information.

## Decision Boundary
Treat captions as timed content, not decorative overlay copy. Define line length, maximum simultaneous lines, background treatment, safe areas, speaker identification, non-speech audio notation, and how captions respond to viewport changes. Preserve author timing while allowing user presentation preferences where the platform supports them. Distinguish same-language accessibility captions from translated subtitles; they may share rendering infrastructure but carry different semantic obligations.

Caption position should avoid critical controls, faces, demonstrations, or burned-in text. When the player exposes controls, captions should adapt to the reduced video area instead of being covered. Fullscreen, picture-in-picture, casting, and embedded players may each have different platform capabilities; specify graceful degradation rather than silently dropping captions.

## Failure Topology
- Captions are rendered beneath player controls and become unreadable whenever controls appear.
- White text is placed directly on bright video with no contrast treatment.
- Speaker changes are unclear in multi-person content where identity affects meaning.
- Meaningful sounds such as alarms or music cues are omitted from accessibility captions.
- Mobile layout shrinks caption text until it is technically present but practically unreadable.
- Picture-in-picture or casting loses captions despite the track remaining selected.

## Falsification and Recovery
Review representative quiet/dialogue/music scenes, multiple speakers, bright/dark footage, portrait/landscape, fullscreen, PiP, controls visible, and user caption-style overrides. The design fails if captions routinely obscure essential visual information, disappear in a playback mode, or require hearing to resolve speaker or sound context.

Recover by defining adaptive safe zones, contrast-preserving backgrounds, speaker/sound conventions, platform fallback behavior, and persistence of caption preferences across playback modes. Verify content quality separately; presentation cannot repair missing or incorrect caption text.

## Output Contract
Return `caption-presentation-contract` with typography/line limits, contrast treatment, safe-area and collision rules, speaker/sound notation, user preference behavior, responsive/fullscreen/PiP/casting deltas, and rendered caption verification scenes.
