---
name: designing-popover-systems
description: Use when a nonmodal anchored surface contains richer information or controls and the design must define focus, dismissal, layering, anchor lifetime and nested-surface behavior without accidentally creating a modal dialog.
---

# Designing Popover Systems

## Parent Contract
**Required parent:** `engineering-rich-interactive-components`.

This faculty owns nonmodal anchored surface behavior. Presentation motion is delegated to `designing-popover-origin-motion`; menu, tooltip and modal-dialog semantics remain separate.

## Decision Model
Define why the surface is anchored. Common roles include quick property editing, small inspectors, contextual details, date/color controls or secondary actions too rich for a menu. If the task must block the rest of the application or contains a long sequential workflow, a dialog or panel is more appropriate.

Specify focus policy from content. A purely informational popover may leave focus on the invoker; an interactive popover may transfer focus into its first meaningful control. Closing should restore focus when appropriate without yanking focus from a destination the user intentionally moved to.

Dismissal is multi-causal: explicit close, Escape, outside interaction, action completion, anchor destruction, route change. Outside-click rules must distinguish interactions inside nested overlays/portals from true outside events. Clicking the anchor can toggle, refocus or reopen depending on component contract, but it must be deterministic.

Layering requires ownership. A popover may open a nested menu, picker or tooltip; global “click outside” handlers must not close the entire stack before the child receives the event. Define overlay ancestry rather than relying on DOM containment alone.

## Failure Topology
- An interactive popover keeps focus on the trigger and keyboard users cannot reach its controls naturally.
- Clicking a nested select is treated as outside and closes the parent.
- Anchor is deleted but an orphaned popover remains at screen coordinates.
- Popover expands into a multi-step workflow with no clear task boundary.
- Escape closes multiple unrelated overlay layers at once.

## Falsification and Recovery
Open nested overlays, portal children, remove/scroll anchor, tab in/out, click outside, press Escape at each depth, change route and test screen reader. The contract fails if overlay ownership or focus restoration depends on incidental DOM nesting.

Recover by modeling overlay ancestry explicitly, choosing one semantic dismissal boundary per event, promoting blocking workflows to dialogs/panels and defining anchor-loss behavior.

## Output Contract
Return `popover-system-contract` with purpose, anchor identity, focus policy, dismissal matrix, overlay ancestry, outside-interaction rules, anchor-loss policy, layering/portal constraints, accessibility semantics and runtime tests.