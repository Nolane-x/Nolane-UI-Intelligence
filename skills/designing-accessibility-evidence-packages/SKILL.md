---
name: designing-accessibility-evidence-packages
description: Package accessibility evidence across automated checks, keyboard behavior, assistive technology, zoom/reflow, contrast, and human judgment so compliance claims are auditable and scoped.
---

# Designing accessibility evidence packages

A passing automated scanner is not a complete accessibility verification. Use this skill when a release, component, or design system needs defensible evidence of accessible behavior.

## Decision ownership

Own evidence scope, test matrix, tooling, manual procedures, assistive-technology environments, defect disposition, and claim wording. Decide what is verified, partially verified, untested, or dependent on consumer implementation.

## Inputs and evidence

Collect applicable standards, component/page inventory, automated results, keyboard tests, screen-reader sessions, zoom/reflow evidence, contrast, motion preferences, high-contrast/forced-colors behavior, platform support, and known exceptions.

## Procedure

Map requirements to evidence methods. Use automation for machine-detectable issues, manual keyboard/focus inspection for interaction, assistive technology for semantics and announcements, and visual stress tests for zoom/contrast/reflow. Record exact versions and environments.

Separate component guarantees from application obligations. A component may expose proper semantics only when consumers supply a label. Document unresolved defects and exceptions with owners and impact rather than hiding them inside a pass/fail score.

## Failure topology

Aggregate accessibility scores imply completeness that does not exist. Testing one screen reader/browser pair may miss platform-specific defects. Another failure is attaching screenshots without reproducible steps or requirement mapping.

Evidence can become stale after UI changes if it is not tied to a revision.

## Falsification

Select claimed requirements and reproduce the evidence from the package. Change a component revision and verify stale evidence is invalidated. Seed issues automation cannot detect, such as illogical focus order, and confirm manual gates catch them.

## Output contract

Produce an `accessibility-evidence-packages-contract` containing revision scope, requirement matrix, automated/manual/AT evidence, environments, defects/exceptions, consumer obligations, reproducibility, and claim limitations.

## Handoffs

Use specific accessibility skills for discovered issues, `designing-ui-regression-evidence` for continuous gates, `verifying-typography-under-zoom` for scaling, and `designing-design-decision-records` for accepted exceptions.