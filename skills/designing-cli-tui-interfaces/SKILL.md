---
name: designing-cli-tui-interfaces
description: Use when designing command-line or terminal interfaces, interactive TUIs, developer tools, operations consoles, scripts, or text-first workflows where grammar, discoverability, composability, keyboard flow, and safe destructive actions matter.
---

# Designing CLI and TUI Interfaces

## Overview
Text interfaces are UI. Their affordances are command grammar, help, completion, output structure, exit status, focus/key maps, reversibility, and the ability to understand consequences before an operation changes state.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require target user expertise, shell/platform, interactive versus scriptable use, command frequency, destructive capability, output consumers (human versus machine), accessibility needs, and network/background behavior.

## Decision Model
For CLI, design a coherent grammar: noun/verb structure, flags, defaults, required arguments, aliases, stdin/stdout/stderr behavior, exit codes, and idempotency. Commands performing similar actions should share vocabulary and option semantics. Prefer explicit safe defaults; reserve terse aliases for common expert paths without hiding the canonical form.

Discoverability includes `--help`, contextual examples, completion, error suggestions, and command previews. Errors name what was invalid and how to recover without dumping implementation internals. Output intended for scripts needs stable structured modes distinct from decorative human formatting.

Destructive or production actions need scope visibility, dry-run/preview where feasible, target/environment differentiation, and recoverability. Interactive confirmation must not break automation unexpectedly; use explicit flags or policies. Secrets never echo casually into command history or logs.

For TUI, define focus/navigation, key map, resize behavior, screen-reader/terminal semantics where available, color fallback, mouse optionality, and what happens in narrow terminals. Preserve selection and scroll under live updates. Every modal layer needs a visible escape key.

## Evidence
Test common and dangerous commands, malformed inputs, shell quoting, small/large terminal sizes, no-color mode, redirected output, automation mode, keyboard-only navigation, slow network, interruption/cancel, and terminal capability differences. Inspect real error and help output rather than README promises.

## Output Contract
Return a `terminal-ui-contract` with `command_grammar`, `canonical_commands[]`, `flag_policy`, `safe_defaults`, `help_and_completion`, `error_contract`, `human_vs_machine_output`, `destructive_action_policy`, `secret_handling`, `tui_navigation`, `resize_and_color_fallback`, and `terminal_tests[]`.

## Failure Traps
- Cryptic one-letter flags as the only documented interface.
- Destructive command defaulting to production scope.
- Confirmation prompt hanging CI scripts.
- Parsing decorative human output in automation.
- Error stack trace with no recovery instruction.
- TUI that assumes 120-column color terminal.
- Live updates constantly moving the user’s selection.

A strong terminal UI is learnable interactively and dependable when automated.