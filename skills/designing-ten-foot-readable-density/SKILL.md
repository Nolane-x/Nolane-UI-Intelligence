---
name: designing-ten-foot-readable-density
description: Use when an interface is viewed from couch or room distance and must balance readable type, focus clarity, information density, overscan/safe areas, content hierarchy, and navigation efficiency without simply scaling a desktop layout up.
---

# Designing Ten-Foot Readable Density

## Distance changes the information budget
A ten-foot interface has fewer effective visual details than a desktop viewed at arm’s length. Text, controls, focus indicators, metadata, and imagery compete for recognition under lower angular size and variable television processing. This skill owns the density decisions that determine what remains visible, what is deferred, and what size/spacing is required for reliable recognition at distance.

## Parent Contract
**Required parent:** `routing-ui-work`.

The routing parent invokes this specialist when room-distance viewing is a material constraint. Typography, game HUD, and remote navigation may contribute rules, but this skill owns the overall readability-density envelope.

## Density model
Reason in terms of visual hierarchy tiers, interaction priority, angular readability, line length, focus travel, and screen occupancy. The decision owner is not “make everything larger”; it is which information can be removed, summarized, progressively revealed, or promoted so critical content remains readable without creating excessive navigation.

Define a minimum reliable type/indicator regime based on target display size and viewing distance assumptions, then validate with rendered testing. Secondary metadata may be hidden until focus or detail view; primary actions and state should remain immediately recognizable. Avoid shrinking text to preserve a desktop information count.

## Focus and scan behavior
At distance, focus is a major orientation cue. Ensure the focused item is distinguishable without close inspection, and that nearby items remain sufficiently stable for spatial memory. Dense grids should preserve clear row/column grouping and avoid tiny badges or microcopy as the only status signals.

Large text alone can still fail if lines become too wide or if hierarchy collapses into giant uniform blocks. Use grouping, whitespace, restrained metadata, and staged disclosure to maintain scanability.

## Safe-area and display variance
Account for television safe areas, overscan behavior where relevant, subtitles/captions, platform system overlays, and variable aspect ratios. Critical text and controls should remain within a protected region. Decorative content may extend further, but meaning should not depend on edges that can be cropped.

## Evidence
Evidence includes target viewing assumptions, display sizes, safe-area overlays, rendered captures, physical-distance review, focus visibility checks, and representative dense/long-content states. Test with actual TV-class displays when possible; a desktop screenshot viewed up close is not equivalent evidence.

## Failure modes
Characteristic Failure includes desktop-density menus with tiny metadata, critical status encoded in small badges, giant type causing excessive wrapping and navigation, focus rings too subtle at distance, captions colliding with controls, and content touching unsafe display edges. Another failure is hiding too much information and forcing deep navigation for routine decisions.

## Falsification
Increase viewing distance, reduce display size within support bounds, add long localized labels, activate captions/system overlays, and populate the densest realistic content state. The contract fails if critical information requires squinting, focus cannot be identified immediately, safe-area clipping changes meaning, or density reduction makes common tasks impractically deep.

## Recovery
Reclassify information by decision importance, remove or defer low-value metadata before reducing type size, simplify group structure, and strengthen focus cues. If a surface fundamentally requires desktop-scale density, route to a different interaction model rather than forcing it into ten-foot constraints.

## Output and Handoff
Output: `ten-foot-readable-density-contract`, containing viewing assumptions, hierarchy tiers, density limits, type/focus requirements, safe areas, progressive disclosure, and evidence. Handoff game-specific priority to HUD information priority and control traversal to remote/directional navigation.

## Sibling Boundary and delete-the-skill
Sibling HUD priority owns in-game information under active play pressure; this skill owns room-distance readability across menus and surfaces. Responsive layout owns geometry changes, not viewing-distance density. The delete-the-skill test passes because without it, teams often scale desktop layouts mechanically and preserve information volume at the expense of real ten-foot legibility.