from pathlib import Path
from html import escape
import json
from urllib.parse import quote

def project_story_html():
 stories=json.loads((Path(__file__).parent/'project-stories.json').read_text())
 result='<section class="section wrap" id="project-stories"><div class="section-heading"><div><p class="kicker">LOOK BEYOND THE FINISH</p><h2>Real projects.<br><em>The work behind them.</em></h2></div><p>Open a project to see its photographs and stages.<br>Selected from the ATD project collection.</p></div><div class="project-stories-grid">'
 for story in stories:
  title=escape(story['title']);hero=story['photos'][-1]
  meta=escape(story['service_label'])+(' · '+escape(story['area']) if story.get('area') else '')
  shown='<h3>Work shown</h3><ul>'+''.join('<li>'+escape(item)+'</li>' for item in story['work_shown'])+'</ul>'
  wa='https://wa.me/447557954457?text='+quote('Hi ATD, I would like to discuss a project similar to '+story['title']+'. My postcode is: ')
  result+='<details class="project-story" id="story-'+story['id']+'"><summary><img src="/assets/'+hero['slug']+'-640.webp" alt="'+escape(hero['caption'])+'" loading="lazy" decoding="async"><span><small class="story-meta">'+meta+'</small><strong>'+title+'</strong><span class="story-open">View project story <b aria-hidden="true">+</b></span></span></summary><div class="project-story-body"><p>'+escape(story['text'])+'</p>'+shown+'<div class="project-story-photos">'
  for photo in story['photos']:
   result+='<figure><a href="/assets/'+photo['slug']+'-1200.webp" target="_blank" rel="noopener noreferrer" aria-label="Enlarge: '+escape(photo['caption'])+'"><img src="/assets/'+photo['slug']+'-640.webp" alt="'+escape(photo['caption'])+'" loading="lazy" decoding="async"></a><figcaption>'+escape(photo['caption'])+'</figcaption></figure>'
  result+='</div>'
  if story.get('review') and not story.get('page'):
   review=story['review']
   result+='<blockquote>“'+escape(review['excerpt'])+'”</blockquote><p>'+escape(review['name'])+' · Google review · '+str(review['rating'])+'/5<br><a class="text-link" href="'+escape(review['url'])+'" target="_blank" rel="noopener noreferrer">Read the original Google review ↗</a></p>'
  if story.get('page'):
   result+='<p><a class="text-link" href="'+escape(story['page'])+'">Read the full project and customer review ↗</a></p>'
  result+='<a class="button" href="/enquiry/booking.html?service='+story['service']+'">Request a quote for similar work ↗</a><a class="story-whatsapp" href="'+escape(wa)+'">Discuss this project on WhatsApp ↗</a></div></details>'
 return result+'</div><p class="fine">Photos show individual projects and stages of work. Your scope, materials and arrangements are agreed separately in your written quotation.</p></section>'
