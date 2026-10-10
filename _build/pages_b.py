"""Page bodies: lead generation, readiness quiz, advertising, contests, support, careers, newsletter, contact."""
from layout import esc, newsletter_form, page_head, PROMO_URL

HP = '<input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">'
CONSENT = ('<div class="field"><label class="check"><input type="checkbox" name="consent" value="Agreed to be contacted" required>'
           '<span>I agree to be contacted about this request. AiNew will not sell my details. See the <a href="{{root}}privacy.html">privacy policy</a>.</span></label></div>')


def opt(name, value, label, req=True):
    return f'<label class="opt"><input type="radio" name="{name}" value="{esc(value)}"{" required" if req else ""}><span>{esc(label)}</span></label>'


def sel(name, label, options, req=True, fid=None):
    fid = fid or name
    o = '<option value="">Choose one</option>' + "".join(f'<option>{esc(x)}</option>' for x in options)
    return f'<div class="field"><label for="{fid}">{label}</label><select id="{fid}" name="{name}"{" required" if req else ""}>{o}</select></div>'


def inp(name, label, typ="text", req=True, ph="", fid=None, ac=""):
    fid = fid or name
    a = f' autocomplete="{ac}"' if ac else ""
    return f'<div class="field"><label for="{fid}">{label}{"" if req else " <span class=\"muted\">(optional)</span>"}</label><input id="{fid}" name="{name}" type="{typ}" placeholder="{esc(ph)}"{" required" if req else ""}{a}></div>'


def area(name, label, req=False, ph="", fid=None):
    fid = fid or name
    return f'<div class="field"><label for="{fid}">{label}{"" if req else " <span class=\"muted\">(optional)</span>"}</label><textarea id="{fid}" name="{name}" placeholder="{esc(ph)}"{" required" if req else ""}></textarea></div>'


INDUSTRIES = ["Retail & e-commerce", "Professional services", "Healthcare", "Real estate", "Finance & insurance", "Education",
              "Hospitality & travel", "Manufacturing", "Construction & trades", "Marketing & media", "Software & IT", "Non-profit", "Other"]

USECASES = [
    ("support", "Customer support that never sleeps", "An assistant trained on your policies answers routine questions instantly and hands tricky ones to a person."),
    ("leads", "Faster lead follow-up", "Every enquiry gets a tailored reply in minutes, is scored, and lands in your CRM with notes."),
    ("content", "Content at a steady pace", "Turn one idea into posts, emails and pages in your brand voice, with a human review step."),
    ("documents", "Paperwork into data", "Extract fields from invoices, forms and contracts into spreadsheets or your accounting tool."),
    ("assistant", "An internal knowledge assistant", "Staff ask questions in plain English and get answers grounded in your own documents."),
    ("talent", "Hire AI talent", "Get matched with vetted freelancers and specialists who build and maintain AI workflows."),
    ("train", "Train your team", "Hands-on sessions so everyone uses AI safely and well in their daily work."),
]


