---
name: designing-multiline-labels
description: Design labels that wrap across lines without losing control association, alignment, target geometry, or scan efficiency.
---

# Designing multiline labels

Labels often grow under localization, accessibility text scaling, or domain terminology. Use this skill when buttons, form labels, tabs, toggles, list rows, or settings must tolerate more than one line safely.

## Decision ownership

Own which label types may wrap, maximum lines, alignment, control geometry, baseline behavior, and whether wrapping changes row height or surrounding layout. Decide when truncation or a different component is preferable.

## Inputs and evidence

Collect longest localized labels, font scaling, helper text, icons, badges, target sizes, table/list density, and adjacent controls. Inspect components whose current height assumes one line.

## Procedure

Allow wrapping where meaning is more important than fixed rhythm, especially form labels and explanatory settings. Keep the label visibly and semantically associated with its control. For buttons, verify multiline text still creates a clear hit area and balanced padding; for tabs, consider whether variable height harms navigation scanning.

Define vertical alignment of icons and trailing actions when labels wrap. Use min-height rather than fixed height where appropriate. Ensure row virtualization can handle variable height if wrapping is possible.

## Failure topology

Fixed-height controls clip the second line. Icons aligned to the first line can look detached from the overall label. Variable-height rows can break virtualized list measurements. Another failure is allowing wrapping in dense tab bars where each tab becomes a different height and reading order becomes noisy.

## Falsification

Test two- and three-line labels, long words, 200% text size, localization, and mixed icon/text controls. Navigate with keyboard and touch. Verify focus rings contain the entire control and dynamic row measurements update correctly.

## Output contract

Produce a `multiline-labels-contract` defining wrap eligibility, line limits, geometry, icon/action alignment, semantic association, virtualization considerations, responsive behavior, and representative long-label tests.

## Handoffs

Use `designing-text-truncation` when wrapping is not viable, `designing-responsive-form-layouts` for form reflow, `designing-line-height-rhythm` for vertical metrics, and component-specific specialists for tabs or buttons.