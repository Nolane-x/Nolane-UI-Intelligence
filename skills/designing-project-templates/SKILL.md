---
name: designing-project-templates
description: Use when this specialist's decision ownership is materially in scope. Own reusable project/work structures, parameters, versioning, instantiation preview, inherited defaults, and safe evolution without pretending templates are live synchronized projects.
---
# Designing Project Templates

## Parent Contract

**Required parent:** `designing-project-and-work-management`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own reusable starting structures for projects or sets of work items. Decide what a template can contain, which values are parameters, how dates shift, how owners/roles resolve, how dependencies survive instantiation, how template versions evolve, and whether existing projects are ever updated. This owner separates reusable intent from copied historical instance data.

## Inputs and evidence

Require repeated project patterns, reusable work hierarchy, relative date logic, role placeholders, default statuses, dependency patterns, permissions, template ownership, update frequency, and whether regulated processes require version attribution. Identify fields that must never copy, such as actual completion evidence or historical assignee-specific data.

## Procedure

Design templates around semantic placeholders—project start, target milestone, owner role, team—rather than hard-coded dates and people. Before instantiation, preview resulting work count, hierarchy, dependencies, relative dates, unresolved role assignments, and optional sections. Give every created project a template-version provenance but treat the instance as independent unless an explicit managed-template model exists. Updating a template should create a new version; if migrations to existing projects are supported, present a diff and select changes rather than silently synchronizing.

## Failure topology

Failures include copying stale dates/assignees, duplicating historical comments, template edits unexpectedly mutating live projects, relative scheduling creating impossible weekends/time zones, dependencies pointing to template IDs instead of new instances, and giant templates users cannot partially apply. Another failure is no provenance, making it impossible to know which process version a project started from.

## Falsification

Reject if instantiation can copy actual completion/history fields; if role placeholders resolve to nonexistent users without blocking disclosure; if dependency links reference the source template after creation; if template updates silently change existing project scope; if users cannot preview item count and schedule shift; or if a regulated project lacks template-version provenance.

## Output contract

Return a `project-templates-contract` with: reusable entity scope; parameter schema; relative-date model; role resolution; excluded historical fields; instantiation preview; optional sections; dependency remapping; template versioning; instance independence; and migration/diff policy. Include one unresolved-role and one template-update scenario.

## Handoffs

Use task hierarchy/dependencies for instantiated structure, scheduling owners for date calculations, project closure for template-independent lifecycle, and bulk edit only after an instance exists. Templates must not become a backdoor for silent mass mutation.