def ai_services():
    goals = [("support", "Automate customer support"), ("leads", "Get and qualify more leads"), ("content", "Create content faster"),
             ("documents", "Process documents and data"), ("assistant", "Build an internal AI assistant"), ("talent", "Hire AI talent"),
             ("train", "Train my team"), ("other", "Something else")]
    cards = "".join(f'<div class="usecase"><h3>{esc(t)}</h3><p>{esc(d)}</p><a href="?goal={k}#plan">Start with this</a></div>' for k, t, d in USECASES)
    return page_head("Put AI to work in your business",
                     "Tell us the job you want done faster. We'll reply within two business days with a free, written starting plan, and introduce a vetted specialist if you want help building it.",
                     [("Home", "index.html"), ("Get AI help", "")],
                     '<div class="btn-row"><a class="btn" href="#plan">Get my free AI plan</a><a class="btn ghost" href="{{root}}readiness.html">Take the 2-minute readiness check</a></div>') + f'''
<section class="section tight"><div class="wrap">
<div class="sec-head"><div><h2>Where AI pays off first</h2><p>The projects that tend to return time and money fastest for small and mid-sized teams.</p></div></div>
<div class="usecases">{cards}</div></div></section>

<section class="section tight"><div class="wrap">
<h2>How it works</h2>
<ol class="steps-list" style="margin-top:18px">
<li><h3>Tell us the goal</h3><p>Four short steps, about two minutes. No call needed to start.</p></li>
<li><h3>Get a written plan</h3><p>What to automate first, which tools fit, rough effort and the risks to manage.</p></li>
<li><h3>Build it your way</h3><p>Do it in-house with the plan, or get matched with a vetted specialist. No obligation either way.</p></li>
</ol></div></section>

<section class="section tight"><div class="wrap">
<div class="panel" id="roi"><div class="roi">
<div><h2>What could AI save you?</h2><p class="muted">A rough yearly estimate: hours saved times what those hours cost, minus tool spend. Adjust the sliders to match your team.</p>
<div class="field"><label for="roi-people">People doing the task: <output for="roi-people"></output></label><input id="roi-people" type="range" min="1" max="50" value="4"></div>
<div class="field"><label for="roi-hours">Hours a week each could save: <output for="roi-hours"></output></label><input id="roi-hours" type="range" min="1" max="20" value="4"></div>
<div class="field"><label for="roi-rate">Loaded cost per hour ($): <output for="roi-rate"></output></label><input id="roi-rate" type="range" min="10" max="200" step="5" value="40"></div>
<div class="field"><label for="roi-cost">Monthly AI tool cost ($): <output for="roi-cost"></output></label><input id="roi-cost" type="range" min="0" max="2000" step="20" value="200"></div>
</div>
<div><p class="muted" style="margin:0">Estimated net value per year</p><output data-out="net" aria-live="polite">$0</output>
<p class="muted"><span data-out="hrs">0</span> hours a year freed for higher-value work (48 working weeks).</p>
<a class="btn" href="#plan">Turn this into a plan</a>
<p class="small muted" style="margin-top:12px">Illustrative only. Real results depend on the task, data quality and adoption.</p></div>
</div></div></div></section>

<section class="section tight" id="plan"><div class="wrap two-col">
<div>
<h2>Get your free AI plan</h2>
<p class="muted">Four quick steps. Your answers go only to the AiNew team and the specialist you choose to work with.</p>
<ul class="kv" style="margin-top:20px">
<li>Free written plan, no sales call required</li>
<li>Reply within two business days</li>
<li>Vetted specialists, matched to your industry and budget</li>
<li>Your details are never sold or shared without permission</li>
</ul>
<p class="small muted" style="margin-top:20px">Prefer to talk first? <a href="{{{{root}}}}contact.html?topic=AI%20services">Send a message</a>.</p>
</div>
<form class="form-panel stepper" data-form="lead-ai-plan" data-subject="NEW LEAD: AI plan request" data-next="1" novalidate>
{HP}
<div class="progress" aria-hidden="true"><span></span></div>
<fieldset class="step" style="border:0;padding:0;margin:0"><legend class="step-label">Step 1 of 4</legend>
<h3>What do you want AI to help with?</h3>
<div class="options">{"".join(opt("goal", k, t) for k, t in goals)}</div>
<div class="step-nav"><span></span><button class="btn" type="button" data-next-step>Continue</button></div></fieldset>

<fieldset class="step" style="border:0;padding:0;margin:0"><legend class="step-label">Step 2 of 4</legend>
<h3>About your organisation</h3>
{sel("industry", "Industry", INDUSTRIES)}
{sel("company_size", "Team size", ["Just me", "2–10", "11–50", "51–200", "201–1,000", "1,000+"])}
{sel("current_ai_use", "How do you use AI today?", ["Not yet", "A few people experiment with chat tools", "We pay for some AI tools", "AI runs in at least one live workflow"])}
<div class="step-nav"><button class="btn ghost" type="button" data-prev-step>Back</button><button class="btn" type="button" data-next-step>Continue</button></div></fieldset>

<fieldset class="step" style="border:0;padding:0;margin:0"><legend class="step-label">Step 3 of 4</legend>
<h3>Scope and timing</h3>
{sel("budget", "Budget for a first project", ["Under $1,000", "$1,000–$5,000", "$5,000–$15,000", "$15,000–$50,000", "$50,000+", "Not sure yet"])}
{sel("timeline", "When do you want to start?", ["As soon as possible", "Within 1–3 months", "In 3–6 months", "Just exploring"])}
{area("details", "Describe the task or problem", False, "e.g. We get 200 support emails a week, mostly about order status and returns.")}
<div class="step-nav"><button class="btn ghost" type="button" data-prev-step>Back</button><button class="btn" type="button" data-next-step>Continue</button></div></fieldset>

<fieldset class="step" style="border:0;padding:0;margin:0"><legend class="step-label">Step 4 of 4</legend>
<h3>Where should we send your plan?</h3>
<div class="grid-2">{inp("name", "Your name", ac="name")}{inp("email", "Work email", "email", ac="email")}</div>
<div class="grid-2">{inp("company", "Company", ac="organization")}{inp("website", "Website", "url", False, "https://", ac="url")}</div>
<div class="grid-2">{inp("phone", "Phone", "tel", False, ac="tel")}{inp("country", "Country", ac="country-name")}</div>
{CONSENT}
<div class="step-nav"><button class="btn ghost" type="button" data-prev-step>Back</button><button class="btn mark-btn" type="submit">Get my free AI plan</button></div>
<p class="form-msg" role="status"></p></fieldset>
</form>
</div></section>

<section class="section tight"><div class="wrap" style="max-width:820px">
<h2>Common questions</h2>
<div class="faq-list">
<details><summary>Is the plan really free?</summary><p>Yes. The written starting plan costs nothing and carries no obligation. If you later hire a specialist through us, you agree scope and price with them before any work starts.</p></details>
<details><summary>Who are the specialists?</summary><p>Independent consultants, developers and automation builders who have applied to our talent network and shown relevant past work. We match on industry, task and budget.</p></details>
<details><summary>What happens to my data?</summary><p>Your answers are used only to prepare your plan and, with your permission, to introduce a specialist. We never sell lead data. Read the <a href="{{{{root}}}}privacy.html">privacy policy</a>.</p></details>
<details><summary>We're very early. Is this still useful?</summary><p>Yes. Many plans start with a usage policy and two low-risk pilots. The <a href="{{{{root}}}}guides/ai-for-small-business.html">small business guide</a> is a good primer while you wait.</p></details>
</div></div></section>'''


