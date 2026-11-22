"""Useful local landing pages grounded in ATD's confirmed coverage."""
from html import escape

AREA_PAGES = {
 '/areas/hornsey/': {
  'title':'Painters, Decorators & Wallpapering in Hornsey N8',
  'description':'Based in Hornsey N8, ATD offers painting, wallpapering and refurbishment quotations. See services, what to send and how to plan work in an occupied home.',
  'label':'Hornsey N8', 'image_slug':'living-room',
 },
 '/areas/crouch-end/': {
  'title':'Painting, Decorating & Refurbishments in Crouch End',
  'description':'Discuss decorating, wallpapering and refurbishment work in Crouch End with ATD. See a real interior decorating and terrace project, with the customer’s review, and request a free quote.',
  'label':'Crouch End', 'image_slug':'project-story-058',
 },
}

AREA_PAGES.update({
 '/areas/muswell-hill/': {
  'title':'Painters & Decorators in Muswell Hill N10',
  'description':'Painting, decorating and wallpapering in Muswell Hill N10 from ATD, based nearby in Hornsey N8. Period-home preparation, written quotes and real customer reviews.',
  'label':'Muswell Hill', 'image_slug':'hallway',
 },
 '/areas/highgate/': {
  'title':'Painters & Decorators in Highgate N6',
  'description':'Interior and exterior decorating and wallpaper hanging in Highgate N6 from ATD, based a short drive away in Hornsey N8. Free written quotations.',
  'label':'Highgate', 'image_slug':'white-bay-windows-photo',
 },
 '/areas/harringay/': {
  'title':'Painters & Decorators in Harringay N4 & N8',
  'description':'Painting, decorating and wallpapering in Harringay from ATD, based right next door in Hornsey N8. Rooms, hallways, stairs and house fronts. Free written quotes.',
  'label':'Harringay', 'image_slug':'cream-hallway-doors-photo',
 },
 '/areas/wood-green/': {
  'title':'Painters & Decorators in Wood Green N22',
  'description':'Painting, decorating and wallpapering for homes, flats and landlords in Wood Green N22, from ATD in nearby Hornsey N8. Free written quotations.',
  'label':'Wood Green', 'image_slug':'furnished-white-living-room-photo',
 },
})

LOCAL = {
 '/areas/muswell-hill/': dict(name='Muswell Hill', code='N10',
  intro='ATD North London Painters is based in Hornsey N8, a short drive from Muswell Hill. We decorate houses and flats across N10: single rooms, hallways and staircases, wallpaper feature walls and house fronts.',
  head='Period homes.<br><em>Careful preparation.</em>',
  local=['Many Muswell Hill homes are Edwardian, with cornicing, picture rails, panelled doors and long staircases. A good finish on these features depends on preparation: filling and sanding, careful cutting-in along mouldings, and protecting original floors.',
         'If your property is in a conservation area, tell us before quoting any work on the front of the house. Colour and material choices for the front may need checking first.']),
 '/areas/highgate/': dict(name='Highgate', code='N6',
  intro='ATD North London Painters is based in Hornsey N8, a short drive from Highgate. We take on interior decorating, wallpaper hanging and exterior painting for houses and flats across N6.',
  head='Inside and out.<br><em>Finished properly.</em>',
  local=['Highgate has many older houses with sash windows, timber doors and painted render. Exterior work on these surfaces needs the right preparation and coatings, and safe access planned in advance. We cover all of this in your written quotation.',
         'Parts of Highgate are in conservation areas. If you are planning to change the colour of a front door or the front of the house, check whether any restrictions apply before work is booked.']),
 '/areas/harringay/': dict(name='Harringay', code='N4 & N8',
  intro='ATD North London Painters is based in Hornsey N8, right next to Harringay. We decorate the area’s terraced houses and flats, from a single bedroom to hallways, stairs and the front of the house.',
  head='Right next door.<br><em>Easy to plan.</em>',
  local=['Harringay’s terraced houses often have long, narrow hallways and stairwells, where getting good access and protecting the floors matters as much as the paint itself. Tell us which rooms need to stay usable while we work.',
         'Being so close, we can usually come and look at the job if one is needed before a final quotation. Send photos first so we can discuss the scope.']),
 '/areas/wood-green/': dict(name='Wood Green', code='N22',
  intro='ATD North London Painters is based in Hornsey N8, close to Wood Green. We decorate houses and flats in N22 for homeowners and landlords, including refreshes between tenancies and full rooms of wallpaper.',
  head='Homes and lets.<br><em>A clean, durable finish.</em>',
  local=['For landlords, tell us when the property will be empty and which rooms are included. A refresh between tenancies can be planned room by room, with paint finishes chosen to stand up to everyday wear.',
         'For homeowners, send photos of each room and any marks, cracks or damp patches you have noticed. These affect how much preparation is needed, which is set out in your quotation.']),
}

