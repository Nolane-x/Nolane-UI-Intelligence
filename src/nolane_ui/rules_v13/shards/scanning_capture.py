"""V13 seventh-wave independently authored rules for scanning capture."""
from __future__ import annotations

from ._capabilities import interaction_caps


SCANNING_CAPTURE_RULES_V13 = [{'rule_id': 'ui.scanning.camera-permission-recovery-path',
  'domain': 'scanning',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Scanner flows must provide a recovery path when camera permission is denied or unavailable',
  'statement': 'A QR, barcode, or document scanning experience must distinguish permission denial, missing '
               'camera capability, and transient device failure and offer the appropriate recovery or '
               'alternate input path.',
  'intent': 'Keep scanning workflows usable without misrepresenting every camera failure as the same '
            'problem.',
  'applies_when': ['A scan flow depends on camera access that may be denied, revoked, unavailable, or '
                   'unsupported.'],
  'does_not_apply_when': [],
  'failure_modes': ['The scanner remains black with a generic error after denial and gives no route to '
                    'settings, file upload, manual code entry, or retry.'],
  'user_impacts': ['Users can become trapped in verification, inventory, or document workflows because the '
                   'product cannot explain the capability boundary.'],
  'observables': ['Test prompt denial, later revocation, no-camera devices, busy camera, and transient '
                  'initialization failure.'],
  'falsifiers': ['Each failure class has truthful feedback and a viable policy-appropriate recovery or '
                 'fallback when one exists.'],
  'repairs': ['Map platform permission and device capability states separately and design recovery actions '
              'for each supported failure path.'],
  'exceptions': [],
  'verification': ['Exercise denial before and after prior grant plus device unavailability, verifying the '
                   'scanner never claims permission success when capture cannot start.'],
  'owner_hints': ['designing-camera-capture-flows'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-scanning-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.scanning.symbology-mismatch-explained',
  'domain': 'scanning',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Barcode scanners must distinguish unsupported code formats from unreadable captures',
  'statement': 'When a captured barcode is valid but its symbology is outside the product’s supported set, '
               'the UI should not report only “scan failed” as though image quality were the problem.',
  'intent': 'Give users the correct recovery path between recapture and using another code format.',
  'applies_when': ['A scanner supports a known subset of QR, 1D, 2D, or domain-specific code symbologies.'],
  'does_not_apply_when': [],
  'failure_modes': ['An unsupported but clearly detected code repeatedly triggers generic blur or alignment '
                    'guidance.'],
  'user_impacts': ['Users waste time recapturing a code the product can never parse.'],
  'observables': ['Present supported, unsupported, damaged, and blurred codes under controlled lighting and '
                  'inspect error classification and guidance.'],
  'falsifiers': ['Unsupported format is distinguishable from capture quality failure when the decoder can '
                 'establish that distinction.'],
  'repairs': ['Propagate decoder capability or format-detection errors into user-facing recovery rather than '
              'collapsing every nonresult into one message.'],
  'exceptions': [],
  'verification': ['Test several supported and unsupported symbologies, verifying recapture guidance appears '
                   'only where another capture could actually help.'],
  'owner_hints': ['designing-barcode-scanning'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-scanning-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.scanning.duplicate-scan-debounced-by-result-identity',
  'domain': 'scanning',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Continuous scanners must debounce repeated reads of the same physical code by logical result '
           'identity',
  'statement': 'A camera stream that sees the same code across many frames should not create repeated '
               'authoritative actions unless the workflow explicitly requires repeat counting.',
  'intent': 'Prevent duplicate inventory, navigation, or verification actions caused by frame-level '
            'detection repetition.',
  'applies_when': ['Scanning remains live after a code is detected and the same target can stay in view for '
                   'multiple frames.'],
  'does_not_apply_when': [],
  'failure_modes': ['One QR code produces several add-item or navigate events because every decoded frame is '
                    'treated as a new user intent.'],
  'user_impacts': ['Users can create duplicate records, overcount stock, or trigger repeated transitions '
                   'without moving the camera.'],
  'observables': ['Hold one code steadily in view, remove and reintroduce it, and compare decoder events '
                  'with committed workflow actions.'],
  'falsifiers': ['One logical scan produces one action within the declared debounce/session policy, while a '
                 'deliberate later rescan can still be recognized.'],
  'repairs': ['Separate frame detections from logical scan events using result identity plus a bounded reset '
              'condition appropriate to the task.'],
  'exceptions': [],
  'verification': ['Test stationary codes, rapid different codes, and remove-return patterns, verifying '
                   'action count follows user intent rather than frame rate.'],
  'owner_hints': ['designing-barcode-scanning'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-scanning-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.scanning.scan-result-reviewed-before-consequential-action',
  'domain': 'scanning',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Scanned content must be reviewable before it triggers a consequential external action',
  'statement': 'A decoded QR, barcode, or document value should not automatically perform payment, '
               'navigation, account change, or submission when the encoded target is consequential and not '
               'already trusted by policy.',
  'intent': 'Keep untrusted physical input from bypassing the normal decision boundary.',
  'applies_when': ['A scan can resolve to URLs, payment destinations, account identifiers, configuration, or '
                   'other consequential targets.'],
  'does_not_apply_when': [],
  'failure_modes': ['Pointing the camera at a code immediately opens an external URL or submits an action '
                    'before the user can inspect the decoded destination.'],
  'user_impacts': ['Malicious or mistaken codes can redirect users or initiate unintended operations.'],
  'observables': ['Scan benign and deliberately misleading targets and observe whether decoded content is '
                  'presented before any external or authoritative transition.'],
  'falsifiers': ['The product exposes enough decoded target context for a decision and requires the normal '
                 'confirmation appropriate to that action class.'],
  'repairs': ['Insert a result-review boundary between decoding and consequential execution, with '
              'trusted-policy exceptions documented separately.'],
  'exceptions': [],
  'verification': ['Test URLs, payment-like payloads, identifiers, and malformed codes, verifying scanning '
                   'alone never grants more authority than manual entry.'],
  'owner_hints': ['designing-qr-code-scanning'],
  'verifier_hints': ['critiquing-security-and-privacy'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-scanning-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.scanning.document-crop-preview-before-save',
  'domain': 'scanning',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Document scanning must preview detected crop and orientation before committing the page',
  'statement': 'Auto edge detection, rotation, and perspective correction should remain reviewable before '
               'the processed scan replaces or uploads the captured image.',
  'intent': 'Prevent automated image cleanup from clipping signatures, margins, labels, or other required '
            'document content.',
  'applies_when': ['Document capture applies automatic crop, rotation, deskew, or perspective '
                   'transformations.'],
  'does_not_apply_when': [],
  'failure_modes': ['The scanner commits an incorrect crop immediately, removing edge content with no way to '
                    'compare against the source capture.'],
  'user_impacts': ['Users can submit incomplete documents even though the camera captured the missing '
                   'content correctly.'],
  'observables': ['Capture documents with difficult edges and orientation, then compare raw image, processed '
                  'preview, edit controls, and saved artifact.'],
  'falsifiers': ['Users can inspect and correct the proposed transform before final save or upload, and the '
                 'source remains recoverable until that decision.'],
  'repairs': ['Keep original capture plus transform parameters through the review step and apply destructive '
              'processing only after acceptance.'],
  'exceptions': [],
  'verification': ['Test low-contrast edges, shadows, folded pages, and rotated documents, confirming '
                   'automated processing never silently becomes final.'],
  'owner_hints': ['designing-document-scanning-capture'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-scanning-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.scanning.multi-page-order-preserved',
  'domain': 'scanning',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Multi-page scanning must preserve and expose page order before final document assembly',
  'statement': 'A multi-page scan workflow must show stable page identity and ordering so retakes, '
               'insertions, and deletions do not silently scramble the final document.',
  'intent': 'Protect document meaning when page sequence carries legal or operational significance.',
  'applies_when': ['The scanner assembles several captured pages into one artifact and supports retake or '
                   'reorder.'],
  'does_not_apply_when': [],
  'failure_modes': ['Retaking page two appends it as page five or recycled thumbnails cause a drag reorder '
                    'to affect the wrong captured page.'],
  'user_impacts': ['Users can submit contracts, forms, or evidence with pages out of sequence or missing.'],
  'observables': ['Capture several uniquely marked pages, retake and reorder middle pages, then inspect '
                  'preview order and final artifact.'],
  'falsifiers': ['Each captured page has stable identity and the final assembled order exactly matches the '
                 'reviewed sequence.'],
  'repairs': ['Model page identity separately from list position and perform retake as replacement of a '
              'chosen page rather than ambiguous insertion.'],
  'exceptions': [],
  'verification': ['Exercise insert, delete, retake, and drag reorder, verifying exported PDF/image sequence '
                   'remains identical to the final preview.'],
  'owner_hints': ['designing-document-scanning-capture'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-scanning-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.scanning.low-quality-capture-recapture-path',
  'domain': 'scanning',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Low-quality scan detection must offer recapture without discarding the prior usable image '
           'prematurely',
  'statement': 'When blur, glare, occlusion, or low resolution is detected, users should be able to compare '
               'or recapture while the existing image remains available until a replacement succeeds.',
  'intent': 'Avoid turning quality assistance into accidental data loss during difficult capture conditions.',
  'applies_when': ['The scanner evaluates capture quality and may recommend or require a retake.'],
  'does_not_apply_when': [],
  'failure_modes': ['Selecting Retake immediately deletes the only captured page and the next camera attempt '
                    'fails or permission is lost.'],
  'user_impacts': ['Users can lose a partially usable document and have to restart a multi-page workflow.'],
  'observables': ['Capture a marginal page, start retake, then simulate camera failure, cancellation, and '
                  'successful replacement.'],
  'falsifiers': ['The prior capture remains recoverable until a new accepted capture replaces it according '
                 'to an explicit decision.'],
  'repairs': ['Treat retake as a staged replacement with old and candidate image identities rather than '
              'destructive delete-before-capture.'],
  'exceptions': [],
  'verification': ['Test repeated failed retakes and app backgrounding, confirming page state survives until '
                   'the user accepts a replacement.'],
  'owner_hints': ['designing-document-scanning-capture'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-scanning-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.scanning.sensitive-capture-retention-visible',
  'domain': 'scanning',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Scanning sensitive documents must communicate whether raw captures remain on device, upload, or '
           'temporary storage',
  'statement': 'When captured identity, financial, health, or confidential documents are processed, the UI '
               'should not imply immediate disposal if raw images are retained for retry, upload, or '
               'processing.',
  'intent': 'Make sensitive-file lifecycle understandable at the capture boundary without claiming deletion '
            'that has not occurred.',
  'applies_when': ['The scan flow handles sensitive documents and may stage raw images locally or remotely '
                   'before final processing.'],
  'does_not_apply_when': [],
  'failure_modes': ['The interface says “processed securely” or clears the preview while raw captures remain '
                    'in cache or upload staging with no retention explanation.'],
  'user_impacts': ['Users can misunderstand where highly sensitive imagery persists and what deleting the '
                   'final document actually removes.'],
  'observables': ['Capture a sensitive document, cancel at different stages, inspect supported retention '
                  'controls and backend/local lifecycle behavior.'],
  'falsifiers': ['The product communicates the relevant retention or deletion boundary and cancellation '
                 'removes data according to that stated policy.'],
  'repairs': ['Define raw-capture lifecycle explicitly and connect user-facing delete/cancel actions to the '
              'actual local and remote storage transitions.'],
  'exceptions': [],
  'verification': ['Test cancellation before upload, during processing, and after finalization, verifying '
                   'stated retention matches observable storage behavior.'],
  'owner_hints': ['designing-sensitive-file-handling'],
  'verifier_hints': ['critiquing-security-and-privacy'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-scanning-owners-v13'],
  'status': 'active'}]

__all__ = ["SCANNING_CAPTURE_RULES_V13"]
