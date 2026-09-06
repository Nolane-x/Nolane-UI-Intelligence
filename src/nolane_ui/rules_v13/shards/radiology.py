"""V13 eighth-wave independently authored rules for radiology."""
from __future__ import annotations

from ._capabilities import interaction_caps


RADIOLOGY_RULES_V13 = [{'rule_id': 'ui.radiology.study-patient-accession-identity-bound',
  'domain': 'radiology',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Radiology studies must keep patient, accession, and study identity bound across navigation',
  'statement': 'Images, reports, measurements, and actions must remain attached to the exact study and '
               'accession under review even when the viewer preloads adjacent examinations.',
  'intent': 'Prevent cross-study or cross-patient interpretation caused by viewer context drift.',
  'applies_when': ['Radiology workspaces allow rapid navigation across multiple studies, series, and '
                   'patients.'],
  'does_not_apply_when': [],
  'failure_modes': ['A viewer preloads the next study and the report panel updates before the image '
                    'canvas, leaving the current images paired with another accession.'],
  'user_impacts': ['Clinicians can interpret or report images under the wrong patient or examination '
                   'identity.'],
  'observables': ['Navigate rapidly through similarly named studies while delaying image and report '
                  'loads and compare visible identity headers on every surface.'],
  'falsifiers': ['All study-dependent panes expose one consistent patient and accession identity, and '
                 'mismatched partial loads are blocked or clearly unavailable.'],
  'repairs': ['Bind every viewer substate and command to immutable study and accession identifiers '
              'instead of shared mutable selection state.'],
  'exceptions': [],
  'verification': ['Race study switching with image, report, and metadata loading, verifying no '
                   'mixed-study composite can appear authoritative.'],
  'owner_hints': ['designing-radiology-study-navigation'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-radiology-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.radiology.preliminary-distinct-from-final-report',
  'domain': 'radiology',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Preliminary radiology reports must remain distinct from final signed reports',
  'statement': 'An unsigned or preliminary interpretation can guide care but must not be rendered as '
               'equivalent to the final report after verification or attending sign-off.',
  'intent': 'Preserve the evidentiary and workflow status of radiology interpretation.',
  'applies_when': ['Radiology reporting workflows can publish preliminary, trainee, attending, '
                   'corrected, and final reports.'],
  'does_not_apply_when': [],
  'failure_modes': ['A preliminary resident report appears in the chart as final and later changes '
                    'after attending review with no preserved status transition.'],
  'user_impacts': ['Clinical decisions can rely on an interpretation whose provisional status was '
                   'hidden.'],
  'observables': ['Publish preliminary and final report versions and inspect viewer, chart summary, '
                  'notifications, and historical report access.'],
  'falsifiers': ['Current report status is visible and superseded preliminary content remains traceable '
                 'when the workflow retains it.'],
  'repairs': ['Model report versions and signature authority explicitly and propagate status to every '
              'consumer surface.'],
  'exceptions': [],
  'verification': ['Transition reports through preliminary, final, addendum, and correction states and '
                   'verify status and version history remain coherent.'],
  'owner_hints': ['designing-radiology-study-navigation'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-radiology-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.radiology.image-series-completeness-visible',
  'domain': 'radiology',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Radiology viewers must expose whether all expected image series are available and loaded',
  'statement': 'A study can be partially transferred or still acquiring images, so the interface must '
               'not imply that the visible series list represents a complete examination unless '
               'completeness is known.',
  'intent': 'Prevent interpretation from treating an incomplete image set as the full study.',
  'applies_when': ['Imaging studies can arrive incrementally from PACS, scanners, archives, or external '
                   'facilities.'],
  'does_not_apply_when': [],
  'failure_modes': ['Only three of five expected series load, but the viewer shows a normal ready state '
                    'with no indication that two series are still unavailable.'],
  'user_impacts': ['Clinicians can miss pathology or make incomplete interpretations without knowing '
                   'the study transfer is partial.'],
  'observables': ['Load studies with delayed, failed, and incremental series transfer and inspect '
                  'series counts, study readiness, and report actions.'],
  'falsifiers': ['The viewer distinguishes complete, partially available, still acquiring, and failed '
                 'series states and identifies missing expected content when known.'],
  'repairs': ['Track study and series transfer completeness independently from currently rendered '
              'images and expose incomplete acquisition or retrieval explicitly.'],
  'exceptions': [],
  'verification': ['Exercise partial transfers and late-arriving series, verifying readiness only '
                   'becomes complete when the expected study content is actually available.'],
  'owner_hints': ['designing-radiology-study-navigation'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-radiology-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.radiology.measurement-unit-and-frame-preserved',
  'domain': 'radiology',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Radiology measurements must preserve unit, image frame, and referenced geometry',
  'statement': 'A numeric measurement has meaning only when tied to the exact image or frame, '
               'calibration, orientation, and unit used to create it.',
  'intent': 'Keep measurements reproducible and prevent annotations from floating onto unrelated '
            'images.',
  'applies_when': ['Radiology viewers allow distance, area, angle, time, SUV-like, or other '
                   'measurements on images and frames.'],
  'does_not_apply_when': [],
  'failure_modes': ['A lesion measurement remains visible after switching to another frame but the '
                    'annotation no longer points to the source image or displays its calibration unit.'],
  'user_impacts': ['Clinicians can compare or communicate measurements that are detached from the '
                   'anatomy and acquisition context that produced them.'],
  'observables': ['Create measurements across series and frames, then navigate, rescale, export, and '
                  'reopen the study while checking references.'],
  'falsifiers': ['Every measurement retains source series, image or frame, geometry, calibration '
                 'context, and unit and reopens on the correct content.'],
  'repairs': ['Persist measurements with stable image/frame identifiers and calibration metadata rather '
              'than screen coordinates alone.'],
  'exceptions': [],
  'verification': ['Measure, navigate, reload, and export across different modalities, verifying each '
                   'annotation resolves to its original geometry and unit.'],
  'owner_hints': ['designing-radiology-study-navigation'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-radiology-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.radiology.comparison-study-identity-visible',
  'domain': 'radiology',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Comparison imaging must make prior-study identity and acquisition time continuously visible',
  'statement': 'When current and prior examinations are viewed together, the interface should make it '
               'difficult to confuse which pane or series belongs to which study date and accession.',
  'intent': 'Prevent current-versus-prior inversion during diagnostic comparison.',
  'applies_when': ['Radiology viewers support side-by-side or synchronized comparison with prior '
                   'studies.'],
  'does_not_apply_when': [],
  'failure_modes': ['Two nearly identical CT examinations are shown side by side but one pane loses its '
                    'date label after fullscreen, causing the prior study to be mistaken for the '
                    'current exam.'],
  'user_impacts': ['Clinicians can report change in the wrong direction or attribute findings to the '
                   'wrong episode.'],
  'observables': ['Open several same-protocol prior studies and test fullscreen, linked scrolling, '
                  'hanging protocols, and pane rearrangement.'],
  'falsifiers': ['Each comparison pane retains study date and identity context through layout changes '
                 'and synchronized navigation.'],
  'repairs': ['Anchor comparison metadata to pane content identity and preserve it when layouts or '
              'viewport modes change.'],
  'exceptions': [],
  'verification': ['Compare multiple temporally adjacent studies and verify current/prior identity '
                   'remains unambiguous in every viewer mode.'],
  'owner_hints': ['designing-radiology-study-navigation'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-radiology-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.radiology.hanging-protocol-fallback-visible',
  'domain': 'radiology',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Failure to apply the intended radiology hanging protocol must be explicit rather than '
           'silently substituting a layout',
  'statement': 'If the preferred study layout cannot be constructed because required series or metadata '
               'are missing, the viewer should disclose that it fell back to another arrangement.',
  'intent': 'Keep layout automation from implying that expected diagnostic views are present when they '
            'are not.',
  'applies_when': ['Radiology viewers automatically choose layouts based on modality, protocol, prior '
                   'studies, and series metadata.'],
  'does_not_apply_when': [],
  'failure_modes': ['The configured chest CT hanging protocol fails because a reconstruction series is '
                    'absent, and the viewer silently opens a generic four-up layout.'],
  'user_impacts': ['Clinicians can assume an expected sequence or comparison is present and overlook '
                   'missing diagnostic content.'],
  'observables': ['Remove required series or metadata and inspect hanging-protocol selection, fallback '
                  'labels, and available-series controls.'],
  'falsifiers': ['The viewer identifies when the intended protocol could not be satisfied and exposes '
                 'the missing dependency or chosen fallback.'],
  'repairs': ['Make hanging-protocol resolution observable and treat fallback as a distinct viewer '
              'state instead of an invisible implementation detail.'],
  'exceptions': [],
  'verification': ['Run complete and incomplete study fixtures and verify each fallback is disclosed '
                   'with enough context to recover the intended layout.'],
  'owner_hints': ['designing-radiology-study-navigation'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-radiology-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.radiology.laterality-orientation-preserved',
  'domain': 'radiology',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Laterality and image orientation must remain preserved through radiology display '
           'transformations',
  'statement': 'Flips, rotations, reformats, mirrored displays, and derived images must not detach or '
               'contradict the orientation and laterality metadata needed to interpret anatomy safely.',
  'intent': 'Prevent transformed presentation from creating a false left-right or directional '
            'interpretation.',
  'applies_when': ['Radiology viewers support orientation transforms, MPR, reformats, image inversion, '
                   'or imported secondary captures.'],
  'does_not_apply_when': [],
  'failure_modes': ['An image is horizontally flipped for display but the laterality marker remains in '
                    'its prior screen position and now labels the opposite side.'],
  'user_impacts': ['Clinicians can localize findings to the wrong side or direction because display '
                   'transformation and orientation metadata diverged.'],
  'observables': ['Apply supported transforms to images with known orientation markers and compare '
                  'overlays, metadata, screenshots, and exports.'],
  'falsifiers': ['Orientation and laterality annotations remain consistent with the transformed image '
                 'geometry or the transform is clearly represented.'],
  'repairs': ['Derive displayed orientation markers from image-space transforms and authoritative '
              'metadata rather than treating them as fixed viewport decorations.'],
  'exceptions': [],
  'verification': ['Test rotations, flips, MPR views, and exports with known orientation fixtures, '
                   'verifying left-right and directional meaning never invert silently.'],
  'owner_hints': ['designing-radiology-study-navigation'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-radiology-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.radiology.partial-study-load-visible',
  'domain': 'radiology',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Partial radiology study loading must remain distinct from a fully loaded diagnostic '
           'workspace',
  'statement': 'A viewer may have metadata, thumbnails, reports, or some pixels before all diagnostic '
               'image data are available; the interface must expose that partial state.',
  'intent': 'Prevent clinicians from interpreting a partially loaded study as complete simply because '
            'the viewer is interactive.',
  'applies_when': ['Large or remote studies load in stages and individual series can fail '
                   'independently.'],
  'does_not_apply_when': [],
  'failure_modes': ['Thumbnails and report text load immediately while high-resolution images for one '
                    'series fail, yet the viewer removes all loading indicators.'],
  'user_impacts': ['Clinicians can begin interpretation without realizing diagnostic pixels are '
                   'incomplete or unavailable.'],
  'observables': ['Throttle and fail image retrieval at different layers while inspecting series list '
                  'state, viewport readiness, and report-signing controls.'],
  'falsifiers': ['Partial load, failed load, and complete diagnostic readiness are separate states, and '
                 'unavailable content remains represented rather than disappearing.'],
  'repairs': ['Track readiness per series and viewport and aggregate it into an explicit study-level '
              'completeness state.'],
  'exceptions': [],
  'verification': ['Open large remote studies under partial failure and verify diagnostic readiness is '
                   'declared only when required pixels and series are actually available.'],
  'owner_hints': ['designing-radiology-study-navigation'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-radiology-owners-v13'],
  'status': 'active'}]


__all__ = ["RADIOLOGY_RULES_V13"]
