---
name: designing-monetary-input
description: Use when users enter money and the interface must preserve exact numeric intent across currencies, locale formatting, decimals, limits, and transactional review.
---

# Designing Monetary Input

## Parent Contract
**Required parent:** `designing-forms`.

This faculty owns entry and interpretation of monetary amounts. It does not decide exchange rates, fees, authorization, or transaction policy. Its responsibility is to ensure the value displayed, edited, parsed, rounded, and submitted represents the same monetary intent.

## Decision Model
A money field is a currency plus an amount, not a decorated floating-point number. Establish currency authority first: fixed by context, selected by the user, inherited from an account, or derived from the item. Make any currency change visible because the same digits can acquire a different meaning.

Accept locale-appropriate separators without making the field impossible to edit. Formatting on every keystroke can move the caret and change intermediate meaning; consider formatting on blur while preserving a stable editable representation. Minor-unit precision varies by currency and product. Do not hard-code two decimals or silently round a value when the lost precision could change a financial result.

Define zero, negative values, maximums, minimums, and empty state separately. If a fee, conversion, or tax changes the amount that will actually be charged, the input owner hands off to transactional review; the entry field must not imply that typed amount equals final debit when it does not.

## Failure Topology
- Locale `1.234,56` is parsed as `1.23456` or `123456` under a US assumption.
- Currency changes but numeric text remains, causing a large unintended value shift.
- Float arithmetic produces a displayed value different from the submitted minor units.
- Automatic grouping separators make caret edits jump unpredictably.
- A three-decimal currency is silently rounded to two decimals.
- Maximum validation fires before fees are applied, yet final transaction exceeds the allowed amount.

## Falsification and Recovery
Falsify with comma and dot decimal locales, paste containing symbols/spaces, zero-decimal and three-decimal currencies, very large values, negative adjustments where allowed, currency changes after entry, IME input, keyboard-only operation, and review of the exact submitted minor units. The design fails if two reasonable parsers could derive different amounts from the same visible field without clarification.

Recover by binding currency explicitly, parsing with locale-aware rules, representing money in precise decimal/minor-unit form, delaying nonessential formatting, surfacing rounding, and handing final-charge differences to transaction review.

## Output Contract
Return `monetary-input-contract` with currency authority, accepted notation, parse/format policy, precision and rounding rules, numeric bounds, currency-change behavior, exact storage/submission representation, review handoff, accessibility behavior, and falsification examples.