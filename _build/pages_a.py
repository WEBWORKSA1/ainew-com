"""Page bodies: home, news, tools, prompts, videos, guides hub, search."""
from layout import esc, newsletter_form, page_head

HP = '<input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">'

VIDEOS = [
    ("aircAruvnKk", "But what is a neural network?", "3Blue1Brown", "what-is-generative-ai"),
    ("LPZh9BOjkQs", "Large language models explained briefly", "3Blue1Brown", "how-large-language-models-work"),
    ("zjkBMFhNj_g", "Intro to large language models (1-hour talk)", "Andrej Karpathy", "how-large-language-models-work"),
    ("wjZofJX0v4M", "Transformers, the tech behind LLMs", "3Blue1Brown", "how-large-language-models-work"),
    ("eMlx5fFNoYc", "Attention in transformers, step by step", "3Blue1Brown", "ai-glossary"),
    ("7xTGNNLPyMI", "Deep dive into LLMs like ChatGPT", "Andrej Karpathy", "how-large-language-models-work"),
    ("kCc8FmEb1nY", "Let's build GPT: from scratch, in code", "Andrej Karpathy", "ai-career-skills-roadmap"),
]


def yt(vid, title, by, guide, big=False):
    return f'''<div><button class="yt" type="button" data-id="{vid}" aria-label="Play video: {esc(title)}">
<img src="https://i.ytimg.com/vi/{vid}/hqdefault.jpg" alt="" loading="lazy" width="480" height="360">
<span class="play"><svg width="22" height="22" viewBox="0 0 24 24" fill="#fff" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg></span></button>
<div class="vcap"><h3>{esc(title)}</h3><p>{esc(by)} on YouTube. Read alongside: <a href="{{{{root}}}}guides/{guide}.html">our guide</a></p></div></div>'''


MONO_COLORS = ["#2F3DF5", "#151A3A", "#0E7C66", "#9B2C8F", "#C2410C", "#1D6FB8", "#5B4BC4", "#7A5C00"]


def mono(name):
    words = [w for w in name.replace("-", " ").replace(".", " ").split() if w]
    initials = (words[0][0] + (words[1][0] if len(words) > 1 else (words[0][1] if len(words[0]) > 1 else ""))).upper()
    h = sum(ord(c) * (i + 1) for i, c in enumerate(name))
    return initials, MONO_COLORS[h % len(MONO_COLORS)]


def tool_card(t, i, featured=False):
    initials, color = mono(t["name"])
    pclass = {"Free": "free", "Freemium": "freemium", "Open source": "oss"}.get(t["pricing"], "")
    text = (t["name"] + " " + t["desc"] + " " + " ".join(t.get("tags", [])) + " " + t["category"]).lower()
    return f'''<article class="tool" data-name="{esc(t["name"].lower())}" data-cat="{esc(t["category"])}" data-price="{esc(t["pricing"])}" data-order="{i}" data-text="{esc(text)}">
<div class="tool-top"><span class="mono" style="background:{color}" aria-hidden="true">{esc(initials)}</span><div><h3>{esc(t["name"])}</h3><span class="tcat">{esc(t["category"])}</span></div></div>
<p>{esc(t["desc"])}</p>
<div class="badges"><span class="badge {pclass}">{esc(t["pricing"])}</span>{"".join(f'<span class="badge">#{esc(g)}</span>' for g in t.get("tags", [])[:3])}</div>
<a class="visit" href="{esc(t["url"])}" target="_blank" rel="noopener nofollow">Visit {esc(t["name"])}</a>
</article>'''


