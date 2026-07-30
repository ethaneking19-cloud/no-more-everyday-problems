/**
 * Application Logic for "No More Everyday Problems"
 * 10 Complete Problem Guides with Interactive Filters & Local Persistences
 */

const featuredItems = [
  {
    key: "keys",
    title: "No More Lost Keys",
    kicker: "Fastest starter article",
    description: "A quick, practical guide built around trackers, key holders, and one easy routine that makes lost keys far less likely.",
    href: "no-more-lost-keys.html",
    stat: "Best starter topic",
    pair: "AirTag + Entryway Organizer",
    audience: "Busy people leaving home in a rush",
    whyItWins: "The fix is immediate and easy to apply.",
    image: "images/NoLostKeysHomeImage.jpg",
    category: "home"
  },
  {
    key: "clutter",
    title: "No More Clutter",
    kicker: "Best home-organizing angle",
    description: "A calmer-home guide with easy storage ideas, visible before-and-after payoff, and tools that are simple to keep using.",
    href: "no-more-clutter.html",
    stat: "High shareability",
    pair: "Clear bins + drawer dividers",
    audience: "People who want their home to feel calmer fast",
    whyItWins: "Storage upgrades make the transformation feel obvious.",
    image: "images/NoMoreClutterHomeImage.jpg",
    category: "home"
  },
  {
    key: "battery",
    title: "No More Dead Phone Battery",
    kicker: "Everyday tech frustration",
    description: "A straightforward mix of portable chargers, fast chargers, and backup habits that help you stay powered up all day.",
    href: "no-more-dead-phone.html",
    stat: "Broad audience fit",
    pair: "Portable charger + fast charger",
    audience: "Students, commuters, and travelers",
    whyItWins: "Everyone understands the pain immediately.",
    image: "images/DeadPhoneHomeImage.jpg",
    category: "tech"
  },
  {
    key: "cables",
    title: "No More Tangled Cables",
    kicker: "Desk & Charger organization",
    description: "Stop dealing with messy desk wires and tangled charger cords with simple cable clips and velcro ties.",
    href: "no-more-tangled-cables.html",
    stat: "Desk productivity boost",
    pair: "Cable clips + Velcro straps",
    audience: "Remote workers and gamers",
    whyItWins: "Instant clean look for your workspace.",
    image: "images/ExtraCableSet.jpg",
    category: "tech"
  },
  {
    key: "wifi",
    title: "No More Slow WiFi",
    kicker: "Higher-ticket upgrade category",
    description: "A simple guide to figuring out whether you need better placement, a mesh system, or a one-room extender.",
    href: "no-more-slow-wifi.html",
    stat: "Higher average order value",
    pair: "Mesh system + setup guide",
    audience: "Families and remote workers",
    whyItWins: "The buying intent is strong when the connection is bad.",
    image: "images/slow_wifi_mesh.jpg",
    category: "tech"
  },
  {
    key: "pet",
    title: "No More Pet Hair Everywhere",
    kicker: "Very viral-friendly",
    description: "A cleaner-home guide with easy pet-hair tools for couches, floors, clothing, and the spots fur seems to collect fastest.",
    href: "no-more-pet-hair.html",
    stat: "Best for viral demos",
    pair: "Pet vacuum + couch tool",
    audience: "Pet owners tired of constant cleanup",
    whyItWins: "People love seeing obvious before-and-after results.",
    image: "images/pet_hair_cover.jpg",
    category: "home"
  },
  {
    key: "car",
    title: "No More Messy Car",
    kicker: "Easy bundle angle",
    description: "A practical car-reset guide with organizers, bins, and small upgrades that keep everyday clutter from taking over.",
    href: "no-more-messy-car.html",
    stat: "Strong bundle potential",
    pair: "Seat organizer + trash bin",
    audience: "Parents, commuters, and rideshare drivers",
    whyItWins: "The fixes are affordable and easy to act on.",
    image: "images/messy_car_organizer.jpg",
    category: "car"
  },
  {
    key: "clothes",
    title: "No More Wrinkled Clothes",
    kicker: "Fast travel & morning fix",
    description: "Handheld steamers and anti-wrinkle sprays that get shirts smooth in under 2 minutes without an ironing board.",
    href: "no-more-wrinkled-clothes.html",
    stat: "Travel essential",
    pair: "Handheld Steamer + Fabric Spray",
    audience: "Travelers, professionals, and students",
    whyItWins: "Saves 15 minutes of tedious ironing.",
    image: "images/NoMoreWrinkledClothesHome.jpg",
    category: "home"
  },
  {
    key: "alarm",
    title: "No More Snoozing Alarms",
    kicker: "Wake up energized",
    description: "Sunrise simulation light clocks and runaway wheel alarms that stop snooze addiction and boost morning energy.",
    href: "no-more-snoozing-alarms.html",
    stat: "Habit transformer",
    pair: "Sunrise Clock + Wheel Alarm",
    audience: "Heavy sleepers and early risers",
    whyItWins: "Directly improves sleep quality and energy.",
    image: "images/sunrise_clock.jpg",
    category: "tech"
  },
  {
    key: "shoes",
    title: "No More Smelly Shoes",
    kicker: "Natural odor elimination",
    description: "Activated bamboo charcoal insert bags and UV dryers that kill shoe odor at the root without chemicals.",
    href: "no-more-smelly-shoes.html",
    stat: "Eco-friendly natural pick",
    pair: "Charcoal Bags + Cedar Inserts",
    audience: "Athletes, workers, and sneakerheads",
    whyItWins: "Reusable for up to 2 years.",
    image: "images/charcoal_bags.jpg",
    category: "home"
  }
];

