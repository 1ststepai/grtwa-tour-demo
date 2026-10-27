/* GRTWA guided simulation. Sample data only; everything runs in this page and nothing is stored or sent. */
(function(){
'use strict';
const $=s=>document.querySelector(s);
const RM=matchMedia('(prefers-reduced-motion: reduce)');
const P='Jordan',PF='Jordan Sample',KID='Ari',GR='Kindergarten',TOUR='Thu, Nov 5',TT='9:30 AM';
let timers=[],cur=0,playing=false,maxSeen=0,autoT=null;
const later=(f,ms)=>{const t=setTimeout(f,ms);timers.push(t);return t};
const clear=()=>{timers.forEach(clearTimeout);timers=[]};
const sb='<div class="sb"><span>9:41</span><i>▮▮▮ ◔ ▬</i></div>';
const th=(n)=>'<div class="th"><div class="av">GR</div><b>'+n+' ›</b></div>';
const phone=(inner,name)=>'<div class="phone q pop" data-t="0"><div class="scr">'+sb+(name?th(name):'')+inner+'</div></div>';
const thread=(items)=>phone('<div class="ms">'+items.join('')+'</div><div class="inp">iMessage</div>','GRTWA Admissions');
const ts=(t,d)=>'<div class="ts q" data-t="'+d+'">'+t+'</div>';
const them=(t,d)=>'<div class="bb q" data-t="'+d+'" data-typ>'+t+'</div>';
const me=(t,d)=>'<div class="bb me q" data-t="'+d+'">'+t+'</div>';
const cal=(m,d)=>'<div class="cal"><small>'+m+'</small><b>'+d+'</b></div>';
const noti=(ap,ti,tx,when,d)=>'<div class="noti q" data-t="'+d+'"><div class="ap">'+ap+'</div><div class="tx"><b>'+ti+'</b><p>'+tx+'</p></div><small>'+when+'</small></div>';
const copy=(s)=>'<div class="copy"><div class="when q" data-t="0"><i></i>'+s.when+'</div><span class="eb q" data-t="80" style="display:block">'+s.eb+'</span><h2 class="q" data-t="160">'+s.title+'</h2><p class="q" data-t="260">'+s.text+'</p></div>';
const mail=(subj,to,body,d)=>'<div class="mail q pop" data-t="'+d+'"><div class="mtb"><i></i><i></i><i></i><span>Mail</span></div><div class="mhd"><div class="av">GR</div><div><b>Gottesman RTW Academy Admissions</b><small>To: '+to+'</small><h4>'+subj+'</h4></div></div><div class="mbd">'+body+'</div></div>';

const S=[
{id:'hero',day:-1,cap:'',dur:0},
{day:0,when:'Day 0 · Tuesday evening',eb:'The booking',title:'A parent books a tour in under a minute.',text:'From the school website, on any phone. A day, a time, a name, and the grade. That is all it takes.',cap:'Day 0. A parent finds the website after dinner and books a tour from their phone.',dur:9000,stage:1,
 hist:[['Day 0 · 8:12 PM','Tour booked on the website for '+TOUR+' at '+TT+'.']],
 devs:()=>phone('<div class="web"><div class="url">grtwacademy.org/visit</div><div class="fm q in" data-t="0" data-add="gone" data-at="6200"><h4>Book a tour</h4><div class="chips"><span>Tue 3</span><span>Wed 4</span><span class="q2" data-add="on" data-at="900">Thu 5</span><span>Mon 9</span></div><div class="chips"><span>9:00</span><span class="q2" data-add="on" data-at="1600">9:30</span><span>1:30</span></div><label>Parent / guardian</label><div class="f" data-type="'+PF+'" data-at="2300"></div><label>Child\'s first name</label><div class="f" data-type="'+KID+'" data-at="3500"></div><label>Grade next year</label><div class="f" data-type="'+GR+'" data-at="4300"></div><div class="go q2" data-add="press" data-at="5500">Confirm my tour</div></div><div class="ok later q" data-t="6300"><b>✓</b><h4>You\'re booked!</h4><p style="font-size:13px;color:#5f6680">'+TOUR+' at '+TT+'<br>Look for a text and an email.</p></div></div>')},
{day:0,when:'Day 0 · seconds later',eb:'Instant confirmation',title:'A personal text arrives before the phone is put down.',text:'The family gets a warm confirmation by text, and the admissions coordinator sees the new tour appear on their desktop, already on the calendar.',cap:'Within seconds: a confirmation text to the parent, and a notification with a calendar card for the coordinator.',dur:10000,
 hist:[['Day 0 · 8:12 PM','Text: "Hi Jordan! Your tour is confirmed for '+TOUR+' at '+TT+'…"'],['Day 0 · 8:13 PM','Parent replied: "Thank you! Can my husband join too?"'],['Day 0 · 8:13 PM','Text: "Of course, the more the merrier…"'],['Day 0 · 8:12 PM','Coordinator notified, tour added to calendar.']],
 devs:()=>thread([ts('Today 8:12 PM',300),them('Hi '+P+'! This is Gottesman RTW Academy. Your tour is confirmed for <b>'+TOUR+' at '+TT+'</b>. We can\'t wait to meet you and '+KID+'.',1500),me('Thank you! Can my husband join too?',3600),them('Of course, the more the merrier. Reply here anytime with questions.',5400),'<div class="dread q" data-t="6000">Delivered</div>'])+'<div class="desk q pop" data-t="2400"><div class="lbl">Coordinator\'s desktop</div>'+noti('GR','New tour booked',PF+' · '+KID+', '+GR,'now',3000)+'<div class="calw q" data-t="3800"><h5>Thursday, November 5</h5><div class="ev"><time>'+TT+'</time><span><b>Family tour</b> · '+PF+' (sample) · '+GR+'</span></div><div class="ev alt2"><time>1:30 PM</time><span>Faculty meeting</span></div></div></div>'},
{day:0,when:'Day 0 · a minute later',eb:'The invite',title:'An email with everything they need, and a calendar invite.',text:'Date, time, address, what to expect, and one tap to add it to their calendar. Nothing for anyone on staff to type.',cap:'The confirmation email lands with the calendar invite attached and the details of the visit.',dur:9000,
 hist:[['Day 0 · 8:13 PM','Email: "Your visit to Gottesman RTW Academy" with calendar invite.']],
 devs:()=>mail('Your visit to Gottesman RTW Academy',PF+' (sample)','<p class="q" data-t="900">Dear '+P+',</p><p class="q" data-t="1300">Thank you for booking a tour. We are so glad you are coming to see our school.</p><div class="ics q" data-t="2000">'+cal('NOV','5')+'<div><strong>Campus tour · '+TT+'</strong><span>146 Dover Chester Road, Randolph, NJ</span><br><span class="pill">Add to calendar</span></div></div><p class="q" data-t="2900"><b>What to expect:</b> about an hour, a walk through classrooms, and time for your questions.</p><p class="q" data-t="3500">Need to change the time? <span class="lk">Reschedule your tour</span></p><p class="q" data-t="4000" style="color:#777">Warmly,<br>The Admissions Team</p>',300)},
{day:1,when:'Day 1 · next morning',eb:'A warm welcome',title:'A short note to say who they will meet.',text:'The next morning, a friendly message introduces the visit and invites questions, so the family feels expected before they arrive.',cap:'Day 1. A welcome message with a preview of the visit, sent on its own.',dur:8000,
 hist:[['Day 1 · 9:00 AM','Text: welcome note with a preview of the visit.']],
 devs:()=>thread([ts('Wed 9:00 AM',300),them('Good morning, '+P+'! A quick hello before your visit. You\'ll see classrooms in action and meet our admissions team.',1500),'<div class="bb card q" data-t="3200"><div style="background-image:url(img/tour.jpg)"></div><p><b>Your visit, next Thursday</b><small>grtwacademy.org · what to expect</small></p></div>',me('Wonderful, '+KID+' is excited!',5000)])},
{day:2,when:'Tour day · 7:30 AM',eb:'Tour day',title:'A morning reminder, and a ready coordinator.',text:'The family gets a reminder with check-in details. The coordinator starts the day with every visit, and each family\'s notes, on one card.',cap:'Tour day. A reminder goes to the family, and the coordinator has the day\'s tours in view.',dur:10000,stage:2,
 hist:[['Tour day · 7:30 AM','Text: reminder with check-in details.'],['Tour day · 9:30 AM','Tour completed.']],
 devs:()=>thread([ts('Thu 7:30 AM',300),them('See you this morning at '+TT+'! Please check in at the front office when you arrive.',1500),me('On our way soon 😊',3600)])+'<div class="desk q pop" data-t="2000"><div class="lbl">Coordinator\'s desktop</div>'+noti('GR','Today: 2 family tours','First visit at '+TT+' with '+PF,'7:00 AM',2600)+'<div class="calw q" data-t="3400"><h5>Today · Thursday, November 5</h5><div class="ev"><time>'+TT+'</time><span><b>'+PF+'</b> · '+KID+', '+GR+' · asked if a parent can join</span></div><div class="ev"><time>1:30 PM</time><span><b>Avery family</b> (sample) · Grades 1–4</span></div></div></div>'},
{day:3,when:'+3 days · Sunday',eb:'The follow-up',title:'A thank-you, and a clear next step.',text:'A few days after the visit, the family hears from the school again with a simple path to apply. When they start, the coordinator knows.',cap:'Three days later. A thank-you with the next step, and a heads-up to the coordinator when the application starts.',dur:10000,stage:3,
 hist:[['+3 days · 10:00 AM','Text: thank-you with the application next step.'],['+3 days · 10:20 AM','Parent replied: "We just started it!"'],['+3 days · 10:21 AM','Coordinator notified: application started.']],
 devs:()=>thread([ts('Sun 10:00 AM',300),them('Thank you for visiting, '+P+'! It was a joy to meet '+KID+'. When you are ready, here is your next step: <span class="lk">Start your application</span>',1500),me('We just started it!',3800),them('Wonderful! Reply here if anything comes up.',5600)])+'<div class="desk q pop" data-t="4400" style="min-height:0"><div class="lbl">Coordinator\'s desktop</div>'+noti('GR','Application started',PF+' · '+KID+', '+GR,'now',4900)+'</div>'},
{day:4,when:'Spring',eb:'The decision',title:'Application accepted, then Enrolled.',text:'Each milestone reaches the family on time, from acceptance to a warm welcome once enrollment is complete. Current families are cared for on the same system.',cap:'Spring. The new family is accepted, then enrolled. Separately, a current family gets their re-enrollment reminder.',dur:11000,stage:5,
 hist:[['Spring · March','Email: application accepted.'],['Spring · April','Enrollment complete. Welcome message sent.']],
 devs:()=>'<div class="status q pop" data-t="200"><span class="eb">New family · '+PF+'</span><h4>'+KID+'\'s journey</h4><div class="st on"><b>✓</b>Tour completed</div><div class="st on"><b>✓</b>Application submitted</div><div class="st" data-add="on" data-at="1400"><b>✓</b>Application accepted</div><div class="st" data-add="on fin" data-at="3200"><b>✓</b>Enrolled</div></div>'+thread([ts('March',600),them('Congratulations, '+P+'! '+KID+'\'s application has been accepted. Your welcome packet is in your email.',1600),ts('April',2800),them('Enrollment is complete. Welcome to the Gottesman RTW Academy family! 🎉',3400)])+'<div class="sep q" data-t="5200">Separate example · a current family</div><div class="sm q" data-t="5600">'+phone('<div class="ms">'+ts('February',5800)+them('Hi Sample Parent B! Re-enrollment for next school year is now open for Sample Child B. <span class="lk">Re-enroll here</span>',6600)+'</div><div class="inp">iMessage</div>','GRTWA Office')+'</div>'},
{id:'dash',day:4,cap:'The staff side. Every family\'s stage and full message history in one place. Tap a family to see everything they received.',dur:12000},
{id:'end',day:5,cap:'What Gottesman RTW Academy gets.',dur:0}
];

/* ---------- pipeline ---------- */
const ST=['Inquiry','Tour booked','Toured','Applied','Accepted','Enrolled'];
const HT=[['Inquiry received','Auto-reply sent with tour times.'],['Tour booked','Confirmation text, email, and calendar invite sent.'],['Tour completed','Reminder sent; thank-you with next step sent.'],['Application started','Coordinator notified.'],['Application accepted','Acceptance email sent.'],['Enrolled','Welcome message sent.']];
const NAMES=['Avery','Brooks','Chen','Diaz','Ellis','Foster','Gray','Hale','Ibarra','Jensen','Kim','Lowe','Moss','Nash','Ortiz','Park','Quinn','Reyes','Shah','Tate'];
const GRS=['Infant / Toddler','Early Childhood','Kindergarten','Grades 1–4','Grades 5–8'];
let fam=[],ni=0,week=0,prevFeat=null;
function mk(s){const n=NAMES[ni++%NAMES.length]+' family'+(ni>NAMES.length?' '+Math.ceil(ni/NAMES.length):'');const f={id:'f'+ni,n:n,g:GRS[ni%GRS.length],s:0,h:[]};for(let i=0;i<=s;i++)step(f,i,'Earlier');return f}
function step(f,i,when){f.s=i;f.h.push([when+' · '+HT[i][0],HT[i][1]])}
function seed(){fam=[];ni=0;[0,0,1,1,1,2,2,3,4].forEach(s=>fam.push(mk(s)))}
seed();
function featStage(){let s=0;for(let i=1;i<=maxSeen&&i<S.length;i++)if(S[i].stage!=null)s=S[i].stage;return s}
function featHist(){let h=[];for(let i=1;i<=Math.min(maxSeen,7);i++)if(S[i].hist)h=h.concat(S[i].hist);return h}
function feat(){return{id:'you',n:PF+' family',g:KID+' · '+GR,s:featStage(),h:featHist(),you:1}}
function all(fs){return [fs].concat(fam)}
function msgCount(){return all(feat()).reduce((a,f)=>a+f.h.length,0)}
function drawKan(fs){const k=$('#kan');if(!k)return;const list=all(fs);
 const first={};k.querySelectorAll('.fc').forEach(e=>first[e.dataset.id]=e.getBoundingClientRect());
 k.innerHTML=ST.map((t,i)=>{const c=list.filter(f=>f.s===i);return '<div class="col"><h4>'+t+'<span>'+c.length+'</span></h4>'+c.map(f=>'<button type="button" class="fc'+(f.you?' you':'')+(first[f.id]||!Object.keys(first).length?'':' new')+'" data-id="'+f.id+'"><b>'+f.n+'</b><small>'+f.g+'</small></button>').join('')+'</div>'}).join('');
 if(!RM.matches)k.querySelectorAll('.fc').forEach(e=>{const a=first[e.dataset.id];if(!a)return;const b=e.getBoundingClientRect();const dx=a.left-b.left,dy=a.top-b.top;if(!dx&&!dy)return;
  e.animate([{transform:'translate('+dx+'px,'+dy+'px)',boxShadow:'0 20px 40px rgba(17,26,61,.25)'},{transform:'none'}],{duration:900,easing:'cubic-bezier(.22,1,.36,1)'})});
 k.querySelectorAll('.fc').forEach(e=>e.onclick=()=>openD(e.dataset.id));
 const m=msgCount();$('#msgs').textContent=m+' messages and updates in this simulation';$('#hrs').textContent=(m*10/60).toFixed(1)}
function openD(id){const f=id==='you'?feat():fam.find(x=>x.id===id);if(!f)return;$('#dname').textContent=f.n;$('#dmeta').textContent=f.g+' · Stage: '+ST[f.s];
 $('#dhist').innerHTML=f.h.map(x=>'<li><small>'+x[0]+'</small><p>'+x[1].replace(/</g,'&lt;')+'</p></li>').join('');
 $('#drawer').classList.add('open');$('#drawer').setAttribute('aria-hidden','false');$('#scrim').classList.add('on');pause();$('#dclose').focus()}
function closeD(){$('#drawer').classList.remove('open');$('#drawer').setAttribute('aria-hidden','true');$('#scrim').classList.remove('on')}
$('#dclose').onclick=closeD;$('#scrim').onclick=closeD;addEventListener('keydown',e=>{if(e.key==='Escape')closeD()});
function simWeek(){week++;const open=fam.filter(f=>f.s<5);for(let i=0;i<4&&open.length;i++){const f=open.splice(Math.floor(Math.random()*open.length),1)[0];step(f,f.s+1,'Week '+week)}
 for(let i=0;i<3;i++){const f=mk(0);f.h=[['Week '+week+' · '+HT[0][0],HT[0][1]]];fam.push(f)}drawKan(feat())}

/* ---------- scenes ---------- */
function heroHTML(){return '<section class="hero"><img src="img/tour.jpg" alt="" fetchpriority="high"><div><span class="eb q" data-t="100">Gottesman RTW Academy · a guided demo</span><h1 class="q" data-t="300">How a family\'s first visit becomes an <em>enrollment</em>.</h1><p class="q" data-t="600">Follow one sample family from the moment they book a tour to their first day, and see what the admissions office sees along the way.</p><div class="q" data-t="900"><button class="start" id="go" type="button"><span></span>Start the guided tour</button><button class="alt" id="self" type="button">Explore at my own pace</button></div><p class="gift q" data-t="1200">Designed and gifted by 1stStep.ai</p></div></section>'}
function dashHTML(){return '<div class="dash"><div class="dtop"><div><span class="eb q" data-t="0">The staff side · sample data</span><h2 class="q" data-t="100">What the admissions office sees</h2><p class="q" data-t="200">A pipeline that keeps itself up to date. Tap any family for their full message history.</p></div><button class="btn q" data-t="300" id="week" type="button">Simulate a week</button></div><div class="kan q" data-t="400" id="kan"></div><div class="saved q" data-t="600"><div><span class="eb">Illustrative example</span><div class="big"><span id="hrs">0.0</span> staff hours saved</div><p class="asm" id="msgs"></p></div><p class="asm"><b>Assumption:</b> about 10 minutes of staff time for each message or update that would otherwise be written, sent, or tracked by hand, multiplied by the messages in this simulation. It is an illustration, not a measured result.</p></div></div>'}
function endHTML(){const c=[['✓','Instant confirmations','Text and email the moment a family books, with a calendar invite attached.'],['◷','Timely reminders','Before every tour, so families arrive knowing where to go.'],['!','Coordinator alerts','A notification and calendar card for every booking, and a clear view of each day\'s tours.'],['→','Thoughtful follow-up','A thank-you and a clear next step after every visit, sent on time.'],['▦','One clear pipeline','Every family\'s stage and full message history in one place.'],['♥','Care for current families','Re-enrollment reminders and updates on the same system.']];
 return '<div class="close"><span class="eb q" data-t="0">The summary</span><h2 class="q" data-t="100">What GRTWA gets</h2><p class="q" data-t="200">Every family receives a warm, timely experience from first click to first day, and the admissions team spends its time with people, not paperwork.</p><div class="caps">'+c.map((x,i)=>'<div class="q" data-t="'+(350+i*120)+'"><i>'+x[0]+'</i><b>'+x[1]+'</b><span>'+x[2]+'</span></div>').join('')+'</div><div class="gifted q" data-t="1200"><strong>Designed and gifted by 1stStep.ai</strong><p>Happy to walk through how this could fit Gottesman RTW Academy.</p><div class="row"><button class="btn" id="replay" type="button">Watch again</button><a class="btn g" href="index.html" style="text-decoration:none">See the website concept</a></div></div></div>'}

function choreo(root){const rm=RM.matches;
 root.querySelectorAll('[data-t]').forEach(e=>{const t=+e.dataset.t;
  if(rm){e.classList.add('in');return}
  if(e.hasAttribute('data-typ')&&t>800){later(()=>{const ty=document.createElement('div');ty.className='typ';ty.innerHTML='<i></i><i></i><i></i>';ty.setAttribute('aria-hidden','true');e.before(ty);later(()=>ty.remove(),1000)},t-1000)}
  later(()=>e.classList.add('in'),t)});
 root.querySelectorAll('[data-at]').forEach(e=>{const t=rm?0:+e.dataset.at;
  if(e.dataset.type!=null){const s=e.dataset.type;if(rm){e.textContent=s;return}later(()=>{e.classList.add('on');let i=0;const tick=()=>{e.textContent=s.slice(0,++i);if(i<s.length)later(tick,55);else later(()=>e.classList.remove('on'),300)};tick()},t)}
  else later(()=>e.dataset.add.split(' ').forEach(c=>e.classList.add(c)),t)})}

function render(i,dir){clear();cur=i;maxSeen=Math.max(maxSeen,i);const s=S[i],st=$('#stage');closeD();
 let h;if(s.id==='hero')h=heroHTML();else if(s.id==='dash')h=dashHTML();else if(s.id==='end')h=endHTML();else h='<div class="scene">'+copy(s)+'<div class="devs">'+s.devs()+'</div></div>';
 st.innerHTML=h;window.scrollTo({top:0,behavior:'instant'});
 choreo(st);
 // timeline
 const d=s.day;document.querySelectorAll('#days li').forEach((li,j)=>{li.className=d>4?'done':j<d?'done':j===d?'on':''});$('#days').style.setProperty('--p',d<0?0:Math.min(d,4)/4);
 $('#days').style.visibility=d<0?'hidden':'visible';
 $('#dock').hidden=s.id==='hero';$('#cap').textContent=s.cap;
 $('#pips').innerHTML=S.slice(1).map((_,j)=>'<i class="'+(j+1===i?'on':'')+'"></i>').join('');
 $('#staffBtn').classList.toggle('on',s.id==='dash');
 $('#prev').disabled=i<=1;$('#next').disabled=i>=S.length-1;
 if(s.id==='hero'){$('#go').onclick=()=>{playing=true;render(1)};$('#self').onclick=()=>{playing=false;render(1)}}
 if(s.id==='dash'){const f=feat();const startS=(prevFeat!=null&&prevFeat<f.s)?prevFeat:(f.s===5&&prevFeat==null?4:f.s);
  drawKan(Object.assign({},f,{s:startS}));if(startS!==f.s)later(()=>drawKan(f),RM.matches?0:1300);$('#week').onclick=()=>{pause();simWeek()}}
 if(s.id==='dash')prevFeat=featStage();
 if(s.id==='end')$('#replay').onclick=()=>{maxSeen=0;prevFeat=null;seed();playing=true;render(1)};
 syncPlay();schedule()}
function schedule(){clearTimeout(autoT);const s=S[cur];if(playing&&s.dur&&cur<S.length-1)autoT=setTimeout(()=>render(cur+1),s.dur+(RM.matches?2000:0));if(cur>=S.length-1){playing=false;syncPlay()}}
function syncPlay(){const b=$('#play');b.classList.toggle('paused',!playing);b.querySelector('.pl').textContent=playing?'Pause':'Play';b.setAttribute('aria-label',playing?'Pause guided tour':'Play guided tour')}
function pause(){playing=false;clearTimeout(autoT);syncPlay()}
$('#play').onclick=()=>{if(playing)pause();else{playing=true;if(cur>=S.length-1)render(1);else{syncPlay();render(cur)}}};
$('#prev').onclick=()=>{pause();if(cur>1)render(cur-1)};
$('#next').onclick=()=>{pause();if(cur<S.length-1)render(cur+1)};
$('#staffBtn').onclick=()=>{pause();render(S.findIndex(s=>s.id==='dash'))};
addEventListener('keydown',e=>{if(e.target.closest&&e.target.closest('input,textarea'))return;if(e.key==='ArrowRight'&&cur>0&&cur<S.length-1){pause();render(cur+1)}if(e.key==='ArrowLeft'&&cur>1){pause();render(cur-1)}});
const q=new URLSearchParams(location.search).get('step');if(q!=null)maxSeen=S.length-1;render(q!=null?Math.max(0,Math.min(S.length-1,+q||0)):0);
})();
