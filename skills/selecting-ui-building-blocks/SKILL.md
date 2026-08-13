---
name: selecting-ui-building-blocks
description: Use when ecosystem research produced candidate libraries, components, primitives, engines, editors, SDKs, or implementation patterns and the agent must make an evidence-bound adopt, adapt, inspire, build, or reject decision.
---

# Selecting UI Building Blocks

## Parent Contract
**Required parent:** `researching-ui-implementation-ecosystems`.

Receive a typed candidate set with source roles, inspected evidence, product capability requirements, stack/platform truth, local design-system constraints, accessibility obligations, license posture, runtime risks and adoption intent. Do not select from an uninspected link dump.

## Decision Boundary
This faculty owns the **make/buy/adapt/inspire decision at UI-building-block granularity**. It chooses whether a candidate should supply implementation, supply a mechanism only, be wrapped behind a local boundary, be rejected, or be replaced by a local implementation. It does not perform detailed visual/semantic adaptation and it cannot certify integration after implementation.

A decision is not “React Bits is good” or “Radix is accessible.” A decision binds one source to one need under one context. The same project may adapt a React Bits text effect, adopt a Radix dialog primitive, use Motion as an engine, inspire from a GSAP example, build a local button, and reject a heavy editor SDK. Selection is per capability and must preserve this granularity.

## Product Truth
External UI code creates leverage and debt simultaneously. Reuse can provide years of interaction refinement, accessibility engineering, motion knowledge, browser fixes and ecosystem testing. It can also introduce foreign visual language, duplicate runtimes, bundle weight, hydration assumptions, hard-to-debug abstractions, license obligations, security surface and lock-in. AI agents systematically overvalue the visible benefit because a demo is immediate while integration cost appears later.

Selection must therefore compare **total product fit**, not visual excitement. A plain headless primitive may be the best foundation for a critical dialog while a spectacular animated card may be useful only as inspiration. Conversely, rebuilding a complex combobox, editor, collision engine or timeline system from scratch may be wasteful and less accessible than adopting a mature abstraction.

## Decision Model
1. **State the capability and consequence.** Name exactly what the source would own. Classify whether failure would be decorative, task-blocking, destructive, accessibility-critical, performance-critical or architecture-critical.
2. **Validate source-role fit.** A gallery provides reusable visual mechanisms; a headless primitive provides semantics/interaction; a motion engine provides temporal mechanics; an editor or canvas SDK may own a major application subsystem. Reject candidates whose abstraction role cannot satisfy the obligation.
3. **Compare `adopt`, `adapt`, `inspire`, `build`, `reject`.** For each serious candidate, describe the smallest viable commitment. `Adopt` retains most upstream abstraction. `Adapt` reuses implementation while reconciling local contracts. `Inspire` transfers a mechanism without material code dependency. `Build` implements locally. `Reject` records why the source is unsuitable.
4. **Check stack and lifecycle compatibility.** Verify framework version, rendering environment, SSR/hydration assumptions, mobile/native constraints, browser support and release drift. A source can be excellent and still be wrong for the current stack.
5. **Check license before material reuse.** `adopt` and `adapt` require current primary license/terms evidence and a compatible intended use. Do not infer rights from “public repository,” “free,” “open source,” README marketing or a model's memory. Distinguish application use from redistribution and development from production where terms do.
6. **Evaluate accessibility and interaction ownership.** Ask which semantics the upstream source really owns and what composition can invalidate them. A visual gallery should not displace a stronger primitive for dialog/focus behavior. Upstream accessibility is evidence about the upstream implementation, not proof of local wrapping.
7. **Evaluate dependency leverage.** Count new runtimes, transitive dependencies, global CSS or portals, provider requirements, client boundaries, package size and conceptual API surface. Prefer an already-adopted local engine when the experiential result is equivalent.
8. **Evaluate design-system fit.** Determine how much of the source surface identity must be removed. If adaptation would fight every token, state, radius, spacing rule and content pattern, the source may be a poor choice even if technically compatible.
9. **Evaluate exit strategy.** For deep dependencies, define the boundary that lets the product replace or upgrade the source. An editor/canvas/data-grid dependency deserves more architectural isolation than a decorative effect.
10. **Make the decision falsifiable.** State conditions that would reverse the selection: license change, unacceptable bundle delta, accessibility regression, API instability, inability to meet reduced motion, or excessive local overrides.

## Evidence
A strong selection cites the research ledger, primary license evidence for material reuse, inspected implementation paths, release/version evidence where relevant, and local product constraints. For complex choices, a small spike can be evidence: render the candidate inside the actual shell, test focus and keyboard paths, measure bundle/performance, or prove SSR compatibility.

Do not use star count as a proxy for maintainability, visual quality as a proxy for semantics, or upstream test claims as a proxy for local behavior. Evidence quality should increase with dependency depth. A copied CSS shimmer needs less architectural evidence than an infinite-canvas SDK that becomes the application's core interaction model.

## Output Contract
Return `ui-source-selection` with:
- `capability_id`
- `decision: adopt|adapt|inspire|build|reject`
- `source_id` and `canonical_citations[]` when external
- `source_role_fit`
- `inspected[] {kind, location, evidence}`
- `license {posture, evidence_ref, intended_use, redistribution_implications}`
- `stack_fit`
- `accessibility_fit`
- `dependency_delta`
- `design_system_reconciliation_cost`
- `performance_and_rendering_risks[]`
- `exit_strategy`
- `alternatives_considered[]`
- `reversal_conditions[]`
- `handoff {adaptation_required, integration_audit_required, runtime_proof_required}`

For `adopt` or `adapt`, license posture must be verified-compatible and README, license and representative implementation must have been inspected.

## Failure Traps
- “Use it because it has 40k stars.”
- Choosing the first source named by the user without comparison.
- Treating a permissive source-code license as proof every asset, font, trademark or hosted service has the same terms.
- Copying a component gallery's dialog because it looks better than the project's semantic primitive.
- Adding a second motion runtime for one decorative effect when the existing runtime can express it.
- Selecting a core SDK without an adapter boundary or acknowledged lock-in.
- Assuming a framework-agnostic visual idea implies framework-compatible source code.
- Rejecting all dependencies reflexively and rebuilding difficult accessibility behavior poorly.
- Selecting a full design system when only one headless primitive is needed.
- Selecting a primitive without budgeting the design work needed to make it locally coherent.
- Treating “MIT” as a substitute for reading the current license file and intended-use details.
- Declaring integration successful here; that belongs to downstream audit and runtime verification.

**Hard gate:** popularity, screenshots or remembered reputation cannot authorize material reuse; `adopt` and `adapt` require current license evidence, implementation inspection, role fit and an explicit integration/exit contract.

## V6 Building-Block Selection Protocol
Use an **adopt-adapt-inspire-build matrix** per capability, not per repository. Score **integration-lockin cost** across API/data model, DOM/semantics, styling/tokens, state ownership, bundle/runtime, migration, and maintenance.

Evaluate **semantic fit score** before visual fit: role/action/state/input/accessibility must match product contracts. Require a **replacement strategy** for material third-party building blocks, even if “replace by local implementation later.” Set a **source-combination ceiling** based on semantic/style/runtime conflict risk so a UI does not become a collage of unrelated libraries.

### Falsification
Strip source styles and compare candidate behavior against a local/native alternative; simulate replacement/update. If value is mostly trade dress or lock-in dominates, selection is wrong.

### Recovery
Choose a different adoption mode, wrap/narrow the source, build locally, or reject the candidate and preserve only transferable mechanisms.
