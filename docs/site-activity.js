/* Anonymous aggregate counts. No cookies, storage, page text, query values or IDs. */
(()=>{'use strict';
 if(location.origin!=='https://atdnorthlondon.co.uk'||navigator.globalPrivacyControl||navigator.doNotTrack==='1')return;
 const sources=['google','instagram','youtube','facebook','chatgpt','other','direct'];
 const rawSource=(new URLSearchParams(location.search).get('utm_source')||new URLSearchParams(location.search).get('source')||'').trim().toLowerCase();
 const supplied=rawSource==='ig'?'instagram':['chatgpt.com','chat.openai.com'].includes(rawSource)?'chatgpt':rawSource;
 let source=sources.includes(supplied)?supplied:'direct',host='';try{host=new URL(document.referrer).hostname;}catch{}
 if(!sources.includes(supplied)){
  for(const [domain,name]of [['google.com','google'],['google.co.uk','google'],['instagram.com','instagram'],['youtube.com','youtube'],['youtu.be','youtube'],['facebook.com','facebook'],['chatgpt.com','chatgpt'],['chat.openai.com','chatgpt']])if(host===domain||host.endsWith('.'+domain))source=name;
  if(source==='direct'&&host&&host!==location.hostname)source='other';
 }
 fetch('https://ujopvetvzfxgcxrphonx.supabase.co/functions/v1/atd-enquiry-tools',{method:'POST',headers:{'Content-Type':'application/json',apikey:'sb_publishable_bfmHVxxrF4psQVJ-aahaaQ_DsEutly9'},body:JSON.stringify({action:'count',event:'page_view',source}),credentials:'omit',keepalive:true}).catch(()=>{});
 if(source!=='direct')document.addEventListener('click',event=>{const a=event.target.closest('a[href]');if(!a)return;const u=new URL(a.href,location.href);if(u.origin!==location.origin||u.pathname.startsWith('/assets/'))return;u.searchParams.set('source',source);a.href=u.href;});
})();