QUIZ = [
    ("Where does most of your business information live?", ["Mostly on paper or in people's heads", "Scattered across email and personal files", "In shared drives and a few core apps", "In organised systems with clear owners"]),
    ("How much of your team's week goes on repetitive tasks (copying, sorting, answering the same questions)?", ["Hardly any", "A little", "A noticeable amount", "A lot, and we know which tasks"]),
    ("How do people use AI tools at work today?", ["Not at all", "A few people, on their own", "Several people, informally", "Shared tools with agreed guidelines"]),
    ("Do you have rules on what data can be put into AI tools?", ["No", "Informal, unwritten", "Partly written down", "A clear written policy"]),
    ("Can you measure the tasks you'd want to improve (volume, time, cost)?", ["No", "Rough guesses only", "For some tasks", "Yes, we track them"]),
    ("Who would own an AI project?", ["Nobody obvious", "Whoever has spare time", "A named person, part-time", "A named owner with time set aside"]),
    ("How comfortable is your team with trying new software?", ["Resistant", "Cautious", "Open", "Keen"]),
    ("How do your main apps connect (CRM, email, accounting, helpdesk)?", ["They don't", "Manual exports", "Some integrations", "Well connected or API-ready"]),
    ("Is budget available for a small pilot?", ["No", "Unsure", "A small amount", "Yes, approved"]),
    ("How would you check that AI output is right before it reaches customers?", ["We wouldn't", "Ad hoc", "Spot checks", "A defined review step"]),
]


def readiness():
    qs = ""
    for i, (q, opts) in enumerate(QUIZ):
        qs += f'<fieldset class="q" style="border:0;padding:0;margin:0 0 22px"><legend style="font-weight:650;margin-bottom:10px">{i + 1}. {esc(q)}</legend><div class="options">'
        qs += "".join(f'<label class="opt"><input type="radio" name="q{i}" value="{v}" required><span>{esc(o)}</span></label>' for v, o in enumerate(opts))
        qs += '</div></fieldset>'
    return page_head("How AI-ready is your business?",
                     "Ten quick questions, about two minutes. Get an instant readiness score and a recommended next step. No email needed to see your result.",
                     [("Home", "index.html"), ("AI readiness score", "")]) + f'''
<section class="section tight" style="padding-top:0"><div class="wrap" style="max-width:900px">
<form id="quiz" class="form-panel" novalidate>{qs}<button class="btn mark-btn" type="submit">See my score</button></form>
<div id="quiz-result" hidden style="margin-top:28px">
<div class="panel two-col" style="align-items:center">
<div><div class="score-ring" id="score-ring"><b id="score-num">0</b></div><h2 id="score-band"></h2><p id="score-advice" class="muted"></p></div>
<form class="form-panel" data-form="lead-readiness" data-subject="NEW LEAD: AI readiness report" data-next="1" style="padding:0;border:0">
{HP}<input type="hidden" name="readiness_score"><input type="hidden" name="readiness_band">
<h3>Get your full report</h3><p class="small muted">A written breakdown of your score, with the three moves that would raise it fastest.</p>
{inp("name", "Name", fid="r-name", ac="name")}{inp("email", "Work email", "email", fid="r-email", ac="email")}
<div class="grid-2">{inp("company", "Company", fid="r-company", ac="organization")}{inp("role", "Your role", fid="r-role", ac="organization-title")}</div>
{CONSENT.replace('name="consent"', 'name="consent" id="r-consent"')}
<button class="btn" type="submit">Email me my report</button><p class="form-msg" role="status"></p>
</form></div>
<div class="inline-cta"><p>Ready to act on it? Get a free, written AI plan for your business.</p><a class="btn sm" href="{{{{root}}}}ai-services.html#plan">Get my free AI plan</a></div>
</div>
</div></section>'''


