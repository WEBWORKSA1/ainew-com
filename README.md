# AiNew.com

What's new in AI, sorted and explained. A static website hosted free on GitHub Pages: AI news radar, AI tools directory, in-depth guides, prompt library, videos, B2B lead generation, contests, supporter pledges and talent network.

## Structure
- Root `*.html`, `guides/`, `assets/`, `data/` — the published site (generated).
- `_src/guides/*.html` — guide sources (first line is a JSON META comment).
- `_src/data/tools.json`, `_src/data/prompts.json` — directory and prompt library data.
- `_build/` — the Python generator. Run `python3 _build/build.py` (Python 3.12+) after editing sources.
- `_scripts/fetch_news.py` + `_docs/github-workflow-news-radar.yml` — optional automation that rebuilds the site, refreshes the news radar every 4 hours and publishes to `gh-pages`.
- `assets/js/config.js` — payment links, YouTube channel and form routing settings.
- `_docs/BUILD-PROMPT.md` — the phase-wise build prompt and roadmap.

Folders starting with `_` are not published by GitHub Pages.

## Hosting
GitHub Pages serves the `gh-pages` branch, which mirrors `main`.

### Turn on automation (one-time, 1 minute)
GitHub only lets the repository owner add workflow files. In the repo click **Add file → Create new file**, name it `.github/workflows/news-radar.yml`, paste the contents of `_docs/github-workflow-news-radar.yml`, and commit. From then on every push to `main` rebuilds the site, generates the share images and icons, refreshes the news radar every 4 hours and republishes `gh-pages`. Until then, the news radar reads publisher feeds live in the visitor's browser.

### Custom domain (required for AdSense)
1. At your DNS provider for ainew.com add:
   - `A` records for `@`: 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153
   - `CNAME` for `www`: `webworksa1.github.io`
2. Repository Settings → Pages → Custom domain: `ainew.com`, then tick "Enforce HTTPS".
3. Confirm https://ainew.com/ads.txt loads, then add the site in AdSense.

## Forms
All forms post through FormSubmit. The destination inbox is stored encoded in `assets/js/config.js` and is never written into the page. The first submission triggers a one-time activation email from FormSubmit; click it to start receiving submissions. FormSubmit's activation email also offers a random alias string; paste it into `formAlias` in `config.js` to stop using the encoded address entirely.

## Payments
Add Stripe Payment Links, PayPal.me, Ko-fi, Buy Me a Coffee or GitHub Sponsors URLs to `pay` in `config.js`. Buttons appear on the Support page automatically. Until then, the pledge form collects commitments.
