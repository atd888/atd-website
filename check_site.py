from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit,unquote
import json
D=Path(__file__).resolve().parent/'dist'
class Page(HTMLParser):
 def __init__(self):super().__init__();self.refs=[];self.h1=0;self.lang=None;self.alts=[]
 def handle_starttag(self,t,a):
  a=dict(a)
  if t=='html':self.lang=a.get('lang')
  if t=='h1':self.h1+=1
  if t=='img':self.alts.append(a.get('alt'))
  for k in ('href','src'):
   if k in a:self.refs.append(a[k])
errors=[];count=0
for f in D.rglob('*.html'):
 p=Page();p.feed(f.read_text());count+=1
 if p.h1!=1:errors.append(f'{f}: H1 count {p.h1}')
 if p.lang!='en-GB':errors.append(f'{f}: language')
 if any(a is None for a in p.alts):errors.append(f'{f}: image missing alt')
 for r in p.refs:
  u=urlsplit(r)
  if not r.startswith('/') or r.startswith('//'):continue
  target=D/unquote(u.path.lstrip('/'))
  if not target.exists():errors.append(f'{f}: missing {r}')
assert not errors,'\n'.join(errors)
print(f'PASS: {count} HTML documents; local page/asset targets exist; one H1 per document; image alternatives; language set.')
print('WebP assets:',sum(f.stat().st_size for f in (D/'assets').glob('*.webp')),'bytes')
