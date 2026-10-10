# AiNew.com — Phase-wise build prompt

Use these prompts in order with an AI coding assistant to rebuild, extend or re-platform AiNew.com. Each phase has a goal, the prompt, and an acceptance check. Phases 1–8 are already implemented in this repository; phases 9–12 are the growth roadmap.

## The concept (why this idea wins)

**AiNew.com = "What's new in AI, sorted and explained."** A daily AI changelog (news radar) + AI tools directory + evergreen guides + prompt library, wrapped around a high-value B2B lead-generation funnel ("Get AI help for your business").

Revenue stack, ranked by expected value per visitor:

| Stream | Mechanism | Why it matters |
|---|---|---|
| B2B AI leads | Free AI plan request, readiness quiz, hire-AI-talent | One qualified SMB lead is worth more than thousands of ad impressions; sold/referred to vetted specialists or served directly |
| Sponsorships | Featured listings ($49), Spotlight ($199/mo), Newsletter ($149/issue), Guide partner ($299/mo), contest prize sponsors | AI vendors have large marketing budgets and buy placements on directories |
| Google AdSense | Auto ads on content pages | Baseline yield on every page view; tech/AI/business keywords carry above-average CPCs |
| Newsletter | Owned audience | Compounds all other streams; sold as sponsor inventory |
| Supporters | Pledges and payment links | Funds contests, talent and promotion |
| YouTube | Own-channel videos embedded on site | Second monetised surface once the channel is in the YouTube Partner Program |
| Domain/site sale | Top-of-page banner to web.works/contact | Exit option and partnership inbound |

## Phase 1 — Research and positioning
**Prompt:** "Visit 35+ leading sites in AI news (The Rundown, Superhuman, TLDR AI, The Neuron, The Batch, MIT Technology Review, VentureBeat, MarkTechPost), AI tool directories (There's An AI For That, Futurepedia, Toolify, FutureTools, TopAI.tools, Insidr, aitools.fyi, Product Hunt, Hugging Face Spaces, SaaSworthy) and AI learning/B2B sites (Learn Prompting, Prompting Guide, Elements of AI, Analytics Vidhya, CB Insights, YC directory, Kaggle). Extract features, forms, lead capture fields, monetisation, card anatomy and design patterns into a table, then list the patterns worth copying."
**Accept when:** a matrix of 35+ sites and a ranked pattern list exist.

## Phase 2 — Brand, design system and legal guardrails
**Prompt:** "Create a distinctive design system for AiNew.com: concept 'the AI changelog' where new items are marked with a highlighter. Tokens: paper #EDF0F7, ink #151A3A, ultramarine #2F3DF5, highlighter #FFE15A, line #D5DAE8; a deep-indigo dark mode. Type: Bricolage Grotesque (UI/headlines) and Newsreader (long reading). Avoid third-party logos (use generated initials). Write a trademark & copyright disclosure stating 'AiNew' refers only to this domain and implies no affiliation with any similarly named mark."
**Accept when:** CSS tokens, light/dark themes, logo wordmark and legal.html exist.

## Phase 3 — Static architecture for GitHub Pages (free plan)
**Prompt:** "Build a dependency-free static site generator in Python (`_build/build.py`) that renders shared layout (head, promo strip, header, footer, cookie notice) around page bodies and Markdown-like guide fragments in `_src/`. Output plain HTML at the repo root with relative links so it works on both `username.github.io/repo/` and a custom domain. Every page: the AdSense script `ca-pub-6620975821265271` in `<head>`, the `google-adsense-account` meta tag, canonical URL, Open Graph, JSON-LD, and a top strip reading 'Contact, if you are interested in this website/domain name/Sponsorship/Advertisement/Partnership' linking to https://web.works/contact."
**Accept when:** `python3 _build/build.py` regenerates the whole site; ads.txt, robots.txt, sitemap.xml and manifest are produced.

