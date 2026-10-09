from pathlib import Path
from html import escape
import re,json,sys
sys.path.insert(0,str(Path(__file__).parent))
from content import PAGES,SOURCES,WIKI
import expand
ROOT=Path(__file__).resolve().parent.parent

def plain(s):return re.sub(r'<[^>]+>',' ',s)
def slug(s):return re.sub('[^a-z0-9]+','-',s.lower()).strip('-')
def card(page):
 return f'<a class="guide-card" href="{page["slug"]}.html"><span class="card-icon" aria-hidden="true">{page["icon"]}</span><span class="eyebrow">{page["group"]}</span><h3>{page["title"]}</h3><p>{page["desc"]}</p><span class="card-bottom">Read guide <span aria-hidden="true"></span></span></a>'

def shell(page,content,toc=''):
 ident=page['slug'];title=page['title'];groups={}
 for pg in PAGES:groups.setdefault(pg['group'],[]).append(pg)
 nav='<a class="nav-home '+('active' if ident=='index' else '')+'" href="index.html" '+('aria-current="page"' if ident=='index' else '')+'>⌂ <span>Welcome</span></a>'
 for group,items in groups.items():
  nav+='<div class="nav-group"><h2>'+group+'</h2>'+''.join('<a href="'+pg['slug']+'.html" data-guide="'+pg['slug']+'" '+('class="active" aria-current="page"' if pg['slug']==ident else '')+'><span class="nav-icon" aria-hidden="true">'+pg['icon']+'</span><span>'+pg['title']+'</span></a>' for pg in items)+'</div>'
 return f'''<!doctype html>
<html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{escape(title)} · Infinity Guide</title><meta name="description" content="{escape(page['desc'],quote=True)}"><meta name="theme-color" content="#0c1716"><meta name="robots" content="noindex,nofollow"><link rel="icon" href="assets/favicon.svg"><link rel="stylesheet" href="assets/style.css"><script src="assets/early.js"></script><script defer src="assets/search-index.js"></script><script defer src="assets/app.js"></script></head>
<body data-page="{ident}"><a class="skip-link" href="#main">Skip to content</a>
<header class="topbar"><button class="icon-button mobile-menu" id="menu-toggle" aria-label="Open navigation" aria-expanded="false" aria-controls="sidebar">☰</button><a href="index.html" class="brand"><span class="brand-mark" aria-hidden="true">∞</span><span>INFINITY <b>GUIDE</b><small>RUNESCAPE: DRAGONWILDS</small></span></a><div class="top-tools"><button class="search-trigger" data-open-search><span aria-hidden="true">⌕</span> <span>Search the guide…</span><kbd>/</kbd></button><a class="wiki-top" href="https://dragonwilds.runescape.wiki/" target="_blank" rel="noopener">Official wiki</a><button class="icon-button" id="theme-toggle" aria-label="Switch colour theme">◐</button></div></header>
<button id="nav-overlay" aria-label="Close navigation" hidden></button><aside id="sidebar" class="sidebar"><div class="server-label"><span class="eyebrow">YOUR COMMUNITY</span><strong>DragonInfinity</strong><span>S3RVNetwork · S3rvStudios</span></div><nav aria-label="Guide navigation">{nav}</nav><div class="sidebar-foot"><span class="eyebrow">YOUR FIELD JOURNAL</span><p><span id="read-total">0</span> / {len(PAGES)-1} guides read</p><div class="progress-track"><span id="read-bar"></span></div><button class="text-button" id="show-saved">View saved guides</button><small>Progress stays on this browser</small></div></aside>
<main id="main" class="main" tabindex="-1">{content}<footer><div><strong>∞ &nbsp; INFINITY GUIDE</strong><p>For DragonInfinity • Hosted by S3RVNetwork<br>Part of S3rvStudios</p></div><div><a href="sources.html">Sources, credits & privacy</a><p>Independent fan guide. RuneScape © Jagex.<br>Reviewed 9 October 2026 · Static edition</p></div></footer></main>{toc}
<dialog id="search-dialog" aria-labelledby="search-title"><div class="dialog-heading"><h2 id="search-title">Search Infinity Guide</h2><button class="icon-button" data-close-dialog aria-label="Close search">×</button></div><label class="sr-only" for="site-search">Search all guides</label><input id="site-search" type="search" placeholder="Try: camp, copper, dodge, password…" autocomplete="off"><p id="search-status" class="small" aria-live="polite">Search guide titles, instructions and topics.</p><div id="search-results"></div><p class="small">Press Esc to close. Use Tab to move through results.</p></dialog>
<dialog id="image-dialog" aria-label="Enlarged guide image"><button class="icon-button image-close" data-close-dialog aria-label="Close image">×</button><img id="large-image" alt=""><p id="image-caption"></p><a id="image-original" target="_blank" rel="noopener">Open full-size image</a></dialog>
<dialog id="saved-dialog" aria-labelledby="saved-title"><div class="dialog-heading"><h2 id="saved-title">Your saved guides</h2><button class="icon-button" data-close-dialog aria-label="Close saved guides">×</button></div><div id="saved-list"></div></dialog><div id="toast" role="status" aria-live="polite"></div><noscript><div class="noscript">All guides are readable without JavaScript. Enable JavaScript for search, saved progress and image enlargement.</div></noscript></body></html>'''

