"""V13 seventh-wave independently authored rules for overlay systems."""
from __future__ import annotations

from ._capabilities import interaction_caps


OVERLAY_SYSTEM_RULES_V13 = [{'rule_id': 'ui.overlay.trigger-anchor-relationship-preserved',
  'domain': 'overlay',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Anchored overlays must remain associated with the trigger that owns their content',
  'statement': 'A popover, tooltip, or menu opened from a trigger should maintain the semantic and spatial '
               'relationship to that trigger as layout changes, or close when the anchor no longer exists.',
  'intent': 'Prevent floating UI from appearing to control or describe the wrong element after reflow or '
            'virtualization.',
  'applies_when': ['An overlay is positioned relative to a control or item that can move, rerender, scroll, '
                   'or unmount while the overlay is open.'],
  'does_not_apply_when': [],
  'failure_modes': ['The anchor row is recycled or removed but the overlay remains at its old screen '
                    'coordinates, now visually attached to a different item.'],
  'user_impacts': ['Users can invoke an action for the wrong resource or misread explanatory content as '
                   'belonging to another control.'],
  'observables': ['Open an anchored overlay, reorder or virtualize the list, resize and scroll, then inspect '
                  'anchor identity and action target.'],
  'falsifiers': ['The overlay tracks the same logical anchor or dismisses safely when that anchor becomes '
                 'invalid; it never silently adopts a replacement row.'],
  'repairs': ['Bind overlay ownership to stable trigger identity and recompute placement only while that '
              'identity remains mounted and valid.'],
  'exceptions': [],
  'verification': ['Exercise scrolling, responsive reflow, virtualization, and remote deletion while '
                   'overlays are open, verifying target identity never drifts.'],
  'owner_hints': ['designing-popover-systems'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-overlay-system-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.overlay.focus-returns-to-logical-trigger',
  'domain': 'overlay',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Closing a temporary overlay must return focus to the logical invoking control or a safe '
           'successor',
  'statement': 'After a menu, popover, or dialog closes, keyboard focus should return to the action context '
               'that opened it unless that trigger was removed, in which case a predictable nearby fallback '
               'is required.',
  'intent': 'Preserve task continuity and avoid dropping keyboard users at the document root after temporary '
            'interaction.',
  'applies_when': ['A keyboard-operable trigger opens a temporary overlay that takes or redirects focus.'],
  'does_not_apply_when': [],
  'failure_modes': ['Closing the overlay sends focus to body, an unrelated control, or a DOM node that was '
                    'removed while the overlay was open.'],
  'user_impacts': ['Keyboard and screen-reader users lose their place and may need to navigate the entire '
                   'interface again.'],
  'observables': ['Open and close overlays by completion, Escape, outside click, and trigger removal while '
                  'tracking active element identity.'],
  'falsifiers': ['Focus returns to the same logical trigger when valid or a documented safe successor when '
                 'the trigger no longer exists.'],
  'repairs': ['Record the logical opener and implement focus restoration against stable identity rather than '
              'raw DOM reference alone.'],
  'exceptions': [],
  'verification': ['Test nested overlays and triggers inside virtualized or conditionally removed content, '
                   'verifying focus never disappears into a noninteractive fallback.'],
  'owner_hints': ['designing-focus-order-and-restoration'],
  'verifier_hints': ['critiquing-accessibility'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-overlay-system-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.overlay.escape-closes-topmost-layer-only',
  'domain': 'overlay',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Escape must dismiss only the topmost dismissible overlay in a nested stack',
  'statement': 'When multiple temporary layers are open, one Escape action should apply to the currently '
               'active dismissible layer rather than collapsing unrelated parent context unless the '
               'interaction model explicitly defines otherwise.',
  'intent': 'Make overlay stacks predictable and prevent accidental loss of a larger task while closing a '
            'small child control.',
  'applies_when': ['A dialog can contain a menu, picker, confirmation, or other nested overlay that also '
                   'responds to Escape.'],
  'does_not_apply_when': [],
  'failure_modes': ['One Escape event bubbles through several handlers and closes the child plus its parent '
                    'dialog or underlying workspace state.'],
  'user_impacts': ['Users can lose unsaved context or unintentionally exit a workflow while attempting to '
                   'close only the active menu.'],
  'observables': ['Open nested dismissible layers and press Escape once at each depth while observing stack '
                  'state and focus restoration.'],
  'falsifiers': ['Exactly the active topmost layer handles the dismissal and propagation stops according to '
                 'the declared stack model.'],
  'repairs': ['Centralize overlay stack ownership and route dismissal to the highest eligible layer before '
              'restoring focus.'],
  'exceptions': [],
  'verification': ['Test menu-in-dialog, popover-in-sheet, and nested confirmation flows, verifying one '
                   'Escape corresponds to one logical dismissal.'],
  'owner_hints': ['designing-dialog-systems'],
  'verifier_hints': ['critiquing-accessibility'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-overlay-system-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.overlay.nested-layer-order-preserves-ownership',
  'domain': 'overlay',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Nested overlays must preserve interaction and visual ownership across stacking contexts',
  'statement': 'A child overlay must remain interactive above the parent surface that owns it, while '
               'unrelated layers must not visually or semantically interleave because of local '
               'stacking-context accidents.',
  'intent': 'Prevent z-index implementation details from breaking the logical modal or popup hierarchy.',
  'applies_when': ['Multiple overlays can nest or coexist across portals, transformed containers, or '
                   'component-specific stacking contexts.'],
  'does_not_apply_when': [],
  'failure_modes': ['A menu opened inside a dialog renders beneath the dialog scrim, or an unrelated toast '
                    'or panel captures input above a modal child.'],
  'user_impacts': ['Users cannot reach the intended control or interact with content that should be inert '
                   'behind an active modal layer.'],
  'observables': ['Open nested layers across components known to create stacking contexts and inspect paint '
                  'order, pointer hit testing, and accessibility exposure.'],
  'falsifiers': ['The rendered and interactive stack follows logical ownership, and background content '
                 'remains inert where the active modality requires it.'],
  'repairs': ['Use a coordinated overlay layer system rather than arbitrary local z-index escalation and '
              'preserve parent-child ownership metadata.'],
  'exceptions': [],
  'verification': ['Exercise combinations of dialog, popover, menu, tooltip, and toast under transforms and '
                   'portals, verifying logical stack order remains stable.'],
  'owner_hints': ['designing-popover-systems'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-overlay-system-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.overlay.viewport-collision-does-not-hide-content',
  'domain': 'overlay',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Overlay collision handling must keep required content and actions reachable inside the viewport',
  'statement': 'When an anchored overlay lacks space in its preferred direction, placement should flip, '
               'shift, resize, or scroll without clipping essential controls beyond reachable viewport '
               'bounds.',
  'intent': 'Keep overlays usable near screen edges, zoomed layouts, and virtual keyboards.',
  'applies_when': ['Menus, popovers, or tooltips can open near viewport edges or inside constrained '
                   'responsive layouts.'],
  'does_not_apply_when': [],
  'failure_modes': ['The overlay preserves its preferred placement even when the confirm button or final '
                    'menu items render off-screen with no internal scroll.'],
  'user_impacts': ['Users cannot complete the interaction and may be trapped in an overlay that is '
                   'technically open but partially unreachable.'],
  'observables': ['Open the overlay at each corner under high zoom, small viewport, and virtual-keyboard '
                  'conditions, then attempt every action.'],
  'falsifiers': ['Essential content remains reachable without two-dimensional page scrolling or hidden '
                 'off-screen controls, and placement still points to the correct anchor.'],
  'repairs': ['Use measured collision detection with bounded shifting, flipping, and internal scrolling '
              'appropriate to the overlay type.'],
  'exceptions': [],
  'verification': ['Test dynamic content growth and localization at constrained sizes, verifying placement '
                   'adapts without losing anchor meaning or actions.'],
  'owner_hints': ['designing-popover-systems'],
  'verifier_hints': ['critiquing-accessibility'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-overlay-system-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.overlay.tooltip-keyboard-parity',
  'domain': 'overlay',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Informational tooltips triggered by hover must have equivalent keyboard access',
  'statement': 'Information necessary to understand a control must not be exposed only through pointer '
               'hover; the same content must be reachable when the trigger receives keyboard focus.',
  'intent': 'Avoid making labels, warnings, or explanations inaccessible to non-pointer users.',
  'applies_when': ['A tooltip contains information that supplements an interactive control or abbreviated '
                   'label.'],
  'does_not_apply_when': [],
  'failure_modes': ['Hover reveals the tooltip but focusing the same trigger via keyboard does nothing or '
                    'closes it before the content can be perceived.'],
  'user_impacts': ['Keyboard and assistive-technology users miss information available to pointer users and '
                   'may make incorrect choices.'],
  'observables': ['Navigate to every tooltip trigger using keyboard only and compare content, timing, '
                  'dismissal, and accessible relationship with hover behavior.'],
  'falsifiers': ['The same informational content is available on focus or through an equivalent accessible '
                 'mechanism without requiring pointer precision.'],
  'repairs': ['Wire tooltip disclosure to both hover and focus semantics and expose the relationship through '
              'appropriate accessible description behavior.'],
  'exceptions': [],
  'verification': ['Test keyboard, screen reader, touch, and magnification paths, confirming no required '
                   'information exists only in hover state.'],
  'owner_hints': ['designing-tooltip-systems'],
  'verifier_hints': ['critiquing-accessibility'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-overlay-system-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.overlay.context-menu-target-remains-stable',
  'domain': 'overlay',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Context-menu actions must stay bound to the item that was invoked even if selection changes',
  'statement': 'Opening a context menu on a resource must establish a stable action target so later '
               'selection movement or background updates cannot silently redirect menu commands.',
  'intent': 'Prevent destructive or modifying commands from applying to a different item than the one under '
            'the user’s invocation.',
  'applies_when': ['Context menus can be opened on list, tree, canvas, or table items while global selection '
                   'can change independently.'],
  'does_not_apply_when': [],
  'failure_modes': ['The user right-clicks item A, keyboard focus moves to B, then choosing Delete from the '
                    'still-open menu deletes B because the command reads current selection.'],
  'user_impacts': ['Users can modify or destroy an unintended resource despite opening the command menu on a '
                   'specific target.'],
  'observables': ['Open a context menu on one item, change selection from another client or keyboard path, '
                  'and then invoke each menu action.'],
  'falsifiers': ['Menu actions resolve to the invocation target or explicitly indicate that they act on the '
                 'broader selection set shown at open time.'],
  'repairs': ['Capture stable target identity and selection scope when the menu opens and pass that context '
              'into every command.'],
  'exceptions': [],
  'verification': ['Race selection changes, item moves, and remote deletion while context menus remain open, '
                   'verifying commands never retarget silently.'],
  'owner_hints': ['designing-context-menus'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-overlay-system-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.overlay.cascading-menu-intent-tolerates-pointer-path',
  'domain': 'overlay',
  'class': 'behavioral',
  'severity': 'moderate',
  'enforcement': 'warn',
  'title': 'Cascading menus must tolerate diagonal pointer travel toward an open submenu',
  'statement': 'A submenu should remain open while the pointer travels through the geometric corridor toward '
               'it instead of collapsing immediately when the pointer briefly leaves the parent item.',
  'intent': 'Make hierarchical menu targets reachable without requiring unrealistically precise orthogonal '
            'pointer motion.',
  'applies_when': ['A desktop-style menu opens a submenu beside the parent menu and users move the pointer '
                   'diagonally between them.'],
  'does_not_apply_when': [],
  'failure_modes': ['The submenu closes as soon as the pointer crosses another parent row, causing repeated '
                    'accidental menu switching during normal diagonal travel.'],
  'user_impacts': ['Users struggle to reach nested commands and may trigger a neighboring submenu or abandon '
                   'the action.'],
  'observables': ['Open submenus at different vertical positions and move the pointer diagonally at normal '
                  'speeds across the gap toward several child targets.'],
  'falsifiers': ['Reasonable motion toward the active submenu keeps it open while deliberate movement toward '
                 'another parent item still switches promptly.'],
  'repairs': ['Use directional intent or a bounded grace corridor rather than a fixed indiscriminate delay '
              'for submenu switching.'],
  'exceptions': [],
  'verification': ['Test fast and slow movement, narrow and wide submenus, and viewport-flipped placement, '
                   'verifying tolerance follows the actual submenu geometry.'],
  'owner_hints': ['designing-cascading-menus'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-overlay-system-owners-v13'],
  'status': 'active'}]

__all__ = ["OVERLAY_SYSTEM_RULES_V13"]
