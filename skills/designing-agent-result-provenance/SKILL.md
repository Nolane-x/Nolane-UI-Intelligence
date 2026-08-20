---
name: designing-agent-result-provenance
description: Attach inspectable lineage to agent results so users can distinguish sourced facts, derived transformations, tool observations, generated content, and unverified claims.
---

# Designing agent result provenance

Agent outputs may combine retrieved sources, local files, tool results, remembered context, calculations, and generated synthesis. Use this skill when users need to know where important claims or artifacts came from.

## Decision ownership

Own provenance granularity, source identity, transformation lineage, freshness/version, linkability, and distinction between evidence and inference. Decide which outputs require claim-level provenance versus artifact-level summary.

## Inputs and evidence

Collect retrieval traces, file versions, URLs, database queries, tool outputs, transformations, memory sources, timestamps, generated artifacts, and verification steps. Identify sources that can change after the task.

## Procedure

Represent provenance near the result it supports. For factual claims, link to concrete sources or tool observations. For transformed artifacts, record inputs and operations. Mark inference separately from directly observed data.

Capture source version or timestamp when mutability matters. Avoid implying that citing a source proves the agent’s interpretation. Preserve provenance through delegation and summarization rather than collapsing all lineage into the final agent identity.

Provide a compact default with deeper inspection for complex tasks.

## Failure topology

A generic “sources” list at the bottom can’t tell users which source supports which claim. Provenance can become fake precision when it records a file name but not the version actually used. Another failure is treating model-generated explanations as sourced facts because they were adjacent to retrieved documents.

## Falsification

Pick important claims and trace them backward to raw evidence. Modify source files and verify version/freshness signals. Delegate a subtask and inspect whether lineage survives. Attempt to cite a source that does not actually support the claim and ensure review can detect the mismatch.

## Output contract

Produce an `agent-result-provenance-contract` defining provenance units, source identifiers, version/freshness, evidence-vs-inference labeling, transformation lineage, delegation preservation, and claim-to-source audit tests.

## Handoffs

Use `designing-agent-context-inspection` for active inputs, `designing-agent-tool-selection-visibility` for tool identity, `designing-agent-uncertainty-disclosure` for weak support, and `engineering-ui-evidence-workflows` for broader evidence governance.