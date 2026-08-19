---
name: designing-subtitle-track-selection
description: Use when media offers multiple subtitle or caption tracks and users need to distinguish language, accessibility type, forced narrative subtitles, generated tracks, and off state.
---

# Designing Subtitle Track Selection

## Parent Contract
**Required parent:** `designing-media-playback-experiences`.

This faculty owns track discovery and selection metadata for textual timed tracks. It does not own how captions are visually rendered. It decides how users distinguish ordinary translation subtitles, same-language accessibility captions, forced narrative text, auto-generated tracks, and unavailable states.

## Decision Boundary
Build the menu from semantic track metadata, not filenames. Show human-readable language names, regional/script distinctions when meaningful, and track characteristics such as CC/SDH or generated quality. “Off” may be a valid state for ordinary subtitles but should not silently suppress forced subtitles required to understand foreign dialogue or signed text; define product rules for those cases.

Persist preference by compatibility rather than raw track ID. If users choose Spanish subtitles, the next episode should select the best compatible Spanish track where available. When no match exists, reveal fallback rather than pretending preference was honored. Track changes should preserve playback position and provide immediate confirmation without stealing focus.

## Failure Topology
- Two tracks both appear as “English” although one includes accessibility sound cues and the other does not.
- The selected database track ID is reused on another episode and points to a different language.
- Auto-generated captions are labeled the same as professionally authored tracks.
- Switching subtitles seeks the media back to zero.
- “Off” removes forced narrative subtitles and makes plot content incomprehensible.
- Casting retains the menu selection visually but receiver chooses its own default track.

## Falsification and Recovery
Test multilingual tracks, regional variants, CC/SDH, generated tracks, forced subtitles, episode transitions, unavailable preferences, casting, offline media, and screen-reader menu navigation. The design fails if users cannot explain which textual track is active or if compatibility fallback occurs silently.

Recover by normalizing semantic track metadata, matching preferences by language/type, marking generated/accessible variants, defining forced-subtitle rules, and synchronizing receiver/offline capabilities. Keep visual presentation preferences separate from track identity.

## Output Contract
Return `subtitle-track-contract` with track taxonomy/labels, language/script metadata, off/forced rules, preference matching, generated-track disclosure, selection feedback, mode-transfer behavior, and subtitle-selection verification cases.
