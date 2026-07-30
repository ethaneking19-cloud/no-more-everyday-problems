# No More Everyday Problems

**Practical guides for the everyday annoyances that should be easier to solve.**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Netlify Status](https://api.netlify.com/api/v1/badges/placeholder/deploy-status)](https://app.netlify.com/sites/placeholder/deploys)

---

## 🚀 What This Is

No More Everyday Problems is a content-first affiliate site that helps people solve the small daily frustrations everyone deals with: lost keys, dead phone batteries, messy cars, pet hair everywhere, and more.

Every guide follows the same proven formula:
1. **One clear problem** — no fluff
2. **Top picks first** — the best solution up front
3. **Why it happens** — a quick, honest explanation
4. **More options** — alternatives for different budgets
5. **Comparison table** — side-by-side to help decide

---

## 📦 10 Complete Guides

| Problem | Page | Category |
|---------|------|----------|
| 🔑 Lost Keys | [`no-more-lost-keys.html`](no-more-lost-keys.html) | Home & Living |
| 📦 Clutter | [`no-more-clutter.html`](no-more-clutter.html) | Home & Living |
| 📱 Dead Phone | [`no-more-dead-phone.html`](no-more-dead-phone.html) | Tech & Devices |
| 🔌 Tangled Cables | [`no-more-tangled-cables.html`](no-more-tangled-cables.html) | Tech & Devices |
| 📶 Slow WiFi | [`no-more-slow-wifi.html`](no-more-slow-wifi.html) | Tech & Devices |
| 🐕 Pet Hair | [`no-more-pet-hair.html`](no-more-pet-hair.html) | Home & Living |
| 🚗 Messy Car | [`no-more-messy-car.html`](no-more-messy-car.html) | Car & Travel |
| 👔 Wrinkled Clothes | [`no-more-wrinkled-clothes.html`](no-more-wrinkled-clothes.html) | Home & Living |
| ⏰ Snoozing Alarms | [`no-more-snoozing-alarms.html`](no-more-snoozing-alarms.html) | Tech & Devices |
| 👟 Smelly Shoes | [`no-more-smelly-shoes.html`](no-more-smelly-shoes.html) | Home & Living |

---

## 🎨 Design

- **Fonts:** Fraunces (headings) + Manrope (body) via Google Fonts
- **Palette:** Warm cream base with terracotta accents, sage greens, and teal highlights
- **Cards:** Frosted glass aesthetic with subtle radial gradients
- **Responsive:** Full mobile support down to 320px
- **Animations:** Subtle fade-up entry animations on scroll

---

## 🛠 Tech Stack

- **100% static** — HTML, CSS, vanilla JavaScript
- **Affiliate ready** — Amazon Associates links with dynamic tag swapping
- **Newsletter** — MailerLite embedded forms
- **Hosting** — GitHub Pages or Netlify (netlify.toml included)
- **SEO** — JSON-LD structured data, Open Graph, Twitter Cards, sitemap.xml, robots.txt

---

## 🏗 Project Structure

```
├── index.html                    # Homepage with quiz + hero + problem grid
├── no-more-*.html                # 10 individual problem guides
├── privacy.html                  # Privacy policy + affiliate disclosure
├── terms.html                    # Terms of service
├── styles.css                    # All styles (no framework)
├── app.js                        # Quiz, hero preview, toast notifications, back-to-top
├── affiliate.js                  # Amazon Associates tag manager
├── images/                       # All product photos and illustrations
│   └── favicon.svg               # Brand favicon
├── robots.txt                    # SEO
├── sitemap.xml                   # SEO
└── netlify.toml                  # Netlify deployment config
```

---

## 🚦 Quick Start

```bash
# Clone the repo
git clone https://github.com/ethaneking19-cloud/no-more-everyday-problems.git

# Open in browser (static site - no build step)
open index.html
```

Or serve locally:
```bash
npx serve .
```

---

## 🔗 Affiliate Setup

All Amazon links use the placeholder tag `YOURID-20`. To add your real Amazon Associates tag:

```js
// In browser console, or add to affiliate.js:
NMEP_Affiliate.setTag("your-tag-20");
```

Or set it permanently in `affiliate.js` by changing `DEFAULT_TAG`.

---

## 📧 Newsletter

The site uses MailerLite for email capture. Update the MailerLite account ID and form ID in each HTML file to connect your own account.

---

## 📄 License

MIT — use it, modify it, build on it.

---

## ✨ Author

Built by [@ethaneking19-cloud](https://github.com/ethaneking19-cloud)