def advertise():
    tiers = [
        ("Featured listing", "$49", "one-time, 30 days", ["Featured badge in the tools directory", "Top of its category", "Included in site search"], "featured", False),
        ("Spotlight sponsor", "$199", "per month", ["Homepage spotlight placement", "Featured listing included", "One newsletter mention", "Clearly labelled sponsor content"], "spotlight", True),
        ("Newsletter sponsor", "$149", "per issue", ["Top-of-issue sponsor slot", "Up to 60 words plus link", "Sent to every subscriber"], "newsletter", False),
        ("Guide partner", "$299", "per month", ["\"Presented by\" credit on one guide", "Contextual, labelled mention", "No change to editorial content"], "guide", False),
    ]
    tcards = "".join(f'''<div class="tier{' pick' if pick else ''}"><h3>{esc(n)}</h3><div class="price">{p} <small>{esc(per)}</small></div><ul>{"".join(f"<li>{esc(x)}</li>" for x in feats)}</ul><a class="btn{'' if pick else ' ghost'}" href="#ad-form" data-tier="{k}">Request {esc(n.lower())}</a></div>''' for n, p, per, feats, k, pick in tiers)
    interests = ["Featured listing", "Spotlight sponsor", "Newsletter sponsor", "Guide partner", "Contest prize sponsor", "Display advertising", "Content partnership", "Website or domain acquisition"]
    checks = "".join(f'<label class="check" style="margin-bottom:8px"><input type="checkbox" name="interest" value="{esc(x)}"><span>{esc(x)}</span></label>' for x in interests)
    return page_head("Advertise and partner with AiNew",
                     "Reach founders, operators and builders while they're choosing AI tools. Every paid placement is clearly labelled, and editorial content is never for sale.",
                     [("Home", "index.html"), ("Advertise", "")]) + f'''
<section class="section tight" style="padding-top:0" id="featured"><div class="wrap">
<div class="sec-head"><div><h2>Launch partner pricing</h2><p>Simple, transparent packages. Custom bundles available.</p></div></div>
<div class="tiers">{tcards}</div>
</div></section>

<section class="section tight" id="sponsor-contest"><div class="wrap split">
<div class="panel"><h2>Sponsor a contest prize</h2><p class="muted">Put your brand behind the AiNew Build Challenge. Sponsors are named on the contest page, in announcements and in the winners' feature, and can set a themed prize (for example "Best workflow built with your product").</p><a class="btn" href="#ad-form">Talk about contest sponsorship</a></div>
<div class="panel inked"><h2>Interested in this website or domain?</h2><p>For acquisition of AiNew.com, the domain name, or a strategic partnership, contact the owner directly.</p><a class="btn" href="{PROMO_URL}" target="_blank" rel="noopener">Contact the owner</a></div>
</div></section>

<section class="section tight" id="ad-form"><div class="wrap two-col">
<div><h2>Start a conversation</h2><p class="muted">Tell us what you want to promote and we'll reply with availability, an audience summary and next steps.</p>
<ul class="kv"><li>Placements labelled "Featured", "Sponsor" or "Presented by"</li><li>No paid reviews and no changes to editorial ratings</li><li>We decline products that break Google's publisher policies or our standards</li></ul></div>
<form class="form-panel" data-form="lead-advertising" data-subject="NEW LEAD: Advertising / sponsorship" data-next="1">
{HP}
<div class="grid-2">{inp("name", "Name", fid="a-name", ac="name")}{inp("email", "Work email", "email", fid="a-email", ac="email")}</div>
<div class="grid-2">{inp("company", "Company", fid="a-company", ac="organization")}{inp("website", "Website", "url", True, "https://", fid="a-website", ac="url")}</div>
<div class="field"><span style="font-weight:600;font-size:.92rem;display:block;margin-bottom:8px">I'm interested in</span>{checks}</div>
{sel("budget", "Monthly budget", ["Under $250", "$250–$1,000", "$1,000–$5,000", "$5,000+", "Not sure yet"], fid="a-budget")}
{area("message", "Anything else we should know?", False, "Launch dates, audience, goals…", fid="a-message")}
{CONSENT.replace('name="consent"', 'name="consent" id="a-consent"')}
<button class="btn" type="submit">Send enquiry</button><p class="form-msg" role="status"></p>
</form></div></section>'''


