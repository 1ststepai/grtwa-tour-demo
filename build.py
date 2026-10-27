# Builds the static concept site. Run: python3 build.py
import html
PHONE='973.584.5530';TEL='tel:+19735845530';ADDR='146 Dover Chester Road, Randolph, NJ 07869'
INQ='https://ga-nj.client.renweb.com/oa/inquiry.cfm?memberid=15873'
APPLY='https://ga-nj.client.renweb.com/oa/?memberid=15873'
FACTS='https://logins2.renweb.com/logins/ParentsWeb-Login.aspx'
GCAL='https://calendar.google.com/calendar/embed?height=600&wkst=1&ctz=America%2FNew_York&showPrint=0&src=Y182ZDFmNTZhZmRkYTE2ZjQwMDBjMGE2MWVjNTY4NWY1MWM4ZGM1NTVlNzI1OTNlMDM5YmE5OGJhODk4ZDhkMThhQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&color=%23d50000'
VOL='https://forms.gle/ZPc91avRwaEoHKKm8'
S_DONATE='https://buy.stripe.com/6oUdR1eH08W4ehh03u2wU05'
S_ENR='https://buy.stripe.com/3cIbIT0Qadck2yz9E42wU04'
S_8TH='https://buy.stripe.com/cNicMXcySgow8WX4jK2wU03'
S_DIN='https://buy.stripe.com/cNibIT1UegowdddcQg2wU02'
O='https://www.grtwacademy.org'
NAV=[('index.html','Home'),('programs.html','Programs'),('tuition.html','Tuition'),('give.html','Give & Pay'),('parents.html','Parents'),('about.html','About'),('contact.html','Contact')]
def ext(u,t,cls=''):return f'<a class="{cls}" href="{u}" target="_blank" rel="noopener">{t}</a>'
def page(fn,title,desc,body,extra_css='',extra_js=''):
    nav=''.join(f'<a href="{u}"{" aria-current=page" if u==fn else ""}>{t}</a>' for u,t in NAV)
    return f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow"><title>{title} · Gottesman RTW Academy (Website concept)</title><meta name="description" content="{desc}">
