# External UI Generation Enforcement v12.1 — Design

Date: 2026-08-22

## Goal

Turn the V12 External UI Intelligence Network from a persistent reference policy into a hard generation-time execution contract. Material UI generation must prove that external implementation intelligence was evaluated before design, carried into implementation selection, rechecked during critique/runtime verification, and accounted for at completion.

## Core invariant

For every material UI task, the agent must emit exactly one reference posture:

- `ACTIVE`: one or more task-shaped V12 reference packs are resolved and bound to the task;
- `EVALUATED_NO_MATCH`: V12 routing was evaluated and no pack materially applies, with an explicit reason.

Silence is invalid. `NOT_EVALUATED`, missing contracts, dropped pack IDs, or missing required lifecycle checkpoints block progression.

## Architecture

1. `src/nolane_ui/external_ui_execution.py` owns deterministic task-to-pack inference, generation-contract compilation, lifecycle checkpoint validation and completion closure.
2. `knowledge/external-ui-generation-routing-v12.json` maps observable task/profile signals to reference-pack IDs. It is routing evidence, not authority and not a popularity table.
3. The V7 concrete design packet accepts an optional V12 reference-execution contract. When the task is marked material and the contract is missing or invalid, the packet cannot be `READY`.
4. `skills/nolane-ui/SKILL.md`, `skills/gating-ui-completion/SKILL.md`, `skills/using-nolane-ui/SKILL.md`, and `AGENTS.md` carry the same hard invariant so host adapters cannot silently omit it.

## Lifecycle requirements

The reference execution contract carries the V12 stages:

`intent → design → implementation-selection → license-gate → critique → runtime-verification → provenance`

Minimum checkpoint closure by NUI phase:

- `ROUTED/DISCOVERED`: `intent`
- `DESIGN_SELECTED/SYSTEMIZED/SPECIFIED`: `intent`, `design`
- `IMPLEMENTABLE/RENDERED`: plus `implementation-selection`, `license-gate`
- `CRITIQUED`: plus `critique`
- `VERIFIED`: plus `runtime-verification`
- `RELEASED`: all stages including `provenance`

A later checkpoint cannot compensate for an earlier missing one.

## Generation binding

The generation contract contains a stable task fingerprint, required pack IDs, resolved pack packets, active source IDs, adoption candidates, GREEN alternatives, consent requirements, unresolved live-verification obligations, and stage checkpoint state. The agent must preserve this compact contract in the design/generation context. Context pressure may shorten descriptions but may not remove IDs, license state, mechanisms, fallbacks, or outstanding checks.

## License behavior

V12.1 preserves permissive-first behavior. Restrictive/reference-only/unverified sources can remain in the research packet without triggering consent. Consent is triggered only by a selected direct-adoption candidate with restrictive/mixed/custom obligations. If a sufficient GREEN candidate exists, it remains the default adoption path.

## Completion gate

A material UI completion claim is blocked when:

- reference evaluation is absent;
- an inferred required pack is missing;
- the contract fingerprint does not match the task profile;
- a required checkpoint for the current phase is absent;
- active pack/source IDs disappear between checkpoints;
- a restrictive adoption candidate lacks explicit consent evidence;
- live verification or provenance obligations remain open at `VERIFIED/RELEASED`.

## Falsification

Mutation tests remove the V12 contract, delete one required pack, drop one checkpoint, change the bound task profile, or remove a previously active source. Each mutation must convert an otherwise valid generation/completion path into `BLOCKED`/invalid. These structural tests prove enforcement mechanics, not model-independent UI quality improvement.
