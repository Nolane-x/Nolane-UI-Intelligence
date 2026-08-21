---
name: designing-browser-and-device-evidence-matrices
description: Use when UI correctness may vary by browser engine, OS, input hardware, device class, pixel density, installed capabilities, or assistive technology stack and verification needs risk-based environment coverage rather than one canonical machine.
---

# Designing Browser and Device Evidence Matrices

## Environment is part of the claim
Web and cross-platform interfaces execute inside engines and hardware that differ in layout, input, media, viewport behavior, accessibility APIs, font rendering, permissions, and feature support. This skill owns which environment combinations are materially different enough to require evidence and how that coverage is justified.

## Parent Contract
**Required parent:** `binding-ui-evidence`.

The parent binds claims to evidence. This specialist begins when implementation behavior can diverge across runtime environments even when product state and intended design are the same.

## Risk-based environment axes
Relevant axes can include browser engine and version, OS, device class, touch/pointer/pen support, keyboard presence, pixel ratio, GPU path, reduced-motion/contrast settings, accessibility technology, installed fonts, permission model, and WebView or embedded-host constraints. The decision owner is the equivalence partition: which environments share enough implementation behavior to be represented by one case and which own unique failure risk.

Do not turn the matrix into a market-share spreadsheet. A low-share environment may deserve a case if it owns a distinct engine path, regulated audience, kiosk deployment, enterprise baseline, or critical assistive technology combination. Conversely, ten Chromium-branded browsers may add little if they exercise the same relevant path.

## Capability-driven cases
Prefer capability predicates over brand folklore. Test the environment where dynamic viewport units differ, where a required input method is absent, where font metrics shift, where WebGL/WebGPU capability changes, or where accessibility semantics are exposed differently. Pin actual versions in evidence so a historical pass is not mistaken for proof against a newer engine regression.

## Matrix cell contract
Each cell states environment identity, product fixture, capabilities under test, known exclusions, expected invariants, evidence artifacts, and freshness. A cell can satisfy multiple claims only if the captured environment actually exercises those paths. If a capability is unavailable, distinguish unsupported-by-product from untested.

## Evidence
Strong evidence includes runtime user-agent/engine metadata, OS/build, viewport and scale, input capabilities, relevant feature probes, accessibility stack where applicable, and artifact links. Pair screenshots with runtime traces when the risk concerns interaction or semantics. Record browser flags or emulation because simulator evidence is not always equivalent to physical hardware.

## Failure modes
Characteristic Failure includes calling a desktop responsive emulator “mobile tested,” treating all Chromium hosts as identical despite different embedding policies, ignoring OS-level font or accessibility differences, stale device lab evidence, and claiming broad support from one engine. Another failure is environment explosion without a rationale, which makes the matrix expensive and therefore eventually ignored.

## Falsification
Change engine, device pixel ratio, hardware input mix, installed font availability, accessibility stack, and permission behavior while holding the product fixture constant. The contract fails if a known distinct environment has no owner, if emulation is mislabeled as physical-device evidence, if a cell cannot state which unique risk it covers, or if stale versions remain counted indefinitely.

## Recovery
When new environment-specific failures appear, determine whether they create a new equivalence class or expose a missing capability axis. Add the narrowest cell that captures the distinct risk, then retire redundant cells with evidence. Do not silently broaden support claims to environments that were never exercised.

## Output and Handoff
Output: `browser-and-device-evidence-matrices-contract`, containing risk axes, environment equivalence classes, cell metadata, capability predicates, freshness, and support-claim boundaries. Handoff geometry-driven variation to responsive regression matrices and environment-caused rendering divergence to rendered-environment drift.

## Sibling Boundary and delete-the-skill
Sibling responsive regression owns layout mode transitions regardless of browser. Accessibility evidence packets own proof of inclusive obligations, though they may reference environment cells here. The delete-the-skill test passes because without environment ownership, one green browser can be mistaken for cross-platform evidence while engine- or device-specific failure classes remain invisible.