<meta name="theme-color" content="#1d2b5c"><link rel="icon" href="img/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400..700;1,9..144,400..600&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/site.css">{extra_css}</head><body>
<a class="skip" href="#main">Skip to content</a>
<div class="banner"><span>A website concept designed and gifted to Gottesman RTW Academy by <a href="https://www.1ststep.ai/" target="_blank" rel="noopener">1stStep.ai</a></span><span class="bsep"> · </span><span class="bmore">Not yet the official site · sample figures are labeled · forms send nothing</span></div>
<header class="top"><div class="w"><a class="logo" href="index.html" aria-label="Gottesman RTW Academy home"><img src="img/logo.png" alt="Gottesman RTW Academy" width="161" height="50"></a>
<button class="burger" aria-label="Menu" aria-expanded="false" aria-controls="nav"><span></span><span></span><span></span></button>
<nav class="main" id="nav" aria-label="Main">{nav}<a class="cta" href="visit.html">Book a Tour</a></nav></div></header>
<main id="main">{body}</main>
<footer class="ft"><div class="w"><div class="ft-hero rv"><p class="ft-big">Known, valued, and <em>celebrated</em>.</p><div class="btns"><a class="btn p" href="visit.html">Book a tour</a>{ext(APPLY,"Apply now","btn o")}</div></div><div class="cols">
<div><img src="img/logo.png" alt="Gottesman RTW Academy" style="height:52px;width:auto;margin-bottom:14px"><p>An independent Jewish community day school, nurturing lifelong learners since 1967. Infants through 8th grade.</p><p>{ADDR}<br><a href="{TEL}">{PHONE}</a> · Fax 973.584.0602</p></div>
<div><h4>Explore</h4><ul><li><a href="programs.html">Programs</a></li><li><a href="about.html">Our Story</a></li><li><a href="about.html#staff">Faculty &amp; Staff</a></li><li><a href="contact.html">Contact</a></li></ul></div>
<div><h4>Admissions</h4><ul><li><a href="visit.html">Book a Tour</a></li><li>{ext(APPLY,"Apply Now")}</li><li><a href="tuition.html">Tuition &amp; Affordability</a></li><li>{ext(INQ,"Request Information")}</li></ul></div>
<div><h4>Community</h4><ul><li><a href="parents.html">Parents Hub</a></li><li><a href="give.html">Give &amp; Pay</a></li><li>{ext("https://facebook.com/GRTWANJ","Facebook")}</li><li>{ext("https://www.instagram.com/gottesmanacademy/","Instagram")}</li></ul></div>
</div><div class="cr"><span>Website concept designed and gifted by <a href="https://www.1ststep.ai/" target="_blank" rel="noopener">1stStep.ai</a></span><span>Content and photography from <a href="{O}/" target="_blank" rel="noopener">grtwacademy.org</a> · sample figures are labeled</span></div></div></footer>
<script src="https://cdn.jsdelivr.net/npm/lenis@1.1.20/dist/lenis.min.js" defer></script><script src="js/site.js" defer></script>{extra_js}</body></html>'''
def phero(eb,h,p,img):return f'<div class="phero"><img src="img/{img}" alt="" fetchpriority="high" data-par><div class="w"><span class="eb hr">{eb}</span><h1 class="split">{h}</h1><p class="hr">{p}</p></div></div>'
pages={}

# ---------- HOME ----------
paths=[('visit.html','📅','Visit','Book a personal tour in under a minute.','Book a tour'),
 (APPLY,'✏️','Apply','Rolling admissions. Start your application online.','Start application'),
 ('tuition.html','🧮','Tuition','Families on assistance never pay more than 14% of AGI.','Estimate my cost'),
 ('give.html','🧡','Give','Donate, pay for a program, or support a fund.','Give &amp; pay'),
 ('parents.html','👪','Parents','Events, calendar, FACTS, and volunteering.','Parents hub')]
pc=''.join(f'<a class="path rv" style="transition-delay:{i*70}ms" href="{u}"{" target=_blank rel=noopener" if u.startswith("http") else ""}><span class="ic" aria-hidden="true">{ic}</span><b>{t}</b><small>{d}</small><span class="ar">{a} →</span></a>' for i,(u,ic,t,d,a) in enumerate(paths))
progs=[('ecc','ecc.jpg','Lillie Brandt Early Childhood Center','Infants through Junior Kindergarten'),('lower','lower.jpg','Lower School','Kindergarten through 5th grade'),('middle','middle.jpg','Middle School','6th through 8th grade'),('stem','services.jpg','STEM','From age three through 8th grade'),('arts','why.jpg','The Arts','Visual arts, music, and drama'),('athletics','athletics.jpg','Athletics','GRTWA Lions, 5th–8th grade'),('judaic','chai.jpg','Judaic Studies','Hebrew, Torah, and Israel'),('camp','program.jpg','Camp Neshama','Summer camp for ages 2–5')]
pcards=''.join(f'<a class="card img rv" href="programs.html#{k}" style="text-decoration:none;color:inherit"><span class="cimg"><img src="img/{im}" alt="" width="900" height="563" loading="lazy" decoding="async"></span><div class="b"><h3>{t}</h3><span class="src" style="font-size:14px">{d}</span><span class="more" aria-hidden="true">Explore →</span></div></a>' for k,im,t,d in progs)
MIMG=[('ecc','Early childhood classroom'),('chai','Students with an Israeli flag'),('lower','Lower School students'),('athletics','Students in the gym'),('why','A student presenting'),('pa','Parent Association event'),('middle','Middle School students'),('program','Young children in the gym'),('neshama','Neshama Project enrichment'),('services','Students collaborating')]
_m=''.join(f'<figure><img src="img/{k}.jpg" alt="" width="420" height="300" loading="lazy" decoding="async"></figure>' for k,a in MIMG)
MARQ=f'<section class="mq-wrap" aria-hidden="true"><div class="mq"><div class="mq-track">{_m}{_m}</div></div></section>'
pages['index.html']=page('index.html','Home','A concept redesign of the Gottesman RTW Academy website.',f'''
<div class="hero"><div class="hbg" data-par><img src="img/afford.jpg" alt="Gottesman RTW Academy students celebrating together in a classroom" fetchpriority="high"></div><div class="w">
<span class="eb hr">Jewish community day school · Randolph, NJ · Since 1967</span>
<h1 class="split">Where every child is known, valued, and <em>celebrated.</em></h1>
<p class="hr">Gottesman RTW Academy educates children from infants through 8th grade with a challenging dual curriculum and the richness of Jewish values.</p>
<div class="btns hr"><a class="btn p" href="visit.html">Book a tour</a><a class="btn o" href="programs.html">Explore programs</a></div></div></div>
<div class="w"><div class="paths">{pc}</div></div>
<section><div class="w"><div class="stats rv">
<div class="stat"><b><span data-count="1967" data-from="1900">1967</span></b><span>Founded as Hebrew Academy of Morris County</span></div>
<div class="stat"><b>~<span data-count="200">200</span></b><span>Students, infants through 8th grade</span></div>
<div class="stat"><b><span data-count="22">22</span></b><span>Acre green campus in Randolph</span></div>
<div class="stat"><b><span data-count="900">900</span>+</b><span>Graduates in an active alumni community</span></div></div>
<p class="src" style="text-align:center;margin-top:12px">Figures as published on grtwacademy.org.</p></div></section>
{MARQ}
<section class="alt"><div class="w g2"><div class="ph rv"><img src="img/front.jpg" alt="The Gottesman RTW Academy building at dusk" loading="lazy"></div>
<div class="rv"><span class="eb">Why families choose GRTWA</span><h2>Joyful, challenging learning rooted in Jewish life.</h2>
<p class="lead">A co-educational, pluralistic Jewish community day school, and the only one in Northwestern New Jersey, welcoming families from every branch of Judaism, unaffiliated families, and families with one Jewish parent.</p>
<ul class="ck"><li>Dual curriculum: about 60% General Studies, 40% Judaic Studies</li><li>Blue Ribbon from the U.S. Department of Education</li><li>Accredited by NJAIS; member of NAIS and Prizmah</li><li>Full-time licensed social workers for social and emotional support</li><li>After-care for all ages until 6:00 p.m.</li></ul>
<a class="btn g" href="about.html">Our story →</a></div></div></section>
<section><div class="w"><div class="hd rv"><span class="eb">Programs</span><h2>A path from first steps to high school.</h2><p>From the infant room to the 8th grade capstone trip to Israel.</p></div>
<div class="g4">{pcards}</div></div></section>
<section style="padding-top:0"><div class="w"><div class="band rv"><div><span class="eb" style="color:var(--or2)">Affordability · TuitionMAX</span><h2>A premier Jewish education, within reach.</h2><p>Through GRTWA's Tuition Assistance Program, eligible families will never pay more than 14% of their adjusted gross income toward tuition, no matter how many children are enrolled.</p><div class="btns"><a class="btn p" href="tuition.html">Estimate my cost</a><a class="btn o" href="visit.html">Book a tour</a></div></div><div class="big">14%<small>of AGI, maximum toward tuition</small></div></div></div></section>
<section class="alt"><div class="w g2"><div class="rv"><span class="eb">A message from the Head of School</span><h2>“From the moment you walk through our doors, we hope you feel what makes GRTWA so special: a true sense of belonging.”</h2><p class="lead">Rav Will Keller, Head of School</p><a class="btn g" href="about.html#head">Read the full welcome →</a></div><div class="ph rv" style="max-width:380px;justify-self:center"><img src="img/rav.jpg" alt="Rabbi Will Keller, Head of School" style="aspect-ratio:3/4" loading="lazy"></div></div></section>
<section><div class="w"><div class="hd rv"><span class="eb">Coming up at GRTWA</span><h2>What's happening</h2></div><div id="evlist" style="max-width:820px;margin:0 auto" data-limit="3"></div><p style="text-align:center;margin-top:18px"><a class="btn g" href="parents.html">All events &amp; parent resources →</a></p></div></section>
''',extra_js='<script src="js/events.js" defer></script>')

# ---------- VISIT (existing flow) ----------
tour=open('parts/tour_book.html').read()
flow=open('parts/tour_flow.html').read()
pages['visit.html']=page('visit.html','Book a Tour','Book a personal tour of Gottesman RTW Academy.',phero('Admissions · Visit','See Gottesman RTW Academy for yourself.','Pick a time that works for your family and book a personal tour in under a minute. No phone tag, no waiting for an email back.','tour.jpg')+tour+f'''
<section><div class="w"><div class="hd"><span class="eb">After your visit</span><h2>The admissions path</h2><p>GRTWA works on a rolling admissions basis. You are welcome to apply at any time for the current or following school year.</p></div>
<div class="g4">
<div class="card rv"><span class="eb">1 · Inquiry</span><h3>Request information</h3><p class="src">The admissions team will call to talk about your family's needs and schedule a visit.</p></div>
<div class="card rv"><span class="eb">2 · Apply</span><h3>Online application</h3><p class="src">$75 non-refundable fee per child, plus records, health forms, and birth certificate.</p></div>
<div class="card rv"><span class="eb">3 · Child visit</span><h3>Meet the team</h3><p class="src">For children entering three-year-olds through 8th grade.</p></div>
<div class="card rv"><span class="eb">4 · Decision</span><h3>Offer &amp; registration</h3><p class="src">Notification by phone and email; 3 weeks to accept the position and any assistance offer.</p></div></div>
<p class="src" style="text-align:center;margin-top:18px">Kindergarten eligibility: a child must turn 5 by October 31 of the entry year. At least one parent must be Jewish.</p>
<div class="btns" style="justify-content:center;margin-top:16px">{ext(APPLY,"Start your application","btn p")}{ext(INQ,"Request information","btn g")}<a class="btn g" href="admissions-workflow.html">How follow-up works →</a><a class="btn g" href="simulation.html">▶ See it in action</a></div></div></section>''',
 extra_css='<link rel="stylesheet" href="css/tour.css">',extra_js='<script src="js/tour.js"></script>')

pages['admissions-workflow.html']=page('admissions-workflow.html','How Follow-up Works','An illustration of how tour confirmations and follow-up could reach families.',phero('Admissions · Follow-up','How follow-up works after a tour is booked.','A look at the confirmations, reminders, and thank-you notes families could receive. Everything on this page is an illustration with fictional sample families.','tour.jpg')+flow+'<section><div class="w" style="text-align:center"><a class="btn p" href="visit.html">← Back to booking a tour</a></div></section>',extra_css='<link rel="stylesheet" href="css/tour.css">',extra_js='<script src="js/tour.js"></script>')
# ---------- PROGRAMS ----------
def prog(id,eb,h,img,alt,inner,rev=False,alt_bg=False):
    return f'<section class="prog{" alt" if alt_bg else ""}" id="{id}"><div class="w g2{" rev" if rev else ""}"><div class="ph rv"><img src="img/{img}" alt="{alt}" loading="lazy"></div><div class="rv"><span class="eb">{eb}</span><h2>{h}</h2>{inner}</div></div></section>'
def acc(t,b):return f'<details class="acc"><summary>{t}</summary><div>{b}</div></details>'
sub=''.join(f'<a href="#{k}">{t}</a>' for k,t in [('ecc','Early Childhood'),('lower','Lower School'),('middle','Middle School'),('stem','STEM'),('arts','Arts'),('athletics','Athletics'),('judaic','Judaic Studies'),('camp','Camp Neshama')])
P=phero('Programs','Infants through 8th grade, one connected journey.','A challenging, integrated dual curriculum in General Studies and Judaic Studies, with technology, the arts, and environmentalism woven throughout.','academics.jpg')+f'<nav class="subnav" aria-label="Programs"><div class="w">{sub}</div></nav>'
P+=prog('ecc','Lillie Brandt Early Childhood Center','Nurturing the whole child, from infancy to Junior Kindergarten.','ecc.jpg','Early childhood students learning with their teacher',
 '<p>A developmentally based program for infants through Junior Kindergarten. Creative, engaging teachers provide project-based and interactive experiences through which children grow cognitively, socially, emotionally, physically, spiritually, and technologically.</p><div class="chips"><span>Kabbalat Shabbat weekly</span><span>5th Grade/ECC Buddy Program</span><span>Hebrew immersion</span><span>Neshama Project enrichment</span></div>'+
 acc('Infant Room (3–18 months)','Loved, nurtured, and kept safe. Flexible full-day and half-day programs with before and after hours options.')+
 acc('Little Lions (3–24 months)','Attend with a parent or caregiver, once a week for 45 minutes, with music, movement, and Jewish cultural, holiday, and Shabbat experiences.')+
 acc('ECC1 (18–24 months)','An extension of infant care supporting children turning two mid-year, building comfort with group play and transitions.')+
 acc('ECC2 (Two-year-olds)','Two mornings to five full days a week. Play-based, theme-based curriculum with literature, art, music, Hebrew language, and library.')+
 acc('ECC3 (Three-year-olds)','Three mornings to five full days a week, with weekly music, physical education, Hebrew immersion, library, and science (STEM).')+
 acc('Junior Kindergarten','A full-day program for kindergarten readiness: pre-reading, math readiness, small-group centers, and Lower School specials.')+
 '<p class="src" style="margin-top:12px">New to Jewish preschool? Greater MetroWest Right Start provides a $1,000 gift voucher toward tuition for families enrolling for the first time.</p>')
P+=prog('lower','Lower School · K–5','A progressively challenging foundation for learning and life.','lower.jpg','Lower School students working together at a table',
 '<p>The dual curriculum is individualized, challenging, and integrated to ensure that students develop a love of learning, gain confidence as learners, and learn key foundation skills.</p><ul class="ck"><li><b>Language arts:</b> literature-based, with emphasis on phonetic awareness and decoding</li><li><b>Math:</b> algebra-based problem-solving, with enrichment for strong mathematical aptitude</li><li><b>Science:</b> hands-on labs taught by a specialist</li><li><b>Hebrew:</b> total immersion with TAL AM / TAL SELA, plus a Mechina option</li><li><b>Israel &amp; Tikkun Olam:</b> weekly Israeli Rishonim visits and social action projects</li></ul>',rev=True,alt_bg=True)
P+=prog('middle','Middle School · 6–8','Rigorous preparation and character for high school and beyond.','middle.jpg','Middle School students reviewing work with a teacher',
 '<p>A strong departmentalized program with group instruction, a highly individualized academic program, and personalized high school transition services.</p><ul class="ck"><li>Honors-level language arts and research paper writing</li><li>Accelerated math; most 8th graders finish algebra or even geometry</li><li>Hebrew with the NETA curriculum; Spanish; Jewish history including Holocaust studies</li><li>Capstone educational trip to Israel in 8th grade</li><li>High School Transition Coordinator guiding families from spring of 7th grade</li></ul>')
P+=prog('stem','STEM Education','Coding and making, starting at age three.','services.jpg','Students collaborating on schoolwork',
 '<p>Students as young as three in the ECC and K–5 students are immersed in a robust bi-weekly science curriculum using ChromeBooks, iPads, Ozobots, Spheros, Bee Bots, and Lego Robotics to learn coding.</p><div class="chips"><span>Science lab &amp; weather station</span><span>Makers Movement</span><span>Robotics</span><span>Drones</span><span>Rocketry</span><span>Computer building</span></div><p>GRTWA is a recipient of the Dr Lynne B Harrison STEM Grant, supporting enriched Middle School STEM and after-school programming.</p>',rev=True,alt_bg=True)
P+=prog('arts','The Arts','Visual arts, music, and drama, every day.','why.jpg','A young student presenting in a classroom',
 '<p>The art curriculum incorporates the elements of design: color, line, texture, pattern, and space. Through drawing, painting, ceramics, and mixed media, students are introduced to masters such as Van Gogh, Mondriaan, Matisse, and Monet.</p><p>Students learn vocal and performance skills, read basic music, and play instruments, with many performance opportunities, building creative, collaborative, and public speaking skills from an early age.</p>')
P+=prog('athletics','Athletics · GRTWA Lions','Participation, sportsmanship, and fun.','athletics.jpg','Students playing in the gym',
 '<p>Athletic participation is encouraged from ECC through 8th grade. All students in 5th through 8th grade can compete in interscholastic co-ed sports, and during games, every student gets a chance to play.</p><div class="chips"><span>Fall · Soccer</span><span>Winter · Basketball &amp; Volleyball</span><span>Spring · Intramurals</span></div><p class="src">The Lions compete against day schools and private schools of similar size in a non-conference league.</p>',rev=True,alt_bg=True)
P+=prog('judaic','Judaic Studies & Hebrew','A strong Jewish identity that guides how students learn, lead, and live.','chai.jpg','Students holding an Israeli flag',
 '<p>A solid foundation in Hebrew language, sacred text study (Torah, Prophets/Tanach), and the culture, history, traditions, and practices of the Jewish people.</p><ul class="ck"><li>Total-immersion Modern Hebrew, with a Mechina program for later starters</li><li>Weekly visits from Israeli Rishonim through the Federation program</li><li>Tefillah, holiday celebrations, and lifecycle learning</li><li>Character education: tzedakah, empathy, fairness, and Tikkun Olam</li></ul>')
P+=f'''<section class="prog alt" id="camp"><div class="w g2 rev"><div class="rv"><img src="img/camplogo.jpg" alt="Camp Neshama at GRTWA logo" style="border-radius:24px;background:#fff;box-shadow:var(--sh)" loading="lazy"><div class="ph" style="margin-top:16px"><img src="img/program.jpg" alt="Young children running in the gym" loading="lazy"></div></div>
<div class="rv"><span class="eb">Summer · Camp Neshama</span><h2>A summer camp bursting with fun and discovery.</h2><div class="chips"><span>Ages 2–5</span><span>June 24 – August 14, 2026</span><span>22-acre campus</span></div>
<p>A high-quality summer experience filled with joyful learning, hands-on exploration, and meaningful Jewish moments, blending play, creativity, and experiential Jewish education.</p>
<div class="btns">{ext(O+"/school_life/camp_neshama/camp_dates_and_rates","Camp dates &amp; rates","btn p")}{ext(O+"/school_life/camp_neshama/meet_our_directors","Meet the directors","btn g")}</div></div></div></section>
<section><div class="w"><div class="band"><div><h2>See it in person.</h2><p>The best way to know GRTWA is to visit, tour, and observe a classroom.</p></div><div><a class="btn p" href="visit.html">Book a tour</a></div></div></div></section>'''
pages['programs.html']=page('programs.html','Programs','Early Childhood, Lower School, Middle School, STEM, Arts, Athletics, Judaic Studies, and Camp Neshama.',P)

# ---------- TUITION ----------
pages['tuition.html']=page('tuition.html','Tuition & Affordability','Estimate your family cost with the TuitionMAX 14% of AGI cap.',phero('Tuition &amp; Affordability','Every Jewish child deserves the gift of a day school education.','Through TuitionMAX, families on assistance will never pay more than 14% of their adjusted gross income toward K–8 tuition, no matter how many children are enrolled.','admissions.jpg')+f'''
<section><div class="w g2" style="align-items:start">
<div class="card rv" style="padding:30px;box-shadow:var(--sh)"><span class="eb">TuitionMAX estimator</span><h2 style="font-size:30px">What might my family pay?</h2>
<span class="sample">Sample tuition placeholder: the school would enter its published rates</span>
<form id="est" oninput="calc()" onsubmit="return false">
<label for="agi">Household adjusted gross income (AGI)</label><input id="agi" type="number" inputmode="numeric" min="0" step="1000" value="150000">
<div class="row2"><div><label for="kids">Children in K–8</label><select id="kids"><option>1</option><option selected>2</option><option>3</option><option>4</option><option>5</option></select></div>
<div><label for="ecc">ECC siblings</label><select id="ecc"><option selected>0</option><option>1</option><option>2</option></select></div></div>
<div class="row2"><div><label for="tk8">K–8 tuition per child <span class="sample" style="padding:1px 7px;font-size:11px">SAMPLE</span></label><input id="tk8" type="number" step="500" value="20000"></div>
<div><label for="tecc">ECC tuition per child <span class="sample" style="padding:1px 7px;font-size:11px">SAMPLE</span></label><input id="tecc" type="number" step="500" value="15000"></div></div></form>
<div style="background:#fff6f0;border-radius:18px;padding:20px;margin-top:20px">
<div style="display:flex;justify-content:space-between"><span>Sample full tuition</span><b id="full">–</b></div>
<div style="display:flex;justify-content:space-between;margin-top:6px"><span>14% of AGI cap</span><b id="cap">–</b></div>
<div style="border-top:1px solid #f3d6c4;margin:12px 0"></div>
<div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font-weight:600;color:var(--navy)">Estimated maximum family cost</span><b id="pay" style="font:700 34px Fraunces,serif;color:var(--or)">–</b></div>
<div class="bar" style="margin-top:12px"><i id="pbar" style="width:0"></i></div><p class="src" id="note" style="margin:10px 0 0"></p></div>
<p class="src" style="margin-top:14px">Illustration only, not an offer of aid. Per the school's published policy, TuitionMAX caps a family's K–8 obligation at no more than 14% of AGI, including ECC siblings of K–8 students. Assistance is based on need and available funds, and families must enroll and provide financial information to the Tuition Assistance Committee. ECC-only families can apply for partial scholarships through several small funds. Fees are not included.</p></div>
<div class="rv"><span class="eb">How it works</span><h2>Affordability is central to who we are.</h2>
<ul class="ck"><li>Applications are strictly confidential and handled with dignity and compassion</li><li>Assistance is available for families with children in grades K–8</li><li>GRTWA subscribes to the NAIS principles of fair practice for financial aid</li><li>Tuition covers approximately 70% of the cost of educating each child; giving closes the gap</li></ul>
<div class="card" style="margin-top:22px"><h3>Get a personalized estimate</h3><span class="sample">Concept preview · nothing is sent</span>
<form class="demo"><div class="row2"><div><label for="ln">Name</label><input id="ln" required autocomplete="name"></div><div><label for="le">Email</label><input id="le" type="email" required autocomplete="email"></div></div>
<label for="lg">Child's grade next year</label><select id="lg"><option>Infant / Toddler</option><option>Early Childhood</option><option>Kindergarten</option><option>Grades 1–5</option><option>Grades 6–8</option></select>
<button class="btn p" style="width:100%;margin-top:16px">Request my estimate</button><div class="ok" role="status">Thanks! In the live version, the school's finance office would follow up. (Concept preview: nothing was sent.)</div></form></div>
<p class="src" style="margin-top:16px">Questions on affordability: Joe Weiss, Chief Financial Officer, ext 3010. School information: Alyssa Glaubman, Outreach and Engagement Coordinator, ext 3346. Main number {PHONE}.</p>
<div class="btns">{ext(O+"/admissions/affordability_tuitionmax","Official affordability page","btn g")}{ext(APPLY,"Apply","btn p")}</div></div></div></section>''',extra_js='''<script>
const $=i=>document.getElementById(i),f=n=>'$'+Math.round(n).toLocaleString();
function calc(){const agi=+$('agi').value||0,k=+$('kids').value,e=+$('ecc').value,full=k*(+$('tk8').value||0)+e*(+$('tecc').value||0),cap=agi*.14,pay=Math.min(full,cap);
$('full').textContent=f(full);$('cap').textContent=f(cap);$('pay').textContent=f(pay);$('pbar').style.width=(full?pay/full*100:0)+'%';
$('note').textContent=pay<full?'At this income, the 14% cap could reduce sample tuition by '+f(full-pay)+' ('+Math.round((1-pay/full)*100)+'%).':'At this income, the 14% cap is above sample full tuition.'}
calc();</script>''')

# ---------- GIVE ----------
def fund(t,d,link,amts,cta,lbl='Secure Stripe checkout'):
    a=''.join(f'<button type="button" aria-pressed="false">${x:,}</button>' for x in amts)
    return f'<div class="card fund rv"><h3>{t}</h3><p class="src" style="font-size:15px">{d}</p><div class="amts" role="group" aria-label="Suggested amounts">{a}</div><p class="src pick" style="min-height:1.4em"></p>{ext(link,cta+" ↗","btn p")}<small class="src" style="margin-top:8px;text-align:center">{lbl}</small></div>'
G=phero('Give &amp; Pay','Every gift strengthens a GRTWA education.','Tuition covers approximately 70% of the cost of educating each child. Gifts support teacher enrichment, special programming, and scholarships. One place for every way to give or pay.','donate2.jpg')
G+=f'''<section><div class="w">
<div class="card rv" style="padding:30px;margin-bottom:34px;box-shadow:var(--sh)"><div style="display:flex;justify-content:space-between;flex-wrap:wrap;gap:10px;align-items:center"><div><span class="eb">Shomrei Torah · Annual Campaign</span><h2 style="font-size:30px;margin:0">The cornerstone of operational and scholarship support.</h2></div><span class="sample">Sample progress · illustrative figures only</span></div>
<div style="display:flex;justify-content:space-between;margin:22px 0 8px;font-weight:600"><span style="color:var(--or);font:700 28px Fraunces,serif">$62,000 raised <small class="src">(sample)</small></span><span class="src">of $100,000 sample goal</span></div>
<div class="bar" style="height:18px"><i data-w="62%"></i></div><p class="src" style="margin-top:8px">62% of sample goal · The school would connect live totals here.</p>
{ext("https://www.wizevents.com/shomreitorah2027/","Give to Shomrei Torah ↗","btn p")}</div>
<div class="hd rv"><span class="eb">Pay &amp; donate</span><h2>Choose where your gift goes.</h2><p>Tap a suggested amount, then enter it on the school's secure Stripe page. Links go to GRTWA's existing payment pages.</p></div>
<div class="g3">
{fund("Donate to GRTWA","Support outstanding academics, Jewish values, and a nurturing community for every student.",S_DONATE,[18,36,180,360,1800],"Donate")}
{fund("Enrichment","Pay for an enrichment program. Please indicate the total cost you are paying.",S_ENR,[50,100,250],"Pay for enrichment")}
{fund("8th Grade Fundraiser","Support the 8th grade class fundraiser.",S_8TH,[18,36,72,180],"Support the 8th grade")}
{fund("Community Dinner / Program","Pay for the Community Dinner or a community program.",S_DIN,[36,72,180,360],"Pay for dinner / program")}
<div class="card fund rv"><h3>Pay for a Program</h3><p class="src" style="font-size:15px">All school program payments in one spot. Indicate the total cost on the form.</p><div style="display:grid;gap:8px;margin:12px 0">{ext(S_ENR,"Enrichment ↗","btn g")}{ext(S_8TH,"8th Grade Fundraiser ↗","btn g")}{ext(S_DIN,"Community Dinner/Program ↗","btn g")}</div><small class="src" style="margin-top:auto;text-align:center">Same links as grtwacademy.org/school_life/pay_for_a_program</small></div>
<div class="card fund rv" style="background:var(--navy);color:#fff"><h3 style="color:#fff">More ways to give</h3><ul style="list-style:none;padding:0;margin:8px 0;line-height:2.1">
<li>{ext("https://www.wizevents.com/grtwaisraeltripfund/","8th Grade Israel Trip Fund ↗")}</li><li>{ext("https://www.wizevents.com/grtwacircleoflife/","Circle of Life Wall ↗")}</li><li>{ext("https://www.wizevents.com/grtwalibrarymediacenter/","Wolff Library/Media Center ↗")}</li><li>{ext("https://www.wizevents.com/grtwatribute/","Send a Tribute ↗")}</li><li>{ext("https://www.wizevents.com/grtwageneraldonation/","General Fund ↗")}</li><li>{ext(O+"/development/giving_opportunities/planned_giving","Planned Giving ↗")}</li></ul></div>
</div><p class="src" style="text-align:center;margin-top:24px">GRTWA is a 501(c)(3) nonprofit; contributions are acknowledged in writing and deductible to the full extent of the law. Questions: Naomi Bacharach '79, Director of Institutional Advancement, ext 3015. Suggested amounts are concept placeholders.</p></div></section>'''
pages['give.html']=page('give.html','Give & Pay','Donate, pay for a program, and support GRTWA funds in one place.',G,extra_js='''<script>document.querySelectorAll('.fund').forEach(c=>c.querySelectorAll('.amts button').forEach(b=>b.onclick=()=>{c.querySelectorAll('.amts button').forEach(x=>{x.classList.toggle('on',x==b);x.setAttribute('aria-pressed',x==b)});c.querySelector('.pick').textContent='Enter '+b.textContent+' on the secure page.'}))</script>''')

