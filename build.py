#!/usr/bin/env python3
"""Generates the Alora C. Kane site. Four pages, one shared shell."""
import os, base64, json

SITE = "https://alorakanebooks.com/"
CSSV = 2

# Flip to True on the day the site goes live at alorakanebooks.com and rebuild.
# While False every page carries a noindex tag and robots.txt blocks crawlers,
# so the github.io preview address never gets into Google, and the "do not
# publish" draft note stays visible on the newsletter panel.
PUBLISHED = False

YOUTUBE = "https://www.youtube.com/@MidnightCrownStories"
SOCIAL_CARD = "assets/social-card.jpg"   # 1200x630, built from the crown avatar
BUILT = "2026-09-05"                     # sitemap lastmod; bump when content changes

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
 '  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
 '  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600&family='
 'Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">')

SHELVES = [
    ("index.html",             "all",      "Everything"),
    ("visual-audiobooks.html", "video",    "Visual audiobooks"),
    ("coloring-books.html",    "coloring", "Coloring books"),
    ("books.html",             "book",     "Books"),
]

# ---------------------------------------------------------------- the stories

STORIES = [
    {
        "slug": "masked-ball",
        "name": "The Masked Festival",
        "kicker": "Story one &middot; Medieval",
        "hook": "She thought he was no one. He thought she was nothing. They were both wrong.",
        "blurb": "Katrina goes to the masked festival to be no one for one night. "
                 "Then she tells the alpha king to move.",
        "art_alt": "A masked couple in a candlelit ballroom",
        "thumb_alt": "The Masked Festival thumbnail",
        "video": {"title": "He Went to a Masked Ball to Escape", "url": None, "status": "Publishing soon"},
        "book": {"url": None, "status": "Being written now", "cover": None},
        "coloring": {"url": None, "status": "In the works", "cover": None},
    },
    {
        "slug": "scentless-omega",
        "name": "The Scentless Omega",
        "kicker": "Story two &middot; Medieval",
        "hook": "Two kings would soon fight over her. The girl on the horse didn't know that yet.",
        "blurb": "Ruby rides into Valecrest to perform with her troupe, get paid, and be gone by "
                 "morning. The alpha king has other plans.",
        "art_alt": "A crowned alpha king and a dark haired woman face to face by candlelight",
        "thumb_alt": "The Scentless Omega thumbnail",
        "video": {"title": "She Rode Into the Alpha King's Court With No Scent", "url": None, "status": "Publishing soon"},
        "book": {"url": None, "status": "Planned", "cover": None},
        "coloring": {"url": None, "status": "Planned", "cover": None},
    },
]

ICONS = {
 "video": '<svg class="way-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 4.5a1 1 0 0 1 1.52-.85l13 7.5a1 1 0 0 1 0 1.7l-13 7.5A1 1 0 0 1 4 19.5z"/></svg>',
 "book": '<svg class="way-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12.6 1.6c.4 3-1.3 4.3-2.8 5.7C8 8.9 6.4 10.5 6.4 13.6a5.9 5.9 0 0 0 11.8 0c0-2.3-1-3.9-2-5.2-.3 1-.9 1.7-1.7 2 .5-2.6-.6-5.6-1.9-8.8z"/><path d="M12 14c1.3 1 1.9 2 1.9 3a1.9 1.9 0 0 1-3.8 0c0-1 .6-2 1.9-3z" fill="#33203a"/></svg>',
 "coloring": '<svg class="way-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M9.2 2.4h5.6a1 1 0 0 1 1 1v3.1H8.2V3.4a1 1 0 0 1 1-1z"/><path d="M8.2 8.1h7.6v9.3l-3.3 4.4a.6.6 0 0 1-1 0L8.2 17.4z"/></svg>',
}

# ---------------------------------------------------------------- shell

PERSON_LD = {
    "@type": "Person",
    "@id": SITE + "#alora",
    "name": "Alora C. Kane",
    "url": SITE,
    "image": SITE + SOCIAL_CARD,
    "jobTitle": "Author",
    "description": "Alora C. Kane writes alpha king and werewolf romance: fated mates, "
                   "rejected omegas and proud alpha males brought to their knees.",
    "email": "mailto:alora@alorakanebooks.com",
    "sameAs": [YOUTUBE],
}

def json_ld(obj):
    data = json.dumps(obj, indent=2, ensure_ascii=False).replace('</', '<\\/')
    return f'<script type="application/ld+json">\n{data}\n</script>'

