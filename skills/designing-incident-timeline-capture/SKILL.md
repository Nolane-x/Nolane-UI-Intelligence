---
name: designing-incident-timeline-capture
description: Own chronological evidence capture for incidents, separating observed events, actions, decisions, communications, and inferred hypotheses while preserving time-source uncertainty.
---
# Designing Incident Timeline Capture

## Decision ownership

Own the incident chronology used during response and later reconstruction. Decide event types, source timestamps, manual entries, corrections, ordering when clocks disagree, pinned milestones, filtering, and linkage from timeline entries to evidence/actions. Generic audit logs record system events; this timeline integrates operational meaning across humans and systems.

## Inputs and evidence

Require telemetry/event sources, clock/timezone behavior, manual responder entries, chat/action integrations, event IDs, correction policy, retention, and postmortem needs. Identify sources with ingestion delay or unreliable clocks so ordering is not falsely precise.

## Procedure

Normalize display time while retaining original timestamp/source. Classify entries as observation, action, decision, communication, state change, or hypothesis update. Automated ingestion should be filterable and deduplicated so key human decisions are not buried. Allow responders to pin milestones such as detection, declaration, mitigation start, recovery, and resolution. Corrections should append provenance rather than rewrite history invisibly. For delayed events, show observed-at versus received-at when material. Link actions to results and evidence so the timeline is more than a transcript.

## Failure topology

Failures include chat messages dumped chronologically with no type, telemetry floods obscuring decisions, source clock skew producing misleading order, manual edits rewriting history, and action entries with no result. Another failure is presenting ingestion time as event time, making responders infer causality from an incorrect sequence.

## Falsification

Reject if two events with uncertain ordering are shown as exact causal sequence; if an edited timeline entry loses its original value/author; if automated noise cannot be filtered; if a mitigation action cannot link to its observed result; if source/original time is irrecoverable; or if the resolution milestone can be moved without provenance.

## Output contract

Return an `incident-timeline-capture-contract` with: event taxonomy; source/original/received timestamps; normalization; delayed/skew cues; manual entry/correction; pinned milestones; automated-noise filtering; action-result linkage; evidence links; attribution; and export/postmortem consumption. Include one clock-skew scenario.

## Handoffs

Hypothesis/evidence logs provide reasoning links, mitigation tracking provides action state, stakeholder/status-page owners provide communication events, and postmortem authoring consumes the finalized chronology.