# ---------- PARENTS ----------
pages['parents.html']=page('parents.html','Parents Hub','Events, calendar, FACTS portal, and volunteering for GRTWA families.',phero('Parents Hub','Everything families need, in one place.','Every GRTWA parent is automatically a member of the Parent Association, dedicated to communication, celebration, and support.','pa.jpg')+f'''
<section><div class="w"><div class="g3" style="margin-bottom:44px">
<a class="path rv" href="{FACTS}" target="_blank" rel="noopener"><span class="ic">🔐</span><b>FACTS / ParentsWeb</b><small>Grades, billing, and family information.</small><span class="ar">Log in ↗</span></a>
<a class="path rv" href="{GCAL}" target="_blank" rel="noopener"><span class="ic">🗓️</span><b>School Calendar</b><small>The official GRTWA Google Calendar.</small><span class="ar">Open calendar ↗</span></a>
<a class="path rv" href="give.html"><span class="ic">💳</span><b>Pay for a Program</b><small>Enrichment, 8th grade, and community dinner.</small><span class="ar">Give &amp; pay →</span></a></div>
<div class="g2" style="align-items:start"><div><span class="eb">Upcoming events</span><h2>What's going on at GRTWA</h2><p class="src">Events listed on grtwacademy.org as of Oct 22, 2026. Add any event to your calendar.</p><div id="evlist"></div></div>
<div><div class="card rv" style="box-shadow:var(--sh)"><span class="eb">Volunteer</span><h3>Lend a hand with the PA</h3><span class="sample">Concept preview · nothing is sent</span>
<form class="demo"><div class="row2"><div><label for="vn">Name</label><input id="vn" required autocomplete="name"></div><div><label for="ve">Email</label><input id="ve" type="email" required autocomplete="email"></div></div>
<label for="vi">I'd like to help with</label><select id="vi"><option>Book Fair</option><option>Holiday Enrichment</option><option>Rosh Chodesh Celebrations</option><option>School Pictures</option><option>Staff Welcome Luncheon</option><option>Social Events</option><option>Fundraising</option></select>
<button class="btn p" style="width:100%;margin-top:16px">Sign me up</button><div class="ok" role="status">You're on the list! (Concept preview: nothing was sent.)</div></form>
<p class="src" style="margin-top:12px">Real signup today: {ext(VOL,"PA volunteer form ↗")} or call the main office at {PHONE}.</p></div>
<div class="card rv" style="margin-top:18px"><h3>What the PA does</h3><ul class="ck"><li>Book Fair</li><li>Graduate &amp; B'nai Mitzvah gifts</li><li>Holiday enrichment: Sukkot, Chanukah, Purim, Tu B'Shevat, Pesach</li><li>Monthly Rosh Chodesh breakfasts</li><li>School pictures each fall</li><li>Staff Welcome Luncheon</li></ul></div></div></div></div></section>''',extra_js='<script src="js/events.js" defer></script>')

