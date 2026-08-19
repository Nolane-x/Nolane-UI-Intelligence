---
name: designing-role-management
description: Use when administrators create, inspect, assign or retire named roles and the interface must distinguish role definition, membership, scope, effective permissions and lifecycle without turning roles into opaque permission bundles.
---

# Designing Role Management

## Parent Contract
**Required parent:** `designing-permissions-and-consent`.

This faculty owns the administrative lifecycle of named roles. Fine-grained permission comparison is delegated to `designing-rbac-matrices`; inheritance and policy precedence are delegated to `designing-policy-inheritance`.

## Decision Boundary
A role is a reusable responsibility/access definition with stable identity, display name, description, scope and permission/policy bindings. Distinguish **system roles** that may be immutable from **custom roles** administrators can edit. Do not let “Admin” become a vague superuser label whose actual authority is invisible.

Role pages should answer: what does this role permit, where does it apply, who currently has it, whether it is inherited, what changes if it is edited, and what dependencies prevent deletion. Editing a role that is assigned to hundreds of users is a high-impact policy change, not equivalent to editing a label.

Assignment and definition are separate tasks. Adding a user to a role should not silently clone/edit the role; changing a role’s permissions should not require navigating through individual members. Where scoped roles exist—project admin vs organization admin—show scope in the role identity and assignment controls.

Role deletion needs dependency-aware recovery. Options may include block while assigned, migrate assignments to another role, remove assignments with explicit consequence, or archive the role. Preserve audit history even after retirement.

Effective permissions may include direct grants or inherited policy beyond the named role. The role view must not falsely imply it explains the user’s full access if other sources exist.

## Failure Topology
- “Manager” role name looks descriptive but no one can inspect its actual authority.
- Editing a custom role instantly changes 10,000 members with no scope/consequence preview.
- System role appears editable until save, then fails mysteriously.
- Deleting a role strands resources whose workflows require at least one owner/admin.
- Role page claims a user lacks permission even though inherited policy grants it elsewhere.
- Same role name exists at project and organization scope with no visible distinction.

## Falsification and Recovery
Falsify with system/custom roles, large membership, scoped roles, inherited grants, deletion dependencies, concurrent admin edits and permission rollback. Compare role-definition changes to effective-access diffs for impacted subjects.

Recover by separating definition/assignment, surfacing scope and mutability, previewing affected members/resources, preserving audit history and delegating effective-access resolution to policy owners.

## Output Contract
Return `role-management-contract` with role identity/type/scope, definition fields, membership summary, mutability, edit impact preview, assignment handoff, retirement/dependency policy, effective-access disclaimer and lifecycle tests.