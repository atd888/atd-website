"""Links to existing ATD work; locations and reviews are already owner-matched."""
from html import escape

SERVICE_EVIDENCE = {
    'painting-decorating': [
        ('/projects/crouch-end-redecoration/', 'Interior decorating in Crouch End N8',
         'Coral-painted shelving and chimney-wall details, with Julian Smilg’s Google review of the same project.'),
        ('/projects/stamford-hill-exterior/', 'Entrance and exterior work in Stamford Hill N16',
         'Entrance decorating and exterior glazed doors at one property, alongside other finishing work and John Burgess’s Google review.'),
    ],
    'wallpapering': [
        ('/gallery/#story-vinyl-wallpaper-corridor', 'Textured vinyl wallpaper along a corridor',
         'Six project photographs show the wallcovering, doorway edges, corners and projecting wall sections. Floor protection remains in place during the finishing stage.'),
    ],
    'bathroom-refurbishments': [
        ('/projects/leyton-bathroom/', 'The red-tiled bathroom project in Leyton E10',
         'Follow the strip-out, red floor tiling and later fittings stage, with Menna Cominetti’s Google review of the project.'),
    ],
    'full-refurbishments': [
        ('/projects/crouch-end-redecoration/', 'Interior decorating and terrace work in Crouch End N8',
         'One property, with coral-painted interior details and terrace framework and decking photographs.'),
        ('/projects/stamford-hill-exterior/', 'Several finishing tasks at one Stamford Hill N16 home',
         'Entrance decorating, exterior glazed doors, timber floors and patterned front-step tiles, with one matching customer review.'),
        ('/projects/e17-kitchen/', 'Kitchen refurbishment details in E17',
         'Timber worktops, open shelving and the kitchen during the finishing stage, with Kevin Paskins’s Google review.'),
    ],
}


def service_evidence_html(slug):
    items = SERVICE_EVIDENCE.get(slug, [])
    if not items:
        return ''
    cards = ''.join(
        '<article><h3><a href="' + escape(url, quote=True) + '">' + escape(title) +
        ' ↗</a></h3><p>' + escape(summary) + '</p></article>'
        for url, title, summary in items
    )
    return (
        '<section class="section wrap local-services" id="service-projects">'
        '<div class="section-heading"><div><p class="kicker">REAL ATD WORK</p>'
        '<h2>See the work.<br><em>Look at the details.</em></h2></div>'
        '<p>Explore the photographs and stages<br>from existing ATD projects.</p></div>'
        '<div class="local-service-grid">' + cards + '</div>'
        '<p class="fine">These are individual project examples. The work, preparation and materials '
        'for your property are agreed separately in your written quotation.</p></section>'
    )
