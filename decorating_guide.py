"""Practical quote planning, grounded in ATD's existing service scope and projects."""
from urllib.parse import quote

GUIDE_ROUTE = '/guides/painting-decorating-quote/'
GUIDE_PAGES = {
    GUIDE_ROUTE: {
        'title': 'Painting & Decorating Quotes in North London: A Guide',
        'description': 'Plan your decorating quote in Hornsey and North London. Understand preparation, paint, access and what to compare, with real ATD project examples.',
        'label': 'Decorating quote guide',
        'image_slug': 'coral-living-room-photo',
    }
}


def guide_teaser():
    return '''<section class="wrap quote-guide-teaser" aria-labelledby="quote-guide-title">
<div><p class="kicker">BEFORE YOU REQUEST A QUOTE</p><h2 id="quote-guide-title">What affects the cost<br><em>of decorating?</em></h2>
<p>Preparation, the surfaces included, materials and access all matter. Use our practical guide to put together your brief and compare quotations for the same work.</p></div>
<a class="button outline" href="/guides/painting-decorating-quote/">Read the decorating quote guide <span aria-hidden="true">↗</span></a></section>'''


def guide_content(button, image, faq):
    brief = ('Hi ATD, I would like a decorating quote.\n'
             'Postcode: \nProperty / rooms: \n'
             'Surfaces (walls, ceilings, doors, woodwork or exterior): \n'
             'Current condition / preparation: \n'
             'Paint or finish preferences (or not sure): \n'
             'Access and whether occupied: \nPreferred timeframe: \n'
             'I can send photographs of the whole space and any damaged areas.')
    whatsapp = 'https://wa.me/447557954457?text=' + quote(brief, safe='')
    out = '''<section class="page-intro wrap guide-intro"><p class="kicker">PLANNING YOUR PROJECT · HORNSEY &amp; NORTH LONDON</p>
<h1>Your decorating quote.<br><em>Know what to include.</em></h1>
<p class="lead">Before asking how much painting and decorating will cost, decide what needs painting and what condition it is in. Two similar-sized rooms can need very different amounts of preparation.</p>
<p>ATD is based in Hornsey N8. This guide explains what to send us, what affects your quotation and how to compare the work included. We quote for your property; this is not a fixed price list or a day-rate estimate.</p>
<div class="service-enquiry-actions">''' + button('Request a decorating quote', '/enquiry/booking.html?service=painting-decorating') + '''<a class="text-link" href="#quote-checklist">Start with the checklist ↓</a></div>
</section><nav class="wrap guide-contents" aria-label="In this guide"><strong>In this guide</strong>
<a href="#cost-factors">What affects cost</a><a href="#compare-quotes">Compare quotations</a><a href="#real-examples">Real project examples</a><a href="#quote-checklist">What to send ATD</a><a href="#quote-questions">Common questions</a></nav>
<article class="wrap decorating-guide">
<section id="cost-factors"><p class="kicker">THE WORK BEHIND THE PRICE</p><h2>What affects a painting<br><em>and decorating quote?</em></h2>
<div class="guide-factor-grid">
<div><h3>1. The surfaces included</h3><p>“Paint the room” can mean walls only, or walls, ceiling, skirting, doors and frames. List each surface. For a door, say whether the frame and both sides are included. Approximate room dimensions and ceiling height help describe the scale.</p></div>
<div><h3>2. The existing condition</h3><p>Sound painted walls need a different scope from surfaces with peeling paint, cracks or old wallpaper. Send close-ups as well as a whole-room photograph. Wallpaper stripping or more extensive repairs should be identified separately; the surface underneath may need assessing before the preparation can be confirmed.</p></div>
<div><h3>3. Paint, colour and finish</h3><p>Tell us whether you want to keep the existing colour or make a change, and whether you have selected a product. Include the finish for walls and woodwork, or say you need advice. The quotation should identify the agreed paint system, coverage and who supplies the materials.</p></div>
<div><h3>4. Access and protection</h3><p>Furniture, an occupied room, stairs, parking and access to upper floors can affect how the work is organised. Explain what can be moved and whether the property will remain in use. Agree protection and moving responsibilities before work starts.</p></div>
<div><h3>5. Exterior condition and access</h3><p>For exterior decorating, show the whole elevation and close-ups of doors, windows and damaged areas. Height, safe access, surface condition and weather affect the plan. Ask whether access equipment and any separately agreed repairs are included.</p></div>
<div><h3>6. The sequence of work</h3><p>Tell us your preferred timeframe and whether other trades are involved. Preparation, coats and drying need to be considered together. A requested date is a starting point for discussion; availability and the programme are agreed separately.</p></div>
</div><p>See our <a href="/painting-decorating/#paint-finishes">plain-language paint finish guide</a> if you are choosing between matt, eggshell, satin and gloss.</p></section>
<section id="compare-quotes"><p class="kicker">COMPARE THE SAME WORK</p><h2>Look beyond<br><em>the total price.</em></h2>
<p>Give each decorator the same brief. A lower total may cover fewer surfaces, less preparation or different materials. Before accepting a quotation, check:</p>
<ul class="guide-checklist"><li><strong>Scope:</strong> the rooms and surfaces included, and anything excluded.</li>
<li><strong>Preparation:</strong> the agreed repairs, stripping, sanding and priming, where required.</li>
<li><strong>Materials:</strong> products, finishes, supply responsibilities and any allowances.</li>
<li><strong>Practical arrangements:</strong> access equipment, protection, furniture, working access and clearing up.</li>
<li><strong>Price and changes:</strong> what the total includes, payment arrangements, any applicable tax and how additional work will be agreed and priced.</li>
<li><strong>Timing:</strong> the proposed start, sequence and any conditions that affect the programme.</li></ul>
<p>A photograph can start the conversation. A visit may be needed before a final written quotation, especially where condition or access is unclear. Agree changes to the scope before the additional work proceeds.</p></section>
<section id="real-examples"><p class="kicker">REAL ATD PROJECTS</p><h2>Different details.<br><em>Different briefs.</em></h2><p>These examples show why a useful brief describes the work, not just the room count. They are examples of scope, not price comparisons.</p>
<div class="guide-project-grid"><figure>''' + image('coral-living-room-photo') + '''<figcaption><h3><a href="/projects/crouch-end-redecoration/">Interior decorating in Crouch End N8 ↗</a></h3><p>Coral-painted shelving and chimney-wall details are part of the same project as the terrace photographs. Identify built-in features and woodwork separately from plain walls when describing your own room.</p></figcaption></figure>
<figure>''' + image('glazed-doors-preparation-photo') + '''<figcaption><h3><a href="/projects/stamford-hill-exterior/">Exterior details in Stamford Hill N16 ↗</a></h3><p>The exterior glazed doors are shown during preparation. This property also features the yellow-door entrance and other finishing work. For your quote, specify each door or window and show its condition.</p></figcaption></figure></div></section>
<section id="quote-checklist" class="guide-brief"><p class="kicker">MAKE YOUR FIRST ENQUIRY USEFUL</p><h2>What to send<br><em>with your quote request.</em></h2>
<ol class="guide-checklist"><li>Your postcode and property type.</li><li>The rooms or exterior areas, with approximate dimensions where known.</li><li>The surfaces to include: walls, ceilings, doors, frames, skirting or exterior woodwork.</li><li>A whole-space photo, close-ups of problem areas and a note about old wallpaper or peeling paint.</li><li>Your colour and finish preferences, or “not sure — please advise”.</li><li>Access, whether the space is occupied and your preferred timeframe.</li></ol>
<p>No measurements yet? Share what you know. You can start the guided form now and attach up to four project photos through your private link after confirming your email, or send the brief and photographs on WhatsApp.</p>
<div class="service-enquiry-actions">''' + button('Start my decorating enquiry', '/enquiry/booking.html?service=painting-decorating') + button('Use the WhatsApp brief', whatsapp, 'outline') + '''</div>
<p class="fine">An enquiry does not confirm a booking. Work, materials, access and timings are agreed in your written quotation.</p></section>
<section id="quote-questions"><p class="kicker">BEFORE YOU DECIDE</p><h2>Decorating quote<br><em>questions, answered.</em></h2>'''
    out += faq([
        ('Can you give a decorating price from photographs?', 'Photographs help us understand the size and condition of the work. We may need measurements, further details or a visit before a final written quotation. The agreed scope and price are specific to your property.'),
        ('Is paint included in the quote?', 'Supply arrangements are agreed for each project. Check that the quotation identifies the materials, finish and who supplies them. Tell us if you have already bought paint or wallpaper.'),
        ('Can I ask for one room or just exterior woodwork?', 'Yes. You can enquire about one room, doors or exterior woodwork. Specify the surfaces and preparation needed so the quotation covers the work you actually want.'),
        ('Does the website offer apply to materials?', 'No. The website offer is 10% off the labour element identified in your agreed quotation. Ask for it when you enquire, before accepting. Materials are excluded; see the <a href="/offer/">offer terms</a>.'),
    ])
    return out + '''</section><p class="guide-next">Explore <a href="/painting-decorating/">painting &amp; decorating</a>, <a href="/wallpapering/">wallpaper hanging</a> or our <a href="/areas/hornsey/">Hornsey N8 services</a>. For advice about your own brief, call <a href="tel:+447557954457">07557 954457</a>.</p></article>'''
