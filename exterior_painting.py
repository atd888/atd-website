"""A focused exterior service page using existing ATD scope and verified work."""
from urllib.parse import quote

EXTERIOR_ROUTE = '/exterior-painting/'
EXTERIOR_META = {
    'title': 'Exterior Painters in Hornsey & North London',
    'description': 'Exterior painting for doors, timber windows, house fronts and railings in Hornsey and North London. See real ATD work and request a free written quotation.',
    'label': 'Exterior painting',
    'image_slug': 'exterior',
}


def exterior_content(button, image, faq, contact_actions):
    booking = '/enquiry/booking.html?service=exterior-painting'
    brief = ('Hi ATD, I would like an exterior painting quote.\n'
             'Postcode: \nSurfaces (doors, windows, walls or railings): \n'
             'Approximate number / size and height: \n'
             'Existing condition: \nAccess arrangements: \n'
             'Preferred timeframe: \nI can send a wide photograph and close-ups.')
    whatsapp = 'https://wa.me/447557954457?text=' + quote(brief, safe='')
    body = '''<section class="service-hero wrap"><div><p class="kicker">BASED IN HORNSEY N8 · SERVING NORTH LONDON</p>
<h1>Exterior painting.<br><em>A better welcome home.</em></h1>
<p class="lead">Front doors, timber windows, exterior walls and railings. Tell ATD which surfaces need attention and the finish you have in mind, from an entrance refresh to a wider exterior decorating project.</p>
<p class="service-local-context">We discuss preparation, suitable coatings, weather and safe access before agreeing the work. Your written quotation defines the surfaces, materials and practical arrangements included.</p>'''
    body += contact_actions('Exterior painting', 'exterior-painting')
    body += '<p class="fine">Hornsey N8 &amp; nearby North London · Free quotations</p></div><div class="service-hero-photo">' + image('exterior', eager=True) + '''</div></section>
<section class="section wrap"><div class="section-heading"><div><p class="kicker">BE SPECIFIC ABOUT THE SURFACES</p><h2>What needs<br><em>a fresh finish?</em></h2></div><p>A front door and a whole house front<br>need different briefs.</p></div><div class="scope-grid">
<article><span class="kicker">01</span><h3>Front doors &amp; entrances</h3><p>Tell us whether the door, frame and surrounding painted surfaces are included, and whether you want both sides painted. A close-up of the existing finish helps us discuss preparation and colour choices.</p></article>
<article><span class="kicker">02</span><h3>Timber windows &amp; frames</h3><p>Show the frames, sills and their current condition. Include the number of windows, their height and how they can be reached. Repairs and any additional preparation need to be assessed and expressly included in the scope.</p></article>
<article><span class="kicker">03</span><h3>House fronts &amp; exterior walls</h3><p>Send a wide photograph of the elevation and closer views of damaged or peeling areas. Identify the surfaces you want painted and any areas to leave untouched. Condition, coatings and access are considered before quoting.</p></article>
<article><span class="kicker">04</span><h3>Railings &amp; exterior metalwork</h3><p>Share photographs and approximate lengths or quantities. Existing coatings, surface condition and the finish you want determine the preparation and paint system to discuss.</p></article></div></section>
<section class="section wrap exterior-evidence"><div><p class="kicker">A REAL ATD PROJECT · STAMFORD HILL N16</p><h2>Look at the work.<br><em>Read the customer’s experience.</em></h2>
<p>Our Stamford Hill project brings together the yellow-door entrance, exterior glazed doors during preparation and other finishing tasks at the same property. John Burgess’s matching Google review describes the exterior painting and brickwork.</p>
<p>The photographs show individual parts and stages of this project. They help explain the work; your own scope is assessed separately.</p>
<a class="text-link" href="/projects/stamford-hill-exterior/">See the project photographs and John’s review ↗</a></div>
<figure>''' + image('glazed-doors-preparation-photo') + '''<figcaption>Exterior glazed doors during preparation at the Stamford Hill property. Work in progress.</figcaption></figure></section>
<section class="section process"><div class="wrap"><div class="section-heading"><div><p class="kicker">A CLEAR SCOPE BEFORE THE FIRST COAT</p><h2>Plan the exterior.<br><em>Know what is included.</em></h2></div></div><div class="process-grid">
<article><span class="step">01</span><h3>Assess the existing finish</h3><p>Photographs start the discussion; a visit may be needed to assess surfaces and access. Tell us about any peeling paint, damaged areas or previous work you know about.</p></article>
<article><span class="step">02</span><h3>Agree preparation &amp; materials</h3><p>Your quote should identify the preparation, coatings, protection and any agreed repairs. Confirm who supplies the materials and whether access equipment is included.</p></article>
<article><span class="step">03</span><h3>Discuss access &amp; timing</h3><p>Height, routes around the property, neighbouring access and weather need to be considered. We discuss a practical programme before you agree to proceed.</p></article></div></div></section>
<section class="project-start wrap" id="exterior-quote"><div><p class="kicker">MAKE THE FIRST STEP EASY</p><h2>Show us<br><em>your exterior.</em></h2></div><div><p>Send your postcode, a wide view, close-ups of the surfaces and the work you want included. Add approximate quantities, height and access details where known. Tell us your preferred timeframe and whether you have chosen a colour or finish.</p>
<div class="service-enquiry-actions">''' + button('Start my exterior enquiry', booking) + button('Send an exterior brief on WhatsApp', whatsapp, 'outline') + '''</div>
<p class="fine">No measurements yet? Share what you know. For the guided form, confirm your email after submitting so ATD can review the request. You can then attach up to four photos through your private link.</p></div></section>
<section class="section wrap faq-grid"><div><p class="kicker">BEFORE YOU ENQUIRE</p><h2>Exterior painting<br><em>questions.</em></h2></div>'''
    body += faq([
        ('Can I ask for just a front door?', 'Yes. Say whether the frame, surrounding painted surfaces and one or both sides of the door are included. Send photographs and your postcode for the next step.'),
        ('Do you paint exterior timber windows?', 'Yes. Share the number of windows, height, access and photographs of the frames and sills. Condition and any repairs must be assessed before the preparation and scope are agreed.'),
        ('Are scaffolding and repairs included?', 'Only where identified and agreed in your written quotation. Tell us about height, access and damaged areas so we can discuss the arrangements and responsibilities before work starts.'),
        ('How much will exterior painting cost?', 'The price depends on the surfaces, condition, preparation, materials and access. ATD quotes for the agreed work at your property. Photos help us begin; a visit may be needed before a final written quotation.'),
        ('Can you work around the weather?', 'Weather and the requirements of the chosen coatings are considered when planning exterior work. Timings are discussed for your project rather than promised from a photograph alone.'),
    ])
    return body + '''</section><section class="wrap exterior-related"><h2>Planning more than the outside?</h2><p>Explore <a href="/painting-decorating/">interior painting and decorating</a>, read our <a href="/guides/painting-decorating-quote/">guide to comparing decorating quotations</a>, or check our <a href="/areas/">North London service areas</a>.</p></section>'''
