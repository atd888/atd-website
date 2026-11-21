"""ATD's page metadata and SEO files. Indexing requires an explicit launch flag.

A public origin is deliberately absent until the user chooses and approves one.
The canonical local preview stays blocked. This isolated launch copy enables only its nine marketing pages after explicit publication approval.
"""
from datetime import date
from html import escape
from pathlib import Path
from urllib.parse import urlsplit
import json
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
SETTINGS_PATH = ROOT / 'seo-settings.json'

PAGE_SEO = {
    '/': {
        'title': 'Painters & Decorators in North London | Free Quotes',
        'description': 'Hornsey N8-based painters and decorators serving North London. Interior and exterior painting, wallpapering and refurbishments. See real work. Get a free quote.',
        'label': 'Home',
        'image_slug': 'exterior',
    },
    '/painting-decorating/': {
        'title': 'Interior & Exterior Painting in North London',
        'description': 'Painting and decorating for rooms, doors, woodwork and exteriors in Hornsey and nearby North London. Preparation and materials agreed in a written quote.',
        'label': 'Painting & decorating',
        'image_slug': 'living-room',
    },
    '/wallpapering/': {
        'title': 'Wallpaper Hanging in North London',
        'description': 'Wallpaper hanging for feature walls and complete rooms in Hornsey and nearby North London. Discuss your chosen paper, wall preparation and a free quote.',
        'label': 'Wallpapering',
        'image_slug': 'wallpaper',
    },
    '/bathroom-refurbishments/': {
        'title': 'Bathroom Refurbishments in North London',
        'description': 'Bathroom refreshes and full refurbishments in Hornsey and nearby North London. See a real project from strip-out to tiling and request an agreed-scope quote.',
        'label': 'Bathroom refurbishments',
        'image_slug': 'bathroom',
    },
    '/full-refurbishments/': {
        'title': 'House & Flat Refurbishments in North London',
        'description': 'Plan a house or flat refurbishment in Hornsey and nearby North London. Discuss rooms, finishes, access and specialist requirements before a written quote.',
        'label': 'Full refurbishments',
        'image_slug': 'kitchen',
    },
    '/gallery/': {
        'title': 'Painting & Refurbishment Project Gallery',
        'description': 'Browse real ATD interiors, exterior decorating, wallpapering and bathroom projects. Finished details and clearly labelled preparation photos show the work.',
        'label': 'Project gallery',
        'image_slug': 'exterior',
    },
    '/areas/': {
        'title': 'Areas We Cover in Hornsey & North London',
        'description': 'Based in Hornsey N8, ATD covers nearby North London for painting, decorating and refurbishments. See our core areas and ask about your property postcode.',
        'label': 'Areas we cover',
        'image_slug': 'entrance',
    },
    '/about/': {
        'title': 'About Our North London Decorating Business',
        'description': 'Meet Landi and ATD North London Painters. Learn how we approach preparation, written quotations and decorating and refurbishment projects in your home.',
        'label': 'About ATD',
        'image_slug': 'entrance',
    },
    '/contact/': {
        'title': 'Request a Painting or Refurbishment Quote',
        'description': 'Contact ATD about painting, wallpapering or refurbishment work in North London. Start a quote request, call Landi or send project photos on WhatsApp.',
        'label': 'Contact ATD',
        'image_slug': 'exterior',
    },
}
from local_areas import AREA_PAGES
from project_pages import PROJECT_PAGES
from decorating_guide import GUIDE_PAGES
from exterior_painting import EXTERIOR_ROUTE, EXTERIOR_META
PAGE_SEO.update(AREA_PAGES)
PAGE_SEO.update(PROJECT_PAGES)
PAGE_SEO.update(GUIDE_PAGES)
PAGE_SEO[EXTERIOR_ROUTE] = EXTERIOR_META
PUBLIC_ROUTES = tuple(PAGE_SEO)
SERVICE_ROUTES = (
    '/painting-decorating/', '/exterior-painting/', '/wallpapering/',
    '/bathroom-refurbishments/', '/full-refurbishments/',
)
SOCIAL_LINKS = (
    'https://www.google.com/maps?cid=5866884612574117255',
    'https://www.instagram.com/atd_london/',
    'https://www.youtube.com/@atdnorthlondon',
    'https://www.facebook.com/atdnorthlondonpainters/',
)


