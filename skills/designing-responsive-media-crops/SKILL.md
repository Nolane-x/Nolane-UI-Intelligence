---
name: designing-responsive-media-crops
description: Adapt image and video crops across aspect ratios without cutting essential subjects, text, instructional detail, or focal meaning.
---

# Designing responsive media crops

Responsive media should fill layouts without turning cropping into random content loss. Use this skill when hero imagery, thumbnails, product media, editorial images, or video previews occupy changing aspect ratios.

## Decision ownership

Own crop strategy, focal metadata, object-fit behavior, breakpoint-specific art direction, safe zones, and fallback when no crop preserves essential information. Decide when to letterbox, contain, replace the asset, or change layout instead of cropping harder.

## Inputs and evidence

Collect source dimensions, focal subjects, embedded text, product boundaries, faces, captions, legal marks, instructional details, supported aspect ratios, and author-supplied focal points. Include alternate assets if editorial systems support art direction.

## Procedure

Classify media as decorative, focal-subject, informational, or composition-sensitive. Decorative media can tolerate aggressive crop; informational imagery often cannot. Define focal coordinates or semantic safe regions where automation is used. For known responsive states, allow art-directed variants when one crop cannot serve all ratios.

Keep captions and credits associated even when the image representation changes. For video, consider motion of important subjects over time rather than a single poster-frame focal point.

## Failure topology

Center cropping cuts faces or products near edges. Automated face detection can preserve the wrong face when several people matter. Embedded text may be clipped even while the visual subject survives.

Overusing alternate assets creates editorial complexity and inconsistent message if variants are not governed together.

## Falsification

Preview every supported ratio with representative assets, including multiple subjects, edge-aligned products, diagrams, and embedded typography. Inspect at localization widths and high zoom. Remove focal metadata and verify fallback is safe rather than silently destructive.

Ask whether users lose information, not only whether the composition remains attractive.

## Output contract

Produce a `responsive-media-crops-contract` with media classes, focal/safe-zone metadata, fit/crop rules, art-direction variants, fallback policy, caption/credit behavior, and visual verification across target aspect ratios.

## Handoffs

Use `designing-image-galleries` for gallery navigation, media-library skills for authoring metadata, `designing-responsive-dashboard-grids` for card constraints, and `verifying-responsive-state-parity` where media carries actionable information.