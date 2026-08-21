---
name: designing-story-state-fixture-coverage
description: Use when isolated component stories or fixtures are used as verification inputs and the team must ensure they represent reachable semantic states, stable data boundaries, interaction preconditions, and high-risk variants rather than a decorative component gallery.
---

# Designing Story-State Fixture Coverage

## Fixtures are executable evidence inputs
A story, fixture, or isolated component example becomes part of the verification system when screenshots, interaction tests, accessibility checks, or documentation depend on it. This skill owns which fixtures exist and whether they faithfully instantiate the component contract. Its core decision is whether a fixture adds a materially distinct state or merely duplicates visual variation.

## Parent Contract
**Required parent:** `binding-ui-evidence`.

The parent binds claims to evidence. This specialist begins before evidence capture, at the point where deterministic component states must be constructed and maintained.

## Fixture anatomy
Each fixture should declare component revision, state predicate, data shape, permissions, async conditions, locale/theme assumptions, and any surrounding provider context required to make the state real. Avoid fixtures that reach a state through private implementation flags unavailable to production unless the purpose is explicitly internal unit testing.

A robust set includes baseline states plus risky boundaries: empty and dense data, validation errors, loading with existing content, permission denial, long text, destructive confirmation, selected/expanded combinations that change interaction, and any state tied to critical accessibility semantics. The decision owner is semantic novelty, not fixture count.

## Reachability and determinism
A fixture should either be reachable through the real state model or document why a direct state injection is equivalent. Determinism matters: random IDs, current time, live network, animation clocks, and nondeterministic content can contaminate evidence. Freeze only what is irrelevant to the claim; do not freeze away behavior the component is supposed to handle.

Fixtures should be composable with interaction tests. If a story starts in a state no user can ever enter, the resulting test may create false confidence. Conversely, some rare failure states are hard to reproduce end-to-end and deserve a controlled fixture when their semantics are still valid.

## Coverage ledger
Map fixtures to state-matrix cells and evidence consumers. Record whether a fixture is required for visual, interaction, accessibility, responsive, or documentation evidence. Orphan fixtures with no claim may be kept for exploration but should not count toward verification coverage.

## Evidence
Evidence of fixture quality includes state predicates, provider configuration, deterministic seed/data, reachability rationale, links to component state contracts, and evidence runs consuming the fixture. Review changes to fixture data because a “harmless” fixture edit can weaken a test without touching production code.

## Failure modes
Characteristic Failure includes happy-path story galleries, dozens of color/size variants with no behavioral states, fixtures that bypass real permission or validation logic, live API dependence that makes baselines flaky, and stale stories that render states the component no longer supports. Another failure is fixture laundering: changing fixture input until a regression disappears rather than fixing the product.

## Falsification
Remove a high-risk state, alter fixture data so an overflow boundary disappears, bypass a real transition with an impossible prop combination, or inject nondeterministic time. The contract fails if coverage still reports complete, if evidence consumers cannot state which fixture revision they used, or if a fixture can materially weaken a test without review.

## Recovery
Reconstruct fixtures from the current component state model, map them to admitted evidence cells, delete or demote redundant decorative cases, and reintroduce risky boundaries. When a fixture must use direct injection, document the production-equivalence rationale. Recapture dependent evidence whenever fixture semantics change.

## Output and Handoff
Output: `story-state-fixture-coverage-contract`, containing fixture inventory, semantic state mapping, reachability, determinism controls, evidence consumers, and freshness. Handoff state-space admission to component-state evidence matrices and screenshot governance to visual-regression baselines.

## Sibling Boundary and delete-the-skill
Sibling component-state matrices define what must be covered; this skill defines the deterministic story/fixture artifacts that instantiate those cells. Consumer regression tests validate integration beyond isolation. The delete-the-skill test passes because without fixture governance, verification can become reproducible but semantically hollow—testing stable examples that no longer represent the product’s dangerous states.