---
name: designing-stakeholder-incident-communications
description: Own incident communication planning across internal leaders, support, customers, partners, and regulated audiences with audience scope, cadence, approval, facts, uncertainty, and next-update commitments.
---
# Designing Stakeholder Incident Communications

## Decision ownership

Own communication as a parallel incident workstream. Decide audience groups, communication owner, factual content, uncertainty language, cadence, approval, distribution status, and next-update commitment. This owner is broader than a public status page and ensures different audiences receive appropriate context without diverging facts.

## Inputs and evidence

Require audience map, severity communication policy, confirmed impact, unresolved uncertainty, legal/privacy constraints, approved channels, communication owner, templates, and expected cadence. Identify facts that are safe for internal but not external distribution.

## Procedure

Maintain one communication plan listing audiences, owner, last update, next due, channel, and status. Draft from canonical incident facts while explicitly separating confirmed impact from investigation hypotheses. Preview audience scope and sensitive fields before send. Time-box next-update promises and surface overdue communications during response. Corrections must link to prior messages rather than pretending the previous statement never occurred. Support/customer teams may need actionable workaround language, while executives may need impact/decision summaries; consistency of facts matters more than identical wording.

## Failure topology

Failures include different teams sending contradictory scope, missed promised updates, unconfirmed root cause communicated as fact, sensitive internal details copied externally, corrections with no reference to the original claim, and communication status living only in a responder's memory. Another failure is repeated "investigating" messages that add no useful information or next commitment.

## Falsification

Reject if two audience drafts disagree on confirmed impact; if an external message can include unreviewed sensitive fields without warning; if a promised next update can become overdue with no operational cue; if a correction erases prior wording; if root-cause hypotheses are indistinguishable from facts; or if no owner is accountable for a required audience.

## Output contract

Return a `stakeholder-incident-communications-contract` with: audience matrix; communication owner; fact/uncertainty sourcing; sensitive-data rules; cadence/next-update deadline; draft/approval/send states; correction protocol; channel tracking; and cross-audience consistency checks. Include one overdue-update and one corrected-impact scenario.

## Handoffs

Status-page authoring owns public service-status publishing, incident timeline records sent communications, severity policy supplies cadence obligations, and war-room collaboration can promote draft facts but cannot replace communication governance.