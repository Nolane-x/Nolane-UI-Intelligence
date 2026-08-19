---
name: designing-device-battery-and-connectivity-state
description: Use when a connected peripheral's battery, signal, network, or link quality affects whether a task can complete and users need actionable device-health state rather than decorative telemetry.
---

# Designing Device Battery and Connectivity State

## Parent Contract
**Required parent:** `designing-device-integration-interfaces`.

This faculty owns device-health cues that influence operations. It does not build an observability dashboard for engineers. It decides when battery level, charging, signal/link quality, last-seen time, or connectivity state should be shown to users and how those values gate or warn about tasks.

## Decision Boundary
Treat telemetry freshness as part of the value. “80% battery” from three days ago is not current health. Show last updated or unknown state when stale. Use categorical warnings only when thresholds are meaningful for the operation; a low-battery printer may finish one page but not a 500-label batch. Connectivity can mean paired, connected, reachable, or data channel healthy—name the layer.

Avoid continuous noisy updates. Surface health at decision points: before long operation, when connection degrades, or in device management. Do not block tasks solely on estimated battery unless device/platform authority supports that threshold. If a device exposes no telemetry, degrade to Unknown rather than inventing a green healthy state.

## Failure Topology
- Stale battery value is displayed without age and users plan a long field task around it.
- “Connected” means Bluetooth link exists although the required service/data channel is dead.
- Low signal warning flashes every second as radio measurements fluctuate.
- UI blocks printing below 20% though printer itself would accept the job.
- Unknown battery is represented as 0%, implying immediate failure.
- Aggregate device card stays green while a critical required link is disconnected.

## Falsification and Recovery
Test fresh/stale/missing telemetry, charging, threshold crossings, fluctuating signal, transport connected but service unavailable, device sleep/wake, and long operations. The design fails if health cues make stronger claims than telemetry supports or if thresholds cause incorrect admission decisions.

Recover by timestamping/freshness modeling, separating transport/service reachability, smoothing noisy signals, using advisory versus hard gates explicitly, and presenting Unknown honestly. Tie warnings to task consequence, not telemetry availability alone.

## Output Contract
Return `device-health-state-contract` with telemetry fields/freshness, connectivity layers, threshold semantics, advisory/gating rules, smoothing/update cadence, unknown behavior, operation preflight, and device-health verification cases.
