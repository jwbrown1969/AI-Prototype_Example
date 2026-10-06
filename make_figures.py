"""Compose article figures from the rendered screen thumbnails in thumbs/.

Usage: python3 make_figures.py   (requires Pillow; run render_thumbs.py first)
Every screen image is an unedited rendering of a prototype file.
"""
import glob
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).parent
OUT = ROOT / "figures"
OUT.mkdir(exist_ok=True)

W = 1600
BG = (255, 255, 255)
INK = (27, 33, 38)
MUTED = (90, 102, 112)
RULE = (213, 219, 224)
WARN = (168, 70, 28)
F = "/usr/share/fonts/opentype/inter/"
H1 = ImageFont.truetype(F + "Inter-SemiBold.otf", 40)
H2 = ImageFont.truetype(F + "Inter-SemiBold.otf", 30)
TX = ImageFont.truetype(F + "Inter-Regular.otf", 24)
SM = ImageFont.truetype(F + "Inter-Regular.otf", 20)


def thumbs(pattern):
    return [Image.open(f).convert("RGB") for f in sorted(glob.glob(str(ROOT / "thumbs" / pattern)))]


def grid(ims, cols, cell_w, gap=10):
    cell_h = int(cell_w * 2)
    rows = (len(ims) + cols - 1) // cols
    g = Image.new("RGB", (cols * cell_w + (cols - 1) * gap, rows * cell_h + (rows - 1) * gap), BG)
    d = ImageDraw.Draw(g)
    for i, im in enumerate(ims):
        im = im.copy()
        im.thumbnail((cell_w, cell_h))
        x, y = (i % cols) * (cell_w + gap), (i // cols) * (cell_h + gap)
        g.paste(im, (x, y))
        d.rectangle([x, y, x + im.width - 1, y + im.height - 1], outline=RULE, width=1)
    # crop to used height of last row
    return g


def canvas(h):
    c = Image.new("RGB", (W, h), BG)
    return c, ImageDraw.Draw(c)


def two_up(left, right, ltitle, lsub, rtitle, rsub, title, out, lcols, rcols, cell, note=None, lcolor=INK):
    gl, gr = grid(left, lcols, cell), grid(right, rcols, cell)
    tw = lambda t, f: int(ImageDraw.Draw(Image.new("RGB", (1, 1))).textlength(t, font=f))
    top = 90
    lx = 40
    lw = max(gl.width, tw(ltitle, H2), tw(lsub, SM))
    rx = lx + lw + 80
    rw = max(gr.width, tw(rtitle, H2), tw(rsub, SM))
    width = max(rx + rw + 40, tw(title, H1) + 80, tw(note or "", SM) + 80)
    h = top + 100 + max(gl.height, gr.height) + (70 if note else 40)
    c = Image.new("RGB", (width, h), BG)
    d = ImageDraw.Draw(c)
    d.text((40, 30), title, font=H1, fill=INK)
    d.text((lx, top + 10), ltitle, font=H2, fill=lcolor)
    d.text((lx, top + 52), lsub, font=SM, fill=MUTED)
    d.text((rx, top + 10), rtitle, font=H2, fill=INK)
    d.text((rx, top + 52), rsub, font=SM, fill=MUTED)
    c.paste(gl, (lx, top + 100))
    c.paste(gr, (rx, top + 100))
    d.line([(rx - 40, top + 10), (rx - 40, top + 100 + max(gl.height, gr.height))], fill=RULE, width=2)
    if note:
        d.text((40, h - 50), note, font=SM, fill=MUTED)
    c.save(out, optimize=True)
    print(out, c.size)


# Figure 1: first request
two_up(thumbs("A_*.png"), thumbs("C_*.png"),
       "No scope: 11 screens", "\"...a mobile web app that lets residents report potholes.\"",
       "Scoped: 3 screens", "Same request, plus the task, a screen limit, and exclusions.",
       "Same app, two requests", OUT / "fig1_first_request.png", lcols=6, rcols=3, cell=150,
       note="Unedited AI output. The scoped build is a sketch because its request asked for one.")

# Figure 2: after three follow-ups
two_up(thumbs("U3_*.png"), thumbs("S3_*.png"),
       "No scope: 26 screens", "Screens after each round:  11  →  12  →  18  →  26",
       "Scoped: 3 screens", "3  →  3  →  3  →  3",
       "After the same three follow-ups",
       OUT / "fig2_follow_ups.png", lcols=9, rcols=3, cell=100, lcolor=WARN,
       note="Follow-ups: \"Make it better.\"  \"What else would residents want? Add it.\"  \"Make it production-ready.\"")

# Figure 3: alternatives
alts = [("Map first", "D1_*.png"), ("Camera first", "D2_*.png"), ("Address first", "D3_*.png")]
cell = 140
gs = [grid(thumbs(p), 3, cell) for _, p in alts]
c, d = canvas(90 + 60 + gs[0].height + 60)
d.text((40, 30), "Three scoped alternatives, 144 seconds combined", font=H1, fill=INK)
x = 40
for (label, _), g in zip(alts, gs):
    d.text((x, 100), label, font=H2, fill=INK)
    c.paste(g, (x, 150))
    x += g.width + 70
d.text((40, c.height - 45), "Same scoped request, one added line naming a starting point. The single unscoped build took 212 seconds.", font=SM, fill=MUTED)
c.save(OUT / "fig3_alternatives.png", optimize=True)
print(OUT / "fig3_alternatives.png", c.size)

# Figure 4: three fidelities in one build
cell = 170
rows = [("Sketch", "F_sketch_*.png"), ("Wireframe", "F_wireframe_*.png"), ("Polished", "F_polished_*.png")]
gs = [grid(thumbs(p), 3, cell) for _, p in rows]
lab_w = 200
c, d = canvas(90 + sum(g.height + 30 for g in gs) + 50)
d.text((40, 30), "One build, three fidelities", font=H1, fill=INK)
y = 100
for (label, _), g in zip(rows, gs):
    d.text((40, y + g.height // 2 - 16), label, font=H2, fill=INK)
    c.paste(g, (40 + lab_w, y))
    y += g.height + 30
d.text((40, c.height - 45), "Same screens, same words. The switch changes only the styling.", font=SM, fill=MUTED)
# trim right whitespace
c = c.crop((0, 0, 40 + lab_w + gs[0].width + 40, c.height))
c.save(OUT / "fig4_fidelities.png", optimize=True)
print(OUT / "fig4_fidelities.png", c.size)

# Figure 5: placeholder text
a, b = thumbs("A_05_*.png")[0], thumbs("B_05_*.png")[0]
cell = 300
ga, gb = grid([a], 1, cell), grid([b], 1, cell)
c, d = canvas(90 + 60 + max(ga.height, gb.height) + 60)
d.text((40, 30), "\"Placeholder text\": 4% of copy kept", font=H1, fill=INK)
d.text((40, 100), "Original details screen", font=H2, fill=INK)
d.text((40 + cell + 80, 100), "Sketch redraw", font=H2, fill=WARN)
c.paste(ga, (40, 150))
c.paste(gb, (40 + cell + 80, 150))
d.text((40, c.height - 45), "The questions a test needs became Label A, Label B, and Label C.", font=SM, fill=MUTED)
c = c.crop((0, 0, max(40 + 2 * cell + 80 + 40, 1000), c.height))
c.save(OUT / "fig5_placeholder.png", optimize=True)
print(OUT / "fig5_placeholder.png", c.size)
