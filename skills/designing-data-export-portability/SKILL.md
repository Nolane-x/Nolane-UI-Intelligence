---
name: designing-data-export-portability
description: Use when users request a portable copy of account or workspace data and the interface must define scope, identity verification, preparation, format, sensitive-content warnings, delivery, expiry, retry, and current policy authority.
---

# Designing Data Export Portability

## Parent Contract
**Required parent:** `designing-privacy-sensitive-interfaces`.

This faculty owns the product flow for assembling and delivering a user-requested data export. It does not decide legal portability rights, response deadlines, mandatory format, or eligible data categories from memory; those obligations require current authoritative verification. It also does not treat a database dump as automatically useful or safe portability.

## Decision Architecture
Define export scope in user terms: profile/account data, authored content, transaction history, activity, uploaded media, workspace data the requester is authorized to export, or other product-specific categories. Distinguish data belonging to the requester from third-party, organization-owned, security-sensitive, or legally restricted material. If several scopes or formats exist, show their practical difference before starting the request.

Exports are commonly background jobs. Represent requested, verifying, preparing, partially available if supported, ready, expired, failed, cancelled, and downloaded states as evidence allows. Reauthentication may be required because the result can contain highly sensitive data. The download destination should use short-lived, authenticated or capability-bounded access and should not expose the archive through a permanent public URL.

Format needs interpretability. Machine-readable JSON/CSV, original files, and human-readable summaries serve different portability purposes. Include schema/readme metadata where needed so exported identifiers and timestamps are understandable. Large exports may be split into parts; preserve checksum/part identity if integrity matters. Warn users that once downloaded, the archive leaves the product's protection boundary.

## Failure Topology
- Export includes organization records the user can view but is not authorized to extract wholesale.
- “Download my data” starts a synchronous browser request that times out on a large account.
- Ready archive uses a permanent predictable URL and remains accessible months later.
- CSV contains ambiguous IDs/timestamps with no schema/context.
- Export job fails halfway but UI only says “Something went wrong” and users do not know whether any archive exists.
- Product promises inclusion/exclusion categories based on outdated legal assumptions rather than current verified policy.

## Falsification and Recovery
Falsify with large account, multi-workspace membership, permission-limited organizational data, identity re-verification, export prepared while user is offline, expired link, partial generation failure, archive with media plus structured data, screen-reader request/status flow, and policy changes affecting scope. The design fails if export scope cannot be explained from current authority or if archive access persists beyond the stated security boundary.

Recover by current-policy verification, explicit scope authorization, background job identity, secure expiring delivery, interpretable formats/schema, partial/failure status, reauthentication, and clear post-download security guidance.

## Output Contract
Return `data-export-portability-contract` with authority-verification obligations, export scope, requester authorization, verification steps, job lifecycle, format/schema package, archive security/expiry, large/partial export behavior, retry/cancel, post-download warnings, accessibility status, and falsification cases.