# ---------- ABOUT ----------
STAFF=[('Administration',[('Rabbi Will Keller','Head of School','3021','keller'),('Mr Joe Weiss','Chief Financial Officer','3010','weiss'),("Mrs Naomi Bacharach '79",'Director of Institutional Advancement','3015','bacharach'),('Ms Yeneida Colon','Director of Operations','3014','colon'),('Mrs Rachel Meiner','Director of the Lillie Brandt Early Childhood Center','3017','meiner')]),
('Leadership Team',[('Ms Nurit Lev','Vice Principal of Judaic Studies','3316'),('Mrs Rosa Lynch','Vice Principal of Elementary General Studies; Academic Excellence Coordinator','3023'),('Ms Sheri Swiss','Vice Principal of Middle School General Studies; High School Transition Coordinator','3308')]),
('Classroom Staff',[('Mrs Erica Arman','Science Teacher','3341'),('Ms Raya Benhaim','Judaic Studies Teacher','3348'),('Ms Sara Borden','General Studies Teacher','3334'),('Mrs Kaitlyn Brady','Infant & ECC1 Caregiver Assistant',''),('Mrs Selena Campione','Associate Teacher','3305'),('Rabbi Yitzchok Cohen','Judaic Studies Teacher','3318'),('Ms Morgan DeLoreto','MS Math Teacher & Elementary Enrichment','3348'),('Ms Marisa Dubofsky','Kindergarten Teacher','3325'),('Mr Andrew Eitel','General Studies Teacher & Special Education','3344'),('Mrs Melissa Estwin','General Studies Teacher','3304'),('Mrs Shelly Forman','MS Math Teacher & Elementary Enrichment','3347'),('Ms Zoe Freeman','ECC Assistant Teacher',''),('Mrs Rachel Fried','Judaic Studies Teacher','3313'),('Ms Sara Kirsch','ECC Assistant Teacher',''),('Mrs Natalia Labkovsky','ECC Assistant Teacher','3002'),('Ms Nurit Lev','Judaic Studies Teacher','3024'),('Mrs Lara Levine','Art Teacher','3317'),('Ms Rhonda Levine','ECC Teacher','3324'),('Mrs Colleen Longo','ECC Assistant Teacher','3303'),('Mrs Yesenia Lucero','Infant & ECC1 Caregiver',''),('Mrs Rosa Lynch','General Studies Teacher','3023'),('Ms Leanza Martinez','ECC1 Caregiver',''),('Ms Nicole Murphy','ECC Teacher','3315'),('Mrs Jaime Nahan','ECC Teacher','3309'),('Ms Rebekah Narley','ECC Teacher','3302'),('Ms Sara Nigro','ECC Assistant Teacher',''),('Mrs Rachel Padian','Reading Specialist',''),('Ms Nancy Peled Wolf','Judaic Studies Teacher','3338'),('Ms Celia Ramos','Infant Caregiver','3110'),('Mrs Amanda Romano','ECC Teacher','3306'),('Ms Janice Rozenwasser','Judaic Studies & Spanish Teacher','3311'),('Ms Lori Seigerman','Kindergarten Teacher','3326'),('Mr Paul Solomon','Physical Education & Health Teacher','3025'),('Ms Sheri Swiss','General Studies Teacher','3308'),('Ms Sandra Urday','Infant & ECC1 Caregiver',''),('Mrs Vered Weinglass','Science Teacher','3339'),('Mrs Rona Zimmerman','ECC Assistant Teacher','')]),
('Support Staff',[('Dr Cheryl Bahar','Director of Special Services','3011'),('Mrs Kate Davis','Admissions and Office of Institutional Advancement Coordinator','3019'),('Mrs Natalie Flanagan','Director of Educational Technology','3020'),('Ms Alyssa Glaubman','Outreach and Engagement Coordinator','3346'),('Mrs Jill Granik','Administrative Assistant',''),('Mrs Meredith Legatt','Nurse','3018'),('Mrs Rebekah Lillianthal','Social Worker','3029'),('Mr Tom Miller','Security','3345'),('Mrs Caryn Reppen','Social Worker','3028'),('Mr Mike Ryan','Custodian','3026'),('Mr Matt Shannon','IT Coordinator','3022'),('Mr Mike Sillcox','Custodian','3026'),('Ms Kim Synalovksi','Bookkeeper','3013'),('Ms Michele Wasserman','Receptionist','3012')])]
cards=''
for grp,ppl in STAFF:
    for p in ppl:
        n,r,x=p[:3];ph=p[3] if len(p)>3 else None
        ini=''.join(w[0] for w in n.replace("'79",'').split()[1:3])
        av=f'<img src="img/s_{ph}.jpg" alt="" loading="lazy">' if ph else ini
        cards+=f'<div class="person" data-g="{grp}" data-s="{html.escape((n+" "+r).lower())}"><div class="av">{av}</div><div><b>{html.escape(n)}</b><small>{html.escape(r)}</small><div class="x">{"ext "+x if x else ""}</div></div></div>'
