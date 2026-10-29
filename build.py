#!/usr/bin/env python3
"""Build the whole iborygame.com site into one folder, ready to upload to the GitHub Pages repo.

    python3 website/build.py            (from the bundle root)  ->  dist/

dist/ = everything in website/ (landing page, privacy policy, account page, 404, CNAME, .nojekyll, img/, and ar/ and es/: the translated pages, built by i18n/site_i18n.py)
        plus the game in dist/play/ (a copy of ibory-phone/).
Upload the CONTENTS of dist/ to the root of the repo. On later game-only releases, replacing dist/play/ is enough.
"""
import os, shutil, sys

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
web, game, out = os.path.join(root, "website"), os.path.join(root, "ibory-phone"), os.path.join(root, "dist")
if os.path.exists(out):
    shutil.rmtree(out)
shutil.copytree(web, out, ignore=shutil.ignore_patterns("build.py", "__pycache__"))
shutil.copytree(game, os.path.join(out, "play"))
need = ["sw.js", "index.html", "privacy.html", "account.html", "404.html", "CNAME", ".nojekyll", "site.css", "ar/index.html", "ar/privacy.html", "ar/account.html", "es/index.html", "es/privacy.html", "es/account.html", "vi/index.html", "vi/privacy.html", "vi/account.html", "ru/index.html", "ru/privacy.html", "ru/account.html", "zh/index.html", "zh/privacy.html", "zh/account.html", "zh-TW/index.html", "zh-TW/privacy.html", "zh-TW/account.html", "ja/index.html", "ja/privacy.html", "ja/account.html", "play/index.html", "play/sw.js", "play/manifest.webmanifest", "play/lang/ar.js", "play/lang/es.js", "play/lang/vi.js", "play/lang/ru.js", "play/lang/zh.js", "play/lang/zh-TW.js", "play/lang/ja.js"]
missing = [n for n in need if not os.path.exists(os.path.join(out, n))]
if missing:
    sys.exit("missing from dist/: " + ", ".join(missing))
n = sum(len(f) for _, _, f in os.walk(out))
print("dist/ ready:", n, "files. Upload its contents to the root of the iborygame.com repo.")