def home(guides, tools, prompts, cats):
    feat = guides[0]
    rest = guides[1:7]
    glist = "".join(f'<li><a href="{{{{root}}}}guides/{g["slug"]}.html"><h3>{esc(g["title"])}</h3><span class="cat">{esc(g["category"])}</span><span class="mins">{g["readMinutes"]} min</span></a></li>' for g in rest)
    picks = [t for t in tools if t["name"] in ("ChatGPT", "Claude", "Gemini", "Perplexity", "Midjourney", "ElevenLabs", "Zapier", "Cursor")][:8]
    if len(picks) < 8:
        picks = tools[:8]
    tcards = "".join(tool_card(t, i) for i, t in enumerate(picks))
    p0 = prompts[0]
    vids = "".join(yt(*v) for v in VIDEOS[:3])
    return f'''
<section class="hero"><div class="wrap hero-grid">
<div>
<h1>What's <span class="swipe">new in AI</span>, sorted and explained.</h1>
<p class="lede">AI changes every week. AiNew keeps the changelog: the headlines worth knowing, the tools worth trying and plain-English guides that help you use them well.</p>
{newsletter_form("{{root}}", "hero", "Get the weekly brief")}
<p class="fine">Free, one email a week. Unsubscribe any time.</p>
<div class="jump"><a href="{{{{root}}}}tools.html"><span>{len(tools)}</span> AI tools</a><a href="{{{{root}}}}guides/"><span>{len(guides)}</span> in-depth guides</a><a href="{{{{root}}}}prompts.html"><span>{len(prompts)}</span> ready prompts</a><a href="{{{{root}}}}readiness.html">Free AI readiness score</a></div>
</div>
<aside class="changelog" aria-labelledby="cl-h">
<div class="changelog-head"><h2 id="cl-h"><span class="live-dot" aria-hidden="true"></span>AI news radar</h2><span class="small muted" data-radar-updated></span></div>
<ul class="rail" id="radar-mini" aria-live="polite"><li class="empty">Loading the latest headlines…</li></ul>
<p style="margin:12px 0 4px"><a class="more" href="{{{{root}}}}news.html">Open the full radar</a></p>
</aside>
</div></section>

<section class="section tight"><div class="wrap">
<div class="sec-head"><div><h2>Start here</h2><p>Practical guides that stay useful after the hype moves on.</p></div><a class="more" href="{{{{root}}}}guides/">All {len(guides)} guides</a></div>
<div class="guides-layout">
<a class="feature" href="{{{{root}}}}guides/{feat["slug"]}.html"><span class="cat">{esc(feat["category"])}, {feat["readMinutes"]} min read</span><h3>{esc(feat["title"])}</h3><p>{esc(feat["summary"])}</p></a>
<ul class="glist">{glist}</ul>
</div></div></section>

<section class="section tight"><div class="wrap">
<div class="lead-band">
<div><h2>Put AI to work in your business</h2>
<p>Tell us the job you want done faster: support, sales follow-up, content, paperwork. We'll reply with a free starting plan and, if you want it, a vetted specialist to build it.</p>
<div class="btn-row"><a class="btn" href="{{{{root}}}}ai-services.html">Get my free AI plan</a><a class="btn ghost" href="{{{{root}}}}readiness.html">Check my AI readiness</a></div></div>
<ul><li>Answer customer questions around the clock</li><li>Follow up every lead within minutes</li><li>Turn documents and email into clean data</li><li>Hire or train AI-ready talent</li></ul>
</div></div></section>

<section class="section tight"><div class="wrap">
<div class="sec-head"><div><h2>Tools worth knowing</h2><p>{len(tools)} AI tools across {len(cats)} categories, filterable by price.</p></div><a class="more" href="{{{{root}}}}tools.html">Browse the directory</a></div>
<div class="tool-grid">{tcards}</div>
</div></section>

<section class="section tight"><div class="wrap">
<div class="potd" id="potd">
<div><h2>Prompt of the day</h2><p class="muted">A new reusable prompt every day from our library of {len(prompts)}. Fill in the brackets and paste it into any chat assistant.</p><a class="more" href="{{{{root}}}}prompts.html">Open the prompt library</a></div>
<div><p class="small muted" id="potd-cat">{esc(p0["category"])}</p><h3 id="potd-title">{esc(p0["title"])}</h3><p class="small" id="potd-use">{esc(p0["use"])}</p><pre id="potd-text">{esc(p0["prompt"])}</pre><button class="copy-btn" type="button" data-copy="potd-text">Copy prompt</button></div>
</div></div></section>

<section class="section tight"><div class="wrap">
<div class="sec-head"><div><h2>Watch and understand</h2><p>The clearest explainers on how modern AI works, paired with our guides.</p></div><a class="more" href="{{{{root}}}}videos.html">All videos</a></div>
<div class="video-grid">{vids}</div>
</div></section>

<section class="section tight"><div class="wrap split">
<div class="panel"><h2>Build Challenge: prizes for useful AI</h2><p>Our contests reward practical AI workflows that save real people real time. Register to get the brief and the confirmed prize pool before entries open.</p><div class="btn-row"><a class="btn" href="{{{{root}}}}contests.html">See the contest</a><a class="btn ghost" href="{{{{root}}}}advertise.html#sponsor-contest">Sponsor a prize</a></div></div>
<div class="panel inked"><h2>Keep AiNew independent</h2><p>Supporter contributions fund new guides, the contest prize pool and paid work for freelance writers and creators. Every amount helps.</p><div class="btn-row"><a class="btn" href="{{{{root}}}}support.html">Support AiNew</a></div></div>
</div></section>

<section class="section tight"><div class="wrap">
<div class="panel" style="display:flex;justify-content:space-between;gap:20px;align-items:center;flex-wrap:wrap">
<div><h2 style="margin-bottom:6px">Reach people choosing AI tools</h2><p class="muted" style="margin:0">Featured listings, newsletter sponsorships and guide partnerships, always clearly labelled.</p></div>
<div class="btn-row"><a class="btn" href="{{{{root}}}}advertise.html">Advertise with us</a><a class="btn ghost" href="{{{{root}}}}submit-tool.html">Submit a tool</a></div>
</div></div></section>
'''


