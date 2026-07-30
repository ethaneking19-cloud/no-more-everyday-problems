"""
No More Everyday Problems - Page Generator
===========================================
Usage: python3 new-page.py

This script generates a new article page from a config, adds it to the
homepage grid, registers it in app.js, and updates the sitemap.

Just fill in the CONFIG below and run!
"""

import os, json

# ============================================================
#  CONFIG — Fill this out for your new page
# ============================================================

CONFIG = {
    "slug": "no-more-stained-shirts",
    "title": "No More Stained Shirts",
    "problem_name": "Stained Shirts",
    "category": "home",           # home, tech, or car
    "icon": "👕",
    
    # Meta / SEO
    "description": "Practical ways to remove stubborn stains from shirts, including stain removers, pre-treaters, and easy laundry hacks.",
    "og_image": "images/stained_shirts_cover.jpg",
    
    # Hero section
    "eyebrow": "Laundry & Clothing Care",
    "h1": "No More Stained Shirts: 5 Fast Stain Removal Fixes",
    "lead": "Spills and splatters ruin favorite shirts fast. A powerful stain pre-treater and an enzyme-based spray can lift tough marks before they set permanently.",
    "chips": ["Quick Action Required", "Works on All Fabrics", "No Bleach Needed"],
    "cover_image": "images/stained_shirts_cover.jpg",
    "cover_alt": "Stain remover spray on a white shirt",
    
    # Start here section
    "start_h2": "If you only try one thing, get an enzyme stain remover spray.",
    "start_copy": 'The single most effective tool for stains is an <strong>Enzyme-Based Stain Remover Spray</strong>. It breaks down protein, oil, and tannin stains at the molecular level before they set.',
    "start_link": "https://www.amazon.com/s?k=enzyme+stain+remover+spray&tag=YOURID-20",
    
    # Best picks (2 products)
    "picks": [
        {
            "name": "OxiClean MaxForce Stain Remover Spray",
            "rank": "Best overall fix",
            "image": "images/stain_spray.jpg",
            "alt": "OxiClean stain remover spray bottle",
            "desc": "Best for everyday food, coffee, and grease stains that happen during meals.",
            "bullets": ["5-in-1 stain fighting power", "Works on set-in stains", "Safe for colors and whites"],
            "link": "https://www.amazon.com/s?k=oxiclean+maxforce+stain+remover&tag=YOURID-20"
        },
        {
            "name": "Shout Advanced Stain Remover Gel",
            "rank": "Best budget fix",
            "image": "images/shout_gel.jpg",
            "alt": "Shout stain remover gel bottle",
            "desc": "Thick gel formula that clings to fabric for deep penetration on tough grease and oil stains.",
            "bullets": ["Ultra-concentrated gel formula", "Brush applicator scrubs in", "Great for collar and cuff stains"],
            "link": "https://www.amazon.com/s?k=shout+advanced+stain+remover+gel&tag=YOURID-20"
        }
    ],
    
    # Why this problem sticks
    "why_h2": "Stains set permanently when they dry or get heated in the dryer.",
    "why_copy": "Most people toss stained clothes straight into the laundry hamper and forget about them for days. By the time the washing machine runs, the stain has already bonded to the fabric fibers.",
    
    # Callout
    "callout_title": "The 5-Minute Pre-Treat Rule",
    "callout_copy": "Treat every stain within 5 minutes of it happening. Even just running cold water through the back of the fabric immediately can prevent 80% of stains from becoming permanent.",
    
    # More great options (3 products)
    "more": [
        {
            "name": "Carbona Stain Devils Complete Kit",
            "desc": "A targeted 9-bottle kit where each formula tackles one specific stain type: ink, blood, rust, and more.",
            "image": "images/carbona_kit.jpg",
            "alt": "Carbona stain removal kit",
            "bullets": ["9 specialized formulas", "Targets specific stain types", "Includes treatment guide"],
            "link": "https://www.amazon.com/s?k=carbona+stain+devils+kit&tag=YOURID-20"
        },
        {
            "name": "Grandma's Secret Spot Remover",
            "desc": "A tiny bottle of concentrated spot cleaner that works miracles on oil-based stains and ring-around-the-collar.",
            "image": "images/grandma_spot.jpg",
            "alt": "Grandma's Secret spot remover bottle",
            "bullets": ["Concentrated formula", "Works on oil and grease", "Small bottle lasts months"],
            "link": "https://www.amazon.com/s?k=grandmas+secret+spot+remover&tag=YOURID-20"
        },
        {
            "name": "Tide To Go Instant Stain Remover Pen",
            "desc": "A pocket-sized pen that erases fresh stains on the spot before they have time to set.",
            "image": "images/tide_pen.jpg",
            "alt": "Tide To Go stain remover pen",
            "bullets": ["Fits in pocket or purse", "No water needed", "Works in under 60 seconds"],
            "link": "https://www.amazon.com/s?k=tide+to+go+stain+remover+pen&tag=YOURID-20"
        }
    ],
    
    # Recommendation
    "rec_title": "The best stain-fighting combo",
    "rec_copy": "Keep a spray bottle of OxiClean at home and a Tide pen in your bag for emergencies. That pair handles 95% of everyday stains.",
    "rec_link1": "https://www.amazon.com/s?k=oxiclean+maxforce+stain+remover&tag=YOURID-20",
    "rec_label1": "View Stain Spray",
    "rec_link2": "https://www.amazon.com/s?k=tide+to+go+stain+remover+pen&tag=YOURID-20",
    "rec_label2": "View Tide Pen",
    
    # Comparison table (4+ rows)
    "table_rows": [
        ["<a href=\"https://www.amazon.com/s?k=oxiclean+maxforce+stain+remover&tag=YOURID-20\" target=\"_blank\">OxiClean MaxForce</a>", "Everyday food stains", "Breaking down proteins & tannins", "5-in-1 cleaning power, safe on colors"],
        ["<a href=\"https://www.amazon.com/s?k=shout+advanced+gel&tag=YOURID-20\" target=\"_blank\">Shout Advanced Gel</a>", "Grease & oil stains", "Deep scrub penetration", "Brush applicator for tough marks"],
        ["<a href=\"https://www.amazon.com/s?k=carbona+stain+devils+kit&tag=YOURID-20\" target=\"_blank\">Carbona Stain Devils Kit</a>", "Specific tough stains", "Targeting ink, blood, rust individually", "9-bottle specialist formula set"],
        ["<a href=\"https://www.amazon.com/s?k=tide+to+go+pen&tag=YOURID-20\" target=\"_blank\">Tide To Go Pen</a>", "On-the-go emergencies", "Instant spot treatment anywhere", "Pocket size, no water needed"]
    ],
    
    # Related articles (3)
    "related": [
        ("👔", "No More Wrinkled Clothes", "Portable steamers and sprays for smooth outfits in 2 minutes.", "no-more-wrinkled-clothes.html"),
        ("📦", "No More Clutter", "Storage tools and tidy-home habits for a calmer room.", "no-more-clutter.html"),
        ("👟", "No More Smelly Shoes", "Bamboo charcoal bags and UV dryers that eliminate odor.", "no-more-smelly-shoes.html")
    ],
    
    # Homepage card data (for index.html + app.js)
    "card_image": "images/stained_shirts_cover.jpg",
    "card_alt": "Stain remover spray on shirt",
    "card_desc": "Enzyme sprays, pre-treaters, and spot pens that lift stains before they set.",
    "appjs": {
        "kicker": "Laundry lifesaver",
        "stat": "Kitchen & dining essential",
        "pair": "Stain Spray + Tide Pen",
        "audience": "Anyone who eats, drinks, or has kids",
        "whyItWins": "Saves favorite shirts from the trash."
    }
}

