---
name: designing-measurement-and-unit-input
description: Use when users enter physical measurements and the interface must coordinate magnitude, unit choice, conversion, precision, bounds, and domain-safe interpretation.
---

# Designing Measurement and Unit Input

## Parent Contract
**Required parent:** `designing-forms`.

This faculty owns values whose meaning depends on a physical or domain unit: length, mass, temperature, duration, pressure, dosage quantity, storage size, and similar measurements. It does not define scientific or safety limits without domain authority; it ensures magnitude and unit cannot drift apart in the UI.

## Decision Boundary
Model a measurement as `{magnitude, unit, dimension}`. Decide whether the unit is fixed, user-selectable, locale-preferred, or inherited from equipment/account settings. A suffix inside an input may be enough for fixed units; selectable units need an operable control whose change semantics are explicit.

When the unit changes, choose between preserving physical quantity and preserving typed digits. Converting `10 cm` to `100 mm` preserves quantity; changing the label to `mm` while leaving `10` does not. In some workflows the user intends to change the interpretation rather than convert, so the product must decide deliberately and signal the result.

Precision belongs to the domain. Conversion can create repeating decimals or values beyond meaningful instrument resolution. Do not display false precision merely because a formula produces it. For temperatures and other affine conversions, never treat conversion as simple multiplication. Bounds and step size must be evaluated in canonical units to avoid inconsistent acceptance.

## Failure Topology
- Unit selector changes label but not magnitude, silently changing the physical value.
- Converted value displays many meaningless decimals and implies nonexistent accuracy.
- A min/max rule is applied before conversion and accepts a value outside the true bound.
- Locale decimal notation conflicts with a unit abbreviation and parsing fails.
- Keyboard users cannot reach a unit selector embedded as decorative suffix UI.
- A safety-critical measurement silently defaults to a unit the user did not choose or confirm.

## Falsification and Recovery
Falsify with unit switching after entry, extreme values, fractional quantities, negative temperatures, locale decimal separators, paste with and without unit text, instrument-derived precision, keyboard/screen-reader operation, and canonical-bound validation. The design fails if the same visible state can be interpreted as two different physical quantities or if conversion implies more certainty than the source value.

Recover by storing canonical quantity separately from display unit, declaring conversion semantics, bounding precision by domain evidence, validating canonically, exposing unit choice accessibly, and requiring explicit confirmation where unit ambiguity carries material risk.

## Output Contract
Return `measurement-input-contract` with dimension model, unit authority, canonical representation, unit-change semantics, conversion equations/source, precision policy, bounds/steps, locale parsing, accessibility behavior, high-risk confirmation rules, and falsification cases.