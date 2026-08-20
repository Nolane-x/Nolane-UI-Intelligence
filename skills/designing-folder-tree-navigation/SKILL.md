---
name: designing-folder-tree-navigation
description: Use when files live in nested hierarchies and a tree must support expansion, lazy loading, current location, selection, keyboard navigation, move targets, and very deep structures without losing path context.
---

# Designing Folder Tree Navigation

## Parent Contract
**Required parent:** `designing-file-transfer-and-storage`.

This faculty owns hierarchical folder navigation. It is distinct from generic sidebar navigation because nodes have parent/child object semantics, may load lazily, and may serve both navigation and destination selection for move/copy operations.

## Decision Boundary
Define current folder versus selected tree node; they may coincide in navigation mode but differ when selecting a move destination. Expansion state is presentation, not file mutation. Lazy-loaded children need loading/error states within the tree without collapsing already known ancestors. Keyboard interaction should follow tree semantics with expansion/collapse, parent/child movement, and typeahead where useful.

Deep hierarchies need horizontal/indentation strategy that remains readable under zoom. Renaming or moving the current folder must update ancestor paths and preserve object identity. Permission boundaries can make a child inaccessible without implying deletion. In move mode, disable illegal destinations such as the object's own descendant and explain why.

## Failure Topology
- Clicking an expand chevron also navigates into the folder unintentionally.
- Tree loses expanded ancestors after a lazy-load error.
- Current path is based on names, so rename breaks selection and route identity.
- Deep nesting pushes labels under clipped horizontal space with no scroll/reflow strategy.
- Move dialog allows placing a folder inside itself or a descendant.
- Permission-denied child disappears and users infer it was deleted.

## Falsification and Recovery
Test keyboard tree navigation, expand/collapse, lazy loading, deep nesting, rename/move, permission change, current-folder synchronization, move/copy destination mode, and responsive panels. The design fails if node expansion, navigation, and destination selection are conflated or if stable location is lost after rename.

Recover by separating expansion/current/destination state, using stable folder IDs, modeling load/error per node, validating move constraints, and preserving ancestor context. Add breadcrumbs or path display when deep tree geometry alone cannot convey location.

## Output Contract
Return `folder-tree-contract` with node identity, expansion/current/destination states, keyboard model, lazy-loading/error behavior, depth strategy, rename/move synchronization, permission representation, invalid-destination rules, and tree verification cases.
