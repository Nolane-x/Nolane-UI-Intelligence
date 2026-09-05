"""V13 sixth-wave rules; all operational prose is independently authored."""
from __future__ import annotations

PRINT_OUTPUT_RULES_V13 = [{'rule_id': 'ui.print.preview-matches-selected-range',
  'domain': 'print',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Print preview must correspond to the exact pages, records, or range selected for output',
  'statement': 'When users choose a subset such as selected pages, labels, records, slides, or table rows, the '
               'preview must render that subset rather than a generic full-document representation.',
  'intent': 'Make the final physical-output decision inspectable before consuming paper, labels, materials, or '
            'sensitive content.',
  'applies_when': ['The print workflow supports page ranges, selected records, current view, label subsets, or other '
                   'bounded output scopes.'],
  'does_not_apply_when': [],
  'failure_modes': ['The preview shows the full source or a stale previous range while the print job will submit a '
                    'different subset.'],
  'user_impacts': ['Users can print the wrong pages or expose unintended records because the visual confirmation '
                   'does not match the queued output.'],
  'observables': ['Change selection and range repeatedly and compare preview page identity, job parameters, and '
                  'resulting output sequence.'],
  'falsifiers': ['Preview content and ordering are generated from the same effective output scope that will be '
                 'submitted to the printer.'],
  'repairs': ['Bind preview rendering and print submission to one immutable print-intent object instead of '
              'independent range state.'],
  'exceptions': [],
  'verification': ['Test current page, arbitrary ranges, discontiguous selections, filtered records, and reordered '
                   'labels and confirm preview and output match exactly.'],
  'owner_hints': ['designing-print-preview'],
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
  'provenance_ids': ['nui-print-output-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.print.current-printer-target-visible',
  'domain': 'print',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'The active printer destination must remain visible at the final submission boundary',
  'statement': 'Before a physical print job is submitted, the interface must identify the currently selected printer '
               'or output destination, especially when multiple nearby, remote, secure, or virtual printers are '
               'available.',
  'intent': 'Prevent confidential or expensive output from being sent to the wrong device because destination '
            'selection was hidden after an earlier step.',
  'applies_when': ['A print workflow can target more than one physical or virtual printer and destination can change '
                   'through defaults, discovery, policy, or user selection.'],
  'does_not_apply_when': [],
  'failure_modes': ['The final Print action is available without a visible destination, or the destination changes '
                    'after selection without being reflected in the confirmation state.'],
  'user_impacts': ['Sensitive documents can print in the wrong location or users can waste material on an unintended '
                   'device.'],
  'observables': ['Switch printer defaults, discovery order, and manual selection while keeping the print panel open '
                  'and inspect the final submitted target identity.'],
  'falsifiers': ['The visible destination at submission matches the authoritative printer identifier in the queued '
                 'job.'],
  'repairs': ['Keep printer identity in the print-intent model and display it adjacent to the final submission '
              'action rather than relying on a hidden default.'],
  'exceptions': [],
  'verification': ['Test local, remote, offline, secure-release, and default-printer changes and confirm the '
                   'submitted target always matches the shown destination.'],
  'owner_hints': ['designing-printer-selection-and-status'],
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
  'provenance_ids': ['nui-print-output-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.print.submitted-distinct-from-printer-accepted',
  'domain': 'print',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Print submission must be distinguished from printer acceptance and physical completion',
  'statement': 'Sending a job to the operating system or print service must not be labeled printed or complete until '
               'the workflow has evidence appropriate to the actual acceptance or completion semantics it claims.',
  'intent': 'Keep multi-stage print lifecycle truthful when the application, spooler, printer, and physical output '
            'can fail independently.',
  'applies_when': ['The product submits print jobs to a spooler, remote print service, printer queue, or hardware '
                   'device with asynchronous status.'],
  'does_not_apply_when': [],
  'failure_modes': ['The interface reports “Printed” immediately after local submission even though the printer can '
                    'still reject, remain offline, jam, or fail before output.'],
  'user_impacts': ['Users can leave or discard source materials believing physical output exists when only the '
                   'submission request succeeded.'],
  'observables': ['Submit jobs to offline, paused, rejecting, and healthy printers and compare application status '
                  'with spooler and hardware evidence.'],
  'falsifiers': ['The UI uses bounded states such as submitted, queued, accepted, printing, and completed according '
                 'to the evidence actually available.'],
  'repairs': ['Map each print lifecycle transition to its authoritative source and avoid collapsing initial '
              'submission into final completion language.'],
  'exceptions': [],
  'verification': ['Exercise offline printers, queue pause, paper-out, cancellation, and successful completion and '
                   'confirm visible status never outruns evidence.'],
  'owner_hints': ['designing-printer-selection-and-status'],
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
  'provenance_ids': ['nui-print-output-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.print.partial-page-failure-retryable',
  'domain': 'print',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Partial print failures must support retry without reprinting already confirmed output blindly',
  'statement': 'When a multi-page or multi-label job fails after some output is confirmed, recovery should identify '
               'the completed subset and let users retry the remaining scope where the printer model can support '
               'that evidence.',
  'intent': 'Avoid duplicate physical output and wasted material when failures occur after only part of a job has '
            'printed.',
  'applies_when': ['The print system exposes enough job progress or page/label accounting to distinguish completed '
                   'output from the failed remainder.'],
  'does_not_apply_when': [],
  'failure_modes': ['Retrying a partially completed job always resubmits the full scope even though the application '
                    'knows which portion already printed.'],
  'user_impacts': ['Users can create duplicate labels, pages, tickets, or other physical artifacts and may not know '
                   'which output is authoritative.'],
  'observables': ['Force a job failure after a known subset of pages or labels completes and inspect recovery scope '
                  'and final duplicate output.'],
  'falsifiers': ['Recovery uses confirmed completion evidence to offer a bounded remainder retry, or explicitly '
                 'states that page-level certainty is unavailable.'],
  'repairs': ['Persist print progress at the strongest trustworthy granularity and construct retry scope from '
              'confirmed incomplete output rather than the original job by default.'],
  'exceptions': [],
  'verification': ['Trigger failures at several positions and verify retry behavior matches the granularity of '
                   'printer evidence without inventing page-level certainty.'],
  'owner_hints': ['designing-printer-selection-and-status'],
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
  'provenance_ids': ['nui-print-output-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.print.layout-overflow-visible-before-submit',
  'domain': 'print',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Print-specific clipping and overflow must be visible in preview before physical output',
  'statement': 'Content that will clip, wrap unexpectedly, overlap margins, split critical rows, or fall outside '
               'printable bounds must be detectable in print preview rather than discovered only after paper output.',
  'intent': 'Make print rendering a verifiable layout state because browser or screen layout can differ materially '
            'from physical pagination.',
  'applies_when': ['The application controls print styles or generated layouts for content that can exceed page '
                   'dimensions, margins, or printer imageable area.'],
  'does_not_apply_when': [],
  'failure_modes': ['The on-screen content looks correct but the print preview hides or fails to reveal clipping and '
                    'pagination defects that appear in output.'],
  'user_impacts': ['Users can waste paper or distribute incomplete documents because critical content is cut off or '
                   'separated from its context.'],
  'observables': ['Render long text, wide tables, large media, and edge-aligned controls through the print '
                  'stylesheet and inspect preview page boxes for overflow.'],
  'falsifiers': ['Preview accurately represents printable bounds and exposes any unavoidable clipping or pagination '
                 'before submission.'],
  'repairs': ['Treat print layout as a dedicated rendered target with page constraints, print-specific overflow '
              'handling, and preview validation.'],
  'exceptions': [],
  'verification': ['Test supported paper sizes, orientations, margins, scaling, localization expansion, and long '
                   'data sets and confirm preview reveals all print-only layout defects.'],
  'owner_hints': ['designing-print-preview'],
  'verifier_hints': ['critiquing-responsive-behavior'],
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
  'provenance_ids': ['nui-print-output-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.print.color-mode-effective-state-visible',
  'domain': 'print',
  'class': 'behavioral',
  'severity': 'moderate',
  'enforcement': 'warn',
  'title': 'Selected color or monochrome print mode must reflect the effective printer capability and job setting',
  'statement': 'If a user selects color, grayscale, monochrome, or another output mode, the UI must reconcile that '
               'choice with printer capabilities and policies instead of leaving an impossible mode apparently '
               'active.',
  'intent': 'Prevent users from expecting color-dependent semantics or cost behavior that the selected printer '
            'cannot actually produce.',
  'applies_when': ['The print workflow exposes color-related options and target printers vary in supported modes, '
                   'policy restrictions, or defaults.'],
  'does_not_apply_when': [],
  'failure_modes': ['The control shows color selected while the target will necessarily print monochrome, or '
                    'silently changes mode without communicating the effective result.'],
  'user_impacts': ['Charts, warnings, branding, accessibility encodings, or cost expectations can change materially '
                   'between intended and physical output.'],
  'observables': ['Switch among printers and policies with different color capabilities while comparing visible '
                  'mode, job ticket, preview, and output.'],
  'falsifiers': ['The shown effective mode matches the submitted job and unsupported choices are disabled, '
                 'explained, or converted with visible consequence.'],
  'repairs': ['Derive mode availability from the active printer capabilities and keep user preference separate from '
              'the effective job setting.'],
  'exceptions': [],
  'verification': ['Test color, monochrome, policy-forced grayscale, printer change, and saved defaults and confirm '
                   'the effective state remains explicit.'],
  'owner_hints': ['designing-printer-selection-and-status'],
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
  'provenance_ids': ['nui-print-output-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.print.confidential-output-destination-warning',
  'domain': 'print',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Confidential print flows must warn when output is sent to an unattended or shared destination',
  'statement': 'When the product knows output contains content marked sensitive and the destination is shared, '
               'remote, or lacks secure release, the final print decision should surface that destination risk '
               'without revealing the protected content itself.',
  'intent': 'Bring physical-output privacy into the same decision boundary as digital access controls when '
            'destination characteristics are known.',
  'applies_when': ['The product carries a sensitivity classification or protected-content context and can identify '
                   'printer location, sharing, or secure-release capability.'],
  'does_not_apply_when': [],
  'failure_modes': ['A sensitive document can be printed to a shared or remote device with no indication that the '
                    'physical destination has weaker privacy properties.'],
  'user_impacts': ['Protected information can be left unattended or exposed to people who never had digital access '
                   'to the source.'],
  'observables': ['Mark representative content sensitive, select personal, shared, remote, and secure-release '
                  'printers, and inspect final confirmation and job routing.'],
  'falsifiers': ['The workflow surfaces known physical-destination risk or enforces a secure destination policy '
                 'appropriate to the declared sensitivity model.'],
  'repairs': ['Combine content sensitivity and printer destination metadata at submission and warn or gate when '
              'policy identifies a material mismatch.'],
  'exceptions': [],
  'verification': ['Test sensitivity changes, printer changes, missing printer metadata, and secure-release '
                   'capability and confirm warnings appear only when supported by evidence.'],
  'owner_hints': ['designing-printer-selection-and-status'],
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
  'provenance_ids': ['nui-print-output-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.print.cancelled-distinct-from-completed',
  'domain': 'print',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Cancelled print jobs must remain distinct from completed jobs in history and status',
  'statement': 'A print job cancelled by the user, spooler, policy, or printer must not be grouped with successfully '
               'completed output merely because it left the application queue.',
  'intent': 'Preserve physical-output history so users can tell whether a requested artifact was actually produced '
            'or intentionally stopped.',
  'applies_when': ['The product displays print history or task status after jobs leave its immediate active queue.'],
  'does_not_apply_when': [],
  'failure_modes': ['Cancelled and completed jobs share the same terminal success state or the cancelled record '
                    'disappears without preserving its outcome.'],
  'user_impacts': ['Users can believe output exists, repeat jobs unnecessarily, or lose an audit trail of '
                   'intentionally prevented printing.'],
  'observables': ['Cancel jobs before submission, in spooler, and at the printer when available and inspect '
                  'application history after refresh.'],
  'falsifiers': ['Cancelled jobs retain a distinct terminal outcome and any partial physical output is represented '
                 'separately when evidence exists.'],
  'repairs': ['Persist terminal print outcome independently of queue membership and map cancellation sources into '
              'explicit non-success states.'],
  'exceptions': [],
  'verification': ['Exercise user cancellation, printer cancellation, policy rejection, and successful completion '
                   'and confirm each remains distinguishable in history.'],
  'owner_hints': ['designing-printer-selection-and-status'],
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
  'provenance_ids': ['nui-print-output-owners-v13'],
  'status': 'active'}]

__all__ = ["PRINT_OUTPUT_RULES_V13"]
