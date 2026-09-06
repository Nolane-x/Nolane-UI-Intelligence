"""V13 eighth-wave independently authored rules for build artifacts."""
from __future__ import annotations

from ._capabilities import interaction_caps


BUILD_ARTIFACT_RULES_V13 = [{'rule_id': 'ui.buildartifact.build-status-distinct-from-artifact-availability',
  'domain': 'buildartifact',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Build success must remain distinct from artifact availability',
  'statement': 'A build can succeed while artifact upload, signing, retention, or publication '
               'fails separately.',
  'intent': 'Prevent users from assuming a successful build guarantees a usable artifact.',
  'applies_when': ['Build jobs produce downloadable or deployable artifacts through a later '
                   'publishing step.'],
  'does_not_apply_when': [],
  'failure_modes': ['The job badge is green but the artifact upload failed and the download link '
                    'returns 404.'],
  'user_impacts': ['Release workflows can proceed on evidence that the required deliverable does '
                   'not exist.'],
  'observables': ['Independently fail compile/test and artifact upload/publish steps while '
                  'inspecting build and artifact status.'],
  'falsifiers': ['Build outcome and artifact availability have separate states and neither implies '
                 'the other without evidence.'],
  'repairs': ['Track artifact publication as its own lifecycle tied to the build attempt.'],
  'exceptions': [],
  'verification': ['Exercise successful build with failed artifact upload and failed build with '
                   'partial artifacts, verifying both dimensions stay explicit.'],
  'owner_hints': ['designing-build-status-and-artifacts'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-build-artifact-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.buildartifact.log-chunk-order-stable',
  'domain': 'buildartifact',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Build logs must preserve stable ordering when streamed in chunks',
  'statement': 'Parallel workers and delayed network delivery can reorder log chunks; display '
               'order should follow authoritative sequence/time semantics.',
  'intent': 'Keep diagnostic evidence from being misleading or impossible to follow.',
  'applies_when': ['Build logs stream incrementally from one or more workers.'],
  'does_not_apply_when': [],
  'failure_modes': ['A delayed chunk from step 2 appears after step 5 with no sequence context, '
                    'making errors look causally reversed.'],
  'user_impacts': ['Engineers can chase the wrong root cause.'],
  'observables': ['Delay and reorder emitted log chunks from parallel steps while inspecting '
                  'timestamps, sequence markers, and final log.'],
  'falsifiers': ['Rendered log order is stable within defined streams and cross-stream '
                 'interleaving preserves explicit provenance.'],
  'repairs': ['Attach sequence/stream identity to log chunks and order deterministically rather '
              'than by client arrival.'],
  'exceptions': [],
  'verification': ['Replay logs under randomized delivery order and verify final rendered evidence '
                   'is deterministic and traceable.'],
  'owner_hints': ['designing-build-status-and-artifacts'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-build-artifact-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.buildartifact.retention-expiry-visible',
  'domain': 'buildartifact',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Artifact retention and expiry must be visible before downloads disappear',
  'statement': 'Short-lived build artifacts can vanish while links and release references remain; '
               'retention boundary should be explicit.',
  'intent': 'Prevent users from relying on an artifact that will expire unexpectedly.',
  'applies_when': ['Build artifacts are subject to retention or cleanup policy.'],
  'does_not_apply_when': [],
  'failure_modes': ['A test bundle link works today and disappears tomorrow with no prior '
                    'indication of its seven-day retention.'],
  'user_impacts': ['Teams can lose debugging evidence or fail recovery after the artifact '
                   'expires.'],
  'observables': ['Create artifacts with different retention policies and inspect list, detail, '
                  'notifications, and post-expiry state.'],
  'falsifiers': ['Artifact expiry time/policy is visible and expired artifacts transition to an '
                 'explicit unavailable state.'],
  'repairs': ['Persist retention metadata with artifact identity and expose it wherever the '
              'artifact is referenced.'],
  'exceptions': [],
  'verification': ['Advance across expiry and verify links, status, and cleanup behavior converge '
                   'without phantom availability.'],
  'owner_hints': ['designing-build-status-and-artifacts'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-build-artifact-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.buildartifact.test-shard-aggregation-consistent',
  'domain': 'buildartifact',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Sharded test summaries must reconcile every shard outcome before reporting a suite '
           'result',
  'statement': 'Parallel test shards can finish, retry, or disappear independently; aggregate '
               'pass/fail must account for all expected shards.',
  'intent': 'Prevent incomplete test execution from being reported as a passing suite.',
  'applies_when': ['A test suite runs across multiple shards or workers.'],
  'does_not_apply_when': [],
  'failure_modes': ['Nine of ten shards pass while one never reports, but the dashboard shows '
                    '“100% passed” from completed shards only.'],
  'user_impacts': ['Bad code can be released because missing execution was treated as success.'],
  'observables': ['Drop, retry, and delay individual shards and compare expected shard count, '
                  'aggregate summary, and detailed results.'],
  'falsifiers': ['Aggregate status distinguishes all-pass from missing/pending/failed shards and '
                 'reconciles to the expected shard set.'],
  'repairs': ['Track expected shard identities and compute suite outcome only after all required '
              'shards reach an allowed terminal state.'],
  'exceptions': [],
  'verification': ['Simulate missing and retried shards and verify the aggregate never reports '
                   'pass prematurely.'],
  'owner_hints': ['designing-build-status-and-artifacts'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-build-artifact-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.buildartifact.flaky-retry-distinguished',
  'domain': 'buildartifact',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Flaky-test retries must remain distinguishable from clean first-attempt passes',
  'statement': 'A test that passes only after retry provides different quality evidence than one '
               'that passed immediately.',
  'intent': 'Prevent retry policy from hiding instability behind an all-green summary.',
  'applies_when': ['Test infrastructure automatically retries failed tests.'],
  'does_not_apply_when': [],
  'failure_modes': ['A test fails twice and passes on the third attempt, but the final report '
                    'shows a plain green check with no retry evidence.'],
  'user_impacts': ['Teams can underestimate flakiness and release risk.'],
  'observables': ['Run deterministic pass, deterministic fail, and retry-pass cases and inspect '
                  'summary, individual test history, and metrics.'],
  'falsifiers': ['Retry-pass state preserves failed attempts and is separately countable from '
                 'clean pass.'],
  'repairs': ['Store every test attempt and derive final status without discarding retry history.'],
  'exceptions': [],
  'verification': ['Trigger known flaky tests and verify reports expose attempt sequence and '
                   'aggregate flaky counts.'],
  'owner_hints': ['designing-build-status-and-artifacts'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-build-artifact-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.buildartifact.cache-hit-not-success-proof',
  'domain': 'buildartifact',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'A build cache hit must not be presented as independent proof that a build step '
           'succeeded',
  'statement': 'Cache reuse says output was reused under a key; it does not by itself prove the '
               'current source/config was correctly represented or revalidated.',
  'intent': 'Prevent cache metadata from being mistaken for fresh execution evidence.',
  'applies_when': ['Build steps can reuse cached outputs.'],
  'does_not_apply_when': [],
  'failure_modes': ['A compilation step displays a green “success” solely because an old cache '
                    'entry was restored, while the cache key omitted a changed compiler flag.'],
  'user_impacts': ['Users can trust stale artifacts that were never rebuilt under the current '
                   'inputs.'],
  'observables': ['Alter cache-relevant and cache-omitted inputs and inspect cache key, '
                  'execution/skipped state, and artifact provenance.'],
  'falsifiers': ['The UI distinguishes executed success from cache reuse and exposes enough '
                 'key/provenance to audit the reuse decision.'],
  'repairs': ['Model cache-hit as an execution mode with source key metadata, not as a substitute '
              'for step result evidence.'],
  'exceptions': [],
  'verification': ['Force valid and invalid cache reuse scenarios and verify summaries never '
                   'equate hit alone with fresh success.'],
  'owner_hints': ['designing-build-status-and-artifacts'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-build-artifact-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.buildartifact.download-checksum-visible',
  'domain': 'buildartifact',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Downloaded build artifacts must expose a checksum or equivalent immutable integrity '
           'identity',
  'statement': 'A filename is not enough to prove that a downloaded artifact matches the reviewed '
               'build output.',
  'intent': 'Allow consumers to verify artifact integrity and identity across transport.',
  'applies_when': ['Artifacts are downloaded or handed to another release/security process.'],
  'does_not_apply_when': [],
  'failure_modes': ['Two builds both publish app.zip and the consumer cannot tell which bytes were '
                    'downloaded.'],
  'user_impacts': ['The wrong or corrupted artifact can be deployed while appearing nominally '
                   'correct.'],
  'observables': ['Publish same-named artifacts from different builds and inspect download '
                  'metadata and integrity verification.'],
  'falsifiers': ['Each downloadable artifact has an immutable digest or equivalent identity tied '
                 'to its build attempt.'],
  'repairs': ['Compute and persist digest after final artifact creation and expose it with '
              'download metadata.'],
  'exceptions': [],
  'verification': ['Download artifacts repeatedly and verify their digest matches the build record '
                   'and differs when bytes differ.'],
  'owner_hints': ['designing-build-status-and-artifacts'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-build-artifact-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.buildartifact.branch-commit-association-stable',
  'domain': 'buildartifact',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Build history must keep branch labels separate from immutable commit identity',
  'statement': 'Branches move over time; historical builds need the exact revision they ran, not a '
               'branch name re-resolved later.',
  'intent': 'Preserve reproducible linkage between build evidence and source code.',
  'applies_when': ['Builds are triggered from mutable branches or tags.'],
  'does_not_apply_when': [],
  'failure_modes': ['A build from main is viewed a day later and its source link opens current '
                    'main instead of the commit that was tested.'],
  'user_impacts': ['Engineers can review or deploy source that differs from the build evidence.'],
  'observables': ['Advance and force-update refs after builds and inspect source links, compare '
                  'views, and artifact metadata.'],
  'falsifiers': ['Historical builds retain immutable commit/revision identity while branch/tag '
                 'labels are shown only as contextual refs.'],
  'repairs': ['Store resolved revision at trigger time and use it for all historical source '
              'links.'],
  'exceptions': [],
  'verification': ['Move refs after build completion and verify every historical build still opens '
                   'the exact tested revision.'],
  'owner_hints': ['designing-build-status-and-artifacts'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-build-artifact-owners-v13'],
  'status': 'active'}]

__all__ = ["BUILD_ARTIFACT_RULES_V13"]
