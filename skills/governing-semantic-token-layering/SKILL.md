---
name: governing-semantic-token-layering
description: Use when primitive, semantic, component, and product-local tokens form dependency layers and leakage between layers would couple consumers to implementation detail.
---

# Governing Semantic Token Layering

## Overview
A token system gains leverage when consumers depend on meaning rather than raw values. This skill owns the dependency boundaries among primitive, semantic, component, and product-local layers. Its concern is not naming aesthetics; it is preventing a dependency graph in which high-level meaning is bypassed or lower layers depend upward.

## Parent Contract
**Required parent:** `architecting-design-tokens`.

The parent establishes the token architecture. This specialist tests and governs directional dependencies once multiple semantic layers exist.

## Layer Law
Declare allowed edge directions. A component token may depend on a semantic role; a semantic role may depend on a primitive; a primitive must not depend on a component. Direct primitive consumption by product UI is either forbidden or recorded as explicit debt with scope and expiry. Layer crossing needs a reason tied to semantic ownership, not convenience.

The key decision is whether a concept deserves a semantic owner. Repeated literal equivalence does not create semantic identity: two colors may currently match while serving different roles and therefore must not be aliased merely to deduplicate values.

## Invariants
Dependencies flow downward through approved layers. Semantic tokens remain meaningful if primitive values change. Component tokens do not become a second global semantic layer by accidental reuse. Local exceptions are discoverable. Equivalent literals do not imply interchangeable meaning.

## Evidence
Evidence includes dependency graphs colored by layer, forbidden-edge scans, representative theme changes that alter primitives while preserving roles, and consumer audits showing which code bypasses semantic contracts. A useful proof is the ability to change a primitive family and predict exactly which semantic roles should move.

## Failure Modes
Failure includes components reading raw palette indexes, semantic aliases named after current colors, primitives referencing component state, component tokens reused globally because they are convenient, and migrations that merge distinct meanings because their current values happen to match.

## Falsification
Falsification changes primitive values, separates previously equal values, and searches for consumers whose intended meaning changes unexpectedly. Also remove a semantic alias and ask whether a component had been relying on its implementation identity rather than role. Unpredictable blast radius falsifies the layering contract.

## Recovery
Recovery classifies each offending edge by intended meaning, inserts or restores the semantic owner when justified, and migrates consumers in a measured sequence. Do not solve leakage by adding aliases with no semantic definition; that only hides the edge.

## Output and Handoff
Output: `semantic-token-layering-contract`, including layer definitions, allowed dependency directions, exception policy, debt register, and migration evidence. Handoff visual role design to the token parent and component API concerns to component-system governance.

## Sibling Boundary and delete-the-skill
Type conformance proves values are compatible; reference integrity proves edges are valid. Neither decides whether an otherwise valid edge is architecturally permitted between layers. The delete-the-skill test therefore exposes unowned dependency-leakage decisions.