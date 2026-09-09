# Volo AI

**Never miss a call again.** Official website for Volo AI — the AI voice receptionist for UK businesses. Volo answers every call 24/7: books appointments, handles enquiries and FAQs, saves data to your database (Airtable, Google Sheets, Calendly, your CRM or any open-source tool) and emails you the full transcript.

- 📧 Email: `qureshidabeer92@gmail.com`
- 💬 WhatsApp: `+92 314 4781120` (all CTAs open WhatsApp with a prefilled message)
- 🇬🇧 Built for UK clients and customers · pricing in **£ GBP**
- ⏰ Volo answers 24/7 — your team still rings first, Volo only steps in after 5 seconds

---

## How it works

1. A customer calls your existing UK number.
2. Your team's phone rings. If a real person picks up within 5 seconds, the call is theirs.
3. If nobody answers, Volo picks up instantly — books the appointment, handles the enquiry or FAQ, saves it to your database and sends you the full transcript.

---

## Pricing

| Plan | Price | Notes |
|------|-------|-------|
| 7-day free trial | £0 | Full access, no card required |
| Monthly | £150/month | Cancel anytime |
| Annual | £1,620/year (£135/mo) | Save 10% (£180 off) |

---

## Project Structure

```
.
├── index.html                       # Single-page Volo AI marketing site
├── privacy-policy.html              # Legal
├── terms-and-conditions.html        # Legal
├── 404.html                         # Custom error page
├── styles.css                       # "Aurora" theme — premium dark + voice gradient
├── script.js                        # Animations, phone-call simulator, video lightbox + DEMO_VIDEOS config
├── robots.txt                       # SEO crawler rules
├── sitemap.xml                      # index + legal pages
├── validate.py                      # Branding / SEO / markup validator
├── scripts/make_og.py               # Generates assets/images/og-image.png (1200×630)
└── assets/
    ├── logo.svg                     # Volo AI logo
    ├── favicon.svg                  # Volo AI favicon
    └── images/og-image.png          # Social-share preview image
```

## Run locally

```bash
python3 -m http.server 8000
# open http://localhost:8000
```

## Adding your demo videos

Open `script.js` and paste your video URLs into the `DEMO_VIDEOS` object at the top:

```js
var DEMO_VIDEOS = {
    'live-call': 'https://www.youtube.com/watch?v=YOUR_ID',
    'setup-5min': '',
    'dashboard': '',
};
```

YouTube (including Shorts), Vimeo and Google Drive links are supported — videos play in a pop-up lightbox. Cards left as `''` show a "Demo coming soon" state and scroll to the CTA section when clicked.

## SEO checklist (already done)

- Unique title, meta description, keywords, canonical, Open Graph + Twitter card
- JSON-LD: `Organization`, `Product` (with pricing/offer data) and `WebSite` on the landing page
- Semantic HTML5, FAQ accordion mirrored as `FAQPage` structured data
- `sitemap.xml` lists all pages; `robots.txt` allows all crawlers
- Preconnected fonts, reduced-motion support, scroll-reveal animations

## Notes

- Canonical URLs, sitemap and JSON-LD use `https://voloai.uk/` — if your live domain differs, replace it across `*.html`, `sitemap.xml` and `robots.txt`.
- Generate a fresh social preview with `python3 scripts/make_og.py` (requires Pillow).
python3 -m http.server 8000
# open http://localhost:8000
```

## ➕ Adding your demo videos

Open `script.js` and paste your video URLs into the `DEMO_VIDEOS` object at the top:

```js
var DEMO_VIDEOS = {
    'whatsapp-booking': 'https://www.youtube.com/watch?v=YOUR_ID',
    'voice-agent': '',
    // ...
};
```

YouTube (including Shorts), Vimeo and Google Drive links are supported — videos play right on the site in a pop-up player. Cards left as `''` show a
"Demo coming soon" badge and scroll to the contact section when clicked.

## SEO checklist (already done)

- Unique title, meta description, keywords, canonical, Open Graph + Twitter card per page
- JSON-LD: Organization/ProfessionalService (24/7, Pakistan, worldwide), WebSite, Service,
  BreadcrumbList and FAQPage on every service page
- Semantic HTML5, breadcrumbs, internal linking between all services
- `sitemap.xml` lists all 12 pages; `robots.txt` allows all crawlers
- Lazy-loaded images/iframes, preconnected fonts, reduced-motion support

## Notes

- Canonical URLs, sitemap and JSON-LD use `https://dhqlimited.com/` — if your live domain differs, replace it across `*.html`, `sitemap.xml` and `robots.txt`.
- Create a 1200×630 `og-image.png` for richer social sharing previews (currently the hero photos are used).

The repo folder is still named `DentalFlow-AI` (git origin). Renaming the remote repo to
match DHQ Limited is optional.
