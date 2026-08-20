---
name: designing-native-share-sheet-intents
description: Use when a mobile product invokes or receives operating-system share intents and must control payload meaning, privacy, preview, completion semantics, and return behavior across unknown external targets.
---

# Designing Native Share Sheet Intents

## Parent Contract

**Required parent:** `designing-mobile-native-application-shells`.

This skill owns the boundary between application content and the operating system's sharing ecosystem. It does not design every external destination. It decides what leaves the app, in which representation, with what privacy classification and user preview, and how the app truthfully handles the limited completion evidence returned by system share surfaces.

## Payload decisions

Start from user intent: share a reference/link, a rendered artifact, original file, selected excerpt, structured object, invitation, or snapshot. These are not interchangeable. Define canonical payload variants and the meaning lost in each. A screenshot can preserve appearance but destroy accessibility and live data; a deep link can preserve identity but fail for recipients without permission; exporting a file can create an uncontrolled durable copy.

Minimize payload by default. Do not add internal IDs, hidden metadata, precise location, diagnostic data, EXIF, account names or private URLs merely because the share API accepts them. For sensitive domains, show what will be disclosed and whether access controls travel with the reference. If content requires server-side link creation, separate link-generation success from presentation of the OS share sheet.

The system owns target selection and often much of the UI. Respect platform contracts rather than recreating a branded destination picker. Activity exclusions should be based on real capability/security constraints, not aesthetic preference. Account for extensions/targets that consume only some payload types or transform them.

Completion semantics are weak on many platforms. Dismissing the share sheet, selecting a target, and the recipient actually receiving/publishing content are different events. Never mark a collaborative invitation as accepted or a document as externally delivered solely because the share surface closed successfully.

Receiving share intents is a separate entry boundary: parse incoming items, show import scope, handle multiple files/URLs/types, and route through authentication/permission/import validation. Do not silently publish imported material.

## Evidence

Inspect platform share APIs, target capability behavior, exported file/link formats, privacy/security requirements, metadata stripping, accessibility of shared artifacts, and return callbacks on supported OS versions. Test common targets plus unknown/unsupported targets, cancellation, offline link generation and very large payloads.

## Failure topology

A share action can leak hidden document metadata, expose a private tokenized URL, mislabel cancellation as success, hand a screenshot where a recipient needs searchable text, generate duplicate invitation links on retries, or lose the user's current editing state when returning from an external target. Another failure is trapping users in an app-specific share picker that omits OS-installed destinations and accessibility behavior.

## Falsification

Share each material payload type through several target classes, cancel at every stage, revoke recipient access, go offline during link generation, inspect resulting metadata, and return to an in-progress draft. The contract fails if disclosure exceeds previewed scope, if success wording outruns available evidence, if return corrupts application state, or if a shareable representation cannot be consumed independently as promised.

## Recovery

Separate payload preparation, OS handoff and downstream outcome. If payload creation fails, keep the user in the app with recoverable context. If the OS returns ambiguous completion, report only what is known. Regenerate/revoke links according to domain policy and strip unnecessary metadata at export boundaries.

## Output contract

Return a `native-share-sheet-intents-contract` containing intent classes, payload variants, disclosure policy, metadata rules, link-generation lifecycle, system-surface invocation, target exclusions with rationale, completion evidence ceiling, receive/import behavior, cancellation/return state, and verification cases.

## Handoffs

Use link-sharing/invitation owners for access semantics, file export owners for artifact generation, privacy-sensitive owners for disclosure constraints, deep-link routing for received links, and app lifecycle restoration when external activity can suspend or recreate the process.