def load_origin(settings_path=None):
    """Return an approved HTTPS origin or an empty string; fail closed otherwise."""
    path = Path(settings_path) if settings_path is not None else SETTINGS_PATH
    settings = json.loads(path.read_text())
    if not isinstance(settings, dict):
        raise ValueError('ATD SEO settings must be a JSON object.')
    raw = settings.get('public_origin', '')
    if not isinstance(raw, str):
        raise ValueError('ATD public_origin must be an HTTPS origin or an empty string.')
    candidate = raw.strip()
    if not candidate:
        return ''
    if any(char.isspace() or ord(char) < 32 for char in candidate):
        raise ValueError('ATD public_origin must not contain whitespace or control characters.')
    parsed = urlsplit(candidate)
    hostname = (parsed.hostname or '').lower().rstrip('.')
    if hostname == 'hello-honey.co.uk' or hostname.endswith('.hello-honey.co.uk'):
        raise ValueError('Hello Honey is a protected separate project; its domain cannot be used for ATD.')
    try:
        port = parsed.port
    except ValueError as exc:
        raise ValueError('ATD public_origin has an invalid port.') from exc
    valid_hostname = bool(hostname and len(hostname) <= 253 and all(
        re.fullmatch(r'[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?', label)
        for label in hostname.split('.')
    ))
    if (parsed.scheme != 'https' or not valid_hostname or
            parsed.username is not None or parsed.password is not None or
            parsed.path not in ('', '/') or parsed.query or parsed.fragment):
        raise ValueError('ATD public_origin must be an HTTPS origin with no credentials, path, query or fragment.')
    return 'https://' + hostname + (':' + str(port) if port and port != 443 else '')


def indexing_enabled():
    """Require both the approved HTTPS origin and an explicit boolean launch flag."""
    settings = json.loads(SETTINGS_PATH.read_text())
    enabled = settings.get('indexing_enabled', False)
    if type(enabled) is not bool:
        raise ValueError('ATD indexing_enabled must be true or false.')
    if enabled and not load_origin():
        raise ValueError('ATD indexing cannot be enabled without a configured HTTPS public origin.')
    return enabled


def _route(path):
    route = '/' + str(path).strip('/') + '/'
    return '/' if route == '//' else route


def _page_info(path, title, description):
    page = PAGE_SEO.get(_route(path), {})
    page_title = page.get('title', title)
    page_description = page.get('description', description)
    # The builder supplies unbranded fallback titles. Be defensive on repeated use.
    for suffix in (' | ATD North London Painters', ' | ATD'):
        if page_title.endswith(suffix):
            page_title = page_title[:-len(suffix)]
    return page, page_title + ' | ATD', page_description


def metadata_html(path, title, description, photos):
    """Build escaped head metadata; emit absolute URL fields only with an origin."""
    route = _route(path)
    origin = load_origin()
    page, page_title, page_description = _page_info(route, title, description)
    esc = lambda value: escape(str(value), quote=True)
    tags = [
        '<title>' + esc(page_title) + '</title>',
        '<meta name="description" content="' + esc(page_description) + '">',
        '<meta property="og:title" content="' + esc(page_title) + '">',
        '<meta property="og:description" content="' + esc(page_description) + '">',
        '<meta property="og:site_name" content="ATD North London Painters">',
        '<meta property="og:type" content="website">',
        '<meta property="og:locale" content="en_GB">',
    ]
    if route == '/' and origin == 'https://atdnorthlondon.co.uk' and indexing_enabled():
        verification = json.loads(SETTINGS_PATH.read_text()).get('google_site_verification', '')
        if verification:
            if not isinstance(verification, str) or not re.fullmatch(r'[A-Za-z0-9_-]+', verification):
                raise ValueError('Invalid Google Search Console verification value.')
            tags.append('<meta name="google-site-verification" content="' + esc(verification) + '">')
        bing_verification = json.loads(SETTINGS_PATH.read_text()).get('bing_site_verification', '')
        if bing_verification:
            if not isinstance(bing_verification, str) or not re.fullmatch(r'[A-Fa-f0-9]{32}', bing_verification):
                raise ValueError('Invalid Bing Webmaster Tools verification value.')
            tags.append('<meta name="msvalidate.01" content="' + esc(bing_verification) + '">')
    photo = next((item for item in photos if item.get('slug') == page.get('image_slug', 'exterior')), None)
    image_url = ''
    if origin:
        # The former gallery address is an alias, never a second canonical page.
        canonical_route = '/gallery/' if route == '/projects/' else route
        url = origin + canonical_route
        tags.extend([
            '<link rel="canonical" href="' + esc(url) + '">',
            '<meta property="og:url" content="' + esc(url) + '">',
        ])
        if photo:
            image_url = origin + '/assets/' + photo['slug'] + '-1200.' + photo.get('format', 'webp')
            tags.extend([
                '<meta property="og:image" content="' + esc(image_url) + '">',
                '<meta property="og:image:alt" content="' + esc(photo.get('title', 'ATD project photograph')) + '">',
                '<meta name="twitter:image" content="' + esc(image_url) + '">',
                '<meta name="twitter:image:alt" content="' + esc(photo.get('title', 'ATD project photograph')) + '">',
            ])
    tags.extend([
        '<meta name="twitter:card" content="' + ('summary_large_image' if image_url else 'summary') + '">',
        '<meta name="twitter:title" content="' + esc(page_title) + '">',
        '<meta name="twitter:description" content="' + esc(page_description) + '">',
    ])
    return '\n'.join(tags)


