---
name: designing-security-operations-handoffs
description: Use when security investigations, monitoring responsibility, or incident context passes between analysts or shifts and unresolved risk, evidence, actions, and assumptions must survive the transition.
---
# Designing Security Operations Handoffs

## Parent Contract

**Required parent:** `designing-security-operations-workspaces`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the transition contract when security work moves from one analyst, team, shift, region, or function to another. Decide what must be summarized versus linked, how unresolved questions and pending actions are represented, which deadlines or watch conditions travel with the work, and how the receiver acknowledges ownership without implying that every statement is verified. This faculty is not generic assignment UX: it protects operational continuity when incomplete security reasoning crosses a human boundary.

## Inputs and evidence

Require current investigation or queue state, named owner and receiving role, severity and urgency, affected entities, scope boundaries, evidence references, working hypotheses with confidence, actions already taken, action outcomes, pending commands, blocked steps, external dependencies, communication commitments, watch conditions, deadlines, escalation state, and access restrictions. Include handoffs with partial telemetry, pending endpoint isolation, unreviewed alerts, conflicting analyst interpretations, overnight monitoring, region-specific access, and receivers who cannot view every referenced artifact.

## Procedure

Construct the handoff from durable state, not a freeform chat recap. Separate verified facts, working interpretation, actions completed, actions still in flight, decisions deferred, and questions requiring follow-up. Link evidence rather than copying lossy summaries, but provide enough context that the receiver can judge priority before opening every artifact. Preserve timestamps and actor identity for critical statements. Make pending destructive or time-sensitive actions prominent; a queued isolation command or expiring access token must not disappear below narrative notes. Include explicit “what would change the assessment” watch conditions so monitoring has a purpose. The receiver should acknowledge acceptance, record any reinterpretation, and be able to decline or escalate if permissions, capacity, or evidence access are inadequate. Handoff completion must not automatically close the sender's unresolved tasks unless ownership truly transfers.

## Failure topology

- The handoff is a prose note that omits which statements are evidence versus hypothesis.
- A pending containment command is summarized as if it already succeeded.
- The receiver gets ownership but lacks access to the linked case or telemetry.
- Time-sensitive watch conditions are lost because only current status is transferred.
- The sender's filters and investigation time window disappear, forcing reconstruction.
- Receiver acknowledgment is treated as agreement with every prior conclusion.
- Multiple partial handoffs create duplicate owners and contradictory action plans.

## Falsification

Hand off a live investigation containing one confirmed fact, two hypotheses, a pending endpoint action, missing telemetry, an external dependency, a deadline, and evidence the receiver cannot initially access. Then have the receiver reinterpret one hypothesis and escalate another task. The design fails if action state is ambiguous, inaccessible evidence is invisible, ownership cannot be reconciled, or the second analyst cannot state what still needs watching and why.

## Output contract

Return `security-operations-handoffs-contract` containing transfer scope, fact-versus-hypothesis structure, evidence links, completed/in-flight/pending action states, watch conditions, deadline and escalation semantics, access verification, sender/receiver ownership, acknowledgment rules, reinterpretation history, and handoff reconstruction scenarios.

## Handoffs

Durable evidence remains governed by `designing-security-case-evidence-management`; incident-specific command authority may route to incident-response faculties; assignment primitives can reuse `designing-assignment-and-ownership`. This skill owns the semantic integrity of the transition itself and must preserve enough context for the receiving analyst to continue without silently inheriting stale assumptions.