home=dict(slug='index',title='Welcome to Ashenfall',desc='Infinity Guide: a beginner-friendly field guide to RuneScape: Dragonwilds for the DragonInfinity community.')
content='''<section class="hero"><div class="hero-shade"></div><div class="hero-content"><div class="hero-kicker"><span class="tiny-rune">✦</span> THE DRAGONINFINITY FIELD GUIDE</div><h1>Every legend<br>starts <em>somewhere.</em></h1><p>New to Dragonwilds? Find your feet, find our camp,<br class="desktop-break"> and make Ashenfall feel like home.</p><div class="hero-actions"><a class="button" href="getting-started.html">Start your adventure</a><a class="button glass" href="connect.html">Join DragonInfinity</a></div><div class="hero-caption">RuneScape: Dragonwilds · An independent community guide</div></div></section>
<div class="home-body"><div class="welcome-strip"><div><span class="eyebrow">A PLACE TO START. A WORLD TO DISCOVER.</span><h2>Welcome, adventurer.</h2><p>You don’t need RuneScape experience. Just take it one step at a time.</p></div><a href="overview.html" class="inline-link">Discover Ashenfall</a></div>
<section class="first-path" aria-labelledby="first-title"><div class="section-heading"><h2 id="first-title">Your first hour, made simple.</h2><span class="small">THREE GOOD FIRST STEPS</span></div><div class="path-grid"><a href="connect.html"><span class="step-no">01</span><div><h3>Join the world</h3><p>Find DragonInfinity and get connected.</p></div><span aria-hidden="true"></span></a><a href="getting-started.html"><span class="step-no">02</span><div><h3>Learn the basics</h3><p>Choose your start. Get comfortable.</p></div><span aria-hidden="true"></span></a><a href="basecamp.html"><span class="step-no">03</span><div><h3>Find your people</h3><p>Follow the map and settle into camp.</p></div><span aria-hidden="true"></span></a></div></section>
<section class="explore"><div class="section-heading"><div><span class="eyebrow">THE KNOWLEDGE TO KEEP GOING</span><h2>What will you learn today?</h2></div><button class="text-button" data-open-search>Search all guides</button></div><div class="guide-grid">'''
for key in ['skills','quests','crafting','combat','building','resources']:
 content+=card(next(x for x in PAGES if x['slug']==key))
content+='''</div></section><section class="explore library-section"><div class="section-heading"><div><span class="eyebrow">THE INFINITY LIBRARY</span><h2>Deep dives & walkthroughs</h2></div></div><div class="library-links">'''
for group in ['Quest walkthroughs','Crafting stations','Skills deep dives','Core systems','World & lore']:
 content+='<details class="library-category" open><summary>'+group+' <span>Explore →</span></summary><div class="library-chip-grid">'+''.join('<a href="'+pg['slug']+'.html">'+pg['icon']+' &nbsp;'+pg['title']+'</a>' for pg in PAGES if pg['group']==group)+'</div></details>'
