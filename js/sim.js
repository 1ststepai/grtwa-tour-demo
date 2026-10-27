/* Interactive simulation. Everything runs in this page; nothing is stored or sent. */
(function(){
const $=s=>document.querySelector(s),esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const S={day:null,time:null,parent:'Sample Parent',child:'Sample Child',grade:'Kindergarten',booked:false};
const DOW=['Sun','Mon','Tue','Wed','Thu','Fri','Sat'],MON=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
const fmt=d=>DOW[d.getDay()]+', '+MON[d.getMonth()]+' '+d.getDate();
const TIMES=['9:00 AM','10:30 AM','1:30 PM'];
// ---- booking ----
const days=[];for(let d=new Date(),i=0;days.length<8;i++){d=new Date();d.setDate(d.getDate()+2+i);if(d.getDay()>0&&d.getDay()<6&&d.getDay()!==5)days.push(d)}
function chips(el,items,cur,cb){el.innerHTML='';items.forEach((it,i)=>{const b=document.createElement('button');b.type='button';b.innerHTML=it.h;if(cur===i)b.className='on';b.onclick=()=>cb(i);el.appendChild(b)})}
function drawDays(){chips($('#days'),days.map(d=>({h:DOW[d.getDay()]+'<small>'+MON[d.getMonth()]+' '+d.getDate()+'</small>'})),S.day,i=>{S.day=i;drawDays();chk()})}
function drawTimes(){chips($('#times'),TIMES.map(t=>({h:t})),S.time,i=>{S.time=i;drawTimes();chk()})}
function chk(){$('#to2').disabled=!(S.day!=null&&S.time!=null)}
function step(n){[1,2,3].forEach(i=>{$('#sp'+i).hidden=i!==n;$('#ss'+i).className=i<=n?'on':''})}
const when=()=>fmt(days[S.day])+' at '+TIMES[S.time];
$('#to2').onclick=()=>{$('#ssum').innerHTML='📅 <b>'+when()+'</b> · Campus tour, 146 Dover Chester Road, Randolph';step(2)};
$('#back1').onclick=()=>step(1);
$('#sf').onsubmit=e=>{e.preventDefault();S.parent=$('#pn').value.trim()||'Sample Parent';S.child=$('#cn').value.trim()||'Sample Child';S.grade=$('#gr').value;S.booked=true;$('#swhen').textContent=when()+' · '+S.grade;step(3);reset();you();};
$('#again').onclick=()=>{S.booked=false;S.day=S.time=null;drawDays();drawTimes();chk();step(1);reset();you()};
drawDays();drawTimes();
// ---- playback ----
const first=()=>esc(S.parent.split(' ')[0]),kid=()=>esc(S.child),W=()=>S.day!=null?fmt(days[S.day]):'Tue, Nov 10',T=()=>S.time!=null?TIMES[S.time]:'10:30 AM';
function phone(who,bubs,cap){return '<div><div class="phone"><div class="scr"><div class="ph"><div class="av">'+(who[0])+'</div><b>'+who+'</b>Text message</div><div class="msgs">'+bubs.map((b,i)=>b.ts?'<div class="ts">'+b.ts+'</div>':'<div class="bub'+(b.me?' me':'')+'" style="animation-delay:'+(i*.5)+'s">'+b.t+'</div>').join('')+'</div></div></div><p class="cap">'+cap+'</p></div>'}
function mail(from,to,subj,body,cap){return '<div class="mail"><div class="mh">From <b>'+from+'</b><br>To <b>'+to+'</b><h4>'+subj+'</h4></div><div class="mb">'+body+'</div><p class="cap" style="padding:0 16px 14px">'+cap+'</p></div>'}
const STEPS=[
{t:'Instant text confirmation',w:'Seconds after booking',stage:'tourbooked',r:()=>phone('Gottesman RTW Academy',[{ts:'Today · just now'},{t:'Hi '+first()+'! Your tour of Gottesman RTW Academy is confirmed for '+W()+' at '+T()+'. 146 Dover Chester Rd, Randolph. Reply R to reschedule. We can\'t wait to meet you and '+kid()+'!'}],'Sample text to the parent\'s phone. Not actually sent.')},
{t:'Confirmation email + calendar invite',w:'Seconds after booking',r:()=>mail('Gottesman RTW Academy Admissions',''+esc(S.parent)+' (sample)','Your tour is confirmed: '+W(),'<p>Dear '+first()+',</p><p>Thank you for booking a visit. We\'re looking forward to showing you and '+kid()+' around our '+esc(S.grade||'')+' program.</p><div class="ics"><div class="d"><i>'+(S.day!=null?MON[days[S.day].getMonth()].toUpperCase():'NOV')+'</i><b>'+(S.day!=null?days[S.day].getDate():'10')+'</b></div><div><b>Campus tour</b><br><small>'+W()+' · '+T()+' · about 45 minutes</small><div class="btns"><span class="chip">＋ Google Calendar</span><span class="chip">＋ Apple / Outlook (.ics)</span></div></div></div><p>Parking is in the front lot. Plan to check in at the main office.</p><p>Warmly,<br>The Admissions Team</p>','Sample email with a calendar invite attached. Not actually sent.')},
{t:'Admissions coordinator notified',w:'Seconds after booking',r:()=>'<div class="alert"><div class="noti"><span class="ic">🔔</span><div><b>New tour booked</b><p>'+esc(S.parent)+' · '+kid()+', '+esc(S.grade||'')+' · '+W()+' at '+T()+'</p></div></div><div class="noti" style="border-color:var(--navy)"><span class="ic">📅</span><div><b>Added to the admissions calendar</b><p>Tour slot is now held, so it can\'t be double-booked.</p></div></div><div class="task"><b>Prep checklist (created for you)</b><ul><li>☐ Pull '+esc(S.grade||'grade')+' info packet</li><li>☐ Let the '+esc(S.grade||'')+' teacher know a family is visiting</li><li>☐ Family record created in the pipeline</li></ul></div><p class="cap">Sample staff notification. Not actually sent.</p></div>'},
{t:'Reminder text, 24 hours before',w:'Day before the tour',r:()=>phone('Gottesman RTW Academy',[{ts:'Day before · 10:00 AM'},{t:'Reminder: your tour is tomorrow, '+W()+' at '+T()+'. See you soon! Need a different time? Just reply.'},{t:'Something came up, can we do later in the week?',me:1},{t:'No problem! Reply 1 for Thu at 10:30 AM or 2 for Thu at 1:30 PM.'},{t:'2',me:1},{t:'Done! You\'re rebooked for Thursday at 1:30 PM. A new calendar invite is in your email.'}],'Sample reminder with a reply-to-reschedule example. Not actually sent.')},
{t:'Thank-you after the tour',w:'Evening after the tour',stage:'toured',r:()=>phone('Gottesman RTW Academy',[{ts:'Tour day · 6:00 PM'},{t:'Thank you for visiting today, '+first()+'! It was a pleasure meeting '+kid()+'. When you\'re ready, here\'s the application: <a href="#" onclick="return false">grtwa.org/apply</a>. Questions? Just reply here.'}],'Sample thank-you with an application link. Not actually sent.')},
{t:'Friendly nudge, 3 days later',w:'Only if no application yet',stage:'applied',r:()=>phone('Gottesman RTW Academy',[{ts:'3 days after the tour'},{t:'Hi '+first()+', just checking in. Any questions we can answer about our '+esc(S.grade||'')+' program or tuition assistance? The application takes about 15 minutes: <a href="#" onclick="return false">grtwa.org/apply</a>'},{t:'Thanks! Just submitted it 🙂',me:1},{t:'Wonderful, we received it! The admissions team will be in touch about next steps.'}],'Sample nudge. Stops automatically once the family applies. Not actually sent.')},
{t:'Review request to happy current parents',w:'After a positive moment',r:()=>phone('Gottesman RTW Academy',[{ts:'To a current parent (Sample Family B)'},{t:'Hi! We loved seeing everyone at the Chanukah concert. If GRTWA has been a great fit for your family, would you share a quick review? It helps new families find us: <a href="#" onclick="return false">g.page/review</a>'}],'Sample review request, sent only to families who opt in. Not actually sent.')},
{t:'Re-enrollment reminder',w:'Each winter, to current families',stage:'enrolled',r:()=>mail('Gottesman RTW Academy','Sample Family C (current parent)','Re-enrollment for next school year is open','<p>Dear Sample Family C,</p><p>It\'s time to save your child\'s spot for next school year. Re-enrollment takes a few minutes in FACTS.</p><div class="ics"><div class="d"><i>DUE</i><b>✓</b></div><div><b>Re-enroll for next year</b><br><small>Sample deadline · log in to FACTS to complete</small><div class="btns"><span class="chip">Complete re-enrollment →</span></div></div></div><p>Families who haven\'t finished get a gentle reminder a week before the deadline, and the office sees who is still outstanding.</p>','Sample re-enrollment email. Not actually sent.')}
];
let cur=-1,timer=null,sent=0;
const tl=$('#tl');tl.innerHTML=STEPS.map((s,i)=>'<li data-n="'+(i+1)+'"><b>'+s.t+'</b><small>'+s.w+'</small></li>').join('');
[...tl.children].forEach((li,i)=>li.onclick=()=>{stop();go(i)});
function go(i){cur=Math.max(-1,Math.min(STEPS.length-1,i));[...tl.children].forEach((li,j)=>li.className=j<cur?'done':j===cur?'cur':'');
$('#stage').innerHTML=cur<0?'<div class="idle"><div style="font-size:42px">▶</div><p>'+(S.booked?'Your sample tour is booked. Press <b>Play</b> to watch the follow-up unfold.':'Book a sample tour above, or just press <b>Play</b> to watch with a sample family.')+'</p></div>':STEPS[cur].r();
$('#bar').style.width=((cur+1)/STEPS.length*100)+'%';$('#cnt').textContent=(cur+1)+' / '+STEPS.length;
sent=cur+1;counter();you();}
function stop(){clearInterval(timer);timer=null;$('#play').textContent='▶ Play'}
function play(){if(timer)return stop();if(cur>=STEPS.length-1)go(-1);$('#play').textContent='❚❚ Pause';go(cur+1);timer=setInterval(()=>{if(cur>=STEPS.length-1)return stop();go(cur+1)},4200)}
$('#play').onclick=play;$('#next').onclick=()=>{stop();go(cur+1)};$('#prev').onclick=()=>{stop();go(cur-1)};$('#rst').onclick=()=>{stop();go(-1)};
$('#goplay').onclick=e=>{e.preventDefault();$('#sim-play').scrollIntoView({behavior:'smooth'});setTimeout(()=>{if(!timer)play()},600)};
function reset(){stop();go(-1)}
// ---- dashboard ----
const COLS=['New inquiry','Tour booked','Toured','Applied','Enrolled'];
const fams=[['Sample Family A','Early Childhood',0],['Sample Family D','Grades 1–4',0],['Sample Family E','Kindergarten',1],['Sample Family F','Grades 5–8',1],['Sample Family G','Infant / Toddler',2],['Sample Family H','Grades 1–4',3],['Sample Family J','Kindergarten',4]].map(f=>({n:f[0],g:f[1],c:f[2]}));
let extra=0;
function stageOf(){if(!S.booked&&cur<0)return -1;let c=S.booked?1:0;STEPS.slice(0,cur+1).forEach(s=>{if(s.stage==='tourbooked')c=Math.max(c,1);if(s.stage==='toured')c=2;if(s.stage==='applied')c=3;if(s.stage==='enrolled')c=4});return c}
function you(){const k=$('#kan');if(!k)return;const yc=stageOf();k.innerHTML=COLS.map((c,i)=>{const list=fams.filter(f=>f.c===i);const y=yc===i?'<div class="fam you"><b>'+(S.booked?esc(S.parent):'Sample Parent')+' <span class="chip">you</span></b><small>'+esc(S.grade||'')+(i>=1?' · tour '+W():'')+'</small></div>':'';return '<div class="col"><h4>'+c+'<span>'+(list.length+(y?1:0))+'</span></h4>'+y+list.map(f=>'<div class="fam"><b>'+f.n+'</b><small>'+f.g+'</small></div>').join('')+'</div>'}).join('')}
const L='KLMNPQRSTUVWXYZ';
$('#week').onclick=()=>{fams.forEach(f=>{if(f.c<4&&Math.random()<.5){f.c++;extra+=2}});for(let i=0;i<2;i++){fams.push({n:'Sample Family '+(L[fams.length%L.length])+(fams.length>20?fams.length:''),g:['Kindergarten','Early Childhood','Grades 1–4','Grades 5–8'][Math.floor(Math.random()*4)],c:0});extra+=1}you();counter()};
function counter(){const m=sent+extra;$('#hrs').textContent=(m*10/60).toFixed(1);$('#msgs').textContent=m+' automated message'+(m===1?'':'s')+' so far in this simulation.'}
go(-1);
})();
