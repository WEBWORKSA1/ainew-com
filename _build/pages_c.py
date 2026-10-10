"""Page bodies: about, policies, legal, thank-you, 404."""
from layout import page_head, PROMO_URL, OPERATOR_URL

EFFECTIVE = "October 10, 2026"


def about(n_guides, n_tools, n_prompts):
    return page_head("About AiNew", "AiNew.com tracks what's new in artificial intelligence and explains it in plain English, so you can decide what's worth your time.",
                     [("Home", "index.html"), ("About", "")]) + f'''
<section class="section tight" style="padding-top:0"><div class="wrap legal">
<h2>Why AiNew exists</h2>
<p>New AI models, tools and features arrive every week. Most coverage is either breathless or impenetrable. AiNew sits in between: we follow the developments, filter out the noise and write practical explanations for people who need to make real decisions about AI at work.</p>
<h2>What you'll find here</h2>
<ul>
<li><strong>News radar</strong>: headlines from established AI publishers and research labs, refreshed automatically several times a day, always linking to the original source.</li>
<li><strong>{n_guides} in-depth guides</strong> on understanding AI, prompting, building with AI, safety and careers.</li>
<li><strong>An AI tools directory</strong> of {n_tools} established tools, searchable by task and pricing model.</li>
<li><strong>A prompt library</strong> of {n_prompts} original, reusable prompts.</li>
<li><strong>Help for businesses</strong>: a free AI readiness check and written starting plans, with optional introductions to vetted specialists.</li>
<li><strong>Contests</strong> that reward practical, useful AI work.</li>
</ul>
<h2>Who runs AiNew</h2>
<p>AiNew.com is an independent publication operated by <a href="{OPERATOR_URL}" target="_blank" rel="noopener">Web Works</a>, a small digital publisher. We're not affiliated with any AI company, and no vendor pays for editorial coverage.</p>
<h2>How we make money</h2>
<p>We're transparent about this because it affects trust. AiNew earns from display advertising served by Google, clearly labelled sponsorships and featured listings, partnerships with service providers, and voluntary contributions from readers. None of these buy a place in our guides or change what we say about a tool. Read our <a href="editorial-policy.html">editorial policy</a> for details.</p>
<h2>Get in touch</h2>
<p>Corrections, tips and partnership ideas are welcome through the <a href="contact.html">contact page</a>. If you're interested in sponsoring, advertising, partnering, or acquiring this website or domain, <a href="{PROMO_URL}" target="_blank" rel="noopener">contact the owner directly</a>.</p>
</div></section>'''


def editorial():
    return page_head("Editorial policy", "How we research, write, label and correct content on AiNew.com.", [("Home", "index.html"), ("Editorial policy", "")]) + f'''
<section class="section tight" style="padding-top:0"><div class="wrap legal">
<p class="muted">Effective {EFFECTIVE}</p>
<h2>Independence</h2>
<p>Editorial decisions are made by AiNew alone. Advertisers, sponsors and partners cannot review, edit or approve guides before publication, and payment never buys a positive mention.</p>
<h2>Accuracy</h2>
<p>Guides are written to stay accurate over time. We avoid unsupported statistics, explain principles rather than chasing version numbers, and link to primary sources where they help. When a guide relies on facts that change, such as product features or pricing, we tell you to confirm the current details with the provider.</p>
<h2>Use of AI in our work</h2>
<p>We cover AI, and we use it. AI tools may help with research, outlining and drafting. Every guide is reviewed, edited and fact-checked by a person before it is published, and a person is accountable for everything we publish.</p>
<h2>Labelling paid content</h2>
<ul><li>Paid tool placements carry a "Featured" badge.</li><li>Sponsored newsletter sections and site placements are labelled "Sponsor".</li><li>Guide partnerships appear as "Presented by" and never alter the guide's content.</li><li>Ads served by Google are labelled by Google.</li></ul>
<h2>Tool directory standards</h2>
<p>Listings are free and editorial. We include established, working products with a clear purpose and public pricing. We remove tools that shut down, change hands in ways that affect users, or break our standards. Listings use generated initials rather than company logos.</p>
<h2>News radar</h2>
<p>The radar automatically collects headlines from public RSS feeds of established publishers. We show only the headline, source and time, and link to the original. Inclusion is not endorsement.</p>
<h2>Corrections</h2>
<p>If we get something wrong, we fix it promptly and, for material errors, note the correction at the end of the guide. Report an error through the <a href="contact.html?topic=Correction">contact page</a>.</p>
</div></section>'''


