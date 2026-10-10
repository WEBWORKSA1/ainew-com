"""Build AiNew.com into static HTML at the repository root.

Usage:  python3 _build/build.py      (Python 3.12+)
Sources: _src/guides/*.html, _src/data/tools.json, _src/data/prompts.json
"""
import json, os, re, html, shutil, datetime
from pathlib import Path

import layout as L
import pages_a as A
import pages_b as B
import pages_c as C

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "_src"

TOOL_CATS = ["Chat assistants", "Writing", "Images", "Video", "Audio & voice", "Coding", "Productivity", "Research",
             "Automation", "Design", "Marketing", "Data & analytics", "Developer platforms", "Education"]
GUIDE_CATS = ["Foundations", "Prompting", "Business", "Build", "Creative", "Safety", "Careers"]
GUIDE_ORDER = ["what-is-generative-ai", "ai-for-small-business", "prompt-engineering-guide", "how-large-language-models-work",
               "ai-agents-explained", "ai-automation-workflows", "make-money-with-ai", "rag-explained", "choosing-an-ai-model",
               "ai-privacy-security-checklist", "ai-image-video-generation", "ai-content-copyright-basics",
               "ai-career-skills-roadmap", "ai-glossary"]

written = []


def write(rel, content):
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    written.append(rel)


def strip_tags(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s)).strip()


def load_guides():
    out = []
    for f in sorted((SRC / "guides").glob("*.html")):
        raw = f.read_text(encoding="utf-8")
        m = re.match(r"\s*<!--META\s+(\{.*?\})\s*-->", raw, re.S)
        meta = json.loads(m.group(1))
        body = raw[m.end():].strip()
        meta["slug"] = f.stem
        meta["body"] = body
        meta["words"] = len(strip_tags(body).split())
        out.append(meta)
    out.sort(key=lambda g: GUIDE_ORDER.index(g["slug"]) if g["slug"] in GUIDE_ORDER else 99)
    return out


def guide_page(g, guides):
    body = g["body"]
    # external links open in a new tab
    def ext(m):
        tag = m.group(0)
        if "target=" in tag:
            return tag
        return tag[:-1] + ' target="_blank" rel="noopener">'
    body = re.sub(r'<a\s+href="https?://[^"]+"[^>]*>', ext, body)
    h2s = re.findall(r'<h2[^>]*id="([^"]+)"[^>]*>(.*?)</h2>', body, re.S)
    toc = "".join(f'<li><a href="#{i}">{html.escape(strip_tags(t))}</a></li>' for i, t in h2s if i != "key-takeaways")
    cta = ('<div class="inline-cta"><p>Want this working in your business, not just on paper? Get a free, written AI starting plan.</p>'
           '<a class="btn sm" href="../ai-services.html#plan">Get my free AI plan</a></div>')
    # put the call to action before the third main section
    idx = [m.start() for m in re.finditer(r"<h2", body)]
    if len(idx) >= 4:
        body = body[:idx[3]] + cta + body[idx[3]:]
    else:
        body += cta
    faqs = re.findall(r"<details>\s*<summary>(.*?)</summary>(.*?)</details>", body, re.S)
    related = [x for x in guides if x["category"] == g["category"] and x["slug"] != g["slug"]]
    related += [x for x in guides if x not in related and x["slug"] != g["slug"]]
    rel_html = "".join(f'<a class="gcard" href="{x["slug"]}.html"><span class="cat">{html.escape(x["category"])}</span><h3>{html.escape(x["title"])}</h3><p>{html.escape(x["summary"])}</p><span class="mins">{x["readMinutes"]} min read</span></a>' for x in related[:3])
    upd = datetime.date.fromisoformat(L.UPDATED).strftime("%B %-d, %Y")
    content = f'''<section class="page-head"><div class="wrap">
<nav class="crumbs" aria-label="Breadcrumb"><a href="../index.html">Home</a> / <a href="index.html">Guides</a> / {html.escape(g["category"])}</nav>
<h1 style="max-width:22ch">{html.escape(g["title"])}</h1>
<p class="lede">{html.escape(g["summary"])}</p>
<div class="byline"><span>By the AiNew editorial team</span><span>Updated {upd}</span><span>{g["readMinutes"]} min read</span></div>
</div></section>
<section class="section tight" style="padding-top:8px"><div class="wrap article-layout">
<article class="prose">{body}
<p class="small muted" style="font-family:var(--f-ui);margin-top:2em">This guide is general information, not professional advice. Spotted an error? <a href="../contact.html?topic=Correction">Tell us</a>.</p>
</article>
<aside><nav class="toc" aria-label="On this page"><h2>On this page</h2><ol>{toc}</ol>
<a class="btn sm" href="../ai-services.html#plan">Get a free AI plan</a></nav></aside>
</div>
<div class="wrap">
<div class="panel" style="margin-top:40px;display:flex;justify-content:space-between;gap:20px;align-items:center;flex-wrap:wrap"><div><h2 style="margin-bottom:4px">Get one useful AI email a week</h2><p class="muted" style="margin:0">New guides, tools worth trying and a prompt to steal.</p></div>{L.newsletter_form("", "guide", "Subscribe free")}</div>
<div class="related"><h2>Keep reading</h2><div class="card-grid">{rel_html}</div></div>
</div></section>'''
    url = f"{L.SITE}/guides/{g['slug']}.html"
    schema = [
        {"@context": "https://schema.org", "@type": "Article", "headline": g["title"], "description": g["description"],
         "datePublished": L.UPDATED, "dateModified": L.UPDATED, "wordCount": g["words"],
         "author": {"@type": "Organization", "name": "AiNew editorial team", "url": f"{L.SITE}/about.html"},
         "publisher": {"@type": "Organization", "name": "AiNew.com", "logo": {"@type": "ImageObject", "url": f"{L.SITE}/assets/img/icon-512.png"}},
         "mainEntityOfPage": url, "image": f"{L.SITE}/assets/img/og-image.png", "articleSection": g["category"]},
        L.breadcrumb([("Home", ""), ("Guides", "guides/"), (g["title"], f"guides/{g['slug']}.html")]),
    ]
    if faqs:
        schema.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": strip_tags(q), "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}} for q, a in faqs]})
    return L.page(f"guides/{g['slug']}.html", g["title"], g["description"], content, "guides", schema=schema, og_type="article")


