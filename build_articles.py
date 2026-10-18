#!/usr/bin/env python3
"""Build justinhelmer.ca editorial pages. Does not touch index.html, lyrics/, 404.html."""
from __future__ import annotations

import html
import json
from pathlib import Path

from content_pages import PAGES, AUTHOR
from expansions import EXTRA

ROOT = Path(__file__).resolve().parent
SITE = "https://justinhelmer.ca"
PUB = "ca-pub-0646320966060599"
UPDATED = "2026-10-20"

HEAD = """<!DOCTYPE html>
<html lang="en" data-cookie-key="justinhelmer_cookies">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="Justin Helmer / Excavationpro">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<link rel="canonical" href="{canonical}">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png" sizes="180x180">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;1,500&family=IBM+Plex+Mono:wght@400&family=Syne:wght@500;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site-kit.css">
<link rel="stylesheet" href="/assets/article.css">
<meta name="google-adsense-account" content="{pub}">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={pub}" crossorigin="anonymous"></script>
<meta property="og:type" content="article">
<meta property="og:url" content="{canonical}">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{desc}">
<meta property="og:site_name" content="justinhelmer.ca">
<meta property="og:image" content="{image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:alt" content="Justin Helmer — music, lyrics, live rooms">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@Excavationpro">
<meta name="twitter:creator" content="@Excavationpro">
<meta name="twitter:title" content="{og_title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{image}">
<meta name="twitter:image:alt" content="Justin Helmer — music, lyrics, live rooms">
<meta name="theme-color" content="#0f1218">
<script type="application/ld+json">{schema}</script>
</head>
<body>
"""

HEADER = """<header class="site">
  <div class="wrap nav">
    <a class="brand" href="/">Justin Helmer</a>
    <nav class="navlinks" aria-label="Primary">
      <a href="/"{home}>Home</a>
      <a href="/music.html"{music}>Music</a>
      <a href="/lyrics/"{lyrics}>Lyrics</a>
      <a href="/about.html"{about}>About</a>
      <a href="/press.html"{press}>Press</a>
      <a href="/contact.html"{contact}>Contact</a>
      <a href="https://bpmfinder.ca/tools.html" class="nav-tools">Tools</a>
    </nav>
  </div>
</header>
"""

FOOTER = """<footer class="site">
  <div class="wrap">
    <nav aria-label="Footer">
      <a href="/">Home</a>
      <a href="/music.html">Music</a>
      <a href="/listen.html">How to listen</a>
      <a href="/lyrics/">Lyrics</a>
      <a href="/about.html">About</a>
      <a href="/press.html">Press</a>
      <a href="/contact.html">Contact</a>
      <a href="/privacy.html">Privacy</a>
      <a href="/terms.html">Terms</a>
    </nav>
    <p class="family">
      <span>More from the workshop:</span>
      <a href="https://excavationpro.ca/">Excavationpro &mdash; artist house</a>
      <a href="https://asiancoastline.com/">Asian Coastline &mdash; free player</a>
      <a href="https://bpmfinder.ca/">BPMfinder &mdash; tempo tools</a>
      <a href="https://deepseekoracle.com/">DeepSeek Oracle &mdash; AI &amp; creator guides</a>
      <a href="https://eternalhaven.ca/">Eternal Haven &mdash; books &amp; games</a>
      <a href="https://chatagent.ca/">Chatagent &mdash; AI agent guides</a>
    </p>
    <p>&copy; 2026 Justin Helmer / Excavationpro &middot; justinhelmer.ca &mdash; official name portal.
    Contact: <a href="mailto:excavationstation@gmail.com">excavationstation@gmail.com</a></p>
  </div>
</footer>
"""

COOKIE = """<div class="cookie-banner" id="cookieBanner" role="dialog" aria-label="Cookie consent">
  <div>Ads may use cookies after you accept. <a href="/privacy.html">Privacy</a></div>
  <div>
    <button type="button" class="ok" id="cookieOk">Accept</button>
    <button type="button" class="no" id="cookieNo">Decline</button>
  </div>
</div>
<script src="/assets/site-kit.js"></script>
</body>
</html>
"""


def plain(value: str) -> str:
    return html.unescape(value)


def attr(value: str) -> str:
    return html.escape(plain(value), quote=True)


