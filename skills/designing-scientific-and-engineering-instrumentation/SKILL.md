---
name: designing-scientific-and-engineering-instrumentation
description: Own the interaction architecture for instrument-facing scientific and engineering workspaces where configuration, live measurement, provenance, safety, and reproducibility must remain synchronized.
---
# Designing Scientific and Engineering Instrumentation

## Decision ownership

Own the top-level contract for interfaces that observe or control laboratory, test, measurement, or process instruments. Decide how instrument identity, configuration, live state, experiment/run state, measurement quality, calibration, provenance, alarms, and control authority coexist. This owner does not define a particular experiment, signal-analysis algorithm, or safety threshold; it ensures those specialists share one coherent runtime model rather than becoming disconnected panels.

## Inputs and evidence

Require instrument inventory and stable IDs, connection states, measurement channels and units, control/setpoint capabilities, configuration schema, experiment lifecycle, calibration state, data provenance, user roles, safety interlocks, expected sampling rates, latency, and degraded/offline behavior. Inspect representative real runs with dozens of channels, instrument reconnects, calibration expiry, and data-quality issues—not only idle screenshots.

## Procedure

Separate observe, configure, and control authority. A user viewing telemetry should not accidentally be one gesture away from changing an actuator. Establish one canonical instrument header with identity, connection, active configuration, calibration validity, control owner, and current run association. Treat each measurement as value + unit + timestamp + quality/provenance, not a naked number. Configuration changes need clear effective timing and relationship to experiment data. During an active run, distinguish live measurements from derived analysis and from operator annotations. Safety interlocks and alarms must remain visible across tabs/modes. If the instrument disconnects, freeze/mark last known values and show freshness rather than continuing to look live.

## Failure topology

Failures include stale values appearing current, units disappearing at high density, configuration changing mid-run without provenance, calibration expiry hidden behind settings, observe and control modes visually indistinguishable, alarms suppressed by navigation, and reconnect creating a second apparent instrument identity. Another critical failure is exporting data without enough instrument/configuration metadata to reproduce or interpret it later.

## Falsification

Reject if users cannot identify which physical/logical instrument produced a visible value; if last-known data can be mistaken for live; if changing configuration cannot be tied to an effective time/run; if an invalid calibration does not affect measurement trust cues; if safety-critical state can disappear when analysis view opens; or if two different units/channels can render as comparable without explicit unit context.

## Output contract

Return a `scientific-and-engineering-instrumentation-contract` containing: instrument identity model; observe/configure/control separation; connection/freshness states; measurement value-unit-time-quality schema; configuration provenance; run linkage; calibration visibility; alarm/interlock persistence; control authority; export provenance requirements; and degraded-mode behavior. Include one mid-run configuration change and one disconnect/reconnect scenario.

## Handoffs

Delegate telemetry dashboards, experiment setup/run control, calibration, live signal monitoring, waveform/spectrum analysis, microscopy measurement, sample/plate/lot traceability, process trends, alarm thresholds, setpoints, provenance, experiment comparison, parameter sweeps, model fitting, and safety interlocks to dedicated owners. Generic data-viz and high-stakes skills remain lower-level authorities.