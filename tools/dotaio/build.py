#!/usr/bin/env python3
"""Builds dotaio-by-dotmod/index.html ("Devices developed by dotmod, and collabs").

Run from the repo root:   python3 tools/dotaio/build.py .

The page is GENERATED. Edit this file instead of the HTML:
  - SECTIONS (below): every section and card - name, version, date, colours, notes, photos.
  - tools/dotaio/doors.html: the "Browse the collections" doors in the header.
The page reuses the masterlist's CSS, profile links and lightbox, copied from index.html at
build time, so rebuild after changing index.html's styles. See CLAUDE.md for the full rules.
"""
import html, re, sys, pathlib

repo = pathlib.Path(sys.argv[1])
src = (repo / "index.html").read_text(encoding="utf-8")

css = re.search(r"<style>\n(.*?)\n</style>", src, re.S).group(1)
profile = re.search(r'(<ul class="profile".*?</ul>)', src, re.S).group(1)
# The visitor counter belongs to the main page; leave it off this one.
profile = re.sub(r'\s*<li class="(visits|is-dotaio)".*?</li>', "", profile, flags=re.S)
lightbox = re.search(r'(<div class="lb" id="lb".*?</div>\n)<script>', src, re.S).group(1)

e = lambda s: html.escape(str(s), quote=True)

DM = "https://dotmod.com/cdn/shop/"
VS = "https://www.vapestore.to/wp-content/uploads/2022/04/"
BC = "https://cdn11.bigcommerce.com/s-bojz5r7/images/stencil/1280x1280/products/3648/"
VH = "https://vapehaus.com.my/cdn/shop/files/"

SW = {  # swatch colours
  "Black":"#1b1b1d","Gold":"#c9a24a","Red":"#b3262e","Royal Blue":"#2747a8","White":"#f2f2f2",
  "Gunmetal":"#55595f","Purple":"#6a3fa0","Tiffany Blue":"#7fd1c6","Silver":"#c8cbd0","Blue":"#3d5f8c","OD Green":"#4f5d3a","Royal Purple":"#7a2fc8","Orange":"#e0782a",
  "Green":"#3f8f4f","Light Yellow":"#efe39a","Dark Grey":"#3b3d42","Frost":"#e8eef2","Smoke":"#4a4d55",
  "Red Frost":"#d97a82","Purple Frost":"#a68bd0","Tiffany Frost":"#a6e3da","Clear":"#e6ecef","Lime Green":"#8fcf3c",
  "Cinnamon":"#9c5a34","Brown":"#6b4a33","Sea Foam Blue":"#8fd3c7","Nero (black)":"#111111",
  "Iceberg (white)":"#f4f6f7","Forged carbon":"#2b2b2b",
}