def submit_tool(cats):
    return page_head("Submit an AI tool", "Listings are free and editorial. We review every submission for quality, safety and a working product before it's added.",
                     [("Home", "index.html"), ("AI tools", "tools.html"), ("Submit a tool", "")]) + f'''
<section class="section tight" style="padding-top:0"><div class="wrap two-col">
<div><h2>What we look for</h2>
<ul class="kv"><li>A live, working product with a public website</li><li>A clear description of what it does and who it's for</li><li>Transparent pricing and a privacy policy</li><li>Nothing deceptive, unsafe or against Google's publisher policies</li></ul>
<div class="panel" style="margin-top:24px"><h3>Want to stand out?</h3><p class="small muted">Featured listings appear at the top of their category with a "Featured" badge for 30 days.</p><a class="btn sm" href="advertise.html#featured">See featured options</a></div></div>
<form class="form-panel" data-form="tool-submission" data-subject="Tool submission" data-next="1">
{HP}
<div class="grid-2">{inp("tool_name", "Tool name")}{inp("tool_url", "Official website", "url", True, "https://")}</div>
<div class="grid-2">{sel("category", "Category", cats)}{sel("pricing", "Pricing model", ["Free", "Freemium", "Paid", "Open source"])}</div>
{area("description", "What does it do? (one or two sentences)", True, "Plain description, no superlatives.")}
<div class="grid-2">{inp("name", "Your name", ac="name")}{inp("email", "Email", "email", ac="email")}</div>
{sel("relationship", "Your relationship to the tool", ["Founder or employee", "Agency or reseller", "User recommending it"])}
<div class="field"><label class="check"><input type="checkbox" name="featured_interest" value="Yes, send featured options"><span>Send me featured listing options</span></label></div>
{CONSENT}
<button class="btn" type="submit">Submit tool for review</button><p class="form-msg" role="status"></p>
</form></div></section>'''