AREA_PAGES.update({
 '/areas/islington/': {
  'title':'Painters & Decorators in Islington N1, N5 & N7',
  'description':'Painting, decorating and wallpapering in Islington from ATD, based in Hornsey N8. Georgian and Victorian homes, flats and lets. Fully insured, free written quotes.',
  'label':'Islington', 'image_slug':'staircase-panelling-detail-photo',
 },
 '/areas/camden/': {
  'title':'Painters & Decorators in Camden Town & NW1',
  'description':'Painting, decorating and wallpapering in Camden Town, Kentish Town and NW1 from ATD North London Painters. Fully insured, 5.0 on Google, free written quotes.',
  'label':'Camden', 'image_slug':'dining-room-refresh-photo',
 },
 '/areas/hampstead/': {
  'title':'Painters & Decorators in Hampstead NW3',
  'description':'Interior decorating, wallpaper hanging and exterior painting in Hampstead and Belsize Park NW3 from ATD. Careful preparation, fully insured, free written quotes.',
  'label':'Hampstead', 'image_slug':'white-bay-windows-photo',
 },
 '/areas/finchley/': {
  'title':'Painters & Decorators in Finchley N3 & N12',
  'description':'Painting, decorating and wallpapering in Finchley and East Finchley from ATD, based nearby in Hornsey N8. Houses, flats and lets. Free written quotations.',
  'label':'Finchley', 'image_slug':'furnished-white-living-room-photo',
 },
 '/areas/tottenham/': {
  'title':'Painters & Decorators in Tottenham N15 & N17',
  'description':'Painting, decorating and wallpapering in Tottenham from ATD, based nearby in Hornsey N8. Homes, flats and refreshes between tenancies. Free written quotes.',
  'label':'Tottenham', 'image_slug':'room-decorating-progress-photo',
 },
 '/areas/stoke-newington/': {
  'title':'Painters & Decorators in Stoke Newington N16',
  'description':'Painting, decorating and exterior work in Stoke Newington and Stamford Hill N16 from ATD. See a real N16 project with the customer’s review. Free quotes.',
  'label':'Stoke Newington', 'image_slug':'green-entrance-finish-photo',
 },
 '/areas/kensington-chelsea/': {
  'title':'Painters & Decorators in Kensington & Chelsea',
  'description':'Interior decorating, wallpaper hanging and exterior painting in Kensington and Chelsea from ATD North London Painters. Fully insured, free written quotations.',
  'label':'Kensington & Chelsea', 'image_slug':'textured-bedroom-wallpaper-context-photo',
 },
 '/areas/notting-hill/': {
  'title':'Painters & Decorators in Notting Hill W11',
  'description':'Painting, decorating and wallpapering in Notting Hill W11 from ATD North London Painters. Period homes, flats and house fronts. Fully insured, free written quotes.',
  'label':'Notting Hill', 'image_slug':'blue-front-door-photo',
 },
})