btns='<button class="on" data-f="">All</button>'+''.join(f'<button data-f="{g}">{g}</button>' for g,_ in STAFF)
pages['about.html']=page('about.html','About & Our Story','The history, mission, and faculty of Gottesman RTW Academy.',phero('About · Our Story','Nearly 60 years of Jewish education in Morris County.','Founded in 1967 as Hebrew Academy of Morris County, GRTWA is the only Jewish community day school in Northwestern New Jersey.','front.jpg')+f'''
<section><div class="w g2" style="align-items:start"><div class="rv"><span class="eb">Our mission</span><h2>Lifelong learners, compassionate individuals, rooted in their heritage.</h2><p class="lead">Gottesman RTW Academy maintains high standards of academic excellence while nurturing each student's social and emotional needs and growth. As a community day school, GRTWA celebrates the richness of Jewish life, has a strong connection to Israel, and welcomes families from a wide range of Jewish backgrounds.</p>
<div class="logos" style="margin-top:24px"><img src="img/njais.png" alt="NJAIS"><img src="img/prizmah.png" alt="Prizmah"></div><p class="src" style="margin-top:10px">Accredited by and a member of the New Jersey Association of Independent Schools (NJAIS); member of the National Association of Independent Schools (NAIS) and Prizmah. Awarded a Blue Ribbon by the U.S. Department of Education.</p></div>
<div class="rv"><span class="eb">Timeline</span><div class="tline">
<div><b>1966</b><p>Two Morristown couples, Morty z"l and Beatsy z"l Wertheimer and Charlotte and Alvin z"l Turner, share a vision for a Jewish day school, joined by Michael z"l and Midge z"l Rubenstein.</p></div>
<div><b>1967</b><p>Hebrew Academy of Morris County (HAMC) is founded.</p></div>
<div><b>Green campus</b><p>A state-of-the-art green facility on a 22-acre Randolph campus, with solar panels, rain gardens, and flexible, technologically advanced classrooms.</p></div>
<div><b>Today</b><p>Renamed Gottesman RTW Academy, honoring the founding families (the Rubensteins, Turners, and Wertheimers) and Paula and Jerry Gottesman, whose $15 million challenge gift provided transformative support.</p></div></div></div></div></section>
<section class="alt"><div class="w g2"><div class="ph rv"><img src="img/founders.jpg" alt="Archival photo of the school's founders" style="aspect-ratio:auto" loading="lazy"></div><div class="rv"><span class="eb">What's in a name</span><h2>R · T · W</h2><p class="lead">The "RTW" honors the three founding families, the Rubensteins, the Turners, and the Wertheimers, whose vision, dedication, and belief in the power of Jewish education laid the foundation for the vibrant community that exists today.</p></div></div></section>
<section id="head"><div class="w g2"><div class="rv"><span class="eb">Head of School</span><h2>A welcome from Rav Will Keller</h2>
<p>At Gottesman RTW Academy, we believe that children thrive when school and family work together. That partnership is at the heart of everything we do, helping each child grow into a curious learner, compassionate leader, proud Jew, and caring member of the community.</p>
<p>Learning at GRTWA is both joyful and challenging. Our exceptional faculty inspire curiosity, encourage critical thinking, and nurture each child's unique strengths.</p>
<p>Whether you are exploring Jewish day school for the first time or are already part of our family, I invite you to visit our campus to meet our students and faculty. I look forward to welcoming you personally.</p><p><b>B'Shalom, Rav Will Keller</b></p></div>
<div class="ph rv" style="max-width:360px;justify-self:center"><img src="img/rav.jpg" alt="Rabbi Will Keller" style="aspect-ratio:3/4" loading="lazy"></div></div></section>
<section class="alt" id="staff"><div class="w"><div class="hd"><span class="eb">Faculty &amp; Staff</span><h2>Staff directory</h2><p>All extensions can be reached by first dialing the main number, <a href="{TEL}">{PHONE}</a>.</p></div>
<div class="dir-tools"><input id="q" type="search" placeholder="Search by name or role" aria-label="Search staff">{btns}</div>
<div class="staff" id="staffg">{cards}</div><p class="src" style="margin-top:16px">Source: grtwacademy.org Faculty and Staff page; names, roles, and extensions as listed there. Some staff appear in more than one role.</p></div></section>''',extra_js='''<script>
let g='';const q=document.getElementById('q');function f(){const v=q.value.toLowerCase();document.querySelectorAll('.person').forEach(p=>p.style.display=(!g||p.dataset.g==g)&&p.dataset.s.includes(v)?'':'none')}
q.oninput=f;document.querySelectorAll('.dir-tools button').forEach(b=>b.onclick=()=>{g=b.dataset.f;document.querySelectorAll('.dir-tools button').forEach(x=>x.classList.toggle('on',x==b));f()})</script>''')

