# NUI V9 Architecture Amendment — Preserve Canonical Ownership

The initial V9 implementation plan proposed five new canonical skill directories for product-envelope, account/workspace lifecycle, settings architecture, interface residue and scope adequacy.

During implementation, an ownership audit found that four of those proposals would overlap existing canonical owners:

- product-envelope discovery belongs upstream in `modeling-product-intent` and is reconciled by `inventorying-product-capabilities`;
- settings structure belongs to `architecting-information`, with domain/security/theme owners consuming its scoped model;
- authentication remains in `designing-authentication-and-passkeys`, while the broader account/workspace lifecycle is represented by product/capability contracts and deterministic V9 validation;
- interface residue is an implementation/platform-fidelity problem owned by `verifying-design-fidelity` plus platform conventions, not a separate aesthetic faculty;
- scope adequacy must be independent from the generator, so its strongest implementation is a deterministic critic (`scope_v9.py`) invoked by the V9 completion gate rather than another generation skill.

The final V9 architecture therefore **preserves all 174 canonical skill nodes** and deepens their decision protocols instead of inflating skill count. New behavior is made executable through `product_v9.py`, `scope_v9.py`, `routing_v9.py`, `v9_repository.py`, tests, knowledge bases and adversarial evals.

This amendment supersedes the original plan only where it proposed new canonical skill directories. The behavioral goals, TDD sequence, release gates, CI artifact, full-project ZIP and verification requirements remain unchanged.

The architectural reason is simple: a skill graph is stronger when one decision has one canonical owner. V9 should make AI reasoning broader and more perceptive, not make routing ambiguous by naming the same responsibility twice.
