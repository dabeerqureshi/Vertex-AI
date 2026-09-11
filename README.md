# Volo AI

**Never miss a call again.** Official website for Volo AI — the AI voice receptionist for UK small businesses. Volo answers every call 24/7: books appointments, handles enquiries and FAQs, captures caller details, saves data to your tools, and emails you the transcript.

- 📧 Email: `hello@voloai.uk`
- 💬 WhatsApp: `+92 314 4781120` (all CTAs open WhatsApp with a prefilled message)
- 🇬🇧 Built for UK clients and customers · pricing in **£ GBP**
- ⏰ Volo answers 24/7 — your team still rings first, Volo only steps in after 5 seconds

---

## How it works

1. A customer calls your existing UK number.
2. Your team's phone rings. If a real person picks up within 5 seconds, the call is theirs.
3. If nobody answers, Volo picks up instantly — books the appointment, handles the enquiry or FAQ, captures the caller's details, saves it to your database and sends you the full transcript.

---

## Pricing

| Plan | Price | What's included |
|------|-------|-----------------|
| 14-day free trial | £0 | Full access, no card required |
| **Lite** | £29/month | 1 number · 50 calls/mo · £0.15/min overage |
| **Business** (most popular) | £79/month | 1 number · 300 calls/mo · £0.12/min overage |
| **Pro** | £129/month | Up to 3 numbers · unlimited calls · £0.10/min overage |
| Annual (any plan) | 2 months free | Pay 10 months: £290 / £790 / £1,290 per year |

---

## Project Structure

```
.
├── index.html                # Landing page (hero, ROI calculator, features, pricing, FAQ)
├── comparison.html           # Volo vs human receptionist / voicemail / other AI
├── privacy-policy.html       # Legal — UK GDPR, call recording notice, sub-processors
├── terms-and-conditions.html # Legal — plans, billing, overages, recording
├── 404.html                  # Custom error page
├── styles.css                # "Aurora" theme — premium dark + voice gradient
├── script.js                 # Animations, phone-call simulator, video lightbox + DEMO_VIDEOS config
├── roi-calculator.js         # Interactive missed-call ROI calculator
├── robots.txt                # SEO crawler rules
├── sitemap.xml               # index + comparison + legal pages
├── scripts/make_og.py        # Generates assets/images/og-image.png (1200×630)
└── assets/
    ├── logo.svg              # Volo AI logo
    ├── favicon.svg           # Volo AI favicon
    └── images/og-image.png   # Social-share preview image
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

## SEO checklist (done)

- Unique title, meta description, canonical, Open Graph + Twitter card per page
- JSON-LD: `Organization`, `Product` (with pricing/offer data) and `WebSite` on the landing page
- Semantic HTML5, FAQ accordion, internal links between index and comparison
- `sitemap.xml` lists all pages; `robots.txt` allows all crawlers
- Preconnected fonts, reduced-motion support, scroll-reveal animations

## Notes

- Canonical URLs, sitemap and JSON-LD use `https://voloai.uk/` — if your live domain differs, replace it across `*.html`, `sitemap.xml` and `robots.txt`.
- If you add pricing changes, update all of: `index.html` (pricing + annual cards + JSON-LD offer), `terms-and-conditions.html` (billing section), and this README.
- Generate a fresh social preview with `python3 scripts/make_og.py` (requires Pillow).
