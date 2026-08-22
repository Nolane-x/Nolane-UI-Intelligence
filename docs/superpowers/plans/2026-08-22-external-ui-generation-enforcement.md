# External UI Generation Enforcement v12.1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make V12 external UI reference intelligence a hard, deterministic prerequisite for material UI generation and completion.

**Architecture:** Add a focused execution module that infers relevant V12 packs from task-profile signals, compiles a stable generation contract, validates lifecycle checkpoints, and blocks completion when the contract is absent or dropped. Integrate the contract into the existing concrete design packet and canonical NUI lifecycle/completion skills rather than creating a parallel lifecycle.

**Tech Stack:** Python 3.12, JSON knowledge artifacts, unittest, existing NUI skill/runtime contracts.

**Spec:** `docs/superpowers/specs/2026-08-22-external-ui-generation-enforcement-design.md`

## Global Constraints

- Material UI generation must explicitly evaluate V12 reference routing; silence is invalid.
- Preserve permissive-first selection and exact-scope license re-verification.
- Do not vendor third-party code/assets/prose or promote popularity into authority.
- Context compression may not erase active source IDs, license state, mechanisms, fallbacks, or open verification obligations.
- Structural enforcement evidence must not be marketed as proof of model-independent aesthetic superiority.

---

### Task 1: Generation execution contract

**Files:**
- Create: `knowledge/external-ui-generation-routing-v12.json`
- Create: `src/nolane_ui/external_ui_execution.py`
- Create: `tests/test_external_ui_execution_v12.py`

**Interfaces:**
- Produces: `infer_reference_pack_ids(profile, routing) -> list[str]`
- Produces: `compile_reference_execution_contract(profile, network, packs, routing, stack=None) -> dict`
- Produces: `validate_reference_execution_contract(contract, profile, routing) -> dict`
- Produces: `validate_reference_stage_checkpoint(contract, checkpoint) -> dict`
- Produces: `validate_reference_completion(contract, phase) -> dict`

- [ ] Write tests that fail when generation routing is unevaluated, a required pack is omitted, the task fingerprint drifts, a lifecycle checkpoint is missing, or active source IDs disappear.
- [ ] Verify the tests fail before implementation.
- [ ] Implement deterministic pack inference and contract compilation using existing `resolve_reference_pack`.
- [ ] Implement checkpoint and phase-completion validators.
- [ ] Run the focused V12.1 tests until green.

### Task 2: Concrete generation gate

**Files:**
- Modify: `src/nolane_ui/concrete.py`
- Modify: `tests/test_concrete_v7.py`

**Interfaces:**
- Extend `compile_concrete_design_packet(..., reference_execution_contract: dict | None = None)` without breaking existing callers.
- When `profile.material_ui` is true, missing/invalid V12 reference execution prevents `READY` and adds an unresolved blocker.

- [ ] Add failing tests for material UI generation with no reference contract and for a valid `EVALUATED_NO_MATCH` contract.
- [ ] Implement the optional integration without weakening historical V7 packet behavior.
- [ ] Run concrete packet tests and V12.1 tests.

### Task 3: Lifecycle and completion hard policy

**Files:**
- Modify: `skills/using-nolane-ui/SKILL.md`
- Modify: `skills/nolane-ui/SKILL.md`
- Modify: `skills/gating-ui-completion/SKILL.md`
- Modify: `AGENTS.md`

**Interfaces:**
- Bootstrap emits/retains `reference_execution_ref` for every material UI task.
- Lifecycle transition rules map phases to required V12 checkpoints.
- Completion packet requires `reference_execution` and blocks silent omission/dropout.

- [ ] Add V12.1 generation-time and completion-time hard rules.
- [ ] Explicitly prohibit treating a restrictive research fallback as a consent trigger.
- [ ] Add falsification/recovery instructions for context dropout.

### Task 4: Verification and integration

**Files:**
- Update: PR #23 metadata/body if needed.

- [ ] Run PR CI on the exact final head: real Chromium smoke, full unittest discovery, completion packet, `nui-validate`, packaging.
- [ ] Review the diff for duplicated architecture, accidental third-party content, overclaims, and backward-compatibility breaks.
- [ ] Keep PR draft until final verification succeeds; then mark ready for review. Do not merge without the user's integration decision.
