"""Refresh data/news.json from public RSS/Atom feeds of established AI publishers.

Stores only headline, link, source and date (no article text), credited to the publisher.
Runs in GitHub Actions on a schedule. Standard library only.
"""
import json, re, html, datetime, urllib.request
from email.utils import parsedate_to_datetime
from pathlib import Path
import xml.etree.ElementTree as ET

FEEDS = [
    ("MIT Technology Review", "https://www.technologyreview.com/topic/artificial-intelligence/feed"),
    ("TechCrunch", "https://techcrunch.com/category/artificial-intelligence/feed/"),
    ("VentureBeat", "https://venturebeat.com/category/ai/feed/"),
    ("The Verge", "https://www.theverge.com/rss/ai-artificial-intelligence/index.xml"),
    ("Ars Technica", "https://arstechnica.com/ai/feed/"),
    ("Google AI Blog", "https://blog.google/technology/ai/rss/"),
    ("OpenAI", "https://openai.com/news/rss.xml"),
    ("Hugging Face", "https://huggingface.co/blog/feed.xml"),
    ("AI News", "https://www.artificialintelligence-news.com/feed/"),
    ("MarkTechPost", "https://www.marktechpost.com/feed/"),
]
PER_FEED = 12
MAX_ITEMS = 120
OUT = Path(__file__).resolve().parent.parent / "data" / "news.json"
UA = "Mozilla/5.0 (compatible; AiNewRadar/1.0; +https://ainew.com/editorial-policy.html)"


def parse_date(s):
    if not s:
        return None
    s = s.strip()
    try:
        d = parsedate_to_datetime(s)
    except Exception:
        try:
            d = datetime.datetime.fromisoformat(s.replace("Z", "+00:00"))
        except Exception:
            return None
    if d.tzinfo is None:
        d = d.replace(tzinfo=datetime.timezone.utc)
    return d.astimezone(datetime.timezone.utc)


def clean(t):
    t = html.unescape(re.sub(r"<[^>]+>", "", t or "")).strip()
    return re.sub(r"\s+", " ", t)


def local(tag):
    return tag.rsplit("}", 1)[-1]


def fetch(source, url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml"})
    with urllib.request.urlopen(req, timeout=20) as r:
        root = ET.fromstring(r.read())
    items = []
    for el in root.iter():
        if local(el.tag) not in ("item", "entry"):
            continue
        title = link = date = None
        for c in el:
            n = local(c.tag)
            if n == "title":
                title = clean(c.text)
            elif n == "link":
                link = (c.get("href") if c.get("href") and c.get("rel", "alternate") == "alternate" else None) or (c.text or "").strip() or link
            elif n in ("pubDate", "published", "updated", "date") and not date:
                date = parse_date(c.text)
        if title and link and link.startswith("http"):
            items.append({"title": title[:220], "link": link, "source": source,
                          "date": (date or datetime.datetime.now(datetime.timezone.utc)).isoformat()})
        if len(items) >= PER_FEED:
            break
    return items


def main():
    now = datetime.datetime.now(datetime.timezone.utc)
    try:
        old = json.loads(OUT.read_text())
    except Exception:
        old = {"items": []}
    allitems, ok = [], 0
    for source, url in FEEDS:
        try:
            got = fetch(source, url)
            allitems += got
            ok += 1
            print(f"ok   {source}: {len(got)}")
        except Exception as e:
            print(f"fail {source}: {e}")
            allitems += [i for i in old.get("items", []) if i.get("source") == source]
    seen, uniq = set(), []
    cutoff = now - datetime.timedelta(days=21)
    for i in sorted(allitems, key=lambda x: x["date"], reverse=True):
        key = i["link"].split("?")[0]
        if key in seen or parse_date(i["date"]) < cutoff:
            continue
        seen.add(key)
        uniq.append(i)
    if ok == 0:
        print("No feeds reachable; keeping previous file.")
        return
    if not uniq and old.get("items"):
        print("No fresh items; keeping previous file.")
        return
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({"updated": now.isoformat(), "feeds_ok": ok, "items": uniq[:MAX_ITEMS]}, ensure_ascii=False, indent=1))
    print(f"Wrote {min(len(uniq), MAX_ITEMS)} items from {ok} feeds")


if __name__ == "__main__":
    main()
