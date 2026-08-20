---
name: designing-batch-and-lot-traceability
description: Own traceability of material or production lots through inputs, transformations, outputs, tests, locations, and affected downstream uses with immutable lineage and recall-oriented exploration.
---
# Designing Batch and Lot Traceability

## Decision ownership

Own batch/lot lineage for scientific, manufacturing, or process contexts. Decide lot identity, parent materials, transformations, split/merge, process steps, test results, locations, disposition, and forward/backward trace. This owner differs from individual sample tracking by emphasizing cohort/material transformation and downstream impact.

## Inputs and evidence

Require lot identifiers, input/output relationships, process step records, quantities/units, timestamps, equipment, operators, quality/test results, storage/transfer, disposition, and downstream consumption. Identify regulatory retention and recall requirements.

## Procedure

Keep lot IDs immutable and represent transformations as explicit events rather than overwriting material state. A user must be able to trace backward from an output to contributing input lots and forward from an input to all derived lots/products/experiments. Split and merge must conserve or explain quantity. Attach tests and disposition to the correct lot/effective time. Location/custody changes remain historical. Impact exploration should separate confirmed use from potential/unknown because incomplete trace data changes risk interpretation.

## Failure topology

Failures include reused lot labels, merge events that erase source lots, tests attached to the wrong revision/state, quantities not reconciling, current location overwriting movement history, and forward trace stopping at a transformed lot. Another failure is presenting incomplete lineage as complete during recall or investigation.

## Falsification

Reject if any derived lot cannot enumerate source lots; if forward trace cannot find known consumers; if quantity imbalance is silent; if a test result has no lot/effective-time binding; if lineage completeness/freshness is unknown; or if disposed/rejected material can appear as eligible input without explicit override authority.

## Output contract

Return a `batch-and-lot-traceability-contract` with: lot identity; transformation events; input/output lineage; split/merge quantity accounting; equipment/operator/time; test/disposition binding; location/custody history; forward/backward trace; completeness/confidence; and downstream impact categories. Include one merged-lot recall scenario.

## Handoffs

Sample tracking handles individual specimens, process trend views handle operational measurements, experiment provenance links lots used in experiments, and dependency/graph exploration can provide navigation mechanics.