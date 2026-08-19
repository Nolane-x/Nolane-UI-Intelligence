---
name: designing-cookie-consent-controls
description: Use when a web product must expose browser-storage or tracking choices and the UI must coordinate categories, pre-consent behavior, reject/accept/customize paths, withdrawal, region/policy variance, and script activation using current authority rather than dark patterns.
---

# Designing Cookie Consent Controls

## Parent Contract
**Required parent:** `designing-permissions-and-consent`.

This faculty owns interaction around cookie and similar web-storage/tracking categories. It does not determine which technologies legally require consent in a jurisdiction; that classification must be verified against current policy and legal authority. The interface must accurately control the actual storage/scripts, not merely display a banner whose toggles are disconnected from runtime behavior.

## Decision Architecture
Map each category to real technical mechanisms and purpose descriptions. Strictly necessary storage, preferences, analytics, advertising, or other classifications must reflect the current product implementation and authority; do not invent categories for visual symmetry. Optional technologies that require a choice under applicable policy should not execute before the relevant state allows them.

Primary paths should be semantically balanced enough that refusal is not made materially harder than acceptance where policy requires genuine choice. “Customize” needs understandable categories, not vendor-by-vendor complexity by default, while a deeper vendor/detail layer may be necessary for transparency. Persist consent state with version/scope metadata and expose a reliable way to reopen controls after the banner disappears.

Changing choices must affect runtime. Loading a disabled script once and then merely hiding its UI is not withdrawal. Some technologies may require reload, cookie deletion, local-storage cleanup, or downstream signaling; describe the effect truthfully and avoid claiming perfect retroactive erasure when it is technically or legally false.

## Failure Topology
- Optional analytics fires before the banner choice, making the control cosmetic.
- Reject is hidden behind multiple screens while Accept all is one prominent click.
- Category labels are vague marketing terms that do not explain purpose.
- Turning analytics off updates the toggle but leaves the tracker active until next session with no disclosure.
- Consent state lacks policy version and cannot explain why users are asked again.
- Banner blocks the site indefinitely even when only optional technologies are at issue and policy does not require such blocking.

## Falsification and Recovery
Falsify with first visit before choice, accept all, reject optional, granular selection, policy/version update, region change, reopening preferences, script load failure, server-side and client-side trackers, keyboard/screen-reader operation, and withdrawal after scripts already ran. The design fails if visible category state cannot be reconciled with actual active storage/tracking mechanisms.

Recover by binding categories to an audited technical inventory, verifying current jurisdictional/policy requirements, gating optional runtime behavior, providing symmetric choice/reopen paths, versioning stored preferences, and implementing truthful reload/cleanup/downstream signaling on change.

## Output Contract
Return `cookie-consent-control-contract` with technical category inventory, authority-verification obligations, initial gating behavior, accept/reject/customize paths, storage/version scope, runtime activation/deactivation, reopen/withdrawal behavior, reload/cleanup semantics, accessibility requirements, and falsification cases.