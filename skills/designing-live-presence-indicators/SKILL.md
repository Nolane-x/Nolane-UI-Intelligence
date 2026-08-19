---
name: designing-live-presence-indicators
description: Use when a shared product exposes who is currently active in a workspace, document, room, or object and must represent membership, freshness, identity, privacy, and overflow without confusing presence with cursor activity or availability.
---

# Designing Live Presence Indicators

## Parent Contract
**Required parent:** `designing-collaboration-and-presence`.

This faculty owns the answer to “who is here now?” Presence is coarser than a collaborative cursor and broader than a typing indicator. It does not claim that someone is watching a particular object, available to respond, or actively editing unless the underlying protocol supplies that stronger evidence.

## Decision Boundary
Define the presence scope and qualifying heartbeat. Workspace presence, document presence, room presence, and object focus are different claims. A websocket connection alone may prove that a client is connected, not that the human is actively viewing the surface. If idle/away state is exposed, tie it to a declared inactivity model and label it as such rather than inferring intent.

Membership must expire. A client crash, suspended mobile browser, or lost network cannot leave someone “online” forever. Use server leases, heartbeat deadlines, or session expiry so stale users disappear predictably. Reconnection should reconcile one person across multiple tabs/devices instead of multiplying avatars unless device-level presence is intentionally useful.

Identity representation needs a scale strategy. A few collaborators can use avatars/names; dozens need counts, grouped overflow, or a participant panel. Never reveal hidden/private membership beyond the viewer's authorization. Presence controls may offer follow/jump-to-user, but those actions need their own target evidence and must not imply remote control.

## Failure Topology
- Closed laptop leaves a collaborator shown as online for hours because no lease expires.
- One user with three tabs appears as three separate people.
- Document-level avatar is interpreted as “currently reading my changes” even though only workspace connection is known.
- Overflow avatar list leaks members of a private room to a guest.
- Presence order reshuffles continuously on every heartbeat and destroys recognition.
- “Away” state is inferred from no mouse movement despite keyboard or assistive-technology activity.

## Falsification and Recovery
Falsify with multi-tab sessions, mobile sleep, abrupt disconnect, reconnect with a new connection ID, idle keyboard-only use, restricted guest membership, hundreds of participants, screen-reader access to participant state, and server heartbeat delay. The design fails if presence outlives its freshness contract or if visual state claims a narrower scope than the telemetry can prove.

Recover by defining scope-specific sessions, server-authoritative expiry, user-level deduplication, conservative active/idle claims, permission-filtered membership, stable ordering, and scalable overflow representation.

## Output Contract
Return `live-presence-contract` with presence scope, qualifying signal, lease/expiry, multi-device deduplication, idle semantics, identity presentation, overflow policy, authorization boundaries, optional follow/jump affordances, accessibility representation, and falsification cases.