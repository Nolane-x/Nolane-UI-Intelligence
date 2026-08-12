# Usage

## Start a material UI task

Load `using-nolane-ui`. The bootstrap hands lifecycle ownership to `nolane-ui`, which compiles a contract, routes faculties, creates obligations, binds evidence, and owns release semantics.

Do **not** preload the entire skill graph. The current research snapshot contains 125 skills, but progressive disclosure is a design constraint: the agent should receive only the smallest sufficient faculty graph for the task.

## Build the v2 task profile

`routing-ui-work` classifies observable conditions rather than keywords. A strong profile can include:

- `intent[]`
- `platform_surfaces[]`
- `input_modalities[]`
- `ai_role`
- `risk_class`
- `temporal_behaviors[]`
- `social_context`
- `specialized_ui_domains[]`
- `regulatory_or_standard_sensitivity`
- `research_freshness_requirement`
- `user_context`
- `information_context`
- `interaction_context`
- `visual_context`
- `evidence_capabilities`

Unknown high-impact dimensions remain unknown. Do not convert missing information into a convenient default merely to keep designing.

## Example: expert AI-agent operations dashboard

A likely route begins:

`using-nolane-ui → nolane-ui → ui-contracting → routing-ui-work`

Then selected faculties can include:

`modeling-product-intent`, `modeling-users-and-tasks`, `architecting-information`, `designing-navigation`, `designing-interactions`, `modeling-component-states`, `designing-data-dense-interfaces`, `designing-human-ai-interaction`, `designing-ai-uncertainty-and-provenance`, `designing-agent-autonomy-and-control` when actions are autonomous, `exploring-aesthetic-directions`, `directing-visual-hierarchy`, `architecting-design-tokens`, `architecting-component-systems`, `adapting-responsive-layouts`, `designing-accessible-interfaces`, and the relevant independent critics.

If responses stream, route latency/streaming/resilience. If multiple agents act, route multi-agent attribution. If generated UI can call actions, route `designing-generative-ui` and security/privacy critique.

## Example: TV application

A TV profile should not inherit mobile defaults. A likely route includes:

`designing-tv-ten-foot-interfaces` + `designing-gamepad-remote-focus` + `critiquing-input-modality`

Then add content/product/navigation/accessibility faculties that actually exist. Test viewing distance, directional focus graph, remote discoverability, focus restoration, overscan/safe-area behavior where applicable, and long-label/localization pressure.

## Example: automotive while driving

When `platform_surfaces=[automotive]` and `driving_context=driving`, hard routing requires automotive ownership plus human-factors/safety verification. Do not reduce the design to a responsive dashboard. Interaction authority, glance behavior, task limits, interruption, voice, physical controls, and recovery must reflect the driving context and current platform/regulatory guidance.

## Example: flight deck

`platform_surfaces=[flight-deck]` hard-routes:

`designing-flight-deck-interfaces` + `engineering-human-factors` + `designing-high-stakes-decisions` + `critiquing-human-factors-and-safety`

The flight-deck owner models phase of flight, crew role, automation modes, alert/control integration, design-related flightcrew error, degraded conditions, and certification evidence. NUI can organize the reasoning and evidence contract; it cannot certify an aircraft system.

## Example: AAC communication surface

Use root accessibility plus `designing-aac-communication-interfaces`, then route the person’s actual input method separately. AAC does not imply touch. The design must preserve communicative intent, vocabulary/motor consistency, symbol semantics, authorship, privacy, offline essentials, and portability.

If the user communicates through switch scanning, gaze, head tracking, keyboard, or another access method, route the corresponding modality faculty as well.

## Example: sign-language media

Route `designing-accessible-media-alternatives` → `designing-sign-language-presentation` plus accessibility verification. Preserve the actual sign language, signing space, timing, interpreter/signer attribution, language selection, readable scale, and coexistence with captions or source video.

Synthetic signing also routes avatar/embodied representation and requires linguistic evidence; smooth animation is not proof of correct signing.

## Example: affective/adaptive UI

When an interface senses or infers emotion, stress, engagement, or another internal state, use `designing-affective-adaptive-interfaces`. The signal is not ground truth. Keep the chain visible in the design reasoning:

