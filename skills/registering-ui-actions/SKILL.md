---
name: registering-ui-actions
description: Use when capabilities must be translated into exact commands a human or system can invoke, especially across multiple surfaces, modalities, roles, or asynchronous states.
---

# Registering UI Actions

## Parent Contract
**Required parent:** `designing-interactions`.

Receive the interaction contract and, for product-wide work, the canonical capability ledger. Preserve product meaning and authority. This skill defines action identity and obligations; it does not decide visual hierarchy or final control styling.

## Decision Boundary
This faculty owns **canonical action semantics**. An action is an executable intent with a defined initiator, target, preconditions, authority, side effects, success condition, failure behavior, and recoverability. Examples include `member.invite`, `document.rename`, `version.restore`, `invoice.download`, `selection.delete`, `search.clear`, and `dialog.dismiss`.

Do not confuse actions with controls. The same action may be bound to a toolbar button, context menu, keyboard shortcut, command palette, swipe gesture, voice command, or automation. Conversely, one visual button must not secretly mean different semantic actions in different states without explicit modeling. This separation lets NUI detect ghost buttons, missing bindings, duplicate semantics, inaccessible modality-only commands, and drift between labels and behavior.

## Product Truth
Generated interfaces commonly use surface labels as if they were the product model. “Save,” “Apply,” “Done,” and “Submit” get scattered across dialogs, while the underlying behavior is unspecified. Later, implementation invents different side effects for each occurrence. Or the opposite happens: a capability exists in the product model, but no executable action is registered, so no control can ever legitimately bind to it.

Canonical action identity prevents these failures. It also makes alternate interaction modes possible: keyboard and screen-reader behavior can invoke the same semantic action without duplicating business meaning. Action identity is therefore an accessibility, testing, analytics, undo, permission, and product-completeness primitive—not merely naming hygiene.

## Decision Model
1. **Derive actions from capabilities and flows.** For each interactive capability, enumerate the smallest meaningful commands needed to achieve, cancel, reverse, retry, inspect, or recover it. Avoid implementation verbs such as `POST` or `setState`.
2. **Assign a canonical ID.** Use domain/object + verb when possible. The ID survives label changes and visual relocation. A command palette entry and a row action that both restore a version should share one action ID.
3. **Specify initiator and authority.** Record human role, system, collaborator, or external service initiator. State permission checks and what the UI communicates when authority is absent or changes mid-flow.
4. **Specify preconditions.** State required selection, connectivity, data state, validation state, ownership, plan entitlement, or confirmation. A disabled control must map to a known unsatisfied precondition, not arbitrary visual dimming.
5. **Specify effect and observability.** Define the user-observable success effect, not just internal mutation. If a rename succeeds, where and when does the new name appear? If export starts asynchronously, what progress or completion signal exists?
6. **Model consequence class.** Label reversible, destructive, transactional, security-sensitive, privacy-sensitive, navigation-only, local-view, or asynchronous. Consequence drives confirmation, undo, idempotency, duplicate-submit protection, and evidence obligations.
7. **Define interruption semantics.** State whether the action can be canceled, interrupted, repeated, queued, retried, or superseded. For long-running operations, distinguish canceling the UI view from canceling the operation itself.
8. **Define failure and recovery.** Every destructive, permission-bound, transactional, and asynchronous action needs an explicit recovery path or a justified irrecoverable boundary. “Show toast” is not recovery when user work can be lost.
9. **Declare binding obligation.** Specify which modalities are required: pointer/touch, keyboard, remote, voice, pen, assistive technology, context menu, command palette, or system automation. Required actions cannot depend solely on a gesture with no discoverable alternative.
10. **Audit collisions and aliases.** Same label + same context + different semantic action is a collision. Different labels + same semantic action may be acceptable aliases, but should converge on the canonical ID.

## Evidence
Bind action claims to product requirements, existing code, accepted interaction designs, permission models, and runtime behavior. Existing analytics event names can expose actions but are not automatically canonical: analytics often conflates UI location with semantic intent. Source handlers can reveal side effects; tests can reveal retry/idempotency behavior; platform conventions can inform invocation, but none may rewrite product authority.

When external component libraries are introduced, their callbacks and event names must map into the registry rather than becoming a second action ontology. `onSelect`, `onOpenChange`, or `onValueChange` are implementation events; NUI still records the product action they represent.

## Output Contract
Return `action-registry` with:
- `actions[] {id, capability_id, initiators, target, preconditions, authority, effect, consequence, async_semantics, interruption, success_observable, failure_modes, recovery, required_modalities, analytics_semantics}`
- `aliases[] {surface_label, context, canonical_action_id}`
- `binding_requirements[] {action_id, minimum_bindings, alternate_modality_requirement}`
- `collisions[] {surface, label, action_ids, resolution}`
- `unresolved_actions[]`

Every required interactive capability must map to at least one action unless it is explicitly system-only. Later bindings reference action IDs; they may not invent new product actions ad hoc.

## Failure Traps
- Treating button text as the canonical action ID.
- Registering `open-modal` when the real product action is `member.invite`; presentation mechanics should not replace intent.
- Creating separate semantic actions for keyboard and pointer activation of the same outcome.
- Forgetting cancel, retry, undo, dismiss, or permission-request actions because they are “secondary.”
- Modeling destructive action recovery as a decorative toast with no restoration mechanism.
- Allowing a rich interactive library to introduce drag-only behavior without a keyboard/touch alternative tied to the same action.
- Mapping one label to two different consequences on the same surface without disambiguation.
- Assuming disabled controls explain themselves; preconditions and recovery must be communicated.
- Letting optimistic UI imply success before a transactional action has a durable success observable.

**Hard gate:** a required capability with no canonical action, or a required action with no binding obligation, remains functionally open.

## V6 Canonical Action Registry Protocol
Assign **canonical action identity** independent of button label/location so the same product action can appear across menus, shortcuts, touch, voice, automation, and generated UI. Classify an **action side-effect class**: local/reversible, remote reversible, external side effect, destructive/irreversible, permission/security change, financial/high-risk.

Define an **action precondition contract** for required object state, permission, connectivity, selection, validation, and freshness. Require an **idempotency declaration** for retryable or remotely executed actions. Maintain an **action deprecation path** when capabilities change so old shortcuts/links/agent tools fail safely instead of invoking a new semantic meaning.

### Falsification
Trigger the same action through multiple surfaces, retry under latency, and invoke it from a stale/deprecated route. Any consequence mismatch falsifies registry integrity.

### Recovery
Centralize the action contract, add precondition/idempotency handling, migrate all surfaces, and disable ambiguous deprecated bindings.