def schema_for(slug: str, page: dict) -> str:
    canonical = SITE + page["path"]
    title = plain(page["h1"])
    desc = plain(page["desc"])
    graph = [
        {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/",
         "name": "Justin Helmer", "publisher": {"@id": SITE + "/#person"}},
        {"@type": "Person", "@id": SITE + "/#person", "name": "Justin Helmer",
         "alternateName": ["Excavationpro", "Lightfather"], "url": SITE + "/",
         "sameAs": ["https://excavationpro.ca/", "https://asiancoastline.com/",
                    "https://x.com/Excavationpro",
                    "https://bsky.app/profile/excavationpro.bsky.social"]},
        {"@type": "MusicGroup", "@id": SITE + "/#musicgroup", "name": "Excavationpro",
         "alternateName": "Justin Helmer", "url": SITE + "/"},
    ]

    if slug == "about.html":
        graph.append({"@type": "AboutPage", "@id": canonical + "#page", "url": canonical,
                      "name": title, "description": desc, "isPartOf": {"@id": SITE + "/#website"}})
    elif slug == "press.html":
        graph.append({"@type": "Article", "@id": canonical + "#article", "headline": title,
                      "description": desc, "url": canonical,
                      "author": {"@type": "Person", "name": "Justin Helmer"},
                      "publisher": {"@id": SITE + "/#person"},
                      "datePublished": page.get("updated", UPDATED),
                      "dateModified": page.get("updated", UPDATED)})
    elif slug == "privacy.html":
        graph.append({"@type": "PrivacyPolicy", "@id": canonical + "#page", "url": canonical,
                      "name": title, "description": desc, "isPartOf": {"@id": SITE + "/#website"}})
    elif slug == "terms.html":
        graph.append({"@type": "TermsOfService", "@id": canonical + "#page", "url": canonical,
                      "name": title, "description": desc, "isPartOf": {"@id": SITE + "/#website"}})
    elif slug == "contact.html":
        graph.append({"@type": "ContactPage", "@id": canonical + "#page", "url": canonical,
                      "name": title, "description": desc, "isPartOf": {"@id": SITE + "/#website"}})
    elif slug == "listen.html":
        graph.append({"@type": "WebPage", "@id": canonical + "#page", "url": canonical,
                      "name": title, "description": desc, "isPartOf": {"@id": SITE + "/#website"}})
    else:
        graph.append({"@type": "CollectionPage", "@id": canonical + "#page", "url": canonical,
                      "name": title, "description": desc, "isPartOf": {"@id": SITE + "/#website"}})

    if page.get("faqs"):
        graph.append({"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": plain(q),
             "acceptedAnswer": {"@type": "Answer", "text": plain(a)}} for q, a in page["faqs"]
        ]})

    crumbs = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"}]
    crumbs.append({"@type": "ListItem", "position": 2, "name": title, "item": canonical})
    graph.append({"@type": "BreadcrumbList", "itemListElement": crumbs})
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)


def header(active: str) -> str:
    keys = ["home", "music", "lyrics", "about", "press", "contact"]
    marks = {k: ' aria-current="page"' for k in keys if k == active}
    return HEADER.format(**{k: marks.get(k, "") for k in keys})


def hero(page: dict) -> str:
    tags = "".join(f'<span class="tag">{t}</span>' for t in page.get("tags", []))
    path = page.get("path", "")
    if path in ("/about.html", "/press.html", "/contact.html", "/privacy.html", "/terms.html"):
        label = path.strip("/").split(".")[0].capitalize()
        crumb = f'<a href="/">Home</a> / {label}'
        kind = "Press" if path == "/press.html" else label
    elif path == "/music.html":
        crumb = '<a href="/">Home</a> / Music'
        kind = "Catalog"
    elif path == "/listen.html":
        crumb = '<a href="/">Home</a> / <a href="/music.html">Music</a> / How to listen'
        kind = "Guide"
    else:
        crumb = f'<a href="/">Home</a> / {plain(page["h1"])}'
        kind = "Page"
    return f"""<section class="hero">
  <p class="breadcrumb">{crumb}</p>
  <h1>{page["h1"]}</h1>
  <p class="lead">{page["lead"]}</p>
  <p class="article-meta">{kind} &middot; Justin Helmer &middot; <time datetime="{page.get("updated", UPDATED)}">Updated {page.get("updated", UPDATED)}</time> &middot; {page.get("minutes", "6 min read")} &middot; {tags}</p>
  <div class="cta-row">
    <a class="btn primary" href="https://asiancoastline.com/listen.html">Open the free player</a>
    <a class="btn" href="/music.html">The catalog</a>
  </div>
</section>"""


def build() -> None:
    for slug, page in PAGES.items():
        canonical = SITE + page["path"]
        head = HEAD.format(title=page["title"], desc=attr(page["desc"]), canonical=canonical,
                           pub=PUB, og_title=attr(page["title"]),
                           image=SITE + "/assets/og-home.jpg", schema=schema_for(slug, page))
        body = page["body"]
        extra = EXTRA.get(slug, "")
        if extra:
            if '<article class="card faq">' in body:
                body = body.replace('<article class="card faq">', extra + '\n<article class="card faq">', 1)
            else:
                body += extra
        page_html = f"""{head}{header(page.get("active", "music"))}
<div class="wrap">
{hero(page)}
<main>
{body}
</main>
</div>
{FOOTER}{COOKIE}"""
        (ROOT / slug).write_text(page_html, encoding="utf-8")
        print("wrote", slug, len(page_html), "chars")

    entries = [
        ("/", "1.0"), ("/music.html", "0.95"), ("/listen.html", "0.9"), ("/lyrics/", "0.85"),
        ("/about.html", "0.8"), ("/press.html", "0.7"), ("/contact.html", "0.6"),
        ("/privacy.html", "0.5"), ("/terms.html", "0.5"),
    ]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for path, prio in entries:
        sm.append(f"  <url><loc>{SITE}{path}</loc><lastmod>{UPDATED}</lastmod>"
                  f"<changefreq>{'weekly' if prio >= '0.8' else 'monthly'}</changefreq>"
                  f"<priority>{prio}</priority></url>")
    sm.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(sm) + "\n", encoding="utf-8")
    print("wrote sitemap.xml")


if __name__ == "__main__":
    build()
