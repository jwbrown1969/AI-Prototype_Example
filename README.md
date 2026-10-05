# AI Prototype Example: one pothole app, seven prompts

Companion demonstration for the Human Factors Brief article "A Sketch of Everything."

Open `index.html` for the guided page. Each prototype in `prototypes/` was generated on October 5, 2026 by a general-purpose AI model in a fresh session that had seen none of the others. The prototypes are unedited. Exact prompts are in `prompts.md`.

## Results

| Run | Prompt asked for | Screens | Original copy kept | Generation time |
|---|---|---|---|---|
| A | The app, no scope, no style | 11 | n/a | 212 s |
| B | A re-rendered as a sketch "with placeholder text" | 11 | 4% | 95 s |
| B2 | A re-rendered as a sketch, keeping every label and line of copy | 11 | 100% | 173 s |
| C | Scoped to one task, three screens maximum, sketch | 3 | n/a | 37 s |
| D1–D3 | Same scope, three different starting points, sketch | 3 each | n/a | 57 s, 45 s, 42 s |

Screens are counted from `<section class="screen">` tags. "Copy kept" is the share of distinct words (three letters or longer) on each screen of A that also appear on the same screen of the re-render, pooled across all eleven screens. Generation time is the wall-clock duration of each generation session, including the model writing the file.

## Limits

One flow, one model, one run per prompt. The demonstration shows that scope and style are separate controls and that a style instruction can change content as well as appearance. It does not measure what participants would say about any version.

## Viewing on GitHub Pages

Settings → Pages → Deploy from branch → `main`, folder `/ (root)`. The page will then be served at `https://jwbrown1969.github.io/AI-Prototype_Example/`.

*Opinions are my own and do not represent my employer.*