def news():
    return page_head("AI news radar", "Headlines from respected AI publishers and research labs, refreshed every few hours. We link straight to the original story; we never copy it.",
                     [("Home", "index.html"), ("News radar", "")]) + f'''
<section class="section tight" style="padding-top:0"><div class="wrap two-col">
<div>
<div class="toolbar"><div class="search-row"><label class="visually-hidden" for="radar-q">Filter headlines</label><input id="radar-q" type="search" placeholder="Filter headlines, e.g. agents, open source, regulation"></div>
<div class="chips" id="radar-sources" aria-label="Filter by source"></div></div>
<p class="count-line" data-radar-updated></p>
<ul class="rail" id="radar-full" aria-live="polite"><li class="empty">Loading the latest headlines…</li></ul>
</div>
<aside>
<div class="panel" style="position:sticky;top:84px">
<h2>Get the signal, not the noise</h2>
<p class="muted">Once a week we pick the developments that matter, explain why, and point you to what to try.</p>
{newsletter_form("{{root}}", "news", "Subscribe free")}
<hr style="border:0;border-top:1px solid var(--line);margin:22px 0">
<h3>How the radar works</h3>
<p class="small muted">An automated job checks public RSS feeds from established AI publishers and labs several times a day. We show the headline, the source and the time, and link to the publisher. Inclusion is not endorsement.</p>
<h3>Want something covered?</h3>
<p class="small muted"><a href="{{{{root}}}}contact.html?topic=Press">Send us a tip or press release</a>.</p>
</div>
</aside>
</div></section>'''


def tools_page(tools, cats):
    counts = {c: sum(1 for t in tools if t["category"] == c) for c in cats}
    chips = f'<button class="chip" type="button" aria-pressed="true" data-cat="all">All<span>{len(tools)}</span></button>' + "".join(
        f'<button class="chip" type="button" aria-pressed="false" data-cat="{esc(c)}">{esc(c)}<span>{counts[c]}</span></button>' for c in cats)
    cards = "".join(tool_card(t, i) for i, t in enumerate(tools))
    return page_head("AI tools directory", f"{len(tools)} established AI tools across {len(cats)} categories. Search by task, filter by pricing model, then go straight to the official site.",
                     [("Home", "index.html"), ("AI tools", "")],
                     '<div class="btn-row"><a class="btn sm" href="{{root}}submit-tool.html">Submit a tool</a><a class="btn sm ghost" href="{{root}}advertise.html#featured">Get featured</a></div>') + f'''
<section class="section tight" style="padding-top:0"><div class="wrap">
<div class="toolbar">
<div class="search-row">
<label class="visually-hidden" for="tool-q">Search tools</label><input id="tool-q" type="search" placeholder="Search by name or task, e.g. transcribe, slides, code review">
<label class="visually-hidden" for="tool-price">Pricing</label><select id="tool-price"><option value="all">Any pricing</option><option>Free</option><option>Freemium</option><option>Paid</option><option>Open source</option></select>
<label class="visually-hidden" for="tool-sort">Sort</label><select id="tool-sort"><option value="default">Editor's order</option><option value="az">Name A to Z</option><option value="za">Name Z to A</option></select>
</div>
<div class="chips" id="tool-chips" aria-label="Filter by category">{chips}</div>
</div>
<p class="count-line" id="tool-count" aria-live="polite"></p>
<div class="tool-grid" id="tool-grid">{cards}</div>
<div class="empty" id="tool-empty" hidden>No tools match those filters. Clear the search or pick "All", or <a href="{{{{root}}}}submit-tool.html">suggest a tool we're missing</a>.</div>
<p class="small muted" style="margin-top:28px">Pricing models change often; confirm current plans on each vendor's site. Listings are editorial and free. Paid placements are always marked "Featured". Tool names are trademarks of their owners; we use generated initials instead of logos.</p>
</div></section>'''


