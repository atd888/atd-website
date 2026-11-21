ATD PUBLIC WEBSITE — ISOLATED STAGING SOURCE

This directory contains only the ATD static website, public enquiry form and the build inputs needed to reproduce its HTML/metadata.

BUILD AND CHECK
PYTHONDONTWRITEBYTECODE=1 python3 build_site.py
PYTHONDONTWRITEBYTECODE=1 python3 check_site.py
node --check dist/app.js
node --check dist/enquiry/client-form.js

The staging builder also runs publish_client_settings.py before generating pages. This restores the exact approved ATD production enquiry settings after public form files are copied from the disabled canonical preview. It requires indexing_enabled=true and public_origin exactly https://atdnorthlondon.co.uk; disabled/empty-origin preview builds stay disabled. A wrong domain, project endpoint, publishable key, verification setting or unexpected browser field aborts the build. Preserve this staging helper/import when merging changes from canonical sources.

No dependency installation is required. Python uses only its standard library. CSS, JavaScript, responsive assets and public client-form files under dist are retained source inputs. build_site.py regenerates content HTML, metadata, JSON-LD, robots and sitemap using photo-selection.json, seo_helpers.py and seo-settings.json.

There is no need to decode original HEIC files, regenerate photos, use the original Downloads folder, or install the separate video/image tools to rebuild this staged website. Those original-media preparation tools and backups are intentionally excluded.

Launch indexing is explicitly enabled in this isolated copy: nine marketing pages are index,follow; legal, offer, form, 404 and legacy alias pages remain noindex. robots allows crawling and points to the nine-URL sitemap at https://atdnorthlondon.co.uk/sitemap.xml. The canonical local working preview remains blocked. The staged public enquiry configuration is now prepared with submissionEnabled=true and verificationEnabled=true, restricted to the exact origin https://atdnorthlondon.co.uk. LAN, file, old GitHub, www, HTTP and unrelated origins cannot pass the public form’s readiness check. The canonical working preview remains disabled. This final form configuration is a staging preparation; this audit has not deployed it or proved real confirmation-email/owner-inbox delivery. The root agent coordinates final publication and backend readiness.

The root agent owns the separately created and verified ATD Site identity in .openai/hosting.json. This indexing task does not change hosting metadata.

See PUBLISHING.txt for provenance and scope. Never use Hello Honey resources for ATD.
