---
name: designing-call-participant-layouts
description: Use when realtime calls must arrange participants, active speaker, pinned people, shared content, self-view, large meetings, hidden video, and join/leave changes without losing identity or control context.
---

# Designing Call Participant Layouts

Call layout is attention allocation over a changing participant set. It must remain understandable as people join, leave, speak, share, disable video, get pinned, or move between presentation and discussion modes.

## Parent Contract
**Required parent:** `designing-realtime-communication-systems`.

The parent owns live communication state. This skill owns visual participant arrangement and layout transitions; device readiness and screen-sharing control are separate owners.

## Participant Identity
Every tile or audio-only representation needs stable participant identity and relevant state: display name, speaking indication, mute state where allowed, video availability, hand raised, role, connection quality if surfaced, and local/self distinction. Never let tile reuse during virtualization momentarily show the wrong name over another participant's video.

## Layout Modes
Define rules for grid, active-speaker, pinned, spotlight/presentation, shared-content, and large-meeting overflow. Automatic active speaker should not override an explicit user pin. Host spotlight and local pin are different authority; show which mechanism is controlling the layout.

Screen share competes with participant video for space. Preserve enough participant awareness during presentation for conversation cues without reducing shared content below useful size. Self-view should be movable/hideable when appropriate and should not obscure critical controls or captions.

## Dynamic Change
Join/leave events should not cause violent reflow that makes users lose the speaker they were tracking. Use stable ordering strategies and deliberate transitions. When many participants have video off, avoid wasting equal visual area on empty tiles if an alternative list/strip communicates presence better.

## Accessibility and Captions
Captions and sign-language interpreters can change layout priority. Ensure caption regions do not cover names or controls, and support pin/spotlight of interpreter feeds according to product needs. Keyboard/screen-reader users need a predictable participant list even if visual tiles reorder by speaker activity.

## Evidence
Test 2, 6, 25, and large participant counts, rapid joins/leaves, active speaker changes, local pin, host spotlight, screen share, captions, interpreter, poor network causing video removal, and participant reconnect with same identity. Verify tile identity under virtualization.

## Failure Modes
- Active-speaker automation steals a user-pinned view.
- Virtualized tile briefly shows wrong participant name/video.
- Join/leave causes constant spatial reshuffling.
- Screen share hides all awareness of who is speaking.
- Audio-only users vanish from participant awareness.
- Captions cover participant controls or shared content.
- Keyboard order changes unpredictably with visual active-speaker sorting.

## Falsification
Pin one participant, enable host spotlight on another, start screen share, and cause multiple joins/leaves. Falsify if the layout cannot explain which priority wins or if identity continuity breaks during reflow.

## Recovery
Restore stable participant keys, separate local pin from host spotlight, freeze explicit user priorities, and downgrade automatic layout behavior when state is ambiguous. Provide an accessible participant list independent of volatile visual sorting.

## Handoff
Pre-join hardware uses `designing-call-join-device-checks`; screen source/ownership uses `designing-screen-share-control`; membership/roles use `designing-room-channel-membership`.

## Output Contract
Return a `call-participant-layouts-contract` with `participant_identity_fields`, `layout_modes[]`, `priority_rules`, `screen_share_composition`, `dynamic_reflow_policy`, `self_view_rules`, `caption_interpreter_accommodations`, `identity_evidence[]`, `falsification_cases[]`, and `recovery_actions[]`.