def privacy():
    return page_head("Privacy policy", "What we collect, why, and the choices you have.", [("Home", "index.html"), ("Privacy policy", "")]) + f'''
<section class="section tight" style="padding-top:0"><div class="wrap legal">
<p class="muted">Effective {EFFECTIVE}</p>
<p>This policy explains how AiNew.com ("AiNew", "we", "us") handles information when you visit the website or contact us.</p>
<h2>Information you give us</h2>
<p>When you submit a form (newsletter, AI plan request, readiness report, advertising enquiry, tool submission, contest registration, support pledge, talent application or contact form), we receive the details you enter, such as your name, email address, company and message. We use this only to respond to you and to provide what you asked for. We do not sell your personal information.</p>
<p>Forms are delivered to our inbox by FormSubmit (formsubmit.co), a form-processing service, which handles the submission on our behalf. If you ask for an introduction to a specialist, we share your request with that specialist only with your permission.</p>
<h2>Information collected automatically</h2>
<p>Like most websites, our host and service providers receive standard technical data such as your IP address, browser type, device, referring page and pages visited. Your theme setting and cookie choice are stored in your browser's local storage and never sent to us.</p>
<h2>Advertising and cookies</h2>
<p>We use Google AdSense to show ads. Google and its partners use cookies to serve ads based on your prior visits to this and other websites.</p>
<ul>
<li>Google's use of advertising cookies enables it and its partners to serve ads to you based on your visit to this site and/or other sites on the internet.</li>
<li>You may opt out of personalised advertising by visiting <a href="https://adssettings.google.com/" target="_blank" rel="noopener">Google Ads Settings</a>. You can also opt out of some third-party vendors' use of cookies for personalised advertising at <a href="https://www.aboutads.info/choices/" target="_blank" rel="noopener">aboutads.info</a> or, in Europe, <a href="https://www.youronlinechoices.eu/" target="_blank" rel="noopener">youronlinechoices.eu</a>.</li>
<li>Learn <a href="https://policies.google.com/technologies/partner-sites" target="_blank" rel="noopener">how Google uses information from sites that use its services</a>.</li>
</ul>
<p>When you choose "Necessary only" in our cookie notice, we ask Google to serve non-personalised ads. Visitors in the European Economic Area, the UK and Switzerland may also see a consent message from Google's certified consent management platform.</p>
<h2>Other third-party services</h2>
<ul>
<li><strong>Google Fonts</strong> delivers the typefaces used on this site.</li>
<li><strong>YouTube</strong> videos use the privacy-enhanced (youtube-nocookie.com) player and load only after you press play; YouTube's privacy policy then applies.</li>
<li><strong>Links</strong> to tools, publishers and partners take you to sites with their own privacy policies.</li>
</ul>
<h2>How long we keep information</h2>
<p>We keep form submissions only as long as needed to respond and for reasonable business records, then delete them. You can unsubscribe from the newsletter at any time.</p>
<h2>Your rights</h2>
<p>Depending on where you live (for example under the GDPR, UK GDPR, or California and other US state privacy laws), you may have the right to access, correct, delete or port your personal information, and to object to or restrict certain processing. We do not sell or share personal information for cross-context behavioural advertising in exchange for money. To make a request, use the <a href="contact.html?topic=Other">contact page</a>.</p>
<h2>Children</h2>
<p>AiNew is not directed at children under 13, and we do not knowingly collect personal information from them. Contests are open only to adults aged 18 or over.</p>
<h2>Security</h2>
<p>The site is served over HTTPS. No method of transmission or storage is completely secure, but we take reasonable steps to protect what you send us.</p>
<h2>Changes</h2>
<p>We may update this policy and will change the effective date above when we do.</p>
<h2>Contact</h2>
<p>Questions about privacy? Use the <a href="contact.html?topic=Other">contact page</a>.</p>
</div></section>'''


