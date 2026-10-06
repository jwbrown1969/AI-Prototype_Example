"""Render one PNG per screen for each prototype (and per fidelity for F).

Usage: python3 render_thumbs.py   (requires playwright and Pillow)
Each screen is shown by hiding every other data-screen section; nothing in
the prototype files is changed.
"""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright
from PIL import Image

ROOT = Path(__file__).parent
SRC = ROOT / "prototypes"
OUT = ROOT / "thumbs"
OUT.mkdir(exist_ok=True)

JOBS = {
    "A": ("A_unscoped_polished.html", [None]),
    "C": ("C_scoped_sketch.html", [None]),
    "D1": ("D1_map_first.html", [None]),
    "D2": ("D2_camera_first.html", [None]),
    "D3": ("D3_address_first.html", [None]),
    "B": ("B_unscoped_sketch.html", [None]),
    "F": ("F_scoped_three_fidelities.html", ["sketch", "wireframe", "polished"]),
    "U1": ("U1_unscoped_round1.html", [None]),
    "U2": ("U2_unscoped_round2.html", [None]),
    "U3": ("U3_unscoped_round3.html", [None]),
    "S1": ("S1_scoped_round1.html", [None]),
    "S2": ("S2_scoped_round2.html", [None]),
    "S3": ("S3_scoped_round3.html", [None]),
}

ELEMENT_SHOTS = {"B"}

SHOW = """
(name) => {
  const all = [...document.querySelectorAll('section[data-screen]')];
  for (const s of all) {
    const on = s.dataset.screen === name;
    s.hidden = !on;
    s.style.setProperty('display', on ? 'block' : 'none', 'important');
    if (on) {
      for (const p of ['position','transform','opacity','visibility','left','right','top']) s.style.removeProperty(p);
      s.style.setProperty('position', 'relative', 'important');
      s.style.setProperty('transform', 'none', 'important');
      s.style.setProperty('opacity', '1', 'important');
      s.style.setProperty('visibility', 'visible', 'important');
      s.style.setProperty('inset', 'auto', 'important');
      s.classList.add('active', 'is-active', 'current');
    }
  }
  window.scrollTo(0, 0);
}
"""


ONLY = None  # set to a list of run names to render a subset


async def main():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch()
        page = await browser.new_page(viewport={"width": 390, "height": 760}, device_scale_factor=2)
        for run, (fname, fids) in JOBS.items():
            if ONLY and run not in ONLY:
                continue
            await page.goto((SRC / fname).as_uri())
            await page.wait_for_timeout(300)
            names = await page.eval_on_selector_all("section[data-screen]", "els => els.map(e => e.dataset.screen)")
            for fid in fids:
                if fid:
                    # press the prototype's own control so its selected state is shown truthfully
                    await page.get_by_role("button", name=fid.capitalize(), exact=True).click()
                    await page.wait_for_timeout(200)
                for i, name in enumerate(names, 1):
                    await page.evaluate(SHOW, name)
                    await page.wait_for_timeout(120)
                    tag = f"{run}_{fid}" if fid else run
                    path = OUT / f"{tag}_{i:02d}_{name}.png"
                    if run in ELEMENT_SHOTS:
                        # this prototype stacks its screens on one page; capture the screen itself
                        await page.locator(f'section[data-screen="{name}"]').screenshot(path=str(path))
                    else:
                        await page.screenshot(path=str(path))
                    im = Image.open(path)
                    im.thumbnail((360, 720))
                    im.save(path, optimize=True)
        await browser.close()


asyncio.run(main())