def head(title, desc, canonical, ld=None):
    robots = ('  <meta name="robots" content="index, follow">' if PUBLISHED
              else '  <meta name="robots" content="noindex, nofollow">')
    ld_block = ("\n  " + "\n  ".join(json_ld(o) for o in ld)) if ld else ""
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="author" content="Alora C. Kane">
{robots}
  <link rel="canonical" href="{SITE}{canonical}">
  <link rel="icon" type="image/png" sizes="256x256" href="favicon.png">
  <link rel="icon" href="favicon.ico" sizes="any">
  <link rel="apple-touch-icon" href="apple-touch-icon.png">
  <meta name="theme-color" content="#241528">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{SITE}{canonical}">
  <meta property="og:site_name" content="Alora C. Kane">
  <meta property="og:locale" content="en_US">
  <meta property="og:image" content="{SITE}{SOCIAL_CARD}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="A gold crown with a ruby on plum velvet, and the name Alora C. Kane">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{SITE}{SOCIAL_CARD}">{ld_block}
  {FONTS}
  <link rel="stylesheet" href="css/style.css?v={CSSV}">
</head>
<body>

  <header class="site-header">
    <a class="wordmark" href="index.html">Alora C. Kane</a>
    <nav>
      <a href="index.html#stories">Stories</a>
      <a href="index.html#newsletter">Freebies</a>
      <a href="index.html#about">About</a>
      <a href="index.html#newsletter" class="nav-cta">Newsletter</a>
    </nav>
  </header>

  <main id="top">
'''

FOOTER = '''
  </main>

  <footer class="site-footer">
    <p class="footer-name">Alora C. Kane</p>
    <p>Contact: <a href="mailto:alora@alorakanebooks.com">alora@alorakanebooks.com</a></p>
    <p class="copyright">&copy; 2026 Alora C. Kane. All rights reserved.</p>
  </footer>

</body>
</html>
'''

def shelf_bar(current):
    out = ['      <div class="filter-bar" role="navigation" aria-label="Browse by kind">']
    for href, key, label in SHELVES:
        cls = "filter-chip active" if key == current else "filter-chip"
        aria = ' aria-current="page"' if key == current else ''
        out.append(f'        <a class="{cls}" href="{href}"{aria}>{label}</a>')
    out.append('      </div>')
    return "\n".join(out)

# ---------------------------------------------------------------- home

def img_size(rel):
    from PIL import Image
    with Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), rel)) as im:
        return im.size

def way_row(kind, label, note, url):
    icon = ICONS[kind]
    if url:
        inner = f'<span class="way-label">{label}</span> <a href="{url}" target="_blank" rel="noopener">{note}</a>'
        cls = "way ready"
    else:
        inner = f'<span class="way-label">{label}</span> <span class="way-note">{note}</span>'
        cls = "way pending"
    return (f'              <li class="{cls}">\n'
            f'                {icon}\n'
            f'                <span>{inner}</span>\n'
            f'              </li>')

def story_card(s):
    v, b, c = s["video"], s["book"], s["coloring"]
    lazy = "" if s is STORIES[0] else ' loading="lazy"'
    w, h = img_size(f'assets/stories/{s["slug"]}.jpg')
    rows = [
        way_row("video", "Watch it free",
                f'as <em>{v["title"]}</em> &middot; {v["status"].lower()}' if not v["url"]
                else f'as <em>{v["title"]}</em> on YouTube', v["url"]),
        way_row("book", "Read the longer version",
                b["status"].lower() if not b["url"] else "on Amazon", b["url"]),
        way_row("coloring", "Color it",
                c["status"].lower() if not c["url"] else "coloring book on Amazon", c["url"]),
    ]
    return f'''        <article class="story-card">
          <div class="story-art">
            <img src="assets/stories/{s["slug"]}.jpg" alt="{s["art_alt"]}" width="{w}" height="{h}"{lazy}>
          </div>
          <div class="story-body">
            <p class="story-kicker">{s["kicker"]}</p>
            <h3>{s["name"]}</h3>
            <p class="story-hook">{s["hook"]}</p>
            <p class="story-blurb">{s["blurb"]}</p>
            <ul class="ways">
{chr(10).join(rows)}
            </ul>
          </div>
        </article>'''

STUB = ('' if PUBLISHED else '        <p class="stub-note">Draft note: the form is live and wired to MailerLite. The coloring pages PDF does not exist yet, so do not publish this page.</p>')

NEWSLETTER = f'''
    <section id="newsletter" class="newsletter smoke">
      <div class="newsletter-panel">
        <h2>Free coloring pages</h2>
        <p class="offer">Join the list and I will send you a set of <strong>printable coloring pages</strong> from the Midnight Crown stories. These pages are not in the coloring books. They are only here.</p>
        <ul class="offer-list">
          <li>New stories the day they go live</li>
          <li>The books behind the stories</li>
          <li>The occasional freebie, like this one</li>
        </ul>
{STUB}
        <form class="signup" id="signup-form">
          <input type="email" id="ml-email" placeholder="your@email.com" aria-label="Email address" required>
          <button type="submit" class="button gold">Send my pages</button>
        </form>
        <p class="signup-status" id="ml-status" hidden></p>
        <p class="fine-print">Your privacy matters. Your email address will only be used to send you updates, story news, and the occasional freebie from me. I use a trusted email service to manage this securely. I will never sell or share your information, and you can unsubscribe at any time.</p>
      </div>
    </section>

    <section id="about" class="about">
      <div class="about-inner">
        <h2>About Alora</h2>
        <p>Alora C. Kane writes alpha king and werewolf romance. Fated mates, rejected omegas, secret heirs, and proud alpha males brought to their knees by their sassy, often omega, mates. These are romances, always, with the happy ending that is earned.</p>
        <p>The tales unfold in old-world kingdoms and in the modern day, where the old laws still hold. Every story is original, richly illustrated, and narrated like a fireside tale. Most run over an hour.</p>
        <p>Midnight Crown Stories is one author, not a studio. I write every story myself, then use AI tools to help edit, illustrate, and give each tale its voice. Care takes time, so uploads are rare and worth the wait.</p>
      </div>
    </section>
