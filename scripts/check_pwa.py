#!/usr/bin/env python3
"""Check the built site is still an installable web app (Android "Install app").

Usage:
    hugo --minify && python3 scripts/check_pwa.py [PUBLIC_DIR]

For every edition in hugo.toml: the manifest exists, is valid JSON, has the
fields and icons Chrome needs, every icon it names was published, the
edition's home page links it, and the edition has an install page (/install/,
the link shared with readers). Also checks the service worker and its offline
page were published. Exits 1 if any check fails.
"""
import json
import re
import sys
import tomllib
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
PUBLIC = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "public"
REQUIRED = ["id", "name", "short_name", "start_url", "scope", "display", "icons"]
ICONS = [("192x192", "any"), ("512x512", "any"), ("512x512", "maskable")]
MANIFEST_LINK = re.compile(r"""<link rel=["']?manifest["']? href=["']?([^"' >]+)""")

config = tomllib.loads((ROOT / "hugo.toml").read_text(encoding="utf-8"))
default = config.get("defaultContentLanguage", "en")
editions = ["" if lang == default else lang for lang in config["languages"]]

errors = []
for edition in editions:
    home = PUBLIC / edition
    path = home / "manifest.webmanifest"
    if not path.is_file():
        errors.append(f"{path}: missing")
        continue
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        errors.append(f"{path}: invalid JSON ({e})")
        continue
    for key in REQUIRED:
        if not manifest.get(key):
            errors.append(f"{path}: no {key}")
    if manifest.get("display") != "standalone":
        errors.append(f"{path}: display is not standalone")
    expected_home = f"/{edition}/" if edition else "/"
    for key in ("id", "start_url"):
        if manifest.get(key) != expected_home:
            errors.append(f"{path}: {key} must be {expected_home}")
    language = config["languages"][edition or default]
    if manifest.get("lang") != language["languageCode"]:
        errors.append(f"{path}: wrong language")
    if manifest.get("scope") != "/":
        errors.append(f"{path}: scope must cover the whole site")
    for key in ("theme_color", "background_color"):
        if manifest.get(key) != config["params"]["assets"]["theme_color"]:
            errors.append(f"{path}: {key} must match the site theme")
    menu = sorted(language["menus"]["main"], key=lambda item: item["weight"])[:3]
    expected_shortcuts = [(item["name"], expected_home + item["url"].lstrip("/")) for item in menu]
    if [(item.get("name"), item.get("url")) for item in manifest.get("shortcuts", [])] != expected_shortcuts:
        errors.append(f"{path}: wrong localized shortcuts")
    icons = manifest.get("icons", [])
    have = {(i.get("sizes"), i.get("purpose", "any")) for i in icons}
    for sizes, purpose in ICONS:
        if (sizes, purpose) not in have:
            errors.append(f"{path}: no {sizes} {purpose} icon")
    for shortcut in manifest.get("shortcuts", []):
        icons = icons + shortcut.get("icons", [])
    for icon in icons:
        if not (PUBLIC / icon["src"].lstrip("/")).is_file():
            errors.append(f"{path}: icon {icon['src']} not published")
    expected = f"/{edition}/manifest.webmanifest" if edition else "/manifest.webmanifest"
    link = MANIFEST_LINK.search((home / "index.html").read_text(encoding="utf-8"))
    if not link or urlparse(link.group(1)).path != expected:
        errors.append(f"{home / 'index.html'}: does not link {expected}")
    if not (home / "install" / "index.html").is_file():
        errors.append(f"{home / 'install/index.html'}: missing (the page shared with readers)")

# Check article and section pages too; a home-only check misses a broken hook.
for page in PUBLIC.rglob("*.html"):
    html = page.read_text(encoding="utf-8")
    if page == PUBLIC / "offline/index.html" or 'http-equiv=refresh' in html or 'http-equiv="refresh"' in html:
        continue
    first = page.relative_to(PUBLIC).parts[0]
    edition = first if first in editions else ""
    expected = f"/{edition}/manifest.webmanifest" if edition else "/manifest.webmanifest"
    links = MANIFEST_LINK.findall(html)
    if len(links) != 1 or urlparse(links[0]).path != expected:
        errors.append(f"{page}: must link exactly one manifest for its edition")
    if re.search(r'<link[^>]+rel=["\']?alternate[^>]+application/manifest', html):
        errors.append(f"{page}: manifest must not be an alternate output")
    if "navigator.serviceWorker.register" not in html:
        errors.append(f"{page}: production service worker registration missing")

for name in ["sw.js", "offline/index.html"]:
    if not (PUBLIC / name).is_file():
        errors.append(f"{PUBLIC / name}: missing")

for error in errors:
    print(error)
if errors:
    sys.exit(1)
print(f"Web app check passed for {len(editions)} editions.")
