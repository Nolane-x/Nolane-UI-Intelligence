---
name: designing-status-page-authoring
description: Own public or customer-facing service-status incident updates, affected component scope, lifecycle, scheduled maintenance, message history, and preview before publication.
---
# Designing Status Page Authoring

## Decision ownership

Own the authoring interface for status incidents visible outside the responder workspace. Decide affected components, public lifecycle state, impact wording, update history, publish preview, scheduling, subscriber notifications, and relation to internal incidents. It does not decide the incident's internal severity or root-cause analysis.

## Inputs and evidence

Require component catalog, public status states, audience, internal-to-public mapping, notification/subscriber behavior, communication approval policy, maintenance support, historical retention, and privacy/legal constraints. Determine whether one internal incident maps to several public component incidents.

## Procedure

Require explicit affected public components and impact status rather than copying internal service names blindly. Draft updates from confirmed facts with a preview matching the external page. Publishing should record author, time, message, affected components, and subscriber notification decision. State transitions—investigating, identified, monitoring, resolved or local equivalents—must have defined meaning and not auto-follow internal severity. Corrections append a new update. Scheduled maintenance should be visually distinct from unplanned incidents while sharing component and notification mechanics.

## Failure topology

Failures include internal identifiers leaked publicly, wrong components marked down, public status automatically resolved when internal incident closes, edits rewriting historical updates, subscriber notifications sent unintentionally, and preview differing from actual page formatting. Another failure is a status page that says all systems operational while an active public incident exists because component mapping drifted.

## Falsification

Reject if public component scope cannot be previewed; if historical messages can be silently edited; if subscriber notification is an implicit side effect; if internal root-cause hypotheses can be published without confirmation; if public resolution is coupled invisibly to internal state; or if an active public incident is inconsistent with the page's overall status without a warning.

## Output contract

Return a `status-page-authoring-contract` with: public component mapping; lifecycle states; draft/preview/publish flow; fact source; subscriber notification control; update history; correction behavior; scheduled-maintenance distinction; internal-incident linkage; and resolution independence. Include one component-mapping mismatch example.

## Handoffs

Stakeholder communication owns audience strategy, maintenance-window operations supplies planned-event context, incident timeline records publications, and service health provides evidence without dictating public wording.