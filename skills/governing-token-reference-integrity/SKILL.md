---
name: governing-token-reference-integrity
description: Use when design tokens alias or reference other tokens and the reference graph must remain acyclic where required, resolvable, stable under rename, and diagnosable across packages.
---

# Governing Token Reference Integrity

## Overview
Token aliases turn a flat dictionary into a dependency graph. This skill owns the graph-integrity decisions: what constitutes a legal edge, when cycles are invalid, how dangling references are reported, and how identities survive moves or renames. It does not decide the visual value of a token.

## Parent Contract
**Required parent:** `architecting-design-tokens`.

The parent supplies the token taxonomy and layer rules. This specialist treats references as graph edges that must remain trustworthy through editing, packaging, and resolution.

## Reference Graph
Model each token as a stable identity and each alias as a typed directed edge. Preserve source location and package boundary on every edge. A legal graph must distinguish intentional indirection from accidental recursion; if a platform supports composite values, references inside composites are edges too.

Decision ownership covers canonical reference syntax, cross-package addressing, rename semantics, cycle policy, missing-target behavior, and diagnostic paths. A resolver should be able to return the complete chain `semantic -> primitive -> literal` rather than only the final literal.

## Integrity Invariants
A reference target exists at the revision being consumed. Renaming a target either updates dependents atomically or produces an explicit broken-reference state. Cycles are rejected unless a documented resolver semantics makes them finite. Package boundaries cannot silently redirect an alias to a same-named token in another namespace.

## Evidence
Required Evidence is machine-readable dependency traversal plus human-readable chain samples, orphan scans, cycle detection, rename/move rehearsal, and package-boundary tests. For a migration, capture both before and after graph identities so accidental retargeting is visible.

## Failure Cases
Failure includes dangling aliases that resolve to null, self-reference hidden inside composites, long cycles crossing package boundaries, same-name accidental capture after import, and refactors that preserve final color in one theme while changing semantic ancestry. A particularly dangerous case is a resolver that substitutes a literal on failure and conceals the broken edge.

## Falsification
Falsification deletes or renames a referenced target, introduces a synthetic cycle, reorders package imports, and resolves every inbound alias. If the system silently chooses another target, emits an unexplained literal, or cannot identify the broken chain, the integrity contract fails.

## Recovery
Recovery quarantines invalid edges, restores the last known valid target identity, and repairs references at their source. Do not patch each consumer with literals. When a cycle reflects a modeling mistake, collapse or re-layer the semantic dependency rather than teaching the resolver an arbitrary escape.

## Output and Handoff
Output: `token-reference-integrity-contract` with identity rules, allowed edge forms, cycle policy, orphan diagnostics, rename semantics, and evidence commands. Handoff semantic re-layering to `architecting-design-tokens`; handoff consumer impact analysis to migration auditing.

## Sibling Boundary and delete-the-skill
Sibling resolution-context governance decides among valid contextual candidates; this skill decides whether the reference chain itself is valid. The delete-the-skill test passes because a token system can have perfect naming and contextual precedence while still containing corrupt alias graphs that no sibling owns.