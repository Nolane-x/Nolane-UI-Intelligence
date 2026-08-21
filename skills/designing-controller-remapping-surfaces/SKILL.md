---
name: designing-controller-remapping-surfaces
description: Use when users can customize controller bindings and the interface must prevent unreachable command sets, expose conflicts and reserved inputs, support multiple devices/layouts, and preserve accessibility and recovery paths after remapping.
---

# Designing Controller Remapping Surfaces

## Remapping changes the command contract
A binding screen is not a list of editable labels. It changes the mapping between physical input and essential product actions, so a bad configuration can make the UI impossible to operate. This skill owns how remapping is captured, validated, previewed, conflicted, restored, and persisted.

## Parent Contract
**Required parent:** `routing-ui-work`.

The routing parent selects this specialist when user-configurable controller input is material. Default navigation semantics, focus adjacency, and prompt switching remain separate owners.

## Binding model
Represent bindings by semantic action, input device/profile, physical control, activation type (press, hold, chord, axis direction), context, and precedence. The decision owner is validity: whether a proposed map preserves every mandatory action and respects platform-reserved or safety-critical controls.

Some actions may share a button because they live in mutually exclusive contexts; others conflict even if the settings UI sees different labels. Conflict detection must use runtime command contexts, not just raw button equality. For axes, include dead-zone direction and threshold semantics where those affect collisions.

## Capture interaction
During rebinding, enter a dedicated capture state that distinguishes the input being assigned from navigation commands used to escape capture. Protect at least one reliable cancel/reset path. Filter accidental stick drift or trigger noise before committing a binding. If the user attempts to bind a reserved system control, explain the platform constraint rather than silently ignoring it.

## Validation and recovery
Before saving, prove that essential actions remain reachable: select/confirm, back/cancel, pause/menu where required, and any accessibility or emergency command mandated by the product. If the user creates a risky map, support timed confirmation or a guaranteed reset gesture. Store a known-good profile so corrupted settings do not require external deletion of configuration files.

## Multiple devices and players
Bindings may be global, per-device, per-player, or per-profile. Make scope visible. Swapping from one controller family to another may require a separate physical map even when semantic actions are shared. Prompt glyphs should derive from the active mapping, not from defaults.

## Evidence
Evidence includes original and proposed maps, detected conflicts, mandatory-action reachability, capture traces, reserved-input handling, persistence/reload, device/profile scope, and reset recovery. Test duplicate assignments, noisy axes, missing essential actions, controller-family changes, and corrupted stored mappings.

## Failure modes
Characteristic Failure includes allowing the user to unbind Back with no reset path, detecting conflicts only by button name, input capture that binds stick drift, prompts that ignore custom bindings, per-player maps leaking across accounts, and settings that persist an invalid partial update after a crash. Another failure is conflict auto-resolution that silently unbinds a different critical action.

## Falsification
Try to remove every essential command, create context-overlapping conflicts, bind reserved controls, disconnect during capture, and reload after a partially written map. The contract fails if the resulting UI can become unreachable, if conflicts are hidden, if recovery depends on an unbound action, or if the active prompts disagree with the committed map.

## Recovery
Keep a known-good map and apply changes transactionally. If validation fails, do not partially commit. If a loaded map is corrupt or incompatible with a new device, enter a safe default/recovery profile and let the user inspect what could not be preserved. Never require the broken mapping to navigate the repair flow.

## Output and Handoff
Output: `controller-remapping-surfaces-contract`, containing binding schema, conflict semantics, capture mode, mandatory reachability, persistence, scope, reset path, and evidence. Handoff prompt rendering to input-device prompt switching and directional traversal to directional focus graphs.

## Sibling Boundary and delete-the-skill
Sibling prompt switching reflects the current mapping but does not validate it. Remote-control navigation defines default sparse-device commands. The delete-the-skill test passes because without a remapping owner, customization can create inaccessible or ambiguous control sets that ordinary input handling cannot safely recover from.