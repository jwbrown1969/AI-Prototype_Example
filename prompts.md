# Exact prompts

Every prompt below ended with the same technical block, which is not repeated each time:

> Output requirements (technical only): write a single self-contained HTML file (inline CSS and JS, no external assets) to [path]. Wrap each distinct screen in `<section class="screen" data-screen="SHORT-NAME">` so screens can be counted. Do not ask questions; make your own decisions. When done, reply with only a list of the data-screen names you created.

## A: unscoped

Build a clickable prototype of a mobile web app that lets residents report potholes to their city.

## B: re-render with placeholder text

Re-render the prototype in prototypes/A_unscoped_polished.html as a hand-drawn grayscale wireframe with placeholder text, no color or imagery.

## B2: re-render keeping copy

Re-render the prototype in prototypes/A_unscoped_polished.html as a hand-drawn grayscale wireframe, no color or imagery. Keep every screen, label, question, option, and line of copy exactly as it appears in the original.

## C: scoped sketch

Build a clickable prototype of a mobile web app that lets residents report potholes to their city.

Scope: one task only. A resident reports a single pothole: marks its location, optionally adds a photo, and receives a confirmation. Three screens maximum. Out of scope: accounts or sign-in, report history, status tracking, notifications, settings, onboarding, and any other feature.

Render it as a hand-drawn grayscale wireframe with placeholder text, no color or imagery.

## D1, D2, D3: scoped alternatives

The C prompt, with one line added before the render instruction:

- D1: Design approach: map-first. The resident starts by placing the pothole on a map.
- D2: Design approach: camera-first. The resident starts by taking a photo, and location comes from the photo or the device.
- D3: Design approach: address-first. The resident starts by typing or confirming a street address or nearest intersection.

## E: scoped sketch re-rendered as polished

Re-render the prototype in prototypes/C_scoped_sketch.html as a polished, finished-looking mobile interface with real visual design: color, typography, and icons. Keep every screen, label, question, option, and line of copy exactly as it appears in the original.
