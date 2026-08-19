---
name: designing-timezone-aware-scheduling
description: Use when participants, resources or events span timezones and the interface must distinguish wall-clock intent, absolute instants, organizer/event zones, DST shifts and conversion without ambiguous dates or silent zone changes.
---

# Designing Timezone-Aware Scheduling

## Parent Contract
**Required parent:** `designing-task-flows`.

This faculty owns timezone semantics in scheduling interfaces. It does not define generic date pickers or recurrence rules beyond their timezone interaction.

## Decision Boundary
Determine which temporal type the domain owns. A live meeting usually represents an **instant** displayed in many zones. A store opening at 09:00 every day represents **wall-clock time in a location zone**. A flight segment may need both local departure/arrival zones. A floating reminder can intentionally have no fixed zone. Do not force all of them into device-local timestamps.

Show the primary event/organizer/resource timezone near editable times when it can differ from the viewer. Conversion to the viewer’s zone may be helpful, but label both rather than replacing authoritative local meaning. Use IANA-style zone identities from the platform/backend where possible instead of fixed UTC offsets that fail across DST.

Changing timezone is a semantic operation. Decide whether it should preserve the instant and change displayed wall time, or preserve wall-clock time and therefore change the instant. The control must state this consequence before commitment in scheduling editors where users could reasonably expect either behavior.

DST creates nonexistent and repeated local times. If a chosen wall-clock time falls into a spring-forward gap, block or resolve according to domain policy with explanation. During fall-back repetition, distinguish the two possible instants if the domain requires precision.

Participant availability should convert from each source correctly, but avoid displaying a wall of zones. A comparison strip can show organizer/viewer/key participant local times and date boundaries, especially when “Tuesday 23:30” is “Wednesday 08:30” elsewhere.

## Failure Topology
- UI stores UTC+7 instead of `Asia/Ho_Chi_Minh` for a recurring schedule whose offset may differ in other regions.
- Changing event timezone silently preserves wall time when user expected the same instant.
- Viewer sees `9:00 AM` with no zone and assumes local time although it is venue time.
- A nonexistent DST time is normalized to 03:00 without explanation.
- Participants cross a date boundary but date label is shown only once at the top.
- Recurring meeting drifts an hour because recurrence was expanded as fixed UTC intervals instead of local wall-clock rule.

## Falsification and Recovery
Falsify across DST changes, zones with half/quarter-hour offsets, date boundaries, organizer/viewer zone switches, preserve-instant vs preserve-wall-time edits and recurring events. Compare stored temporal representation to authoritative instants/rules.

Recover by naming temporal type and authoritative zone, exposing zone-changing semantics, using zone IDs rather than offsets, validating DST anomalies and presenting converted dates/times redundantly where needed.

## Output Contract
Return `timezone-scheduling-contract` with temporal type, authoritative/display zones, conversion presentation, zone-change semantics, DST gap/repeat policy, participant comparison, recurrence handoff and instant/wall-time parity tests.