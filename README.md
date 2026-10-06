# AI Prototype Example: one pothole app, eight prompts

Companion demonstration for the Human Factors Brief article "Scope Is the Skill."

The argument it supports: overdesign in AI prototyping follows the prompt. Given no scope, a model fills in a full product; given a stated task, a screen limit, and what is out of scope, it builds the small thing. Fidelity can then be set by prompt in either direction.

Open `index.html` for the guided page. Each prototype in `prototypes/` was generated on October 5, 2026 by a general-purpose AI model, each in its own session. Runs A, C, and D1–D3 were fresh generations. B and B2 were each given A's file to re-render, and E was given C's file to re-render; none saw anything else. The prototypes are unedited. Exact prompts, including the technical block every prompt shared, are in `prompts.md`.

## Results

| Run | Prompt asked for | Screens | Original copy kept | Generation time |
|---|---|---|---|---|
| A | The app, no scope, no style | 11 | n/a | 212 s |
| B | A re-rendered as a sketch "with placeholder text" | 11 | 4% | 95 s |
| B2 | A re-rendered as a sketch, keeping every label and line of copy | 11 | 100% | 173 s |
| C | Scoped to one task, three screens maximum, sketch | 3 | n/a | 37 s |
| D1–D3 | Same scope, three different starting points, sketch | 3 each | n/a | 57 s, 45 s, 42 s |
| E | C re-rendered as a polished interface, keeping every label and line of copy | 3 | 100% | 105 s |

Every prompt, scoped or not, ended with the same technical block, which includes "Do not ask questions; make your own decisions." Apart from C's rendering instruction (a hand-drawn grayscale wireframe), scope was the only difference between the prompts for A and C.

Unrequested additions in the scoped builds: C, D1, and D2 each added an optional note field; D1 added an address search and "No account needed"; D3 added an optional rough-size choice; E added street labels and zoom buttons to the map. Placeholder text varied: D2 filled its body copy with lorem ipsum, and C and E use it in the note field's placeholder.

## Reproducing the counts

`python3 count.py` (requires `beautifulsoup4`). Screens are the `<section>` elements carrying a `data-screen` attribute, whatever other classes they have. "Copy kept" is the share of distinct words (three letters or longer) on each screen of the source prototype that also appear on the same-named screen of the re-render, pooled across all screens. Generation time is the wall-clock duration of each generation session, including the model writing the file.

## Limits

One flow, one model, one run per prompt. Another run could return a different screen count or keep more or less copy. The demonstration does not measure what participants would say about any version.

*Opinions are my own and do not represent my employer.*
