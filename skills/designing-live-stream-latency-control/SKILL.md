---
name: designing-live-stream-latency-control
description: Use when viewers can trade playback stability for lower live latency and need to understand delay from live edge, catch-up behavior, and consequences of low-latency modes.
---

# Designing Live Stream Latency Control

## Parent Contract
**Required parent:** `designing-media-playback-experiences`.

This faculty owns user-visible control over distance from the live edge. It is distinct from basic buffering and live-state labeling. The product may expose modes such as low latency, normal/stable, or automatic, each affecting buffer depth, catch-up rate, and resilience.

## Decision Boundary
Define latency in terms users can act on. Some products need only “Live” versus “Behind”; others may show seconds. If modes are selectable, explain the tradeoff: lower latency can increase stalls on weak networks. Decide when the player may gently increase playback rate to catch up and when that would harm content, accessibility, or user expectations. A “Go Live” action should jump deliberately to the edge and preserve selected tracks.

Latency state must distinguish intentional pause/rewind from transport drift. Do not constantly force a user who paused back to live. When network conditions deteriorate, automatic mode can expand buffer, but UI should not claim low-latency performance it no longer achieves.

## Failure Topology
- Player labels “Low latency” while actual delay grows silently to a minute.
- Auto catch-up speeds spoken audio enough to reduce comprehension without indication.
- “Go live” becomes enabled for a one-second difference and creates unnecessary jumps.
- Rebuffering logic erases a user's intentional behind-live position.
- Latency is calculated against local wall clock instead of stream timing and is wrong after clock skew.
- Mode setting persists to content where low latency is unsupported.

## Falsification and Recovery
Test strong/weak networks, pausing, rewind, reconnect, long viewing sessions, mode changes, catch-up, and unsupported streams. Compare displayed state to measured stream live edge. The design fails when intentional DVR delay is mistaken for fault or when advertised latency mode cannot be reconciled with actual behavior.

Recover by deriving latency from stream timeline, setting meaningful thresholds, separating user delay from transport drift, constraining catch-up rates, and degrading mode visibly when conditions require a larger buffer.

## Output Contract
Return `live-stream-latency-contract` with live-edge metric, user-visible modes, thresholds, go-live behavior, catch-up policy, intentional-delay protection, network degradation behavior, and latency verification cases.
