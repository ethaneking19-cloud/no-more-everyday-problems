"""
No More Everyday Problems - Related Articles Updater
=====================================================
Usage: python3 update-related.py

Automatically regenerates "You might also like" sections on all
article pages based on the app.js featuredItems data.
No manual editing needed — just run this after adding new pages.
"""

import os, re

# Read all existing pages from directory
pages = sorted([f for f in os.listdir(".") if f.startswith("no-more-") and f.endswith(".html")])

# Define related article mappings (each page links to 3 others)
# Key: page filename, Value: list of (icon, title, desc, href)
# Start with known mappings, then auto-fill new pages

RELATED = {
    'no-more-lost-keys.html': [
        ('🔑', 'No More Clutter', 'Storage tools and tidy-home habits that make a room feel calmer fast.', 'no-more-clutter.html'),
        ('📱', 'No More Dead Phone Battery', 'Portable chargers, fast chargers, and simple ways to stay powered.', 'no-more-dead-phone.html'),
        ('🚗', 'No More Messy Car', 'Organizers, bins, and add-ons that make the whole car feel cleaner.', 'no-more-messy-car.html'),
    ],
    'no-more-clutter.html': [
        ('🔑', 'No More Lost Keys', 'Smart trackers, key holders, and ways to stop the daily scramble.', 'no-more-lost-keys.html'),
        ('🔌', 'No More Tangled Cables', 'Clips, ties, and boxes that keep desk wires organized.', 'no-more-tangled-cables.html'),
        ('🐕', 'No More Pet Hair Everywhere', 'Better vacuums, rollers, and routines for cleaner furniture.', 'no-more-pet-hair.html'),
    ],
    'no-more-dead-phone.html': [
        ('🔌', 'No More Tangled Cables', 'Clips, ties, and boxes that keep desk wires and chargers organized.', 'no-more-tangled-cables.html'),
        ('📶', 'No More Slow WiFi', 'Smarter placement, mesh systems, and fixes for weak rooms.', 'no-more-slow-wifi.html'),
        ('⏰', 'No More Snoozing Alarms', 'Sunrise light clocks and wheel alarms that stop snooze addiction.', 'no-more-snoozing-alarms.html'),
    ],
    'no-more-slow-wifi.html': [
        ('📱', 'No More Dead Phone Battery', 'Portable chargers, fast chargers, and simple ways to stay powered.', 'no-more-dead-phone.html'),
        ('🔌', 'No More Tangled Cables', 'Clips, ties, and boxes that keep desk wires organized.', 'no-more-tangled-cables.html'),
        ('⏰', 'No More Snoozing Alarms', 'Sunrise light clocks and wheel alarms that stop snooze addiction.', 'no-more-snoozing-alarms.html'),
    ],
    'no-more-pet-hair.html': [
        ('🚗', 'No More Messy Car', 'Organizers, bins, and add-ons that make the whole car feel cleaner.', 'no-more-messy-car.html'),
        ('📦', 'No More Clutter', 'Storage tools and tidy-home habits for a calmer room.', 'no-more-clutter.html'),
        ('👟', 'No More Smelly Shoes', 'Bamboo charcoal bags and UV dryers that eliminate odor.', 'no-more-smelly-shoes.html'),
    ],
    'no-more-messy-car.html': [
        ('🐕', 'No More Pet Hair Everywhere', 'Better vacuums, rollers, and routines for cleaner furniture.', 'no-more-pet-hair.html'),
        ('🔑', 'No More Lost Keys', 'Smart trackers, key holders, and ways to stop the daily scramble.', 'no-more-lost-keys.html'),
        ('📦', 'No More Clutter', 'Storage tools and tidy-home habits for a calmer room.', 'no-more-clutter.html'),
    ],
    'no-more-tangled-cables.html': [
        ('📱', 'No More Dead Phone Battery', 'Portable chargers, fast chargers, and simple ways to stay powered.', 'no-more-dead-phone.html'),
        ('📶', 'No More Slow WiFi', 'Smarter placement, mesh systems, and fixes for weak rooms.', 'no-more-slow-wifi.html'),
        ('📦', 'No More Clutter', 'Storage tools and tidy-home habits for a calmer room.', 'no-more-clutter.html'),
    ],
    'no-more-wrinkled-clothes.html': [
        ('👟', 'No More Smelly Shoes', 'Bamboo charcoal bags and UV dryers that eliminate odor.', 'no-more-smelly-shoes.html'),
        ('📦', 'No More Clutter', 'Storage tools and tidy-home habits for a calmer room.', 'no-more-clutter.html'),
        ('⏰', 'No More Snoozing Alarms', 'Sunrise light clocks and wheel alarms that stop snooze addiction.', 'no-more-snoozing-alarms.html'),
    ],
    'no-more-snoozing-alarms.html': [
        ('📱', 'No More Dead Phone Battery', 'Portable chargers, fast chargers, and simple ways to stay powered.', 'no-more-dead-phone.html'),
        ('📶', 'No More Slow WiFi', 'Smarter placement, mesh systems, and fixes for weak rooms.', 'no-more-slow-wifi.html'),
        ('👔', 'No More Wrinkled Clothes', 'Portable steamers and sprays for smooth outfits in 2 minutes.', 'no-more-wrinkled-clothes.html'),
    ],
    'no-more-smelly-shoes.html': [
        ('👔', 'No More Wrinkled Clothes', 'Portable steamers and sprays for smooth outfits in 2 minutes.', 'no-more-wrinkled-clothes.html'),
        ('🐕', 'No More Pet Hair Everywhere', 'Better vacuums, rollers, and routines for cleaner furniture.', 'no-more-pet-hair.html'),
        ('🚗', 'No More Messy Car', 'Organizers, bins, and add-ons that make the whole car feel cleaner.', 'no-more-messy-car.html'),
    ],
}

# For any new pages not in RELATED, generate default related articles
all_known = set(RELATED.keys())
for page in pages:
    if page not in all_known:
        print(f"  ℹ️  New page detected: {page} — using default related articles")
        # Pick 3 other pages (not itself)
        others = [p for p in pages if p != page][:3]
        icons = ['🔑', '📦', '📱']
        RELATED[page] = []
        for i, other in enumerate(others[:3]):
            # Extract title from filename
            name = other.replace('no-more-', '').replace('.html', '').replace('-', ' ').title()
            RELATED[page].append((icons[i % len(icons)], f'No More {name}', 'A practical fix for everyday life.', other))

# Update each page
updated = 0
for filename in pages:
    if filename not in RELATED:
        continue
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Build new related articles HTML
    cards = ''
    for icon, title, desc, href in RELATED[filename]:
        cards += f'''                <a class="related-card" href="{href}">
                  <span class="related-icon">{icon}</span>
                  <strong>{title}</strong>
                  <p class="muted">{desc}</p>
                </a>
'''
    
    new_related = f'''
            <section class="panel fade-up delay-1">
              <span class="eyebrow">Keep reading</span>
              <h2>You might also like</h2>
              <div class="related-grid">
{cards}              </div>
            </section>
'''
    
    # Find and replace the existing related articles section
    pattern = r'\n\s*<section class="panel fade-up delay-1">\s*<span class="eyebrow">Keep reading</span>.*?</section>'
    match = re.search(pattern, content, re.DOTALL)
    
    if match:
        content = content[:match.start()] + new_related + content[match.end():]
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        updated += 1
        print(f"  ✅ Updated related articles in {filename}")

print(f"\n✅ Done! Updated {updated} pages.")
