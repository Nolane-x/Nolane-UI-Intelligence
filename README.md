# Nolane UI Intelligence

**Universal Design Cognition & Verification System for AI agents.**

Nolane UI Intelligence (NUI) is a platform-agnostic Agent Skill graph for UI/UX work. It is built around a simple claim: an agent becomes more reliable at interface design when taste, product reasoning, interaction semantics, design systems, accessibility, implementation fidelity, and verification are treated as separate obligations instead of one vague instruction to “make it beautiful.”

NUI does not promise objective beauty or replace designers. It constrains the observable work process so an agent must make its design assumptions explicit, route to the relevant specialist skills, build a coherent visual/system contract, expose applicable states, attack its own proposal through independent critics, bind evidence, and pass a completion gate before claiming success.

## What makes NUI different

- **Universal core.** The core describes capabilities and evidence, not Codex-, Claude-, Figma-, React-, or Tailwind-specific commands.
- **Depth-locked skill graph.** Narrow skills own one judgment domain; parent gates cannot be waived by a child skill.
- **Progressive disclosure.** The router selects the smallest sufficient faculty set for the current UI problem.
- **Design before code when design is material.** Direct-to-code is allowed only through an explicit lightweight exception.
- **Constraint-derived UI.** Components and patterns must be justified by semantic and interaction needs, not fashion.
- **Contextual anti-slop.** No blanket ban on cards, gradients, glass, serif faces, minimalism, maximalism, or motion.
- **Independent criticism.** The generator may not certify material UI completion by itself.
- **Evidence-gated release.** Missing verification remains UNKNOWN/BLOCKED.
- **Deterministic invariants.** Machine-checkable constraints are checked by the kernel rather than trusted to model self-report.

## Canonical lifecycle

`INTAKE → CONTRACTED → ROUTED → DISCOVERED → ARCHITECTED → DIVERGED → DESIGN_SELECTED → SYSTEMIZED → SPECIFIED → IMPLEMENTABLE → RENDERED → CRITIQUED → VERIFIED → RELEASED`

Any failed obligation, stale evidence, contradiction, or material regression routes to `RECOVERY`.

## Repository map

- `skills/` — universal cognitive and design skills
- `schemas/` — typed record contracts
- `src/nolane_ui/` — deterministic validators
- `evals/` — routing, pressure, craft, responsive, accessibility, and adversarial fixtures
- `adapters/` — runtime capability mappings
- `docs/research/` — source and synthesis ledger
- `artifacts/` — bounded completion packets and verification outputs

## Authority order

User/product requirements > normative standards > authoritative platform guidance > project design system > direct measured evidence > mature design-system guidance > high-quality agent heuristics > community heuristics > model preference.

## Start here

For any material UI/UX task, load `skills/using-nolane-ui/SKILL.md` first. The router decides which additional skills are relevant. Do not preload the entire repository into a model context.

## Verification

Run:

```bash
python -m unittest discover -s tests -v
python scripts/nui-validate .
```

The release claim is intentionally bounded. A passing repository validator proves structural/contract invariants; it does not prove that any future interface is beautiful, usable, accessible, or faithful without task-specific evidence.
