"""Restore ATD's approved public form settings after copying preview form files.

This helper belongs only to the isolated ATD public-site checkout. It never reads
server credentials or changes canonical preview files or hosting metadata.
"""
from pathlib import Path
import json
import os
import re
import tempfile

PRODUCTION_ORIGIN = 'https://atdnorthlondon.co.uk'
ATD_ENDPOINT = 'https://ujopvetvzfxgcxrphonx.supabase.co/functions/v1/submit-booking-request'
ATD_PUBLISHABLE_KEY = 'sb_publishable_bfmHVxxrF4psQVJ-aahaaQ_DsEutly9'
PUBLIC_KEYS = {
    'endpoint', 'publishableKey', 'submissionEnabled', 'verificationEnabled',
    'parentOrigins', 'maxPhotoUploads', 'allowedOrigins', 'privacyUrl',
}


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('Duplicate ATD public configuration field.')
        result[key] = value
    return result


def _json(text):
    return json.loads(text, object_pairs_hook=_unique_object)


def read_client_settings(path):
    """Parse the JSON assignment without executing browser JavaScript."""
    raw = Path(path).read_bytes()
    if len(raw) > 8192:
        raise ValueError('ATD public form configuration is unexpectedly large.')
    match = re.fullmatch(
        r'(?:\s*//[^\n]*(?:\n|$))*\s*window\.ATD_CLIENT_CONFIG\s*=\s*(\{[\s\S]*\})\s*;\s*',
        raw.decode('utf-8'),
    )
    if not match:
        raise ValueError('ATD public form configuration must be one JSON assignment.')
    config = _json(match.group(1))
    if not isinstance(config, dict) or set(config) != PUBLIC_KEYS:
        raise ValueError('Unexpected ATD public form fields; review before publication.')
    if config['endpoint'] != ATD_ENDPOINT or config['publishableKey'] != ATD_PUBLISHABLE_KEY:
        raise ValueError('ATD public form project endpoint or publishable key does not match the approved ATD project.')
    if type(config['submissionEnabled']) is not bool or type(config['verificationEnabled']) is not bool:
        raise ValueError('ATD public form requires explicit submission and email-confirmation settings.')
    if type(config['maxPhotoUploads']) is not int or config['maxPhotoUploads'] != 4 or config['privacyUrl'] != './privacy.html':
        raise ValueError('ATD public form upload/privacy settings differ from the reviewed release.')
    for name in ('allowedOrigins', 'parentOrigins'):
        value = config[name]
        if not isinstance(value, list) or not value or not all(isinstance(item, str) and item for item in value) or len(set(value)) != len(value):
            raise ValueError('ATD public form origins must be explicit nonempty lists.')
    return config


def prepare_public_client_settings(root):
    """Validate first, then atomically write enabled production or disabled preview.

    Empty origin is allowed only for disabled previews. A non-ATD origin, wrong
    project/key, malformed settings, or extra browser fields aborts the build.
    Merely knowing the domain never enables the form: indexing must be true too.
    """
    root = Path(root)
    settings = _json((root / 'seo-settings.json').read_text())
    if not isinstance(settings, dict):
        raise ValueError('ATD SEO settings must be an object.')
    enabled = settings.get('indexing_enabled', False)
    origin = settings.get('public_origin', '')
    if type(enabled) is not bool:
        raise ValueError('ATD indexing_enabled must be true or false.')
    if origin not in ('', PRODUCTION_ORIGIN):
        raise ValueError('ATD public-site origin must exactly match the approved naked HTTPS ATD domain.')
    if enabled and origin != PRODUCTION_ORIGIN:
        raise ValueError('ATD production submission requires the exact approved public origin.')
    path = root / 'dist' / 'enquiry' / 'client-config.js'
    config = read_client_settings(path)
    production = enabled and origin == PRODUCTION_ORIGIN
    config['submissionEnabled'] = production
    if production:
        config['allowedOrigins'] = [PRODUCTION_ORIGIN]
        config['parentOrigins'] = [PRODUCTION_ORIGIN]
    # Disabled copied-preview origins are retained; they cannot submit because
    # submissionEnabled is false. Production origins are always replaced above.
    comment = ('// ATD public enquiry settings; only the approved HTTPS website can submit.' if production else
               '// ATD preview settings; no client submissions or emails.')
    output = comment + '\nwindow.ATD_CLIENT_CONFIG=' + json.dumps(config, indent=2) + ';\n'
    temporary = None
    try:
        with tempfile.NamedTemporaryFile('w', encoding='utf-8', dir=path.parent, prefix='.client-config-', delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(output)
        os.replace(temporary, path)
    finally:
        if temporary and temporary.exists():
            temporary.unlink()
    return production
