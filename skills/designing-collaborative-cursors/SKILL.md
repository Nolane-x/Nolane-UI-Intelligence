---
name: designing-collaborative-cursors
description: Use when multiple people manipulate the same visual workspace and remote pointer or caret positions must communicate immediate activity without implying authoritative selection, presence, or control.
---

# Designing Collaborative Cursors

## Parent Contract
**Required parent:** `designing-collaboration-and-presence`.

This faculty owns ephemeral remote pointer/caret projection inside a shared workspace. A collaborative cursor is not general online presence, a persistent annotation, or proof that another user owns an object. It communicates where a collaborator is currently pointing or editing with bounded temporal confidence.

## Decision Model
Define the coordinate space before rendering. Canvas cursors should transmit normalized/world coordinates or object-relative positions, not raw viewport pixels that break under zoom, pan, density, or differently sized windows. Text carets need document-position identity robust to concurrent edits. The local renderer transforms canonical remote position into the current viewport.

Remote motion should be sampled and interpolated without pretending every intermediate point came from the other user. Apply bounded smoothing to reduce network jitter, but stop or fade the cursor when updates become stale. Teleporting a cursor across the document after a large viewport change may be more honest than animating through unrelated content.

Identity labels should be distinguishable and stable during a session, but they must not cover controls or content persistently. Cursor color alone cannot be the only identity channel. When many collaborators are active, reduce visual load through proximity labels, fading, following modes, or selective display rather than showing thirty opaque pointers.

## Failure Topology
- Cursor positions are sent in screen pixels and appear in the wrong location for collaborators at another zoom level.
- Network delay keeps a cursor visible over an object long after the user left.
- Smoothed animation crosses unrelated objects and implies actions that never occurred.
- Remote cursor color is the only identity cue and becomes ambiguous for low-vision/color-deficient users.
- Labels cover resize handles and make the shared editor harder to operate.
- Cursor is treated as object lock/ownership even though no locking protocol exists.

## Falsification and Recovery
Falsify with different viewport sizes, pan/zoom changes, high latency, packet loss, reconnect, thirty collaborators, transformed objects, text edits before a remote caret, reduced motion, screen magnification, and a remote user leaving abruptly. The design fails if cursor location cannot be mapped into a shared canonical space or if stale telemetry is indistinguishable from current activity.

Recover by transmitting canonical positions plus revision/context, interpolating only within bounded freshness, expiring stale cursors, separating cursor identity from lock/selection state, adapting density for many participants, and offering non-color identity cues.

## Output Contract
Return `collaborative-cursor-contract` with canonical coordinate/caret model, sampling frequency, interpolation bounds, staleness expiry, identity labeling, density policy, viewport transformation, concurrency revision handling, reduced-motion behavior, and falsification cases.