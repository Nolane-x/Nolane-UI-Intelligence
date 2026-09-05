"""V13 sixth-wave rules; all operational prose is independently authored."""
from __future__ import annotations

DESIGN_SYSTEM_RUNTIME_RULES_V13 = [{'rule_id': 'ui.design-system.invalid-token-fallback-not-silent',
  'domain': 'design-system',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Invalid design-token resolution must not silently fall back to an unrelated value',
  'statement': 'When a semantic or component token cannot resolve because of a missing reference, type error, mode '
               'gap, or invalid alias, the runtime must make that defect diagnosable rather than substituting an '
               'arbitrary default that hides the broken contract.',
  'intent': 'Keep design-system failures observable so consumers do not ship visually plausible but semantically '
            'wrong fallback values.',
  'applies_when': ['The UI resolves design tokens at build or runtime and token references can fail across themes, '
                   'modes, packages, or consumer overrides.'],
  'does_not_apply_when': [],
  'failure_modes': ['A broken token reference quietly produces a generic color, spacing, or fallback value and the '
                    'consuming component appears valid enough to escape detection.'],
  'user_impacts': ['Accessibility, brand, hierarchy, or state semantics can degrade while the underlying '
                   'design-system contract remains hidden and spreads to more consumers.'],
  'observables': ['Break representative token aliases and mode references and inspect runtime value, diagnostics, '
                  'component rendering, and validation output.'],
  'falsifiers': ['Invalid resolution fails loudly, emits structured diagnostics, or uses a documented sentinel '
                 'fallback that cannot be mistaken for a valid semantic value.'],
  'repairs': ['Make token resolution typed and diagnosable, and reserve fallbacks for explicitly declared fallback '
              'chains rather than catch-all substitution.'],
  'exceptions': [],
  'verification': ['Exercise missing references, cycles, type mismatches, absent mode values, and invalid consumer '
                   'overrides and confirm each is surfaced as a contract failure.'],
  'owner_hints': ['governing-token-reference-integrity'],
  'verifier_hints': ['critiquing-design-system'],
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
  'provenance_ids': ['nui-design-system-runtime-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.design-system.theme-switch-clears-stale-mode',
  'domain': 'design-system',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Theme or mode switches must not leave components rendering stale token values',
  'statement': 'When the active design-system theme, density, contrast, or other token mode changes, all consumers '
               'must resolve against the new effective mode rather than keeping cached values from the previous '
               'context.',
  'intent': 'Prevent mixed-mode interfaces where only part of the rendered tree responds to a theme transition.',
  'applies_when': ['The design system supports runtime mode switching and consumers may cache computed token values '
                   'or render through multiple roots, portals, or embedded surfaces.'],
  'does_not_apply_when': [],
  'failure_modes': ['After switching mode, some components retain old colors, spacing, typography, or state tokens '
                    'until rerender, navigation, or reload.'],
  'user_impacts': ['The interface can lose contrast, semantic consistency, or visual hierarchy because two token '
                   'modes coexist unintentionally.'],
  'observables': ['Switch modes while opening portals, overlays, virtualized content, and embedded roots and compare '
                  'resolved tokens before and after the transition.'],
  'falsifiers': ['Every active consumer derives from the new effective mode or an intentionally isolated mode '
                 'boundary is explicit and stable.'],
  'repairs': ['Propagate mode context through all render roots and invalidate cached token resolution when effective '
              'mode changes.'],
  'exceptions': [],
  'verification': ['Exercise rapid mode switching, lazy components, modals, portals, SSR hydration, and nested mode '
                   'overrides and confirm no stale token values remain.'],
  'owner_hints': ['governing-token-mode-inheritance'],
  'verifier_hints': ['critiquing-design-system'],
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
  'provenance_ids': ['nui-design-system-runtime-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.design-system.deprecated-token-use-diagnosable',
  'domain': 'design-system',
  'class': 'behavioral',
  'severity': 'moderate',
  'enforcement': 'warn',
  'title': 'Consumers of deprecated design tokens must remain discoverable during migration',
  'statement': 'When tokens are deprecated, the design-system toolchain should preserve machine-readable deprecation '
               'signals so active consumers can be found and migrated before the token is removed.',
  'intent': 'Turn token deprecation into a controlled lifecycle rather than a documentation note that cannot '
            'identify real usage.',
  'applies_when': ['The design system evolves token names or semantics while multiple applications, packages, or '
                   'components can continue referencing older tokens.'],
  'does_not_apply_when': [],
  'failure_modes': ['Deprecated tokens still resolve normally with no diagnostic path, leaving maintainers unable to '
                    'know which consumers will break at removal.'],
  'user_impacts': ['A later design-system release can cause widespread visual regressions because migration scope '
                   'was invisible until the deprecated token disappeared.'],
  'observables': ['Mark representative tokens deprecated and inspect build diagnostics, usage reports, code search '
                  'metadata, and consumer behavior across packages.'],
  'falsifiers': ['Deprecation produces a discoverable signal and removal planning can enumerate affected consumers '
                 'before the breaking release.'],
  'repairs': ['Attach deprecation metadata to token definitions and expose it through linting, build output, '
              'registry APIs, or migration reports.'],
  'exceptions': [],
  'verification': ['Deprecate, alias, migrate, and finally remove sample tokens and confirm each active consumer can '
                   'be identified before the breaking step.'],
  'owner_hints': ['governing-token-deprecation-lifecycles'],
  'verifier_hints': ['critiquing-design-system'],
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
  'provenance_ids': ['nui-design-system-runtime-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.design-system.unsupported-component-state-rejected',
  'domain': 'design-system',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Components must reject or explicitly handle unsupported state combinations',
  'statement': 'If a component contract does not support a state combination such as '
               'disabled-plus-loading-plus-selected, consumers must not silently compose the states and receive '
               'undefined visual or interaction behavior.',
  'intent': 'Keep component behavior within reviewed state contracts rather than allowing accidental Cartesian '
            'combinations to create hidden product defects.',
  'applies_when': ['Reusable components expose multiple state props, variants, or attributes whose combinations have '
                   'explicit support boundaries.'],
  'does_not_apply_when': [],
  'failure_modes': ['A consumer passes an unsupported combination and the component renders a plausible but untested '
                    'state with ambiguous semantics or interaction.'],
  'user_impacts': ['Users can encounter inconsistent controls, inaccessible states, or contradictory behavior that '
                   'bypassed design-system review.'],
  'observables': ['Enumerate unsupported state combinations from the component contract and render them in '
                  'development, tests, and consuming applications.'],
  'falsifiers': ['Unsupported combinations are blocked, normalized through documented rules, or explicitly covered '
                 'by the component state contract.'],
  'repairs': ['Encode state invariants in types, runtime assertions, stories, and tests rather than relying on '
              'consumer discipline alone.'],
  'exceptions': [],
  'verification': ['Exercise component-state matrices across supported and unsupported combinations and confirm only '
                   'reviewed states can reach production rendering.'],
  'owner_hints': ['governing-component-state-contracts'],
  'verifier_hints': ['critiquing-design-system'],
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
  'provenance_ids': ['nui-design-system-runtime-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.design-system.consumer-override-scope-visible',
  'domain': 'design-system',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Design-system consumer overrides must expose the scope they intentionally diverge',
  'statement': 'A product-specific override to tokens or component behavior should identify whether it applies '
               'locally, per theme, per product, or globally so the exception cannot leak into unrelated consumers '
               'unnoticed.',
  'intent': 'Allow necessary product adaptation without turning one exception into uncontrolled design-system fork '
            'behavior.',
  'applies_when': ['Consumers can override design tokens, component styles, slots, behaviors, or configuration '
                   'beyond the canonical system defaults.'],
  'does_not_apply_when': [],
  'failure_modes': ['An override intended for one product or surface is implemented at a shared layer and silently '
                    'changes other consumers.'],
  'user_impacts': ['Unrelated interfaces can regress or lose system consistency because the exception boundary was '
                   'not explicit.'],
  'observables': ['Apply a representative override and inspect its effect across local component, page, product, '
                  'theme, and shared-package consumers.'],
  'falsifiers': ['The override has a bounded scope that matches its documented intent and does not alter consumers '
                 'outside that boundary.'],
  'repairs': ['Represent exceptions through scoped extension points and record ownership rather than patching shared '
              'primitives or global token values.'],
  'exceptions': [],
  'verification': ['Test override application across multiple products and themes and confirm only the intended '
                   'consumer scope diverges from canonical behavior.'],
  'owner_hints': ['governing-design-system-exceptions'],
  'verifier_hints': ['critiquing-design-system'],
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
  'provenance_ids': ['nui-design-system-runtime-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.design-system.version-mismatch-diagnosable',
  'domain': 'design-system',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Design-system package version mismatches must be diagnosable when contracts depend on coordinated '
           'releases',
  'statement': 'If component packages, token packages, assets, or runtime adapters require compatible versions, a '
               'mismatched consumer installation must expose the incompatibility instead of failing through subtle '
               'styling or behavior drift.',
  'intent': 'Turn cross-package version skew into an explicit integration failure before consumers debug symptoms as '
            'isolated UI defects.',
  'applies_when': ['The design system is distributed across multiple packages or runtimes with versioned '
                   'compatibility relationships.'],
  'does_not_apply_when': [],
  'failure_modes': ['A consumer loads incompatible component and token versions and receives missing states, wrong '
                    'values, or runtime errors with no version-coherence diagnosis.'],
  'user_impacts': ['Teams can ship hard-to-reproduce UI regressions because package skew looks like ordinary '
                   'consumer code failure.'],
  'observables': ['Install intentionally incompatible package combinations and inspect build, startup, runtime '
                  'diagnostics, and affected component output.'],
  'falsifiers': ['Known incompatible combinations are rejected or produce actionable diagnostics that identify the '
                 'mismatched package contract.'],
  'repairs': ['Publish compatibility metadata and validate coordinated package versions during install, build, or '
              'runtime initialization.'],
  'exceptions': [],
  'verification': ['Exercise supported and unsupported version matrices and confirm compatibility failures are '
                   'explicit before users encounter broken UI.'],
  'owner_hints': ['governing-design-system-version-compatibility'],
  'verifier_hints': ['critiquing-design-system'],
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
  'provenance_ids': ['nui-design-system-runtime-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.design-system.semantic-token-type-preserved',
  'domain': 'design-system',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Semantic token references must preserve declared token type through alias resolution',
  'statement': 'A color token must not resolve through an alias chain to spacing, duration, typography, or another '
               'incompatible token type even if the serialized raw value happens to parse.',
  'intent': 'Protect semantic meaning and tooling guarantees across deep alias chains and consumer extensions.',
  'applies_when': ['The token system supports aliases, references, inheritance, or composition across typed semantic '
                   'token definitions.'],
  'does_not_apply_when': [],
  'failure_modes': ['A cross-type reference resolves because raw values share a compatible syntax, allowing '
                    'semantically invalid token substitution to enter components.'],
  'user_impacts': ['Consumers can receive nonsensical or fragile values and automated tooling can no longer trust '
                   'token type when generating platform output.'],
  'observables': ['Create cross-type alias chains that still serialize to valid-looking values and inspect resolver '
                  'type checks and generated artifacts.'],
  'falsifiers': ['Alias resolution preserves type compatibility at every edge or an explicit conversion function '
                 'documents the semantic transformation.'],
  'repairs': ['Validate token-reference types before value resolution and prevent raw serialization coincidence from '
              'bypassing semantic type contracts.'],
  'exceptions': [],
  'verification': ['Test valid same-type aliases, invalid cross-type aliases, nested aliases, and extension tokens '
                   'and confirm type safety survives full resolution.'],
  'owner_hints': ['governing-token-type-conformance'],
  'verifier_hints': ['critiquing-design-system'],
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
  'provenance_ids': ['nui-design-system-runtime-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.design-system.breaking-change-migration-gated',
  'domain': 'design-system',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Breaking design-system changes must be gated by consumer migration evidence before broad rollout',
  'statement': 'Removing or materially changing a token, component state, API, or interaction contract should not '
               'reach all consumers until known usages are migrated or the rollout explicitly bounds the unresolved '
               'impact.',
  'intent': 'Make design-system evolution a controlled release process rather than transferring migration risk '
            'invisibly to downstream products.',
  'applies_when': ['A design-system release includes known breaking changes consumed by multiple applications or '
                   'teams.'],
  'does_not_apply_when': [],
  'failure_modes': ['The breaking version is promoted broadly while active consumers still rely on removed or '
                    'changed contracts and no migration status is known.'],
  'user_impacts': ['Multiple products can regress simultaneously and downstream teams discover the migration only '
                   'after release.'],
  'observables': ['Introduce a breaking contract change, enumerate affected consumers, and inspect release gating, '
                  'migration status, and rollout controls.'],
  'falsifiers': ['Consumer impact is known and either migrated, explicitly waived, or bounded behind staged rollout '
                 'before the breaking version becomes default.'],
  'repairs': ['Connect breaking-change metadata to consumer usage inventory and require migration or explicit '
              'exception evidence in the release gate.'],
  'exceptions': [],
  'verification': ['Simulate a breaking token and component change across several consumers and confirm unresolved '
                   'usage blocks or bounds broad promotion.'],
  'owner_hints': ['governing-design-system-breaking-change-rollouts'],
  'verifier_hints': ['critiquing-design-system'],
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
  'provenance_ids': ['nui-design-system-runtime-owners-v13'],
  'status': 'active'}]

__all__ = ["DESIGN_SYSTEM_RUNTIME_RULES_V13"]