SECTIONS = [
 ("v1", "dotAIO V1", "2019 – 2021", [
  dict(name="dotAIO", ver="Original · standard kit", date="June 24, 2019",
       colors=["Black","Gold","Red","Royal Blue"], ltd=["White","Gunmetal","Purple","Tiffany Blue"],
       notes=["35W, 4-level auto power","1 × 18650","CNC aluminium, gold-plated accents","Started the platform; its doors, tanks and RBAs fit every later 18650 dotAIO"],
       imgs=[f"../images/dotaio-v1-{n}.jpg" for n in range(1, 5)]),
  dict(name="dotAIO G10", ver="Limited edition · G10", date="November 13, 2019",
       colors=[], ltd=["Orange","Black","Green","Light Yellow","Dark Grey","Royal Blue","Red"],
       notes=["35W, 4-level auto power","1 × 18650","G10 composite body","First run (Orange or Black) limited to 100 units worldwide"],
       imgs=[f"../images/dotaio-g10-{n}.jpg" for n in range(1, 5)]),
  dict(name="dotAIO SE", ver="Special Edition", date="December 13, 2019",
       colors=["Black","White"], ltd=[],
       notes=["35W, 4-level auto power","1 × 18650","Zinc alloy and stainless steel","Backlit oversized fire button doubles as a tri-colour battery LED"],
       imgs=[f"../images/dotaio-se-{n}.jpg" for n in range(1, 5)]),
  dict(name="dotAIO Frost", ver="Limited release · polycarbonate", date="January 15, 2020",
       colors=[], ltd=["Frost","Smoke","Red Frost","Purple Frost","Tiffany Frost"],
       notes=["35W, 4-level auto power","1 × 18650","Frosted polycarbonate, about 90 g","Semi-transparent body shows the internals"],
       imgs=["https://dotmod67-com.myshopify.com/cdn/shop/products/frostFront_1024x1024@2x.jpg?v=1597503418", VS+"dotmod_dotaio_-_smoke.png", VS+"dotmod_-_dotaio_-_pod_mod_-_frosted_red.png", VS+"dotmod_dotaio_35w_pod_system_clear_tiffany_blue.png"]),
  dict(name="dotAIO mini", ver="Compact · 18350", date="March 19, 2021",
       colors=["Black","Gold","Red","Royal Blue"], ltd=["Purple","Tiffany Blue"],
       notes=["35W, 4-level auto power","1 × 18350","Aluminium, 57 × 45.5 × 21 mm","Takes all dotAIO coils, tanks and RBAs"],
       imgs=[DM+"products/Gold_1_ddffcd12-cd9c-4e8f-94ef-f6e3a9fe3dec.jpg?v=1761046214", DM+"products/Black_1_dd2b45f0-489d-4339-b751-89c0cd260e65.jpg?v=1761046275", DM+"products/Red_1_561c9868-cb87-4c04-aad8-d516407bee84.jpg?v=1761046268", DM+"products/RB_1.jpg?v=1761046206"]),
 ]),
 ("v2", "dotAIO V2", "2021 – 2025", [
  dict(name="dotAIO V2", ver="Standard kit", date="November 12, 2021",
       colors=["Black","Red","Royal Blue","Silver"], ltd=["Tiffany Blue","Purple","Lime Green","Orange"],
       notes=["Up to 75W in 0.1W steps, TC and bypass","1 × 18650","Aluminium, LCD screen with selectable colours","dotCoils 0.15–1.0 Ω; fits V1 doors, tanks and RBAs"],
       imgs=[DM+"files/Black_F.png?v=1761046856", DM+"products/RoyalBlue_F.png?v=1761046833", DM+"products/Red_F.png?v=1761046839", DM+"files/Silver_F.png?v=1761046871"]),
  dict(name="dotAIO V2 Cinnamon", ver="Limited edition", date="Date not published",
       colors=[], ltd=["Cinnamon"],
       notes=["Up to 75W","1 × 18650","Metallic matte cinnamon finish","Ships with the dotAIO V3 tank; extra side airflow slots"],
       imgs=["https://dotmod.fr/883-large_default/dotaio-v2-cinnamon.jpg", "https://dotmod.fr/882-large_default/dotaio-v2-cinnamon.jpg", "https://dotmod.fr/884-large_default/dotaio-v2-cinnamon.jpg"]),
  dict(name="dotAIO V2 Lite", ver="Lightweight · polycarbonate", date="December 16, 2022",
       colors=["Clear","Smoke","Red","Green","Orange","Purple"], ltd=["Tiffany Blue"],
       notes=["Up to 75W, TC and bypass","1 × 18650","Matte polycarbonate","Same chip and screen as the V2 in a lighter body"],
       imgs=[BC+"23961/Collage-Square__75340.1671236323.jpg?c=2", BC+"23951/Clear1__16679.1671236062.jpg?c=2", BC+"23950/Smoke1__96744.1671236068.jpg?c=2", BC+"23959/Orange1__77307.1671236088.jpg?c=2"]),
  dict(name="dotAIO V2 G10", ver="Limited edition · G10", date="Date not published",
       colors=[], ltd=["Orange","Black","Purple","Brown","Green","White"],
       notes=["Up to 75W","1 × 18650","G10 composite","Sold in small batches"],
       imgs=[f"../images/dotaio-v2-g10-{n}.jpg" for n in range(1, 5)]),
 ]),
 ("x", "dotAIO X", "2024", [
  dict(name="dotAIO X Essential", ver="Essential kit", date="April 19, 2024",
       colors=["Black","Gunmetal"], ltd=[],
       notes=["5–60W","1 × 18650 in a separate magnetic module","Aluminium, modular","dotAIO Tank Module, V3 dotAIO tank, 0.3 Ω and 0.7 Ω dotCoils"],
       imgs=[DM+"files/01_c71fd5ef-1935-47fa-8829-0939ebd2f3a2.png?v=1761049386", DM+"files/02_b630b13a-d150-4d0a-8838-989d09ed3b62.png?v=1761049404", DM+"files/03_b6a8fac2-d37d-4ac0-9e77-e1b4631d7a89.png?v=1761049414", DM+"files/es.png?v=1761049290"]),
  dict(name="dotAIO X Pro", ver="Pro kit · adds Boro Tank Module", date="April 19, 2024",
       colors=["Black","Gunmetal"], ltd=[],
       notes=["5–60W","1 × 18650 in a separate magnetic module","Aluminium, modular","Takes boro tanks and bridges as well as dotAIO tanks and RBAs"],
       imgs=[DM+"files/04_b6c04320-d47d-4c3f-8d0f-abc5a3ddb956.png?v=1761049408", DM+"files/05_c34ed412-960c-4055-b802-0cd4a22a7f0b.png?v=1761049371", DM+"files/DSC5924.jpg?v=1761049285", DM+"files/06_c5301f78-7911-47dc-953b-b3c12f563422.png?v=1761049375"]),
 ]),
 ("collabs", "dotmod collabs", "2024 – 2025", [
  dict(name="dotAIO V2 Sturdy Iceberg", ver="dotmod × Sturdy Mfg. Co.", date="January 26, 2024",
       colors=[], ltd=["Iceberg (white)"],
       notes=["Up to 75W","1 × 18650","White Delrin","Sturdy-designed panels, buttons and drip tip; V3 dotAIO tank"],
       imgs=[f"../images/dotaio-v2-iceberg-{n}.jpg" for n in range(1, 5)]),
  dict(name="dotAIO V2 Sturdy Nero", ver="dotmod × Sturdy Mfg. Co.", date="June 14, 2024",
       colors=[], ltd=["Nero (black)"],
       notes=["Up to 75W","1 × 18650","All-black patterned Delrin","Bigger rear airflow slot and new slots above the screen"],
       imgs=[VH+"IMG_2642.jpg?v=1719644303&width=1946", VH+"DotModxSturdyDotAIONewGallery_webp.jpg?v=1719644303&width=1946", VH+"DotModxSturdyDotAIONewScreen_webp.jpg?v=1719644302&width=1946", VH+"DotModxSturdyDotAIONewPanel1_webp.jpg?v=1719644302&width=1946"]),
  dict(name="dotAMP", ver="dotmod × BP Mods collaboration", date="December 2024",
       colors=["Black","Red","Royal Blue","Gunmetal","Silver"], ltd=[],
       notes=["80W max output","Built-in 2000mAh battery, USB-C 5V/2A fast charging","Aluminium body, 0.96″ TFT screen","Ships with the dotAIO V3 tank; fits all earlier dotAIO tanks and RBAs"],
       imgs=[DM+"files/BK_F_3dcb95c1-603d-4fc8-bd23-42cbf3b1fc9a.png?v=1761050716", DM+"files/GM_F_b100cef8-cee3-4a62-8176-9b10f9776255.png?v=1761050726", DM+"files/R_F_86e4aba2-8598-4227-899f-b96e4027ce2b.png?v=1761050800", DM+"files/RB_F_3bc77f20-4d05-4a93-b5c4-c0410b2f1c2c.png?v=1761050813"]),
  dict(name="dotAIO V2 G10 Monarchy", ver="dotmod × Monarchy · limited to 3,000 units", date="January 17, 2025",
       colors=[], ltd=["Black","Royal Blue"],
       notes=["Up to 75W","1 × 18650","G10 composite","Made with Monarchy; ships with the dotAIO V3 tank"],
       imgs=["https://my.dotmod.com/cdn/shop/files/MNCH_F.png?v=1776072214", "https://my.dotmod.com/cdn/shop/files/MNCH_B.png?v=1776072213"]),
  dict(name="dotApollo", ver="dotmod × Mission XV collaboration", date="September 2025",
       colors=["Black","Red","Blue","Silver"], ltd=[],
       notes=["5–80W; PM, Bypass, Auto, Curve and Boost modes","1 × 18650 (not included), USB-C 5V/2A fast charging","0.96″ colour screen","Ships with the dotAIO V4 tank; fits dotAIO accessories, boro tanks and RBAs including the dotRBA X"],
       imgs=["https://dotmod.fr/153-large_default/dotapollo-dotmod-missionxv.jpg", "https://dotmod.fr/159-large_default/dotapollo-dotmod-missionxv.jpg", "https://dotmod.fr/164-large_default/dotapollo-dotmod-missionxv.jpg", "https://i.shgcdn.com/443cc8a6-dc8e-4167-a6c6-73bade82aaec/-/format/auto/-/preview/3000x3000/-/quality/lighter/"]),
  dict(name="Ergon", soon=True,
       fields=[("Version", "dotmod × Sturdy Mfg collaboration", "modder"), ("Modder, country", "Sturdy Mfg, Malaysia", "modder"), ("Status", "Coming soon (since 2025)", "year")],
       colors=["OD Green","Royal Purple"], ltd=[], notes=[],
       imgs=[f"../images/ergon-sturdy-{n}.jpg" for n in range(1, 5)]),
 ]),
 ("v3", "dotAIO V3", "2025 – 2026", [
  dict(name="dotAIO V3", ver="Standard kit", date="November 21, 2025",
       colors=["Black","Silver","Gunmetal","Red","Royal Blue"], ltd=[],
       notes=["5–80W in 0.1W steps","1 × 18650","Aluminium, 88.7 × 45.8 × 23.6 mm, 105 g","0.96″ full-colour screen with GIF upload; dotAIO V4 tank and pod included"],
       imgs=[DM+"files/bk_f_8f630f46-3d65-410c-bc96-4e4168b059c7.jpg?v=1770999879", DM+"files/sl_f_ddb64403-be64-4ae4-b04d-9ba19cdc33f3.jpg?v=1770999879", DM+"files/gm_f_34f596f8-319b-462c-8320-ae99852c95d6.jpg?v=1770999879", DM+"files/rb_f_ffd97ddf-1970-4e01-9af7-f91c95964f74.jpg?v=1770999879"]),
  dict(name="dotAIO V3 Orange", ver="Limited release colour", date="2026",
       colors=[], ltd=["Orange"],
       notes=["5–80W","1 × 18650","Aluminium","Spring 2026 limited colour"],
       imgs=[DM+"files/OG_F_4803e19c-bd68-4a62-8786-353a9de8b2ae.png?v=1770999879", DM+"files/OG_B_9868a70f-5ae4-4c30-b2ad-3a0c7afa1375.png?v=1770999879"]),
  dict(name="dotAIO V3 Sea Foam Blue", ver="Limited release colour", date="2026",
       colors=[], ltd=["Sea Foam Blue"],
       notes=["5–80W","1 × 18650","Aluminium","2026 limited colour"],
       imgs=[DM+"files/SFB_F_6871d57e-81c2-40ac-96b6-beee2d0d5241.jpg?v=1774461645", DM+"files/SFB_B_5fe866d6-f5fb-4f54-bb44-c5703dfdf772.jpg?v=1774461645"]),
  dict(name="dotAIO V3 Forged Carbon", ver="Limited edition", date="2026",
       colors=[], ltd=["Forged carbon"],
       notes=["5–80W","1 × 18650","Forged carbon fibre finish","Listed by authorised retailers in 2026"],
       imgs=[f"../images/dotaio-v3-forged-carbon-{n}.jpg" for n in range(1, 5)]),
 ]),
 ("proto", "Unreleased prototypes", "", [
  dict(name="dotAIO V2 Titanium",
       fields=[("Status", "Unreleased prototype", "year")],
       colors=[], ltd=[], notes=["Titanium body","Teal finish with a gold circuit-board pattern"],
       imgs=[f"../images/dotaio-v2-titanium-{n}.jpg" for n in range(1, 3)]),
 ]),
]

