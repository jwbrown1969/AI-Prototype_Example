"""Count screens and copy retention for the pothole-app prototypes.

Usage: python3 count.py   (requires beautifulsoup4: pip install beautifulsoup4)

Screens: every <section> element that has a data-screen attribute.
Copy kept: for a re-render, the share of distinct words (three letters or
longer, case-insensitive) on each screen of the source prototype that also
appear on the same-named screen of the re-render, pooled across all screens.
"""
import re
from pathlib import Path
from bs4 import BeautifulSoup

DIR = Path(__file__).parent / "prototypes"

RUNS = {
    "A": "A_unscoped_polished.html",
    "B": "B_unscoped_sketch.html",
    "B2": "B2_unscoped_sketch_copy_kept.html",
    "C": "C_scoped_sketch.html",
    "D1": "D1_map_first.html",
    "D2": "D2_camera_first.html",
    "D3": "D3_address_first.html",
    "E": "E_scoped_polished.html",
    "F": "F_scoped_three_fidelities.html",
}
RERENDERS = {"B": "A", "B2": "A", "E": "C"}


def screens(name):
    soup = BeautifulSoup((DIR / RUNS[name]).read_text(encoding="utf-8"), "html.parser")
    return {
        s["data-screen"]: re.sub(r"\s+", " ", s.get_text(" ", strip=True))
        for s in soup.find_all("section")
        if s.has_attr("data-screen")
    }


def words(text):
    return set(re.findall(r"[a-z']{3,}", text.lower()))


def copy_kept(source, rerender):
    src, dst = screens(source), screens(rerender)
    total = kept = 0
    for name, text in src.items():
        w = words(text)
        total += len(w)
        kept += len(w & words(dst.get(name, "")))
    return kept, total


if __name__ == "__main__":
    for run in RUNS:
        s = screens(run)
        line = f"{run:3} {len(s):2} screens: {', '.join(s)}"
        if run in RERENDERS:
            k, t = copy_kept(RERENDERS[run], run)
            line += f"\n    copy kept from {RERENDERS[run]}: {k}/{t} = {100 * k / t:.1f}%"
        print(line)
