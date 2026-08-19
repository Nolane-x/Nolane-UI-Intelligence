---
name: designing-casting-and-external-playback
description: Use when playback moves from the local player to a TV, speaker, receiver, or remote session and device discovery, ownership, capability negotiation, state synchronization, and disconnect recovery must remain coherent.
---

# Designing Casting and External Playback

## Parent Contract
**Required parent:** `designing-media-playback-experiences`.

This faculty owns handoff to a remote playback target. It does not own Bluetooth pairing itself. Casting creates a distributed media session: the local UI may become a controller while decoding happens elsewhere, and not every local track/quality/control capability transfers.

## Decision Boundary
Define discovery, connection, connected-controller, reconnecting, and disconnected states. Show the active target identity prominently enough to explain why local video/audio stopped. Synchronize play/pause/position/track state from receiver acknowledgments rather than assuming commands succeeded. Capability negotiation should determine whether captions, alternate audio, speed, live DVR, queue, or quality controls remain available.

Decide ownership across app restart, network switch, lock screen, and another controller joining the same receiver. Disconnect may stop remote playback or merely relinquish control; label the consequence. If connection fails mid-handoff, preserve local position and offer a predictable fallback instead of starting both local and remote streams.

## Failure Topology
- Local player shows Playing immediately after sending a cast command even though receiver rejected it.
- Users hear audio on a TV but cannot tell which device owns playback.
- Caption preference silently disappears on the receiver.
- Disconnect stops a family TV session when the user expected only to disconnect their phone controller.
- Failed handoff leaves local and remote media playing simultaneously.
- Returning to the app shows stale position because receiver state was not reconciled.

## Falsification and Recovery
Test discovery, connect, command acknowledgment, track changes, app background/restart, receiver controls, network loss, second controller, disconnect variants, and failed handoff. The design fails if local state is speculative rather than receiver-confirmed or if users cannot predict what disconnect will do.

Recover by modeling receiver as authoritative during remote playback, negotiating capabilities, reconciling state on reconnect, separating stop-cast from disconnect-controller semantics, and maintaining one canonical session identity across local/remote modes.

## Output Contract
Return `external-playback-contract` with discovery/connect states, target identity, receiver authority, capability negotiation, command acknowledgment, reconnect/state reconciliation, disconnect semantics, local fallback, and casting verification cases.
