(() => {
'use strict';
const $ = (s,root=document)=>root.querySelector(s);
const $$ = (s,root=document)=>Array.from(root.querySelectorAll(s));
const key='infinity-guide-v1';
let state={saved:[],read:[],checks:{}};
try {const data=JSON.parse(localStorage.getItem(key));if(data&&typeof data==='object')state={saved:Array.isArray(data.saved)?data.saved:[],read:Array.isArray(data.read)?data.read:[],checks:data.checks&&typeof data.checks==='object'?data.checks:{}};}catch{}
let timer;
function toast(msg){$('#toast').textContent=msg;$('#toast').classList.add('visible');clearTimeout(timer);timer=setTimeout(()=>$('#toast').classList.remove('visible'),2800);}
function save(){try{localStorage.setItem(key,JSON.stringify(state));}catch{toast('Browser storage is unavailable. Changes last for this page only.');}}
const index=(window.GUIDE_INDEX||[]).filter(p=>!p.alias);
function update(){
 $$('[data-bookmark]').forEach(b=>{const on=state.saved.includes(b.dataset.bookmark);b.setAttribute('aria-pressed',String(on));b.textContent=on?'Saved ✓':'Save guide';});
 $$('[data-read]').forEach(b=>{const on=state.read.includes(b.dataset.read);b.setAttribute('aria-pressed',String(on));b.textContent=on?'Read ✓':'Mark as read';});
 $$('[data-guide]').forEach(a=>a.dataset.complete=String(state.read.includes(a.dataset.guide)));
 const n=state.read.filter(s=>index.some(p=>p.slug===s&&s!=='sources')).length;
 $('#read-total').textContent=n;$('#read-bar').style.width=(n/Math.max(1,index.length-1)*100)+'%';
 $$('[data-check]').forEach(c=>c.checked=Boolean(state.checks[c.dataset.check]));
 $$('[data-checklist]').forEach(box=>$('.check-count',box).textContent=$$('input:checked',box).length+' / '+$$('input',box).length+' complete');
}
$$('[data-bookmark]').forEach(b=>b.addEventListener('click',()=>{const id=b.dataset.bookmark;state.saved=state.saved.includes(id)?state.saved.filter(x=>x!==id):[...state.saved,id];save();update();toast(state.saved.includes(id)?'Guide saved on this browser.':'Guide removed from saved.');}));
$$('[data-read]').forEach(b=>b.addEventListener('click',()=>{const id=b.dataset.read;state.read=state.read.includes(id)?state.read.filter(x=>x!==id):[...state.read,id];save();update();}));
$$('[data-check]').forEach(c=>c.addEventListener('change',()=>{state.checks[c.dataset.check]=c.checked;save();update();}));
$$('.reset-check').forEach(b=>b.addEventListener('click',()=>{const box=b.closest('[data-checklist]');$$('[data-check]',box).forEach(c=>delete state.checks[c.dataset.check]);save();update();}));
$('#clear-progress')?.addEventListener('click',()=>{if(confirm('Clear all saved guides, reading progress and checklists on this browser?')){state={saved:[],read:[],checks:{}};save();update();toast('Guide progress cleared.');}});
$('#theme-toggle').addEventListener('click',()=>{const theme=document.documentElement.dataset.theme==='light'?'dark':'light';document.documentElement.dataset.theme=theme;try{localStorage.setItem('infinity-theme',theme);}catch{}themeLabel();});
function themeLabel(){$('#theme-toggle').setAttribute('aria-label',document.documentElement.dataset.theme==='light'?'Switch to dark theme':'Switch to light theme');}
function setMenu(open){$('#sidebar').classList.toggle('open',open);$('#menu-toggle').setAttribute('aria-expanded',String(open));$('#menu-toggle').setAttribute('aria-label',open?'Close navigation':'Open navigation');$('#nav-overlay').hidden=!open;}
$('#menu-toggle').addEventListener('click',()=>setMenu(!$('#sidebar').classList.contains('open')));
$('#nav-overlay').addEventListener('click',()=>setMenu(false));
const media=matchMedia('(max-width:760px)');
function mobileNav(){if(!media.matches && $('#sidebar').classList.contains('open'))setMenu(false);if(media.matches&&!$('#sidebar').classList.contains('open'))$('#sidebar').setAttribute('inert','');else $('#sidebar').removeAttribute('inert');}
new MutationObserver(mobileNav).observe($('#sidebar'),{attributes:true,attributeFilter:['class']});
media.addEventListener('change',mobileNav);mobileNav();
function escape(s){return String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));}
function result(p,snippet){return '<a class="search-result" href="'+p.slug+'.html"><span class="eyebrow">'+escape(p.group)+'</span><strong>'+escape(p.title)+'</strong><p>'+escape(snippet||p.desc)+'</p></a>';}
function showSearch(){setMenu(false);$('#search-dialog').showModal();$('#site-search').focus();search();}
$$('[data-open-search]').forEach(b=>b.addEventListener('click',showSearch));
function search(){
 const q=$('#site-search').value.trim().toLowerCase();
 if(!q){$('#search-status').textContent='Popular starting points';$('#search-results').innerHTML=index.filter(p=>['getting-started','connect','basecamp','keybinds'].includes(p.slug)).map(p=>result(p)).join('');return;}
 const terms=q.split(/\s+/).filter(Boolean);
 const scored=index.map(p=>{const t=p.title.toLowerCase(),d=p.desc.toLowerCase(),all=(t+' '+d+' '+p.text).toLowerCase();if(!terms.every(x=>all.includes(x)))return null;return {p,score:terms.reduce((n,x)=>n+(t.includes(x)?8:0)+(d.includes(x)?3:0)+1,0)};}).filter(Boolean).sort((a,b)=>b.score-a.score);
 $('#search-status').textContent=scored.length+' guide'+(scored.length===1?'':'s')+' found for “'+q+'”';
 $('#search-results').innerHTML=scored.length?scored.map(({p})=>{let snippet=p.desc;const pos=p.text.toLowerCase().indexOf(terms[0]);if(pos>=0)snippet=(pos>50?'…':'')+p.text.slice(Math.max(0,pos-50),pos+145)+'…';return result(p,snippet);}).join(''):'<div class="empty-state"><strong>No matching guides yet.</strong><p>Try a shorter term such as “ore”, “camp” or “spell”. For a specific item, search the official wiki.</p><a href="https://dragonwilds.runescape.wiki/w/Special:Search?search='+encodeURIComponent(q)+'" target="_blank" rel="noopener">Search the wiki</a></div>';
}
$('#site-search').addEventListener('input',search);
$('#show-saved').addEventListener('click',()=>{const saved=index.filter(p=>state.saved.includes(p.slug));$('#saved-list').innerHTML=saved.length?saved.map(p=>result(p)).join(''):'<div class="empty-state"><p>No saved guides yet. Open a guide and choose <strong>Save guide</strong> to keep it here.</p></div>';setMenu(false);$('#saved-dialog').showModal();});
$$('[data-close-dialog]').forEach(b=>b.addEventListener('click',()=>b.closest('dialog').close()));
$$('dialog').forEach(d=>d.addEventListener('click',e=>{if(e.target===d){const r=d.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)d.close();}}));
$$('.zoom').forEach(a=>a.addEventListener('click',e=>{e.preventDefault();const img=$('img',a);$('#large-image').src=a.href;$('#large-image').alt=img.alt;$('#image-caption').textContent=img.alt;$('#image-original').href=a.href;$('#image-dialog').showModal();}));
$$('.print-button').forEach(b=>b.addEventListener('click',()=>window.print()));
$$('[data-copy]').forEach(b=>b.addEventListener('click',async()=>{try{if(!navigator.clipboard)throw Error();await navigator.clipboard.writeText(b.dataset.copy);toast('Copied to clipboard.');}catch{const input=document.createElement('textarea');input.value=b.dataset.copy;input.style.position='fixed';input.style.opacity='0';document.body.append(input);input.select();let ok=false;try{ok=document.execCommand('copy');}catch{}input.remove();toast(ok?'Copied to clipboard.':'Copy this text: '+b.dataset.copy);}}));
$$('[data-table-filter]').forEach(input=>{const table=input.closest('label').nextElementSibling;const status=document.createElement('p');status.className='small';status.setAttribute('aria-live','polite');table.after(status);input.addEventListener('input',()=>{const q=input.value.trim().toLowerCase();let count=0;$$('tbody tr',table).forEach(row=>{const match=row.textContent.toLowerCase().includes(q);row.hidden=!match;if(match)count++;});status.textContent=q?(count?count+' matching rows':'No matching rows. Try another term.') : '';});});
document.addEventListener('keydown',e=>{const typing=e.target.matches('input,textarea,[contenteditable=true]');if(e.key==='/'&&!typing&&!$('dialog[open]')){e.preventDefault();showSearch();}if(e.key==='Escape'&&$('#sidebar').classList.contains('open')){setMenu(false);$('#menu-toggle').focus();}});
update();themeLabel();
})();
