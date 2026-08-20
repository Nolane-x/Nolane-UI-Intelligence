---
name: designing-marketplace-trust-signals
description: Use when a marketplace shows seller ratings, verification, transaction history, badges, guarantees, review summaries, protection claims, or risk indicators and must tie every signal to bounded evidence and policy meaning.
---

# Designing Marketplace Trust Signals

Trust signals influence purchase and seller opportunity. They must communicate evidence the platform actually has, not manufacture confidence through decorative badges, vague “verified” labels, or unqualified protection claims.

## Parent Contract
**Required parent:** `designing-marketplace-operations`.

The parent owns marketplace roles and policy. This skill owns buyer/seller-facing trust evidence and the limits of what each signal proves.

## Signal Provenance
For every signal, define source, computation, time window, eligibility, update cadence, and claim boundary. “Identity verified” may mean a document/processor check passed; it does not prove product quality. “Top seller” may reflect sales volume, service metrics, review quality, or a platform program; state the basis users need to interpret it.

Ratings require denominator and distribution context. Show count, recency or relevant filtering where useful, and distinguish product review from seller/service review. Prevent a five-star score from looking equally reliable at two reviews and twenty thousand reviews.

## Verification and Badges
Badges should correspond to governed states, expire when evidence expires, and update when seller eligibility changes. Avoid creating multiple visually prestigious badges that all derive from the same underlying evidence. If verification is mandatory for every seller, a special badge may mislead by implying exceptional vetting.

## Protection Claims
Buyer protection, authenticity checks, escrow, returns, or guarantees need concise eligibility conditions and links to policy. Never present “protected purchase” when exclusions materially apply and are only discoverable after a dispute.

## Reviews and Abuse
Show moderation/removal policy at the level needed to understand review integrity. Incentivized, verified-purchase, imported, or edited reviews should be identified if the platform distinguishes them. Fraud detection scores or internal risk signals are usually not direct user-facing trust badges.

## Evidence
Test new seller with little history, long-tenure seller, recently suspended seller, expired verification, low review count, disputed reviews, protected versus excluded category, and seller operating under multiple storefronts. Verify signal state changes when source evidence changes.

## Failure Modes
- “Verified” has no visible meaning or source boundary.
- Rating hides tiny sample size.
- Expired verification badge remains cached.
- Protection language omits material exclusions at purchase decision time.
- Platform risk score leaks as a pseudo-objective public reputation label.
- Multiple badges double-count the same evidence and exaggerate trust.
- Review moderation makes removed criticism disappear without integrity context where disclosure is required.

## Falsification
Create a seller whose identity is verified but whose fulfillment record is poor. Falsify if the verification presentation implies operational reliability. Expire one verification source; falsify if badges persist or if the UI cannot explain which claim is no longer supported.

## Recovery
Bind every signal to explicit evidence and expiry, separate identity, quality, service, and protection claims, expose denominator/conditions, and remove unsupported prestige treatments. When evidence is insufficient, omit or qualify the signal rather than substituting generic reassurance.

## Handoff
Seller verification state comes from `designing-seller-onboarding`; moderation enforcement from listing/seller policy systems; disputes inform but do not automatically define public reputation unless policy explicitly does so.

## Output Contract
Return a `marketplace-trust-signals-contract` with `signals[]`, `evidence_sources`, `claim_boundaries`, `rating_context`, `badge_expiry_rules`, `protection_conditions`, `review_integrity_markers`, `update_evidence[]`, `falsification_cases[]`, and `recovery_actions[]`.