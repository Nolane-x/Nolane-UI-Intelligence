---
name: designing-organization-administration
description: Use when administrators manage an organization’s identity, membership, teams, domains, ownership, lifecycle and global controls and the UI must protect tenant boundaries and high-impact changes.
---

# Designing Organization Administration

## Parent Contract
**Required parent:** `routing-ui-work`.

This faculty owns the information and interaction architecture of organization-level administration. Role, RBAC, policy inheritance, billing and authentication/session management remain specialist dependencies rather than being reimplemented here.

## Decision Boundary
Define the organization object and its governance surfaces before listing settings. Typical capabilities may include profile/identity, members, invitations, teams/groups, roles, domains, security/authentication integrations, global policies, integrations, audit, billing relationship, data lifecycle and ownership transfer. Include only capabilities justified by product truth.

Administration must keep **tenant scope visible**. In products where users belong to several organizations, every destructive or policy-changing surface should make the active organization unmistakable. Switching organizations must not leave stale member selections, drafts or cached counts that later apply to the new tenant.

Ownership and last-admin invariants are safety boundaries. Removing the final owner, disabling the only authentication method, deleting a verified domain or leaving the organization can strand access. Gate such operations with precondition checks and explain required remediation instead of failing after submission.

Membership lifecycle needs pending invite, active, suspended, removed and external/guest distinctions where supported. Removing a member can affect resource ownership, assignments, API tokens, automation and shared content; preview dependencies rather than presenting a generic “Remove user?” dialog.

Global administration often changes many downstream users. Use effective-scope previews, auditability and explicit save/rollout models for high-impact configuration.

## Failure Topology
- Administrator edits Organization B using stale selections loaded under Organization A.
- Remove-member dialog omits resources/workflows owned solely by that member.
- Last owner can demote themselves and lock everyone out.
- Member counts mix guests, invited and active users without labels.
- Organization deletion is placed beside harmless profile fields with the same confirmation pattern.
- Global setting appears to affect one project because scope is not visible.

## Falsification and Recovery
Falsify with multi-organization switching, last-owner removal, member dependency removal, pending invites, domain/security changes, organization deletion and stale tabs. Assert every action against tenant ID and preconditions at commit.

Recover by binding admin state to explicit organization identity, separating lifecycle sections, adding dependency previews/precondition gates and delegating specialized policy/billing/security edits to their canonical owners.

## Output Contract
Return `organization-administration-contract` with organization identity/scope, capability map, membership lifecycle, ownership invariants, dependency previews, global-change safeguards, tenant-switch isolation, destructive lifecycle and cross-tenant tests.