def terms():
    return page_head("Terms of use", "The rules for using AiNew.com.", [("Home", "index.html"), ("Terms of use", "")]) + f'''
<section class="section tight" style="padding-top:0"><div class="wrap legal">
<p class="muted">Effective {EFFECTIVE}</p>
<h2>Using the site</h2>
<p>By using AiNew.com you agree to these terms. If you don't agree, please don't use the site. You must be at least 13 to use the site, and 18 to enter contests.</p>
<h2>Our content</h2>
<p>Guides, prompts, descriptions, design and code on AiNew.com are owned by AiNew or its licensors and protected by copyright. You may read, share links to and quote brief excerpts with attribution. You may use prompts from the prompt library in your own work. You may not republish whole guides, scrape the site in bulk, or present our content as your own.</p>
<h2>Information only</h2>
<p>Content is general information, not professional, legal, financial or technical advice for your situation. AI tools change often; check current details with each provider. See the <a href="disclaimer.html">disclaimer</a>.</p>
<h2>Third-party links and services</h2>
<p>We link to tools, publishers and partners we don't control and aren't responsible for their content, products or policies. Any agreement you make with a specialist introduced through AiNew is between you and that specialist.</p>
<h2>Submissions</h2>
<p>If you send us tool listings, contest entries, tips or feedback, you confirm you have the right to do so, and you allow us to use them to run the site. Contest entries are also governed by the contest rules.</p>
<h2>Contributions</h2>
<p>Support contributions are voluntary, are not donations to a registered charity, and do not purchase goods or services.</p>
<h2>Acceptable use</h2>
<p>Don't misuse forms (spam, malware, false information), interfere with the site's operation, or attempt to access data that isn't yours.</p>
<h2>Liability</h2>
<p>The site is provided "as is". To the fullest extent the law allows, AiNew is not liable for indirect or consequential losses arising from use of the site. Nothing in these terms limits liability that cannot be limited by law.</p>
<h2>Changes</h2>
<p>We may update these terms and will change the effective date when we do. Questions? <a href="contact.html">Contact us</a>.</p>
</div></section>'''


def disclaimer():
    return page_head("Disclaimer and disclosures", "How to use our content, and how AiNew makes money.", [("Home", "index.html"), ("Disclaimer", "")]) + f'''
<section class="section tight" style="padding-top:0"><div class="wrap legal">
<p class="muted">Effective {EFFECTIVE}</p>
<h2>General information only</h2>
<p>Everything on AiNew.com is for general information and education. It is not legal, financial, medical, security or other professional advice. For decisions with legal, financial or safety consequences, consult a qualified professional.</p>
<h2>Accuracy and change</h2>
<p>AI products, features, pricing and policies change quickly. We work to keep content accurate, but we can't guarantee that every detail is current. Confirm important details with the provider.</p>
<h2>AI output</h2>
<p>AI tools can produce incorrect, biased or outdated output. Review anything an AI produces, including output from prompts in our library, before relying on it or publishing it.</p>
<h2>Advertising disclosure</h2>
<p>AiNew displays ads served by Google AdSense. Advertisers don't influence editorial content.</p>
<h2>Sponsorship and partner disclosure</h2>
<p>Some placements are paid. These are always labelled "Featured", "Sponsor" or "Presented by". We may also earn referral fees from partners, including specialists introduced through our AI services. Links to third-party tools may in future include partner tracking; this never affects which tools we list or what we say about them.</p>
<h2>Testimonials and results</h2>
<p>Estimates such as the ROI calculator are illustrative. We don't promise any particular business or income result.</p>
</div></section>'''


