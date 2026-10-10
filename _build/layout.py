"""Shared layout for AiNew.com pages."""
import json, html

SITE = "https://ainew.com"
NAME = "AiNew.com"
PUB = "ca-pub-6620975821265271"
UPDATED = "2026-10-10"
PROMO_URL = "https://web.works/contact"
OPERATOR_URL = "https://web.works/"

ADSENSE = ('<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6620975821265271"\n'
           '     crossorigin="anonymous"></script>')

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400..800'
         '&family=Newsreader:ital,opsz,wght@0,6..72,400..700;1,6..72,400&display=swap">')

NAV = [
    ("news.html", "News", "news"),
    ("tools.html", "AI tools", "tools"),
    ("guides/", "Guides", "guides"),
    ("prompts.html", "Prompts", "prompts"),
    ("videos.html", "Videos", "videos"),
    ("contests.html", "Contests", "contests"),
    ("support.html", "Support us", "support"),
]

ICON_SUN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>'
ICON_SEARCH = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>'
ICON_MENU = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>'


def esc(s):
    return html.escape(str(s), quote=True)


def promo():
    return (f'<a class="promo" href="{PROMO_URL}" target="_blank" rel="noopener">'
            'Contact, if you are interested in this <strong>website / domain name / Sponsorship / Advertisement / Partnership</strong></a>')


def header(root, active):
    links = "".join(
        f'<a href="{root}{h}"{" aria-current=\"page\"" if key == active else ""}>{t}</a>' for h, t, key in NAV)
    links += f'<a class="m-only" href="{root}ai-services.html">Get AI help</a><a class="m-only" href="{root}advertise.html">Advertise</a>'
    return f'''<header class="site-head"><div class="wrap head-row">
<a class="logo" href="{root}index.html" aria-label="AiNew.com home">Ai<span class="new">New</span><span class="tld">.com</span></a>
<nav class="nav" id="site-nav" aria-label="Main">{links}</nav>
<div class="head-tools">
<a class="icon-btn" href="{root}search.html" aria-label="Search the site">{ICON_SEARCH}</a>
<button class="icon-btn" id="theme-btn" type="button" aria-label="Switch colour theme">{ICON_SUN}</button>
<a class="btn sm" href="{root}ai-services.html">Get AI help</a>
<button class="icon-btn menu-btn" id="menu-btn" type="button" aria-controls="site-nav" aria-expanded="false" aria-label="Open menu">{ICON_MENU}</button>
</div></div></header>'''


def newsletter_form(root, place="footer", btn="Subscribe"):
    return f'''<form class="inline-sub" data-form="newsletter-{place}" data-subject="New newsletter subscriber" data-ok="You're on the list. Watch your inbox for the next issue.">
<label class="visually-hidden" for="nl-{place}">Email address</label>
<input id="nl-{place}" type="email" name="email" placeholder="you@example.com" required autocomplete="email">
<input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
<button class="btn" type="submit">{btn}</button>
<p class="form-msg" role="status"></p></form>'''


def footer(root):
    col = lambda title, items: (f'<div><h2>{title}</h2><ul>' +
                                "".join(f'<li><a href="{root}{h}">{t}</a></li>' for h, t in items) + '</ul></div>')
    return f'''<footer class="site-foot"><div class="wrap">
<div class="foot-grid">
<div><a class="logo" href="{root}index.html">Ai<span class="new">New</span><span class="tld">.com</span></a>
<p class="muted small" style="margin-top:12px">What's new in AI, sorted and explained. Practical guides, a curated tools directory and help for teams putting AI to work.</p>
{newsletter_form(root, "footer")}</div>
{col("Explore", [("news.html","News radar"),("tools.html","AI tools directory"),("guides/","Guides"),("prompts.html","Prompt library"),("videos.html","Videos"),("search.html","Search")])}
{col("For business", [("ai-services.html","Get AI help"),("readiness.html","AI readiness score"),("ai-services.html?goal=talent","Hire AI talent"),("advertise.html","Advertise & sponsor"),("submit-tool.html","Submit a tool")])}
{col("Community", [("contests.html","Contests & prizes"),("support.html","Support AiNew"),("careers.html","Careers & talent network"),("newsletter.html","Newsletter")])}
{col("About", [("about.html","About"),("editorial-policy.html","Editorial policy"),("contact.html","Contact"),("privacy.html","Privacy policy"),("terms.html","Terms of use"),("disclaimer.html","Disclaimer"),("legal.html","Trademark & copyright")])}
</div>
<div class="foot-legal">
<p>&copy; <span data-year>2026</span> AiNew.com. Original articles, prompts and design are protected by copyright. All rights reserved.</p>
<p>AiNew.com is an independent publication. The name refers only to this website's domain and does not refer to, imitate or imply affiliation with any company, product or registered mark of the same or similar name. Third-party names and trademarks belong to their owners and are used for identification only. <a href="{root}legal.html">Full trademark &amp; copyright disclosure</a>.</p>
<p>This site shows ads served by Google and may contain clearly labelled sponsored placements and partner links. <a href="{root}disclaimer.html">How we make money</a>.</p>
</div></div></footer>'''


