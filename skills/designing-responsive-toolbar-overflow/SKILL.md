---
name: designing-responsive-toolbar-overflow
description: Use when a command toolbar cannot fit its available width and commands must migrate into overflow without losing priority, current state, discoverability, grouping, or operation context.
---

# Designing Responsive Toolbar Overflow

## Command Scarcity
A toolbar under width pressure must decide which commands stay visible and which move into overflow. This skill owns that migration based on command priority and state, not arbitrary DOM order or icon width.

## Parent Contract
**Required parent:** `adapting-responsive-layouts`.

The parent supplies responsive composition authority. Command semantics and permission policy remain with their existing owners; this skill governs spatial overflow behavior.

## Command Inventory
For each command capture task frequency, consequence, reversibility, current active/toggled state, selection dependency, grouping, and whether visibility itself communicates status. Persistent primary actions and stateful mode controls may need to remain visible even when less frequently used than simple commands.

Define overflow order and group preservation. A command moved into a menu must retain label, disabled reason, shortcut if relevant, checked/active state, and outcome. Do not turn mutually related controls into unrelated menu items if that destroys comprehension.

## Evidence
Evidence includes width sweeps, long labels, permission variants, selection-dependent enablement, active/toggled states, and keyboard operation of both inline and overflow forms. Track the same command identity across presentations so analytics and side effects do not fork.

## Failure Modes
Failure includes primary save/apply actions disappearing behind “More,” active formatting modes hidden with no visible cue, command groups split unpredictably, disabled reasons lost in overflow, duplicate commands rendered both inline and in the menu, and focus reset when commands migrate.

## Falsification
Falsification narrows the toolbar while a command is active, while focus is on the next-to-overflow item, and while permissions hide neighboring actions. The contract fails if command identity/state changes, a required action becomes undiscoverable, or overflow order depends on transient measurement noise.

## Recovery
Recovery restores explicit priority/group rules, preserves one command identity with alternate rendering, and uses stable measurement thresholds with hysteresis if necessary. If too many commands are equally primary, revisit task architecture rather than creating an enormous overflow menu.

## Output
Output: `responsive-toolbar-overflow-contract` with priority tiers, grouping, migration rule, state equivalence, focus behavior, and width-pressure evidence.

## Handoff
Handoff navigation destinations to adaptive navigation transitions and semantic sacrifice of whole regions to priority collapse.

## Sibling Boundary and delete-the-skill
Region collapse is coarse-grained; toolbar overflow owns individual command migration and state equivalence. Without it, responsive layout has no decision owner for which command remains visible and what contract survives overflow.