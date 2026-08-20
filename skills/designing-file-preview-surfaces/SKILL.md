---
name: designing-file-preview-surfaces
description: Use when users need to inspect files before opening, downloading, approving, or sharing them and preview capability must distinguish safe rendering, unsupported types, fidelity, pagination, and metadata.
---

# Designing File Preview Surfaces

## Parent Contract
**Required parent:** `designing-file-transfer-and-storage`.

This faculty owns non-authoritative file preview. It decides what can be rendered safely and approximately inside the product, how users know when the preview is incomplete, and how to move to the original/open/download action. It does not own full editors for every file type.

## Decision Boundary
Classify file types by preview capability: exact-enough native view, rendered conversion, extracted text/image, metadata-only, or unsupported. Preview must never imply editability or legal fidelity it does not have. For PDFs/docs/spreadsheets, define pagination/sheets/pages and whether fonts, formulas, comments, signatures, animation, or macros are omitted. Security scanning or sandboxing may delay preview even after upload completes.

Large files need progressive rendering and explicit loading per page/section rather than freezing the entire interface. Accessible alternatives should expose text/structure where possible and provide original download/open when the preview renderer cannot preserve semantics. Sensitive previews may need masking, watermarking, or no-thumbnail policy according to privacy owners.

## Failure Topology
- Converted document preview drops a signature but looks authoritative.
- Unsupported file displays a blank pane rather than explaining the limitation.
- Preview fetch executes active content from an untrusted file.
- Multi-page file loads all pages at once and exhausts memory.
- Screen reader receives an image-only preview although extractable text exists.
- Preview remains stale after file replacement and does not show version identity.

## Falsification and Recovery
Test supported/unsupported/corrupt/huge files, converted fidelity, multi-page navigation, replaced versions, accessibility extraction, scan-processing delay, and sensitive content. Compare preview against original for material omissions. The design fails if users can reasonably treat an approximate preview as exact without disclosure.

Recover by labeling preview fidelity, sandboxing risky formats, rendering progressively, binding preview to exact file version, and providing original/open alternatives. Suppress previews entirely where safe rendering or privacy cannot be guaranteed.

## Output Contract
Return `file-preview-contract` with format capability matrix, fidelity/omission disclosure, sandboxing, progressive navigation, version binding, accessibility alternatives, sensitive-content policy, and preview verification cases.
