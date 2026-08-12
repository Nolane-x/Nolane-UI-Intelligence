# Research and Source Ledger

This ledger records the sources used to design Nolane UI Intelligence (NUI), why each source was consulted, and which *mechanism* was synthesized into NUI. NUI v1 does not bulk-copy third-party skill text or third-party design databases. The skill prose, schemas, router, critics, validators, and eval fixtures in this repository are independently authored for NUI.

## Authority policy

Sources are not equal. NUI uses this order when guidance conflicts:

1. explicit user/product requirements
2. normative standards
3. authoritative platform guidance
4. the active project's design system
5. direct measured evidence
6. mature design-system guidance
7. high-quality agent-skill heuristics
8. community heuristics
9. model preference

A useful community rule never becomes a normative requirement merely because it is popular.

## Agent design systems and skills consulted

| Source | Authority in NUI | Mechanism synthesized | Reuse/licensing posture |
|---|---|---|---|
| OpenAI `frontend-app-builder` — https://github.com/openai/plugins/blob/main/plugins/build-web-apps/skills/frontend-app-builder/SKILL.md | High-quality official agent workflow | Designer-before-engineer sequencing; complete-surface design; design-system extraction before implementation; target-vs-render fidelity; handoff blocked by missing visual comparison | Repository metadata does not expose a single top-level license. NUI copies no source text or assets; it independently implements the mechanisms. |
| OpenAI Product Design router — https://github.com/openai/role-specific-plugins/blob/main/plugins/product-design/skills/index/SKILL.md | High-quality official agent workflow | Router-only index; focused skills for audit/ideate/build/QA; separating user-facing audit from implementation fidelity QA; no build without a design target for material new visual work | NUI copies no source text. Routing rules are independently modeled and generalized beyond OpenAI tooling. |
| Anthropic `frontend-design` — https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md | High-quality official design heuristic | Ground visual language in the subject; deliberate typography; structural devices must encode real meaning; one justified aesthetic risk/signature; self-critique against generic defaults; copy as design material | Source file points to repository license terms. NUI paraphrases no protected passages; it synthesizes concepts into distinct skills/contracts. |
| UI Craft — https://github.com/educlopez/ui-craft | High-quality community design-engineering system | Separate deterministic checks from design judgment; independent review roles; craft floor; anti-slop as a review concern; durable design brief/system | Repository reports MIT. NUI does not vendor the project or copy its rules; concepts are re-derived into NUI architecture. |
| Impeccable — https://github.com/pbakaus/impeccable | High-quality community design language | Rich critique/refinement vocabulary; explicit design-review passes; anti-pattern awareness; treating UI craft as a repeatable agent capability | Repository reports Apache-2.0. No code/text is vendored in NUI v1. |
| UI/UX Pro Max — https://github.com/nextlevelbuilder/ui-ux-pro-max-skill | Community knowledge engine | Structured/retrievable design knowledge; product-aware recommendation rather than one universal preset; cross-agent installation model | CLI README states CC-BY-NC-4.0. NUI deliberately does **not** import its databases or prose; only the abstract knowledge-engine idea informed NUI's progressive-disclosure architecture. |
| Podo Design Agent Skills — https://github.com/podo/design-agent-skills | Community routing/catalogue pattern | Two-level discovery/routing and broad design-domain coverage; progressive disclosure instead of loading a huge prompt | Repository reports MIT. NUI uses its own graph, names, contracts, and content. |

## Normative and authoritative design sources

These sources define constraints or platform behavior. NUI references them rather than mirroring their full contents.

| Source | URL | NUI use |
|---|---|---|
| WCAG 2.2 | https://www.w3.org/TR/WCAG22/ | Web accessibility conformance obligations; exact normative claims should be checked against current criterion text. |
| WAI-ARIA Authoring Practices Guide | https://www.w3.org/WAI/ARIA/apg/ | Expected widget semantics, names/states, and keyboard interaction for custom web widgets. |
| Apple Human Interface Guidelines | https://developer.apple.com/design/human-interface-guidelines/ | iOS/iPadOS/macOS platform conventions, accessibility, interaction, typography, layout, and system behavior. |
| Material Design 3 | https://m3.material.io/ | Android/material component/state guidance and interaction patterns; used as platform/design-system guidance rather than universal law. |
| Fluent 2 | https://fluent2.microsoft.design/ | Mature token/component semantics and platform/product system examples. |
| Design Tokens Community Group specification | https://www.designtokens.org/tr/2025.10/ | Portable token serialization/interchange guidance; NUI's internal semantic tiers remain format-independent. |

## Verification/tooling sources

These are execution oracles, not design authorities.

| Source | URL | NUI use |
|---|---|---|
| Storybook testing | https://storybook.js.org/docs/writing-tests | Component-state surfaces, interaction tests, accessibility checks, and visual regression integration when a project uses Storybook. |
| Storybook accessibility testing | https://storybook.js.org/docs/writing-tests/accessibility-testing | Automated axe-based evidence while preserving the rule that automated checks are partial coverage. |
| Playwright visual comparisons | https://playwright.dev/docs/test-snapshots | Rendered screenshot baselines/diffs for applicable fidelity/regression claims. |
| Playwright ARIA snapshots | https://playwright.dev/docs/aria-snapshots | Semantic/accessibility-tree evidence complementary to pixel evidence. |
| shadcn MCP | https://ui.shadcn.com/docs/mcp | Verified component discovery/retrieval in projects that actually use a compatible registry; never assumed globally. |
| Chrome DevTools / Lighthouse | https://developer.chrome.com/docs/devtools/ and https://developer.chrome.com/docs/lighthouse/ | Browser/runtime inspection and performance/accessibility diagnostic evidence where available. |

## What NUI intentionally did not import

- No UI/UX Pro Max style/palette/font/product database.
- No copied anti-pattern list from Impeccable/UI Craft.
- No copied OpenAI or Anthropic skill workflow text.
- No mirrored WCAG, ARIA APG, HIG, Material, Fluent, Storybook, or Playwright documentation.
- No third-party component source code.

NUI instead converts the recurring ideas into its own architecture: authority hierarchy, typed contracts, state algebra, contextual anti-slop, independent critics, evidence binding, capability adapters, and deterministic completion gates.

## Provenance rule for future contributions

When a new external source materially changes a NUI skill, add it here with: exact source URL, authority class, mechanism learned, any licensing constraint known at the time, and whether any source text/code was incorporated. If incorporation is proposed, verify the source license and preserve required attribution before merging. Inspiration without copied expression should still be documented when it materially shapes policy.
