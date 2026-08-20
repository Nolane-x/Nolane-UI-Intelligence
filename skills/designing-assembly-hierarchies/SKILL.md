---
name: designing-assembly-hierarchies
description: Own product assembly structure across components, instances, subassemblies, mates/constraints, suppression, variants, reference context, BOM linkage, and edit-in-place boundaries.
---
# Designing Assembly Hierarchies

## Decision ownership

Own mechanical/product assembly organization, where component instances and subassemblies carry product meaning beyond generic scene parentage. Decide component definition versus occurrence, assembly tree, mates/constraints, suppression, variants/configurations, edit-in-place context, reference paths, and BOM-oriented identity.

## Inputs and evidence

Require component/part definitions, instance IDs, subassemblies, mate/constraint model, variant/configuration system, suppression states, external references, BOM metadata, permissions, and expected assembly scale. Identify shared component definitions used in many occurrences.

## Procedure

Distinguish part definition from each occurrence in the assembly. Selecting an occurrence should reveal path and whether edits affect one occurrence parameters, the shared part, or assembly-level transforms. Subassembly context must be clear during edit-in-place, with surrounding geometry visually de-emphasized but recoverable. Mates/constraints need status and affected components. Suppressed components remain in structure with reason/configuration scope. Variants/configurations should show effective substitutions/suppressions without cloning the entire assembly invisibly. Large trees require search/filter while preserving parent path.

## Failure topology

Failures include editing one occurrence and unintentionally changing all instances, losing assembly context during part edit, suppressed components disappearing entirely, broken mates hidden, variant changes mutating the base configuration, and duplicate part names with unclear occurrence paths. Another failure is scene hierarchy transform semantics overriding mechanical assembly constraints unexpectedly.

## Falsification

Reject if definition-versus-occurrence edit scope is ambiguous; if edit-in-place cannot identify current assembly context; if suppressed/broken components vanish with no trace; if variant overrides cannot be distinguished from base; if mate failures cannot locate components; or if a component occurrence lacks a stable path/identity.

## Output contract

Return an `assembly-hierarchies-contract` with: part/definition identity; occurrence path; subassembly structure; edit scope/context; mate/constraint status; suppression; variants/configurations; external references; BOM linkage; search/scale behavior; and broken-reference recovery. Include one shared-part edit-scope scenario.

## Handoffs

Scene hierarchy provides general outliner mechanics, parametric constraints govern geometric dependencies, clash inspection evaluates assemblies, material assignment may occur at part/occurrence scope, and manufacturing handoff consumes BOM/product structure.