`signal → feature → inference → confidence/freshness → proposed adaptation → authority`

Material adaptation also routes consent/privacy and security/privacy critique. Consequential actions cannot be authorized solely by an affect inference.

## Example: existing product needs help and guidance

Use `designing-in-product-assistance` only after asking whether the primary UI can simply be made clearer. Assistance owns residual explanation, coaching, procedural guidance, troubleshooting, recovery, and escalation beyond onboarding.

A help layer must preserve task state, use the product’s terminology, remain accessible, and inherit ordinary permission/undo rules if an AI helper can take actions.

## What an agent should produce before code

For material new design, implementation should not be forced to invent major product, human-factors, interaction, or visual decisions. Depending on routing, artifacts may include:

- UI contract with authority, target fidelity, risk and non-goals;
- v2 task profile with hard routes and capability gaps;
- product/user/task and human-factors models;
- IA/task-flow/navigation contracts;
- interaction, operation, component-semantic and state contracts;
- aesthetic direction and hierarchy/composition/type/color/spacing contracts;
- token/component-system contracts;
- platform and modality contracts;
- accessibility and specialist obligations;
- AI authority/provenance/correction contracts when applicable;
- safety/trust/privacy/transaction contracts where consequences require them;
- verification plan and evidence requirements.

If a trusted source already fixes an axis, record it as frozen. Do not redesign it for ceremony.

## During implementation

Treat selected contracts as production constraints. If implementation reveals a material unresolved decision, return to the earliest owning faculty rather than hiding the choice in CSS or component code.

Use existing project components when their semantics match. Component availability is not proof of pattern correctness.

Generated UI should normally be constrained to an approved component vocabulary and typed data/action bindings. Rendering authority must not silently become permission to execute privileged actions.

## Verification

After an inspectable render exists:

1. Run `challenging-ui-designs` with verification lenses based on plausible failure impact.
2. Bind browser, screenshot, semantic-tree, interaction, component, token, accessibility, device, simulation, research, or expert evidence through `binding-ui-evidence`.
3. Repair findings through `recovering-ui-work`.
4. Re-test affected and transitive obligations.
5. Submit a bounded packet to `gating-ui-completion`.

Generation and verification routing are independent. A safety critic can be required even if the design was inherited. An accessibility critic can be required even if the task was “only visual.”

Strict fidelity work requires an authoritative target and inspectable current render. Static source code cannot close a visual-fidelity obligation.

## Research-sensitive work

When a task depends on a high-drift standard, platform, AI protocol, automotive rule, safety authority, or emerging modality, route `researching-ui-frontiers` and `calibrating-ui-authority` rather than relying on model memory.

`knowledge/research-radar.json` defines tracked triggers. A source change can reopen a domain even though the 2026-08-12 research wave is marked bounded `SATURATED`.

`SATURATED` never means “research is finished forever.” It means the last adversarial sweep in the bounded wave produced zero new non-decomposable owner classes and passed the evidence gate.

## Reduced path for small changes

A local change can skip discovery/divergence/systemization only when:

- product semantics, IA and visual direction are already established;
- the change introduces no new interaction/component/surface/modality/AI/risk class;
- omitted faculties have no material failure mode for the change;
- deterministic hard routes are still satisfied;
- relevant state/regression/accessibility verification still occurs.

Record the decision. “Small change” is not a universal bypass.

## Audit-only use

For audit requests, preserve the artifact and route critic faculties after contract/profile creation. Critics use `may_modify: false` and report findings. A later repair request creates a repair scope; critics must not silently change their evidence target and certify the result themselves.

## Completion language

Use bounded claims, for example:

> The reviewed desktop and tablet routes were rendered and compared against the accepted target; the declared keyboard flow, state matrix, token checks, and scoped automated accessibility checks passed. Native mobile screen-reader behavior, the Japanese locale, and the offline reconnect path were not tested and remain outside this release claim.

Avoid absolute labels such as “pixel-perfect,” “fully accessible,” “certified,” “production-ready,” or “industry-complete” unless the evidence packet actually supports the exact scope. Repository-level bounded research saturation is not task-level UI quality evidence.
