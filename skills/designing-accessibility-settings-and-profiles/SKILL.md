---
name: designing-accessibility-settings-and-profiles
description: Use when users must discover, activate, configure, save, restore, transfer, or override accessibility preferences, assistive modes, display adaptations, input accommodations, or context-specific access profiles.
---

# Designing Accessibility Settings And Profiles

## Overview
Accessibility settings have a bootstrap problem: a person may need a feature in order to operate the interface that enables that feature. The settings surface must therefore remain discoverable and operable under the user’s *current* capabilities, not only after the preferred configuration is active. It also has to manage persistence, preview, conflicts, privacy, and recovery without trapping a user in an unusable state.

## Parent Contract
**Required parent:** `designing-accessible-interfaces`.

Consume root accessibility obligations, available system/application adaptations, supported input modalities, device ownership context, profile/persistence capabilities, and privacy constraints. Distinguish product settings from operating-system settings and assistive-technology configuration. Do not duplicate a platform setting unless the product has a clear scope or needs to expose a shortcut into the authoritative setting.

## Decision Model
### 1. Guarantee a bootstrap access path
Identify how a user reaches accessibility settings before zoom, screen reader, high contrast, switch control, reduced motion, captions, or alternative input is enabled. Provide platform-native shortcuts, direct activation, first-run accessibility entry, or external control paths where appropriate. Never require the inaccessible default interaction to enable its own replacement.

### 2. Separate preference, capability, and context
A user preference is not a diagnosis. Model functional needs such as larger text, less motion, stronger contrast, alternate input, captions, longer timeouts, or simplified presentation. Allow context-specific profiles where environment changes the need, but do not silently infer sensitive disability information from use.

### 3. Make preview safe and reversible
Changes that can make content unreadable or interaction impossible need a preview/revert mechanism, timeout rollback, or known recovery gesture. Preserve a reset-to-accessible-baseline path that does not depend on the failed setting.

### 4. Define persistence scope
Specify whether a setting is session, device, account, workspace, document, or organization scoped. Make synchronization visible enough to prevent surprises on shared devices. When preferences travel across devices, translate intent rather than blindly copying unsupported values.

### 5. Resolve conflicts explicitly
System, browser, assistive technology, application, content, and organization policy may all influence output. Define precedence without overriding user safety unnecessarily. Forced colors, text scaling, reduced motion, and input settings must be tested against application themes and custom design tokens.

### 6. Protect privacy and autonomy
Accessibility settings can reveal sensitive information. Limit telemetry, sharing, administrator visibility, and cross-context propagation to justified purposes. Organization policy must not silently disable a person’s access needs without an alternative route and explicit rationale.

## Evidence
ISO/IEC 20071-5:2022 specifies requirements and recommendations for making accessibility settings themselves accessible and usable, including access, operation, saving, and modification. ISO/IEC 24756:2009 provides a still-current framework for describing user, system, and environment access capabilities across platforms. Where personal-needs profiles are used, treat older but confirmed ISO/IEC 24751 models as conceptual support rather than assuming education-specific metadata directly applies to every product. Validate with the actual assistive technologies, operating-system features, devices, and users in scope.

## Output Contract
Produce an `accessibility-settings-contract` containing: bootstrap entry paths; setting inventory; functional-need model; direct activation shortcuts; preview/revert behavior; safe baseline and recovery; persistence and synchronization scope; device translation rules; precedence with OS/browser/AT settings; privacy classification; administrator boundaries; shared-device behavior; reset/export/import semantics; unsupported-feature handling; and verification scenarios performed both before and after each critical accessibility feature is active.

## Failure Traps
- Hiding accessibility settings behind an interface that requires the feature being enabled.
- Treating a preference as a medical label or inferring disability without need.
- Applying a visual setting instantly with no safe rollback when it can make the UI unreadable.
- Syncing sensitive accessibility settings onto shared devices without visibility.
- Overriding operating-system reduced-motion, text-size, or contrast intent for brand consistency.
- Providing “reset” only through the interaction mode that has become unusable.
- Assuming values copy perfectly across platforms with different capabilities.
- Letting organization policy remove the only usable access path silently.

The settings experience succeeds when users can reach, change, test, preserve, and recover their access configuration without first having to overcome the barrier that configuration exists to solve.

## V6 Accessibility Preference Governance
Define a **preference precedence lattice** among OS settings, browser/platform settings, organization policy, product profile, per-surface overrides, and temporary session needs. Keep a **profile portability contract** for settings that should follow a user across devices while excluding device-specific capabilities that cannot transfer safely.

Ship **reset-safe defaults** that restore a usable baseline without erasing unrelated account state. For high-impact settings provide a **setting effect preview** or reversible live change so users can judge readability/motion/density before committing. Detect **assistive-setting conflict** such as custom themes fighting forced colors, compact density fighting target size, or motion personalization overriding reduced motion.

### Falsification
Apply conflicting system/product settings, switch devices, reset, and upgrade from an older profile. If the result becomes inaccessible or unpredictable, preference governance fails.

### Recovery
Apply the precedence lattice, fall back to validated defaults, explain unsupported transfers, and preserve user agency to undo product-level customization.
