---
name: sourcing-rights-safe-visual-media
description: Use when discovery and asset-level rights/provenance verification for external visual media; public discoverability never substitutes for reuse permission
---

# Sourcing Rights-Safe Visual Media

## Parent Contract
**Required parent:** `researching-visual-references`.

`researching-visual-references` discovers visual precedents and source candidates. This owner decides whether a specific external media asset is legally/provenance-safe enough for actual product use; reference viewing alone grants no reuse right.

## Decision Boundary
Own discovery *and* asset-level permission/provenance evidence. Never turn a search-provider reputation into a blanket license. Output `visual-asset-provenance-ledger`.

## Retrieval-to-Use Boundary
The **retrieval-to-use boundary** is explicit: search results are candidates only. For every chosen file capture source page, canonical asset identifier, creator, specific license/rights statement, verification date, attribution text if needed, commercial-use and modification status, and local transformations. This is **asset-level rights proof**.

Apply **source-license distrust** even to open aggregators: metadata can be stale or wrong. Follow through to the origin when practical. Maintain an **attribution completeness ledger** that survives build pipelines and design handoff. Record a **third-party rights caveat** for recognizable people, trademarks, property, culturally sensitive material, privacy/publicity or other non-copyright restrictions when relevant.

## Source Strategy
Use Openverse for broad discovery but verify the source work. Prefer Commons/museum/library open-access sources for historically or scientifically grounded material. Use stock-photo services under their actual custom licenses, not “royalty-free = public domain.” Prefer project-owned/customer-supplied media when provenance is cleaner. Search by semantic job and subject specificity, not merely palette/style.

## Selection
Score candidates on truthfulness, subject specificity, composition/crop potential, visual quality, diversity/non-stereotyping, resolution, rights clarity and performance cost. Reject a prettier candidate when its rights or subject truth are ambiguous. Do not download a corpus “just in case”; keep pointers until an asset is materially selected.

## Decision Model
Search by semantic job → follow candidate to canonical origin → verify per-asset rights → capture creator/attribution/other-rights caveats → score visual fit → retain only candidates with clear use boundary → ledger transformations.

## Evidence
Require canonical asset URL/id, creator, exact license/rights statement, verification date, commercial/modification status, attribution where required, third-party-rights caveat and transformation lineage.

## Output Contract
Emit `visual-asset-provenance-ledger` with asset-level origin, rights, attribution, verification timestamp, permitted uses, third-party caveats, selected derivative chain and quarantine state.

## Failure Traps
Search thumbnail used directly; aggregator license trusted blindly; royalty-free treated as public domain; attribution lost in build; copyrighted museum object confused with CC0 metadata; recognizable person/brand ignored.

## Falsification
Remove the license field from one asset, replace the origin link with a search-result thumbnail, or mark a mixed-license source as CC0. The ledger must fail. Verify that attribution survives a crop/optimization transformation.

## Recovery
Quarantine the asset, re-open the canonical rights page, select a clearer-license alternative or commission/generate one, then rerun integration evidence. Never retroactively invent a license because the layout already depends on the image.
