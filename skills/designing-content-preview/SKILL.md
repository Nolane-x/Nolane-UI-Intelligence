---
name: designing-content-preview
description: Use when authors need to inspect how draft content will render in one or more destination contexts and the preview must make renderer, device, data, unpublished state, and fidelity boundaries explicit.
---

# Designing Content Preview

## Parent Contract
**Required parent:** `designing-editor-canvas-workspaces`.

This faculty owns draft-to-destination inspection before release. It does not grant publishing authority and does not replace design-fidelity verification. A preview is useful only when authors know what runtime, channel, viewport, personalization state, and content revision it represents.

## Decision Boundary
Define renderer parity. The strongest preview uses the same templates, tokens, parsing, feature configuration, and data transformations as production while isolating unpublished access. If exact parity is impossible, label the known deviations rather than presenting a polished approximation as authoritative.

Preview context must be selectable when output varies by channel or audience: desktop/mobile, email client class, locale, theme, logged-in state, segment, or destination layout. Avoid an explosion of fake device frames; expose only contexts that materially change decisions. Keep the current draft revision synchronized and show when preview is stale because rendering is still based on an older save.

Interactive previews need boundaries. Links may need interception so authors do not accidentally leave the preview; forms, purchases, emails, analytics, or other side effects should be disabled or sandboxed. Private preview URLs require authentication or unguessable bounded capability and should expire/revoke according to product policy.

## Failure Topology
- Preview uses a simplified renderer and content looks different after publication with no warning.
- Author edits the draft but preview silently remains on the prior revision.
- Mobile “preview” is just desktop scaled down inside a device chrome frame.
- Clicking a CTA from preview triggers a real external side effect or production analytics event.
- Shared preview link remains valid after the draft becomes private or is deleted.
- Personalization preview shows one hard-coded user and is presented as representative of every audience.

## Falsification and Recovery
Falsify with stale draft save, channel-specific overrides, long localization, responsive media, personalized content, preview-link sharing, expired authentication, interactive CTA, production renderer update, keyboard/screen-reader navigation, and a published comparison against the same revision. The design fails if authors cannot identify which revision/context produced the render or if preview can cause production side effects.

Recover by reusing the production rendering pipeline where feasible, recording revision/context, exposing stale state, sandboxing actions, authenticating preview links, limiting context choices to decision-relevant variants, and documenting unavoidable parity gaps.

## Output Contract
Return `content-preview-contract` with renderer/parity source, draft revision binding, channel/audience/viewport contexts, stale-state behavior, action sandboxing, preview-link authority/lifetime, personalization limits, accessibility inspection, parity verification, and falsification cases.