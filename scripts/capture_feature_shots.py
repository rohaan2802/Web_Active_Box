"""Capture 20 labelled feature screenshots for the README gallery."""
from __future__ import annotations

import http.server
import socketserver
import threading
from pathlib import Path

from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "screenshots"
PORT = 5511
BASE = f"http://127.0.0.1:{PORT}/"
MAX_W = 1400


def save(page, name: str, full_page: bool = False) -> None:
    raw = OUT / f"_{name}.png"
    page.screenshot(path=str(raw), full_page=full_page)
    img = Image.open(raw).convert("RGB")
    if img.width > MAX_W:
        h = int(img.height * MAX_W / img.width)
        img = img.resize((MAX_W, h), Image.Resampling.LANCZOS)
    dest = OUT / f"{name}.jpg"
    img.save(dest, quality=82, optimize=True)
    raw.unlink(missing_ok=True)
    print(dest.name, dest.stat().st_size)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for p in OUT.glob("*"):
        p.unlink()
    preview = ROOT / "docs" / "preview.webp"
    if preview.exists():
        preview.unlink()

    handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("127.0.0.1", PORT), handler)
    httpd.allow_reuse_address = True
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": 1440, "height": 900},
            device_scale_factor=1.25,
            color_scheme="dark",
        )
        page = context.new_page()
        page.goto(BASE, wait_until="networkidle")
        page.wait_for_timeout(600)

        # 01 hero dark
        save(page, "01-hero-dark-desktop")

        # 02 theme light
        page.locator(".theme-toggle").click()
        page.wait_for_timeout(300)
        save(page, "02-hero-light-desktop")

        # 03 features
        page.locator("#features").scroll_into_view_if_needed()
        page.wait_for_timeout(250)
        save(page, "03-features-section")

        # 04 work gallery all
        page.locator("#work").scroll_into_view_if_needed()
        page.wait_for_timeout(250)
        save(page, "04-work-gallery-all")

        # 05 filter Objects
        page.locator('[data-filter="Objects"]').click()
        page.wait_for_timeout(250)
        save(page, "05-work-filter-objects")

        # 06 filter Photography
        page.locator('[data-filter="Photography"]').click()
        page.wait_for_timeout(250)
        save(page, "06-work-filter-photography")

        # 07 lightbox
        page.locator('[data-filter="All"]').click()
        page.wait_for_timeout(200)
        page.locator("[data-preview]").first.click()
        page.wait_for_timeout(350)
        save(page, "07-image-viewer-lightbox")
        page.keyboard.press("Escape")
        page.wait_for_timeout(200)

        # 08 team
        page.locator("#team").scroll_into_view_if_needed()
        page.wait_for_timeout(250)
        save(page, "08-team-section")

        # 09 testimonials
        page.locator("#testimonials").scroll_into_view_if_needed()
        page.wait_for_timeout(250)
        save(page, "09-testimonials-section")

        # 10 download CTA
        page.locator("#download").scroll_into_view_if_needed()
        page.wait_for_timeout(250)
        save(page, "10-download-cta")

        # 11 project notes / the build
        page.locator("#project-notes").scroll_into_view_if_needed()
        page.wait_for_timeout(250)
        save(page, "11-project-notes-build")

        # 12 Work filter — Print (useful gallery path)
        page.locator("#work").scroll_into_view_if_needed()
        page.wait_for_timeout(200)
        page.locator('button[data-filter="Print"]').click()
        page.wait_for_timeout(350)
        save(page, "12-work-filter-print")

        # 13 reading progress mid-page
        page.evaluate("window.scrollTo(0, document.body.scrollHeight * 0.45)")
        page.wait_for_timeout(300)
        save(page, "13-reading-progress-midscroll")

        # 14 back to top
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(400)
        save(page, "14-back-to-top-control")

        # 15 header + nav desktop light
        page.evaluate("window.scrollTo(0, 0)")
        page.wait_for_timeout(200)
        save(page, "15-header-nav-theme-controls")

        # Mobile shots
        page.set_viewport_size({"width": 390, "height": 844})
        page.goto(BASE, wait_until="networkidle")
        page.wait_for_timeout(500)
        # ensure dark for mobile hero
        page.evaluate("document.documentElement.dataset.theme='dark'")
        page.wait_for_timeout(200)
        save(page, "16-mobile-hero")

        page.locator(".menu-toggle").click()
        page.wait_for_timeout(300)
        save(page, "17-mobile-nav-open")
        page.locator(".menu-toggle").click()
        page.wait_for_timeout(200)

        page.locator("#work").scroll_into_view_if_needed()
        page.wait_for_timeout(250)
        save(page, "18-mobile-work-gallery")

        # Tablet
        page.set_viewport_size({"width": 768, "height": 1024})
        page.goto(BASE, wait_until="networkidle")
        page.wait_for_timeout(500)
        page.locator("#features").scroll_into_view_if_needed()
        page.wait_for_timeout(250)
        save(page, "19-tablet-features-layout")

        # Skip link focus (desktop)
        page.set_viewport_size({"width": 1440, "height": 900})
        page.goto(BASE, wait_until="networkidle")
        page.wait_for_timeout(400)
        page.keyboard.press("Tab")
        page.wait_for_timeout(200)
        save(page, "20-skip-link-keyboard-focus")

        browser.close()

    httpd.shutdown()
    print("shots", len(list(OUT.glob("*.jpg"))))


if __name__ == "__main__":
    main()