total = sum(len(c) for _, _, _, c in SECTIONS)
DOORS = pathlib.Path(__file__).with_name("doors.html").read_text(encoding="utf-8").rstrip("\n")
DOORS = re.sub(r"\d+ models &amp; editions", f"{total} models &amp; editions", DOORS)
limited = sum(1 for _, _, _, cs in SECTIONS for c in cs if c["ltd"] and not c["colors"])
lines = sum(1 for sid, _, _, _ in SECTIONS if sid != "proto")

def swatch(n, is_ltd):
    tag = '<span class="sw-ltd">Limited</span>' if is_ltd else ""
    return f'<li><i style="background:{SW.get(n, "#777")}"></i>{e(n)}{tag}</li>'

def card(sid, i, c):
    key = f"{sid}-{i+1:02d}"
    fields = c.get("fields") or [("Version", c["ver"], "modder"), ("Launch date", c["date"], "year")]
    search = " ".join([c["name"], *[v for _, v, _ in fields], *c["colors"], *c["ltd"], *c["notes"]]).lower()
    ribbon = '<span class="soon-ribbon" aria-hidden="true">Coming soon</span>' if c.get("soon") else ""
    if c["imgs"]:
        imgs = [f'<img src="{e(c["imgs"][0])}" alt="{e(c["name"])}" loading="lazy" decoding="async">']
        imgs += [f'<img class="shot-src" src="{e(u)}" alt="" loading="lazy" decoding="async" hidden>' for u in c["imgs"][1:4]]
    else:
        imgs = ['<div class="ph">Photo coming soon</div>']
    if ribbon: imgs.insert(0, ribbon)
    well = "\n          ".join(imgs)
    rows = [f'<div><dt>{e(k)}</dt><dd class="{cls}">{e(v)}</dd></div>' for k, v, cls in fields]
    sw = "".join(swatch(n, False) for n in c["colors"]) + "".join(swatch(n, True) for n in c["ltd"])
    if sw: rows.append(f'<div><dt>Colours</dt><dd><ul class="swatches">{sw}</ul></dd></div>')
    if c["notes"]: rows.append('<div><dt>Notes</dt><dd><ul class="notes">' + "".join(f"<li>{e(n)}</li>" for n in c["notes"]) + "</ul></dd></div>")
    fields_html = "\n            ".join(rows)
    soon = " is-soon" if c.get("soon") else ""
    return f'''      <article class="card{soon}" data-search="{e(search)}" data-key="{key}">
        <div class="well">
          {well}
        </div>
        <div class="body">
          <h3 class="name">{e(c["name"])}</h3>
          <dl class="fields">
            {fields_html}
          </dl>
        </div>
      </article>'''