def contests():
    return page_head("AiNew Build Challenge", "A contest for practical AI. Build a workflow that saves a real small business at least five hours a week, document it, and compete for the prize pool.",
                     [("Home", "index.html"), ("Contests", "")],
                     '<div class="btn-row"><a class="btn" href="#register">Register for the brief</a><a class="btn ghost" href="{{root}}advertise.html#sponsor-contest">Sponsor a prize</a></div>') + f'''
<section class="section tight" style="padding-top:0"><div class="wrap split">
<div class="panel"><h2>Season 1 at a glance</h2>
<ul class="kv"><li><strong>Status:</strong>&nbsp;registration open, entries open soon</li><li><strong>Theme:</strong>&nbsp;AI workflows for small businesses</li><li><strong>Who can enter:</strong>&nbsp;individuals 18+ and small teams, worldwide where permitted</li><li><strong>Cost to enter:</strong>&nbsp;free, no purchase necessary</li><li><strong>Prize pool:</strong>&nbsp;funded by sponsors and supporters; confirmed amounts are published here before entries open</li></ul></div>
<div class="panel inked"><h2>Grow the prize pool</h2><p>Supporters and sponsors fund the prizes directly. Back the next winner, or put your brand on a themed award.</p><div class="btn-row"><a class="btn" href="{{{{root}}}}support.html?fund=Contest%20prize%20pool">Add to the prize pool</a></div></div>
</div></section>

<section class="section tight"><div class="wrap">
<h2>How it runs</h2>
<ol class="steps-list" style="margin-top:18px">
<li><h3>Register</h3><p>Get the full brief, judging rubric and key dates by email.</p></li>
<li><h3>Build</h3><p>Use any tools. Solve a real, repeatable task for a real or realistic business.</p></li>
<li><h3>Submit</h3><p>A short write-up, a 3-minute demo video and a reusable template or prompt set.</p></li>
<li><h3>Get judged</h3><p>A panel scores entries against the published rubric. Winners are featured on AiNew.</p></li>
</ol></div></section>

<section class="section tight"><div class="wrap two-col">
<div><h2>Judging criteria</h2>
<div class="tiers" style="grid-template-columns:1fr 1fr">
<div class="tier"><div class="price">40%</div><h3>Impact</h3><p class="small muted">Time or money saved, backed by a believable measure.</p></div>
<div class="tier"><div class="price">25%</div><h3>Originality</h3><p class="small muted">A fresh approach, not a copy of a tutorial.</p></div>
<div class="tier"><div class="price">20%</div><h3>Clarity</h3><p class="small muted">Could a non-expert follow and trust it?</p></div>
<div class="tier"><div class="price">15%</div><h3>Reusability</h3><p class="small muted">How easily others can adapt it.</p></div>
</div>
<h3 style="margin-top:28px">More formats coming</h3>
<ul class="kv"><li>Monthly Prompt Sprint: the most useful prompt in a set category</li><li>Student AI Explainer: teach one AI concept in under 600 words</li><li>Sponsor-themed awards for work built on partner products</li></ul>
</div>
<form class="form-panel" id="register" data-form="contest-registration" data-subject="Contest registration" data-next="1">
{HP}<h3>Register for Season 1</h3><p class="small muted">We'll send the brief, rules and the confirmed prize pool before entries open.</p>
<div class="grid-2">{inp("name", "Name", ac="name")}{inp("email", "Email", "email", ac="email")}</div>
<div class="grid-2">{inp("country", "Country", ac="country-name")}{sel("experience", "Your AI experience", ["Beginner", "Comfortable user", "Builder / developer", "Professional / consultant"])}</div>
{sel("entry_type", "Entering as", ["Individual", "Team of 2–4"])}
{area("idea", "Early idea", False, "One or two lines is plenty.")}
<div class="field"><label class="check"><input type="checkbox" name="age_confirmed" value="18 or older" required><span>I confirm I am 18 or older.</span></label></div>
{CONSENT}
<button class="btn mark-btn" type="submit">Register for the brief</button><p class="form-msg" role="status"></p>
</form></div></section>

<section class="section tight"><div class="wrap">
<h2>Official rules summary</h2>
<ol class="rules small muted">
<li>No purchase or payment is necessary to enter or win. Paying or supporting AiNew does not improve the chance of winning.</li>
<li>This is a contest of skill judged against the published criteria; it is not a lottery or game of chance.</li>
<li>Open to individuals aged 18 or over. Void where prohibited or restricted by law. Employees of AiNew and of prize sponsors may not enter.</li>
<li>Entries must be the entrant's original work and must not infringe anyone's rights or include personal data without consent.</li>
<li>Entrants keep ownership of their work and grant AiNew a non-exclusive licence to display and promote entries.</li>
<li>Prize amounts, entry dates and judging dates are confirmed on this page before entries open; the full rules sent to registrants govern.</li>
<li>Winners may need to confirm eligibility and identity before receiving a prize. Taxes on prizes are the winner's responsibility.</li>
<li>AiNew may disqualify entries that break the rules, and may modify or cancel a contest if required by law or circumstances beyond its control.</li>
</ol></div></section>'''


