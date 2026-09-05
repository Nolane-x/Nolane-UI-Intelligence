"""V13 sixth-wave rules; all operational prose is independently authored."""
from __future__ import annotations

UPLOAD_IMPORT_RULES_V13 = [{'rule_id': 'ui.upload.retry-preserves-upload-identity',
  'domain': 'upload',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Retrying an interrupted upload must preserve the logical file identity',
  'statement': 'A retry of the same selected file should continue or replace the failed attempt under one logical '
               'upload identity instead of creating duplicate pending objects that are indistinguishable to the '
               'user.',
  'intent': 'Keep resumable and retried uploads coherent when transport attempts fail independently of the logical '
            'file the user intended to attach or import.',
  'applies_when': ['A file upload can fail or pause and the interface offers retry without requiring the user to '
                   'choose a different logical file.'],
  'does_not_apply_when': [],
  'failure_modes': ['Each retry creates another visible or server-side pending object even though all attempts '
                    'represent the same selected file.'],
  'user_impacts': ['Users can attach duplicate files, consume storage, or delete the wrong attempt because retry '
                   'history is collapsed into duplicate objects.'],
  'observables': ['Interrupt one upload repeatedly, retry it, and inspect client item identity, server temporary '
                  'objects, and final attachment identity.'],
  'falsifiers': ['Retries remain associated with one logical upload while execution attempts are tracked separately '
                 'or clearly presented when duplication is intentional.'],
  'repairs': ['Separate logical upload identity from transport attempt identifiers and make retry update that '
              'logical item rather than append a new one.'],
  'exceptions': [],
  'verification': ['Retry across network loss, process restart, and resumable-session expiry and confirm exactly one '
                   'final logical file is attached.'],
  'owner_hints': ['designing-resumable-file-uploads'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-upload-import-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.upload.batch-partial-failure-maps-files',
  'domain': 'upload',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Multi-file upload results must map partial failures to the exact files affected',
  'statement': 'When a batch contains a mix of successful, rejected, cancelled, or failed files, the interface must '
               'preserve per-file outcomes instead of reporting the whole batch as one generic status.',
  'intent': 'Let users recover only failed items while keeping successfully uploaded files and their identities '
            'intact.',
  'applies_when': ['The upload surface accepts multiple files or directories in one selection or queue and processes '
                   'items independently.'],
  'does_not_apply_when': [],
  'failure_modes': ['The batch ends with a generic failure or success message that does not identify which files '
                    'actually reached authoritative storage.'],
  'user_impacts': ['Users can re-upload successful files, miss failed files, or remove valid uploads because the '
                   'batch result does not map back to file identity.'],
  'observables': ['Upload a batch containing valid, oversized, unauthorized, and network-failing items and inspect '
                  'item-level state after the queue settles.'],
  'falsifiers': ['Every selected file has a durable outcome and retry can target only failed or cancelled items '
                 'without duplicating successful ones.'],
  'repairs': ['Persist per-file queue state and render result identity at the file row or item level rather than '
              'collapsing completion into a batch boolean.'],
  'exceptions': [],
  'verification': ['Force mixed batch outcomes, reload the page, and confirm per-file success, failure reason, and '
                   'retry state survive reconciliation.'],
  'owner_hints': ['designing-multi-file-upload-queues'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-upload-import-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.upload.duplicate-target-does-not-silent-overwrite',
  'domain': 'upload',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Uploading a duplicate target must not silently overwrite an existing stored object',
  'statement': 'If an upload resolves to the same destination name, key, path, or semantic record as existing '
               'content, the workflow must expose replace, version, merge, skip, or conflict behavior before '
               'destructive overwrite.',
  'intent': 'Protect existing user data when filesystem-like names or record keys collide during import or '
            'attachment workflows.',
  'applies_when': ['Uploaded content can target an existing path, asset, document, record, or logical key rather '
                   'than always creating immutable new objects.'],
  'does_not_apply_when': [],
  'failure_modes': ['A newly uploaded file silently replaces existing content solely because its resolved '
                    'destination identity matches.'],
  'user_impacts': ['Users can lose the prior version or unknowingly substitute content referenced elsewhere in the '
                   'product.'],
  'observables': ['Upload different bytes or records that resolve to an already occupied target and inspect conflict '
                  'UI, version history, and final stored identity.'],
  'falsifiers': ['The product applies an explicit, reviewable conflict policy and preserves prior content when '
                 'replacement is not intentionally confirmed.'],
  'repairs': ['Detect destination identity collisions before commit and route them through versioning, merge, '
              'rename, skip, or explicit replacement semantics.'],
  'exceptions': [],
  'verification': ['Test filename, normalized-path, case-folding, record-key, and concurrent upload collisions and '
                   'confirm no destructive overwrite is silent.'],
  'owner_hints': ['designing-upload-conflict-resolution'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-upload-import-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.upload.mapping-missing-required-fields-visible',
  'domain': 'upload',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Structured imports must expose unmapped required fields before commit',
  'statement': 'When importing structured data, required destination fields that have no valid source mapping must '
               'be surfaced in the mapping or validation step instead of failing deep in the commit phase.',
  'intent': 'Make schema mismatch recoverable while users still have the source columns and target model in view.',
  'applies_when': ['A CSV, spreadsheet, JSON, or other structured import maps source fields into a destination '
                   'schema with required attributes.'],
  'does_not_apply_when': [],
  'failure_modes': ['The mapping step appears valid even though one required destination field is unmapped or mapped '
                    'to incompatible source data.'],
  'user_impacts': ['Users can spend time correcting late failures or accidentally import records with missing '
                   'critical information if the backend fills unsafe defaults.'],
  'observables': ['Prepare sources that omit or rename required fields and inspect mapping validation before any '
                  'records are committed.'],
  'falsifiers': ['Every required target field is mapped or explicitly resolved through a permitted default before '
                 'commit becomes available.'],
  'repairs': ['Validate destination schema requirements during mapping and attach errors to the specific unmapped or '
              'incompatible fields.'],
  'exceptions': [],
  'verification': ['Test missing columns, renamed fields, incompatible types, and optional fields and confirm only '
                   'genuine required gaps block import.'],
  'owner_hints': ['designing-structured-import-mapping'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-upload-import-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.upload.preview-distinct-from-commit',
  'domain': 'upload',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Import preview must remain explicitly non-authoritative until commit',
  'statement': 'A preview of parsed, transformed, or mapped upload data must not be presented as if records already '
               'exist in the destination until the authoritative import commit succeeds.',
  'intent': 'Separate inspection of prospective changes from persisted product state during staged import workflows.',
  'applies_when': ['The product parses or previews uploaded content before a later step commits records, assets, '
                   'configuration, or other authoritative state.'],
  'does_not_apply_when': [],
  'failure_modes': ['Preview rows or transformed data appear in normal product views or success messaging before the '
                    'import transaction has committed.'],
  'user_impacts': ['Users can believe data is safely imported, share references to nonexistent records, or navigate '
                   'away before the actual commit happens.'],
  'observables': ['Upload and preview valid data, stop before commit, then inspect destination queries, navigation, '
                  'counts, and success indicators.'],
  'falsifiers': ['Preview state is clearly staged and destination product state changes only after a successful '
                 'authoritative commit.'],
  'repairs': ['Keep preview data in a staging model and visually label it as prospective until commit returns '
              'authoritative identities and outcomes.'],
  'exceptions': [],
  'verification': ['Abandon preview, fail commit, and complete commit while confirming only the final successful '
                   'path creates normal destination records.'],
  'owner_hints': ['designing-structured-import-mapping'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-upload-import-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.upload.cancel-stops-or-marks-server-processing',
  'domain': 'upload',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Cancelling an upload must truthfully reflect whether server-side processing actually stopped',
  'statement': 'If the client cancels transport after bytes were accepted but background scanning, transcoding, '
               'parsing, or import work may continue, the UI must distinguish local cancellation from confirmed '
               'server cancellation.',
  'intent': 'Prevent “cancelled” from becoming a false claim about work that already crossed an authoritative '
            'processing boundary.',
  'applies_when': ['Upload lifecycle includes server-side processing that can continue after client transfer '
                   'completes or after the user requests cancellation.'],
  'does_not_apply_when': [],
  'failure_modes': ['The interface immediately labels the operation cancelled even though server-side processing can '
                    'still complete and create an artifact or record.'],
  'user_impacts': ['Users can assume no side effect will occur, then later discover an imported file, generated '
                   'asset, or billable process completed anyway.'],
  'observables': ['Request cancellation at several lifecycle points and inspect server job state, resulting '
                  'artifacts, and user-visible cancellation status.'],
  'falsifiers': ['The UI distinguishes cancellation requested, transport stopped, processing stopped, and completed '
                 'side effect according to authoritative evidence.'],
  'repairs': ['Propagate cancellation to server jobs when supported and represent uncertain or late cancellation as '
              'pending rather than definitive.'],
  'exceptions': [],
  'verification': ['Cancel during transfer, scanning, parsing, and finalization and verify visible state matches '
                   'whether the server actually stopped each stage.'],
  'owner_hints': ['designing-file-uploaders'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-upload-import-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.upload.scan-processing-distinct-from-ready',
  'domain': 'upload',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Uploaded files awaiting validation or security scanning must not appear ready for use',
  'statement': 'A file that finished transport but is still scanning, parsing, transcoding, validating, or '
               'moderating must remain in a processing state until the product can safely treat it as usable.',
  'intent': 'Separate byte transfer completion from product readiness when post-upload processing can reject or '
            'transform the artifact.',
  'applies_when': ['The backend performs asynchronous validation, malware scanning, transcoding, moderation, '
                   'metadata extraction, or other readiness checks after upload.'],
  'does_not_apply_when': [],
  'failure_modes': ['The attachment appears fully available immediately after transfer even though later processing '
                    'can still reject or materially alter it.'],
  'user_impacts': ['Users can reference, share, or depend on an artifact that is not yet safe or valid and may '
                   'disappear after a delayed processing result.'],
  'observables': ['Complete transport while holding the post-upload processor pending, then inspect availability, '
                  'actions, links, and final transition after processing.'],
  'falsifiers': ['The artifact remains visibly processing and only exposes actions appropriate to that state until '
                 'readiness is authoritative.'],
  'repairs': ['Model transfer and readiness as separate lifecycle states and gate downstream actions on the '
              'authoritative post-processing result.'],
  'exceptions': [],
  'verification': ['Test accepted, rejected, delayed, and transformed processing outcomes and confirm readiness '
                   'appears only after the correct terminal event.'],
  'owner_hints': ['designing-file-uploaders'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-upload-import-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.upload.account-scope-revalidated-before-attach',
  'domain': 'upload',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Completed uploads must revalidate account and destination scope before attachment',
  'statement': 'If the user switches account, workspace, project, or destination while an upload is in flight, final '
               'attachment must verify the current intended scope rather than silently committing to stale context.',
  'intent': 'Prevent long-running uploads from crossing identity or tenancy boundaries after the surrounding '
            'navigation context changes.',
  'applies_when': ['Upload transfer can outlive the account, workspace, record, or container context from which it '
                   'started.'],
  'does_not_apply_when': [],
  'failure_modes': ['A file finishes after the user switched context and attaches to the old or new destination '
                    'without a deliberate scope decision.'],
  'user_impacts': ['Sensitive files can be attached to the wrong tenant, record, conversation, or account because '
                   'the upload inherited stale or ambiguous context.'],
  'observables': ['Start an upload, switch account or destination before completion, and inspect final attachment '
                  'target, permission check, and visible reconciliation.'],
  'falsifiers': ['The final commit is bound to the original immutable destination or explicitly re-confirmed for the '
                 'new scope with current authorization.'],
  'repairs': ['Persist upload destination identity independently of navigation and revalidate authorization at final '
              'attachment commit.'],
  'exceptions': [],
  'verification': ['Switch accounts, workspaces, routes, and records during upload and confirm no file crosses a '
                   'scope boundary without explicit validated intent.'],
  'owner_hints': ['designing-file-uploaders'],
  'verifier_hints': ['critiquing-security-and-privacy'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-upload-import-owners-v13'],
  'status': 'active'}]

__all__ = ["UPLOAD_IMPORT_RULES_V13"]
