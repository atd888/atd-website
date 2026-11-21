#!/bin/sh
# Rebuild the site and copy it into docs/ (the folder GitHub Pages serves).
set -e
cd "$(dirname "$0")"
PYTHONDONTWRITEBYTECODE=1 python3 build_site.py
python3 check_site.py
rm -rf docs && cp -r dist docs
echo "atdnorthlondon.co.uk" > docs/CNAME && touch docs/.nojekyll
echo "Ready: commit and push to publish."