'''

SIGNUP_JS = '''
  <script>
    var f = document.getElementById('signup-form');
    if (f) {
      f.addEventListener('submit', async function (e) {
        e.preventDefault();
        var status = document.getElementById('ml-status');
        var email = document.getElementById('ml-email').value;
        status.hidden = false;
        status.textContent = 'Sending...';
        try {
          var res = await fetch('https://assets.mailerlite.com/jsonp/2617378/forms/197803070582687706/subscribe', {
            method: 'POST',
            body: new URLSearchParams({
              'fields[email]': email,
              'ml-submit': '1',
              'anticsrf': 'true'
            })
          });
          var data = await res.json();
          if (data.success) {
            f.hidden = true;
            status.textContent = 'Almost there. Check your inbox for a confirmation email, then your coloring pages are on their way.';
          } else {
            status.textContent = 'That did not go through. Check the address and try again.';
          }
        } catch (err) {
          status.textContent = 'Connection hiccup. Please try again in a moment.';
        }
      });
    }
  </script>
'''

HOME_TITLE = "Alora C. Kane | Alpha King and Werewolf Romance"
HOME_DESC = ("Alpha king and werewolf romance by Alora C. Kane. Free visual audiobooks on YouTube. "
             "Coloring books and the longer, spicier novels on Amazon.")

def build_home():
    ld = [
        {"@context": "https://schema.org", "@type": "WebSite", "@id": SITE + "#site",
         "url": SITE, "name": "Alora C. Kane",
         "description": HOME_DESC, "inLanguage": "en-US",
         "publisher": {"@id": SITE + "#alora"}},
        dict({"@context": "https://schema.org"}, **PERSON_LD),
    ]
    h = head(HOME_TITLE, HOME_DESC, "", ld)
    h += '''
    <section class="hero smoke">
      <h1>Alora C. Kane</h1>
      <p class="tagline">Old kingdoms and modern ones, where the old laws still hold and proud men are brought to their knees by strong women.</p>
      <p class="genres">Alpha king &middot; werewolf romance &middot; fated mates</p>
    </section>

    <section id="stories" class="stories smoke">
      <h2>Midnight Crown Stories</h2>
      <p class="section-intro">Full length stories, written by me, illustrated and narrated like a fireside tale. Watch them free on YouTube. Buy the coloring books and the spicier versions, where rather more happens.</p>

