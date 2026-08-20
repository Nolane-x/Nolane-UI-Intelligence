---
name: designing-uml-and-modeling-diagrams
description: Use when this specialist's decision ownership is materially in scope. Own typed modeling-diagram interactions such as structured node compartments, relationship end semantics, multiplicity, and synchronization with an underlying model.
---
# Designing UML and Modeling Diagrams

## Parent Contract

**Required parent:** `designing-diagramming-and-node-graph-editors`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own UI behavior for formal modeling diagrams where visual elements represent typed model entities and relationships. Decide how structured compartments, relationship kinds, endpoint adornments, multiplicity/cardinality, stereotypes or type tags, and model-versus-view identity are inspected and edited. This owner is notation-aware without claiming that one notation must be used for every system design.

## Inputs and evidence

Collect supported diagram families and relationship types, source-of-truth model schema, whether one model entity can appear in several diagrams, editable versus generated properties, validation rules, expected model size, and import/export round-tripping requirements. Determine whether notation fidelity is required for standards compliance or only familiar communication.

## Procedure

Separate model identity from diagram occurrence: users need to know whether deleting a shape removes the view or the underlying entity. Structured nodes should expose compartments that can collapse without hiding the fact that more model content exists. Relationship creation must reveal the chosen relationship type and endpoint semantics before commit; cardinality/multiplicity should be editable near the relevant end, not in a disconnected form with unclear target. If the diagram reflects source code or schema, show synchronization status and conflicts rather than silently overwriting manual edits. Provide notation legends or accessible text for symbols whose meaning is not obvious.

## Failure topology

Failures include deleting a visual occurrence and unexpectedly deleting the model entity, multiple views drifting out of sync, relationship arrows that are visually similar but semantically different, multiplicity labels detached from their endpoints, compartments truncating critical members, and generated diagrams that users can apparently edit even though changes will be overwritten. Another failure is perfect notation with unusable navigation on large models.

## Falsification

Reject if users cannot distinguish view deletion from model deletion; if relationship type can change through a subtle icon with no textual confirmation; if an entity shown in two diagrams can display contradictory editable state without a conflict cue; if synchronization can overwrite local edits without preview; or if notation meaning is inaccessible to non-visual users.

## Output contract

Return an `uml-and-modeling-diagrams-contract` with: model/view identity rules; supported node/relationship semantics; compartment behavior; endpoint/multiplicity editing; notation labeling; synchronization state machine; generated-versus-editable boundaries; delete consequences; validation hooks; and multi-diagram consistency requirements. Include one entity appearing in multiple views as a test scenario.

## Handoffs

Use graph creation/connection/routing owners for lower-level mechanics, graph validation for finding presentation, graph diff/history for model changes over time, and dependency exploration for impact inspection. The underlying schema or code-model semantics remain authoritative outside this skill.