def support():
    tiers = [("5", "Supporter", "Covers a day of hosting and tools."), ("25", "Builder", "Funds research time for a new guide."),
             ("100", "Champion", "Pays a freelance editor or creator for an afternoon."), ("500", "Patron", "Seeds a contest prize. Thanked by name with your permission.")]
    tcards = "".join(f'<div class="tier{" pick" if n == "Builder" else ""}"><div class="price">${a}</div><h3>{n}</h3><p class="small muted">{d}</p><button class="btn ghost sm" type="button" data-amount="{a}" aria-pressed="false">Choose ${a}</button></div>' for a, n, d in tiers)
    funds = ["Where it's needed most", "Operations & hosting", "New guides & research", "Promotion & marketing", "Talent fund (paying writers and creators)", "Contest prize pool"]
    return page_head("Support independent AI education",
                     "AiNew is free to read. Supporter contributions keep it that way, and fund new guides, paid work for freelance creators, promotion and the contest prize pool.",
                     [("Home", "index.html"), ("Support us", "")]) + f'''
<section class="section tight" style="padding-top:0"><div class="wrap">
<div class="tiers">{tcards}</div>
<div data-pay-wrap hidden style="margin-top:24px" class="panel"><h3>Contribute instantly</h3><div class="btn-row">
<a class="btn" data-pay="stripe" hidden target="_blank" rel="noopener">Pay by card</a>
<a class="btn ghost" data-pay="paypal" hidden target="_blank" rel="noopener">PayPal</a>
<a class="btn ghost" data-pay="kofi" hidden target="_blank" rel="noopener">Ko-fi</a>
<a class="btn ghost" data-pay="bmc" hidden target="_blank" rel="noopener">Buy us a coffee</a>
<a class="btn ghost" data-pay="github" hidden target="_blank" rel="noopener">GitHub Sponsors</a></div></div>
</div></section>

<section class="section tight"><div class="wrap two-col">
<div><h2>Where your support goes</h2>
<ul class="kv"><li><strong>Operations:</strong>&nbsp;hosting, tools, data feeds and the newsletter</li><li><strong>Original guides:</strong>&nbsp;research and editing time for in-depth, accurate content</li><li><strong>Promotion:</strong>&nbsp;reaching more people who need clear, honest AI information</li><li><strong>Talent fund:</strong>&nbsp;paying freelance writers, editors and video creators fairly</li><li><strong>Contests:</strong>&nbsp;prize money for the Build Challenge and future competitions</li></ul>
<p class="small muted" style="margin-top:20px">You can direct your contribution to one area. AiNew is an independent publication, not a registered charity, so contributions are not tax-deductible. Contributions are voluntary and do not purchase goods or services. Questions about a contribution or a refund? <a href="{{{{root}}}}contact.html?topic=Support">Contact us</a>.</p>
</div>
<form class="form-panel" data-form="support-pledge" data-subject="NEW SUPPORT PLEDGE" data-next="1">
{HP}<h3>Pledge your support</h3><p class="small muted">Tell us how you'd like to help and we'll send a secure payment link by email within one business day.</p>
<div class="grid-2"><div class="field"><label for="pledge-amount">Amount (USD)</label><input id="pledge-amount" name="amount" type="number" min="1" step="1" placeholder="25" required></div>
{sel("frequency", "Frequency", ["One-time", "Monthly"])}</div>
{sel("fund", "Direct it to", funds)}
<div class="grid-2">{inp("name", "Name", ac="name")}{inp("email", "Email", "email", ac="email")}</div>
<div class="field"><label class="check"><input type="checkbox" name="public_thanks" value="Yes, thank me publicly"><span>Thank me by name on the supporters list</span></label></div>
{area("message", "Message", False, "Anything you'd like us to cover?")}
{CONSENT}
<button class="btn mark-btn" type="submit">Send my pledge</button><p class="form-msg" role="status"></p>
</form></div></section>
<script>(function(){{var f=new URLSearchParams(location.search).get("fund");if(!f)return;var s=document.getElementById("fund");if(s)Array.prototype.forEach.call(s.options,function(o){{if(o.text===f)s.value=o.text}})}})();</script>'''


def careers():
    roles = [
        ("AI explainer writer", "Freelance, remote", "Research and write clear, accurate guides for non-experts. Strong editing and fact-checking habits matter more than hype."),
        ("Short-form video creator", "Freelance, remote", "Turn our guides into 60-second and 5-minute explainers for YouTube and social."),
        ("Community and contest manager", "Part-time, remote", "Run the Build Challenge, support entrants and judges, and grow the newsletter community."),
        ("Partnerships and ad sales", "Commission-based, remote", "Bring in sponsors and featured listings that fit our standards."),
        ("AI implementation specialist", "Network, project-based", "Join our expert network and get matched with businesses that request AI plans and builds."),
    ]
    rcards = "".join(f'<div class="usecase"><span class="small muted">{esc(t)}</span><h3>{esc(n)}</h3><p>{esc(d)}</p><a href="#apply" data-role="{esc(n)}">Apply for this role</a></div>' for n, t, d in roles)
    return page_head("Work with AiNew", "We pay people to make AI understandable and useful. Join as a writer, creator, community lead, partner or implementation specialist.",
                     [("Home", "index.html"), ("Careers", "")]) + f'''
<section class="section tight" style="padding-top:0"><div class="wrap">
<div class="usecases">{rcards}</div>
<div class="inline-cta"><p>Hiring AI talent for your own company? We can match you with vetted specialists.</p><a class="btn sm" href="{{{{root}}}}ai-services.html?goal=talent#plan">Hire AI talent</a></div>
</div></section>
<section class="section tight" id="apply"><div class="wrap two-col">
<div><h2>Join the talent network</h2><p class="muted">One application covers every role. We review applications on a rolling basis and reply when there's a fit.</p>
<ul class="kv"><li>Paid work, agreed in writing before you start</li><li>Remote and flexible</li><li>Credit for your work on the site</li></ul></div>
<form class="form-panel" data-form="talent-application" data-subject="Talent network application" data-next="1">
{HP}
{sel("role", "Role", [r[0] for r in roles] + ["Other"])}
<div class="grid-2">{inp("name", "Full name", ac="name")}{inp("email", "Email", "email", ac="email")}</div>
<div class="grid-2">{inp("portfolio", "Portfolio or work samples", "url", True, "https://")}{inp("linkedin", "LinkedIn or profile", "url", False, "https://")}</div>
<div class="grid-2">{inp("country", "Country", ac="country-name")}{sel("availability", "Availability", ["A few hours a week", "Part-time", "Full-time freelance", "Per project"])}</div>
{inp("rate", "Expected rate", "text", False, "e.g. $40/hour or $300 per article")}
{area("why", "Why you, in a few lines", True)}
{CONSENT}
<button class="btn" type="submit">Send application</button><p class="form-msg" role="status"></p>
</form></div></section>
<script>(function(){{document.addEventListener("click",function(e){{var a=e.target.closest("[data-role]");if(!a)return;var s=document.getElementById("role");if(s)s.value=a.getAttribute("data-role")}})}})();</script>'''


