---
name: compiling-concrete-design-packets
description: Use when routing and authority resolution are complete and when the agent needs a compact set of concrete, source-bound choices it can execute immediately without collapsing back into generic UI defaults.
---

# Compiling Concrete Design Packets

## Parent Contract
**Required parent:** `routing-to-ui-authorities`.

Consume the task profile, hard obligations, authority route, local design memory, relevant pattern cards, and implementation constraints. Do not reopen every upstream debate. This skill converts deep reasoning into a **bounded decision packet** that remains traceable to why each choice exists.

## Decision Boundary
Own the bridge between “we understand the problem” and “the implementation agent knows what to do next.” It does not generate a full page, choose an arbitrary style preset, or replace specialist owners. It chooses a small number of high-leverage decisions that constrain the search space without erasing uncertainty.

## Packet Construction
Allocate a decision budget. Typical high-value slots are: task structure, platform/domain convention, signature, typography, material/surface logic, interaction semantics, motion/choreography, responsive recomposition, and implementation shortcut. Select only slots that actually change the current task.

Each selected card must carry:
- a concrete action or rule that can affect implementation;
- source/provenance handles and the authority dimension it relies on;
- **contraindication carry-through** so the fast path cannot forget when the pattern should not be used;
- a local validation statement that can fail;
- a transfer boundary separating mechanism from upstream trade dress or domain assumptions.

Do not fill the budget because space exists. Five decisive constraints can be stronger than nine decorative suggestions.

## Uncertainty Preservation
An **unresolved-authority blocker** remains a blocker inside the packet. Do not replace it with a popular default, a model preference, or the nearest pattern in the database. If a domain-specific rule is absent, state what must be researched. The packet is allowed to be `NEEDS_RESEARCH`.

## Immediate Answerability Without Premature Closure
Fast execution is useful when it compresses already-resolved knowledge. It is dangerous when it skips semantic, safety, accessibility, platform, or legal work. Mark every item as `hard`, `strong`, or `exploratory`; hard items survive compression. For exploratory visual directions, present bounded alternatives rather than one style-category verdict.

A palette/font/style lookup may seed exploration. It never becomes the reason a design is appropriate. Concrete packets should answer “what mechanism and why here?” rather than “which aesthetic label ranked highest?”

## Output — `concrete-design-packet`
Return `status`, `decisions[] {pattern_id, dimension, decision, force, rationale, provenance, contraindications, validation, transfer_boundary}`, `blockers[]`, `discarded_candidates[]`, `decision_budget`, and `re_expansion_triggers[]`.

## Falsification
Remove source names and style labels. If the decisions no longer make sense from user task, platform/domain conditions and local evidence, the packet is recommendation theater. Run a near-neighbor prompt in a different domain; if the same signature, palette, layout and motion packet survives unchanged, the compiler has converged to a house style.

## Recovery
Drop weak cards, reopen only the unresolved dimension, fetch stronger concrete evidence, and rebuild the packet without invalidating independent decisions. When implementation reveals a contraindication, trigger re-expansion rather than patching around the original choice.

## Hard gate
**A fast packet cannot become executable if it drops a hard obligation, invents an answer for an unresolved authority, strips contraindications/provenance, or uses category/style retrieval as a substitute for product-specific reasoning.**
