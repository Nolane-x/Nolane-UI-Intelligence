---
name: designing-listing-moderation-workflows
description: Use when marketplace listings can be drafted, submitted, reviewed, restricted, rejected, appealed, edited, or removed and sellers and moderators need exact policy, evidence, revision, and publication state.
---

# Designing Listing Moderation Workflows

Listing moderation is a policy adjudication workflow over a versioned commercial artifact. The interface must distinguish whether a listing is unpublished because the seller has not submitted it, because automated review is pending, because a moderator restricted it, or because a previous published revision remains live while changes are reviewed.

## Parent Contract
**Required parent:** `designing-marketplace-operations`.

The parent owns marketplace roles and transaction boundaries. This skill owns listing revision, review, enforcement, reason, appeal, and publish-state semantics.

## Listing Revision Model
Track draft revision, submitted revision, reviewed revision, and live revision separately when asynchronous moderation permits them to diverge. A seller editing a live listing should know whether changes take effect immediately or create a pending revision while the old version remains purchasable.

Policy findings should bind to exact content/attributes and policy categories. “Listing rejected” without identifying the problematic element prevents meaningful correction. Where policy or safety requires limited disclosure, still distinguish correctable content issue, prohibited category, verification requirement, suspected abuse, and system error.

## Moderator Workflow
Moderators need evidence, listing history, seller context permitted by policy, prior enforcement, decision options, and reason templates without losing independent judgement. High-impact actions such as permanent removal or seller restriction should show scope and downstream consequences before commit.

Appeals or seller corrections should create linked cases, not erase the original moderation decision. Preserve timestamps, actors, evidence, and which revision was under review.

## Evidence
Test automated hold, human review, seller correction while review is pending, live-revision replacement, prohibited item, false positive, appeal, policy update, and seller suspension. Verify buyer visibility matches the exact live revision and state.

## Failure Modes
- Draft, pending, rejected, and removed all look like “inactive.”
- Seller edits a rejected listing but the platform reviews the wrong revision.
- Policy reason is too vague to support correction or appeal.
- Moderator action scope is unclear and removes unrelated listings.
- Appeal overwrites the original decision history.
- Buyer sees an unreviewed revision while seller UI says it is pending.

## Falsification
Keep revision A live, submit revision B for review, reject B, and allow seller correction C. Falsify if any screen cannot state which revision is live, under review, or rejected, or if an appeal loses the evidence associated with B.

## Recovery
Rebind moderation events to immutable listing revisions, restore live/pending separation, expose actionable reason categories, and preserve appeal lineage. If review state is unknown, prevent publication changes until the canonical moderation record is retrieved.

## Handoff
Seller eligibility is owned by `designing-seller-onboarding`; buyer-facing trust representation by `designing-marketplace-trust-signals`; inventory availability is separate from moderation and belongs to marketplace inventory.

## Output Contract
Return a `listing-moderation-workflows-contract` with `listing_revision_states[]`, `live_pending_relationship`, `policy_findings[]`, `moderator_actions[]`, `decision_scope`, `appeal_lineage`, `buyer_visibility_rules`, `evidence_cases[]`, `falsification_cases[]`, and `recovery_actions[]`.