---
name: mapping-visual-media-opportunities
description: Use when the decision of where subject-native photographs, illustrations, diagrams, archival material, video, 3D or generated media carry more product meaning than generic interface geometry
---

# Mapping Visual Media Opportunities

## Parent Contract
**Required parent:** `directing-visual-ambition`.

`directing-visual-ambition` defines the intended experiential/visual level. This owner translates that ambition into evidence-bearing media opportunities without using media quantity as a proxy for ambition.

## Decision Boundary
Own where imagery, illustration, archival material, diagram, video, 3D, generative media or data visualization materially carries product meaning. Do not automatically add images to every screen. Output `visual-media-opportunity-map`.

## Observation Before Decoration
Build a **media semantic job map** from user comprehension, emotional intent and subject truth: show the actual object, demonstrate scale, teach a mechanism, establish place/people, provide evidence, create atmosphere, compare states, or express brand character. Estimate **subject-native evidence density**: how much real visual material exists in the domain and how valuable it is to the task.

For each candidate slot estimate **media omission cost**: what is lost if the UI contains only type, controls and geometry? Select from a **representational modality ladder**—real photograph/archive → truthful diagram/data → commissioned/generated illustration → meaningful abstraction → pure typography/geometry—according to semantic job, rights, safety, latency and production constraints. Record **visual slot necessity** rather than filling every empty region.

## Anti-Card/Orb Rule
Do not equate “more media” with “less UI”. Product controls and information structure remain interface. The defect is substituting generic geometry for a subject that could be shown more truthfully. A scientific product may legitimately need plotted geometry; a banking product may need no photography; a museum landing page likely loses substantial truth if the art itself is absent.

## Branching
If native media is high-value and rights-cleared, source it. If native media exists but cannot be used, commission/generate a truthful alternative. If abstraction conveys a real relation better, keep abstraction and document its semantics. If imagery would distract from high-stakes action or increase ambiguity, deliberately omit it.

## Decision Model
Inventory subject-native evidence → identify semantic jobs → estimate omission cost → select representational modality → assess rights/safety/performance → rank necessary slots → explicitly reject filler media.

## Evidence
Require subject/material inventory, each slot’s semantic job, omission counterfactual, preferred/fallback modality, shape-substitution risk, constraint reason and final use/omit/commission/generate decision.

## Output Contract
Emit `visual-media-opportunity-map` with surface, subject-native-media state, ranked opportunities, semantic jobs, preferred media/fallbacks, omission cost, rights/safety constraints, shape risk and decision.

## Failure Traps
Every section gets an image; premium means stock photography; no-media banking console gets forced hero art; museum page hides the collection; decorative illustration steals authority from real data.

## Falsification
Blind the product name and replace every image candidate with a gradient orb. If the page still communicates equally well, the planned media may be decorative theatre. Conversely remove all media from a domain where physical artifact/scale is central; if comprehension or affect collapses, omission was not neutral.

## Recovery
Return to the semantic jobs, remove filler slots, promote only high-information media, and route unresolved rights/generation needs to sourcing or authoring owners before visual composition continues.