const previewTarget = document.querySelector("[data-hero-preview]");
const topicButtons = document.querySelectorAll("[data-topic-trigger]");

const previewMarkup = (item) => `
  <div class="spotlight-shell fade-up">
    <div class="spotlight-shell-top">
      <div class="preview-photo">
        <img src="${item.image}" alt="${item.title}" />
      </div>
      <div>
        <span class="eyebrow">Featured Guide</span>
        <span class="spotlight-stat">${item.kicker}</span>
        <h2>${item.title}</h2>
        <p class="section-copy">${item.description}</p>
      </div>
    </div>
    <div class="chip-row">
      <span class="chip chip-accent">${item.stat}</span>
      <span class="chip">${item.pair}</span>
    </div>
    <div class="spotlight-meta">
      <div>
        <span>Best for</span>
        <strong>${item.audience}</strong>
      </div>
      <div>
        <span>Why it wins</span>
        <strong>${item.whyItWins}</strong>
      </div>
    </div>
    <div class="inline-actions">
      <a class="button button-primary" href="${item.href}">View Solutions Now</a>
      <a class="button button-ghost" href="index.html#popular-fixes">Browse All Fixes</a>
    </div>
  </div>
`;

const renderPreview = (key) => {
  if (!previewTarget) {
    return;
  }

  const item = featuredItems.find((entry) => entry.key === key) || featuredItems[0];
  previewTarget.innerHTML = previewMarkup(item);

  topicButtons.forEach((button) => {
    button.classList.toggle("is-active", button.dataset.topicTrigger === item.key);
  });
};

if (previewTarget) {
  renderPreview("keys");
}

topicButtons.forEach((button) => {
  button.addEventListener("click", () => {
    renderPreview(button.dataset.topicTrigger);
  });
});

// Feature target removed — no matching [data-featured-solution] element in HTML

/* Interactive Quick Problem Finder Quiz */
const initQuiz = () => {
  const quizFilterContainer = document.querySelector("[data-quiz-filters]");
  const quizResultContainer = document.querySelector("[data-quiz-results]");

  if (!quizFilterContainer || !quizResultContainer) return;

  const renderQuizResults = (category) => {
    const items = category === "all" 
      ? featuredItems 
      : featuredItems.filter(item => item.category === category);

    quizResultContainer.innerHTML = items.map(item => `
      <div class="quiz-result-card fade-up">
        <div class="quiz-card-header">
          <span class="badge-tag">${item.category.toUpperCase()}</span>
          <h3>${item.title}</h3>
        </div>
        <p>${item.description}</p>
        <div class="quiz-card-footer">
          <span class="chip">${item.stat}</span>
          <a class="button button-primary button-sm" href="${item.href}">Solve This Now →</a>
        </div>
      </div>
    `).join("");
  };

  renderQuizResults("all");

  quizFilterContainer.querySelectorAll("button").forEach(btn => {
    btn.addEventListener("click", () => {
      quizFilterContainer.querySelectorAll("button").forEach(b => b.classList.remove("is-active"));
      btn.classList.add("is-active");
      renderQuizResults(btn.dataset.quizCat);
    });
  });
};

initQuiz();

/* Newsletter forms with Toast Notification feedback */
const forms = document.querySelectorAll("[data-newsletter-form]");

const showToast = (message) => {
  let toast = document.querySelector(".toast-notification");
  if (!toast) {
    toast = document.createElement("div");
    toast.className = "toast-notification";
    document.body.appendChild(toast);
  }
  toast.textContent = message;
  toast.classList.add("show");
  setTimeout(() => {
    toast.classList.remove("show");
  }, 4000);
};

forms.forEach((form) => {
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    const emailInput = form.querySelector("input[type='email']");
    const email = emailInput ? emailInput.value : "";
    
    if (email) {
      const subs = JSON.parse(localStorage.getItem("nmep_subscribers") || "[]");
      subs.push({ email, date: new Date().toISOString() });
      localStorage.setItem("nmep_subscribers", JSON.stringify(subs));
    }

    showToast("🎉 You're subscribed to No More Everyday Problems!");
    
    const note = form.querySelector("[data-form-note]");
    if (note) {
      note.textContent = "Thank you! You'll receive our weekly practical fix digest.";
      note.classList.add("success-note");
    }
    form.reset();
  });
});

const yearTarget = document.querySelector("[data-year]");
if (yearTarget) {
  yearTarget.textContent = new Date().getFullYear();
}
