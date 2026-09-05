"""V13 sixth-wave rules; all operational prose is independently authored."""
from __future__ import annotations

COMMAND_KEYBOARD_RULES_V13 = [{'rule_id': 'ui.commands.shortcut-conflict-resolved-by-context',
  'domain': 'commands',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Keyboard shortcut conflicts must resolve deterministically from active context',
  'statement': 'When the same key sequence is valid in multiple command scopes, dispatch must use the active focus '
               'and application context rather than executing two commands or selecting an arbitrary handler.',
  'intent': 'Keep power-user input predictable as editors, dialogs, panels, and global commands compete for the same '
            'shortcut namespace.',
  'applies_when': ['A keyboard-driven interface has local, modal, editor, global, or plugin command scopes that can '
                   'register overlapping shortcuts.'],
  'does_not_apply_when': [],
  'failure_modes': ['Pressing one shortcut triggers multiple actions or changes behavior unpredictably because '
                    'command priority is not bound to active context.'],
  'user_impacts': ['Users can invoke unintended destructive actions, lose work, or stop trusting keyboard workflows '
                   'because shortcut meaning changes unexpectedly.'],
  'observables': ['Register or activate conflicting commands across nested contexts, move focus between them, and '
                  'log which command handler receives the key sequence.'],
  'falsifiers': ['A documented precedence model selects exactly one applicable command for the active context and '
                 'the result remains stable across rerenders.'],
  'repairs': ['Route shortcuts through a contextual command resolver with explicit scope precedence rather than '
              'independent event listeners competing for the same keys.'],
  'exceptions': [],
  'verification': ['Exercise the same shortcut in global, modal, editor, and focused-control contexts and confirm '
                   'exactly the intended handler executes each time.'],
  'owner_hints': ['designing-keyboard-power-user-ux'],
  'verifier_hints': ['critiquing-input-modality'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-command-keyboard-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.commands.disabled-command-explains-precondition',
  'domain': 'commands',
  'class': 'contextual',
  'severity': 'moderate',
  'enforcement': 'warn',
  'title': 'Unavailable commands must expose the missing precondition when users can reasonably act on it',
  'statement': 'A disabled or omitted command that depends on selection, connection, permission, save state, or '
               'another recoverable precondition should communicate why it is unavailable instead of appearing '
               'arbitrarily inert.',
  'intent': 'Turn command unavailability into actionable state information so users can satisfy the real '
            'precondition rather than guessing.',
  'applies_when': ['A visible command is unavailable because a specific product state or user action can make it '
                   'available again.'],
  'does_not_apply_when': [],
  'failure_modes': ['The command is disabled with no accessible reason even though the product knows the missing '
                    'selection, permission, connection, or state requirement.'],
  'user_impacts': ['Users may repeatedly retry, search documentation, or abandon a task that is blocked by a simple '
                   'recoverable precondition.'],
  'observables': ['Place the interface in each known disabled-command state and inspect visible, accessible, or help '
                  'text for a reason tied to the actual precondition.'],
  'falsifiers': ['The disabled state exposes a truthful precondition or recovery route without inventing a reason '
                 'when the system genuinely does not know.'],
  'repairs': ['Attach availability reasons to command state and surface them through tooltip, description, status '
              'region, or command-palette metadata appropriate to the modality.'],
  'exceptions': [],
  'verification': ['Toggle each precondition and confirm the reason changes or disappears exactly when the command '
                   'becomes executable.'],
  'owner_hints': ['designing-command-palettes'],
  'verifier_hints': ['critiquing-user-experience'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-command-keyboard-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.commands.target-scope-visible-before-execution',
  'domain': 'commands',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Commands that act on a non-obvious target must reveal their execution scope before commit',
  'statement': 'A command affecting the current selection, active document, workspace, remote environment, or '
               'account must expose that target when context could be ambiguous at the moment of execution.',
  'intent': 'Prevent context-sensitive commands from mutating a different resource than the user believes is active.',
  'applies_when': ['The same command can execute against different resources depending on focus, active tab, '
                   'selection, connection, or workspace context.'],
  'does_not_apply_when': [],
  'failure_modes': ['The command executes against a background or stale target because the visible interface does '
                    'not make the active command scope apparent.'],
  'user_impacts': ['Users can modify, delete, publish, run, or export the wrong resource even though the command '
                   'name itself was correct.'],
  'observables': ['Switch active resources while keeping the command surface open, then inspect target indication '
                  'and mutation payload for each execution.'],
  'falsifiers': ['The active target is visible at execution time or the command is safely bound to an unambiguous '
                 'selection that cannot change underneath the user.'],
  'repairs': ['Resolve command scope from authoritative active-context state and display the target for '
              'consequential actions or ambiguous command surfaces.'],
  'exceptions': [],
  'verification': ['Rapidly switch tabs, selections, workspaces, and remote targets before execution and confirm the '
                   'command always affects the shown scope.'],
  'owner_hints': ['designing-command-palettes'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-command-keyboard-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.commands.palette-refreshes-after-context-change',
  'domain': 'commands',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Open command palettes must refresh availability when the underlying context changes',
  'statement': 'A command palette or searchable action menu that stays open while focus, selection, document, '
               'permission, or connection state changes must recompute command availability before execution.',
  'intent': 'Prevent stale command lists from presenting actions that were valid for the previous context but are '
            'unsafe or impossible now.',
  'applies_when': ['A persistent command surface can remain open while context changes through keyboard navigation, '
                   'background updates, or another window.'],
  'does_not_apply_when': [],
  'failure_modes': ['A command remains enabled and executes using stale context after the selection or authority '
                    'that made it valid has changed.'],
  'user_impacts': ['Users can run an action against unintended state or receive confusing failures from a command '
                   'that the interface still presented as available.'],
  'observables': ['Open the palette, change selection or permission without closing it, and compare listed '
                  'availability with a freshly opened palette and actual command result.'],
  'falsifiers': ['The open palette updates or revalidates command state before execution and never relies solely on '
                 'the context captured when it opened.'],
  'repairs': ['Subscribe command-state computation to active-context changes and perform a final availability check '
              'at dispatch.'],
  'exceptions': [],
  'verification': ['Change focus, selection, connectivity, and permission while the palette remains open and verify '
                   'stale actions update before any command can fire.'],
  'owner_hints': ['designing-command-palettes'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-command-keyboard-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.commands.destructive-shortcut-has-recovery-boundary',
  'domain': 'commands',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Destructive keyboard shortcuts must include an appropriate recovery or confirmation boundary',
  'statement': 'A shortcut that can irreversibly delete, discard, publish, revoke, or overwrite consequential state '
               'must not bypass the same recovery safeguards that apply to equivalent pointer or menu actions.',
  'intent': 'Keep keyboard acceleration from becoming a privileged path around product safeguards for '
            'high-consequence actions.',
  'applies_when': ['A keyboard shortcut invokes an action whose normal UI includes undo, confirmation, version '
                   'history, staging, or another deliberate recovery mechanism.'],
  'does_not_apply_when': [],
  'failure_modes': ['The shortcut commits the destructive action immediately while the menu or pointer path requires '
                    'confirmation or provides stronger recovery.'],
  'user_impacts': ['Power users can lose data or trigger consequential side effects because the fastest input path '
                   'silently weakens safety boundaries.'],
  'observables': ['Invoke the same destructive operation through shortcut and non-keyboard surfaces and compare '
                  'confirmation, undo, staging, and persisted outcomes.'],
  'falsifiers': ['The shortcut preserves an equivalent safety or recovery boundary appropriate to the action and '
                 'user expectations.'],
  'repairs': ['Route shortcut dispatch through the canonical command lifecycle rather than calling a lower-level '
              'destructive mutation directly.'],
  'exceptions': [],
  'verification': ['Test keyboard, menu, toolbar, and accessibility activation paths for the same destructive '
                   'command and confirm none bypass required recovery semantics.'],
  'owner_hints': ['designing-keyboard-power-user-ux'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-command-keyboard-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.commands.chord-timeout-does-not-trigger-partial',
  'domain': 'commands',
  'class': 'behavioral',
  'severity': 'moderate',
  'enforcement': 'warn',
  'title': 'Incomplete keyboard chords must time out without executing a partial command accidentally',
  'statement': 'When a command requires a multi-key chord, an incomplete or timed-out sequence must not reinterpret '
               'the prefix as a different destructive or unrelated command unless that behavior is deliberately '
               'specified.',
  'intent': 'Make multi-stroke shortcuts safe under hesitation, dropped events, layout differences, and users who '
            'abandon a chord midway.',
  'applies_when': ['The product supports sequential keyboard chords where a prefix can overlap with another command '
                   'or normal text/input behavior.'],
  'does_not_apply_when': [],
  'failure_modes': ['After the chord timeout, the prefix executes a command the user did not intend, or buffered '
                    'input is replayed into the wrong target.'],
  'user_impacts': ['Users can trigger surprising actions simply by pausing during a chord or changing their mind '
                   'before completing it.'],
  'observables': ['Begin each registered chord, wait beyond the timeout, cancel focus, and inspect whether any '
                  'command or text mutation occurs from the abandoned prefix.'],
  'falsifiers': ['Timeout and cancellation clear chord state cleanly, with any deliberate fallback behavior '
                 'documented and non-destructive by default.'],
  'repairs': ['Treat chord prefixes as pending command state with explicit timeout and cancellation semantics '
              'instead of dispatching them opportunistically.'],
  'exceptions': [],
  'verification': ['Test slow input, dropped second keys, focus changes, Escape cancellation, and conflicting '
                   'prefixes across supported keyboard layouts.'],
  'owner_hints': ['designing-keyboard-power-user-ux'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-command-keyboard-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.commands.remap-collision-warning',
  'domain': 'commands',
  'class': 'behavioral',
  'severity': 'moderate',
  'enforcement': 'warn',
  'title': 'Shortcut remapping must detect collisions before replacing an existing binding',
  'statement': 'When users assign a custom shortcut that already belongs to another active command in the same '
               'dispatch scope, the remapping UI must expose the collision and resulting resolution before saving.',
  'intent': 'Prevent customization from silently disabling or shadowing existing commands that users may still '
            'depend on.',
  'applies_when': ['The product lets users customize keyboard shortcuts or command bindings within overlapping '
                   'contexts.'],
  'does_not_apply_when': [],
  'failure_modes': ['A new binding silently replaces, shadows, or creates ambiguity with an existing command and the '
                    'user learns only after the old shortcut stops working.'],
  'user_impacts': ['Personalized command maps become unreliable and users can lose access to important actions '
                   'without understanding why.'],
  'observables': ['Assign a key sequence already used by another command in the same and different contexts, then '
                  'inspect warnings and the effective binding map.'],
  'falsifiers': ['The remapper identifies same-scope collisions, explains whether replace, unbind, or context '
                 'separation will occur, and saves only the confirmed resolution.'],
  'repairs': ['Run collision analysis against the effective scoped binding registry before persistence and present '
              'the affected command names to the user.'],
  'exceptions': [],
  'verification': ['Create collisions across global, editor, modal, and plugin scopes and confirm the saved dispatch '
                   'map matches the resolution shown before commit.'],
  'owner_hints': ['designing-keyboard-power-user-ux'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-command-keyboard-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.commands.assistive-technology-reserved-key-not-captured',
  'domain': 'commands',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Application shortcuts must not unconditionally capture keys reserved by assistive technology',
  'statement': 'Keyboard handling must avoid globally suppressing key combinations needed by screen readers, switch '
               'access, browser navigation, or platform accessibility unless a bounded mode has an accessible escape '
               'and justified ownership.',
  'intent': 'Preserve assistive-technology control of the interaction environment while still allowing '
            'application-specific keyboard acceleration where it is safe.',
  'applies_when': ['The application registers global or high-priority key handlers that can cancel default browser '
                   'or platform behavior across large regions of the interface.'],
  'does_not_apply_when': [],
  'failure_modes': ['A blanket preventDefault or equivalent handler intercepts assistive or platform navigation keys '
                    'even when the application has no active command requiring them.'],
  'user_impacts': ['Keyboard and assistive-technology users can become unable to navigate, exit a mode, or invoke '
                   'essential platform accessibility functions.'],
  'observables': ['Inspect key-event cancellation and test representative assistive-technology navigation sequences '
                  'while focus moves through application regions and modal modes.'],
  'falsifiers': ['Reserved or unowned key sequences reach the platform or assistive technology, and any '
                 'intentionally captured mode exposes an accessible exit path.'],
  'repairs': ['Scope key capture to explicit command contexts, avoid blanket cancellation, and document mode '
              'ownership with reliable Escape or equivalent recovery.'],
  'exceptions': [],
  'verification': ['Test with keyboard-only navigation and at least one supported assistive-technology interaction '
                   'model to confirm application handlers do not steal unowned keys.'],
  'owner_hints': ['designing-keyboard-power-user-ux'],
  'verifier_hints': ['critiquing-accessibility'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-command-keyboard-owners-v13'],
  'status': 'active'}]

__all__ = ["COMMAND_KEYBOARD_RULES_V13"]
