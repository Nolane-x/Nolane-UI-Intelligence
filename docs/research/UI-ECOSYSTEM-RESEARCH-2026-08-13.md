# NUI v4 — UI Ecosystem Intelligence Research

**As of:** 2026-08-13  
**Scope:** implementation ecosystems, animated/interactive components, source retrieval, adaptation, integration risk and agent routing.

## Why this wave reopened NUI

V3 could reason about product closure, interaction and visual evidence, but a strong agent could still fall back to generic implementation because it had no governed way to discover and reuse current UI primitives, animation engines, design systems or specialist component ecosystems. A link such as React Bits was usable only as human context, not as a typed decision input. V4 closes that gap without turning NUI into a static link dump.

The architectural finding is that external UI sources have **different source roles**. A gallery of animated components, a headless accessibility primitive, a motion engine, an editor SDK and a design-system implementation cannot be compared as if they were interchangeable “UI libraries.” Source role therefore precedes popularity or aesthetic novelty.

## Primary-source mechanisms incorporated

### React Bits

Primary repository: https://github.com/DavidHDev/react-bits  
License evidence: https://github.com/DavidHDev/react-bits/blob/main/LICENSE.md

Useful mechanism: a large, inspectable gallery of animated/interactive React effects that can seed implementation research and aesthetic mechanism extraction. NUI does not treat the gallery as semantic/accessibility authority. Current license text is MIT + Commons Clause and restricts selling/sublicensing/redistributing the components themselves, so `adapt`/`adopt` requires live license inspection and an integration audit.

### GSAP official agent skills

Primary repository: https://github.com/greensock/gsap-skills

Useful mechanism: split animation intelligence into core tweens, timelines, ScrollTrigger, plugins, framework integration and performance rather than one giant “animation” prompt. NUI adopts the architectural lesson — typed routing to the needed mechanics — while keeping product/motion appropriateness and accessibility as independent NUI owners.

### Design Agent Skills catalogue

Primary repository: https://github.com/podo/design-agent-skills

Useful mechanism: a two-tier router with lightweight pointers and on-demand upstream retrieval. The same repository also exposes the supply-chain problem: upstream sources change, overlap and may not be pinned. NUI therefore uses a curated typed registry plus primary-source verification instead of preloading every external skill.

### tldraw

Primary repository: https://github.com/tldraw/tldraw  
License evidence: https://github.com/tldraw/tldraw/blob/main/LICENSE.md

Useful mechanism: a mature infinite-canvas abstraction. It also demonstrates why capability fit is insufficient: current production use is governed by a non-MIT tldraw license/license-key model. NUI separates implementation power from legal/adoption posture.

## Ecosystem coverage model

The v4 registry spans categories including motion/animation, creative effects, headless primitives, interaction state machines, design systems, positioning/overlays, data visualization, rich text, data grids, forms, drag/drop, notifications, canvas/whiteboard, 3D/spatial, mobile UI and design-agent skill catalogues.

The registry is deliberately a **curated retrieval cache**. It is expected to become stale. High/very-high drift entries set `verify_live_before_use=true`; queries can return `live_search_required=true`. This converts “the model should probably browse” into a deterministic routing condition.

## Selection model

The allowed terminal decisions are `adopt`, `adapt`, `inspire`, `build`, or `reject`. Ranking factors are capability fit, stack fit, category fit, source-role fit and accessibility posture. Stars/popularity are intentionally excluded.

`adopt` and `adapt` require current license posture plus README/license/implementation inspection. Material `inspire` decisions still require citation and an adaptation boundary so a distinctive mechanism is not laundered into unattributed local design.

## Rich-interaction model

Animated/direct-manipulation UI is treated as a stateful interaction system, not decoration. The contract includes state ownership, activation thresholds, semantic commit, modality equivalence, focus/announcement behavior, reduced motion, interruption/retargeting, SSR/hydration strategy, cleanup, performance and exit strategy.

## Falsification

The v4 adversarial suite contains 14 distinct failure classes: popularity-only selection, unresolved license, screenshot-only inspection, stale API, wrong stack, wrong source role, copy-without-adaptation, missing reduced motion, drag without keyboard, SSR/hydration mismatch, dependency overkill, no exit strategy, missing citation and trusting an upstream demo as local runtime proof.

## Bounds

NUI does not claim that the registry lists every useful UI repository, that every listed source is safe/current for a future project, or that a source's upstream quality transfers unchanged into local integration. Live primary-source verification and local runtime evidence remain required where the task depends on them.
