---
name: designing-scroll-linked-motion
description: Use when visual change is driven by scroll position and the mapping must preserve native scrolling, content comprehension, accessibility and performance while avoiding scroll hijacking.
---

# Designing Scroll-Linked Motion

## Parent Contract
**Required parent:** `designing-motion`.

This skill owns animations whose progress is meaningfully tied to scroll progress or viewport passage. It does not own page storytelling, information architecture or the scroll container itself.

## Decision Boundary
Ask whether scroll position is actually the right control signal. Sticky explanatory sequences, progress indicators, spatial diagrams and subtle parallax may benefit. A generic marketing section does not need scroll choreography just because it looks cinematic.

Preserve native scroll authority. Wheel, touchpad, touch, keyboard, scrollbar drag and assistive navigation must move content predictably. Do not replace scroll distance with fixed animation steps, trap users inside sections, or require high-frequency wheel gestures to advance a story.

Map progress explicitly: define start/end anchors, clamping, direction reversal and behavior when layout height changes. Responsive reflow, font loading and dynamic content can move anchors; avoid cached document coordinates that drift from reality. Effects must be reversible when the user scrolls back unless the product state is genuinely one-way.

Parallax needs depth meaning and restrained amplitude. Large differential motion can impair reading and trigger vestibular discomfort. Reduced-motion mode should remove nonessential spatial movement while keeping progress/content order intact.

Performance is a first-class constraint. Prefer compositor-friendly properties and platform-native scroll-driven facilities where appropriate; avoid main-thread work proportional to every scroll event.

## Failure Topology
- Scroll is hijacked into a sequence and users cannot move at their chosen speed.
- Progress jumps after images load and change section height.
- Text moves at a different rate from its reading context.
- Reverse scrolling does not reverse the visual state, leaving contradictions.
- Reduced motion disables content rather than only motion.
- Main-thread listeners cause scroll jank.

## Falsification and Recovery
Use mouse wheel, trackpad, touch, PageDown, keyboard focus jumps and scrollbar thumb; resize, zoom text, load delayed media, scroll rapidly both directions and enable reduced motion. If content access or reading order depends on animation frames, the design fails.

Recover by restoring native scrolling, making progress a pure function of current geometry, reducing spatial amplitude and turning essential information into persistent content rather than transient motion.

## Output Contract
Return `scroll-linked-motion-contract` with purpose, scroll container, progress anchors, reversible mapping, dynamic-layout recalculation, input-equivalence, reduced-motion substitute, performance strategy and scroll stress tests.