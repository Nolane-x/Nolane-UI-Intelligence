---
name: designing-truncation-and-overflow-truth
description: Use when visible text may be clipped, ellipsized, line-clamped, or summarized and the interface must preserve access to the full truth, distinguish omission from absence, and protect decision-critical content.
---

# Designing Truncation and Overflow Truth

## Truncation Changes Information
Ellipsis is not merely a layout technique: it withholds characters. This skill owns whether shortening is permissible, what information may be hidden, how omission is signaled, and how the complete value remains recoverable for users and assistive technology.

## Parent Contract
**Required parent:** `crafting-typography`.

The parent defines typography. This specialist governs intentional visible omission after text has been judged too large for its allotted space.

## Truth Classification
Classify content as identity-critical, decision-critical, comparison-critical, descriptive, redundant, or decorative. Account numbers, file names, version identifiers, warnings, and differentiating suffixes often cannot be safely end-truncated. For some values middle truncation preserves both prefix and suffix; for prose, line clamping may be acceptable only with a clear expansion path.

The rendered string must communicate that more content exists. A clipped edge with no signal can be mistaken for complete text. The accessibility name should not blindly expose hidden sensitive text when the visible UI intentionally redacts it; truncation and redaction are different policies.

## Evidence
Evidence includes collision cases where two values become visually identical after truncation, keyboard/touch access to the full value, copy behavior, screen-reader naming, long/localized text, zoom, and constrained-width states. Verify recovery without hover because hover may be unavailable.

## Failure Modes
Failure includes two files both shown as `quarterly-repo…`, hidden negative signs or units, warnings clamped before the consequence, full values available only in hover tooltips, ellipsis used even though text is actually absent, and copy actions copying the truncated visual string instead of the canonical value.

## Falsification
Falsification constructs values that differ only in the truncated region, disables hover, navigates by keyboard/touch, and asks the user to identify/copy the correct full value. If distinct canonical values become operationally indistinguishable or full truth is unrecoverable, the truncation contract is false.

## Recovery
Recovery expands the field, changes truncation strategy, exposes an explicit detail/copy affordance, or preserves a discriminating segment. Decision-critical text should wrap or restructure rather than disappear. If space is fundamentally inadequate, revisit region priority instead of hiding truth.

## Output and Handoff
Output: `truncation-and-overflow-truth-contract` defining eligible content classes, truncation method, ambiguity checks, full-value recovery, accessibility/copy behavior, and evidence. Handoff wrapping without omission to line-breaking design.

## Sibling Boundary and delete-the-skill
Line-breaking retains all text; readable measure sets preferred width. Neither owns information loss and recoverability. Removing this skill leaves a distinct truth/identity failure class unowned.