def cookie(root):
    return f'''<div class="cookie" id="cookie" role="dialog" aria-label="Cookie choices">
<p>We use cookies for essential site features and to show ads from Google, which may be personalised. Choose what you're comfortable with. <a href="{root}privacy.html">Privacy policy</a></p>
<div class="btn-row"><button class="btn sm" data-consent="all" type="button">Accept all</button><button class="btn sm ghost" data-consent="necessary" type="button">Necessary only</button></div></div>'''


def page(path, title, desc, body, active="", ads=True, noindex=False, schema=None, og_type="website", full_title=None):
    depth = path.count("/")
    root = "../" * depth
    canon_path = path[:-10] if path.endswith("index.html") else path
    canon = f"{SITE}/{canon_path}"
    t = full_title or (f"{title} | AiNew.com" if title != NAME else "AiNew.com — What's new in AI, sorted and explained")
    sch = ""
    for s in (schema or []):
        sch += '<script type="application/ld+json">' + json.dumps(s, ensure_ascii=False) + '</script>'
    robots = '<meta name="robots" content="noindex,follow">' if noindex else '<meta name="robots" content="index,follow,max-image-preview:large">'
    out = f'''<!doctype html>
<html lang="en" data-root="{root}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(t)}</title>
<meta name="description" content="{esc(desc)}">
{robots}
<link rel="canonical" href="{canon}">
<meta name="google-adsense-account" content="{PUB}">
<meta property="og:type" content="{og_type}"><meta property="og:site_name" content="AiNew.com">
<meta property="og:title" content="{esc(t)}"><meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canon}"><meta property="og:image" content="{SITE}/assets/img/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#2F3DF5">
<link rel="icon" href="{root}assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{root}assets/img/icon-192.png">
<link rel="manifest" href="{root}site.webmanifest">
<script>try{{var t=localStorage.getItem("ainew-theme");if(t)document.documentElement.setAttribute("data-theme",t)}}catch(e){{}}</script>
{FONTS}
<link rel="stylesheet" href="{root}assets/css/site.css?v={UPDATED}">
{ADSENSE if ads else ""}
{sch}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{promo()}
{header(root, active)}
<main id="main">
{body.replace("{{root}}", root)}
</main>
{footer(root)}
{cookie(root)}
<script src="{root}assets/js/config.js?v={UPDATED}" defer></script>
<script src="{root}assets/js/site.js?v={UPDATED}" defer></script>
</body>
</html>
'''
    return out


def breadcrumb(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": f"{SITE}/{u}"}
                                for i, (n, u) in enumerate(items)]}


def page_head(title, lede, crumbs=None, extra=""):
    c = ""
    if crumbs:
        c = '<nav class="crumbs" aria-label="Breadcrumb">' + " / ".join(
            f'<a href="{{{{root}}}}{u}">{n}</a>' if u else n for n, u in crumbs) + '</nav>'
    return f'<section class="page-head"><div class="wrap">{c}<h1>{title}</h1><p class="lede">{lede}</p>{extra}</div></section>'
