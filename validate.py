import glob
import json
import re
import sys
import os
import xml.etree.ElementTree as ET

fails = []

# 1. no nested button-in-anchor markup anywhere; no old DHQ branding
for f in glob.glob('*.html'):
    s = open(f, encoding='utf-8').read()
    if '<button class="cta-button">' in s:
        fails.append((f, 'nested cta-button'))
    if re.search(r'<a [^>]*><button class="btn ', s):
        fails.append((f, 'nested btn'))
    if 'demo-duration' in s:
        fails.append((f, 'demo-duration left'))
    if 'aria-label="Back to top" aria-hidden' in s:
        fails.append((f, 'back-to-top aria-hidden'))
    if 'dhqlimited.com' in s:
        fails.append((f, 'old DHQ domain left'))
    if 'DHQ' in s:
        fails.append((f, 'old DHQ brand left'))
    if 'theme-color' not in s:
        fails.append((f, 'theme-color missing'))

# 2. JSON-LD validity
blocks = 0
for f in glob.glob('*.html'):
    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', open(f, encoding='utf-8').read(), re.S):
        blocks += 1
        try:
            json.loads(b)
        except Exception as e:
            fails.append((f, 'jsonld: ' + str(e)))

idx = open('index.html', encoding='utf-8').read()
if '\"Product\"' not in idx:
    fails.append(('index', 'Product JSON-LD missing'))
if '\"Organization\"' not in idx:
    fails.append(('index', 'Organization JSON-LD missing'))
if 'voloai.uk' not in idx:
    fails.append(('index', 'voloai.uk domain missing'))

# 3. sitemap valid
try:
    t = ET.parse('sitemap.xml')
    urls = len(t.getroot().findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url'))
    print('sitemap urls:', urls)
except Exception as e:
    fails.append(('sitemap.xml', str(e)))

# 4. svgs parse
for p in ('assets/logo.svg', 'assets/favicon.svg'):
    try:
        ET.parse(p)
    except Exception as e:
        fails.append((p, str(e)))

# 5. script.js markers
js = open('script.js', encoding='utf-8').read()
for marker in ('youtube-nocookie.com/embed', 'lastFocused', 'live\\/'):
    if marker.replace('\\/', '/') not in js and marker not in js:
        fails.append(('script.js', 'missing ' + marker))

# 6. og-image exists
if not os.path.isfile('assets/images/og-image.png'):
    fails.append(('assets/images/og-image.png', 'missing'))

print('JSON-LD blocks:', blocks)
print('FAILS:', fails if fails else 'NONE')
sys.exit(0 if not fails else 1)
