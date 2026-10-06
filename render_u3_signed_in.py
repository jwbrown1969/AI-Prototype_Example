import asyncio, re, sys
from pathlib import Path
from playwright.async_api import async_playwright
from PIL import Image

async def signed_in_page(b):
    p = await b.new_page(viewport={"width": 390, "height": 760}, device_scale_factor=2)
    await p.goto(Path('prototypes/U3_unscoped_round3.html').resolve().as_uri()); await p.wait_for_timeout(600)
    await p.click('#welcomeSignIn'); await p.wait_for_timeout(400)
    await p.locator('section[data-screen="sign-in"] input').first.fill('5550123344')
    await p.locator('section[data-screen="sign-in"] button', has_text='Send code').click(); await p.wait_for_timeout(500)
    await p.fill('#vfCode', '123456'); await p.wait_for_timeout(2500)
    return p

async def main():
    async with async_playwright() as pw:
        b = await pw.chromium.launch()
        p = await signed_in_page(b)
        print('after sign-in:', await p.evaluate("document.querySelector('.screen.active')?.dataset.screen"))
        await p.evaluate("location.hash='#/my-reports'"); await p.wait_for_timeout(900)
        html = await p.evaluate("document.querySelector('section[data-screen=\"my-reports\"]').innerHTML")
        ids = re.findall(r'data-detail="([^"]+)"', html)
        print('ids:', ids[:5])
        if not ids:
            sys.exit(0)
        rid = ids[0]
        names = await p.eval_on_selector_all("section[data-screen]", "els => els.map(e => e.dataset.screen)")
        for i, name in enumerate(names, 1):
            h = f'#/r/{rid}' if name == 'report-detail' else (f'#/{name}/{rid}' if name in ('thread', 'claim') else f'#/{name}')
            await p.evaluate(f"location.hash='{h}'"); await p.wait_for_timeout(900)
            act = await p.evaluate("document.querySelector('.screen.active')?.dataset.screen")
            status = 'navigated' if act == name else f'kept earlier render (app showed {act})'
            print(f'{i:02d} {name}: {status}')
            if act == name:
                out = f'thumbs/U3_{i:02d}_{name}.png'
                await p.screenshot(path=out)
                im = Image.open(out); im.thumbnail((360, 720)); im.save(out, optimize=True)
        await b.close()

asyncio.run(main())