def favicon_and_images():
    img = ROOT / "assets" / "img"
    img.mkdir(parents=True, exist_ok=True)
    (img / "favicon.svg").write_text('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#151A3A"/><rect x="9" y="36" width="46" height="13" rx="3" fill="#FFE15A" transform="rotate(-4 32 42)"/><text x="32" y="44" font-family="Arial,Helvetica,sans-serif" font-size="30" font-weight="800" text-anchor="middle" fill="#ffffff" letter-spacing="-1">Ai</text></svg>''')
    written.append("assets/img/favicon.svg")
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        return
    def font(size, bold=True):
        for p in ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]:
            if os.path.exists(p):
                return ImageFont.truetype(p, size)
        return ImageFont.load_default()
    # OG image
    W, H = 1200, 630
    im = Image.new("RGB", (W, H), "#EDF0F7")
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W, 18], fill="#2F3DF5")
    f1 = font(150)
    x, y = 90, 150
    d.text((x, y), "Ai", font=f1, fill="#151A3A")
    wAi = d.textlength("Ai", font=f1)
    wNew = d.textlength("New", font=f1)
    d.rounded_rectangle([x + wAi + 6, y + 30, x + wAi + wNew + 30, y + 175], radius=14, fill="#FFE15A")
    d.text((x + wAi + 18, y), "New", font=f1, fill="#151A3A")
    d.text((x + wAi + wNew + 44, y + 78), ".com", font=font(60, False), fill="#737A9C")
    d.text((x, 395), "What's new in AI, sorted and explained.", font=font(46), fill="#151A3A")
    d.text((x, 465), "News radar  |  AI tools  |  Guides  |  Prompts  |  AI help for business", font=font(28, False), fill="#4A5175")
    im.save(img / "og-image.png", optimize=True)
    written.append("assets/img/og-image.png")
    for s in (192, 512):
        ic = Image.new("RGB", (s, s), "#151A3A")
        dd = ImageDraw.Draw(ic)
        dd.rectangle([int(s * .14), int(s * .58), int(s * .86), int(s * .76)], fill="#FFE15A")
        fz = font(int(s * .46))
        tw = dd.textlength("Ai", font=fz)
        dd.text(((s - tw) / 2, s * .2), "Ai", font=fz, fill="#FFFFFF")
        ic.save(img / f"icon-{s}.png", optimize=True)
        written.append(f"assets/img/icon-{s}.png")


