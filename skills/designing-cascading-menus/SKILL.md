---
name: designing-cascading-menus
description: Use when a command hierarchy uses nested submenus and the design must balance discoverability, pointer intent, keyboard traversal, depth limits and safe dismissal across multiple menu levels.
---

# Designing Cascading Menus

## Parent Contract
**Required parent:** `engineering-rich-interactive-components`.

This faculty owns nested menu hierarchy and traversal. It does not own general navigation trees or arbitrary nested popovers.

## Decision Model
Use a cascade only when commands have a stable, meaningful hierarchy that saves space without hiding frequent work. Deep nesting increases motor and memory cost; commands used frequently may deserve a flatter route, shortcut or command palette.

Each item is either an executable command, a stateful command, a separator/group heading, or a submenu trigger. Avoid ambiguous items that both execute and open a submenu unless the platform has a strong convention and the behavior is explicit.

Pointer traversal needs intent tolerance. The user moving diagonally from a parent item into a submenu should not lose it because the pointer briefly crosses outside the parent row. However, intent delays must not make neighboring submenu switching feel sticky. Keyboard arrows should traverse hierarchy deterministically with locale direction accounted for.

Placement must handle viewport edges and scrolling. A submenu that flips direction still belongs to the same logical level; arrow-key semantics should follow reading/platform convention rather than blindly following visual left/right if that would break established behavior.

## Failure Topology
- Five-level cascades hide essential commands behind motor precision tests.
- Pointer corridor logic keeps the wrong submenu open too long.
- A parent item both executes and opens, causing accidental actions.
- Flipped submenus reverse keyboard semantics inconsistently.
- Disabled parent items hide useful explanations or child availability.
- Hover opens submenus but keyboard focus does not expose equivalent hierarchy.

## Falsification and Recovery
Traverse slowly/quickly, move diagonally, switch siblings, use keyboard only, test RTL, edge placement, large text and 3+ levels. Measure whether the intended submenu can be reached without accidental closure and whether escape/back movement returns one logical level at a time.

Recover by flattening hierarchy, promoting frequent commands, tuning intent zones, separating execute vs expand semantics, and using a tree/command surface when depth reflects information rather than commands.

## Output Contract
Return `cascading-menu-contract` with hierarchy rationale, item types, depth policy, pointer-intent model, keyboard traversal, RTL/placement behavior, dismissal/backtracking, disabled states and traversal tests.