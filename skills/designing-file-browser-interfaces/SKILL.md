---
name: designing-file-browser-interfaces
description: Use when users navigate durable file collections and need a coherent model for location, selection, sorting, metadata, actions, view modes, and large collections rather than a generic list of filenames.
---

# Designing File Browser Interfaces

## Parent Contract
**Required parent:** `designing-file-transfer-and-storage`.

This faculty owns the file-collection workspace. It does not own the folder tree specifically. It decides how current location, files versus folders, selection, primary actions, metadata density, sort/view state, and large-collection loading support file-management tasks.

## Decision Boundary
Define the location model first: hierarchical folders, virtual collections, search results, recent/shared views, or a hybrid. A file browser should tell users where they are and whether operations affect the real location or only the current filtered view. Selection must remain stable across view-mode changes where the same objects persist. Distinguish opening/previewing from selecting, especially on touch where single/double click conventions differ.

Metadata should match tasks: size, modified time, owner, sync status, type, sensitivity, or version only when useful. Grid and list views may offer different density but share file identity/action semantics. Sorting large remote collections must be authoritative across pagination, not only the visible page. Empty, inaccessible, offline, and loading states need different recovery paths.

## Failure Topology
- Breadcrumb suggests a folder path while the content is actually a search result collection.
- Switching list/grid view loses multi-selection.
- Sorting occurs only client-side on the loaded page and creates false global order.
- Double-click is required for opening with no clear touch/keyboard equivalent.
- File actions change between view modes because separate components use different command registries.
- Offline state looks like an empty folder and implies data was deleted.

## Falsification and Recovery
Test hierarchical/virtual locations, list/grid, multi-selection, large pagination, sorting, keyboard/touch open, offline/permission loss, rename/delete, and route/history navigation. The design fails if users cannot tell whether they are acting on objects or on a view/filter abstraction.

Recover by making location type explicit, centralizing file identity/actions, preserving selection across presentation changes, moving sort authority to the full collection source, and separating empty from unavailable/offline states.

## Output Contract
Return `file-browser-contract` with location model, file/folder representation, selection/open semantics, view-mode parity, metadata priorities, sort/loading authority, collection states, and file-browser verification flows.