def legal():
    return page_head("Trademark and copyright disclosure", "Who owns what on AiNew.com, and how to report a concern.", [("Home", "index.html"), ("Trademark & copyright", "")]) + f'''
<section class="section tight" style="padding-top:0"><div class="wrap legal">
<p class="muted">Effective {EFFECTIVE}</p>
<h2>About the name</h2>
<p>"AiNew" as used on this website refers only to the domain name AiNew.com and the independent publication hosted on it. It is used descriptively, to mean "what's new in AI". AiNew.com is not affiliated with, endorsed by, or connected to any company, product, service or registered or unregistered trademark that uses the same or a similar name, in any jurisdiction. Any resemblance is unintentional. If you believe our use of the name causes confusion with your mark, please <a href="contact.html?topic=Copyright%20or%20takedown">contact us</a> and we'll review it promptly.</p>
<h2>Third-party trademarks</h2>
<p>Product names, company names and brands mentioned on AiNew.com, including those in the tools directory and guides, are trademarks or registered trademarks of their respective owners. They are used for identification and commentary only. Their use does not imply any affiliation with or endorsement by them. We don't use third-party logos; tool cards show generated initials.</p>
<h2>Our copyright</h2>
<p>&copy; 2026 AiNew.com. The original text of our guides, the prompt library, tool descriptions, page design, graphics and site code are protected by copyright. All rights reserved, except that you may use prompts from the prompt library in your own work.</p>
<h2>Third-party content</h2>
<ul>
<li><strong>News radar</strong> headlines belong to their publishers. We show the headline, source and time only, credited and linked to the original article.</li>
<li><strong>Videos</strong> are embedded through YouTube's player under YouTube's Terms of Service and remain the property of their creators.</li>
<li><strong>Fonts</strong> (Bricolage Grotesque and Newsreader) are used under the SIL Open Font License via Google Fonts.</li>
</ul>
<h2>Reporting infringement</h2>
<p>If you believe content on AiNew.com infringes your copyright or trademark, send a notice through the <a href="contact.html?topic=Copyright%20or%20takedown">contact page</a> including: your contact details; the work or mark you own; the URL of the material on our site; a statement that you have a good-faith belief the use is not authorised; and a statement that your notice is accurate and that you are the owner or authorised to act for the owner. We respond to valid notices promptly and remove or correct material where appropriate.</p>
</div></section>'''


def thank_you():
    return '''<section class="wrap ty">
<h1>Thanks, it's on its way</h1>
<p class="lede" style="margin:0 auto 24px">We've received your submission and will reply by email. Check your spam folder if you don't hear from us within two business days.</p>
<div class="btn-row" style="justify-content:center"><a class="btn" href="{{root}}guides/">Read a guide while you wait</a><a class="btn ghost" href="{{root}}index.html">Back to the homepage</a></div>
</section>'''


def not_found():
    return '''<section class="wrap ty">
<h1>That page isn't here</h1>
<p class="lede" style="margin:0 auto 24px">The link may be old or mistyped. Try a search, or start from one of these.</p>
<form action="{{root}}search.html" class="search-row" style="justify-content:center;margin-bottom:20px"><label class="visually-hidden" for="nf-q">Search</label><input id="nf-q" name="q" type="search" placeholder="Search guides, tools and prompts" style="max-width:420px"></form>
<div class="btn-row" style="justify-content:center"><a class="btn" href="{{root}}index.html">Homepage</a><a class="btn ghost" href="{{root}}tools.html">AI tools</a><a class="btn ghost" href="{{root}}guides/">Guides</a></div>
</section>'''