sections_html = "\n".join(f'''  <section class="cat{" is-proto" if sid == "proto" else ""}" id="{sid}" aria-labelledby="{sid}-h">
    <header class="cat-head">
      <h2 id="{sid}-h">{e(title)}{f' <span class="cat-tag">({e(years)})</span>' if years else ""}</h2>
      <p class="cat-count" data-total="{len(cards)}">{len(cards)} {"item" if len(cards)==1 else "items"}</p>
    </header>
    <div class="grid">
{chr(10).join(card(sid, i, c) for i, c in enumerate(cards))}
    </div>
  </section>''' for sid, title, years, cards in SECTIONS)

chips = "".join(f'<a class="chip" href="#{sid}" data-target="{sid}"><span>{e(title)}</span><span class="chip-n">{len(cards)}</span></a>' for sid, title, _, cards in SECTIONS)

extra_css = """
/* ================= dotaio-by-dotmod page additions ================= */
/* Product shots are cut-outs on white or transparent backgrounds, so they sit
   whole (contain) on a white print instead of being cropped to fill. */
.well img, .thumb img { object-fit: contain; background: #fff; }
.well .ph { border-radius: 16px; }
.back-link {
  display: inline-flex; align-items: center; gap: 8px;
  margin: 0 0 22px; padding: 7px 14px 7px 10px;
  border: 1.5px solid var(--line); border-radius: 999px;
  color: var(--ink-2); text-decoration: none; font-size: .92rem; font-weight: 600;
  font-variation-settings: "wdth" 96; background: var(--surface);
  transition: border-color .18s ease, color .18s ease;
}
.back-link:hover { border-color: var(--brass); color: var(--ink); }
.swatches { list-style: none; margin: 0; padding: 0; display: flex; flex-wrap: wrap; gap: 6px; }
.swatches li {
  display: inline-flex; align-items: center; gap: 6px;
  padding: 4px 10px 4px 5px; border: 1px solid var(--line); border-radius: 999px;
  font-size: .9rem; line-height: 1.2; color: var(--ink-2); background: var(--bg);
}
.swatches i { width: 14px; height: 14px; border-radius: 50%; flex: 0 0 auto; box-shadow: inset 0 0 0 1px rgba(0,0,0,.25); }
.sw-ltd {
  margin-left: 2px; font-size: .62rem; font-weight: 750; letter-spacing: .07em; text-transform: uppercase;
  color: var(--brass);
}
/* "Coming soon" ribbon across the top-left corner of a card's big photo. */
.well .soon-ribbon {
  position: absolute; z-index: 2; top: 30px; left: -52px; width: 210px;
  transform: rotate(-45deg);
  padding: 7px 0; text-align: center;
  background: #b88a35; color: #fff;
  font-size: .78rem; font-weight: 800; letter-spacing: .14em; text-transform: uppercase;
  font-variation-settings: "wdth" 110;
  box-shadow: 0 3px 10px rgba(0, 0, 0, .35);
  pointer-events: none;
}
@media (max-width: 639px) { .well .soon-ribbon { top: 26px; left: -54px; width: 200px; padding: 5px 0; font-size: .6rem; letter-spacing: .1em; } }
.foot { padding: 28px 0 60px; border-top: 1px solid var(--line); color: var(--ink-3); font-size: .92rem; }
.foot a { color: var(--ink-2); }
@media (max-width: 639px) { .swatches li { font-size: .8rem; } }
"""