# ============================================================
#  GENERATOR — Don't edit below unless you know what you're doing
# ============================================================

def build_html(config):
    c = config
    
    # Build picks HTML
    picks_html = ""
    for p in c["picks"]:
        picks_html += f'''                <div class="pick-card">
                  <div class="pick-photo pick-photo-contain">
                    <img loading="lazy" src="{p['image']}" alt="{p['alt']}" />
                  </div>
                  <span class="pick-rank">{p['rank']}</span>
                  <strong>{p['name']}</strong>
                  <p class="muted">{p['desc']}</p>
                  <ul>
                    {''.join(f'<li>{b}</li>' for b in p['bullets'])}
                  </ul>
                  <a class="button button-primary" href="{p['link']}" target="_blank" rel="noreferrer">👉 Buy Now (See Today's Price)</a>
                </div>
'''
    
    # Build more options HTML
    more_html = ""
    for m in c["more"]:
        more_html += f'''                <article class="product-card">
                  <div class="pick-photo pick-photo-contain">
                    <img loading="lazy" src="{m['image']}" alt="{m['alt']}" />
                  </div>
                  <h3>{m['name']}</h3>
                  <p class="muted">{m['desc']}</p>
                  <ul>
                    {''.join(f'<li>{b}</li>' for b in m['bullets'])}
                  </ul>
                  <a class="button button-primary" href="{m['link']}" target="_blank" rel="noreferrer">👉 Buy Now (See Today's Price)</a>
                </article>
'''
    
    # Build chips
    chips_html = '\n'.join(f'                    <span class="chip{' chip-accent' if i==0 else ''}">{chip}</span>' for i, chip in enumerate(c["chips"]))
    
    # Build table rows
    table_html = '\n'.join(f'''                  <tr>
                    <td>{row[0]}</td>
                    <td>{row[1]}</td>
                    <td>{row[2]}</td>
                    <td>{row[3]}</td>
                  </tr>''' for row in c["table_rows"])
    
    # Build related cards
    related_html = ""
    for icon, title, desc, href in c["related"]:
        related_html += f'''                <a class="related-card" href="{href}">
                  <span class="related-icon">{icon}</span>
                  <strong>{title}</strong>
                  <p class="muted">{desc}</p>
                </a>
'''
    
    # Build the full page
    html = f'''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{c['title']} | No More Everyday Problems</title>
    <meta name="description" content="{c['description']}" />
    <link rel="stylesheet" href="styles.css" />
    <link rel="icon" type="image/svg+xml" href="images/favicon.svg" />
    <meta property="og:type" content="article" />
    <meta property="og:title" content="{c['title']}" />
    <meta property="og:description" content="{c['description']}" />
    <meta property="og:image" content="{c['og_image']}" />
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Article",
      "name": "{c['title']}",
      "description": "{c['description']}",
      "url": "https://nomoreeverydayproblems.com/{c['slug']}.html",
      "image": "https://nomoreeverydayproblems.com/{c['og_image']}",
      "author": {{ "@type": "Organization", "name": "No More Everyday Problems" }}
    }}
    </script>
    <!-- MailerLite Universal -->
    <script>
    (function(w,d,e,u,f,l,n){{w[f]=w[f]||function(){{(w[f].q=w[f].q||[])
    .push(arguments);}},l=d.createElement(e),l.async=1,l.src=u,
    n=d.getElementsByTagName(e)[0],n.parentNode.insertBefore(l,n);}})
    (window,document,'script','https://assets.mailerlite.com/js/universal.js','ml');
    ml('account', '2531427');
</script>
    <!-- End MailerLite Universal -->
  </head>
  <body>
    <div class="page-shell article-shell">
      <header class="site-header">
        <div class="container header-row">
          <a class="brand-mark" href="index.html">
            <img class="brand-logo" src="images/NoMoreLogo.jpg" alt="No More Everyday Problems logo" />
            <span class="brand-copy">
              <span>Simple fixes that work</span>
              <strong>No More Everyday Problems</strong>
            </span>
          </a>
          <nav class="site-nav" aria-label="Primary">
            <a href="index.html#popular-fixes">Popular Fixes</a>
            <a href="index.html#popular-fixes">All Fixes</a>
            <a href="index.html#newsletter">Newsletter</a>
          </nav>
        </div>
      </header>

      <main class="article-hero">
        <div class="container article-layout article-layout-wide">
          <div class="article-main">
            <section class="panel fade-up">
              <div class="article-cover">
                <div class="article-cover-copy">
                  <div class="breadcrumbs"><a href="index.html">Home</a> / {c['problem_name']}</div>
                  <span class="eyebrow">{c['eyebrow']}</span>
                  <h1 style="max-width: 13ch;">{c['h1']}</h1>
                  <p class="lead">{c['lead']}</p>
                  <div class="article-meta">
{chips_html}
                  </div>
                  <div class="disclosure">
                    Some links on this page may be affiliate links, which means the site may earn a commission if you buy through them at no extra cost to you.
                  </div>
                </div>
                <div class="cover-visual">
                  <img loading="lazy" src="{c['cover_image']}" alt="{c['cover_alt']}" />
                </div>
              </div>
            </section>

            <section class="panel fade-up delay-1">
              <span class="eyebrow">Start here</span>
              <h2>{c['start_h2']}</h2>
              <p class="article-copy">{c['start_copy']}</p>
              <div class="inline-actions">
                <a class="button button-primary" href="{c['start_link']}" target="_blank" rel="noreferrer">👉 Buy Now (See Today's Price)</a>
                <a class="button button-secondary" href="#comparison">See Comparison Table</a>
              </div>
            </section>

            <section class="panel fade-up delay-1">
              <span class="eyebrow">Best picks</span>
              <h2>The best products for {c['problem_name'].lower()}</h2>
              <div class="picks-banner">
{picks_html}              </div>
            </section>

            <section class="panel">
              <span class="eyebrow">Why this problem sticks</span>
              <h2>{c['why_h2']}</h2>
              <p class="article-copy">{c['why_copy']}</p>
            </section>

            <section class="callout">
              <h3 class="callout-title">{c['callout_title']}</h3>
              <p class="muted">{c['callout_copy']}</p>
            </section>

            <section class="panel">
              <span class="eyebrow">More great options</span>
              <h2>Other smart ways to handle {c['problem_name'].lower()}</h2>
              <div class="pick-grid">
{more_html}              </div>
            </section>

            <section class="callout">
              <span class="eyebrow">My recommendation</span>
              <h2>{c['rec_title']}</h2>
              <p class="article-copy">{c['rec_copy']}</p>
              <div class="inline-actions">
                <a class="button button-secondary" href="{c['rec_link1']}" target="_blank" rel="noreferrer">{c['rec_label1']}</a>
                <a class="button button-secondary" href="{c['rec_link2']}" target="_blank" rel="noreferrer">{c['rec_label2']}</a>
              </div>
            </section>

            <section class="compare-table-wrap" id="comparison">
              <span class="eyebrow">Compare the options</span>
              <h2>Which one is right for you?</h2>
              <table>
                <thead>
                  <tr><th>Product</th><th>Best for</th><th>What it helps with</th><th>Why people like it</th></tr>
                </thead>
                <tbody>
{table_html}
                </tbody>
              </table>
            </section>

            <section class="panel fade-up delay-1">
              <span class="eyebrow">Keep reading</span>
              <h2>You might also like</h2>
              <div class="related-grid">
{related_html}              </div>
            </section>

            <section class="newsletter">
              <div>
                <h2>Get 1 simple fix every week.</h2>
                <p class="section-copy">One useful idea, one quick recommendation, and one less everyday problem to deal with.</p>
              </div>
              <div class="newsletter-form">
                <div class="ml-embedded" data-form="0HCgMH"></div>
              </div>
            </section>
          </div>
        </div>
      </main>

      <footer class="footer-shell">
        <div class="container footer-card">
          <div class="footer-row">
            <div><strong>No More Everyday Problems</strong><p class="tiny">Practical guides for the everyday annoyances that should be easier to solve.</p></div>
            <div class="footer-links">
              <a href="index.html">Home</a>
              <a href="privacy.html">Privacy Policy</a>
              <a href="terms.html">Terms of Service</a>
            </div>
          </div>
          <p class="tiny" style="color: var(--muted); margin-bottom: 0.5rem;">As an Amazon Associate, we earn from qualifying purchases.</p>
          <p class="tiny">&copy; <span data-year></span> No More Everyday Problems.</p>
        </div>
      </footer>
    </div>
    <script src="affiliate.js"></script>
    <script src="app.js"></script>
  </body>
</html>
'''
    return html


