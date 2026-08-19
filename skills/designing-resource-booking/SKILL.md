---
name: designing-resource-booking
description: Use when users reserve rooms, equipment, staff, capacity or other constrained resources and the interface must combine availability, eligibility, capacity, hold/confirmation and resource-specific constraints.
---

# Designing Resource Booking

## Parent Contract
**Required parent:** `designing-task-flows`.

This faculty owns booking a constrained resource. Slot selection and scheduling conflicts are specialist siblings; inventory/asset administration is outside this boundary.

## Decision Model
Define the resource model: identity, location/timezone, capacity, availability calendar, eligibility/permission, attributes, lead/setup/cleanup time, booking duration rules and whether the resource can support concurrent capacity. A room with capacity 12 is not equivalent to twelve identical seats unless the backend models it that way.

Discovery should let users filter by the attributes that affect the job—capacity, equipment, accessibility features, location, skill, service type—without hiding why a resource is unavailable. When comparing alternatives, show time/resource constraints together rather than forcing users to bounce between a calendar and a separate catalog.

Selection is not confirmation. Availability may be eventually consistent; revalidate or hold before commit. If the system creates temporary holds, show hold scope/expiration. If approval is required after request, distinguish `requested` from `booked/confirmed` and keep the user informed of resource state.

Resource-specific buffer time matters. A studio may need setup/cleanup; a clinician may need appointment types that alter duration; equipment may have maintenance blocks. Render the actual bookable interval and explain additional blocked time where it affects nearby choices.

Changes/cancellations should state consequences such as release timing, fees, participant notifications or linked services when authoritative. Recurrence requires checking each occurrence, not assuming one resource is available forever.

## Failure Topology
- UI says “Booked” immediately although request still awaits facility approval.
- Room appears free 10:00–11:00 but hidden cleanup buffer makes the booking invalid.
- Resource capacity is shown as a descriptive number but not checked against attendee count.
- Accessible-room filter is missing even though that attribute is required for some users.
- A recurring reservation is accepted based only on first occurrence.
- Two users see the same last resource as available and both receive optimistic success.

## Falsification and Recovery
Falsify with capacity/attribute filters, buffers, approval-required resources, concurrency, holds, recurring bookings, cancellation and timezone changes. Reconcile displayed availability/confirmation to the resource scheduler at commit.

Recover by modeling resource constraints explicitly, separating request/hold/confirmation, revalidating atomically, exposing buffers/eligibility and checking recurrence occurrence-by-occurrence.

## Output Contract
Return `resource-booking-contract` with resource attributes/constraints, discovery filters, availability/hold/confirmation states, capacity/buffer semantics, approval path, concurrency, recurrence/cancellation handoffs, accessibility needs and booking-integrity tests.