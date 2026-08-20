---
name: designing-extrusion-and-inset-operations
description: Own interactive extrusion and inset modeling operations with direction, distance, region/individual behavior, topology preview, numeric entry, cancel, and non-manifold safeguards.
---
# Designing Extrusion and Inset Operations

## Decision ownership

Own two common topology-generating operations where selected faces/edges produce new geometry. Decide operation mode, region versus individual behavior, direction/reference, distance/offset, thickness, preview, numeric entry, topology result, cancel, and follow-up transform state. This owner is narrower than generic modeling command execution because duplicate/internal geometry failures are common.

## Inputs and evidence

Require selection type, mesh topology, normals, coordinate/reference space, allowable operation variants, snapping, numeric units, non-manifold policy, history model, and modifier stack behavior. Identify whether an extrusion creates coincident geometry at zero distance and how cancellation removes it.

## Procedure

Before commit, show operation type and affected component count. Extrusion should expose direction/axis or normal basis and allow numeric entry while preserving visual preview. Region versus individual extrusion must be explicit because topology differs. Inset needs offset/thickness mode and boundary handling. Cancellation must restore pre-operation topology, not leave duplicate faces. Warn or block outcomes that create invalid/non-manifold structures according to product policy. After commit, keep the operation parameters editable in history/last-operation controls when supported.

## Failure topology

Failures include zero-distance extrusion leaving doubled faces, normals causing movement opposite expectation, region/individual mode hidden, inset self-intersection, numeric unit mismatch, cancel reverting movement but not created topology, and repeated operation accidentally extruding twice. Another failure is geometry preview lag that lets users confirm a different result from what they saw.

## Falsification

Reject if cancel can leave new topology; if operation direction/reference is unclear; if region versus individual cannot be identified; if numeric value unit is unknown; if preview/commit topology can differ under normal latency; or if invalid self-intersection/non-manifold result can be created with no detection where the model kernel knows it.

## Output contract

Return an `extrusion-and-inset-operations-contract` with: eligible selection; operation variants; direction/reference; numeric parameters/units; preview; snapping; topology validity checks; cancel/undo; repeated-operation guard; and post-commit parameter editability. Include one zero-distance cancel and one self-intersection scenario.

## Handoffs

Mesh selection supplies components, 3D snapping/constraints supply precision, boolean modeling handles volume combinations, and history/undo provides transactional recovery.