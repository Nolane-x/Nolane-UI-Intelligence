---
name: designing-live-region-announcement-strategy
description: Use when asynchronous changes need to be announced nonvisually without turning every state update into interruptive screen-reader chatter.
---

# Designing Live Region Announcement Strategy

## Parent Contract
**Required parent:** `designing-screen-reader-experiences`.

This faculty owns the announcement policy for asynchronous interface events. It decides which changes warrant spoken notification, their urgency, wording, aggregation, and suppression rules. It does not own visible toast design or generic loading state; the concern is the nonvisual temporal channel and the cost of interrupting a user's current reading or input.

## Decision Boundary
Inventory events by consequence rather than implementation event frequency. A completed destructive action, form submission result, connection loss, or new search-result count may deserve an announcement; every streamed token, progress tick, validation keystroke, or background refresh usually does not. Choose polite versus assertive delivery based on whether delaying the information could cause an incorrect action. Assertive announcements are exceptional because they can cut off current speech.

Define deduplication and coalescing. Rapid updates such as “12 results…14 results…18 results” should often resolve to one stable message after the relevant interaction settles. Announcements need enough context to stand alone without forcing the user to search visually, but must not repeat labels already spoken by focus movement. When the same operation has visible feedback, the spoken message should describe the state outcome rather than read decorative copy verbatim.

## Failure Topology
- A live region announces every incremental render and makes the interface effectively unusable with speech.
- Success and error messages are inserted before the live region exists, so no announcement occurs.
- Assertive messaging interrupts a user entering sensitive or high-stakes information for low-priority updates.
- Duplicate visual toast and live-region text cause the same result to be spoken twice.
- Status text lacks the affected object or action, producing messages such as “Saved” with no usable context.
- Background polling announces changes the user did not request and cannot act on.

## Falsification and Recovery
Test with actual screen-reader speech across fast updates, slow network responses, repeated retries, route changes, background polling, and focus movement that occurs near the same time as the event. Capture the spoken sequence, not merely the DOM attributes. The contract fails when a material outcome is silent, a low-value event interrupts work, or message ordering makes cause and result ambiguous.

Recover by reducing the event set, delaying/coalescing noisy sources, lowering urgency, separating status from alert semantics, and ensuring stable live-region hosts exist before updates. Verify that keyboard and pointer users receive equivalent state truth without requiring the spoken channel.

## Output Contract
Return `live-region-announcement-contract` with event taxonomy, announcement eligibility, urgency level, message composition, coalescing windows, deduplication rules, suppression cases, live-region lifecycle, and recorded speech verification scenarios.
