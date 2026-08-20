---
name: designing-dashboard-permission-boundaries
description: Use when dashboard visibility, editing, underlying data access, sharing, export, and drill permissions differ and the interface must communicate capability without leaking restricted information.
---

# Designing Dashboard Permission Boundaries

Dashboard authorization is multidimensional. Being allowed to see a rendered tile does not automatically grant permission to edit the dashboard, inspect its query, export rows, drill to records, or reshare the asset.

## Parent Contract
**Required parent:** `designing-business-intelligence-workspaces`.

The parent establishes analytical workspace behavior. This skill owns permission-aware affordances and disclosure boundaries for dashboards and their dependent analytical capabilities.

## Capability Matrix
Model capabilities separately: view dashboard, view specific tile, change personal filters, edit definition, publish, inspect metric/query, access underlying rows, export, schedule, subscribe, share, manage permissions, and embed. Derive controls from authoritative capability checks rather than from role-name guesses in the client.

Partial visibility must remain coherent. If a user can view nine of ten tiles, decide whether the missing tile is hidden, replaced with a permission state, or blocks the whole dashboard based on product policy and semantic risk. Hiding can be dangerous when users then interpret totals as complete; a visible omission marker may be required.

Do not leak restricted metadata through labels, tooltips, filter value lists, query errors, export filenames, lineage graphs, or preview thumbnails. Redaction should explain the boundary without exposing the protected detail.

Permission changes can occur while the dashboard is open. Revalidate consequential actions and handle revoked access without leaving stale interactive data or cached exports exposed. Saved links should distinguish missing asset from denied access only as policy permits; security copy must not become an enumeration oracle.

## Sharing Semantics
Before sharing, show the target audience and whether recipients need independent data permissions. A dashboard owner must not infer that “share dashboard” delegates access to its underlying sources unless the product explicitly implements such delegation.

## Evidence
Test a matrix of viewers with different dashboard, dataset, row, export, and edit privileges. Verify both visible controls and server enforcement. Include permission revocation mid-session, shared link opening, exported-data attempt, drill into restricted rows, and preview-as-viewer from an editor account.

## Failure Modes
- Client role checks expose edit controls that server later rejects.
- A hidden tile makes the remaining dashboard look complete.
- Filter suggestions reveal restricted entity names.
- Sharing UI implies access transfer that does not occur.
- Export remains enabled after row-level access is revoked.
- Error text discloses restricted dataset or query identifiers.

## Falsification
Give two users the same dashboard but different underlying-data rights. Ask them to perform view, filter, drill, query-inspect, export, and share operations. Falsify if the UI predicts capabilities incorrectly or leaks information through a denied path.

## Recovery
Introduce a capability matrix, authoritative checks, omission semantics, redaction policy, and revalidation at consequential actions. Remove speculative role-based affordances where capability cannot be established.

## Handoff
Coordinate with `designing-dashboard-edit-view-modes` for mode-specific controls, `designing-query-provenance-inspection` for redacted provenance, and `designing-data-lineage-exploration` for permission-aware lineage traversal.

## Output Contract
Return a `dashboard-permission-boundaries-contract` with `capability_matrix`, `partial_visibility_policy`, `redaction_rules`, `sharing_semantics`, `revalidation_points[]`, `revocation_behavior`, `server_enforcement_evidence[]`, `leakage_tests[]`, `failure_findings[]`, and `recovery_actions[]`.