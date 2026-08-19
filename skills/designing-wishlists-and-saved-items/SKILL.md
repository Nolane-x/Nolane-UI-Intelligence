---
name: designing-wishlists-and-saved-items
description: Use when shoppers preserve products for later consideration and the interface must maintain intent, list identity, privacy, availability/price drift, movement to cart, and sharing without pretending saved items are reserved.
---

# Designing Wishlists and Saved Items

## Parent Contract
**Required parent:** `designing-commerce-checkout`.

This faculty owns durable shopping intent outside the active cart. It does not own cart totals, inventory reservation, or general bookmarks. A wishlist may represent personal consideration, a named collection, a gift list, or shareable intent; each requires explicit persistence and audience semantics.

## Decision Model
Define what is saved: product family, exact variant, quantity preference, seller offer, or another purchasable identity. Saving only the product family can be useful before variant choice, while a gift registry may require exact configuration. The visible representation should disclose what will happen when “Move to cart” encounters unresolved or unavailable choices.

Persistence and privacy need a clear scope. Anonymous local saves, signed-in account lists, private lists, shared lists, and public registries are different. Changing visibility should be a deliberate authority action, not a side effect of copying a link. If multiple lists are supported, moving versus copying an item must be distinct and recoverable.

Saved commercial facts age. Price, promotion, variant availability, seller, and delivery can change without changing the user's saved intent. Surface material changes when the user revisits the list; never imply that saving reserved price or stock unless the commerce system truly provides that guarantee. Removed products should leave a safe unavailable state long enough for users to understand what changed.

## Failure Topology
- Saving a product silently chooses the currently pictured variant and later adds that unintended variant to cart.
- Wishlist displays the old sale price with no indication the promotion ended.
- Copying a share URL silently changes a private list to public.
- “Move to cart” removes the saved item before cart insertion succeeds.
- Out-of-stock item disappears completely, so users cannot remember what they intended to buy.
- Anonymous wishlist is discarded on sign-in instead of being merged or intentionally kept separate.

## Falsification and Recovery
Falsify with unspecified variants, price/stock changes, product deletion, anonymous-to-account sign-in, multiple named lists, shared/public list permissions, move-to-cart failure, duplicate saved items, mobile/keyboard/screen-reader use, and a public registry owner changing visibility. The design fails if saved intent is mistaken for reservation or if privacy can broaden as an accidental consequence of sharing mechanics.

Recover by storing explicit saved identity and unresolved options, separating intent from commercial guarantees, reconciling fresh price/availability on view, committing cart insertion before removal, defining anonymous merge, and making list visibility independent from copy-link actions.

## Output Contract
Return `saved-commerce-intent-contract` with saved identity granularity, persistence/account merge, list ownership/privacy, multi-list semantics, commercial-drift presentation, unavailable-item behavior, move/copy-to-cart transaction, sharing handoff, accessibility behavior, and falsification cases.