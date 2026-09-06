"""V13 eighth-wave independently authored rules for software pipeline."""
from __future__ import annotations

from ._capabilities import interaction_caps


PIPELINE_RULES_V13 = [{'rule_id': 'ui.pipeline.environment-target-visible',
  'domain': 'pipeline',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Delivery actions must expose the exact target environment before execution',
  'statement': 'Deploying the same artifact to development, staging, and production has different '
               'consequence; target identity must stay visible through approval and execution.',
  'intent': 'Prevent releases from being sent to the wrong environment.',
  'applies_when': ['A pipeline can deploy to multiple environments.'],
  'does_not_apply_when': [],
  'failure_modes': ['A user approves “Deploy” from a generic screen after switching context from '
                    'staging to production in another tab.'],
  'user_impacts': ['The wrong environment can receive an irreversible release.'],
  'observables': ['Switch environments around queued approvals and manual deploy actions while '
                  'inspecting request payload and audit event.'],
  'falsifiers': ['The effective environment is explicit and immutable for each approval/execution '
                 'attempt.'],
  'repairs': ['Bind every deployment attempt to a stable environment ID and surface it in '
              'confirmation and history.'],
  'exceptions': [],
  'verification': ['Race context changes against approval/deploy and verify the committed target '
                   'always equals the reviewed environment.'],
  'owner_hints': ['designing-software-delivery-pipelines'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-pipeline-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.pipeline.artifact-commit-identity-bound',
  'domain': 'pipeline',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Pipeline artifacts must remain bound to the exact source commit or revision that '
           'produced them',
  'statement': 'Branch names and tags can move; deployment review needs immutable source identity '
               'for the artifact being released.',
  'intent': 'Prevent a reviewed artifact from being confused with newer source at the same label.',
  'applies_when': ['Builds produce deployable artifacts from version-control revisions.'],
  'does_not_apply_when': [],
  'failure_modes': ['A release says “main” without commit SHA, and main advances after approval so '
                    'reviewers cannot tell which code the artifact contains.'],
  'user_impacts': ['Unreviewed code can appear to have inherited prior approval.'],
  'observables': ['Advance branches/tags after builds and inspect artifact metadata, approvals, '
                  'deploy history, and rollback.'],
  'falsifiers': ['Artifact and deployment history preserve immutable source revision identity '
                 'regardless of branch movement.'],
  'repairs': ['Record source revision/digest at build time and display that immutable identity '
              'throughout delivery.'],
  'exceptions': [],
  'verification': ['Move refs between approval and deployment and verify the deployed artifact '
                   'retains the originally built revision.'],
  'owner_hints': ['designing-software-delivery-pipelines'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-pipeline-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.pipeline.stage-dependency-state-visible',
  'domain': 'pipeline',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Pipeline stages must expose unmet, skipped, failed, and satisfied dependencies '
           'separately',
  'statement': 'A downstream stage can be absent for many reasons; collapsing dependency outcomes '
               'hides whether prerequisites actually succeeded.',
  'intent': 'Keep delivery progression and bypass decisions auditable.',
  'applies_when': ['Pipeline stages depend on tests, builds, scans, or approvals.'],
  'does_not_apply_when': [],
  'failure_modes': ['A deploy stage appears green because it was skipped when an upstream security '
                    'scan failed.'],
  'user_impacts': ['Users can mistake non-execution for successful validation.'],
  'observables': ['Exercise success, failure, skip, manual bypass, and conditional paths while '
                  'inspecting graph and summary state.'],
  'falsifiers': ['Each stage records whether it ran and why; downstream success never implies a '
                 'skipped prerequisite passed.'],
  'repairs': ['Model dependency result and execution result separately and propagate explicit '
              'skip/bypass reasons.'],
  'exceptions': [],
  'verification': ['Run representative conditional pipelines and verify every stage outcome can be '
                   'reconstructed from the graph.'],
  'owner_hints': ['designing-software-delivery-pipelines'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-pipeline-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.pipeline.approval-bound-to-artifact-version',
  'domain': 'pipeline',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Deployment approvals must bind to the artifact version actually being released',
  'statement': 'An approval becomes stale if the artifact changes after review; it must not '
               'silently transfer to a new build.',
  'intent': 'Prevent approval from authorizing unreviewed code.',
  'applies_when': ['Manual approval gates precede deployment and artifacts can be rebuilt or '
                   'replaced.'],
  'does_not_apply_when': [],
  'failure_modes': ['A production approval remains valid after the release candidate is rebuilt '
                    'with a new digest.'],
  'user_impacts': ['A different artifact can be deployed under an earlier approval.'],
  'observables': ['Approve a candidate, rebuild/repoint it, and inspect approval validity and '
                  'deploy eligibility.'],
  'falsifiers': ['Approval references immutable artifact identity and invalidates when that '
                 'identity changes.'],
  'repairs': ['Store approval as a relation to artifact digest/revision and require reapproval for '
              'any material replacement.'],
  'exceptions': [],
  'verification': ['Replace the artifact after approval and verify deployment is blocked until the '
                   'new identity is explicitly approved.'],
  'owner_hints': ['designing-software-delivery-pipelines'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-pipeline-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.pipeline.rollback-target-visible',
  'domain': 'pipeline',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Rollback actions must expose the exact prior deployment or artifact target',
  'statement': '“Rollback” is ambiguous when multiple revisions, configuration changes, or partial '
               'rollouts exist.',
  'intent': 'Prevent recovery actions from restoring an unintended state.',
  'applies_when': ['The delivery system supports rollback to earlier deployments.'],
  'does_not_apply_when': [],
  'failure_modes': ['A rollback button chooses “previous” based on latest pipeline run, which is '
                    'not the version currently active in production.'],
  'user_impacts': ['Incident response can deploy the wrong artifact and worsen an outage.'],
  'observables': ['Create interleaved deployments, failed attempts, and partial rollouts, then '
                  'inspect rollback choices.'],
  'falsifiers': ['Rollback target identifies the currently deployed predecessor or explicit '
                 'selected deployment with immutable artifact/environment identity.'],
  'repairs': ['Derive rollback candidates from authoritative deployment history, not pipeline '
              'adjacency.'],
  'exceptions': [],
  'verification': ['Exercise rollback after failed and superseded runs and verify the selected '
                   'target is exactly what becomes active.'],
  'owner_hints': ['designing-software-delivery-pipelines'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-pipeline-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.pipeline.canceled-distinct-from-failed',
  'domain': 'pipeline',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Canceled pipeline attempts must remain distinct from failed executions',
  'statement': 'Cancellation says work stopped by decision or supersession; failure says attempted '
               'work produced an error.',
  'intent': 'Prevent reliability and release decisions from treating human cancellation as system '
            'failure or vice versa.',
  'applies_when': ['Pipeline runs can be canceled before or during execution.'],
  'does_not_apply_when': [],
  'failure_modes': ['A canceled integration test stage is counted as a test failure in release '
                    'summaries.'],
  'user_impacts': ['Teams can misdiagnose system health or incorrectly block/allow release.'],
  'observables': ['Cancel queued and running stages and compare status, metrics, retry, and '
                  'downstream behavior with actual failures.'],
  'falsifiers': ['Canceled and failed attempts preserve distinct causes and downstream policy '
                 'reacts according to each.'],
  'repairs': ['Use explicit terminal outcome enums and store cancellation actor/reason separately '
              'from execution errors.'],
  'exceptions': [],
  'verification': ['Cancel and fail equivalent stages and verify summaries, retry controls, and '
                   'gates remain semantically distinct.'],
  'owner_hints': ['designing-software-delivery-pipelines'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-pipeline-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.pipeline.partial-rollout-state-visible',
  'domain': 'pipeline',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Partial rollout state must expose which targets received which artifact version',
  'statement': 'Canary or phased deployment can leave a fleet split across versions; a single '
               '“deployed” state hides real exposure.',
  'intent': 'Make partial deployment and rollback decisions evidence-based.',
  'applies_when': ['A deployment rolls out gradually across instances, regions, tenants, or '
                   'percentages.'],
  'does_not_apply_when': [],
  'failure_modes': ['The release page says production is on v2 while 70% of instances still run v1 '
                    'after a paused rollout.'],
  'user_impacts': ['Operators can make incident or compatibility decisions from a false '
                   'uniform-state assumption.'],
  'observables': ['Pause and fail phased rollouts and inspect target distribution, aggregate '
                  'status, and rollback controls.'],
  'falsifiers': ['The UI exposes rollout progress and version distribution, including '
                 'paused/failed subsets.'],
  'repairs': ['Track deployment state per rollout target and derive aggregate labels without '
              'erasing heterogeneity.'],
  'exceptions': [],
  'verification': ['Interrupt rollout at multiple percentages and verify displayed target/version '
                   'distribution matches runtime state.'],
  'owner_hints': ['designing-software-delivery-pipelines'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-pipeline-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.pipeline.retry-creates-distinct-attempt-identity',
  'domain': 'pipeline',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Pipeline retries must create distinct attempt identity while preserving lineage',
  'statement': 'A retry is a new execution with new logs/timestamps even when it reuses the same '
               'stage configuration.',
  'intent': 'Prevent new evidence from overwriting the failed attempt it is meant to replace.',
  'applies_when': ['Users can retry failed or canceled pipeline stages.'],
  'does_not_apply_when': [],
  'failure_modes': ['Retrying a test stage overwrites the original logs and makes the failed '
                    'attempt look like it passed.'],
  'user_impacts': ['Incident and quality history becomes impossible to reconstruct.'],
  'observables': ['Retry stages multiple times and inspect attempt numbers, logs, duration, '
                  'artifacts, and final summary.'],
  'falsifiers': ['Every retry has a unique attempt identity linked to its predecessor; prior '
                 'evidence remains immutable.'],
  'repairs': ['Model retry as a new attempt record and aggregate stage state without mutating '
              'historical attempts.'],
  'exceptions': [],
  'verification': ['Create several retries with different outcomes and verify each attempt remains '
                   'separately inspectable.'],
  'owner_hints': ['designing-software-delivery-pipelines'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-pipeline-owners-v13'],
  'status': 'active'}]

__all__ = ["PIPELINE_RULES_V13"]