_LONDON_BASE='ATD North London Painters is based in Hornsey N8 and takes on painting and decorating work across London.'
_LONDON_COVER='Yes. We are based in Hornsey N8 and work across London. Send your postcode and we will confirm the details, including parking and access.'
LOCAL.update({
 '/areas/islington/': dict(name='Islington', code='N1 · N5 · N7',
  intro='ATD North London Painters is based in Hornsey N8, a short drive from Islington. We decorate houses and flats across N1, N5 and N7: single rooms, hallways and staircases, wallpaper feature walls and house fronts.',
  head='Georgian and Victorian homes.<br><em>Finished with care.</em>',
  local=['Many Islington homes are Georgian or Victorian terraces with tall ceilings, cornicing, sash windows and long staircases. Good results on these features come from preparation: filling, sanding, careful cutting-in and protecting original floors.',
         'Much of Islington is in conservation areas. If you want to change the colour of a front door, railings or the front of the house, check whether any restrictions apply before work is booked.']),
 '/areas/camden/': dict(name='Camden', code='NW1 · NW5',
  intro='ATD North London Painters is based in Hornsey N8 and covers Camden Town, Kentish Town and the surrounding NW1 and NW5 streets. We decorate houses and flats, from a single room to a whole property.',
  head='Houses and flats.<br><em>A clean, lasting finish.</em>',
  local=['Camden has a mix of Victorian terraces, converted flats and newer apartments. For flats, tell us about access, lifts, parking and any building rules on working hours, so the job can be planned properly.',
         'For landlords and letting agents, we can refresh a property between tenancies room by room, with hard-wearing finishes chosen for everyday use.'],
  base=_LONDON_BASE, cover=_LONDON_COVER),
 '/areas/hampstead/': dict(name='Hampstead', code='NW3',
  intro='ATD North London Painters is based in Hornsey N8 and works in Hampstead and Belsize Park. We take on interior decorating, wallpaper hanging and exterior painting for houses and flats across NW3.',
  head='Period character.<br><em>Careful preparation.</em>',
  local=['Hampstead’s period houses often have panelled doors, decorative mouldings, sash windows and high ceilings. These surfaces need patient preparation before any paint goes on, and that preparation is listed in your written quotation.',
         'Much of Hampstead is in conservation areas. If you are planning changes to the front of the house, check whether any restrictions apply before work is booked.'],
  base=_LONDON_BASE, cover=_LONDON_COVER),
 '/areas/finchley/': dict(name='Finchley', code='N2 · N3 · N12',
  intro='ATD North London Painters is based in Hornsey N8, a short drive from Finchley. We decorate houses and flats in East Finchley, Finchley Central and North Finchley, from a single room to the whole house.',
  head='Family homes.<br><em>Room by room.</em>',
  local=['Many Finchley homes are family houses where people keep living while the work happens. Tell us which rooms need to stay usable, and we can plan the work in a sensible order around you.',
         'Send photos of each room and any cracks, marks or damp patches you have noticed. These affect how much preparation is needed, which is set out in your quotation.']),
 '/areas/tottenham/': dict(name='Tottenham', code='N15 · N17',
  intro='ATD North London Painters is based in Hornsey N8, close to Tottenham. We decorate houses and flats across N15 and N17 for homeowners and landlords, including refreshes between tenancies.',
  head='Homes and lets.<br><em>A durable finish.</em>',
  local=['For landlords, tell us when the property will be empty and which rooms are included. A refresh between tenancies can be planned room by room, with finishes chosen to stand up to everyday wear.',
         'For homeowners, send photos of each room and any marks or damage. Being close by, we can usually come and look at the job if a visit is needed before a final quotation.']),
 '/areas/stoke-newington/': dict(name='Stoke Newington', code='N16',
  intro='ATD North London Painters is based in Hornsey N8 and works across Stoke Newington and Stamford Hill. We decorate houses and flats in N16, inside and out.',
  head='Inside and out.<br><em>A real N16 project.</em>',
  local=['In Stamford Hill N16 we decorated an entrance, glazed doors and finishing details for John Burgess, who reviewed us on Google for “thorough preparation and great attention to detail”.',
         'Stoke Newington’s Victorian terraces often have long hallways, staircases and timber sash windows. Tell us which surfaces need work and send photos so we can discuss the preparation needed.'],
  link=('/projects/stamford-hill-exterior/','See the Stamford Hill N16 project and review ↗')),
 '/areas/kensington-chelsea/': dict(name='Kensington & Chelsea', code='W8 · SW3 · SW10',
  intro='ATD North London Painters takes on painting, decorating and wallpapering work in Kensington and Chelsea. We decorate houses and flats, from a single feature wall to a whole property.',
  head='High standards.<br><em>A careful finish.</em>',
  local=['Period houses and mansion flats in Kensington and Chelsea often have detailed mouldings, panelling and high ceilings. The finish depends on preparation, so your written quotation lists exactly what is included.',
         'For flats, tell us about building access, parking, lifts and any managing-agent rules on working hours. Much of the borough is in conservation areas, so check any restrictions before planning exterior colour changes.'],
  base=_LONDON_BASE, cover=_LONDON_COVER),
 '/areas/notting-hill/': dict(name='Notting Hill', code='W11',
  intro='ATD North London Painters takes on painting, decorating and wallpapering work in Notting Hill. We decorate houses and flats in W11, inside and out.',
  head='Colourful streets.<br><em>Well-prepared surfaces.</em>',
  local=['Notting Hill’s stucco-fronted houses and painted terraces need the right preparation and exterior coatings to last, and safe access planned in advance. We cover all of this in your written quotation.',
         'Much of Notting Hill is in conservation areas. If you are planning to change the colour of a front door or the front of the house, check whether any restrictions apply before work is booked.'],
  base=_LONDON_BASE, cover=_LONDON_COVER),
})

