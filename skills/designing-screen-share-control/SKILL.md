---
name: designing-screen-share-control
description: Use when users present a screen, window, tab, application, or other live source in a realtime session and need explicit source choice, privacy preview, sharing state, handoff, pause/stop, and failure recovery.
---

# Designing Screen Share Control

Screen sharing crosses a privacy boundary: private local pixels become shared media. The interface must make source selection, active source, audience, and stop state continuously obvious without relying on a tiny browser indicator users may not notice.

## Parent Contract
**Required parent:** `designing-realtime-communication-systems`.

The parent owns the live session. This skill owns share-source selection and publication control; participant layout determines how the shared content is composed in the call.

## Source Selection
Represent the source types the platform can actually distinguish—entire display, application window, browser tab, or application-specific surface. Explain privacy implications near choice. A full-display share may expose notifications and unrelated apps; tab/window share is narrower but can still contain sensitive content.

Show a recognizable preview or source identity before publication when platform APIs permit it. Never render a fake preview from an old screenshot if live capture has not started. If system picker selection occurs outside the app, reconcile the returned source and show what is actually being shared.

## Active Share State
Once sharing, keep persistent local indication of source and audience. Controls for pause (if supported), switch source, stop, include system audio, and share cursor/annotations should reflect actual media state. A button labelled “Stop sharing” must stop publication even if focus has moved to another app.

If multiple simultaneous sharers are supported, clarify who owns which share and how participants choose among them. If not supported, starting a new share should disclose that it replaces the existing one.

## Privacy and Failure
Handle source closing, display disconnect, capture permission revocation, protected-content black screen, network degradation, and app suspension. Do not continue claiming an active share when the outgoing track is ended. For accidentally shared sensitive content, stopping cannot guarantee viewers did not see or record prior frames; avoid false recall language.

## Evidence
Test full display, window, tab, system audio on/off, switch source, source close, screen disconnect, browser permission denial, multiple displays, presentation while notifications occur, and stop from outside the call window. Verify outgoing track/source identity.

## Failure Modes
- UI says “sharing” but the media track ended.
- Source switch publishes before user confirms the new source.
- Full-display privacy risk is hidden.
- Stop control only works when the call window is focused.
- Starting a second share silently replaces the first.
- A frozen last frame remains visible and looks live after source failure.

## Falsification
Share a window, close it, then switch to a full display while the call window is unfocused. Falsify if active-source indicators disagree with published media or if users cannot reliably stop sharing from the persistent control path.

## Recovery
Reconcile against actual media track state, clear frozen frames, surface ended/failed share, require deliberate source replacement, and keep a global stop path. If source identity cannot be established, pause publication rather than guessing.

## Handoff
Call layout uses `designing-call-participant-layouts`; device readiness uses `designing-call-join-device-checks`; moderation authority over who may share routes through membership/moderation owners.

## Output Contract
Return a `screen-share-control-contract` with `source_types[]`, `selection_preview`, `active_source_indicator`, `audience_state`, `switch_stop_rules`, `multi_sharer_policy`, `privacy_warnings`, `failure_states[]`, `published_track_evidence[]`, `falsification_cases[]`, and `recovery_actions[]`.