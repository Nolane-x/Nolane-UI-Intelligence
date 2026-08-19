---
name: designing-password-creation-and-strength
description: Use when an account flow creates or changes a password and the UI must communicate requirements, strength evidence, visibility, manager support, and recovery without inventing harmful composition rules.
---

# Designing Password Creation and Strength

## Parent Contract
**Required parent:** `designing-authentication-and-passkeys`.

This faculty owns password-entry interaction and requirement communication. It does not set security policy independently of the service’s authoritative requirements, and it does not privilege passwords over passkeys or other factors when the parent architecture chooses otherwise.

## Decision Boundary
Expose actual acceptance constraints before submission when they affect creation, but do not turn requirement lists into a game of green checkmarks if the policy itself is weak or outdated. Length, breached-password screening, and service-specific restrictions are different kinds of evidence. A “strength” meter must explain what its signal represents; it cannot claim that a password is safe merely because it contains four character classes.

Support password managers and paste. Blocking paste, disabling autofill, or forcing repeated manual entry increases failure without proving ownership. A reveal control should preserve focus, announce state, and respect shoulder-surfing context. Confirmation fields are justified only when they prevent a specific costly typo and cannot be replaced by reveal or manager workflows.

When the service rejects a password for server-authoritative reasons, retain the user’s understanding without retaining secret values longer than necessary. Never echo a rejected password into logs, analytics, validation messages, or screenshots. Changing an existing password also needs current-session and recovery consequences defined by the parent account lifecycle.

## Failure Topology
- Strength meter awards “Strong” to a predictable pattern because it checks character variety only.
- Password manager paste is blocked and users are pushed toward weaker memorable choices.
- Requirements appear only after submit, causing repeated blind retries.
- Reveal toggling moves the cursor or clears the input.
- Client accepts a password that the server rejects under a different rule with no reconciliation.
- Validation telemetry captures the secret value.

## Falsification and Recovery
Falsify with long manager-generated passwords, Unicode, paste/autofill, mobile reveal controls, server-side breach rejection, policy changes between page load and submit, accessibility zoom, screen reader announcement, and a password-change flow that revokes other sessions. The design fails if UI “strength” overstates evidence or if accepted input pathways punish secure tooling.

Recover by sourcing rules from authoritative service policy, supporting managers, separating acceptance from heuristic strength, making reveal accessible, handling server disagreement explicitly, and routing session/recovery effects to the account lifecycle owner.

## Output Contract
Return `password-creation-contract` with authoritative requirements, allowed input pathways, strength-signal semantics, reveal/confirmation behavior, server-rejection handling, secret-data boundaries, accessibility behavior, account-lifecycle handoffs, and falsification cases.