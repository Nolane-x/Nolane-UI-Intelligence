---
name: designing-second-screen-control-continuity
description: Use when control of a shared experience can move between a primary display and one or more second screens and the interface must preserve command state, selection, queue position, ownership, latency feedback, and current context while users switch where they control it.
---

# Designing Second-Screen Control Continuity

## Control continuity is not state mirroring
A second screen can control media, presentations, meetings, games, appliances, vehicles, or collaborative sessions while the primary display remains the shared output. The difficult problem is not showing the same data twice; it is preserving a coherent control context as input moves between surfaces with different latency, capability, and ownership.

## Parent Contract
**Required parent:** `routing-ui-work`.

The routing parent activates this specialist for coordinated control across surfaces. Companion authority determines which surface may act; this skill owns continuity once authority exists.

## Control context
Track active target/session, selected object, playback/task position, navigation context, pending commands, last authoritative acknowledgement, controlling principal, and surface-local UI state. The decision owner is which parts of that context follow the user across surfaces and which remain local presentation preferences.

For example, a phone may preserve the currently selected TV episode and playback queue while using a completely different navigation layout. A presenter remote may keep current slide/notes context while the room display never exposes those private notes.

## Command sequencing and latency
Commands from different surfaces can arrive with variable latency. Use stable command IDs and authoritative sequence/state rather than assuming local order equals accepted order. If the user pauses on one device and immediately seeks on another, the receiving UI must reconcile against current playback state rather than replay stale local assumptions.

Optimistic feedback can improve responsiveness, but distinguish pending from confirmed state when latency or failure matters. Avoid each second screen running its own independent queue of commands that later collides with the primary.

## Surface switching
When the user picks up another controller/surface, establish control context quickly without forcing a full task restart. If simultaneous control is allowed, expose ownership or shared-control policy. If only one controller may be active, transition ownership explicitly and decide what happens to pending commands from the prior surface.

## Evidence
Evidence includes session identity, control-context snapshots, command IDs/order, authoritative acknowledgements, surface-switch events, latency scenarios, and simultaneous-control tests. Test switching while a command is pending, reconnecting after stale local state, and two surfaces issuing contradictory commands.

## Failure modes
Characteristic Failure includes second screens showing different current selections, commands applied in stale order, a new controller replaying old queued actions, private control context leaking to the shared display, and ownership switching with no indication. Another failure is visually synced state that nevertheless uses different command revision underneath.

## Falsification
Add network delay and reordering, switch controlling surfaces during a pending action, disconnect/reconnect a second screen, and issue conflicting commands from two authorized surfaces. The contract fails if accepted state depends on packet arrival rather than authority/order rules, if stale queued input executes after takeover, or if users cannot tell which surface currently controls the shared target.

## Recovery
Query authoritative session state, discard or reconcile stale unacknowledged commands by ID, restore only current control context, and re-establish ownership before accepting new side effects. Preserve surface-local preferences separately so recovery does not require cloning one UI onto another.

## Output and Handoff
Output: `second-screen-control-continuity-contract`, containing control context, command sequencing, pending/confirmed feedback, switching rules, simultaneous-control policy, privacy boundaries, and evidence. Handoff authority decisions to companion-surface authority and write conflicts to cross-device state conflict resolution.

## Sibling Boundary and delete-the-skill
Sibling cross-device session handoff moves an entire active task/session; this skill keeps control of one shared target coherent while presentation may remain distributed. The delete-the-skill test passes because simple synchronization cannot protect against stale commands, latency reorder, and control-context loss during rapid surface switching.