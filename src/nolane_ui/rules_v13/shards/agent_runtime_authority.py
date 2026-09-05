"""V13 agent runtime rules for replay, partial completion, timeout, permission, branching, correction, handoff, and side-effect evidence."""
from __future__ import annotations

from ._capabilities import interaction_caps


AGENT_RUNTIME_AUTHORITY_RULES_V13 = [
    {'rule_id': 'ui.ai.retry-shows-reused-and-changed-inputs',
     'domain': 'ai',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Agent retry controls must reveal which inputs will be reused and which have changed',
     'statement': 'Before replaying a failed or unsatisfactory agent run, the UI should distinguish preserved inputs, '
                  'newly edited instructions, changed files, refreshed external context, and regenerated tool state '
                  'rather than presenting retry as identical when it is not.',
     'intent': 'Give users a truthful mental model of replay so they can reason about whether a retry is reproduction, '
               'correction, or a materially new run.',
     'applies_when': ['An agent workflow supports retry, replay, rerun, or resume after failure while underlying '
                      'prompts, files, environment, or external data can change.'],
     'does_not_apply_when': [],
     'failure_modes': ['The retry button implies the same operation but silently reads changed workspace state or new '
                       'context that was not part of the original run.'],
     'user_impacts': ['Users can misattribute different output to agent randomness when the inputs actually changed, or '
                      'accidentally reapply stale instructions to new state.'],
     'observables': ['Run an agent, modify each input class independently, invoke retry, and compare the run packet or '
                     'evidence with the input summary shown before execution.'],
     'falsifiers': ['The retry surface identifies material reused versus refreshed inputs and any unknown external '
                    'dependencies remain explicitly unknown.'],
     'repairs': ['Persist original run inputs and compute a pre-retry delta against current context before the replay is '
                 'authorized.'],
     'exceptions': [],
     'verification': ['Test unchanged retry, edited prompt, changed files, changed permissions, refreshed web/tool '
                      'context, and resumed partial state and verify the summary matches the actual execution packet.'],
     'owner_hints': ['designing-agent-retry-and-replay-controls'],
     'verifier_hints': ['critiquing-ai-trust-and-agency'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-agent-runtime-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.ai.partial-completion-separates-committed-from-planned',
     'domain': 'ai',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Agent partial completion must separate committed side effects from unfinished planned work',
     'statement': 'When an agent stops after completing only part of a plan, the result surface must distinguish actions '
                  'already committed to external or repository state from steps that were merely planned, attempted, '
                  'skipped, or left pending.',
     'intent': 'Prevent a natural-language summary from blurring the authority boundary between what happened and what '
               'the agent still intended to do.',
     'applies_when': ['Agent runs can execute multiple tool calls or mutations and terminate through failure, '
                      'interruption, budget, cancellation, or user takeover before the plan is complete.'],
     'does_not_apply_when': [],
     'failure_modes': ['The final message summarizes the overall plan as completed or lists planned steps without '
                       'marking which side effects actually became authoritative.'],
     'user_impacts': ['Users can assume work was applied when it was not, repeat already committed effects, or overlook '
                      'a partially changed system.'],
     'observables': ['Interrupt runs after different tool-call boundaries and compare the final UI with authoritative '
                     'side-effect records and unfinished plan nodes.'],
     'falsifiers': ['Committed, failed, pending, skipped, and merely proposed steps remain explicitly distinguishable '
                    'and traceable to execution evidence.'],
     'repairs': ['Derive completion reporting from the run ledger and tool results rather than from the plan text or '
                 'model summary alone.'],
     'exceptions': [],
     'verification': ['Test cancellation before tool call, after side effect, after partial batch, and during follow-up '
                      'reasoning and verify status for every plan node and side effect.'],
     'owner_hints': ['designing-agent-partial-completion-recovery'],
     'verifier_hints': ['critiquing-ai-trust-and-agency'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-agent-runtime-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.ai.tool-timeout-distinct-from-tool-failure',
     'domain': 'ai',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Tool timeouts must remain distinct from confirmed tool failure',
     'statement': 'If an agent tool call exceeds the client wait budget without a definitive provider result, the UI '
                  'must represent that outcome as timed out or unknown rather than claiming failure when the remote '
                  'action may still complete.',
     'intent': 'Keep absence of a timely response separate from authoritative rejection so retries do not accidentally '
               'duplicate side effects.',
     'applies_when': ['Agent tools can perform remote or asynchronous operations whose final result may arrive after the '
                      'UI timeout threshold.'],
     'does_not_apply_when': [],
     'failure_modes': ['The client labels a timeout as failed and immediately offers a blind retry even though the first '
                       'operation may still be processing or may later succeed.'],
     'user_impacts': ['Users can trigger duplicate external changes or receive contradictory success and failure records '
                      'for one intended action.'],
     'observables': ['Force tool responses beyond the timeout boundary with both eventual success and eventual failure '
                     'and inspect run status, retry controls, and side-effect ledger.'],
     'falsifiers': ['Timeout remains an unresolved or explicitly timed-out state until later evidence resolves it, and '
                    'retry behavior respects operation idempotency or confirmation requirements.'],
     'repairs': ['Model timeout separately from provider failure and reconcile late results into the original tool-call '
                 'identity before permitting risky replay.'],
     'exceptions': [],
     'verification': ['Test late success, late failure, lost response, cancellable tool, and non-idempotent tool and '
                      'verify each status and retry path remains evidence-bounded.'],
     'owner_hints': ['designing-agent-tool-call-lifecycles'],
     'verifier_hints': ['critiquing-ai-trust-and-agency'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-agent-runtime-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.ai.permission-elevation-expiry-visible',
     'domain': 'ai',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Temporary agent permission elevation must expose its expiry or revocation boundary',
     'statement': 'When a user grants an agent broader tool or data authority only for a task, step, session, or bounded '
                  'time, the UI must make that elevated state visible and reconcile when it expires instead of leaving '
                  'controls that imply persistent access.',
     'intent': 'Keep temporary delegation legible so users understand when the agent can still exercise broader '
               'authority.',
     'applies_when': ['Agent permissions can be elevated temporarily beyond a lower default scope and later expire, be '
                      'revoked, or revert automatically.'],
     'does_not_apply_when': [],
     'failure_modes': ['The run surface continues showing the agent as authorized after the elevation ended, or silently '
                       'reuses the old grant for a later action.'],
     'user_impacts': ['Users can believe access ended when it did not or believe a later action is authorized when it '
                      'will actually be denied.'],
     'observables': ['Grant temporary elevation under each supported lifetime, let it expire or revoke it, and compare '
                     'visible permission state with the actual tool authorization result.'],
     'falsifiers': ['The UI shows the currently effective scope and transitions back at the same boundary enforced by '
                    'the permission authority.'],
     'repairs': ['Represent elevated grants as first-class scoped leases or session state and subscribe the UI to their '
                 'expiry and revocation events.'],
     'exceptions': [],
     'verification': ['Test one-action, one-run, timed, session, and manual revocation boundaries and verify every '
                      'subsequent tool call and permission indicator agrees.'],
     'owner_hints': ['designing-agent-tool-permission-escalation'],
     'verifier_hints': ['critiquing-security-and-privacy'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-agent-runtime-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.ai.run-branch-identity-visible',
     'domain': 'ai',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Agent run branches must have stable identity when users fork from earlier state',
     'statement': 'If users branch an agent run from a prior message, checkpoint, plan, or tool result, the new branch '
                  'must be distinguishable from the original run so later side effects and messages cannot be mistaken '
                  'as continuation of one linear history.',
     'intent': 'Preserve causal traceability across exploratory agent branches without forcing a particular visual tree '
               'design.',
     'applies_when': ['An agent experience supports forking, branching, retry-from-here, alternate plan execution, or '
                      'parallel continuation from an earlier state.'],
     'does_not_apply_when': [],
     'failure_modes': ['Branched messages and tool effects appear in the same linear history with no stable branch '
                       'identity or provenance back to the fork point.'],
     'user_impacts': ['Users can attribute side effects to the wrong branch, compare outputs against the wrong context, '
                      'or apply changes from an abandoned alternative.'],
     'observables': ['Create several branches from the same and different checkpoints, perform distinct side effects, '
                     'then inspect run IDs, branch labels, parent linkage, and result histories.'],
     'falsifiers': ['Each branch has stable identity and parent context, and side effects or messages remain '
                    'attributable to the branch that produced them.'],
     'repairs': ['Persist branch lineage in run metadata and surface branch identity wherever execution history or side '
                 'effects can otherwise become ambiguous.'],
     'exceptions': [],
     'verification': ['Test nested branching, branch rename, retry within branch, merge or accept flows where supported, '
                      'and verify causal identity remains intact.'],
     'owner_hints': ['designing-agent-run-branching'],
     'verifier_hints': ['critiquing-ai-trust-and-agency'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-agent-runtime-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.ai.human-correction-invalidates-stale-downstream-plan',
     'domain': 'ai',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Human correction of agent state must invalidate downstream plan steps that depended on the old state',
     'statement': 'When a user corrects a value, file, selection, assumption, or decision that later planned agent steps '
                  'depend on, the UI must not continue presenting those downstream steps as still valid without '
                  're-evaluating their preconditions.',
     'intent': 'Give human correction real authority over future execution rather than treating it as cosmetic '
               'annotation while stale automation proceeds.',
     'applies_when': ['Agent plans contain future steps derived from intermediate state that users can directly edit or '
                      'override before those steps execute.'],
     'does_not_apply_when': [],
     'failure_modes': ['A human changes a dependency but the original downstream steps remain queued and execute against '
                       'assumptions that are no longer true.'],
     'user_impacts': ['Users can see their correction immediately overwritten or trigger harmful actions based on a '
                      'state they explicitly fixed.'],
     'observables': ['Create plans with visible dependencies, alter upstream state before execution, and inspect which '
                     'downstream nodes remain runnable and what inputs they actually use.'],
     'falsifiers': ['Dependent steps are invalidated, regenerated, or require explicit reapproval; independent steps may '
                    'remain valid when their preconditions still hold.'],
     'repairs': ['Track plan dependencies or execution preconditions and propagate human edits through invalidation '
                 'before the scheduler authorizes downstream work.'],
     'exceptions': [],
     'verification': ['Test value edits, file replacement, target change, permission change, and manual completion of a '
                      'planned step and verify stale dependents cannot execute silently.'],
     'owner_hints': ['designing-human-correction-of-agent-state'],
     'verifier_hints': ['critiquing-ai-trust-and-agency'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-agent-runtime-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.ai.multi-agent-handoff-current-actor-visible',
     'domain': 'ai',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Multi-agent handoffs must expose which agent currently owns the active work',
     'statement': 'When work moves between specialized agents or agent instances, the UI must make the current acting '
                  'identity and handoff boundary visible enough that users can attribute new tool calls, messages, and '
                  'authority to the correct actor.',
     'intent': 'Prevent multi-agent orchestration from collapsing into one ambiguous persona when actor identity matters '
               'for context or permissions.',
     'applies_when': ['The product routes or hands off work among multiple named agents, roles, providers, or '
                      'specialized execution contexts.'],
     'does_not_apply_when': [],
     'failure_modes': ['After handoff, the interface keeps the prior actor identity or generic agent label while a '
                       'different agent begins issuing tool calls or messages.'],
     'user_impacts': ['Users can approve the wrong authority, misunderstand why context changed, or attribute an action '
                      'to an agent that did not perform it.'],
     'observables': ['Force handoffs across several agents and compare active actor label, run metadata, tool-call '
                     'attribution, permission scope, and conversation chronology.'],
     'falsifiers': ['The active actor updates at the handoff boundary and prior contributions remain attributed to their '
                    'original agent identity.'],
     'repairs': ['Carry agent identity through orchestration events and render it from execution metadata rather than '
                 'inferred conversation position.'],
     'exceptions': [],
     'verification': ['Test automatic routing, user-selected handoff, failed handoff rollback, and return to a prior '
                      'agent and verify actor attribution stays correct.'],
     'owner_hints': ['designing-multi-agent-handoff-visibility'],
     'verifier_hints': ['critiquing-ai-trust-and-agency'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-agent-runtime-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.ai.side-effect-ledger-matches-authoritative-actions',
     'domain': 'ai',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Agent side-effect ledgers must reflect authoritative actions rather than planned or merely requested ones',
     'statement': 'A side-effect history presented as what the agent changed must include only actions confirmed or '
                  'otherwise resolved by the relevant authority and must not silently omit reversals, failures, or late '
                  'outcomes.',
     'intent': 'Make the ledger an evidence surface for external change rather than a polished restatement of agent '
               'intent.',
     'applies_when': ['Agent workflows display a ledger, activity history, or summary of files changed, messages sent, '
                      'records updated, purchases made, or other external effects.'],
     'does_not_apply_when': [],
     'failure_modes': ['The ledger records a requested tool call as completed before authority confirms it, or omits a '
                       'later rollback, rejection, or compensation event.'],
     'user_impacts': ['Users can trust an audit surface that disagrees with the system of record and make recovery '
                      'decisions from false history.'],
     'observables': ['Execute successful, failed, timed-out, reversed, and partially applied side effects and compare '
                     'ledger entries with authoritative tool or provider evidence.'],
     'falsifiers': ['Every ledger entry has a truthful lifecycle and stable operation identity, including corrections or '
                    'compensation when final state changes.'],
     'repairs': ['Populate the ledger from tool-result and authority events rather than model narration, retaining '
                 'unresolved state until evidence closes it.'],
     'exceptions': [],
     'verification': ['Test late provider results, manual reversal, partial batch, duplicate retry, and external edits '
                      'and verify ledger state remains aligned with authoritative evidence.'],
     'owner_hints': ['designing-agent-side-effect-ledgers'],
     'verifier_hints': ['critiquing-ai-trust-and-agency'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-agent-runtime-owners-v13'],
     'status': 'active'},
]

__all__ = ['AGENT_RUNTIME_AUTHORITY_RULES_V13']
