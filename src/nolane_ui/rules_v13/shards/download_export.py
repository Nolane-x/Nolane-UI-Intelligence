"""V13 sixth-wave rules; all operational prose is independently authored."""
from __future__ import annotations

DOWNLOAD_EXPORT_RULES_V13 = [{'rule_id': 'ui.download.export-snapshot-time-visible',
  'domain': 'download',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Downloaded exports must expose the snapshot or generation time of their data',
  'statement': 'When exported content represents a point-in-time snapshot rather than a continuously current view, '
               'the UI must expose the data cutoff or generation time before or with the download.',
  'intent': 'Let users distinguish current product state from a static export that may already be stale when opened '
            'or shared.',
  'applies_when': ['An export or generated report materializes records, metrics, configuration, or audit data at a '
                   'particular snapshot or cutoff time.'],
  'does_not_apply_when': [],
  'failure_modes': ['The downloaded artifact looks authoritative but the user has no visible indication of when its '
                    'underlying data stopped updating.'],
  'user_impacts': ['People can circulate or make decisions from stale exports while assuming they reflect the latest '
                   'product state.'],
  'observables': ['Generate exports before and after data changes and inspect both the download surface and artifact '
                  'metadata for the snapshot boundary.'],
  'falsifiers': ['The snapshot or generation time is available in the workflow or artifact and corresponds to the '
                 'data actually included.'],
  'repairs': ['Capture the authoritative export cutoff and include it in download status, filename metadata, report '
              'header, or another durable artifact surface.'],
  'exceptions': [],
  'verification': ['Change source data during long-running export generation and verify the communicated cutoff '
                   'matches the records present in the final file.'],
  'owner_hints': ['designing-data-export-portability'],
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
  'provenance_ids': ['nui-download-export-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.download.resume-preserves-file-identity',
  'domain': 'download',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Resuming a download must continue the same artifact rather than splice a different version',
  'statement': 'A resumable download must bind range or continuation requests to the same artifact version so a '
               'regenerated file cannot be silently combined with bytes from an earlier version.',
  'intent': 'Protect file integrity when large downloads pause while the underlying export, media object, or '
            'generated artifact can change.',
  'applies_when': ['The client or service supports resumable or ranged downloads for artifacts whose content can be '
                   'regenerated, replaced, or versioned.'],
  'does_not_apply_when': [],
  'failure_modes': ['A resumed transfer continues against a different artifact version while the client appends the '
                    'new bytes to the partially downloaded old file.'],
  'user_impacts': ['Users can receive corrupted or internally inconsistent files that appear to have downloaded '
                   'successfully.'],
  'observables': ['Start a ranged download, replace or regenerate the source artifact, then resume and compare '
                  'entity tags, version identifiers, and final file hash.'],
  'falsifiers': ['Resume is accepted only when artifact identity still matches, otherwise the transfer restarts or '
                 'asks the user to fetch the new version.'],
  'repairs': ['Bind resume tokens or byte ranges to immutable artifact identity and reject continuation when the '
              'source version changes.'],
  'exceptions': [],
  'verification': ['Interrupt transfers across artifact replacement, expiration, and server restart and verify the '
                   'final bytes always belong to one coherent version.'],
  'owner_hints': ['designing-download-progress-and-retry'],
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
  'provenance_ids': ['nui-download-export-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.download.generated-artifact-expiry-visible',
  'domain': 'download',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Generated download artifacts must expose expiry before the user depends on the link',
  'statement': 'If a generated report, export, or signed download is available only for a bounded retention period, '
               'the UI must communicate that expiry instead of presenting the artifact as a durable permanent link.',
  'intent': 'Prevent users from bookmarking, sharing, or postponing retrieval of artifacts that the system already '
            'knows will become unavailable.',
  'applies_when': ['A generated artifact or download URL expires because of retention policy, signed URL lifetime, '
                   'temporary storage, or security policy.'],
  'does_not_apply_when': [],
  'failure_modes': ['The UI shows a normal download link with no expiry context even though the backend will '
                    'invalidate it after a known time.'],
  'user_impacts': ['Users can lose access to long-running exports or share links that fail unexpectedly for '
                   'collaborators.'],
  'observables': ['Generate a temporary artifact, inspect its visible availability window, cross the expiry '
                  'boundary, and attempt access from the original link.'],
  'falsifiers': ['The workflow communicates expiry and provides regeneration or a durable-save option when the '
                 'artifact lifecycle permits it.'],
  'repairs': ['Expose artifact expiration metadata in the download surface and retain a regeneration route tied to '
              'the logical export request.'],
  'exceptions': [],
  'verification': ['Test short-lived artifacts across refresh, navigation, sharing, and expiry and confirm the UI '
                   'never implies indefinite availability.'],
  'owner_hints': ['designing-download-progress-and-retry'],
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
  'provenance_ids': ['nui-download-export-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.download.partial-export-scope-visible',
  'domain': 'download',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Exports containing only a subset of requested data must identify the omitted scope',
  'statement': 'When an export excludes records because of limits, permissions, filters, timeouts, unsupported '
               'fields, or partial failure, the download flow must disclose that the artifact is incomplete.',
  'intent': 'Keep exported artifacts from appearing complete when the generation pipeline knowingly omitted part of '
            'the requested scope.',
  'applies_when': ['An export request can complete with fewer records, fields, attachments, partitions, or pages '
                   'than the user requested.'],
  'does_not_apply_when': [],
  'failure_modes': ['The export is offered as successful without identifying that a subset of the intended data was '
                    'omitted.'],
  'user_impacts': ['Users can archive, analyze, or migrate incomplete data while assuming the file is a complete '
                   'representation of the selected scope.'],
  'observables': ['Trigger an export with one inaccessible or failing subset and compare requested scope, generation '
                  'result metadata, and delivered artifact.'],
  'falsifiers': ['The UI reports incomplete coverage and identifies the reason or omitted subset at a level that '
                 'supports recovery without exposing protected data.'],
  'repairs': ['Carry coverage and omission metadata through the export pipeline and present it before download and, '
              'where appropriate, inside the artifact.'],
  'exceptions': [],
  'verification': ['Exercise permission-limited, capped, timed-out, and failed-partition exports and confirm '
                   'incompleteness remains visible after generation succeeds.'],
  'owner_hints': ['designing-data-export-portability'],
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
  'provenance_ids': ['nui-download-export-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.download.lossy-format-warning-before-generation',
  'domain': 'download',
  'class': 'contextual',
  'severity': 'moderate',
  'enforcement': 'warn',
  'title': 'Choosing a lossy export format must disclose material information loss before generation',
  'statement': 'If an export format cannot preserve comments, formulas, rich structure, precision, metadata, '
               'attachments, color, or other meaningful source information, that loss must be disclosed before the '
               'user commits to the format.',
  'intent': 'Make format choice an informed transformation decision instead of a hidden degradation discovered after '
            'the artifact is opened elsewhere.',
  'applies_when': ['The product offers multiple export formats with materially different representational '
                   'capabilities or fidelity.'],
  'does_not_apply_when': [],
  'failure_modes': ['A format is presented as interchangeable even though it drops or flattens important information '
                    'that another available format could preserve.'],
  'user_impacts': ['Users can permanently lose context or share an artifact that cannot represent the source '
                   'accurately enough for its intended use.'],
  'observables': ['Export a source containing features unsupported by each format and compare the selection UI with '
                  'the actual information retained in the output.'],
  'falsifiers': ['The format chooser identifies material limitations relevant to the current content or the export '
                 'preserves all semantically important information.'],
  'repairs': ['Evaluate selected content against format capabilities and surface meaningful fidelity tradeoffs '
              'before starting generation.'],
  'exceptions': [],
  'verification': ['Use representative complex source data and verify each format warning corresponds to actual '
                   'retained and omitted information.'],
  'owner_hints': ['designing-export-configuration'],
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
  'provenance_ids': ['nui-download-export-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.download.retry-reuses-logical-export-job',
  'domain': 'download',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Retrying export generation must reuse logical job identity rather than create ambiguous duplicates',
  'statement': 'When a failed or timed-out export is retried, the interface must keep attempts associated with one '
               'logical request or clearly distinguish a deliberately duplicated export job.',
  'intent': 'Prevent users from receiving multiple indistinguishable artifacts or paying repeated processing cost '
            'because retry created hidden duplicate work.',
  'applies_when': ['Export generation runs asynchronously and users can retry after failure, timeout, lost '
                   'connection, or uncertain completion.'],
  'does_not_apply_when': [],
  'failure_modes': ['Each retry silently creates a new independent export job while older attempts may still '
                    'complete and appear as duplicate downloadable artifacts.'],
  'user_impacts': ['Users can download the wrong version, consume duplicate resources, or mistake multiple artifacts '
                   'for separate requested exports.'],
  'observables': ['Force uncertain completion and retry several times, then inspect backend job identity, visible '
                  'history, notifications, and final artifacts.'],
  'falsifiers': ['Retries are grouped under one logical export request with explicit attempt status, or intentional '
                 'duplicate jobs receive distinct user-visible identity.'],
  'repairs': ['Separate logical export identity from execution-attempt identity and make retries attach to the same '
              'logical request by default.'],
  'exceptions': [],
  'verification': ['Retry across network loss, server timeout, and delayed original completion and confirm job '
                   'history and downloadable outputs remain unambiguous.'],
  'owner_hints': ['designing-render-and-export-queues'],
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
  'provenance_ids': ['nui-download-export-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.download.filename-collision-does-not-silent-overwrite',
  'domain': 'download',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Downloading to a conflicting filename must not silently overwrite an existing local artifact',
  'statement': 'When the client controls destination naming and a file with the same name already exists, the '
               'download workflow must preserve the existing artifact or obtain an explicit overwrite decision.',
  'intent': 'Prevent local data loss when repeated exports or generated files reuse predictable filenames.',
  'applies_when': ['The application can save or write downloaded artifacts directly into a user-visible local '
                   'destination rather than delegating collision handling entirely to the operating system.'],
  'does_not_apply_when': [],
  'failure_modes': ['A second download replaces an existing file with the same name without user awareness or '
                    'version distinction.'],
  'user_impacts': ['Users can lose a prior export or confuse two different snapshots because one artifact silently '
                   'replaced another.'],
  'observables': ['Download two different artifacts that resolve to the same local filename and inspect destination '
                  'behavior and retained file identities.'],
  'falsifiers': ['The workflow versions, renames, or explicitly confirms replacement and the user can distinguish '
                 'the resulting artifact from the existing one.'],
  'repairs': ['Detect destination collisions before write and apply a safe naming or explicit overwrite policy '
              'instead of unconditional replacement.'],
  'exceptions': [],
  'verification': ['Exercise repeated downloads, sanitized filename collisions, and concurrent saves and confirm no '
                   'existing artifact is silently destroyed.'],
  'owner_hints': ['designing-download-progress-and-retry'],
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
  'provenance_ids': ['nui-download-export-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.download.expired-link-has-regeneration-path',
  'domain': 'download',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Expired generated-download links must recover through logical regeneration rather than a dead end',
  'statement': 'When a temporary download link expires but the underlying export request can be regenerated, the '
               'expired state should preserve enough request identity to offer a bounded regeneration path.',
  'intent': 'Turn expected artifact expiry into a recoverable lifecycle instead of forcing users to reconstruct '
            'complex export parameters manually.',
  'applies_when': ['Generated artifacts expire independently of the saved export definition or source data needed to '
                   'create them again.'],
  'does_not_apply_when': [],
  'failure_modes': ['Opening an expired artifact produces only a generic not-found or forbidden state even though '
                    'the product can recreate the same logical export.'],
  'user_impacts': ['Users can lose time and reproducibility rebuilding filters, formats, scopes, or options that the '
                   'system still knows.'],
  'observables': ['Let a generated artifact expire and reopen it from history, notification, or bookmark while the '
                  'logical export request remains available.'],
  'falsifiers': ['The expired state identifies the artifact lifecycle and offers regeneration from preserved request '
                 'parameters when policy allows.'],
  'repairs': ['Retain logical export metadata beyond artifact retention and route expired artifact references to a '
              'regeneration flow instead of a dead resource URL.'],
  'exceptions': [],
  'verification': ['Expire artifacts across different entry points and verify regeneration reproduces the intended '
                   'export definition without reviving invalid permissions.'],
  'owner_hints': ['designing-download-progress-and-retry'],
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
  'provenance_ids': ['nui-download-export-owners-v13'],
  'status': 'active'}]

__all__ = ["DOWNLOAD_EXPORT_RULES_V13"]
