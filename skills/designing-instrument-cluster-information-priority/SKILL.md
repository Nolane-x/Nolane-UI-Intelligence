---
name: designing-instrument-cluster-information-priority
description: Use when an instrument cluster must arbitrate persistent vehicle state, speed, telltales, warnings, driver-assistance status, navigation, energy/fuel, and contextual information so critical state remains stable and legible under competing demands.
---

# Designing Instrument Cluster Information Priority

## The cluster is an authoritative driving surface
An instrument cluster is not merely another display region. It often carries continuously referenced and safety-relevant vehicle information that must remain stable while secondary features compete for space. This skill owns the priority architecture that decides which information is persistent, which can temporarily expand, and which must never be displaced.

## Parent Contract
**Required parent:** `designing-high-stakes-decisions`.

The parent establishes evidence, authority, and conservative behavior for high-consequence UI. This specialist begins when information placement and persistence on the driver instrument cluster are being decided.

## Information tiers
Classify cluster information by continuous driving necessity, immediate hazard response, operational state, route/task assistance, and optional context. The exact taxonomy must align with OEM and applicable normative requirements. The decision owner is the protected set of information and its allowed displacement rules.

Persistent critical information should have stable anchors. Temporary content may occupy flexible regions but must yield when higher-priority warnings arrive. Navigation maneuvers, media metadata, phone status, efficiency coaching, and other contextual features should not force critical telltales or required driving state into unfamiliar locations.

## Mode and automation state
Modern clusters may change with drive mode, EV charging/energy state, advanced driver-assistance mode, or automation availability. Mode-specific content must communicate state changes clearly without making core status unpredictable. When automation mode changes authority/responsibility, the cluster should emphasize the current system state and driver obligations according to governing requirements.

## Warning integration
Warnings can interrupt cluster composition, but their lifecycle remains owned by vehicle-warning priority. This skill decides where and how the cluster reserves attention/space so urgent warnings can appear without obscuring other equally critical state. Avoid stacking multiple intense visual elements until hierarchy collapses.

## Legibility and glance behavior
Use concise labels, stable iconography, appropriate numeric alignment, and high recognition. Values frequently compared over time should not jump position. Avoid decorative animation near critical numeric/status fields. If personalization is allowed, constrain it so mandatory information remains discoverable and consistent.

## Evidence
Evidence includes information-tier mapping, protected anchors, mode transitions, simultaneous-warning layouts, personalization limits, driver-assistance states, and representative day/night themes. Capture dynamic transitions as well as resting layouts. Normative/OEM source revisions must be recorded where they define mandatory content.

## Failure modes
Characteristic Failure includes navigation cards displacing required status, different drive modes moving critical values unpredictably, personalization hiding telltales, several warnings competing without hierarchy, transient media content covering automation-state indicators, and decorative animation drawing attention from operational state.

## Falsification
Activate several optional features, switch modes, trigger urgent warnings, change personalization, and transition assistance/automation state rapidly. The contract fails if protected information disappears or moves without rule, if lower-priority content wins a collision, if state responsibility becomes ambiguous, or if warning insertion makes other mandatory state unreadable.

## Recovery
Restore the protected information frame first, remove or demote optional content, reconcile current authoritative vehicle/automation state, then reintroduce contextual information only into available regions. If the priority hierarchy conflicts with governing cluster requirements, escalate the contract rather than solving it through local layout tricks.

## Output and Handoff
Output: `instrument-cluster-information-priority-contract`, containing information tiers, protected anchors, displacement policy, mode behavior, personalization limits, warning accommodation, and evidence. Handoff warning lifecycle to vehicle-warning priority and wider center-stack density to distraction-aware density.

## Sibling Boundary and delete-the-skill
Sibling vehicle-warning priority owns the urgency and lifecycle of warnings; this skill owns the entire cluster hierarchy into which warnings enter. The delete-the-skill test passes because without a cluster priority owner, optional features and dynamic modes can gradually erode the stable placement of critical driving information.