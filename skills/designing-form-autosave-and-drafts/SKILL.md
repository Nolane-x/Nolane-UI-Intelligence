---
name: designing-form-autosave-and-drafts
description: Use when unfinished form work must survive interruption and the interface needs truthful save status, conflict handling, draft lifecycle, and resume semantics.
---

# Designing Form Autosave and Drafts

## Parent Contract
**Required parent:** `designing-forms`.

This faculty owns persistence before final submission. It distinguishes unsaved local edits, queued persistence, server-confirmed draft state, stale copies, and intentionally discarded work. It does not redefine the final transaction or claim that “autosave” is safe when the backend cannot guarantee the corresponding persistence semantics.

## Decision Boundary
Choose the persistence unit explicitly: field, section, whole draft, or operation log. Debouncing every keystroke is not a design model. Saving too frequently can cause contention and stale races; saving too coarsely increases loss. The UI must expose only statuses it can prove: “Saving…”, “Saved at 14:32”, “Offline—changes kept on this device”, or “Couldn’t save” should map to concrete storage states.

Draft identity matters. A newly started draft, an existing submitted record reopened for editing, and a recovered browser-local draft are not interchangeable. Define ownership, expiration, cross-device visibility, and whether another editor can create a competing version. If the server returns a newer revision, never overwrite silently simply because the client has an autosave timer.

Discard must be a real destructive action. If a draft has already synchronized, clearing local fields without deleting the remote draft is not “discard.” Likewise, a successful final submission should transition or retire the draft predictably instead of leaving a ghost draft in recents.

## Failure Topology
- The interface says “Saved” before the server acknowledgement arrives.
- A slow older save response overwrites a newer edit.
- Going offline keeps edits in memory but the UI implies cross-device safety.
- Two tabs autosave competing versions with no revision detection.
- Final submit succeeds, yet the draft later reappears and can be resubmitted.
- “Discard” only resets the current screen while the server draft remains.

## Falsification and Recovery
Falsify with rapid edits, slow and reordered network responses, tab duplication, offline/online transitions, session expiry during save, a newer remote revision, browser restart, and final submission racing with autosave. The design fails if displayed save status cannot be derived from an actual persistence state or if an older write can silently win.

Recover with revision-aware writes, monotonic save acknowledgements, explicit local-vs-remote status, conflict escalation, durable draft identifiers, defined expiry/cleanup, and a final-submit transition that closes the draft lifecycle.

## Output Contract
Return `form-draft-persistence-contract` containing persistence granularity, save triggers, status-state mapping, revision/conflict policy, offline semantics, draft identity/lifetime, multi-tab behavior, discard semantics, resume behavior, final-submit handoff, and falsification scenarios.