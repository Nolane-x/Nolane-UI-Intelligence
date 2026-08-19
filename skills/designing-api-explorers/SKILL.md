---
name: designing-api-explorers
description: Use when developers inspect and execute API operations and the interface must coordinate endpoint identity, parameters, authentication context, request construction, response evidence, environments, history, and destructive-call safety.
---

# Designing API Explorers

## Parent Contract
**Required parent:** `designing-data-dense-interfaces`.

This faculty owns interactive API inspection and request execution. It does not own the API specification itself, secret storage, or environment administration. The explorer must make the exact operation and execution context auditable enough that developers can understand what will be sent before a request crosses a real service boundary.

## Decision Architecture
Represent operation identity from the protocol: method + path for HTTP, procedure for RPC, operation for GraphQL, or equivalent. Separate path/query/header/body/auth inputs according to semantics rather than placing everything in one generic key-value grid. Requiredness, type, enum, examples, defaults, and deprecated status should come from authoritative schema when available.

Execution context must be prominent. Base URL/environment, authentication identity, headers inherited from workspace configuration, and variable substitution can change consequences without changing the visible endpoint. Show resolved values safely while redacting secrets. For destructive or production calls, add consequence-aware friction based on method/domain semantics rather than assuming every POST is dangerous and every GET is safe.

Response inspection should preserve status, duration, headers, body, schema validation, truncation, and request correlation. Large/binary responses need alternate viewers. Request history must distinguish templates from actual executions and avoid persisting secrets in copied commands, logs, URLs, or exportable history.

## Failure Topology
- Developer thinks request targets staging while a hidden environment variable resolves production base URL.
- Authorization header appears in copied cURL command and leaks into issue trackers.
- One generic parameter table loses distinction between query arrays, headers, and structured body.
- Retrying a destructive request after timeout creates duplicate resources because outcome is unknown.
- Large response freezes the UI because full JSON is syntax-highlighted eagerly.
- Schema marks a field deprecated but explorer silently continues presenting it as recommended.

## Falsification and Recovery
Falsify with production/staging switch, expired credentials, path variables, multipart upload, huge/binary response, timeout with unknown outcome, schema mismatch, deprecated operation, keyboard-only request construction, and copied/exported examples. The design fails if users cannot reconstruct the exact resolved request context or if secret material crosses into ordinary history/export surfaces.

Recover by showing environment/auth context beside execution, type-aware parameter editors, resolved-request preview with redaction, destructive-call confirmation tied to operation risk, bounded response rendering, and secret-safe history with correlation IDs.

## Output Contract
Return `api-explorer-contract` with operation model, parameter editors, environment/auth context, variable resolution, request preview, execution-risk gates, response viewers, history/redaction rules, performance limits, accessibility operation, and falsification cases.