def area_content(route, button, faq):
 if route in LOCAL:
  return local_area_content(route, button, faq)
 hornsey=route=='/areas/hornsey/'
 name='Hornsey N8' if hornsey else 'Crouch End'
 intro=('Based in Hornsey N8, ATD North London Painters works with homeowners, landlords and local businesses on interior and exterior decorating, wallpapering and property refurbishments.' if hornsey else 'ATD North London Painters is based nearby in Hornsey and covers Crouch End for painting, decorating, wallpapering and agreed-scope property refurbishment work.')
 body='<section class="page-intro wrap"><p class="kicker">ATD NORTH LONDON PAINTERS</p><h1>Painting &amp; decorating<br><em>in '+name+'.</em></h1><p class="lead">'+intro+'</p>'+button('Request a free quote')+'</section>'
 scopes=[('Painting & decorating','/painting-decorating/','Rooms, ceilings, doors and woodwork, or an exterior refresh. Send photographs of the existing surfaces and explain which areas need attention.'),('Wallpapering','/wallpapering/','Feature walls or complete rooms. Share your chosen wallcovering, wall sizes and whether old paper needs removing.'),('Bathroom refurbishment','/bathroom-refurbishments/','Tell us what you want to keep or replace, the room dimensions and whether this is your only bathroom. The quotation sets out the agreed work and specialist arrangements.'),('House & flat refurbishment','/full-refurbishments/','For several rooms or a wider property project, share your priorities, a floor plan if available, and your intended timing. Access and the sequence of work are discussed before agreement.')]
 body+='<section class="section wrap local-services"><p class="kicker">CHOOSE THE WORK YOU NEED</p><h2>Services in '+name+'</h2><div class="local-service-grid">'+''.join('<article><h3><a href="'+url+'">'+label+' ↗</a></h3><p>'+text+'</p></article>' for label,url,text in scopes)+'</div></section>'
 body+='<p class="wrap local-exterior-link">Planning work outside? See our <a href="/exterior-painting/">exterior painting service</a> for doors, timber windows, house fronts and railings, with a focused quote checklist.</p>'
 if hornsey:
  body+='<section class="wrap project-start"><div><p class="kicker">A LOCAL STARTING POINT</p><h2>One room or a wider refresh?</h2></div><div><p>For a focused decorating job, list the walls, ceilings and woodwork you want included. For several rooms, send a room-by-room list so we can discuss priorities and a practical sequence.</p><p>If you will be living in the property during the work, let us know which rooms need to remain usable. Furniture, access and drying times can then be considered in the quotation.</p><a class="text-link" href="/projects/crouch-end-redecoration/">See a nearby Crouch End decorating project ↗</a></div></section>'
 else:
  body+='<section class="wrap project-start"><div><p class="kicker">A REAL CROUCH END PROJECT</p><h2>Colour inside.<br><em>Terrace details outside.</em></h2></div><div><p>At the same Crouch End property, our photographs show coral-painted shelving and chimney-wall details indoors, alongside the terrace framework and decking outside.</p><p>The full project page brings these photographs together with Julian Smilg’s Google review. The decorating and terrace work belong to one customer project.</p><a class="text-link" href="/projects/crouch-end-redecoration/">See the Crouch End decorating, terrace and customer review ↗</a></div></section>'
 body+='<section class="section wrap"><div class="section-heading"><div><p class="kicker">MAKE YOUR ENQUIRY USEFUL</p><h2>Start with your space.</h2></div><p>A few details help us discuss the next step.<br>A visit may be needed before a final written quotation.</p></div><div class="process-grid"><article><span class="step">01</span><h3>Postcode & photos</h3><p>Send your property postcode, a wide view and closer photographs of any damaged or unusual surfaces.</p></article><article><span class="step">02</span><h3>Scope & access</h3><p>Tell us what you want changed, approximate dimensions, access arrangements and whether the property will be occupied.</p></article><article><span class="step">03</span><h3>Timing & finishes</h3><p>Share your preferred timeframe and any chosen paint or wallpaper. Preparation, materials, exclusions and timing are agreed in writing.</p></article></div></section>'
 body+='<section class="section faq-section"><div class="wrap faq-grid"><div><p class="kicker">BEFORE YOU ENQUIRE</p><h2>Your local project.</h2></div>'+faq([('Do you offer free quotations in '+name+'?','Yes. Call ATD on 07557 954457, send photos on WhatsApp, or use the project form. Availability and whether a visit is needed are discussed after reviewing the details.'),('Can I request just one room or feature wall?','Yes. Explain which surfaces need work and include photos. The final scope depends on the existing condition and the finish you want.'),('Does sending the form confirm a booking?','No. Your request goes straight to Landi to review, and no email confirmation is needed. Work starts only after the scope, price and practical arrangements have been agreed.')])+'</div></section>'
 body+='<section class="connect wrap"><h2>Discuss your '+name+' project.</h2><p>Call or WhatsApp 07557 954457. ATD North London Painters is based in Hornsey and serves nearby North London areas.</p>'+button('Send photos on WhatsApp','https://wa.me/447557954457','outline')+'<p class="fine"><a href="/areas/">All areas we cover ↗</a></p></section>'
 return body


