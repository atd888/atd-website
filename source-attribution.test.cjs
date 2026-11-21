const {test}=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const vm=require('node:vm');
const site=fs.readFileSync('dist/site-activity.js','utf8');
const extras=fs.readFileSync('dist/enquiry/client-extras.js','utf8');
function run(code,{query='',referrer='',origin='https://atdnorthlondon.co.uk',dnt=false,gpc=false}={}){
 const calls=[],events={};
 const document={referrer,addEventListener:(name,fn)=>events[name]=fn,getElementById:()=>({addEventListener:(name,fn)=>events[name]=fn})};
 const window={ATD_CLIENT_CONFIG:{submissionEnabled:true,allowedOrigins:['https://atdnorthlondon.co.uk']},addEventListener:()=>{}};
 const context={URL,URLSearchParams,AbortSignal,window,document,location:{origin,hostname:new URL(origin).hostname,search:query,href:origin+'/'+query},navigator:{doNotTrack:dnt?'1':'0',globalPrivacyControl:gpc},fetch:(url,options)=>{calls.push({url,payload:JSON.parse(options.body)});return Promise.resolve({ok:true,json:async()=>({ok:true})});}};
 vm.runInNewContext(code,context);
 return {calls,events,window};
}
for(const [label,query,referrer,expected] of [
 ['Instagram short label without referrer','?utm_source=ig','','instagram'],
 ['Instagram canonical label','?utm_source=instagram','','instagram'],
 ['Normalise casing and spaces','?utm_source=%20IG%20','','instagram'],
 ['Internal source alias','?source=ig','','instagram'],
 ['ChatGPT search UTM','?utm_source=chatgpt.com','','chatgpt'],
 ['ChatGPT canonical source','?source=chatgpt','','chatgpt'],
 ['ChatGPT referrer','','https://chatgpt.com/c/test','chatgpt'],
 ['Legacy ChatGPT referrer','','https://chat.openai.com/','chatgpt'],
 ['Spoofed ChatGPT domain','','https://chatgpt.com.example.org/','other'],
 ['Unrelated similar name','','https://notchatgpt.com/','other'],
 ['Google kept','?utm_source=google','','google'],
 ['YouTube kept','?source=youtube','','youtube'],
 ['Instagram referrer fallback','','https://l.instagram.com/','instagram'],
 ['Unknown external source','','https://example.org/','other'],
 ['Direct visitor','','','direct'],
 ['No arbitrary source values','?utm_source=some-private-value','','direct'],
 ]){
 test(label,()=>{
  const a=run(site,{query,referrer});const b=run(extras,{query,referrer});
  assert.equal(a.calls[0].payload.source,expected);assert.equal(b.window.ATDAttribution.source,expected);
  assert.deepEqual(Object.keys(a.calls[0].payload).sort(),['action','event','source']);
  b.events.change();assert.equal(b.calls[0].payload.source,expected);
 });
}
test('Preserve privacy opt-outs',()=>{
 for(const prefs of [{dnt:true},{gpc:true}]){
  assert.equal(run(site,prefs).calls.length,0);
  const a=run(extras,prefs);a.events.change();assert.equal(a.calls.length,0);
 }
});
test('Keep page measurement restricted to ATD production',()=>assert.equal(run(site,{origin:'https://hello-honey.co.uk'}).calls.length,0));
test('Preserve canonical attribution across internal service links',()=>{
 const a=run(site,{query:'?utm_source=ig'});const link={href:'https://atdnorthlondon.co.uk/enquiry/booking.html?service=exterior-painting'};
 a.events.click({target:{closest:()=>link}});const u=new URL(link.href);assert.equal(u.searchParams.get('source'),'instagram');assert.equal(u.searchParams.get('service'),'exterior-painting');
});
test('Do not rewrite external links',()=>{
 const a=run(site,{query:'?utm_source=ig'});const link={href:'https://wa.me/447557954457'};a.events.click({target:{closest:()=>link}});assert.equal(link.href,'https://wa.me/447557954457');
});

test('ChatGPT survives the page-to-quote handoff without carrying arbitrary query values',()=>{const a=run(site,{query:'?utm_source=chatgpt.com&private_note=not-sent'});const link={href:'https://atdnorthlondon.co.uk/enquiry/booking.html?service=wallpapering'};a.events.click({target:{closest:()=>link}});const u=new URL(link.href);assert.equal(u.searchParams.get('source'),'chatgpt');assert.equal(u.searchParams.get('service'),'wallpapering');assert.equal(u.searchParams.has('private_note'),false);const b=run(extras,{query:u.search});assert.equal(b.window.ATDAttribution.source,'chatgpt');b.events.change();assert.equal(b.calls[0].payload.source,'chatgpt');});
