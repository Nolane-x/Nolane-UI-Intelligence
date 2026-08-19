---
name: designing-link-sharing
description: Use when possession of a URL can expose or authorize access and the product must make link scope, capability, expiration, revocation, copying, and accidental redistribution understandable.
---

# Designing Link Sharing

## Parent Contract
**Required parent:** `designing-collaboration-and-presence`.

This faculty owns shareable-link behavior as a capability distribution problem. It does not own the general sharing dialog or recipient invitations. A copied URL may be merely a locator that still requires normal access, or it may itself carry authority; the interface must make that distinction explicit.

## Decision Boundary
Classify link mode before presenting Copy link: restricted locator, organization-authenticated link, anyone-with-link capability, password-protected link, expiring review link, or another bounded mode. The visible label should describe who can open it, not implementation language such as “token enabled.” If changing link mode broadens access, stage or confirm that change separately from copying.

Capability links need lifecycle controls grounded in server authority: creation time, scope, role, expiration, revocation, optional rotation, and perhaps usage limits. Copying an existing capability should not silently mint a new token unless product policy requires it. Regenerating or revoking a link must explain whether old copies stop working immediately and whether active sessions remain valid.

Previewing a link should reflect the recipient experience without leaking the actual capability into logs, screenshots, or analytics. Link text may be shortened visually, but copy must use the canonical URL. If the link can escape the organization through forwarding, the UI should communicate that redistribution property at the moment authority is broadened.

## Failure Topology
- “Copy link” silently changes access from restricted to public.
- Revoking a link only hides it from the dialog while old URLs remain valid.
- Regenerate creates a new token but does not explain that bookmarks using the old token will break.
- Analytics captures the full secret-bearing capability URL.
- Organization-only link is labeled “Anyone with link,” causing users to expect external access that will fail.
- A password or expiry requirement is visible to the owner but omitted from recipient preview/testing.

## Falsification and Recovery
Falsify with restricted-to-public mode change, copied link forwarded externally, expiration, revocation, regeneration, owner permission loss, authenticated and anonymous recipients, recipient preview, browser history/logging, and an old link opened after rotation. The design fails if a user cannot state who gains access from possession of the URL or what happens to previously distributed copies after a lifecycle action.

Recover by separating copy from authority mutation, representing link modes in audience language, enforcing expiry/revocation server-side, protecting token material from telemetry, providing recipient-perspective verification, and stating old-link consequences before rotation.

## Output Contract
Return `link-sharing-contract` with link mode, audience/capability semantics, creation/copy behavior, role and scope, expiration, revocation/rotation, redistribution warning, recipient preview, token-data boundaries, accessibility copy/status behavior, and falsification cases.