def structured_data(path, title, description, services, areas):
    """Describe the actual business and page without storefront or ranking claims."""
    route = _route(path)
    origin = load_origin()
    page, page_title, page_description = _page_info(route, title, description)
    prefix = origin + '/' if origin else ''
    business_id = prefix + '#business'
    page_id = (origin + route if origin else '') + '#webpage'
    business = {
        '@type': 'HousePainter', '@id': business_id,
        'name': 'ATD North London Painters', 'legalName': 'AT DERMYSHI LTD',
        'telephone': '+447557954457', 'email': 'tdermyshi88@gmail.com',
        'description': 'Based in Hornsey N8, ATD North London Painters provides painting, decorating, wallpapering and agreed-scope property refurbishments across nearby North London.',
        'contactPoint': {'@type': 'ContactPoint', 'telephone': '+447557954457', 'contactType': 'customer enquiries', 'availableLanguage': 'English'},
        'areaServed': [{'@type': 'Place', 'name': area} for area in areas],
        'sameAs': list(SOCIAL_LINKS),
    }
    if origin:
        business['url'] = origin + '/'
    webpage = {
        '@type': 'WebPage', '@id': page_id,
        'name': page_title, 'description': page_description,
        'inLanguage': 'en-GB', 'about': {'@id': business_id},
    }
    graph = [business, webpage]
    if origin:
        website_id = origin + '/#website'
        graph.append({
            '@type': 'WebSite', '@id': website_id,
            'name': 'ATD North London Painters', 'url': origin + '/',
            'inLanguage': 'en-GB', 'publisher': {'@id': business_id},
        })
        webpage.update({'url': origin + route, 'isPartOf': {'@id': website_id}})
        if route != '/' and route in PUBLIC_ROUTES:
            breadcrumb_id = origin + route + '#breadcrumb'
            graph.append({
                '@type': 'BreadcrumbList', '@id': breadcrumb_id,
                'itemListElement': [
                    {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': origin + '/'},
                    {'@type': 'ListItem', 'position': 2, 'name': page.get('label', title), 'item': origin + route},
                ],
            })
            webpage['breadcrumb'] = {'@id': breadcrumb_id}
    if route in SERVICE_ROUTES:
        service = next((item for item in services if '/' + item['slug'].strip('/') + '/' == route), {})
        service_id = (origin + route if origin else '') + '#service'
        node = {
            '@type': 'Service', '@id': service_id,
            'name': service.get('name', page.get('label', title)),
            'serviceType': service.get('name', page.get('label', title)),
            'description': page_description,
            'provider': {'@id': business_id},
            'areaServed': [{'@type': 'Place', 'name': area} for area in areas],
        }
        if origin:
            node['url'] = origin + route
        graph.append(node)
        webpage['mainEntity'] = {'@id': service_id}
    if route in AREA_PAGES:
        area = AREA_PAGES[route]['label']
        service_id = (origin + route if origin else '') + '#local-service'
        node = {
            '@type': 'Service', '@id': service_id,
            'name': 'ATD painting, decorating and refurbishment services in ' + area,
            'description': page_description,
            'serviceType': [item['name'] for item in services],
            'provider': {'@id': business_id},
            'areaServed': {'@type': 'Place', 'name': area},
        }
        if origin:
            node['url'] = origin + route
        graph.append(node)
        webpage['mainEntity'] = {'@id': service_id}
    return {'@context': 'https://schema.org', '@graph': graph}


def write_seo_files(dist):
    """Write SEO files for the explicit preview or authorised launch state."""
    destination = Path(dist)
    destination.mkdir(parents=True, exist_ok=True)
    origin = load_origin()
    enabled = indexing_enabled()
    robots = ('User-agent: *\nAllow: /\nSitemap: ' + origin + '/sitemap.xml\n') if enabled else 'User-agent: *\nDisallow: /\n'
    (destination / 'robots.txt').write_text(robots)
    manifest = {
        'business': 'ATD North London Painters', 'public_origin': origin,
        'indexing_enabled': enabled, 'paths': list(PUBLIC_ROUTES),
    }
    if origin:
        manifest['urls'] = [origin + route for route in PUBLIC_ROUTES]
    (destination / 'public-route-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    sitemap_path = destination / 'sitemap.xml'
    if not origin:
        sitemap_path.unlink(missing_ok=True)
        return
    namespace = 'http://www.sitemaps.org/schemas/sitemap/0.9'
    ET.register_namespace('', namespace)
    root = ET.Element('{' + namespace + '}urlset')
    # Stored content dates only: do not make untouched pages look newly edited.
    modified = json.loads(SETTINGS_PATH.read_text()).get('page_last_modified', {})
    if not isinstance(modified, dict) or any(route not in PUBLIC_ROUTES for route in modified):
        raise ValueError('Sitemap modification dates must target public ATD pages.')
    for route in PUBLIC_ROUTES:
        entry = ET.SubElement(root, '{' + namespace + '}url')
        ET.SubElement(entry, '{' + namespace + '}loc').text = origin + route
        if route in modified:
            value = modified[route]
            if not isinstance(value, str) or date.fromisoformat(value).isoformat() != value:
                raise ValueError('Sitemap dates must use YYYY-MM-DD.')
            ET.SubElement(entry, '{' + namespace + '}lastmod').text = value
    ET.ElementTree(root).write(sitemap_path, encoding='utf-8', xml_declaration=True)