def newsletter(guide, tool, prompt):
    return page_head("The AiNew Weekly", "One short email a week: the AI developments worth your attention, tools to try, a prompt to steal and a guide to go deeper. Free.",
                     [("Home", "index.html"), ("Newsletter", "")]) + f'''
<section class="section tight" style="padding-top:0"><div class="wrap two-col">
<div><h2>Subscribe</h2>{newsletter_form("{{root}}", "page", "Subscribe free")}
<ul class="kv" style="margin-top:24px"><li>Five-minute read, every week</li><li>No hype, no spam, unsubscribe in one click</li><li>Your email is never sold</li></ul>
<p class="small muted" style="margin-top:20px">Want to reach our readers? <a href="{{{{root}}}}advertise.html">Sponsor an issue</a>.</p></div>
<article class="issue" aria-label="What an issue looks like">
<header><h3 style="margin:0">What an issue looks like</h3><p>The AiNew Weekly</p></header>
<div class="blk"><h3>The shift worth knowing</h3><p class="muted small">One development from the week, explained: what changed, who it affects and whether you should act.</p></div>
<div class="blk"><h3>Tool to try: {esc(tool["name"])}</h3><p class="muted small">{esc(tool["desc"])}</p></div>
<div class="blk"><h3>Prompt to steal: {esc(prompt["title"])}</h3><p class="muted small">{esc(prompt["use"])}</p></div>
<div class="blk"><h3>Go deeper: {esc(guide["title"])}</h3><p class="muted small">{esc(guide["summary"])}</p></div>
</article></div></section>'''


def contact():
    topics = ["General question", "AI services", "Advertising", "Partnership", "Website or domain acquisition", "Press", "Support", "Correction", "Copyright or takedown", "Other"]
    return page_head("Contact AiNew", "Questions, corrections, partnerships or press. Use the form and we'll reply by email, usually within two business days.",
                     [("Home", "index.html"), ("Contact", "")]) + f'''
<section class="section tight" style="padding-top:0"><div class="wrap two-col">
<div>
<div class="panel inked" style="margin-bottom:18px"><h2>Interested in this website or domain?</h2><p>For acquisition, sponsorship, advertising or partnership, contact the owner directly.</p><a class="btn" href="{PROMO_URL}" target="_blank" rel="noopener">Contact the owner</a></div>
<div class="panel"><h3>Prefer email?</h3><p class="small muted">Open a new message in your email app.</p><a class="btn ghost sm" href="{{{{root}}}}contact.html" data-contact data-subject="Message from AiNew.com">Email AiNew</a>
<h3 style="margin-top:20px">Faster routes</h3><ul class="kv small"><li><a href="{{{{root}}}}ai-services.html#plan">Request a free AI plan</a></li><li><a href="{{{{root}}}}advertise.html#ad-form">Advertising enquiry</a></li><li><a href="{{{{root}}}}submit-tool.html">Submit a tool</a></li></ul></div>
</div>
<form class="form-panel" data-form="contact" data-subject="Contact form" data-next="1">
{HP}
<div class="grid-2">{inp("name", "Name", ac="name")}{inp("email", "Email", "email", ac="email")}</div>
{sel("topic", "Topic", topics)}
{area("message", "Message", True)}
{CONSENT}
<button class="btn" type="submit">Send message</button><p class="form-msg" role="status"></p>
</form></div></section>
<script>(function(){{var t=new URLSearchParams(location.search).get("topic");if(!t)return;var s=document.getElementById("topic");if(!s)return;Array.prototype.forEach.call(s.options,function(o){{if(o.text.toLowerCase().indexOf(t.toLowerCase())===0)s.value=o.text}})}})();</script>'''
