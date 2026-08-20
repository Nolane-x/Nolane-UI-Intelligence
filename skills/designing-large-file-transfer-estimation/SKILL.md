---
name: designing-large-file-transfer-estimation
description: Use when transfers are long enough that users need useful time, size, bandwidth, and completion estimates without presenting volatile network predictions as precise promises.
---

# Designing Large File Transfer Estimation

## Parent Contract
**Required parent:** `designing-file-transfer-and-storage`.

This faculty owns predictive feedback for long transfers. It does not own the transfer protocol itself. It decides when estimates are stable enough to show, how uncertainty is represented, and how changing throughput, processing phases, pause, retry, or compression affect remaining-time claims.

## Decision Boundary
Separate known total bytes, transferred/acknowledged bytes, current throughput, and non-transfer processing. Estimate time only after enough throughput history exists; initial “calculating” is more truthful than a wildly oscillating number. Smooth transient spikes without hiding sustained degradation. Present ranges or approximate wording when variance is high. If server-side processing follows transfer, label it as another phase rather than adding unknown processing time to a fake download ETA.

Large uploads/downloads may change rate when app backgrounds, network type changes, concurrency shifts, or server throttles. Recompute and communicate material changes. Users should still see deterministic progress (bytes/percentage where valid) even when ETA is unavailable. Do not infer mobile data cost unless network/platform data is authoritative.

## Failure Topology
- ETA jumps from 2 minutes to 3 hours every few seconds.
- Transfer reaches “100%, 0 seconds remaining” and then spends ten minutes processing with no new label.
- Estimate uses bytes read locally instead of bytes durably acknowledged.
- Paused transfer continues counting down.
- Network switch leaves stale throughput and misleading ETA for minutes.
- Unknown compressed output size is presented as exact total.

## Falsification and Recovery
Simulate stable/variable bandwidth, slow start, throttling, pause/resume, network switch, concurrent transfers, server processing, unknown size, and app background. Compare estimates with actual remaining time statistically rather than one happy-path run. The design fails if precision suggests confidence the estimator does not have.

Recover by delaying ETA until evidence stabilizes, smoothing with bounded windows, falling back to deterministic progress, separating phases, resetting estimator after major network changes, and using approximate/range language under high variance.

## Output Contract
Return `large-transfer-estimation-contract` with measurable inputs, estimator warm-up/smoothing, confidence/approximation rules, phase separation, reset triggers, paused/unknown behavior, deterministic fallback, and transfer-estimate verification scenarios.
