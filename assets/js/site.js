/* AiNew.com — site behaviour. No dependencies. */
(function () {
  "use strict";
  var doc = document.documentElement;
  var ROOT = doc.getAttribute("data-root") || "";
  var C = window.AINEW_CONFIG || {};
  var $ = function (s, el) { return (el || document).querySelector(s); };
  var $$ = function (s, el) { return Array.prototype.slice.call((el || document).querySelectorAll(s)); };
  var store = {
    get: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  };
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]; }); }

  /* Contact routing: decoded only when needed, never written into the page */
  function route() {
    if (C.formAlias) return C.formAlias;
    var r = C.r || [], k = C.k || 0, out = "";
    for (var i = 0; i < r.length; i++) out += String.fromCharCode((r[i] - i) ^ k);
    return out.split("").reverse().join("");
  }

  /* Theme */
  var saved = store.get("ainew-theme");
  if (saved) doc.setAttribute("data-theme", saved);
  var tbtn = $("#theme-btn");
  if (tbtn) tbtn.addEventListener("click", function () {
    var cur = doc.getAttribute("data-theme") || (matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
    var next = cur === "dark" ? "light" : "dark";
    doc.setAttribute("data-theme", next); store.set("ainew-theme", next);
    tbtn.setAttribute("aria-label", next === "dark" ? "Switch to light theme" : "Switch to dark theme");
  });

  /* Mobile menu */
  var mbtn = $("#menu-btn"), nav = $("#site-nav");
  if (mbtn && nav) mbtn.addEventListener("click", function () {
    var open = nav.classList.toggle("open");
    mbtn.setAttribute("aria-expanded", open ? "true" : "false");
  });

  /* Footer year */
  $$("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* Email links: the address is assembled on click only */
  $$("a[data-contact]").forEach(function (a) {
    a.addEventListener("click", function (e) {
      e.preventDefault();
      var subj = a.getAttribute("data-subject") || "Inquiry from AiNew.com";
      window.location.href = "mai" + "lto:" + route() + "?subject=" + encodeURIComponent(subj);
    });
  });

  /* Forms → FormSubmit (AJAX) */
  $$("form[data-form]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var hp = form.querySelector("[name=_honey]");
      if (hp && hp.value) return;
      if (!form.reportValidity()) return;
      var msg = form.querySelector(".form-msg") || (function () { var p = document.createElement("p"); p.className = "form-msg"; p.setAttribute("role", "status"); form.appendChild(p); return p; })();
      var btn = form.querySelector("[type=submit]");
      var label = btn ? btn.textContent : "";
      if (btn) { btn.disabled = true; btn.textContent = "Sending…"; }
      var data = {};
      new FormData(form).forEach(function (v, k) {
        if (k === "_honey") return;
        data[k] = data[k] ? data[k] + ", " + v : v;
      });
      var kind = form.getAttribute("data-form");
      data._subject = (form.getAttribute("data-subject") || "AiNew.com form") + " — " + kind;
      data._template = "table";
      data._captcha = "false";
      data.page = location.pathname;
      fetch("https://formsubmit.co/ajax/" + route(), {
        method: "POST",
        headers: { "Content-Type": "application/json", "Accept": "application/json" },
        body: JSON.stringify(data)
      }).then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { return { ok: r.ok, j: j }; }); })
        .then(function (res) {
          if (!res.ok || String(res.j.success) === "false") throw new Error(res.j.message || "send failed");
          var next = form.getAttribute("data-next");
          if (next) { location.href = ROOT + "thank-you.html?f=" + encodeURIComponent(kind); return; }
          form.reset();
          msg.className = "form-msg ok";
          msg.textContent = form.getAttribute("data-ok") || "Done. Check your inbox for a confirmation.";
        })
        .catch(function () {
          msg.className = "form-msg err";
          msg.textContent = "That didn't send. Check your connection and try again, or use the contact page.";
        })
        .then(function () { if (btn) { btn.disabled = false; btn.textContent = label; } });
    });
  });

  /* Filterable grids (tools, prompts) */
  function filterable(cfg) {
    var grid = $(cfg.grid); if (!grid) return;
    var cards = $$(cfg.item, grid);
    var q = $(cfg.q), sel = $(cfg.select), sort = $(cfg.sort), count = $(cfg.count), empty = $(cfg.empty);
    var chips = $$(cfg.chips);
    var cat = "all";
    function apply() {
      var term = (q && q.value || "").trim().toLowerCase();
      var price = sel ? sel.value : "all";
      var shown = 0;
      cards.forEach(function (c) {
        var ok = (cat === "all" || c.dataset.cat === cat) &&
          (price === "all" || c.dataset.price === price) &&
          (!term || c.dataset.text.indexOf(term) > -1);
        c.hidden = !ok; if (ok) shown++;
      });
      if (count) count.textContent = "Showing " + shown + " of " + cards.length;
      if (empty) empty.hidden = shown !== 0;
    }
    chips.forEach(function (ch) {
      ch.addEventListener("click", function () {
        chips.forEach(function (x) { x.setAttribute("aria-pressed", "false"); });
        ch.setAttribute("aria-pressed", "true"); cat = ch.dataset.cat; apply();
      });
    });
    if (q) q.addEventListener("input", apply);
    if (sel) sel.addEventListener("change", apply);
    if (sort) sort.addEventListener("change", function () {
      var v = sort.value;
      cards.sort(function (a, b) {
        if (v === "az") return a.dataset.name.localeCompare(b.dataset.name);
        if (v === "za") return b.dataset.name.localeCompare(a.dataset.name);
        return (+a.dataset.order) - (+b.dataset.order);
      }).forEach(function (c) { grid.appendChild(c); });
    });
    var param = new URLSearchParams(location.search);
    if (param.get("q") && q) q.value = param.get("q");
    var pc = param.get("cat");
    if (pc) chips.forEach(function (ch) { if (ch.dataset.cat === pc) ch.click(); });
    apply();
  }
  filterable({ grid: "#tool-grid", item: ".tool", q: "#tool-q", select: "#tool-price", sort: "#tool-sort", count: "#tool-count", empty: "#tool-empty", chips: "#tool-chips .chip" });
  filterable({ grid: "#prompt-grid", item: ".prompt", q: "#prompt-q", count: "#prompt-count", empty: "#prompt-empty", chips: "#prompt-chips .chip" });

  /* Copy buttons */
  document.addEventListener("click", function (e) {
    var b = e.target.closest && e.target.closest("[data-copy]");
    if (!b) return;
    var src = document.getElementById(b.getAttribute("data-copy"));
    if (!src) return;
    var text = src.innerText;
    var done = function () { b.textContent = "Copied"; b.classList.add("done"); setTimeout(function () { b.textContent = "Copy prompt"; b.classList.remove("done"); }, 1800); };
    if (navigator.clipboard) navigator.clipboard.writeText(text).then(done, function () {});
    else { var t = document.createElement("textarea"); t.value = text; document.body.appendChild(t); t.select(); try { document.execCommand("copy"); done(); } catch (x) {} t.remove(); }
  });

  /* Prompt of the day (rotates daily) */
  var potd = $("#potd");
  if (potd) fetch(ROOT + "data/prompts.json").then(function (r) { return r.json(); }).then(function (list) {
    var d = new Date(); var day = Math.floor((d - new Date(d.getFullYear(), 0, 0)) / 864e5);
    var p = list[day % list.length];
    $("#potd-title").textContent = p.title;
    $("#potd-use").textContent = p.use;
    $("#potd-cat").textContent = p.category;
    $("#potd-text").textContent = p.prompt;
  }).catch(function () {});

  /* YouTube facade: loads the player only after a click */
  $$("button.yt[data-id]").forEach(function (b) {
    b.addEventListener("click", function () {
      var f = document.createElement("iframe");
      f.src = "https://www.youtube-nocookie.com/embed/" + b.dataset.id + "?autoplay=1&rel=0";
      f.title = b.getAttribute("aria-label") || "YouTube video";
      f.allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture";
      f.allowFullscreen = true;
      b.innerHTML = ""; b.appendChild(f);
    }, { once: true });
  });

  /* News radar */
  function timeAgo(iso) {
    var t = Date.parse(iso); if (!t) return "";
    var h = Math.round((Date.now() - t) / 36e5);
    if (h < 1) return "just now"; if (h < 24) return h + "h ago";
    var d = Math.round(h / 24); return d === 1 ? "yesterday" : d + " days ago";
  }
  function renderRadar(el, items, limit) {
    if (!items.length) { el.innerHTML = '<li class="empty">The radar refreshes every few hours. Check back shortly, or browse the guides below.</li>'; return; }
    el.innerHTML = items.slice(0, limit).map(function (n) {
      var fresh = (Date.now() - Date.parse(n.date)) < 864e5;
      return '<li class="' + (fresh ? "is-new" : "") + '"><div class="meta"><span>' + esc(n.source) + '</span><span>' + esc(timeAgo(n.date)) + '</span>' + (fresh ? '<span class="mark">new</span>' : "") + '</div><a href="' + esc(n.link) + '" target="_blank" rel="noopener nofollow">' + esc(n.title) + '</a></li>';
    }).join("");
  }
  var radarMini = $("#radar-mini"), radarFull = $("#radar-full");
  if (radarMini || radarFull) fetch(ROOT + "data/news.json", { cache: "no-cache" }).then(function (r) { return r.json(); }).then(function (data) {
    var items = (data.items || []).filter(function (n) { return n.title && n.link; });
    var upd = $$("[data-radar-updated]");
    upd.forEach(function (u) { u.textContent = data.updated ? "Updated " + timeAgo(data.updated) : ""; });
    if (radarMini) renderRadar(radarMini, items, 6);
    if (radarFull) {
      var srcWrap = $("#radar-sources"), q = $("#radar-q"), current = "all";
      var sources = {}; items.forEach(function (n) { sources[n.source] = (sources[n.source] || 0) + 1; });
      srcWrap.innerHTML = '<button class="chip" aria-pressed="true" data-s="all">All<span>' + items.length + '</span></button>' +
        Object.keys(sources).sort().map(function (s) { return '<button class="chip" aria-pressed="false" data-s="' + esc(s) + '">' + esc(s) + '<span>' + sources[s] + '</span></button>'; }).join("");
      var draw = function () {
        var term = (q.value || "").toLowerCase();
        renderRadar(radarFull, items.filter(function (n) {
          return (current === "all" || n.source === current) && (!term || n.title.toLowerCase().indexOf(term) > -1);
        }), 200);
      };
      srcWrap.addEventListener("click", function (e) {
        var b = e.target.closest(".chip"); if (!b) return;
        $$(".chip", srcWrap).forEach(function (x) { x.setAttribute("aria-pressed", "false"); });
        b.setAttribute("aria-pressed", "true"); current = b.dataset.s; draw();
      });
      q.addEventListener("input", draw); draw();
    }
  }).catch(function () {
    [radarMini, radarFull].forEach(function (el) { if (el) renderRadar(el, [], 0); });
  });

  /* Multi-step lead form */
  $$("form.stepper").forEach(function (form) {
    var steps = $$(".step", form), bar = $(".progress span", form), i = 0;
    function show(n) {
      steps.forEach(function (s, k) { s.classList.toggle("on", k === n); });
      if (bar) bar.style.width = ((n + 1) / steps.length * 100) + "%";
      var first = steps[n].querySelector("input,select,textarea"); if (first && n > 0) first.focus({ preventScroll: true });
    }
    function valid(n) {
      var ok = true;
      $$("input,select,textarea", steps[n]).forEach(function (f) { if (ok && !f.checkValidity()) { f.reportValidity(); ok = false; } });
      return ok;
    }
    $$("[data-next-step]", form).forEach(function (b) { b.addEventListener("click", function () { if (valid(i)) show(++i); }); });
    $$("[data-prev-step]", form).forEach(function (b) { b.addEventListener("click", function () { show(--i); }); });
    var pre = new URLSearchParams(location.search).get("goal");
    if (pre) $$("input[name=goal]", form).forEach(function (r) { if (r.value === pre) r.checked = true; });
    show(0);
  });

  /* Readiness quiz */
  var quiz = $("#quiz");
  if (quiz) quiz.addEventListener("submit", function (e) {
    e.preventDefault();
    if (!quiz.reportValidity()) return;
    var qs = $$(".q", quiz), total = 0;
    qs.forEach(function (q) { var c = q.querySelector("input:checked"); total += c ? +c.value : 0; });
    var pct = Math.round(total / (qs.length * 3) * 100);
    var band = pct >= 75 ? "Ready to scale" : pct >= 50 ? "Ready to pilot" : pct >= 25 ? "Getting started" : "Foundations first";
    var advice = {
      "Ready to scale": "Your data, people and process basics are in place. The next gains come from connecting AI to core workflows and measuring results.",
      "Ready to pilot": "You have enough in place to run one or two focused pilots. Pick a high-volume, low-risk task and set a clear success measure.",
      "Getting started": "Start with team-wide AI literacy and a short usage policy, then test AI on everyday tasks before automating anything.",
      "Foundations first": "Before tools, sort out where your information lives and who owns it. A small amount of structure makes every AI tool far more useful."
    }[band];
    var res = $("#quiz-result");
    res.hidden = false;
    $("#score-ring").style.setProperty("--v", pct);
    $("#score-num").textContent = pct;
    $("#score-band").textContent = band;
    $("#score-advice").textContent = advice;
    $$("[name=readiness_score]").forEach(function (f) { f.value = pct + "/100"; });
    $$("[name=readiness_band]").forEach(function (f) { f.value = band; });
    res.scrollIntoView({ behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth", block: "start" });
  });

  /* ROI calculator */
  var roi = $("#roi");
  if (roi) {
    var calc = function () {
      var v = function (id) { return +($("#" + id).value) || 0; };
      var hrs = v("roi-people") * v("roi-hours") * 48;
      var net = hrs * v("roi-rate") - v("roi-cost") * 12;
      $$("[data-out]", roi).forEach(function (o) { o.textContent = o.dataset.out === "hrs" ? Math.round(hrs).toLocaleString() : (net < 0 ? "-$" : "$") + Math.abs(Math.round(net)).toLocaleString(); });
      $$("output[for]", roi).forEach(function (o) { var src = $("#" + o.getAttribute("for")); if (src) o.textContent = src.value; });
    };
    $$("input", roi).forEach(function (i) { i.addEventListener("input", calc); }); calc();
  }

  /* Support page: payment buttons appear only when configured */
  var pay = C.pay || {};
  $$("[data-pay]").forEach(function (a) {
    var url = pay[a.getAttribute("data-pay")];
    if (url) { a.href = url; a.hidden = false; }
  });
  if ($$("[data-pay]").some(function (a) { return !a.hidden; })) $$("[data-pay-wrap]").forEach(function (w) { w.hidden = false; });
  $$("[data-amount]").forEach(function (b) {
    b.addEventListener("click", function () {
      var f = $("#pledge-amount"); if (f) { f.value = b.dataset.amount; f.focus(); }
      $$("[data-amount]").forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
    });
  });
  if (C.youtubeChannel) $$("[data-yt-channel]").forEach(function (a) { a.href = C.youtubeChannel; a.hidden = false; });

  /* Site search */
  var sres = $("#search-results");
  if (sres) {
    var sq = $("#search-q"); var term0 = new URLSearchParams(location.search).get("q") || ""; sq.value = term0;
    fetch(ROOT + "data/search.json").then(function (r) { return r.json(); }).then(function (idx) {
      var run = function () {
        var t = sq.value.trim().toLowerCase();
        if (!t) { sres.innerHTML = ""; $("#search-count").textContent = "Type to search guides, tools and prompts."; return; }
        var words = t.split(/\s+/);
        var hits = idx.map(function (d) {
          var hay = (d.t + " " + d.d + " " + d.x).toLowerCase(), s = 0;
          words.forEach(function (w) { if (d.t.toLowerCase().indexOf(w) > -1) s += 5; if (hay.indexOf(w) > -1) s += 1; else s -= 99; });
          return { d: d, s: s };
        }).filter(function (h) { return h.s > 0; }).sort(function (a, b) { return b.s - a.s; }).slice(0, 40);
        $("#search-count").textContent = hits.length ? hits.length + " results" : "No matches. Try a broader word, like \"writing\" or \"agents\".";
        sres.innerHTML = hits.map(function (h) { return '<li><a href="' + ROOT + esc(h.d.u) + '">' + esc(h.d.t) + '</a><span class="k">' + esc(h.d.k) + '</span><p>' + esc(h.d.d) + '</p></li>'; }).join("");
      };
      sq.addEventListener("input", run); run();
    });
  }

  /* Consent banner */
  var ck = $("#cookie");
  var choice = store.get("ainew-consent");
  if (choice === "necessary") (window.adsbygoogle = window.adsbygoogle || []).requestNonPersonalizedAds = 1;
  if (ck && !choice) {
    ck.classList.add("show");
    $$("[data-consent]", ck).forEach(function (b) {
      b.addEventListener("click", function () {
        store.set("ainew-consent", b.dataset.consent);
        if (b.dataset.consent === "necessary") (window.adsbygoogle = window.adsbygoogle || []).requestNonPersonalizedAds = 1;
        ck.classList.remove("show");
      });
    });
  }
})();