def main():
    guides = load_guides()
    tools = json.loads((SRC / "data" / "tools.json").read_text())
    prompts = json.loads((SRC / "data" / "prompts.json").read_text())
    pcats = []
    for p in prompts:
        if p["category"] not in pcats:
            pcats.append(p["category"])
    tcats = [c for c in TOOL_CATS if any(t["category"] == c for t in tools)]

    org = {"@context": "https://schema.org", "@type": "Organization", "name": "AiNew.com", "url": L.SITE,
           "logo": f"{L.SITE}/assets/img/icon-512.png"}
    site = {"@context": "https://schema.org", "@type": "WebSite", "name": "AiNew.com", "url": L.SITE,
            "potentialAction": {"@type": "SearchAction", "target": f"{L.SITE}/search.html?q={{search_term_string}}",
                                "query-input": "required name=search_term_string"}}

    P = []  # (path, title, desc, body, active, kwargs)
    P.append(("index.html", L.NAME, "What's new in AI, sorted and explained: a live AI news radar, a curated directory of AI tools, practical guides, ready-to-use prompts and help for businesses.", A.home(guides, tools, prompts, tcats), "", {"schema": [org, site]}))
    P.append(("news.html", "AI news radar", "Live AI headlines from respected publishers and research labs, refreshed every few hours and linked to the original source.", A.news(), "news", {}))
    P.append(("tools.html", "AI tools directory", f"Search {len(tools)} established AI tools across {len(tcats)} categories. Filter by task and pricing model, from chat assistants to video, coding and automation.", A.tools_page(tools, tcats), "tools", {}))
    P.append(("prompts.html", "Prompt library", f"{len(prompts)} original, copy-ready AI prompts for business strategy, marketing, sales, writing, productivity, learning, coding and creative work.", A.prompts_page(prompts, pcats), "prompts", {}))
    P.append(("videos.html", "AI video hub", "Hand-picked video explainers on neural networks, transformers and large language models, each paired with an in-depth AiNew guide.", A.videos_page(), "videos", {}))
    P.append(("guides/index.html", "AI guides", "Practical, plain-English guides to generative AI, prompting, AI agents, RAG, automation, AI safety, copyright and AI careers.", A.guides_hub(guides, GUIDE_CATS), "guides", {}))
    P.append(("search.html", "Search", "Search AiNew guides, AI tools and prompts.", A.search_page(), "", {"noindex": True}))
    P.append(("ai-services.html", "Get AI help for your business", "Tell us the task you want done faster and get a free written AI plan within two business days, plus optional introductions to vetted AI specialists.", B.ai_services(), "", {}))
    P.append(("readiness.html", "AI readiness score", "Take the free 2-minute AI readiness check. Answer 10 questions and get an instant score and recommended next step for your business.", B.readiness(), "", {}))
    P.append(("advertise.html", "Advertise and sponsor", "Featured AI tool listings, newsletter sponsorships, guide partnerships and contest prize sponsorship on AiNew.com. Clearly labelled, transparent pricing.", B.advertise(), "", {}))
    P.append(("submit-tool.html", "Submit an AI tool", "Submit your AI tool for a free editorial listing in the AiNew tools directory, or ask about a featured placement.", B.submit_tool(tcats), "tools", {}))
    P.append(("contests.html", "AiNew Build Challenge", "Enter the AiNew Build Challenge: build an AI workflow that saves a small business five hours a week and compete for a sponsor-funded prize pool.", B.contests(), "contests", {}))
    P.append(("support.html", "Support AiNew", "Support independent AI education. Contributions fund new guides, paid work for creators, promotion and the AiNew contest prize pool.", B.support(), "support", {}))
    P.append(("careers.html", "Careers and talent network", "Paid, remote work with AiNew for AI writers, video creators, community managers, partnership sellers and AI implementation specialists.", B.careers(), "", {}))
    P.append(("newsletter.html", "The AiNew Weekly newsletter", "Subscribe to The AiNew Weekly: one short email with the AI developments worth knowing, a tool to try, a prompt and a guide.", B.newsletter(guides[0], tools[0], prompts[0]), "", {}))
    P.append(("contact.html", "Contact", "Contact AiNew.com about corrections, AI services, advertising, partnerships, press or copyright questions.", B.contact(), "", {}))
    P.append(("about.html", "About AiNew", "AiNew.com is an independent publication that tracks what's new in AI and explains it in plain English. Learn who we are and how we make money.", C.about(len(guides), len(tools), len(prompts)), "", {}))
    P.append(("editorial-policy.html", "Editorial policy", "How AiNew.com researches, writes, labels sponsored content, lists tools and corrects mistakes.", C.editorial(), "", {}))
    P.append(("privacy.html", "Privacy policy", "How AiNew.com collects and uses information, including Google AdSense advertising cookies, form submissions and your privacy choices.", C.privacy(), "", {}))
    P.append(("terms.html", "Terms of use", "Terms of use for AiNew.com: content ownership, permitted use, submissions, contributions and liability.", C.terms(), "", {}))
    P.append(("disclaimer.html", "Disclaimer", "AiNew.com disclaimer and disclosures: general information only, advertising, sponsorships and partner relationships.", C.disclaimer(), "", {}))
    P.append(("legal.html", "Trademark and copyright disclosure", "Trademark and copyright disclosure for AiNew.com, including third-party marks, embedded content and how to report infringement.", C.legal(), "", {}))
    P.append(("thank-you.html", "Thank you", "Your submission was received.", C.thank_you(), "", {"noindex": True, "ads": False}))
    P.append(("404.html", "Page not found", "The page you were looking for could not be found.", C.not_found(), "", {"noindex": True, "ads": False}))

    for path, title, desc, body, active, kw in P:
        if path not in ("index.html",) and "schema" not in kw:
            crumbs = [("Home", "")] + ([("Guides", "guides/")] if path.startswith("guides/") else [(title, path)])
            kw["schema"] = [L.breadcrumb(crumbs)]
        out = L.page(path, title, desc, body, active, **kw)
        if path == "404.html":
            out = out.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n<script>document.write(\'<base href="\'+(location.pathname.toLowerCase().indexOf("/ainew-com/")===0?location.pathname.slice(0,11):"/")+\'">\')</script>', 1)
        write(path, out)

    for g in guides:
        write(f"guides/{g['slug']}.html", guide_page(g, guides))

    # public data
    write("data/prompts.json", json.dumps(prompts, ensure_ascii=False))
    if not (ROOT / "data" / "news.json").exists():
        write("data/news.json", json.dumps({"updated": None, "items": []}))
    idx = [{"t": g["title"], "d": g["summary"], "x": " ".join(strip_tags(h) for h in re.findall(r"<h2[^>]*>(.*?)</h2>", g["body"])) + " " + g["category"], "u": f"guides/{g['slug']}.html", "k": "Guide"} for g in guides]
    idx += [{"t": t["name"], "d": t["desc"], "x": t["category"] + " " + " ".join(t.get("tags", [])) + " " + t["pricing"], "u": "tools.html?q=" + t["name"].replace(" ", "%20"), "k": "Tool"} for t in tools]
    idx += [{"t": p["title"], "d": p["use"], "x": p["category"], "u": "prompts.html?q=" + p["title"].replace(" ", "%20"), "k": "Prompt"} for p in prompts]
    idx += [{"t": t, "d": d, "x": "", "u": p, "k": "Page"} for p, t, d, *_ in P if p not in ("search.html", "thank-you.html", "404.html", "index.html")]
    write("data/search.json", json.dumps(idx, ensure_ascii=False))

    # sitemap, robots, ads.txt, manifest
    urls = [p for p, *_ in P if p not in ("search.html", "thank-you.html", "404.html")] + [f"guides/{g['slug']}.html" for g in guides]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for u in urls:
        loc = u[:-10] if u.endswith("index.html") else u
        pr = "1.0" if u == "index.html" else ("0.8" if u.startswith("guides/") or u in ("tools.html", "news.html", "ai-services.html") else "0.6")
        sm += f"  <url><loc>{L.SITE}/{loc}</loc><lastmod>{L.UPDATED}</lastmod><priority>{pr}</priority></url>\n"
    write("sitemap.xml", sm + "</urlset>\n")
    write("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /search.html\nDisallow: /thank-you.html\n\nSitemap: {L.SITE}/sitemap.xml\n")
    write("ads.txt", "google.com, pub-6620975821265271, DIRECT, f08c47fec0942fa0\n")
    write("site.webmanifest", json.dumps({"name": "AiNew.com", "short_name": "AiNew", "start_url": "./index.html", "display": "standalone",
                                          "background_color": "#EDF0F7", "theme_color": "#2F3DF5",
                                          "icons": [{"src": "assets/img/icon-192.png", "sizes": "192x192", "type": "image/png"},
                                                    {"src": "assets/img/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, indent=1))
    favicon_and_images()
    print(f"Built {len(written)} files: {len(P)} pages, {len(guides)} guides, {len(tools)} tools, {len(prompts)} prompts")


if __name__ == "__main__":
    main()
