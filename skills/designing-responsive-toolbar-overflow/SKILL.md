---
name: designing-responsive-toolbar-overflow
description: Move toolbar commands into responsive overflow while preserving command identity, state, grouping, shortcuts, and discoverability.
---

# Designing responsive toolbar overflow

Toolbars often contain more actions than can remain visible at every width. Use this skill to define a stable overflow strategy rather than allowing buttons to wrap, clip, or vanish unpredictably.

## Decision ownership

Own command priority, overflow ordering, group preservation, representation changes, active-state signaling, and rules for commands that must never overflow. Decide whether labels may become icon-only before commands move into a menu.

## Inputs and evidence

Collect command frequency, consequence, keyboard shortcuts, current enabled/disabled/toggled state, contextual commands, user customization, localization lengths, and narrow-container widths. Identify commands whose visibility is required to communicate state even when rarely invoked.

## Procedure

Assign priority by task importance and state visibility, not frequency alone. Define deterministic movement into overflow and preserve logical groups. When a toggle or mode command moves, show its current state inside the overflow representation. Keep destructive and confirmation-sensitive actions clearly labeled.

Avoid measuring after each render in a way that causes commands to hop between visible and overflow positions. Use stable sizing or reserved boundaries. If labels become icons, require recognizable icons and accessible names; do not use iconification merely to postpone a necessary overflow design.

## Failure topology

Overflow can become a dumping ground where command order changes with every width. Active toggles hidden in overflow make the current mode invisible. Another failure is duplicate command instances whose disabled or selected states desynchronize.

Localization can change which commands overflow, causing frequently used actions to disappear only in some languages.

## Falsification

Resize continuously while invoking commands and changing contextual state. Verify command identity, shortcut, tooltip/name, enabled state, and selection survive movement. Test longest translations and user-customized toolbars. Ensure keyboard focus does not jump to an unrelated command when the focused item overflows.

Audit the overflow menu at several widths for stable grouping and ordering.

## Output contract

Produce a `responsive-toolbar-overflow-contract` defining command priority, grouping, never-overflow items, iconification rules, overflow order, state synchronization, focus behavior, localization handling, and test cases around threshold transitions.

## Handoffs

Use `designing-command-bars-and-toolbars` for base command structure, `designing-responsive-priority-collapse` for priority logic, `designing-icon-label-pairing` for icon-only decisions, and `verifying-responsive-state-parity` for command equivalence.