# ---------- CONTACT ----------
def ct(t,n,r,x):return f'<div class="card"><span class="eb">{t}</span><b style="display:block;color:var(--navy)">{n}</b><small class="src">{r}</small><div style="color:var(--or);font-weight:600;font-size:14px">ext {x}</div></div>'
pages['contact.html']=page('contact.html','Contact','Address, phone, and directions for Gottesman RTW Academy.',phero('Contact','We would love to hear from you.','Have questions or need more information? Reach out and the team will be glad to connect with you.','apply.jpg')+f'''
<section><div class="w g2" style="align-items:stretch"><div class="rv"><h2>Visit our campus</h2><p class="lead">{ADDR}</p>
<div class="btns" style="margin-bottom:24px"><a class="btn p" href="{TEL}">📞 {PHONE}</a>{ext("https://www.google.com/maps/dir/?api=1&destination=146+Dover+Chester+Rd,+Randolph,+NJ+07869","Get directions ↗","btn g")}</div>
<p class="src">Fax 973.584.0602 · Local school district busing, carpools, or private transportation services are available.</p>
<div class="g2" style="gap:12px;margin-top:20px">{ct("General information","Ms Yeneida Colon","Director of Operations","3014")}{ct("Admissions &amp; outreach","Ms Alyssa Glaubman","Admissions and Outreach &amp; Engagement Coordinator","3346")}{ct("Development","Mrs Naomi Bacharach '79","Director of Institutional Advancement","3015")}{ct("Financial information","Mr Joe Weiss","Chief Financial Officer","3010")}</div>
<p style="margin-top:18px"><a href="about.html#staff">Full faculty &amp; staff directory →</a></p></div>
<div class="rv"><iframe class="map" title="Map of Gottesman RTW Academy" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=146+Dover+Chester+Rd,+Randolph,+NJ+07869&output=embed"></iframe></div></div></section>''')

pages['simulation.html']=page('simulation.html','See How It Works (Simulation)','An interactive simulation of tour booking and automatic follow-up, using sample data.',phero('Interactive simulation','See how it all works, start to finish.','Book a sample tour, watch the follow-up messages go out on their own, and see what the admissions office sees. Sample data only; nothing is sent.','tour.jpg')+open('parts/sim.html').read(),extra_css='<link rel="stylesheet" href="css/tour.css"><link rel="stylesheet" href="css/sim.css">',extra_js='<script src="js/sim.js"></script>')

for k,v in pages.items():open(k,'w').write(v)
print('built',list(pages))
