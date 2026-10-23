(function(){
const d=document,R=matchMedia('(prefers-reduced-motion: reduce)').matches,touch=matchMedia('(hover: none)').matches;
const h=d.querySelector('header.top'),b=d.querySelector('.burger'),n=d.querySelector('nav.main');
// condensing header
let last=-1;const onS=()=>{const y=scrollY;if((y>40)!==(last>40))h.classList.toggle('sc',y>40);last=y};addEventListener('scroll',onS,{passive:true});onS();
b&&b.addEventListener('click',()=>{const o=n.classList.toggle('open');b.classList.toggle('open',o);b.setAttribute('aria-expanded',o)});
// split headline into words for staggered reveal
d.querySelectorAll('h1.split').forEach(el=>{let i=0;const walk=node=>{[...node.childNodes].forEach(c=>{if(c.nodeType===3){const f=d.createDocumentFragment();c.textContent.split(/(\s+)/).forEach(t=>{if(!t)return;if(/^\s+$/.test(t)){f.append(t);return}const o=d.createElement('span');o.className='wd';const s=d.createElement('span');s.textContent=t;s.style.transitionDelay=(120+i++*55)+'ms';o.append(s);f.append(o)});c.replaceWith(f)}else if(c.nodeType===1)walk(c)})};walk(el);el.setAttribute('aria-label',el.textContent.replace(/\s+/g,' ').trim())});
requestAnimationFrame(()=>requestAnimationFrame(()=>d.documentElement.classList.add('ready')));
// scroll reveals (with failsafe so content can never stay hidden)
const show=el=>el.classList.add('in');
const rv=d.querySelectorAll('.rv');
if(R||!('IntersectionObserver' in window)){rv.forEach(show)}else{
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){show(e.target);io.unobserve(e.target)}}),{threshold:0,rootMargin:'0px 0px -6% 0px'});
rv.forEach(el=>io.observe(el));
// stagger siblings inside grids
d.querySelectorAll('.g3,.g4,.paths,.stats').forEach(g=>[...g.children].forEach((c,i)=>{if(c.classList.contains('rv')&&!c.style.transitionDelay)c.style.transitionDelay=(i%4*80)+'ms'}));
// anything already scrolled past (fast flings, anchor jumps) gets revealed
let t;addEventListener('scroll',()=>{clearTimeout(t);t=setTimeout(()=>rv.forEach(el=>{if(!el.classList.contains('in')&&el.getBoundingClientRect().top<innerHeight)show(el)}),120)},{passive:true});
}
// animated counters
const cs=d.querySelectorAll('[data-count]');
const run=el=>{const to=+el.dataset.count,from=+(el.dataset.from||0),t0=performance.now(),D=1800;const step=now=>{const p=Math.min(1,(now-t0)/D),e=1-Math.pow(1-p,4);el.textContent=Math.round(from+(to-from)*e);if(p<1)requestAnimationFrame(step)};requestAnimationFrame(step)};
if(!R&&'IntersectionObserver' in window){cs.forEach(el=>{el.style.minWidth=el.textContent.length+'ch';el.textContent=el.dataset.from||0});const co=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){run(e.target);co.unobserve(e.target)}}),{threshold:.6});cs.forEach(el=>co.observe(el))}
// hero parallax (transform only, rAF-throttled)
const par=d.querySelectorAll('[data-par]');
if(!R&&par.length){let tk=false;const upd=()=>{tk=false;const y=scrollY;if(y<innerHeight*1.2)par.forEach(p=>p.style.transform='translate3d(0,'+(y*.28).toFixed(1)+'px,0)')};addEventListener('scroll',()=>{if(!tk){tk=true;requestAnimationFrame(upd)}},{passive:true})}
// Lenis smooth scroll: desktop pointer only
addEventListener('load',()=>{if(R||touch||!window.Lenis)return;const l=new Lenis({lerp:.11,anchors:{offset:-90}});const raf=t=>{l.raf(t);requestAnimationFrame(raf)};requestAnimationFrame(raf)});
// demo forms
d.querySelectorAll('form.demo').forEach(f=>f.addEventListener('submit',e=>{e.preventDefault();const ok=f.querySelector('.ok');if(ok){ok.style.display='block'};f.querySelector('button[type=submit],button:not([type])')?.setAttribute('disabled','')}));
const bars=d.querySelectorAll('.bar i[data-w]');const bo=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.style.width=e.target.dataset.w}}));bars.forEach(x=>bo.observe(x));
const sn=d.querySelectorAll('.subnav a');if(sn.length){const so=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting)sn.forEach(a=>{const on=a.hash=='#'+e.target.id;a.classList.toggle('on',on);if(on){const w=a.parentElement;w.scrollTo({left:a.offsetLeft-w.clientWidth/2+a.offsetWidth/2,behavior:'smooth'})}})}),{rootMargin:'-40% 0px -55% 0px'});d.querySelectorAll('.prog').forEach(s=>so.observe(s))}
})();
