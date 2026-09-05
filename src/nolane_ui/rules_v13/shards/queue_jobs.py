"""V13 sixth-wave rules; all operational prose is independently authored."""
from __future__ import annotations

QUEUE_JOBS_RULES_V13 = [{'rule_id': 'ui.jobs.queued-running-complete-distinct',
  'domain': 'jobs',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Background jobs must distinguish queued, running, and completed lifecycle states',
  'statement': 'A background task that has only entered a queue must not appear to be actively processing, and a '
               'running task must not be presented as complete until the authoritative terminal result exists.',
  'intent': 'Keep asynchronous work status aligned with the scheduler and worker lifecycle so users understand '
            'whether work has actually begun or finished.',
  'applies_when': ['The product exposes asynchronous jobs that can wait for capacity before a worker starts '
                   'execution.'],
  'does_not_apply_when': [],
  'failure_modes': ['A queued job shows active progress or success styling even though no worker has acquired it, or '
                    'a running job is marked complete before terminal output exists.'],
  'user_impacts': ['Users can wait on work that has not started, assume resources are being consumed, or depend on '
                   'results that are not final.'],
  'observables': ['Hold a job in queue, then allow execution and completion while comparing scheduler state, worker '
                  'state, and visible lifecycle labels.'],
  'falsifiers': ['Queued, running, and terminal states map to distinct authoritative events and transitions do not '
                 'advance ahead of backend evidence.'],
  'repairs': ['Model scheduler admission, execution start, and terminal result separately rather than using a single '
              'generic “processing” boolean.'],
  'exceptions': [],
  'verification': ['Exercise long queue waits, immediate execution, worker startup failure, and successful '
                   'completion and confirm visible states match each backend phase.'],
  'owner_hints': ['designing-background-task-progress'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-queue-job-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.jobs.cancel-requested-distinct-from-cancelled',
  'domain': 'jobs',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'A cancellation request must remain distinct from confirmed job cancellation',
  'statement': 'When job cancellation is asynchronous or best-effort, the UI must represent “cancellation requested” '
               'separately from a terminal cancelled state until the worker or scheduler confirms the job stopped.',
  'intent': 'Prevent users from assuming side effects cannot continue after a cancellation signal that the execution '
            'system has not yet honored.',
  'applies_when': ['Background jobs can be cancelled after execution starts and cancellation acknowledgement can be '
                   'delayed or rejected.'],
  'does_not_apply_when': [],
  'failure_modes': ['The job immediately appears cancelled when the client sends the request even though the worker '
                    'continues running and may still produce output.'],
  'user_impacts': ['Users can start conflicting work or make safety assumptions while the supposedly cancelled '
                   'process is still active.'],
  'observables': ['Request cancellation during queued, running, and finalizing phases and compare UI state with '
                  'scheduler and worker acknowledgement.'],
  'falsifiers': ['The UI stays in cancel-requested or stopping state until authoritative cancellation or completion '
                 'resolves the job.'],
  'repairs': ['Treat cancel request as an intermediate event and transition to cancelled only from scheduler or '
              'worker confirmation.'],
  'exceptions': [],
  'verification': ['Delay, reject, and race cancellation against completion and confirm the visible terminal state '
                   'always reflects the actual winner.'],
  'owner_hints': ['designing-background-task-progress'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-queue-job-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.jobs.retry-creates-attempt-under-same-job',
  'domain': 'jobs',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Retrying a failed background job must create an attempt under stable logical job identity',
  'statement': 'A retry should preserve the user-facing logical job while recording a new execution attempt, unless '
               'the user deliberately chooses to create a separate job with independent meaning.',
  'intent': 'Make job history and downstream references coherent when infrastructure failures require multiple '
            'execution attempts.',
  'applies_when': ['A failed or timed-out job can be retried with the same logical inputs and user intent.'],
  'does_not_apply_when': [],
  'failure_modes': ['Every retry creates a new top-level job indistinguishable from an intentionally separate '
                    'request, breaking history and notifications.'],
  'user_impacts': ['Users can see duplicate jobs, lose attempt lineage, or act on an older failed copy instead of '
                   'the successful retry.'],
  'observables': ['Retry one logical job multiple times and inspect identifiers, attempt history, notifications, '
                  'output references, and audit records.'],
  'falsifiers': ['The logical job remains stable while each execution attempt has its own status, timing, and '
                 'failure evidence.'],
  'repairs': ['Separate job identity from attempt identity in storage and UI and route ordinary retry through the '
              'existing logical job.'],
  'exceptions': [],
  'verification': ['Retry after deterministic failure, infrastructure timeout, and worker crash and confirm lineage '
                   'remains one job with multiple attempts.'],
  'owner_hints': ['designing-work-queues'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-queue-job-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.jobs.priority-change-effective-state-visible',
  'domain': 'jobs',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Changing job priority must reveal whether the scheduler accepted the new effective priority',
  'statement': 'If users can reprioritize queued work, the UI must distinguish a requested priority from the '
               'scheduler’s accepted effective priority when policy, quotas, or execution state can prevent the '
               'change.',
  'intent': 'Keep queue-management decisions grounded in actual scheduling state rather than optimistic local '
            'ordering.',
  'applies_when': ['A work queue lets authorized users raise, lower, or otherwise change scheduling priority while '
                   'jobs are queued or pending.'],
  'does_not_apply_when': [],
  'failure_modes': ['The interface immediately reorders a job after a priority edit even though the scheduler '
                    'rejected or ignored the requested priority.'],
  'user_impacts': ['Operators can believe urgent work moved ahead when the underlying scheduler still treats it at '
                   'the previous priority.'],
  'observables': ['Request allowed and disallowed priority changes and compare local queue order, scheduler '
                  'metadata, and effective execution order.'],
  'falsifiers': ['The UI reflects scheduler-accepted priority and shows pending or rejected changes instead of '
                 'treating local request state as authoritative.'],
  'repairs': ['Persist requested and effective priority separately and reconcile queue presentation from scheduler '
              'acknowledgement.'],
  'exceptions': [],
  'verification': ['Test policy caps, permission failures, running jobs, concurrent reprioritization, and accepted '
                   'changes and confirm visible state follows effective scheduling.'],
  'owner_hints': ['designing-work-queues'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-queue-job-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.jobs.dependency-blocked-state-visible',
  'domain': 'jobs',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Jobs waiting on dependencies must be distinguished from ordinary queue capacity waits',
  'statement': 'A job blocked by an unmet prerequisite, approval, upstream task, missing artifact, or failed '
               'dependency must expose that reason rather than appearing to wait normally for worker capacity.',
  'intent': 'Make stalled work diagnosable by separating dependency state from scheduler backlog.',
  'applies_when': ['Background work can depend on other jobs, approvals, artifacts, locks, or prerequisite state '
                   'before it becomes runnable.'],
  'does_not_apply_when': [],
  'failure_modes': ['A dependency-blocked job remains labelled queued with no indication that adding worker capacity '
                    'would not make it run.'],
  'user_impacts': ['Operators can investigate the wrong bottleneck or leave recoverable dependency failures '
                   'unresolved for long periods.'],
  'observables': ['Create jobs blocked by pending, failed, missing, and satisfied dependencies and compare visible '
                  'queue state and recovery routes.'],
  'falsifiers': ['The job exposes its blocked dependency category and transitions to runnable only when the '
                 'prerequisite becomes satisfied or explicitly bypassed.'],
  'repairs': ['Represent dependency resolution separately from queue admission and attach blocker metadata to job '
              'status.'],
  'exceptions': [],
  'verification': ['Exercise chained jobs, failed upstream tasks, manual approvals, missing artifacts, and '
                   'dependency recovery and confirm the blocker remains accurate.'],
  'owner_hints': ['designing-work-queues'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-queue-job-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.jobs.partial-output-labelled-before-completion',
  'domain': 'jobs',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Intermediate job outputs must be labelled as partial until the job reaches a compatible terminal state',
  'statement': 'If a long-running job exposes previews, partial results, logs, frames, pages, or intermediate '
               'artifacts before completion, those outputs must not be represented as final unless the job contract '
               'makes them independently authoritative.',
  'intent': 'Let users inspect useful progress without confusing provisional output with the completed deliverable.',
  'applies_when': ['Background processing emits consumable intermediate output while later stages can still change, '
                   'invalidate, or replace that output.'],
  'does_not_apply_when': [],
  'failure_modes': ['An intermediate artifact appears in the normal completed-output surface and can be mistaken for '
                    'the final result while the job is still running.'],
  'user_impacts': ['Users can download, publish, or act on incomplete results that later change or fail validation.'],
  'observables': ['Hold the job after intermediate output appears and compare labels, actions, and final artifact '
                  'identity when processing continues.'],
  'falsifiers': ['Intermediate output is explicitly partial or preview state and transitions to final only when the '
                 'job contract supports that claim.'],
  'repairs': ['Carry output completeness metadata with artifacts and gate final-result actions until the '
              'corresponding job stage is authoritative.'],
  'exceptions': [],
  'verification': ['Inspect partial output across successful completion, later failure, cancellation, and '
                   'replacement and confirm users can always distinguish finality.'],
  'owner_hints': ['designing-background-task-progress'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-queue-job-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.jobs.retry-preserves-effective-parameters',
  'domain': 'jobs',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Job retry must show the effective parameters being reused before execution',
  'statement': 'When a failed background job is retried, users should be able to determine whether the retry uses '
               'the original effective inputs, current defaults, or an edited configuration rather than assuming '
               'these are equivalent.',
  'intent': 'Preserve reproducibility when system defaults, referenced resources, or configuration can change '
            'between attempts.',
  'applies_when': ['A retryable job has parameters or references whose effective values may differ at retry time '
                   'from those used by the failed attempt.'],
  'does_not_apply_when': [],
  'failure_modes': ['Retry silently picks up new defaults or changed references while the UI presents it as the same '
                    'operation being attempted again.'],
  'user_impacts': ['Users can compare attempts incorrectly or produce a materially different result while believing '
                   'only execution reliability changed.'],
  'observables': ['Change defaults or referenced configuration after a failure, invoke retry, and compare attempt '
                  'parameter snapshots and visible review state.'],
  'falsifiers': ['Retry either reuses a recorded effective parameter snapshot or clearly previews the changed values '
                 'before a new attempt starts.'],
  'repairs': ['Persist effective parameters with each attempt and define retry semantics explicitly rather than '
              're-resolving hidden defaults without disclosure.'],
  'exceptions': [],
  'verification': ['Retry after configuration, environment, model, template, and resource changes and confirm '
                   'parameter lineage remains inspectable.'],
  'owner_hints': ['designing-background-task-progress'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-queue-job-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.jobs.queue-position-does-not-invent-precision',
  'domain': 'jobs',
  'class': 'contextual',
  'severity': 'moderate',
  'enforcement': 'warn',
  'title': 'Queue position estimates must not imply precision the scheduler cannot guarantee',
  'statement': 'If scheduling depends on priority, capacity, quotas, dependencies, preemption, or future arrivals, '
               'the UI must avoid presenting a precise “you are number N” claim unless that ordering is genuinely '
               'stable and meaningful.',
  'intent': 'Prevent users from treating a volatile scheduling hint as a contractual execution order.',
  'applies_when': ['The product exposes estimated wait position or ordering for jobs in a queue whose scheduler can '
                   'reorder work dynamically.'],
  'does_not_apply_when': [],
  'failure_modes': ['The interface shows an exact fixed queue position even though later jobs can legitimately '
                    'execute first because of scheduler policy.'],
  'user_impacts': ['Users can make timing commitments or repeatedly refresh because the displayed order suggests a '
                   'certainty the system does not possess.'],
  'observables': ['Observe displayed position while changing capacity, priority, dependencies, and incoming workload '
                  'and compare the claim with actual dispatch order.'],
  'falsifiers': ['The product shows only the level of ordering or wait estimate the scheduler can support, with '
                 'uncertainty or priority context when exact position is unstable.'],
  'repairs': ['Derive user-facing estimates from scheduler guarantees and express ranges, classes, or uncertainty '
              'instead of fabricated ordinal precision.'],
  'exceptions': [],
  'verification': ['Stress the queue with reprioritization, worker scaling, preemption, and new high-priority '
                   'arrivals and confirm the UI never overstates ordering certainty.'],
  'owner_hints': ['designing-work-queues'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-queue-job-owners-v13'],
  'status': 'active'}]

__all__ = ["QUEUE_JOBS_RULES_V13"]
