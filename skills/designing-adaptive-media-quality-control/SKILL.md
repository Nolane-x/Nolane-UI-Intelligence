---
name: designing-adaptive-media-quality-control
description: Use when streaming media can change rendition automatically or manually and users need a coherent relationship among Auto mode, resolution/bitrate choices, bandwidth, device capability, data use, and actual active quality.
---

# Designing Adaptive Media Quality Control

## Parent Contract
**Required parent:** `designing-media-playback-experiences`.

This faculty owns quality-selection semantics above the streaming engine. It does not implement adaptive bitrate algorithms. It decides which choices are exposed, how Auto differs from fixed preference, what active rendition means, and how quality interacts with data-saving or device constraints.

## Decision Boundary
Separate user preference from currently delivered rendition. In Auto, the player may change resolution continuously; showing “1080p” as if locked is misleading. A fixed selection can be treated as target, maximum, or strict rendition depending on engine capability—label the actual semantics. Avoid listing raw bitrate variants that users cannot interpret when resolution/frame rate/HDR labels are more meaningful.

Quality choices may be constrained by viewport, device decoder, DRM, subscription, battery/data policy, live latency, or casting receiver. If an option becomes unavailable, explain the constraint instead of silently switching while leaving selection unchanged. Remember preference only at a sensible scope; a 4K desktop preference may not belong on cellular mobile.

## Failure Topology
- Menu displays a fixed check beside 1080p while Auto has already fallen to 480p.
- User selects 4K but engine treats it as a maximum and frequently delivers lower quality without any distinction.
- Unsupported HDR/codec variants appear selectable and fail at playback.
- Data-saver policy silently overrides manual choice with no visible reason.
- Casting quality menu controls local renditions instead of receiver capability.
- Preference follows users to a constrained device and causes repeated buffering.

## Falsification and Recovery
Test Auto adaptation, fixed preferences, network changes, data saver, different viewport/device capability, casting, live streams, and unsupported variants. Inspect actual rendition metadata against the UI. The design fails if a displayed selection cannot be reconciled with what is being delivered.

Recover by separating preference/active rendition, labeling target-versus-fixed semantics, capability-filtering options, surfacing policy overrides, and scoping persistence. Use quality labels meaningful to users while retaining technical diagnostics elsewhere.

## Output Contract
Return `adaptive-media-quality-contract` with option semantics, Auto behavior, active-versus-preferred display, capability/policy constraints, persistence scope, data/latency interactions, receiver behavior, and rendition verification cases.
