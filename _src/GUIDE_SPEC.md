# Guide fragment spec (AiNew.com)

Each guide is ONE file: `/home/claude/ainew/_src/guides/<slug>.html`. It is an HTML *fragment* (no <html>, <head>, <body>, no CSS, no scripts). The build script wraps it in the site layout.

## Line 1: metadata comment (valid JSON, one line)
<!--META {"title":"...","description":"...","category":"...","readMinutes":9,"summary":"..."} -->

- title: 45–65 chars, plain, specific, no clickbait, no year.
- description: 140–160 chars, for the meta description.
- category: exactly one of: Foundations, Prompting, Business, Build, Creative, Careers, Safety
- readMinutes: integer = word count / 220, rounded.
- summary: one sentence (max 22 words) for cards.

## Body rules
- Allowed tags only: h2, h3, p, ul, ol, li, strong, em, a, blockquote, table, thead, tbody, tr, th, td, code, pre, aside, section, details, summary, dl, dt, dd.
- Every <h2> MUST have a kebab-case id (used for the table of contents). Do not use <h1> (layout adds it).
- Start with an intro of 2–3 short paragraphs, then:
  <aside class="takeaways"><h2 id="key-takeaways">Key takeaways</h2><ul><li>…</li></ul></aside>
- Optional callouts: <aside class="note"><p><strong>Tip:</strong> …</p></aside> (or Warning:, Example:).
- Use at least one real structural aid where it genuinely helps: a comparison table, a checklist, or a numbered step sequence.
- End with a FAQ section exactly like this (3–5 questions):
  <section class="faq"><h2 id="faq">Frequently asked questions</h2>
  <details><summary>Question?</summary><p>Answer.</p></details>
  …</section>
- Internal links: other guides are siblings, link as `slug.html` (e.g. `prompt-engineering-guide.html`). Link to site pages with `../tools.html` (AI tools directory), `../prompts.html` (prompt library), `../ai-services.html` (get expert AI help for your business), `../readiness.html` (free AI readiness score quiz). Use 3–6 internal links naturally in the text.
- External links: only to stable, authoritative homepages/docs you are certain exist (e.g. official product homepages, nist.gov, oecd.ai). Max 4. Plain `<a href>`; the build adds rel attributes.

## All guide slugs on the site (for cross-linking)
what-is-generative-ai, how-large-language-models-work, ai-glossary, prompt-engineering-guide, ai-agents-explained, rag-explained, ai-for-small-business, ai-automation-workflows, choosing-an-ai-model, ai-privacy-security-checklist, ai-image-video-generation, ai-content-copyright-basics, make-money-with-ai, ai-career-skills-roadmap

## Content rules (Google AdSense quality bar — this decides approval)
- 100% original writing. Never copy or closely paraphrase any source. No quotes from articles/books.
- 1,400–2,000 words of genuinely useful, specific, practical content (glossary may be longer). Concrete examples, worked examples, decision criteria. No filler, no "In today's fast-paced world".
- Evergreen and accurate. Knowledge is current to mid-2026; avoid claims about specific prices, exact model version numbers, benchmark scores, market-size statistics, or dated "latest" news. If you name products, name only long-established ones and describe them generically (e.g. "chat assistants such as ChatGPT, Claude and Gemini").
- No invented statistics, studies, quotes, people, or testimonials. If you'd need a number you can't stand behind, explain the principle instead.
- Not legal, medical or financial advice; where relevant say so in one sentence and recommend a qualified professional.
- Family-safe, non-sensational. Second person ("you"), plain sentence-case headings, active voice.
- Write like an experienced practitioner explaining to a smart non-expert.