content+='''</div></section><div class="feature-row"><a class="camp-feature" href="basecamp.html"><div><span class="eyebrow">YOUR NEXT DESTINATION</span><h2>A bed. A campfire.<br>A place to call home.</h2><p>Follow our annotated route to the clan village.</p><span class="inline-link">Find basecamp</span></div><img src="assets/media/HowToGetToClanVillage.png" alt="Annotated map showing the route to DragonInfinity camp" loading="lazy"></a><a class="roadmap-feature" href="overview.html#2026-2027-roadmap"><span class="eyebrow">BEYOND THE HORIZON</span><h2>The next chapter<br>of Ashenfall.</h2><p>Luminance and the Blood Crystal Saga. Explore Jagex’s announced 2026 / 2027 plans.</p><span class="inline-link">View the roadmap</span><span class="roadmap-date">2026 — 2027</span></a></div><section class="help-banner"><div><span class="eyebrow">EVERY ADVENTURER NEEDS A HAND SOMETIMES</span><h2>Stuck? You’re in good company.</h2><p>Check common fixes, look up a term or explore the official wiki.</p></div><div><a href="troubleshooting.html" class="button secondary">Find help</a><a href="glossary.html" class="text-button">Beginner glossary</a></div></section></div>'''
(ROOT/'index.html').write_text(shell(home,content))
search=[]
for i,pg in enumerate(PAGES):
 secs=pg['sections'];totalwords=len(plain(' '.join(x[1] for x in secs)).split());mins=max(2,round(totalwords/190))
 actions='' if pg['slug']=='sources' else f'<button class="button secondary bookmark-button" data-bookmark="{pg["slug"]}" aria-pressed="false">Save guide</button><button class="text-button read-button" data-read="{pg["slug"]}" aria-pressed="false">Mark as read</button>'
 article=f'<div class="article-layout"><article class="article"><div class="breadcrumbs"><a href="index.html">Welcome</a><span>/</span>{pg["group"]}</div><header class="article-header"><span class="eyebrow">{pg["group"]}</span><h1>{pg["title"]}</h1><p class="lead">{pg["desc"]}</p><div class="article-meta"><span>{mins} MIN READ</span><span>REVIEWED 09 OCT 2026</span></div><div class="article-actions">{actions}<button class="text-button print-button">Print guide</button></div></header><details class="mobile-toc"><summary>On this page</summary><ul>'
 for heading,body in secs:article+=f'<li><a href="#{slug(heading)}">{heading}</a></li>'
 article+='</ul></details>'
 for heading,body in secs:article+=f'<section id="{slug(heading)}" class="article-section"><h2>{heading}</h2>{body}</section>'
 if pg['wiki'] or pg['sources']:
  article+='<section class="further" id="further-reading"><span class="eyebrow">GO A LITTLE DEEPER</span><h2>Further reading</h2><p>For exact requirements, detailed walkthroughs and more depth, visit the topic pages below.</p><div class="source-links">'
  for wiki in pg['wiki']:
   label=wiki.replace('_',' ').replace('RuneScape:Dragonwilds Wiki','Wiki home')
   url='https://dragonwilds.runescape.wiki/' if wiki=='RuneScape:Dragonwilds_Wiki' else WIKI+wiki
   article+=f'<a href="{url}" target="_blank" rel="noopener">Wiki · {label} <span></span></a>'
  for skey in pg['sources']:
   t,u=SOURCES[skey];article+=f'<a href="{u}" target="_blank" rel="noopener">{t} <span></span></a>'
  article+='</div></section>'
 if pg['related']:
  article+='<section class="related"><h2>Continue exploring</h2><div class="related-grid">'+''.join(card(next(x for x in PAGES if x['slug']==r)) for r in pg['related'])+'</div></section>'
 article+='</article><aside class="toc"><span class="eyebrow">ON THIS PAGE</span><nav aria-label="On this page">'+''.join(f'<a href="#{slug(h)}">{h}</a>' for h,b in secs)+('</nav><a href="#further-reading" class="toc-source">Sources & wiki links</a>' if pg['wiki'] or pg['sources'] else '</nav>')+'<div class="toc-note"><span aria-hidden="true">✦</span><p>One useful step at a time.<br>You’ll get there.</p></div></aside></div>'
 (ROOT/(pg['slug']+'.html')).write_text(shell(pg,article))
 search.append(dict(slug=pg['slug'],title=pg['title'],desc=pg['desc'],group=pg['group'],text=re.sub(r'\s+',' ',plain(' '.join(h+' '+b for h,b in secs)))))
(ROOT/'assets/search-index.js').write_text('window.GUIDE_INDEX='+json.dumps(search,ensure_ascii=False)+';')
(ROOT/'404.html').write_text(shell(dict(slug='404',title='This trail ends here',desc='Find your way back to Infinity Guide.'),'<div class="not-found"><span class="eyebrow">404 · UNCHARTED TERRITORY</span><h1>This trail ends here.</h1><p>The page may have moved. Return to the guide or search for what you need.</p><a class="button" href="index.html">Back to the guide</a><button class="button secondary" data-open-search>Search guides</button></div>'))
print('Built',len(PAGES)+2,'HTML files and search index.')
