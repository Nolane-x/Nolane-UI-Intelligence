---
name: designing-color-independent-status-encoding
description: Use when success, warning, error, availability, severity, or categorical state is currently communicated by hue and must remain understandable without color perception.
---

# Designing Color-Independent Status Encoding

## Parent Contract
**Required parent:** `designing-accessible-interfaces`.

This faculty owns redundant semantic encoding for state. It does not choose the product palette or chart theme. Its job is to make status recognizable when hue is unavailable, altered, low-saturation, projected poorly, printed monochrome, or indistinguishable to a user.

## Decision Boundary
For each meaningful color state, identify at least one independent cue appropriate to the task: text label, icon shape with an accessible name, pattern, position, line style, symbol, or explicit numeric value. Choose cues that are readable at the scale and density of the component. A tiny icon shape may not be sufficient in a dense monitoring grid; a full text label may be excessive in a compact chart legend. The redundancy must encode the same state, not merely decorate the color.

Keep encoding consistent across product surfaces. If a triangle means warning in dashboards, it should not mean success in a different module. Avoid icon-only differences whose silhouettes are too similar at small sizes. For data visualization, pair hue with line style, direct labels, marker shape, or spatial grouping according to the analytical task rather than adding arbitrary patterns everywhere.

## Failure Topology
- Required fields are indicated only by red labels.
- Online/offline presence uses green/gray dots with no text or shape distinction.
- Chart series are distinguishable only through adjacent hues in the legend.
- A status icon exists but is decorative and has no semantic label for assistive technology.
- Error and warning both use the same exclamation symbol, leaving color as the only differentiator.
- Printed or screenshot-exported content loses the only cue because color is removed.

## Falsification and Recovery
Review screens in grayscale, common color-vision simulations, forced-colors mode, low-saturation displays, and monochrome print/export where applicable. Ask whether a user can identify each material state without knowing the original colors. The design fails if color removal changes a decision or causes two operational states to collapse.

Recover by selecting a redundant cue based on task density, adding explicit labels where consequence is high, standardizing semantic iconography, and adapting visualizations with shape/line/direct labels. Do not respond by removing useful color; keep color as one channel while adding independent meaning.

## Output Contract
Return `color-independent-status-contract` with state inventory, primary and redundant encodings, density-specific variants, assistive labels, visualization adaptations, cross-surface consistency rules, and color-removal verification cases.
