"""Dependency-free check for this static site's local files and fragment links."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import re,sys
ROOT=Path(__file__).resolve().parent.parent
class Scan(HTMLParser):
 def __init__(self,text):
  super().__init__();self.links=[];self.ids=set();self.duplicate_ids=[];self.images=[];self.feed(text)
 def handle_starttag(self,t,attrs):
  a=dict(attrs)
  if 'id' in a:
   if a['id'] in self.ids:self.duplicate_ids.append(a['id'])
   self.ids.add(a['id'])
  for k in ('href','src'):
   if k in a:self.links.append(a[k])
  if t=='img':self.images.append(a)
pages={p:Scan(p.read_text()) for p in ROOT.glob('*.html')};errors=[];count=0
for p,doc in pages.items():
 for dup in doc.duplicate_ids:errors.append(f'{p.name}: duplicate ID {dup}')
 for img in doc.images:
  if not img.get('alt') and img.get('id')!='large-image':errors.append(f'{p.name}: missing image alt text')
 for u in doc.links:
  parsed=urlsplit(u)
  if parsed.scheme or parsed.netloc:continue
  target=ROOT/unquote(parsed.path) if parsed.path else p
  if not target.exists():errors.append(f'{p.name}: missing {u}')
  elif parsed.fragment and target in pages and unquote(parsed.fragment) not in pages[target].ids:errors.append(f'{p.name}: missing fragment {u}')
  count+=1
for name in ('index.html','.nojekyll','assets/style.css','assets/app.js','assets/search-index.js'):
 if not (ROOT/name).exists():errors.append('Required file missing: '+name)
media=list((ROOT/'assets/media').glob('*.png'))
print(f'{len(pages)} HTML pages; {count} local references; {len(media)} screenshots.')
if errors:
 print('\n'.join(errors));sys.exit(1)
print('PASS: local files, fragment links, image alt text and unique IDs.')
print('External wiki destinations and browser rendering require separate verification.')
