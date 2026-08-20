---
name: designing-tax-category-mapping
description: Own administrative mapping of products, expenses, accounts, jurisdictions, rates, exemptions, tax codes, and effective dates with provenance and change impact without providing tax advice.
---
# Designing Tax Category Mapping

## Decision ownership

Own the interface that maps operational/accounting records to externally or internally defined tax categories/codes. Decide mapping source, jurisdiction/entity scope, effective dates, category/code identity, exemptions, override provenance, unmapped exceptions, and downstream impact. This owner does not determine which legal tax treatment is correct; authoritative tax policy/data remains external.

## Inputs and evidence

Require tax-code catalog/provider/version, jurisdictions, entities/registrations, account/product/expense dimensions, effective dates, exemptions/certificates, rate/source metadata if shown, transaction usage, permissions, and filing/report dependencies. Identify provider updates and conflicting mappings.

## Procedure

Bind mappings to authoritative code identity plus version/effective period. Show scope clearly: entity, jurisdiction, product/category/account, and transaction type. Unmapped or conflicting records remain visible as exceptions rather than defaulting silently. Overrides require actor/reason and, where appropriate, supporting authority. Provider/catalog updates should produce a diff and migration review rather than automatically remapping historical transactions. Historical transactions retain the mapping/rule effective at posting unless accounting policy explicitly restates them.

## Failure topology

Failures include a tax rate displayed without jurisdiction/source, category updates rewriting history, unknown items mapped to a default taxable code silently, exemptions with no expiry/document, and users assuming a UI suggestion is tax advice. Another failure is one mapping applied across legal entities with different registrations unnoticed.

## Falsification

Reject if mapping source/version/effective date is unknown; if unresolved records can silently receive a default; if overrides lack rationale; if catalog updates mutate historical classification invisibly; if jurisdiction/entity scope is ambiguous; or if UI copy presents suggested mapping as legal determination.

## Output contract

Return a `tax-category-mapping-contract` with: authoritative catalog/source/version; entity/jurisdiction scope; operational selector; tax code/category; effective dates; exemptions/evidence; unmapped/conflict queue; override provenance; update/migration behavior; historical preservation; and explicit non-advice boundary. Include one provider-code migration scenario.

## Handoffs

Expense/AP/journal workflows consume mappings, chart of accounts supplies dimensions, statements/filings consume recorded tax data, and authority research/legal policy remains outside this skill.