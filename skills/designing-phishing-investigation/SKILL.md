---
name: designing-phishing-investigation
description: Use when analysts investigate suspicious messages and campaigns and must connect sender identity, delivery path, content, URLs, attachments, recipients, user actions, and remediation without destroying evidence provenance.
---
# Designing Phishing Investigation

## Decision ownership

Own the investigative surface for phishing and malicious-message analysis. Decide how message headers, sender identity, authentication results, routing path, body content, links, attachments, delivery status, recipient scope, user interactions, and campaign relationships are assembled into one review. This faculty does not perform malware reverse engineering and does not own general email client design. It exists to help analysts distinguish spoofing, account compromise, malicious infrastructure, benign bulk mail, and user exposure while preserving the original artifact.

## Inputs and evidence

Require raw message identity, headers, envelope sender, display sender, SPF/DKIM/DMARC or equivalent authentication evidence, relay chain, subject/body, URLs, attachment metadata and hashes, delivery actions, recipient list, mailbox location, click/open/download telemetry, reported-by-user context, sender history, domain age/reputation where available, quarantine/remediation status, and related messages. Include forwarding, mailing lists, display-name spoofing, compromised trusted accounts, URL rewriting, password-protected archives, image-only messages, and messages already removed before investigation.

## Procedure

Preserve the original message as immutable evidence and render normalized views as derived layers. Make sender identities explicit: display name, visible address, envelope sender, authenticated domain, and sending infrastructure may disagree. Show authentication outcomes with the exact domain or identifier they validate; a passing DKIM signature does not mean the display sender is trusted. Extract links and attachments into inspectable inventories, indicating rewritten versus original URLs and whether content was detonated, scanned, or unavailable. Summarize recipient exposure by delivered, blocked, opened, clicked, credential-submitted, attachment-opened, and unknown when telemetry supports those states. Correlate related messages through explainable shared features, not visual resemblance alone. Make remediation state—quarantined, deleted, blocked sender/domain, reset credentials, revoked sessions—auditable per recipient or scope.

## Failure topology

- The interface highlights the display sender and hides conflicting envelope/authentication identity.
- A green authentication badge is interpreted as “safe message.”
- URL rewriting destroys the original link analysts need to investigate.
- Campaign grouping merges unrelated newsletters because subject lines are similar.
- “No click” is shown when click telemetry is simply unavailable.
- Removing messages from mailboxes is summarized as success despite failed or offline recipients.
- Opening an attachment preview mutates or executes the original evidence artifact.

## Falsification

Investigate a display-name spoof, a malicious message from a compromised legitimate account, a rewritten tracking URL, an attachment unavailable for scanning, a campaign with partial recipient telemetry, and a remediation action that fails for one mailbox. The design fails if analysts cannot recover the original message facts, distinguish identity layers, or tell exposure unknown from exposure negative.

## Output contract

Return `phishing-investigation-contract` containing message identity model, sender/authentication layers, immutable artifact handling, URL/attachment extraction, recipient-exposure states, campaign-correlation evidence, remediation tracking, telemetry uncertainty, and phishing investigation scenarios.

## Handoffs

Attachment execution results route to `designing-malware-analysis-result-views`; IOC pivots route to `designing-indicator-of-compromise-search`; credential/session consequences route to authentication and identity specialists; case preservation routes to `designing-security-case-evidence-management`. Generic messaging UI does not own phishing evidence semantics.