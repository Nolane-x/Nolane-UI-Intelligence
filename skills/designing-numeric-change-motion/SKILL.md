---
name: designing-numeric-change-motion
description: Use when a displayed numeric value changes and motion should reveal direction, magnitude or update occurrence without falsifying intermediate values or degrading rapid reading.
---

# Designing Numeric Change Motion

## Parent Contract
**Required parent:** `designing-motion`. Numerical meaning, units, precision and analytical truth remain owned by data/domain faculties.

## Decision Boundary
This skill owns temporal presentation of a value that has changed: counters, balances, KPIs, scores, quantities, prices or measurements. It must preserve the authoritative start/end values and never invent a meaningful trajectory where none exists.

Choose a technique based on what users need to perceive. A brief highlight can answer “this changed.” Digit rolling can reinforce direction for compact counters. Interpolating through intermediate numbers is appropriate only when those values are understood as animation frames, not observed measurements; for financial or scientific contexts, fake intermediate readings can be misleading.

Preserve digit stability. Tabular numerals, fixed decimal alignment and unit placement can prevent nearby layout from jittering. Large magnitude changes may need sign/delta annotation instead of longer animation. Rapid streams should coalesce to the latest value or use rate-appropriate visualization; do not queue every tick.

Assistive output needs separate policy. Screen readers should not announce dozens of animation-frame numbers. Announce the committed value or a meaningful aggregated change according to context and live-region priority.

## Failure Topology
- A bank balance “counts” through values that look like real balances.
- Variable-width digits cause the entire dashboard to shake.
- High-frequency updates queue and the display lags seconds behind truth.
- Green/red directional animation is the only indicator of gain/loss.
- Screen reader announces every interpolated frame.

## Falsification and Recovery
Test positive/negative/zero changes, decimal/large magnitude, unit changes, rapid update bursts, localization separators, tabular/non-tabular fonts, screen reader and reduced motion. Compare visible final value timestamp with model timestamp; any persistent lag or fabricated semantic reading fails.

Recover by coalescing to latest truth, replacing interpolation with localized change highlighting, stabilizing numeric geometry and decoupling assistive announcements from visual frames.

## Output Contract
Return `numeric-change-motion-contract` with change purpose, technique, interpolation truth policy, digit/unit geometry, burst/coalescing behavior, color-independent direction cue, assistive announcement and reduced-motion fallback.