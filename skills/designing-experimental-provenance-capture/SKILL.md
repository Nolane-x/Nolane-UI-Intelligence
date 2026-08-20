---
name: designing-experimental-provenance-capture
description: Own traceability from scientific results back to protocol, instruments, samples, calibration, configuration, raw data, transformations, software, operators, and timestamps.
---
# Designing Experimental Provenance Capture

## Decision ownership

Own the provenance graph that makes an experiment and its derived results reconstructable. Decide which identities and versions must be recorded, how raw/derived data lineage is represented, what metadata is automatic versus operator-entered, how corrections are versioned, and how provenance remains attached to exports. This owner does not decide scientific conclusions.

## Inputs and evidence

Require run manifest, protocol/version, instrument IDs/config/calibration, sample/lot IDs, operator, timestamps/clock source, raw data assets, analysis software/version, parameter settings, transformations, derived outputs, annotations, and corrections. Identify external files or manual steps that cannot be captured automatically.

## Procedure

Capture immutable IDs and versions at the moment they become effective, not retrospectively from current settings. Link raw data to acquisition configuration and sample/instrument context. Derived results form explicit lineage edges to source data plus analysis method/version/parameters. Manual annotations/corrections carry actor/time and never overwrite original evidence invisibly. Provide a human-readable provenance summary plus machine-exportable references. If provenance is incomplete, mark missing edges/fields rather than manufacturing defaults. Exports should embed or accompany enough identifiers to resolve the source record later.

## Failure topology

Failures include current instrument settings retroactively displayed as run settings, derived plots detached from raw files, software updates changing results without version record, sample labels used instead of stable IDs, corrections overwriting source values, and exported CSVs losing all provenance. Another failure is a giant metadata dump that technically exists but cannot answer "where did this result come from?".

## Falsification

Reject if a derived result cannot traverse to raw data and analysis parameters; if acquisition config is read from current instrument state rather than frozen run evidence; if corrections erase originals; if missing provenance appears complete; if software/method version is absent for material transformations; or if exported results cannot identify the originating run.

## Output contract

Return an `experimental-provenance-capture-contract` with: run/protocol identity; instrument/config/calibration; sample/lot lineage; raw-data identity; operator/time; transformation/software/version/parameters; derived-result lineage; annotation/correction history; completeness state; and export/resolution strategy. Include one reanalysis-with-new-software scenario.

## Handoffs

Experiment setup/run control create source events, calibration/sample/lot owners supply identities, waveform/spectrum/model fitting create analysis lineage, and comparison consumes provenance to ensure like-for-like results.