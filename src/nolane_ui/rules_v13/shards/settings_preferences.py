"""V13 sixth-wave rules; all operational prose is independently authored."""
from __future__ import annotations

SETTINGS_PREFERENCES_RULES_V13 = [{'rule_id': 'ui.settings.saved-state-distinct-from-effective',
  'domain': 'settings',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Saved settings must be distinguished from settings that are currently effective',
  'statement': 'When a preference has been stored but cannot take effect until restart, reconnect, reload, policy '
               'refresh, or another boundary, the UI must not represent saved state as already active.',
  'intent': 'Separate persistence truth from runtime truth so users can tell whether a setting merely saved or is '
            'actually influencing current behavior.',
  'applies_when': ['A setting can persist successfully while its effective runtime value changes later or depends on '
                   'another system boundary.'],
  'does_not_apply_when': [],
  'failure_modes': ['The control shows the newly saved value as active even though the running feature continues '
                    'using the previous effective configuration.'],
  'user_impacts': ['Users can troubleshoot against the wrong configuration or believe a safety, privacy, '
                   'accessibility, or workflow preference is already enforced.'],
  'observables': ['Change a setting that requires an activation boundary and compare stored value, rendered control '
                  'state, and actual runtime behavior before activation.'],
  'falsifiers': ['The interface distinguishes saved and effective states and clearly communicates the boundary '
                 'required for the new value to become active.'],
  'repairs': ['Model persisted value and effective runtime value separately, then render pending activation instead '
              'of collapsing them into one boolean state.'],
  'exceptions': [],
  'verification': ['Save the preference, inspect behavior before and after the required activation boundary, and '
                   'verify status labels track the actual effective value.'],
  'owner_hints': ['designing-configuration-drift-review'],
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
  'provenance_ids': ['nui-settings-preference-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.settings.sync-bound-to-account',
  'domain': 'settings',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Synced preferences must stay bound to the account that owns them',
  'statement': 'Preferences synchronized across devices must not leak from one signed-in account to another merely '
               'because both accounts use the same browser profile, device, or application installation.',
  'intent': 'Keep preference synchronization aligned with account identity so switching users cannot inherit private '
            'or consequential settings from the previous principal.',
  'applies_when': ['The product synchronizes user preferences through an account while multiple accounts can use the '
                   'same client installation or device.'],
  'does_not_apply_when': [],
  'failure_modes': ['After an account switch, controls or behavior remain configured from the previous account until '
                    'a later refresh or manual correction.'],
  'user_impacts': ['A user can inherit another person’s privacy, notification, locale, accessibility, or workflow '
                   'choices without realizing the settings are not theirs.'],
  'observables': ['Configure distinct preferences in two accounts, switch between them without restarting the '
                  'client, and inspect both control values and behavior.'],
  'falsifiers': ['Each account loads and applies its own synchronized preference set, while intentionally '
                 'device-local preferences are labeled as such.'],
  'repairs': ['Namespace synced settings by account identity and clear or rehydrate account-owned effective state '
              'during identity transitions.'],
  'exceptions': [],
  'verification': ['Alternate accounts across online and offline states and confirm synchronized preferences never '
                   'cross account ownership boundaries.'],
  'owner_hints': ['designing-cold-start-preference-capture'],
  'verifier_hints': ['critiquing-security-and-privacy'],
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
  'provenance_ids': ['nui-settings-preference-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.settings.device-conflict-resolution-visible',
  'domain': 'settings',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Conflicting preference edits from different devices must resolve visibly',
  'statement': 'When the same synchronized preference changes concurrently on multiple devices, reconciliation must '
               'expose the resulting effective value instead of silently oscillating or overwriting a recent local '
               'choice.',
  'intent': 'Make cross-device settings convergence legible so users know which preference actually won and whether '
            'another device changed it.',
  'applies_when': ['A synchronized preference can be edited independently on two clients that reconnect or '
                   'synchronize at different times.'],
  'does_not_apply_when': [],
  'failure_modes': ['A local preference appears saved, then later changes because a remote value wins without any '
                    'visible reconciliation or source indication.'],
  'user_impacts': ['Users can repeatedly “fix” a setting that keeps reverting, or miss a privacy or notification '
                   'change introduced from another device.'],
  'observables': ['Edit the same synchronized setting to different values on two disconnected clients, reconnect '
                  'them, and trace the resulting local and server state.'],
  'falsifiers': ['The reconciliation policy produces one authoritative value and the affected clients visibly update '
                 'to that value without claiming the losing edit remained active.'],
  'repairs': ['Apply a documented conflict policy, retain enough revision metadata to detect divergence, and surface '
              'the reconciled value when a local choice is superseded.'],
  'exceptions': [],
  'verification': ['Create simultaneous preference conflicts across multiple devices and verify convergence, '
                   'notification, and subsequent edits all start from the same effective value.'],
  'owner_hints': ['designing-configuration-drift-review'],
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
  'provenance_ids': ['nui-settings-preference-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.settings.reset-scope-preview',
  'domain': 'settings',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Resetting preferences must preview exactly which scope will return to defaults',
  'statement': 'A reset action must state whether it affects one control, a section, a workspace, an account, a '
               'device, or all synchronized preferences before destructive confirmation.',
  'intent': 'Prevent broad configuration loss when reset wording such as “restore defaults” can refer to multiple '
            'nested preference scopes.',
  'applies_when': ['A settings surface offers reset, restore-default, clear-customization, or equivalent actions at '
                   'more than one possible scope.'],
  'does_not_apply_when': [],
  'failure_modes': ['The user can confirm a reset without knowing whether unrelated preferences or other scopes will '
                    'also be restored.'],
  'user_impacts': ['Users can lose carefully configured accessibility, notification, privacy, or workflow settings '
                   'well beyond the intended change.'],
  'observables': ['Open reset controls from section, workspace, and account contexts and compare the previewed scope '
                  'with the resulting configuration changes.'],
  'falsifiers': ['The confirmation names the affected scope and only those preferences are reset, with broader '
                 'resets requiring a separate explicit decision.'],
  'repairs': ['Bind reset commands to an explicit scope object and summarize the classes of settings that will be '
              'affected before mutation.'],
  'exceptions': [],
  'verification': ['Seed distinct non-default values across nested scopes, perform each reset path, and verify only '
                   'the previewed scope changes.'],
  'owner_hints': ['designing-configuration-drift-review'],
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
  'provenance_ids': ['nui-settings-preference-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.settings.dependency-disable-explains-consequence',
  'domain': 'settings',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Disabling a prerequisite setting must explain the dependent behavior that becomes inactive',
  'statement': 'If turning off one preference disables or overrides other configured features, the settings UI must '
               'expose that dependency rather than leaving dependent controls apparently configured but ineffective.',
  'intent': 'Keep effective configuration understandable when settings have prerequisite, parent-child, policy, or '
            'mode dependencies.',
  'applies_when': ['One preference gates the runtime effect of one or more dependent settings while those dependent '
                   'values may remain stored.'],
  'does_not_apply_when': [],
  'failure_modes': ['A parent toggle is disabled and dependent preferences still appear enabled or configured even '
                    'though their behavior can no longer occur.'],
  'user_impacts': ['Users can believe protections or features remain active because stored dependent values look '
                   'unchanged despite being operationally ignored.'],
  'observables': ['Configure a dependent preference, disable its prerequisite, and compare visible control state '
                  'with runtime behavior and persisted values.'],
  'falsifiers': ['The UI shows which dependent settings are inactive while preserving their stored values when '
                 'restoration is intentional.'],
  'repairs': ['Model dependency state explicitly and render dependent controls as inactive-with-reason rather than '
              'conflating persistence with effectiveness.'],
  'exceptions': [],
  'verification': ['Toggle prerequisites on and off around configured dependents and verify the UI, stored values, '
                   'and effective behavior remain consistent.'],
  'owner_hints': ['designing-accessibility-settings-and-profiles'],
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
  'provenance_ids': ['nui-settings-preference-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.settings.autosave-failure-visible',
  'domain': 'settings',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Automatic preference saving must expose failures instead of implying persistence',
  'statement': 'A settings surface that saves changes automatically must show when persistence fails and must not '
               'leave the control in a settled state that implies the new value is safely stored.',
  'intent': 'Prevent silent configuration loss in interfaces where the absence of a Save button makes visual state '
            'the primary signal of persistence.',
  'applies_when': ['Changing a preference triggers automatic network or local persistence without a separate '
                   'explicit save action.'],
  'does_not_apply_when': [],
  'failure_modes': ['The control remains on the new value after a save error even though refresh or another device '
                    'would still load the old preference.'],
  'user_impacts': ['Users can leave the settings surface believing a consequential preference was saved when it will '
                   'later revert.'],
  'observables': ['Force the persistence request to fail after a preference change and compare the rendered state '
                  'with authoritative stored configuration.'],
  'falsifiers': ['A failed autosave produces a visible recoverable error and the UI distinguishes unsaved local '
                 'intent from authoritative stored state.'],
  'repairs': ['Track pending and failed persistence states per preference and offer retry or rollback without '
              'pretending the mutation committed.'],
  'exceptions': [],
  'verification': ['Exercise transient and permanent save failures, navigate away and back, and confirm the user can '
                   'determine whether the change persisted.'],
  'owner_hints': ['designing-configuration-drift-review'],
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
  'provenance_ids': ['nui-settings-preference-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.settings.workspace-vs-global-scope-visible',
  'domain': 'settings',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Workspace-scoped and global preferences must be visually distinguishable before editing',
  'statement': 'When the same concept can be configured globally and overridden per workspace, project, profile, or '
               'device, the control must show which scope is being edited and whether an override is active.',
  'intent': 'Prevent users from changing the wrong configuration layer when identical preference names exist at '
            'multiple scopes.',
  'applies_when': ['The product supports a hierarchy such as account default plus workspace override, or global '
                   'default plus device-local preference.'],
  'does_not_apply_when': [],
  'failure_modes': ['A user changes a setting from one context without realizing the change affects every workspace '
                    'or only the current workspace.'],
  'user_impacts': ['A local customization can unexpectedly alter all contexts, or a supposed global fix can fail '
                   'elsewhere because only an override changed.'],
  'observables': ['Set different values at global and workspace levels, navigate between contexts, and inspect '
                  'labels, inheritance indicators, and effective behavior.'],
  'falsifiers': ['The edited scope and inheritance relationship are visible, and removing an override predictably '
                 'reveals the parent value.'],
  'repairs': ['Represent preference scope as first-class state and show whether the value is inherited, overridden, '
              'device-local, or globally authoritative.'],
  'exceptions': [],
  'verification': ['Edit the same preference at each supported scope and verify changes affect exactly the labeled '
                   'scope with inheritance updating correctly.'],
  'owner_hints': ['designing-configuration-drift-review'],
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
  'provenance_ids': ['nui-settings-preference-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.settings.requires-restart-state-visible',
  'domain': 'settings',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Preferences that require restart or reload must remain visibly pending until activation',
  'statement': 'When a setting cannot affect the current process until restart, reload, reconnect, or relaunch, the '
               'UI must retain a pending-activation state until that boundary actually occurs.',
  'intent': 'Prevent users from assuming a runtime-sensitive preference is already active simply because its stored '
            'value changed successfully.',
  'applies_when': ['A preference changes configuration consumed only during process startup, session establishment, '
                   'renderer initialization, or another discrete activation boundary.'],
  'does_not_apply_when': [],
  'failure_modes': ['The setting immediately appears fully active even though current behavior still reflects the '
                    'previous runtime value.'],
  'user_impacts': ['Users can make decisions based on a security, accessibility, performance, or integration setting '
                   'that has not taken effect yet.'],
  'observables': ['Change the setting, inspect current runtime behavior before restart, then activate the boundary '
                  'and compare effective behavior afterward.'],
  'falsifiers': ['A pending indicator remains until activation and disappears only after the runtime reports or '
                 'demonstrates the new value is effective.'],
  'repairs': ['Track activation generation separately from stored configuration and clear pending state only after '
              'the relevant runtime boundary completes.'],
  'exceptions': [],
  'verification': ['Repeat the setting change with restart, reload cancellation, crash recovery, and multiple '
                   'windows to ensure pending state reflects real activation.'],
  'owner_hints': ['designing-configuration-drift-review'],
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
  'provenance_ids': ['nui-settings-preference-owners-v13'],
  'status': 'active'}]

__all__ = ["SETTINGS_PREFERENCES_RULES_V13"]
