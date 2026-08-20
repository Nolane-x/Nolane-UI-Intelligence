---
name: designing-market-watchlists
description: Own user-curated monitoring lists of financial instruments with identity, quote freshness, selected metrics, sorting, alerts, grouping, stale/closed-market state, and neutral non-advisory presentation.
---
# Designing Market Watchlists

## Decision ownership

Own monitoring and organization of instruments the user has chosen to observe. Decide add/remove/search identity, groups/lists, quote fields, freshness, market-session state, sorting, alerts/notes, compact density, and navigation to analysis/order entry. This owner does not rank or recommend instruments unless a separate authorized recommendation product exists.

## Inputs and evidence

Require instrument master, symbols/venues/currencies, quote data/timestamps, market sessions, selected metrics, user lists, alert rules, permissions/data entitlements, and mobile/dense requirements. Identify duplicate symbols across venues and delayed data entitlements.

## Procedure

Disambiguate instruments using symbol plus venue/name/currency. Quote values always carry freshness/session context at appropriate level. Closed-market, delayed, stale, and missing data differ. User-selected columns/sorts persist per list but active sort must remain visible so movement is explainable. Alerts need condition, source data basis, state, and history. Grouping may reflect user purpose without implying portfolio ownership. Percent change needs reference basis such as prior close. Avoid color-only up/down and avoid default sorting that implies "best" investments.

## Failure topology

Failures include same ticker from wrong venue, delayed data looking real-time, percent change with unknown baseline, stale rows sorted among live rows as comparable, alerts firing on bad/missing data, and green/red movement treated as a recommendation. Another failure is removing an instrument and silently deleting associated alert history.

## Falsification

Reject if instrument identity or quote freshness cannot be recovered; if closed/delayed/stale states are conflated; if percent-change basis is unknown; if active sorting is hidden; if alerts lack data/time evidence; if list ranking is labeled as desirability; or if removing a row destroys related records without disclosure.

## Output contract

Return a `market-watchlists-contract` with: list/group identity; instrument disambiguation; quote fields/source/freshness; session state; percent-change basis; sort/filter; user columns; alerts/notes; missing/stale behavior; removal consequences; and non-advisory language. Include one duplicate-symbol venue scenario.

## Handoffs

Order entry consumes a user-selected instrument but re-confirms identity, order-book interfaces provide market depth, portfolio positions remain separate from watch membership, and notification systems deliver configured alerts.