(function(){const h=document.querySelector('header.top'),b=document.querySelector('.burger'),n=document.querySelector('nav.main');
addEventListener('scroll',()=>h.classList.toggle('sc',scrollY>10),{passive:true});
b&&b.addEventListener('click',()=>{const o=n.classList.toggle('open');b.classList.toggle('open',o);b.setAttribute('aria-expanded',o)});
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.12});
document.querySelectorAll('.rv').forEach(el=>io.observe(el));
document.querySelectorAll('form.demo').forEach(f=>f.addEventListener('submit',e=>{e.preventDefault();const ok=f.querySelector('.ok');if(ok){ok.style.display='block'};f.querySelector('button[type=submit],button:not([type])')?.setAttribute('disabled','')}));
const bars=document.querySelectorAll('.bar i[data-w]');const bo=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.style.width=e.target.dataset.w}}));bars.forEach(x=>bo.observe(x));
const sn=document.querySelectorAll('.subnav a');if(sn.length){const so=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting)sn.forEach(a=>a.classList.toggle('on',a.hash=='#'+e.target.id))}),{rootMargin:'-40% 0px -55% 0px'});document.querySelectorAll('.prog').forEach(s=>so.observe(s))}
})();
