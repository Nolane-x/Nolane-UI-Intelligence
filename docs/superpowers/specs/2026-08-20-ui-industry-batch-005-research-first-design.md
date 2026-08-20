# UI Industry Batch 005 — Research-First 100-Skill Design

Date: 2026-08-20
Baseline: 674 canonical skills on `main`.
Target: exactly 100 newly admitted canonical skills, producing a 774-node graph only if every node survives ownership review.

## Objective

Expand NUI into under-covered UI domains without numerical inflation. Batch 005 is not allowed to reuse canonical prose or the fixed inventory/prose from closed PR #19. The batch is research-first: candidate concepts are admitted because they own a material decision and failure class, not because a quota needs filling.

## Non-negotiable authorship rule

Every new `SKILL.md` body is individually authored. No loop, macro, template expander, Cartesian product, noun substitution, bulk prose transformation, LLM batch prompt, or programmatic body generator may create or rewrite canonical skill prose. Shared repository headings are protocol only. Automation is allowed only for deterministic bookkeeping: graph insertion, count checks, provenance indexing, collision detection, hash/checksum work, parent-chain validation, and tests.

## Admission court

A candidate is canonical only when all of the following are true:

1. the trigger is independently recognizable;
2. it owns a material decision not fully settled by its parent;
3. its boundary against siblings is explicit;
4. it has characteristic state/invariants or domain semantics;
5. it has characteristic failure topology;
6. its recommendations can be falsified against runtime, render, user, or authoritative evidence;
7. it defines recovery after falsification;
8. it produces a bounded output contract useful downstream;
9. it does not collide with any existing output;
10. source evidence establishes a mechanism rather than copying trade dress.

If a candidate fails ownership review, it is removed. Replacement candidates must independently pass the same court; no cosmetic backfill is permitted.

## Research courts and counts

- Mobile-native application shells and lifecycle: 10
- Visual application builders: 12
- Business-intelligence workspaces: 12
- Clinical-care workflows: 14
- Public-service experiences: 10
- Marketplace operations: 10
- Realtime communications: 10
- Spatial/XR specialists under the existing `designing-spatial-xr-interfaces` owner: 10
- Recommendation/personalization: 6
- Design-to-code handoff: 6

Total: 100.

These counts are integration boundaries, not prose templates. The courts deliberately have different sizes because the admitted decision surface differs by domain.

## Source posture

Research uses strong current repositories and authoritative standards as evidence. Repositories are classified as normative/authoritative, mature-system corroboration, mechanism implementation, domain evidence, or discovery-only. External code, brand composition, naming systems, and trade dress are not copied into NUI.

Priority source families for this batch include React Navigation / Expo / React Native ecosystems; Penpot / Webstudio / GrapesJS / Plasmic / tldraw; Superset / Metabase / Grafana / Kibana / TanStack / Vega / ECharts; OHIF / Cornerstone3D / OpenMRS / Medplum; GOV.UK / NHS.UK / USWDS; Medusa / Saleor / Vendure; Element / Matrix / Mattermost / Mastodon; Three.js / Babylon.js / react-three-fiber / XR tooling; recommendation/ranking product patterns; and design-token/component handoff ecosystems.

## Required skill depth

A new skill must make its domain model inspectable. At minimum its substantive guidance must cover its authority/parent relationship, owned decisions, inputs/evidence, procedure or decision model, failure topology, falsification, recovery, output contract, and handoffs. Skills may use different internal structures when the domain calls for a state machine, temporal model, hazard model, provenance model, or spatial model; identical prose scaffolding is not a quality goal.

## Collision policy

Batch review checks four collision classes:

- lexical: duplicate/near-duplicate bodies, suspicious repeated shingles, trivial rename;
- structural: same trigger + parent + output shape + failure class;
- semantic: removing one sibling would leave no material decision uncovered;
- authority: a narrower skill claims decisions owned by a stronger parent or normative source.

## Verification

The merge candidate must prove:

- exactly 100 batch slugs and exactly 774 canonical graph nodes;
- every `SKILL.md` exists and frontmatter matches its slug;
- all parent chains reach `using-nolane-ui` without cycles;
- all outputs are unique and non-colliding;
- provenance record covers all 100 skills and source roles;
- no exact normalized body duplicates or trivial rename pairs;
- no suspicious common-body generator artifact;
- full unit-test discovery passes;
- `python scripts/nui-validate .` passes;
- the exact PR head being merged has green CI;
- after merge, `main` is re-read and the 774-node graph is confirmed.

## Claim boundary

Passing Batch 005 proves structural and authorship-integrity properties of the repository. It does not by itself prove that NUI empirically improves every future UI output. V10 empirical claim discipline remains unchanged.
