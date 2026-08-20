---
name: designing-ci-job-log-navigation
description: Own navigation and diagnosis inside long CI job logs, including step boundaries, timestamps, folding, search, annotations, failure focus, retries, and secret-safe output.
---
# Designing CI Job Log Navigation

## Decision ownership

Own the delivery-specific log-reading experience for build/test/deploy jobs. Decide step segmentation, current/failure focus, streaming state, fold/search behavior, timestamps, annotations, retry links, downloadable raw logs, and treatment of secret redaction. Generic log viewers supply baseline mechanics; this owner binds logs to pipeline jobs and actionable diagnosis.

## Inputs and evidence

Require job/step structure, log streaming protocol, line volume, annotations, timestamps, exit status, retry/rerun model, secret-masking behavior, encoding, and retention. Inspect failures where the causal line occurs well before the final exit message.

## Procedure

Keep job and step identity persistent. Automatically focus the first meaningful failure annotation where reliable, but let users return to chronological context. Collapse successful/noisy steps by default only if their presence/count is clear. Search must include streamed and retained content with result navigation. Preserve ANSI/structured emphasis safely, and expose raw text when formatting obscures evidence. Redacted secrets need a clear placeholder that does not reveal length/value. Retrying from a log should state whether it reruns the job, stage, or whole pipeline.

## Failure topology

Failures include jumping only to the final "exit 1" line, log streaming that moves the viewport while users inspect older lines, secret masking that leaks fragments, collapsed steps hiding warnings, search missing not-yet-loaded history, and retry buttons whose scope is ambiguous. Another failure is loss of log retention with no expiry notice.

## Falsification

Reject if users cannot stop auto-follow while streaming; if failure annotations cannot reveal surrounding lines; if retry scope is unknown; if redaction leaks sensitive tokens; if search covers only rendered lines; if a folded step with relevant warnings appears clean; or if raw logs expire without disclosed retention.

## Output contract

Return a `ci-job-log-navigation-contract` with: job/step hierarchy; streaming/follow behavior; failure focus; folding rules; search coverage; timestamps/annotations; raw-log access; secret redaction; retention; retry/rerun links; and context preservation. Include one early-root-cause/late-exit case.

## Handoffs

Pipeline stage visualization provides job context, deployment-failure diagnosis consumes evidence, and generic log viewer handles reusable rendering/search primitives.