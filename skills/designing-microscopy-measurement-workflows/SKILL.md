---
name: designing-microscopy-measurement-workflows
description: Use when this specialist's decision ownership is materially in scope. Own image-based scientific measurement workflows for microscopy where scale, channels, regions, annotations, segmentation provenance, and measurement tables must stay linked to source imagery.
---
# Designing Microscopy Measurement Workflows

## Parent Contract

**Required parent:** `designing-scientific-and-engineering-instrumentation`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own measurement interaction on microscopy images or image stacks. Decide calibration/scale, channel and z/time selection, region-of-interest creation, measurement tools, segmentation/threshold provenance, annotation, overlays, and linkage from tabular results back to image evidence. Generic image editing does not own scientific measurement truth.

## Inputs and evidence

Require image/stack identity, pixel/physical scale, acquisition metadata, channels, z/time dimensions, calibration validity, measurement types, segmentation algorithms/options, ROI geometry, units, uncertainty/resolution, and export requirements. Identify derived/composite channels versus acquired data.

## Procedure

Keep acquisition metadata and physical scale visible/recoverable. Distinguish display contrast from pixel-value transformation so visual enhancement does not silently alter measurement. ROIs need stable identity and linkage to measurement rows. For automated segmentation, expose model/algorithm/version and parameters, allow inspection of boundaries, and preserve manual corrections separately. Multi-channel measurements must state the active/source channel. Z/time navigation should not detach annotations from their plane/time applicability. Tables should select/highlight the corresponding ROI in the image and vice versa.

## Failure topology

Failures include measurements in pixels when physical scale is invalid, contrast adjustment altering quantitative values, annotations appearing on the wrong z-plane, segmentation results with no algorithm provenance, ROI IDs changing after sorting, and exported tables detached from source images. Another failure is composite fluorescence color encouraging users to assume channels are co-located without registration evidence.

## Falsification

Reject if a measurement cannot identify image/ROI/unit; if physical scale validity is unknown; if display-only adjustments can affect quantitative analysis unnoticed; if segmentation provenance is missing; if an ROI measurement cannot be navigated back to the exact plane/channel; or if manual segmentation correction overwrites original automated output without history.

## Output contract

Return a `microscopy-measurement-workflows-contract` with: image/stack identity; spatial calibration; channel/z/time context; ROI model; measurement types/units; display-versus-analysis transforms; segmentation provenance; correction history; bidirectional image-table linkage; annotation scope; and export provenance. Include one invalid-scale and one segmentation-correction scenario.

## Handoffs

Sample tracking links specimen identity, experimental provenance captures acquisition/setup, image/media workspaces supply viewing mechanics, and model fitting/experiment comparison may consume derived measurements.