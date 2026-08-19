---
name: designing-voice-control-targetability
description: Use when users may operate the interface through spoken target names and visible labels must map predictably to accessible control identities.
---

# Designing Voice Control Targetability

## Parent Contract
**Required parent:** `designing-voice-conversational-ui`.

This faculty owns targetability for system voice-control technologies that let users say a visible label or command to activate an existing control. It is distinct from designing a conversational assistant. The critical invariant is that what users can see, infer, and pronounce corresponds to what the accessibility layer exposes as an actionable target.

## Decision Boundary
Use visible text as the strongest command vocabulary wherever possible. Icon-only actions need stable accessible names and may require visible labels in contexts where numbered overlays are impractical. Avoid duplicate visible labels for unrelated controls in the same scope unless surrounding context can disambiguate them. If the interface changes labels responsively, the accessible name and documentation must change coherently rather than preserving a hidden desktop vocabulary.

Consider pronunciation, localization, abbreviations, symbols, and dynamic identifiers. A control labeled with an opaque icon, emoji, or stylized acronym may be hard to speak. User-generated object names can create collisions with command words; define how selection or scoped commands resolve ambiguity. Voice targeting must not depend on hover-only text that never appears for users who cannot hover.

## Failure Topology
- Visible “Save copy” is programmatically named “Duplicate,” so speaking the visible label fails.
- Ten unlabeled icon buttons require users to guess invisible terminology.
- Two “More” buttons are indistinguishable without a contextual target name.
- Localized visual labels coexist with English-only accessible labels.
- An acronym is visually stylized in a way speech recognition cannot predict.
- Dynamic content changes the target's name while the user is composing a command.

## Falsification and Recovery
Operate representative screens with platform voice control, including duplicate labels, icon-only controls, menus, dialogs, lists, localized UI, and narrow layouts. Compare spoken commands to visible labels and accessible names. The design fails if a user who can see the label still needs undocumented semantic knowledge to activate it by voice.

Recover by aligning visible and accessible naming, disambiguating repeated controls with stable object context, adding visible labels where icon-only targeting is brittle, and validating localized pronunciation. Do not solve ambiguity by adding long inaccessible hidden phrases that no user could reasonably know to speak.

## Output Contract
Return `voice-targetability-contract` with visible-to-accessible naming rules, duplicate-label disambiguation, icon-only policy, pronunciation/localization risks, dynamic-name stability, responsive naming rules, and platform voice-control verification scenarios.