def local_area_content(route, button, faq):
 a=LOCAL[route]; name=a['name']
 body='<section class="page-intro wrap"><p class="kicker">ATD NORTH LONDON PAINTERS · '+escape(a['code'])+'</p><h1>Painters &amp; decorators<br><em>in '+escape(name)+'.</em></h1><p class="lead">'+escape(a['intro'])+'</p><p class="hero-service-line">Fully insured · 8+ years’ experience · 5.0 on Google from 23 reviews</p>'+button('Request a free quote')+'</section>'
 body+='<section class="wrap project-start"><div><p class="kicker">DECORATING IN '+escape(name.upper())+'</p><h2>'+a['head']+'</h2></div><div>'+''.join('<p>'+escape(t)+'</p>' for t in a['local'])+'<a class="text-link" href="'+a.get('link',('/#before-after',''))[0]+'">'+escape(a.get('link',('','See before-and-after photos of our work ↗'))[1])+'</a></div></section>'
 scopes=[('Painting & decorating','/painting-decorating/','Walls, ceilings, doors, skirting and staircases, from one room to the whole house.'),('Wallpapering','/wallpapering/','Feature walls and full rooms. Send your chosen paper, the wall sizes and whether old paper needs removing.'),('Exterior painting','/exterior-painting/','Front doors, timber windows, render and railings, with preparation and access planned in the quotation.')]
 body+='<section class="section wrap local-services"><p class="kicker">WHAT WE DO IN '+escape(name.upper())+'</p><h2>Services in '+escape(name)+'</h2><div class="local-service-grid">'+''.join('<article><h3><a href="'+url+'">'+label+' ↗</a></h3><p>'+text+'</p></article>' for label,url,text in scopes)+'</div><p class="also-offer">Also: <a href="/bathroom-refurbishments/">bathroom refurbishments ↗</a> and <a href="/full-refurbishments/">full refurbishments ↗</a>.</p></section>'
 body+='<section class="section wrap"><div class="section-heading"><div><p class="kicker">GET A QUICK, ACCURATE QUOTE</p><h2>What to send us.</h2></div><p>A visit may be needed before a final written quotation.</p></div><div class="process-grid"><article><span class="step">01</span><h3>Postcode & photos</h3><p>Your '+escape(a['code'])+' postcode, a wide photo of each room or surface, and close-ups of any damage.</p></article><article><span class="step">02</span><h3>What you want done</h3><p>Which walls, ceilings, woodwork or surfaces are included, and roughly how big the rooms are.</p></article><article><span class="step">03</span><h3>Timing & finishes</h3><p>When you would like the work done, and any paint colours or wallpaper you have chosen.</p></article></div></section>'
 body+='<section class="section faq-section"><div class="wrap faq-grid"><div><p class="kicker">BEFORE YOU ENQUIRE</p><h2>Your '+escape(name)+' project.</h2></div>'+faq([('Do you cover all of '+name+'?',a.get('cover','Yes. We are based nearby in Hornsey N8. Send your postcode and we will confirm coverage and discuss access and parking.')),('Are you insured?','Yes. ATD is fully insured, and Landi has more than 8 years of painting and decorating experience.'),('Is the quotation free?','Yes. Call 07557 954457, send photos on WhatsApp or use the online form. Your written quotation lists the preparation, materials and finish included.'),('Does sending the form confirm a booking?','No. Your request goes straight to Landi to review, and no email confirmation is needed. Work starts only after the scope, price and arrangements are agreed.')])+'</div></section>'
 body+='<section class="connect wrap"><h2>Discuss your '+escape(name)+' project.</h2><p>Call or WhatsApp 07557 954457. '+escape(a.get('base','ATD North London Painters is based in Hornsey N8 and covers '+name+' and nearby North London.'))+'</p>'+button('Send photos on WhatsApp','https://wa.me/447557954457','outline')+'<p class="fine"><a href="/areas/">All areas we cover ↗</a></p></section>'
 return body
