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

## F: scoped, three fidelities in one build (generated October 6, 2026)

Build a clickable prototype of a mobile web app that lets residents report potholes to their city.

Scope: one task only. A resident reports a single pothole: marks its location, optionally adds a photo, and receives a confirmation. Three screens maximum. Out of scope: accounts or sign-in, report history, status tracking, notifications, settings, onboarding, and any other feature.

Fidelity: build the prototype once, with a control that switches the whole prototype between three fidelities. Switching must not change the screens, the flow, or any wording; every fidelity uses the same real copy.
1. Sketch: hand-drawn look, wobbly lines, handwriting-style font, grayscale.
2. Wireframe: crisp gray boxes, system font, consistent grid, one accent color marking what can be tapped.
3. Polished: finished visual design with color, typography, and icons.

## Follow-up rounds (generated October 6, 2026)

Each round ran in a fresh session given only the original request, the current prototype file, and one follow-up message, framed as: "You are continuing a prototyping conversation. The user's original request was: [original request]. The current prototype is the file [path]. The user's next message is: [follow-up]. Respond by producing the updated prototype." Each ended with the same technical block as above.

- Unscoped arm: original request is prompt A; starts from A_unscoped_polished.html; produces U1, U2, U3.
- Scoped arm: original request is prompt C without its rendering line (the build prompt plus the scope paragraph); starts from E_scoped_polished.html; produces S1, S2, S3.

Follow-ups, in order, identical for both arms:

1. This is good. Make it better.
2. What else would residents want from an app like this? Add it.
3. Make it production-ready.
