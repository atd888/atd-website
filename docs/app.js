(() => {
 const mobileButton=document.querySelector('.mobile-toggle'),mobileMenu=document.querySelector('#mobile-menu');
 const serviceButton=document.querySelector('.service-nav>button'),serviceMenu=document.querySelector('#services-menu');
 function closeMenus(){if(mobileButton){mobileButton.setAttribute('aria-expanded','false');mobileButton.setAttribute('aria-label','Open navigation');mobileMenu.hidden=true;}if(serviceButton){serviceButton.setAttribute('aria-expanded','false');serviceMenu.hidden=true;}}
 mobileButton?.addEventListener('click',()=>{const open=mobileButton.getAttribute('aria-expanded')!=='true';mobileButton.setAttribute('aria-expanded',String(open));mobileButton.setAttribute('aria-label',open?'Close navigation':'Open navigation');mobileMenu.hidden=!open;});
 serviceButton?.addEventListener('click',()=>{const open=serviceButton.getAttribute('aria-expanded')!=='true';serviceButton.setAttribute('aria-expanded',String(open));serviceMenu.hidden=!open;});
 document.addEventListener('click',event=>{if(!event.target.closest('.service-nav')&&serviceButton){serviceButton.setAttribute('aria-expanded','false');serviceMenu.hidden=true;}});
 document.addEventListener('keydown',event=>{if(event.key==='Escape'){const mobileOpen=mobileButton?.getAttribute('aria-expanded')==='true',serviceOpen=serviceButton?.getAttribute('aria-expanded')==='true';closeMenus();if(mobileOpen)mobileButton.focus();else if(serviceOpen)serviceButton.focus();}});
 mobileMenu?.addEventListener('click',event=>{if(event.target.closest('a'))closeMenus();});
 const form=document.querySelector('#enquiry-form');
 if(form){const choices={'painting-decorating':'Painting & decorating','wallpapering':'Wallpapering','bathroom-refurbishments':'Bathroom refurbishments','full-refurbishments':'Full refurbishments'};const chosen=choices[new URLSearchParams(location.search).get('service')];if(chosen)form.elements.service.value=chosen;
 form.addEventListener('submit',event=>{event.preventDefault();if(!form.reportValidity())return;const f=new FormData(form);const message=`Hello ATD, I would like to discuss a project.\n\nName: ${f.get('name').trim()}\nPostcode: ${f.get('postcode').trim()}\nService: ${f.get('service')}\n\n${f.get('details').trim()}\n\nPreferred timing: ${f.get('timing').trim()||'To discuss'}${f.get('offer')?'\n\nPlease include the website offer: 10% off labour, materials excluded.':''}\n\nI can attach photographs here.`;document.querySelector('#form-status').textContent='Opening your WhatsApp draft. Review it and tap Send in WhatsApp to contact ATD.';window.location.assign('https://wa.me/447557954457?text='+encodeURIComponent(message));});}
 const dialog=document.querySelector('#photo-dialog'),photoButtons=[...document.querySelectorAll('[data-photo]')];
 const viewerStage=dialog?.querySelector('.photo-stage');
 let lastPhoto,activePhotos=[],photoIndex=0,viewerScrollTimer;
 const galleryServices={interiors:'painting-decorating',exteriors:'exterior-painting',wallpaper:'wallpapering',bathroom:'bathroom-refurbishments'};
 const motionBehavior=()=>window.matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth';
 function enquiryForCategory(category){return galleryServices[category]||'';}
 function updateGalleryLink(link,service){if(!link)return;const destination=new URL(link.getAttribute('href'),location.href);destination.search='';destination.hash='';if(service)destination.searchParams.set('service',service);link.href=destination.href;}
 function syncPhoto(index){
  if(!dialog||index<0||index>=activePhotos.length)return;
  photoIndex=index;lastPhoto=activePhotos[index];
  dialog.querySelector('[data-photo-caption]').textContent=lastPhoto.dataset.caption;
  updateGalleryLink(dialog.querySelector('#photo-enquiry-link'),enquiryForCategory(lastPhoto.dataset.topics)||enquiryForCategory(lastPhoto.dataset.category));
  dialog.querySelector('#photo-position').textContent=(index+1)+' of '+activePhotos.length;
  dialog.querySelector('[data-photo-prev]').disabled=index===0;
  dialog.querySelector('[data-photo-next]').disabled=index===activePhotos.length-1;
  [...viewerStage.children].forEach((slide,i)=>{
   slide.setAttribute('aria-hidden',String(i!==index));
   if(Math.abs(i-index)<=1){const img=slide.querySelector('img');if(!img.getAttribute('src'))img.src=activePhotos[i].dataset.photo;}
  });
 }
 function showPhoto(index,animate=true){
  if(!viewerStage||index<0||index>=activePhotos.length)return;
  clearTimeout(viewerScrollTimer);syncPhoto(index);
  viewerStage.scrollTo({left:viewerStage.clientWidth*index,behavior:animate?motionBehavior():'instant'});
 }
 function syncScrolledPhoto(){
  clearTimeout(viewerScrollTimer);
  if(dialog?.open&&viewerStage.clientWidth)syncPhoto(Math.max(0,Math.min(activePhotos.length-1,Math.round(viewerStage.scrollLeft/viewerStage.clientWidth))));
 }
 viewerStage?.addEventListener('scroll',()=>{clearTimeout(viewerScrollTimer);viewerScrollTimer=setTimeout(syncScrolledPhoto,100);},{passive:true});
 viewerStage?.addEventListener('scrollend',syncScrolledPhoto);
 photoButtons.forEach(button=>button.addEventListener('click',()=>{
  activePhotos=photoButtons.filter(photo=>!photo.hidden);
  viewerStage.replaceChildren(...activePhotos.map(photo=>{
   const slide=document.createElement('div');slide.className='photo-slide';
   const img=document.createElement('img');img.alt=photo.dataset.caption;img.draggable=false;img.decoding='async';slide.append(img);return slide;
  }));
  if(!dialog.open)dialog.showModal();
  showPhoto(activePhotos.indexOf(button),false);
 }));
 dialog?.querySelector('.dialog-close').addEventListener('click',()=>dialog.close());
 dialog?.querySelector('[data-photo-prev]').addEventListener('click',()=>showPhoto(photoIndex-1));
 dialog?.querySelector('[data-photo-next]').addEventListener('click',()=>showPhoto(photoIndex+1));
 dialog?.addEventListener('keydown',event=>{if(event.altKey||event.ctrlKey||event.metaKey)return;if(event.key==='ArrowLeft'){event.preventDefault();showPhoto(photoIndex-1);}if(event.key==='ArrowRight'){event.preventDefault();showPhoto(photoIndex+1);}});
 dialog?.addEventListener('click',event=>{if(event.target===dialog)dialog.close();});
 dialog?.addEventListener('close',()=>{clearTimeout(viewerScrollTimer);lastPhoto?.focus({preventScroll:true});});
 window.addEventListener('resize',()=>{if(dialog?.open)showPhoto(photoIndex,false);});
 const galleryRails=[...document.querySelectorAll('.gallery')].map(rail=>{
  const controls=document.createElement('div');controls.className='gallery-rail-controls';
  const previous=document.createElement('button'),next=document.createElement('button'),count=document.createElement('span');
  previous.type=next.type='button';previous.textContent='← Previous';next.textContent='Next →';
  previous.setAttribute('aria-label','Previous '+rail.getAttribute('aria-label').toLowerCase());next.setAttribute('aria-label','Next '+rail.getAttribute('aria-label').toLowerCase());
  count.setAttribute('role','status');count.setAttribute('aria-live','polite');
  controls.append(previous,count,next);rail.after(controls);
  const visible=()=>[...rail.querySelectorAll('[data-photo]')].filter(card=>!card.hidden);
  function nearest(cards){const left=rail.getBoundingClientRect().left;let index=0,distance=Infinity;cards.forEach((card,i)=>{const d=Math.abs(card.getBoundingClientRect().left-left);if(d<distance){distance=d;index=i;}});return index;}
  function update(){const cards=visible(),index=nearest(cards);controls.hidden=cards.length<2;count.textContent=cards.length?(index+1)+' of '+cards.length:'';previous.disabled=index===0;next.disabled=index>=cards.length-1;}
  function move(direction){const cards=visible(),target=cards[nearest(cards)+direction];if(target)rail.scrollTo({left:rail.scrollLeft+target.getBoundingClientRect().left-rail.getBoundingClientRect().left,behavior:motionBehavior()});}
  previous.addEventListener('click',()=>move(-1));next.addEventListener('click',()=>move(1));
  rail.addEventListener('scroll',update,{passive:true});
  rail.addEventListener('keydown',event=>{if(event.target===rail&&['ArrowLeft','ArrowRight'].includes(event.key)){event.preventDefault();move(event.key==='ArrowLeft'?-1:1);}});
  return {rail,reset(){const cards=visible();rail.hidden=!cards.length;rail.scrollTo({left:0,behavior:'instant'});update();}};
 });
 const filters=document.querySelectorAll('[data-filter]'),cards=document.querySelectorAll('[data-category]');
 function applyGalleryFilter(category,remember=false){
  const filter=[...filters].find(item=>item.dataset.filter===category)||[...filters].find(item=>item.dataset.filter==='all');
  if(!filter)return;
  filters.forEach(item=>item.setAttribute('aria-pressed',String(item===filter)));
  let shown=0;
  cards.forEach(card=>{card.hidden=filter.dataset.filter==='finished'?card.dataset.category==='progress':filter.dataset.filter!=='all'&&card.dataset.category!==filter.dataset.filter&&card.dataset.topics!==filter.dataset.filter;if(!card.hidden)shown++;});
  galleryRails.forEach(item=>item.reset());
  const hint=document.querySelector('.gallery-swipe-hint');if(hint)hint.hidden=shown<2;
  const progressIntro=document.querySelector('[data-progress-intro]');
  if(progressIntro)progressIntro.hidden=![...cards].some(card=>!card.hidden&&card.dataset.category==='progress');
  document.querySelector('#gallery-status').textContent=`${shown} project ${shown===1?'photo':'photos'}`;
  const galleryLink=document.querySelector('#gallery-enquiry-link');
  updateGalleryLink(galleryLink,enquiryForCategory(filter.dataset.filter));
  if(galleryLink)galleryLink.textContent=({interiors:'Discuss interior decorating',exteriors:'Discuss exterior decorating',wallpaper:'Discuss wallpapering',bathroom:'Discuss your bathroom project'}[filter.dataset.filter]||'Discuss your project')+' ↗';
  if(remember){
   const url=new URL(location.href);
   if(filter.dataset.filter==='all')url.searchParams.delete('category');else url.searchParams.set('category',filter.dataset.filter);
   // Some browsers restrict History on file previews; filtering still works there.
   if(url.href!==location.href)try{history.pushState(null,'',url.href);}catch{}
  }
 }
 filters.forEach(filter=>filter.addEventListener('click',()=>applyGalleryFilter(filter.dataset.filter,true)));
 if(filters.length){
  applyGalleryFilter(new URLSearchParams(location.search).get('category')||'all');
  window.addEventListener('popstate',()=>{if(dialog?.open)dialog.close();applyGalleryFilter(new URLSearchParams(location.search).get('category')||'all');});
 }

 // Open the specific project when a service page links to its gallery story.
 function revealProjectStory(){
  let id='';try{id=decodeURIComponent(location.hash.slice(1));}catch{return;}
  const story=id.startsWith('story-')?document.getElementById(id):null;
  if(!story?.matches('details.project-story'))return;
  story.open=true;
  requestAnimationFrame(()=>story.scrollIntoView({block:'start',behavior:'auto'}));
 }
 window.addEventListener('hashchange',revealProjectStory);
 revealProjectStory();

 const enquiryFrame=document.querySelector('#client-enquiry-frame');
 if(enquiryFrame){
  const frameURL=new URL(enquiryFrame.getAttribute('src'),location.href);
  const service=new URLSearchParams(location.search).get('service');
  if(['painting-decorating','exterior-painting','wallpapering','bathroom-refurbishments','full-refurbishments','full-flat-refurbishment'].includes(service)){frameURL.searchParams.set('service',service);enquiryFrame.src=frameURL.href;}
  const startLinks=[...document.querySelectorAll('[data-request-start]')];
  const initialGoal=new URLSearchParams(location.search).get('request_type');
  if(['quote','appointment','both'].includes(initialGoal)){frameURL.searchParams.set('request_type',initialGoal);enquiryFrame.src=frameURL.href;}
  function markGoal(goal){startLinks.forEach(link=>{if(link.dataset.requestStart===goal)link.setAttribute('aria-current','true');else link.removeAttribute('aria-current');link.removeAttribute('aria-pressed');});}
  markGoal(initialGoal||'quote');
  startLinks.forEach(link=>link.addEventListener('click',event=>{event.preventDefault();enquiryFrame.contentWindow.postMessage({type:'ATD_REQUEST_GOAL',requestType:link.dataset.requestStart},location.protocol==='file:'?'*':frameURL.origin);enquiryFrame.scrollIntoView({block:'start',behavior:'auto'});}));
  window.addEventListener('message',event=>{
   if(event.source!==enquiryFrame.contentWindow||(event.origin!==frameURL.origin&&!(location.protocol==='file:'&&['null','file://'].includes(event.origin))))return;
   if(event.data?.type==='ATD_ENQUIRY_GOAL'&&['quote','appointment','both'].includes(event.data.requestType)){markGoal(event.data.requestType);return;}
   if(event.data?.type==='ATD_ENQUIRY_STEP'&&Number.isInteger(event.data.step)&&event.data.step>=0&&event.data.step<=3){enquiryFrame.scrollIntoView({block:'start',behavior:'auto'});return;}
   if(!event.data||event.data.type!=='ATD_ENQUIRY_HEIGHT'||typeof event.data.height!=='number'||!Number.isFinite(event.data.height))return;
   enquiryFrame.style.height=Math.min(16008,Math.max(480,Math.ceil(event.data.height)+8))+'px';
  });
 }

})();

/* Before/after comparison sliders */
document.querySelectorAll('.ba input[type=range]').forEach(input=>{const box=input.closest('.ba');const set=()=>box.style.setProperty('--pos',input.value+'%');input.addEventListener('input',set);set();});