'''
    h += shelf_bar("all") + "\n\n      <div class=\"story-list\">\n\n"
    h += "\n\n".join(story_card(s) for s in STORIES)
    h += "\n\n      </div>\n    </section>\n"
    h += NEWSLETTER + FOOTER.replace("</body>", SIGNUP_JS + "</body>")
    return h

# ---------------------------------------------------------------- shelf pages

def tile(s, kind):
    d = s[kind]
    if kind == "video":
        img = f'<img src="assets/thumbs/{s["slug"]}.jpg" alt="{s["thumb_alt"]}">'
        shape, line = "wide", d["title"]
        cta, href = "Watch on YouTube", d["url"]
    else:
        cover = d.get("cover")
        img = (f'<img src="assets/covers/{cover}" alt="Cover of {s["name"]}">' if cover
               else f'<span>{s["name"]}</span>')
        shape = "tall"
        line = "Coloring book" if kind == "coloring" else "The longer version"
        cta, href = "Buy on Amazon", d["url"]
    empty = "" if (kind == "video" or d.get("cover")) else " empty"
    body = (f'<a class="button gold" href="{href}" target="_blank" rel="noopener">{cta}</a>'
            if href else f'<p class="p-status">{d["status"]}</p>')
    return f'''        <article class="product">
          <div class="p-cover {shape}{empty}">{img}</div>
          <h3>{s["name"]}</h3>
          <p class="p-line">{line}</p>
          {body}
        </article>'''

SHELF_COPY = {
 "video": ("Visual audiobooks",
           "Every story, narrated and illustrated, free on YouTube. Most run over an hour.",
           "Nothing is public yet. The channel opens once three stories are ready.",
           "Free visual audiobooks by Alora C. Kane on YouTube: alpha king and werewolf romance, "
           "illustrated and narrated, most over an hour long."),
 "coloring": ("Coloring books",
              "Printable coloring books drawn from the stories, on Amazon.",
              "The first coloring book is being drawn now.",
              "Printable alpha king and werewolf romance coloring books by Alora C. Kane, drawn "
              "from the Midnight Crown stories, on Amazon."),
 "book": ("Books",
          "The longer versions, where rather more happens.",
          "The first book is being written now.",
          "Alpha king and werewolf romance novels by Alora C. Kane on Amazon: the longer, "
          "spicier versions of the free YouTube stories."),
}

def build_shelf(filename, kind):
    title, intro, nothing, desc = SHELF_COPY[kind]
    live = [s for s in STORIES if (kind == "video" or s[kind].get("cover"))]
    ld = [{"@context": "https://schema.org", "@type": "CollectionPage",
           "url": SITE + filename, "name": title, "description": desc,
           "isPartOf": {"@id": SITE + "#site"}, "author": {"@id": SITE + "#alora"},
           "breadcrumb": {"@type": "BreadcrumbList", "itemListElement": [
               {"@type": "ListItem", "position": 1, "name": "Alora C. Kane", "item": SITE},
               {"@type": "ListItem", "position": 2, "name": title, "item": SITE + filename}]}}]
    h = head(f"{title} | Alora C. Kane", desc, filename, ld)
    h += f'''
    <section class="page-hero smoke">
      <h1>{title}</h1>
      <p class="tagline">{intro}</p>
    </section>

    <section class="stories smoke">
{shelf_bar(kind)}

'''
    if live:
        h += '      <div class="product-grid">\n\n'
        h += "\n\n".join(tile(s, kind) for s in live)
        h += '\n\n      </div>\n'
    else:
        h += f'''      <div class="shelf-empty">
        <p>{nothing}</p>
        <p class="shelf-empty-hint">Join the list and I will tell you the day it lands.</p>
        <a class="button gold" href="index.html#newsletter">Get the free coloring pages</a>
      </div>
'''
    h += '    </section>\n'
    h += FOOTER
    return h

# ---------------------------------------------------------------- write

def build_404():
    h = head("Page not found | Alora C. Kane", "That page is not here.", "404.html")
    h = h.replace('<meta name="robots" content="index, follow">', '<meta name="robots" content="noindex">')
    h += '''
    <section class="page-hero smoke">
      <h1>Not here</h1>
      <p class="tagline">That page does not exist, or it moved. The stories are still where they were.</p>
      <p><a class="button gold" href="/">Back to the stories</a></p>
    </section>
'''
    return h + FOOTER

def build_sitemap():
    rows = "".join(f"  <url><loc>{SITE}{'' if f == 'index.html' else f}</loc><lastmod>{BUILT}</lastmod></url>\n"
                   for f, _, _ in SHELVES)
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + rows + '</urlset>\n')

def build_robots():
    if PUBLISHED:
        return f"User-agent: *\nAllow: /\n\nSitemap: {SITE}sitemap.xml\n"
    return "User-agent: *\nDisallow: /\n"

def main():
    root = os.path.dirname(os.path.abspath(__file__))
    out = {"index.html": build_home(), "404.html": build_404(),
           "sitemap.xml": build_sitemap(), "robots.txt": build_robots()}
    for filename, kind, _ in SHELVES[1:]:
        out[filename] = build_shelf(filename, kind)
    for name, text in out.items():
        open(os.path.join(root, name), "w", encoding="utf8").write(text)
    print(("LIVE" if PUBLISHED else "PREVIEW, noindex") + " build: " + ", ".join(out))

if __name__ == "__main__":
    main()
