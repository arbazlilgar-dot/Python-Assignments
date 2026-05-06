/* RedBooking — Vanilla JS (modular) */
(function () {
  "use strict";

  const $  = (s, r=document) => r.querySelector(s);
  const $$ = (s, r=document) => Array.from(r.querySelectorAll(s));
  const fmt = (n) => "₹" + Math.round(n).toLocaleString("en-IN");

  /* ============== Navbar ============== */
  const navToggle = $("[data-nav-toggle]");
  const mobileMenu = $("[data-mobile-menu]");
  if (navToggle && mobileMenu) {
    navToggle.addEventListener("click", () => {
      const open = mobileMenu.classList.toggle("open");
      navToggle.innerHTML = open ? '<i class="bi bi-x-lg"></i>' : '<i class="bi bi-list"></i>';
    });
  }
  // Sticky shadow on scroll
  const nav = $(".app-navbar");
  if (nav) {
    const onScroll = () => nav.classList.toggle("scrolled", window.scrollY > 6);
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  /* ============== Hero swap & dates ============== */
  const swap = $("[data-swap]");
  if (swap) {
    swap.addEventListener("click", () => {
      const f = $("[data-from]"), t = $("[data-to]");
      if (f && t) { const tmp = f.value; f.value = t.value; t.value = tmp; }
    });
  }
  $$('input[type="date"]').forEach((el) => {
    const today = new Date().toISOString().split("T")[0];
    if (!el.value) el.value = today;
    el.min = today;
  });

  /* ============== Listing: Filters + Sort ============== */
  const busList = $("[data-bus-list]");
  if (busList) initListing();

  function initListing() {
    const cards     = $$("[data-bus]", busList);

    // Persist bus context (incl. base price) when user clicks "View seats"
    cards.forEach((card) => {
      const link = card.querySelector('a[href*="seats.html"]');
      if (!link) return;
      link.addEventListener("click", (e) => {
        const basePrice = +card.dataset.price || 0;
        const ctx = {
          operator: card.querySelector(".bus-info h4")?.textContent?.trim() || "",
          type:     card.querySelector(".bus-info .type")?.textContent?.trim() || "",
          rating:   +card.dataset.rating || 0,
          departure: card.dataset.departure || "",
          duration:  +card.dataset.duration || 0,
          types:     card.dataset.types || "",
          basePrice
        };
        try { localStorage.setItem("rb_bus_ctx", JSON.stringify(ctx)); } catch (_) {}
        // Also pass via query string so the seats page works without storage
        const url = new URL(link.getAttribute("href"), window.location.href);
        url.searchParams.set("base", String(basePrice));
        url.searchParams.set("op",   ctx.operator);
        link.setAttribute("href", url.pathname + "?" + url.searchParams.toString());
      });
    });
    const emptyEl   = $("[data-empty]");
    const countEls  = $$("[data-result-count]");
    const rangeEl   = $("[data-filter-price]");
    const rangeOut  = $("[data-range-out]");
    const sortSel   = $("[data-sort-select]");
    const timePills = $$("[data-time-pill]");
    const typeBoxes = $$("[data-filter-type]");
    const ratingRds = $$("[data-filter-rating]");

    function timeBucket(hhmm) {
      const h = parseInt(hhmm.split(":")[0], 10);
      if (h < 6)  return "early";
      if (h < 12) return "morning";
      if (h < 18) return "afternoon";
      return "night";
    }

    function applyFilters() {
      const maxPrice = rangeEl ? +rangeEl.value : Infinity;
      const activeTimes = timePills.filter(p => p.classList.contains("active")).map(p => p.dataset.time);
      const activeTypes = typeBoxes.filter(c => c.checked).map(c => c.value);
      const minRating = +(ratingRds.find(r => r.checked)?.value || 0);

      let visible = 0;
      const toShow = [], toHide = [];
      cards.forEach((c) => {
        const price    = +c.dataset.price;
        const rating   = +c.dataset.rating;
        const types    = (c.dataset.types || "").split(/\s+/);
        const bucket   = timeBucket(c.dataset.departure);

        const okPrice  = price <= maxPrice;
        const okTime   = !activeTimes.length || activeTimes.includes(bucket);
        const okType   = !activeTypes.length || activeTypes.some(t => types.includes(t));
        const okRating = rating >= minRating;
        const show = okPrice && okTime && okType && okRating;
        if (show) { toShow.push(c); visible++; } else { toHide.push(c); }
      });

      // Animate out hidden
      toHide.forEach(c => {
        if (!c.classList.contains("is-hidden")) {
          c.classList.add("is-leaving");
          setTimeout(() => { c.classList.add("is-hidden"); c.classList.remove("is-leaving"); }, 300);
        }
      });
      // Animate in shown
      toShow.forEach(c => {
        if (c.classList.contains("is-hidden") || c.classList.contains("is-leaving")) {
          c.classList.remove("is-hidden", "is-leaving");
          c.classList.remove("is-entering"); void c.offsetWidth;
          c.classList.add("is-entering");
          setTimeout(() => c.classList.remove("is-entering"), 450);
        }
      });

      countEls.forEach(e => e.textContent = visible);
      if (emptyEl) emptyEl.hidden = visible !== 0;
    }

    function applySort() {
      const mode = sortSel?.value || "departure";
      const sorted = cards.slice().sort((a, b) => {
        switch (mode) {
          case "price-asc":    return +a.dataset.price - +b.dataset.price;
          case "price-desc":   return +b.dataset.price - +a.dataset.price;
          case "rating-desc":  return +b.dataset.rating - +a.dataset.rating;
          case "duration-asc": return +a.dataset.duration - +b.dataset.duration;
          default:             return a.dataset.departure.localeCompare(b.dataset.departure);
        }
      });
      busList.classList.add("is-loading");
      setTimeout(() => {
        sorted.forEach(c => busList.appendChild(c));
        busList.classList.remove("is-loading");
        sorted.forEach((c, i) => {
          if (c.classList.contains("is-hidden")) return;
          c.classList.remove("is-entering"); void c.offsetWidth;
          c.style.animationDelay = (i * 30) + "ms";
          c.classList.add("is-entering");
          setTimeout(() => { c.classList.remove("is-entering"); c.style.animationDelay = ""; }, 500 + i*30);
        });
      }, 200);
    }

    /* ---- Skeleton helpers for filter/sort transitions ---- */
    const toolbar = document.querySelector(".results-toolbar");
    const skeletonHTML = `
      <div class="bus-card-skeleton">
        <div>
          <div class="skeleton sk-line lg"></div>
          <div class="skeleton sk-line md"></div>
          <div class="skeleton sk-line sm"></div>
        </div>
        <div>
          <div class="skeleton sk-block"></div>
        </div>
        <div>
          <div class="skeleton sk-line lg"></div>
          <div class="skeleton sk-line sm"></div>
          <div class="skeleton sk-btn"></div>
        </div>
      </div>`;

    let pendingTimer = null;
    function withTransition(fn, delay = 280) {
      if (pendingTimer) clearTimeout(pendingTimer);
      busList.classList.add("is-loading");
      toolbar?.classList.add("is-updating");
      // Inject 3 skeleton placeholders at the top to convey work
      const sk = document.createElement("div");
      sk.setAttribute("data-skeletons", "");
      sk.innerHTML = skeletonHTML.repeat(3);
      busList.prepend(sk);
      pendingTimer = setTimeout(() => {
        sk.remove();
        fn();
        busList.classList.remove("is-loading");
        toolbar?.classList.remove("is-updating");
      }, delay);
    }

    const debouncedFilter = (() => {
      let t; return () => { clearTimeout(t); t = setTimeout(() => withTransition(applyFilters), 120); };
    })();

    rangeEl?.addEventListener("input", () => {
      if (rangeOut) rangeOut.textContent = "₹" + (+rangeEl.value).toLocaleString("en-IN");
      debouncedFilter();
    });
    if (rangeEl && rangeOut) rangeOut.textContent = "₹" + (+rangeEl.value).toLocaleString("en-IN");

    timePills.forEach(p => p.addEventListener("click", () => { p.classList.toggle("active"); withTransition(applyFilters); }));
    typeBoxes.forEach(c => c.addEventListener("change", () => withTransition(applyFilters)));
    ratingRds.forEach(r => r.addEventListener("change", () => withTransition(applyFilters)));
    sortSel?.addEventListener("change", () => withTransition(applySort, 320));

    $$("[data-filter-clear]").forEach(b => b.addEventListener("click", (e) => {
      e.preventDefault();
      timePills.forEach(p => p.classList.remove("active"));
      typeBoxes.forEach(c => c.checked = false);
      ratingRds.forEach(r => r.checked = (r.value === "0"));
      if (rangeEl) { rangeEl.value = rangeEl.max; if (rangeOut) rangeOut.textContent = "₹" + (+rangeEl.value).toLocaleString("en-IN"); }
      withTransition(applyFilters);
    }));

    applyFilters();
  }

  /* ============== Seat selection ============== */
  const seatGrids = $$("[data-seat-grid]");
  if (seatGrids.length) initSeats();

  function initSeats() {
    const MAX_SEATS  = 6;
    const TAX_RATE   = 0.05;

    /* ---------- Resolve base price from listing context ---------- */
    const params = new URLSearchParams(window.location.search);
    let ctx = {};
    try { ctx = JSON.parse(localStorage.getItem("rb_bus_ctx") || "{}"); } catch (_) {}
    const basePrice = Math.max(
      +params.get("base") || 0,
      +ctx.basePrice || 0,
      0
    ) || 1199; // fallback if user landed directly

    // Tier premiums on top of base. Seat price NEVER goes below base.
    const TIERS = {
      standard: { label: "Standard",        delta: 0   },
      window:   { label: "Window / front",  delta: 100 },
      upper:    { label: "Upper deck",      delta: 200 },
      premium:  { label: "Premium upper",   delta: 300 },
    };
    const priceFor = (tier) => basePrice + (TIERS[tier]?.delta || 0);

    /* ---------- Classify each seat into a tier, then write derived price ---------- */
    const seatGridEls = $$("[data-seat-grid]");
    seatGridEls.forEach((grid, gridIdx) => {
      const isUpper = gridIdx > 0 || /upper/i.test(grid.previousElementSibling?.textContent || "");
      const seatsInGrid = $$(".seat", grid);
      // Group into rows of 4 seats (matches the 2+aisle+2 layout)
      const rows = [];
      let row = [];
      seatsInGrid.forEach((s) => {
        row.push(s);
        if (row.length === 4) { rows.push(row); row = []; }
      });
      if (row.length) rows.push(row);

      rows.forEach((r, rIdx) => {
        const lastTwoRows = rIdx >= rows.length - 2;
        r.forEach((seat, idx) => {
          let tier;
          if (isUpper) {
            tier = lastTwoRows ? "premium" : "upper";
          } else {
            // window seats = first & last in row
            const isWindow = idx === 0 || idx === r.length - 1;
            tier = isWindow && lastTwoRows ? "window"
                 : isWindow ? "window"
                 : "standard";
            // earlier rows: keep window for edges, standard for middle
            if (!lastTwoRows && !isWindow) tier = "standard";
          }
          const price = priceFor(tier);
          seat.dataset.tier  = tier;
          seat.dataset.price = String(price);
          seat.title = `${seat.dataset.seat} · ${TIERS[tier].label} · ₹${price}`;
        });
      });
    });

    /* ---------- Update the price-tiers legend with derived values ---------- */
    const tiersBox = document.querySelector(".price-tiers");
    if (tiersBox) {
      tiersBox.innerHTML = Object.entries(TIERS)
        .map(([k, t]) => `<span><b>${fmt(priceFor(k))}</b> ${t.label}</span>`)
        .join("");
    }

    /* ---------- Update header summary with operator from context ---------- */
    if (ctx.operator) {
      const routeEl = document.querySelector(".search-summary .route span");
      if (routeEl) routeEl.textContent = ctx.operator;
    }
    if (ctx.type) {
      const metaEl = document.querySelector(".search-summary .meta");
      if (metaEl) metaEl.textContent = `${ctx.type}${ctx.departure ? " · " + ctx.departure : ""}`;
    }

    const seats      = $$(".seat");
    const countEl    = $("[data-seat-count]");
    const pluralEl   = $("[data-plural]");
    const priceEl    = $("[data-seat-price]");
    const taxEl      = $("[data-seat-tax]");
    const totalEl    = $("[data-seat-total]");
    const listEl     = $("[data-selected-list]");
    const msgEl      = $("[data-seat-msg]");
    const continueBtn = $("[data-continue-btn]");

    function showMsg(text, type = "info") {
      if (!msgEl) return;
      if (!text) { msgEl.hidden = true; msgEl.textContent = ""; msgEl.className = "alert-msg"; return; }
      msgEl.hidden = false;
      msgEl.className = "alert-msg alert-" + type;
      msgEl.innerHTML = `<i class="bi bi-${type === "danger" ? "exclamation-triangle-fill" : "info-circle-fill"}"></i> ${text}`;
    }

    function refresh() {
      const selected = $$(".seat.selected");
      const count = selected.length;
      const base  = selected.reduce((s, el) => s + (+el.dataset.price || 0), 0);
      const tax   = base * TAX_RATE;
      const total = base + tax;

      if (countEl)  countEl.textContent = count;
      if (pluralEl) pluralEl.textContent = count === 1 ? "" : "s";
      if (priceEl)  priceEl.textContent = fmt(base);
      if (taxEl)    taxEl.textContent   = fmt(tax);
      if (totalEl)  totalEl.textContent = fmt(total);

      if (listEl) {
        if (!count) {
          listEl.innerHTML = `
            <div class="empty-selected">
              <i class="bi bi-ticket-perforated"></i>
              <p>No seats selected yet. Pick a seat from the layout to see your fare.</p>
            </div>`;
        } else {
          listEl.innerHTML = selected.map(el => `
            <div class="sel-row">
              <span class="sel-chip">${el.dataset.seat}</span>
              <span class="sel-meta">Seat ${el.dataset.seat}</span>
              <span class="sel-price">${fmt(+el.dataset.price)}</span>
            </div>`).join("");
        }
      }

      if (continueBtn) {
        const enabled = count > 0;
        continueBtn.style.opacity = enabled ? "" : ".6";
        continueBtn.style.pointerEvents = enabled ? "" : "none";
        continueBtn.setAttribute("aria-disabled", String(!enabled));
      }

      if (count === 0) showMsg("Select at least 1 seat to continue.", "info");
      else if (count > MAX_SEATS) showMsg(`You can book a maximum of ${MAX_SEATS} seats per transaction.`, "danger");
      else showMsg("");
    }

    seats.forEach(seat => {
      seat.addEventListener("click", () => {
        if (seat.classList.contains("booked")) {
          showMsg("This seat is already booked. Please pick another.", "danger");
          seat.classList.add("shake");
          setTimeout(() => seat.classList.remove("shake"), 400);
          return;
        }
        const isSelected = seat.classList.contains("selected");
        if (!isSelected && $$(".seat.selected").length >= MAX_SEATS) {
          showMsg(`You can select up to ${MAX_SEATS} seats only.`, "danger");
          return;
        }
        seat.classList.toggle("selected");
        // bump total
        const totalRow = document.querySelector(".summary-row.total");
        if (totalRow) { totalRow.classList.remove("bump"); void totalRow.offsetWidth; totalRow.classList.add("bump"); }
        refresh();
      });
    });

    // Persist selection for booking page
    if (continueBtn) {
      continueBtn.addEventListener("click", (e) => {
        const selected = $$(".seat.selected").map(el => ({ seat: el.dataset.seat, price: +el.dataset.price }));
        if (!selected.length) { e.preventDefault(); return; }
        try { sessionStorage.setItem("rb_selected_seats", JSON.stringify(selected)); } catch (_) {}
      });
    }

    refresh();
  }

  /* ============== Boarding/Dropping points ============== */
  $$("[data-points]").forEach((group) => {
    group.querySelectorAll(".point").forEach((p) => {
      p.addEventListener("click", () => {
        group.querySelectorAll(".point").forEach((x) => x.classList.remove("active"));
        p.classList.add("active");
      });
    });
  });

  /* ============== Payment tabs ============== */
  const payTabs = $$("[data-pay-tab]");
  payTabs.forEach((t) => {
    t.addEventListener("click", () => {
      payTabs.forEach(x => x.classList.remove("active"));
      $$("[data-pay-pane]").forEach(x => x.classList.remove("active"));
      t.classList.add("active");
      const target = document.querySelector(`[data-pay-pane="${t.dataset.payTab}"]`);
      if (target) target.classList.add("active");
    });
  });

  /* ============== Auth tabs ============== */
  const authTabs = $$("[data-auth-tab]");
  authTabs.forEach((t) => {
    t.addEventListener("click", () => {
      authTabs.forEach(x => x.classList.remove("active"));
      t.classList.add("active");
      const which = t.dataset.authTab;
      $$("[data-auth-pane]").forEach(p => p.classList.toggle("hidden", p.dataset.authPane !== which));
      const title = $("[data-auth-title]"), sub = $("[data-auth-sub]");
      if (title) title.textContent = which === "login" ? "Welcome back" : "Create account";
      if (sub)   sub.textContent   = which === "login" ? "Sign in to continue your journey" : "Start booking buses in seconds";
    });
  });

  /* ============== Form validation w/ loading ============== */
  $$("form[data-validate]").forEach((form) => {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      let ok = true;
      form.querySelectorAll("[required]").forEach((el) => {
        const valid = !!el.value.trim();
        el.classList.toggle("is-invalid", !valid);
        if (!valid) ok = false;
      });
      if (!ok) return;
      const btn = form.querySelector('button[type="submit"], .btn-primary');
      if (btn) {
        btn.classList.add("is-loading");
        btn.setAttribute("disabled", "true");
      }
      const next = form.dataset.next;
      setTimeout(() => { if (next) window.location.href = next; }, 600);
    });
  });

  /* ============== Autocomplete (city / bus stops) ============== */
  const SUGGESTIONS = [
    { name: "Bengaluru", type: "City", state: "Karnataka" },
    { name: "Hyderabad", type: "City", state: "Telangana" },
    { name: "Mumbai", type: "City", state: "Maharashtra" },
    { name: "Pune", type: "City", state: "Maharashtra" },
    { name: "Delhi", type: "City", state: "Delhi" },
    { name: "Jaipur", type: "City", state: "Rajasthan" },
    { name: "Chennai", type: "City", state: "Tamil Nadu" },
    { name: "Coimbatore", type: "City", state: "Tamil Nadu" },
    { name: "Ahmedabad", type: "City", state: "Gujarat" },
    { name: "Surat", type: "City", state: "Gujarat" },
    { name: "Udaipur", type: "City", state: "Rajasthan" },
    { name: "Kolkata", type: "City", state: "West Bengal" },
    { name: "Bhubaneswar", type: "City", state: "Odisha" },
    { name: "Vijayawada", type: "City", state: "Andhra Pradesh" },
    { name: "Visakhapatnam", type: "City", state: "Andhra Pradesh" },
    { name: "Goa", type: "City", state: "Goa" },
    { name: "Indore", type: "City", state: "Madhya Pradesh" },
    { name: "Nagpur", type: "City", state: "Maharashtra" },
    { name: "Lucknow", type: "City", state: "Uttar Pradesh" },
    { name: "Kochi", type: "City", state: "Kerala" },
    { name: "Trivandrum", type: "City", state: "Kerala" },
    { name: "Mysore", type: "City", state: "Karnataka" },
    { name: "Mangalore", type: "City", state: "Karnataka" },
    { name: "Majestic Bus Stand", type: "Bus Stop", state: "Bengaluru" },
    { name: "Madiwala Bus Stop", type: "Bus Stop", state: "Bengaluru" },
    { name: "Silk Board", type: "Bus Stop", state: "Bengaluru" },
    { name: "Electronic City Toll", type: "Bus Stop", state: "Bengaluru" },
    { name: "Satellite Bus Stand", type: "Bus Stop", state: "Ahmedabad" },
    { name: "Mehdipatnam", type: "Bus Stop", state: "Hyderabad" },
    { name: "Ameerpet", type: "Bus Stop", state: "Hyderabad" },
    { name: "Secunderabad", type: "Bus Stop", state: "Hyderabad" },
    { name: "Dadar Bus Stop", type: "Bus Stop", state: "Mumbai" },
    { name: "Borivali", type: "Bus Stop", state: "Mumbai" },
    { name: "Kashmere Gate ISBT", type: "Bus Stop", state: "Delhi" },
    { name: "Anand Vihar ISBT", type: "Bus Stop", state: "Delhi" }
  ];

  $$("[data-autocomplete]").forEach((input) => {
    const wrap = input.closest(".field") || input.parentElement;
    if (!wrap) return;
    if (getComputedStyle(wrap).position === "static") wrap.style.position = "relative";
    const pop = document.createElement("div");
    pop.className = "autocomplete-pop";
    wrap.appendChild(pop);
    let activeIdx = -1, current = [];

    function render(list) {
      current = list;
      activeIdx = -1;
      if (!list.length) {
        pop.innerHTML = `<div class="ac-empty">No matches found</div>`;
        return;
      }
      const cities = list.filter(x => x.type === "City");
      const stops  = list.filter(x => x.type === "Bus Stop");
      let html = "";
      if (cities.length) {
        html += `<div class="ac-group">Cities</div>` + cities.map((s, i) =>
          `<div class="ac-item" data-i="${list.indexOf(s)}"><i class="bi bi-geo-alt"></i><span class="ac-name">${s.name}</span><span class="ac-sub">${s.state}</span></div>`).join("");
      }
      if (stops.length) {
        html += `<div class="ac-group">Bus Stops</div>` + stops.map((s) =>
          `<div class="ac-item" data-i="${list.indexOf(s)}"><i class="bi bi-bus-front"></i><span class="ac-name">${s.name}</span><span class="ac-sub">${s.state}</span></div>`).join("");
      }
      pop.innerHTML = html;
      pop.querySelectorAll(".ac-item").forEach((el) => {
        el.addEventListener("mousedown", (e) => {
          e.preventDefault();
          input.value = current[+el.dataset.i].name;
          close();
        });
      });
    }
    function open() { pop.classList.add("open"); }
    function close() { pop.classList.remove("open"); }
    function setActive(i) {
      const items = pop.querySelectorAll(".ac-item");
      if (!items.length) return;
      activeIdx = (i + items.length) % items.length;
      items.forEach(x => x.classList.remove("active"));
      items[activeIdx].classList.add("active");
      items[activeIdx].scrollIntoView({ block: "nearest" });
    }

    input.addEventListener("input", () => {
      const q = input.value.trim().toLowerCase();
      if (q.length < 1) { close(); return; }
      const list = SUGGESTIONS.filter(s => s.name.toLowerCase().includes(q)).slice(0, 12);
      render(list);
      open();
    });
    input.addEventListener("focus", () => {
      const q = input.value.trim().toLowerCase();
      const list = q ? SUGGESTIONS.filter(s => s.name.toLowerCase().includes(q)).slice(0, 12)
                     : SUGGESTIONS.filter(s => s.type === "City").slice(0, 8);
      render(list); open();
    });
    input.addEventListener("blur", () => setTimeout(close, 120));
    input.addEventListener("keydown", (e) => {
      if (!pop.classList.contains("open")) return;
      const items = pop.querySelectorAll(".ac-item");
      if (e.key === "ArrowDown") { e.preventDefault(); setActive(activeIdx + 1); }
      else if (e.key === "ArrowUp") { e.preventDefault(); setActive(activeIdx - 1); }
      else if (e.key === "Enter") {
        if (activeIdx >= 0 && items[activeIdx]) {
          e.preventDefault();
          input.value = current[+items[activeIdx].dataset.i].name;
          close();
        }
      } else if (e.key === "Escape") { close(); }
    });
  });

  /* ============== Bookings tabs ============== */
  const bookingsTabs = $("[data-bookings-tabs]");
  if (bookingsTabs) {
    const cards = $$("[data-booking]");
    const counts = { all: cards.length, upcoming: 0, completed: 0, cancelled: 0 };
    cards.forEach(c => { counts[c.dataset.status] = (counts[c.dataset.status] || 0) + 1; });
    bookingsTabs.querySelectorAll(".sort-pill").forEach(btn => {
      const tab = btn.dataset.tab;
      if (counts[tab] != null) btn.innerHTML = `${btn.textContent.trim()} <span style="opacity:.6">(${counts[tab]})</span>`;
      btn.addEventListener("click", () => {
        bookingsTabs.querySelectorAll(".sort-pill").forEach(x => x.classList.remove("active"));
        btn.classList.add("active");
        cards.forEach(c => {
          const show = tab === "all" || c.dataset.status === tab;
          if (show) {
            c.classList.remove("is-hidden");
            c.style.animation = "none"; void c.offsetWidth; c.style.animation = "";
          } else {
            c.classList.add("is-hidden");
          }
        });
        const visible = cards.filter(c => !c.classList.contains("is-hidden")).length;
        let empty = document.querySelector("[data-bookings-empty]");
        if (!visible) {
          if (!empty) {
            empty = document.createElement("div");
            empty.className = "empty-state";
            empty.setAttribute("data-bookings-empty", "");
            empty.innerHTML = `<i class="bi bi-emoji-frown"></i><h4>No ${tab} bookings</h4><p>You don't have any ${tab} bookings right now.</p>`;
            cards[0].parentElement.appendChild(empty);
          } else { empty.hidden = false; empty.querySelector("h4").textContent = `No ${tab} bookings`; }
        } else if (empty) { empty.hidden = true; }
      });
    });
  }

  /* ============== Dynamic passenger forms ============== */
  const passengerList = $("[data-passenger-list]");
  if (passengerList) {
    let selected = [];
    try { selected = JSON.parse(sessionStorage.getItem("rb_selected_seats") || "[]"); } catch (_) {}
    let busCtx = {};
    try { busCtx = JSON.parse(localStorage.getItem("rb_bus_ctx") || "{}"); } catch (_) {}
    const fallbackBase = +busCtx.basePrice || 1199;
    if (!selected.length) selected = [{ seat: "L6", price: fallbackBase }, { seat: "L7", price: fallbackBase }];

    passengerList.innerHTML = selected.map((s, i) => `
      <div class="passenger-card">
        <div class="passenger-card-head">
          <strong>Passenger ${i + 1}</strong>
          <span class="seat-num">Seat ${s.seat} · ${fmt(s.price)}</span>
        </div>
        <div class="form-row">
          <div><label class="label">Full name</label><input class="input" name="p${i}_name" required placeholder="As per ID" /></div>
          <div><label class="label">Age</label><input class="input" type="number" name="p${i}_age" required min="1" max="120" placeholder="28" /></div>
          <div>
            <label class="label">Gender</label>
            <select class="input" name="p${i}_gender" required><option value="">Select</option><option>Male</option><option>Female</option><option>Other</option></select>
          </div>
        </div>
      </div>`).join("");

    // Update summary if present
    const base = selected.reduce((s, x) => s + x.price, 0);
    const tax  = Math.round(base * 0.05);
    const discount = 250;
    const total = base + tax - discount;
    const summaryRows = document.querySelectorAll(".summary-row");
    if (summaryRows.length) {
      summaryRows.forEach(row => {
        const label = row.firstElementChild?.textContent || "";
        const v = row.querySelector(".v") || row.lastElementChild;
        if (/Base fare/i.test(label)) { row.firstElementChild.innerHTML = `Base fare (${selected.length} seat${selected.length>1?'s':''})`; v.textContent = fmt(base); }
        else if (/Taxes/i.test(label)) v.textContent = fmt(tax);
        else if (/Discount/i.test(label)) v.textContent = "−" + fmt(discount);
        else if (row.classList.contains("total")) v.textContent = fmt(total);
      });
    }
    // Update seats list in summary text "Seats L6, L7"
    document.querySelectorAll("div").forEach(d => {
      if (/^Volvo A\/C Sleeper/i.test(d.textContent || "") && d.textContent.includes("Seats")) {
        d.innerHTML = d.innerHTML.replace(/Seats[^<]*/i, "Seats " + selected.map(s => s.seat).join(", "));
      }
    });
  }

})();
