---
name: designing-experiment-setup-workflows
description: Own preparation of reproducible experiment runs across protocol, instruments, samples, parameters, prerequisites, resource reservations, and preflight validation.
---
# Designing Experiment Setup Workflows

## Decision ownership

Own the state before an experiment begins. Decide protocol/version selection, instrument assignment, sample/input linkage, parameter specification, resource constraints, prerequisite checks, optional deviations, and the preflight summary that becomes the run's starting provenance. This owner does not execute the run or analyze results.

## Inputs and evidence

Require experiment/protocol schema, versioned method, eligible instruments, calibration/availability, sample identities, parameter ranges and units, environmental prerequisites, consumables/resources, safety requirements, operator roles, and data destination. Identify defaults that are scientifically safe versus merely convenient.

## Procedure

Start from a versioned protocol or explicit ad-hoc definition and show which fields are inherited versus overridden. Resolve instrument and sample identities early enough to validate compatibility. Parameter entry must carry unit/range and flag values outside validated operating envelopes. Prerequisites—calibration, consumables, environment, permissions, data storage—should be summarized in a preflight that distinguishes blocking from advisory findings. Deviations from protocol need rationale/provenance. Before start, freeze or snapshot the setup into a run manifest so later configuration changes do not rewrite what the experiment actually used.

## Failure topology

Failures include selecting an instrument whose calibration is expired, defaults copied from an old protocol without version visibility, unit mismatches, samples linked by ambiguous labels, setup changed after run start with no provenance, and preflight warnings scattered across tabs. Another failure is forcing every exploratory experiment through a rigid regulated workflow even when policy allows lightweight setup.

## Falsification

Reject if a run can start without knowing protocol/version and instrument identity; if invalid parameter units/ranges are not surfaced; if sample IDs can collide; if blocking prerequisites are discoverable only after execution begins; if deviations cannot be recorded; or if setup edits after start mutate the original manifest.

## Output contract

Return an `experiment-setup-workflows-contract` with: protocol/version; inherited/overridden fields; instrument/sample identity; parameter schema with units/ranges; resource/prerequisite checks; blocking/advisory findings; deviation record; operator; data destination; and immutable run-manifest snapshot. Include one expired-calibration and one protocol-deviation case.

## Handoffs

Experiment run control consumes the frozen setup; calibration, sample tracking, plate layout, setpoint, and safety owners provide prerequisite evidence. Experimental provenance preserves the resulting manifest.