import json
BASE = "https://asrialbaker.github.io/dotrba-masterlist/"
URL = BASE + "dotaio-by-dotmod/"
DESC = "Every dotAIO by dotmod from 2019 to 2026, plus the dotAMP and dotApollo collabs: launch dates, versions, limited editions and colours. Compiled by Asri Al-Baker."
OG_IMG = BASE + "images/dotaio-v2-iceberg-1.jpg"
items = [c["name"] for _, _, _, cs in SECTIONS for c in cs]
ld = {"@context": "https://schema.org", "@graph": [
  {"@type": "CollectionPage", "@id": URL + "#page", "url": URL,
   "name": "Devices developed by dotmod, and collabs", "description": DESC, "inLanguage": "en",
   "isPartOf": {"@type": "WebSite", "@id": BASE + "#website", "url": BASE, "name": "DOTRBA Masterlist"},
   "author": {"@type": "Person", "@id": BASE + "#asri", "name": "Asri al-Baker",
              "sameAs": ["https://www.youtube.com/@wak-aio", "https://www.instagram.com/wak.aio"]},
   "primaryImageOfPage": OG_IMG,
   "breadcrumb": {"@id": URL + "#breadcrumb"},
   "mainEntity": {"@type": "ItemList", "name": "dotmod devices and collabs", "numberOfItems": len(items),
                  "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n} for i, n in enumerate(items)]}},
  {"@type": "BreadcrumbList", "@id": URL + "#breadcrumb", "itemListElement": [
   {"@type": "ListItem", "position": 1, "name": "DOTRBA Masterlist", "item": BASE},
   {"@type": "ListItem", "position": 2, "name": "Devices developed by dotmod, and collabs", "item": URL}]}]}
SEO = f"""<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="icon" href="/dotrba-masterlist/favicon.ico" sizes="48x48">
<link rel="icon" type="image/png" sizes="32x32" href="/dotrba-masterlist/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/dotrba-masterlist/favicon-16x16.png">
<link rel="icon" type="image/png" sizes="192x192" href="/dotrba-masterlist/icon-192.png">
<link rel="apple-touch-icon" sizes="180x180" href="/dotrba-masterlist/apple-touch-icon.png">
<link rel="manifest" href="/dotrba-masterlist/site.webmanifest">
<meta name="theme-color" content="#1b252e">
<link rel="canonical" href="{URL}">
<meta name="author" content="Asri al-Baker">
<meta property="og:type" content="website">
<meta property="og:site_name" content="DOTRBA Masterlist">
<meta property="og:title" content="Devices developed by dotmod, and collabs, 2019–2026">
<meta property="og:description" content="{DESC}">
<meta property="og:url" content="{URL}">
<meta property="og:image" content="{OG_IMG}">
<meta property="og:image:width" content="900">
<meta property="og:image:height" content="900">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Devices developed by dotmod, and collabs, 2019–2026">
<meta name="twitter:description" content="{DESC}">
<meta name="twitter:image" content="{OG_IMG}">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>"""

page = f'''<!doctype html>
<!-- GENERATED by tools/dotaio/build.py - do not edit this file by hand. Change tools/dotaio/build.py or tools/dotaio/doors.html, then run: python3 tools/dotaio/build.py .  (see CLAUDE.md) -->
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="referrer" content="no-referrer">
<title>Devices developed by dotmod, and collabs: every model and edition, 2019–2026 | DOTRBA Masterlist</title>
<meta name="description" content="{DESC}">
{SEO}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,300..900&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@500;700&display=swap" rel="stylesheet">
<style>
{css}
{extra_css}
</style>
</head>
<body>
<header class="hero">
  <div class="wrap">
    <a class="back-link" href="../"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m14.5 5-7 7 7 7"/></svg>DOTRBA Masterlist</a>
    <h1>DEVICES DEVELOPED BY DOTMOD, AND COLLABS</h1>
    <p class="by">Compiled by <strong>Asri al-Baker</strong></p>
    {profile}
{DOORS}
    <dl class="meta"><div class="meta-item"><dt>First release</dt><dd>June 24, 2019</dd></div><div class="meta-item"><dt>Latest model</dt><dd>dotAIO V3 · November 21, 2025</dd></div><div class="meta-item is-count"><dt>Models and editions, 2019 to 2026</dt><dd>{total}</dd></div><div class="meta-item is-count"><dt>Product lines</dt><dd>{lines}</dd></div><div class="meta-item is-count"><dt>Limited editions</dt><dd>{limited}</dd></div></dl>
  </div>
</header>

<nav class="bar" aria-label="Generations and search">
  <div class="wrap bar-inner">
    <div class="search">
      <label for="q" class="sr-only">Search the list</label>
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
      <input id="q" type="search" placeholder="Search model, colour or notes" autocomplete="off">
    </div>
    <div class="chips">{chips}</div>
  </div>
</nav>

<main class="wrap">

{sections_html}
  <div class="empty" id="empty" hidden>
    <p id="empty-msg"></p>
    <button type="button" id="clear">Clear search</button>
  </div>
</main>

<footer class="wrap foot">
  <p>Launch dates are from dotmod's official <a href="https://dotmod.com/blogs/news/dotaio-timeline-and-evolution" target="_blank" rel="noopener noreferrer">dotAIO timeline</a>. Limited colours came out after their base model; dotmod didn't publish their exact dates. The collabs aren't on dotmod's timeline: retailers first listed the dotAMP in December 2024 (dotmod France shipped it from December 23, 2024), and the dotApollo was in retail by September 2025. Photos load from dotmod.com and authorised retailers.</p>
</footer>

{lightbox}<script src="dotaio.js"></script>
</body>
</html>
'''

out = repo / "dotaio-by-dotmod"
out.mkdir(exist_ok=True)
(out / "index.html").write_text(page, encoding="utf-8")
print("cards:", total, "limited:", limited)