## Phase 4 — Content that passes AdSense review
**Prompt:** "Write 14 original 1,400–2,000-word evergreen guides (generative AI basics, how LLMs work, glossary, prompt engineering, AI agents, RAG, AI for small business, automation workflows, choosing a model, privacy & security checklist, image/video generation, copyright basics, making money with AI, career roadmap). Each has key takeaways, a TOC, at least one table/checklist, internal links and an FAQ with FAQPage schema. No invented statistics, no copied text. Also build: an 89-tool directory with search/category/pricing filters, a 72-prompt library with copy buttons, and About, Contact, Editorial policy, Privacy (AdSense cookie disclosures and opt-out links), Terms, Disclaimer pages."
**Accept when:** ~30k words of original content, all policy pages live, no thin pages, no broken links.

## Phase 5 — Lead generation engine
**Prompt:** "Create a dedicated `ai-services.html` lead funnel: use-case cards that preselect the goal, a 3-step 'how it works', an ROI calculator, a 4-step progressive form (goal → organisation → budget/timeline → contact) with a progress bar, consent checkbox and FAQ. Add `readiness.html`, a 10-question AI readiness quiz that shows an instant score and band, then offers a full report in exchange for name/email/company/role. Repeat CTAs in header, homepage band, mid-article and TOC."
**Accept when:** both funnels submit successfully and redirect to thank-you.html.

## Phase 6 — Forms with a hidden inbox
**Prompt:** "Route every form (newsletter, AI plan, readiness report, advertising, tool submission, contest registration, support pledge, talent application, contact) through FormSubmit's AJAX endpoint. The destination address must never appear in HTML, JS strings, mailto links or the repo: store it encoded in `assets/js/config.js`, decode only at send time, and build any 'Email us' link on click. Add honeypot spam protection. Support a FormSubmit alias string to replace the encoded address entirely."
**Accept when:** a repo-wide search for the address returns nothing and test submissions arrive.

## Phase 7 — Community and revenue pages
**Prompt:** "Build: `advertise.html` (launch pricing tiers, contest sponsorship, website/domain enquiry, enquiry form); `submit-tool.html`; `contests.html` (Build Challenge with judging rubric, registration form, compliant no-purchase-necessary rules summary, prize pool funded by sponsors/supporters); `support.html` (tiers, fund designation — operations, guides, promotion, talent fund, prize pool — pledge form and config-driven payment buttons for Stripe/PayPal/Ko-fi/Buy Me a Coffee/GitHub Sponsors); `careers.html` (paid freelance roles + talent network application); `newsletter.html`; `videos.html` (click-to-load privacy-enhanced YouTube embeds)."
**Accept when:** every page has a working form or CTA and honest disclosures.

## Phase 8 — Automation and publishing
**Prompt:** "Add a GitHub Actions workflow that every 4 hours fetches public RSS feeds from established AI publishers, stores headline/link/source/date only in `data/news.json`, commits it, and publishes the site to the `gh-pages` branch for GitHub Pages. Add client-side site search over guides, tools and prompts."
**Accept when:** the radar shows fresh headlines on the live site without manual work.

## Phase 9 — Launch checklist (owner actions)
1. Point AiNew.com DNS to GitHub Pages and set the custom domain (see README).
2. Add AiNew.com in AdSense, confirm ads.txt is reachable at https://ainew.com/ads.txt, request review.
3. In AdSense → Privacy & messaging, enable Google's certified CMP for EEA/UK visitors.
4. Submit the sitemap in Google Search Console.
5. Send one test form submission and click FormSubmit's activation email.
6. Review and personally edit each guide; confirm prices, SLAs and prize amounts.

## Phase 10 — Traffic growth
**Prompt:** "Create programmatic but genuinely useful pages: one page per tool category with a buying guide; 'X vs Y' comparison pages for the 20 most-searched tool pairs; a weekly 'What's new in AI' recap archive written from the radar. Add internal-link hubs and update the sitemap."

## Phase 11 — Monetisation depth
**Prompt:** "Add affiliate links where programmes exist (marked rel="sponsored"), a paid tool-submission checkout via Stripe Payment Links, a sponsor dashboard page with a media kit PDF, and manual AdSense units (in-article and multiplex) once AdSense approves the site."

## Phase 12 — Scale
**Prompt:** "Migrate the newsletter to a dedicated ESP, add a lightweight CMS (Decap CMS on GitHub) for guides and tools, add user-submitted reviews with moderation, and add a jobs board for AI roles with paid postings."