def add_to_appjs(config):
    """Add the new topic to app.js featuredItems array."""
    c = config
    aj = c["appjs"]
    
    with open("app.js", "r", encoding="utf-8") as f:
        content = f.read()
    
    entry = f'''  {{
    key: "{c['problem_name'].lower().replace(' ', '-')}",
    title: "{c['title']}",
    kicker: "{aj['kicker']}",
    description: "{c['card_desc']}",
    href: "{c['slug']}.html",
    stat: "{aj['stat']}",
    pair: "{aj['pair']}",
    audience: "{aj['audience']}",
    whyItWins: "{aj['whyItWins']}",
    image: "{c['card_image']}",
    category: "{c['category']}"
  }}
];'''
    
    # Insert before the closing bracket of featuredItems
    content = content.replace("];\n\nconst previewTarget", entry + "\nconst previewTarget")
    
    with open("app.js", "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"  [OK] Added to app.js")


def add_to_index(config):
    """Add a new card to the index.html problem grid."""
    c = config
    
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()
    
    card = f'''\n              <a class="problem-card fade-up" href="{c['slug']}.html">
                <div class="card-photo">
                  <img loading="lazy" src="{c['card_image']}" alt="{c['card_alt']}" />
                </div>
                <strong>{c['title']}</strong>
                <p class="muted">{c['card_desc']}</p>
                <span class="card-link">Open the page</span>
              </a>\n'''
    
    # Insert before the closing </div> of problem-grid
    marker = '            </div>\n          </div>\n        </section>\n\n        <!-- Interactive Quick Problem Finder Quiz -->'
    content = content.replace(marker, card + '            ' + marker)
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"  [OK] Added to index.html problem grid")


