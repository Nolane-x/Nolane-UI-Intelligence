---
name: designing-driver-distraction-aware-information-density
description: Use when an automotive interface must adapt information volume, glance demand, interaction depth, and visual complexity to driving workload so important content remains comprehensible without treating every screen as a parked-state dashboard.
---

# Designing Driver-Distraction-Aware Information Density

## Density is an attention allocation decision
Automotive screens can display enormous amounts of data, but the driver cannot safely consume desktop-like information density while controlling a vehicle. This skill owns how much information is visible, how deeply it can be interacted with, and what is deferred or summarized according to driver role and driving workload.

## Parent Contract
**Required parent:** `designing-high-stakes-decisions`.

The parent establishes conservative decision making under high consequence. This specialist begins when information architecture and visual density must account for driving attention rather than only screen size.

## Attention-demand model
Classify visible information by decision urgency, glance frequency, reading burden, interaction steps, and whether the driver must visually search. The decision owner is the density envelope for each driving state or workload regime. High-value status may remain visible while low-urgency metadata, long lists, rich editing, or exploratory settings are deferred.

Avoid a simplistic “moving equals huge text” rule. A compact, stable status strip may be safer than a large surface that forces more scanning. Optimize for glanceability, predictability, and minimal visual search. Preserve consistent locations for frequently consulted information.

## Progressive disclosure
Use summary-first presentation during high-demand states and allow details when parked, in a passenger-owned region, or under an approved lower-demand interaction path. If information must be hidden temporarily, preserve a clear way to resume later. Do not remove context needed to understand an active warning or current vehicle state.

Notifications are part of density. Queue low-priority interruptions rather than allowing each app to claim attention independently. Multiple simultaneous badges, banners, route prompts, media overlays, and vehicle status elements should be arbitrated as one attention system.

## Typography and layout constraints
Type size, line length, icon recognition, contrast, and grouping should support quick parsing. Avoid paragraphs where a short action-oriented summary suffices. Dense tables and settings grids generally belong in parked/passenger contexts unless the task has been redesigned for glance-level interaction.

## Evidence
Evidence includes driving/workload assumptions, information-priority map, parked versus moving layouts, glance-oriented task reviews, notification-collision cases, and preserved resume state. Use simulator or controlled usability evidence where available and separate empirical findings from design heuristics.

## Failure modes
Characteristic Failure includes copying a tablet dashboard into the center stack, shrinking text to retain every field, hiding critical context alongside low-priority detail, several independent notification systems competing simultaneously, and dynamic layout changes that force the driver to relearn where status appears. Another failure is assuming voice makes a dense task safe without evaluating cognitive demand.

## Falsification
Populate the maximum realistic data set, trigger navigation and vehicle notifications together, switch from parked to moving mid-task, and test at representative glance durations. The contract fails if critical status requires extended visual search, if deferred information is lost, if density remains unchanged across materially different workload states without rationale, or if lower-priority content displaces urgent information.

## Recovery
Reclassify information by time-to-decision and role, remove or defer low-value material before reducing legibility, consolidate notifications, and stabilize recurring locations. If a task intrinsically requires long reading or complex editing, move it to a safer context instead of compressing it into a driving surface.

## Output and Handoff
Output: `driver-distraction-aware-information-density-contract`, containing workload regimes, information classes, density envelopes, disclosure rules, notification arbitration, resume behavior, and evidence. Handoff action availability to driving-state lockouts and warning interruption to vehicle-warning priority.

## Sibling Boundary and delete-the-skill
Sibling instrument-cluster priority owns the cluster’s safety-critical information hierarchy; this skill owns broader driver-facing density across infotainment and task surfaces. The delete-the-skill test passes because responsive layout alone cannot decide how much information a driver should be asked to process while attention is constrained.