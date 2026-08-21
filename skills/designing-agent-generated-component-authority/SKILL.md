---
name: designing-agent-generated-component-authority
description: Use when an agent can generate interactive UI components and the product must decide which generated controls are allowed to display data, mutate state, request approval, or trigger tools without granting arbitrary generated markup product authority.
---

# Designing Agent Generated-Component Authority

## Generated UI is executable product surface
A generated component is not merely formatted model output once it can contain controls, bind to live data, or initiate actions. This skill owns the authority boundary between generated presentation and product-controlled capability. Its core decision is what a generated component may claim, read, mutate, and trigger based on its declared schema and the host’s trust policy.

## Parent Contract
**Required parent:** `designing-generative-ui`.

The parent defines the generative-UI runtime and how agent-produced interfaces are rendered. This specialist starts where a generated view attempts to become an interactive authority-bearing surface.

## Authority classes
Classify generated components by capability rather than visual complexity. Useful classes include `presentational`, `local-interaction`, `read-bound`, `proposal-producing`, `approval-requesting`, and `action-invoking`. A presentational chart may render trusted tool data but cannot silently gain write capability because it contains a button. An action-invoking component must route through host-owned action registration and authorization.

Generated components should never define their own security semantics. The host owns action IDs, input validation, resource resolution, permission checks, side-effect disclosure, and result binding. Generated code or schema may choose among capabilities explicitly exposed by the host, but it cannot create new ones by naming them.

## Data and claim authority
Separate data provenance from component provenance. A generated card may display authoritative account data while its explanatory text is model-generated. Mark derived fields and predictions accordingly. A component must not present model-inferred status with the same visual authority as server-confirmed status unless the product deliberately defines that semantic distinction.

Input fields also need ownership rules. Local form state may be generated, but submission should be converted into a host-validated action request. Sensitive values should not be exposed to generated component code unless its execution boundary is designed for that data class.

## Interaction gates
Every control maps to an allowed capability and current state. Disable or remove controls whose authority is absent, expired, or incompatible with the current data revision. Approval UI itself should be host-owned or constrained by a trusted schema so a generated component cannot misrepresent what the user is authorizing.

## Evidence
Evidence includes the generated schema or component revision, capability manifest, data-source bindings, action mappings, host validation decisions, approval handoffs, and runtime events. Test evidence should prove that a malicious or malformed generated component cannot invoke unregistered actions, escalate scope, forge success state, or conceal the authoritative result.

## Failure modes
Characteristic Failure includes generated buttons calling arbitrary tool names, inferred data rendered as server truth, host actions triggered with unvalidated resource IDs, a generated confirmation dialog that omits material side effects, and stale generated controls remaining active after capability revocation. Another failure is visual authority leakage: generated UI mimics trusted system warnings or verified badges without possessing that authority.

## Falsification
Feed a generated schema with an unknown action, altered action parameters, forged success status, a stale resource revision, and a request to render privileged data. The contract fails if the host executes an undeclared capability, if generated state overrides runtime truth, if sensitive data crosses an unauthorized boundary, or if the user cannot distinguish generated claims from authoritative facts.

## Recovery
On authority violation or schema uncertainty, downgrade the component to safe presentation, preserve raw trusted evidence, and block interactive actions until the host can validate them. If an unauthorized action already executed, record it in the side-effect ledger and route to authority-violation recovery. Do not let a rendering failure erase the underlying tool result.

## Output and Handoff
Output: `agent-generated-component-authority-contract`, containing capability classes, host-owned action registry, data/claim provenance rules, validation gates, trust presentation, and downgrade behavior. Handoff malformed representation to generative-ui schema fallbacks and execution state to tool-call lifecycles.

## Sibling Boundary and delete-the-skill
Sibling tool-result presentation owns how results evolve from raw to structured views, not what generated controls may do. Schema fallback owns graceful degradation when a component cannot render. This skill owns authority. The delete-the-skill test passes because without it, generative UI turns model-produced structure into an implicit capability system and allows presentation code to acquire product powers accidentally.