def add_to_sitemap(config):
    """Add new page to sitemap.xml."""
    c = config
    
    with open("sitemap.xml", "r", encoding="utf-8") as f:
        content = f.read()
    
    entry = f'''  <url>
    <loc>https://nomoreeverydayproblems.com/{c['slug']}.html</loc>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>\n'''
    
    # Insert before closing </urlset>
    content = content.replace("</urlset>", entry + "</urlset>")
    
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"  [OK] Added to sitemap.xml")


# ============================================================
#  MAIN
# ============================================================

if __name__ == "__main__":
    c = CONFIG
    
    print(f"\n>>> Generating page: {c['title']}")
    print(f"   Slug: {c['slug']}.html")
    print(f"   Category: {c['category']}")
    print()
    
    # 1. Generate HTML page
    html = build_html(c)
    filename = f"{c['slug']}.html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  [OK] Created {filename}")
    
    # 2. Add to app.js
    add_to_appjs(c)
    
    # 3. Add card to index.html
    add_to_index(c)
    
    # 4. Update sitemap
    add_to_sitemap(c)
    
    print(f"\n[DONE] New page '{c['slug']}.html' is ready.")
    print(f"\nNext steps:")
    print(f"  1. Add product images to images/ folder")
    print(f"  2. Open {c['slug']}.html in your browser to preview")
    print(f"  3. Edit the page to customize product details")
    print(f"  4. Run 'git add -A && git commit && git push'")