def prompts_page(prompts, pcats):
    counts = {c: sum(1 for p in prompts if p["category"] == c) for c in pcats}
    chips = f'<button class="chip" type="button" aria-pressed="true" data-cat="all">All<span>{len(prompts)}</span></button>' + "".join(
        f'<button class="chip" type="button" aria-pressed="false" data-cat="{esc(c)}">{esc(c)}<span>{counts[c]}</span></button>' for c in pcats)
    cards = ""
    for i, p in enumerate(prompts):
        text = (p["title"] + " " + p["use"] + " " + p["category"] + " " + p["prompt"]).lower()
        cards += f'''<article class="prompt" data-cat="{esc(p["category"])}" data-name="{esc(p["title"].lower())}" data-order="{i}" data-text="{esc(text)}">
<span class="small muted">{esc(p["category"])}</span><h3>{esc(p["title"])}</h3><p class="use">{esc(p["use"])}</p>
<pre id="p{i}">{esc(p["prompt"])}</pre>
<div class="row"><button class="copy-btn" type="button" data-copy="p{i}">Copy prompt</button></div></article>'''
    return page_head("Prompt library", f"{len(prompts)} original, reusable prompts for business, writing, coding and creative work. Replace the [brackets] with your details and paste into any chat assistant.",
                     [("Home", "index.html"), ("Prompts", "")]) + f'''
<section class="section tight" style="padding-top:0"><div class="wrap">
<div class="toolbar"><div class="search-row"><label class="visually-hidden" for="prompt-q">Search prompts</label><input id="prompt-q" type="search" placeholder="Search prompts, e.g. cold email, lesson plan, refactor"></div>
<div class="chips" id="prompt-chips" aria-label="Filter by category">{chips}</div></div>
<p class="count-line" id="prompt-count" aria-live="polite"></p>
<div class="card-grid" id="prompt-grid">{cards}</div>
<div class="empty" id="prompt-empty" hidden>No prompts match. Try a broader word, or read the <a href="{{{{root}}}}guides/prompt-engineering-guide.html">prompt engineering guide</a> to write your own.</div>
<div class="inline-cta"><p>Want prompts built into your team's daily workflow?</p><a class="btn sm" href="{{{{root}}}}ai-services.html?goal=train">Get team training</a></div>
</div></section>'''


def videos_page():
    v0 = VIDEOS[2]
    grid = "".join(yt(*v) for v in VIDEOS if v[0] != v0[0])
    return page_head("AI video hub", "Hand-picked explainers from some of the clearest teachers of modern AI, each paired with an AiNew guide so you can go deeper.",
                     [("Home", "index.html"), ("Videos", "")],
                     '<div class="btn-row"><a class="btn sm" data-yt-channel hidden target="_blank" rel="noopener">Subscribe on YouTube</a></div>') + f'''
<section class="section tight" style="padding-top:0"><div class="wrap">
<div class="two-col" style="align-items:center;margin-bottom:40px">{yt(*v0)}
<div><h2>Start with the big picture</h2><p class="muted">If you watch one thing, make it this talk: how large language models are trained, what they're good at, and where they fail. Then read <a href="{{{{root}}}}guides/how-large-language-models-work.html">How large language models work</a> for the written version.</p></div></div>
<div class="video-grid">{grid}</div>
<p class="small muted" style="margin-top:28px">Videos play through YouTube's privacy-enhanced embedded player and remain the property of their creators. Nothing loads from YouTube until you press play. Creator? <a href="{{{{root}}}}contact.html?topic=Partnership">Suggest your video</a> or <a href="{{{{root}}}}advertise.html">sponsor a placement</a>.</p>
</div></section>'''


def guides_hub(guides, gcats):
    out = page_head("AI guides", "Plain-English, practitioner-written guides to understanding AI, prompting well, and putting it to work safely in your business and career.",
                    [("Home", "index.html"), ("Guides", "")])
    out += '<section class="section tight" style="padding-top:0"><div class="wrap">'
    for c in gcats:
        gs = [g for g in guides if g["category"] == c]
        if not gs:
            continue
        out += f'<h2 style="margin-top:28px">{esc(c)}</h2><div class="card-grid" style="margin-bottom:12px">'
        out += "".join(f'<a class="gcard" href="{g["slug"]}.html"><span class="cat">{esc(c)}</span><h3>{esc(g["title"])}</h3><p>{esc(g["summary"])}</p><span class="mins">{g["readMinutes"]} min read</span></a>' for g in gs)
        out += '</div>'
    out += '''<div class="inline-cta" style="margin-top:40px"><p>Not sure where to start? Take the 2-minute AI readiness check and get a personalised next step.</p><a class="btn sm" href="{{root}}readiness.html">Check my readiness</a></div></div></section>'''
    return out


def search_page():
    return page_head("Search AiNew", "Find guides, tools and prompts across the site.", [("Home", "index.html"), ("Search", "")]) + '''
<section class="section tight" style="padding-top:0"><div class="wrap" style="max-width:820px">
<div class="search-row"><label class="visually-hidden" for="search-q">Search</label><input id="search-q" type="search" placeholder="Search, e.g. agents, privacy, video, cold email" autofocus></div>
<p class="count-line" id="search-count" aria-live="polite" style="margin-top:14px"></p>
<ul class="results" id="search-results"></ul>
</div></section>'''
