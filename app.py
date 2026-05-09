import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image
import base64

# ── Page config ────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Grand Ventures | Fire & Life Safety Buy-and-Build",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Sans:wght@300;400;500;600&display=swap');

:root {
    --navy: #1F2D3D;
    --teal: #0F6E56;
    --tealL: #E1F5EE;
    --amber: #854F0B;
    --amberL: #FAEEDA;
    --red: #A32D2D;
    --off: #F8F9FA;
    --grey: #F5F5F2;
    --dkgrey: #64748B;
    --white: #FFFFFF;
}

* { box-sizing: border-box; }

.stApp {
    background: var(--navy);
    font-family: 'DM Sans', sans-serif;
}

/* Hide streamlit default elements */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
[data-testid="stSidebar"] { display: none; }

/* ── HERO ── */
.hero {
    background: linear-gradient(135deg, #1F2D3D 0%, #0d1e2e 60%, #0F6E56 100%);
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    padding: 80px 10% 60px;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: '';
    position: absolute;
    top: -50%;
    right: -20%;
    width: 600px;
    height: 600px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(15,110,86,0.15) 0%, transparent 70%);
    pointer-events: none;
}
.hero::after {
    content: '';
    position: absolute;
    bottom: -100px;
    left: 30%;
    width: 400px;
    height: 400px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(133,79,11,0.08) 0%, transparent 70%);
    pointer-events: none;
}
.hero-tag {
    font-family: 'DM Sans', sans-serif;
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 3px;
    color: #0F6E56;
    text-transform: uppercase;
    margin-bottom: 24px;
    padding: 6px 16px;
    border: 1px solid rgba(15,110,86,0.4);
    border-radius: 20px;
    display: inline-block;
}
.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(42px, 6vw, 80px);
    font-weight: 900;
    color: #FFFFFF;
    line-height: 1.05;
    margin-bottom: 16px;
    max-width: 750px;
}
.hero-title span {
    color: #0F6E56;
}
.hero-sub {
    font-family: 'DM Sans', sans-serif;
    font-size: 18px;
    font-weight: 300;
    color: rgba(202,220,252,0.85);
    max-width: 580px;
    line-height: 1.7;
    margin-bottom: 40px;
}
.hero-stats {
    display: flex;
    gap: 48px;
    margin-bottom: 48px;
    flex-wrap: wrap;
}
.hero-stat {
    display: flex;
    flex-direction: column;
}
.hero-stat-num {
    font-family: 'Playfair Display', serif;
    font-size: 36px;
    font-weight: 700;
    color: #FFFFFF;
    line-height: 1;
}
.hero-stat-label {
    font-size: 12px;
    color: rgba(202,220,252,0.6);
    letter-spacing: 1px;
    margin-top: 4px;
    text-transform: uppercase;
}
.hero-divider {
    width: 1px;
    height: 48px;
    background: rgba(255,255,255,0.15);
    align-self: center;
}
.hero-cta {
    display: flex;
    gap: 16px;
    flex-wrap: wrap;
}
.btn-primary {
    background: #0F6E56;
    color: white;
    padding: 14px 32px;
    border-radius: 4px;
    font-family: 'DM Sans', sans-serif;
    font-size: 14px;
    font-weight: 600;
    letter-spacing: 0.5px;
    text-decoration: none;
    display: inline-block;
    border: none;
    cursor: pointer;
    transition: all 0.2s;
}
.btn-secondary {
    background: transparent;
    color: white;
    padding: 14px 32px;
    border-radius: 4px;
    font-family: 'DM Sans', sans-serif;
    font-size: 14px;
    font-weight: 500;
    text-decoration: none;
    display: inline-block;
    border: 1px solid rgba(255,255,255,0.3);
    cursor: pointer;
}

/* ── SECTION WRAPPERS ── */
.section-light {
    background: var(--off);
    padding: 80px 10%;
}
.section-dark {
    background: var(--navy);
    padding: 80px 10%;
}
.section-teal {
    background: var(--teal);
    padding: 80px 10%;
}
.section-mid {
    background: #253C52;
    padding: 80px 10%;
}

.section-tag {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 3px;
    color: var(--teal);
    text-transform: uppercase;
    margin-bottom: 12px;
}
.section-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(28px, 4vw, 48px);
    font-weight: 700;
    color: var(--navy);
    line-height: 1.15;
    margin-bottom: 16px;
}
.section-title-light {
    font-family: 'Playfair Display', serif;
    font-size: clamp(28px, 4vw, 48px);
    font-weight: 700;
    color: var(--white);
    line-height: 1.15;
    margin-bottom: 16px;
}
.section-sub {
    font-size: 16px;
    color: var(--dkgrey);
    line-height: 1.7;
    max-width: 640px;
    margin-bottom: 48px;
}
.section-sub-light {
    font-size: 16px;
    color: rgba(202,220,252,0.75);
    line-height: 1.7;
    max-width: 640px;
    margin-bottom: 48px;
}

/* ── CARDS ── */
.card-grid-3 {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
    margin-top: 40px;
}
.card-grid-2 {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 24px;
    margin-top: 40px;
}
.card {
    background: var(--white);
    border-radius: 8px;
    padding: 32px;
    border: 1px solid #E2E8F0;
    position: relative;
    overflow: hidden;
}
.card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 4px;
    height: 100%;
    background: var(--teal);
}
.card-dark {
    background: rgba(255,255,255,0.05);
    border-radius: 8px;
    padding: 32px;
    border: 1px solid rgba(255,255,255,0.1);
    position: relative;
    overflow: hidden;
}
.card-dark::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 4px;
    height: 100%;
    background: var(--teal);
}
.card-num {
    font-family: 'Playfair Display', serif;
    font-size: 48px;
    font-weight: 700;
    color: var(--teal);
    line-height: 1;
    margin-bottom: 8px;
}
.card-title {
    font-size: 16px;
    font-weight: 600;
    color: var(--navy);
    margin-bottom: 8px;
}
.card-title-light {
    font-size: 16px;
    font-weight: 600;
    color: var(--white);
    margin-bottom: 8px;
}
.card-body {
    font-size: 14px;
    color: var(--dkgrey);
    line-height: 1.6;
}
.card-body-light {
    font-size: 14px;
    color: rgba(202,220,252,0.75);
    line-height: 1.6;
}
.card-source {
    font-size: 11px;
    color: var(--teal);
    font-style: italic;
    margin-top: 12px;
    display: block;
}

/* ── STAT ROW ── */
.stat-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 0;
    background: var(--navy);
    border-radius: 8px;
    overflow: hidden;
    margin-top: 40px;
}
.stat-cell {
    padding: 32px 24px;
    text-align: center;
    border-right: 1px solid rgba(255,255,255,0.08);
}
.stat-cell:last-child { border-right: none; }
.stat-big {
    font-family: 'Playfair Display', serif;
    font-size: 40px;
    font-weight: 700;
    color: var(--white);
    line-height: 1;
    margin-bottom: 6px;
}
.stat-label {
    font-size: 12px;
    color: rgba(202,220,252,0.6);
    text-transform: uppercase;
    letter-spacing: 1px;
}
.stat-source {
    font-size: 10px;
    color: rgba(202,220,252,0.35);
    margin-top: 4px;
}

/* ── TABLE ── */
.data-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 24px;
    font-size: 14px;
}
.data-table th {
    background: var(--navy);
    color: var(--white);
    padding: 12px 16px;
    text-align: left;
    font-weight: 600;
    font-size: 12px;
    letter-spacing: 0.5px;
    text-transform: uppercase;
}
.data-table td {
    padding: 12px 16px;
    border-bottom: 1px solid #F0F0F0;
    color: #333;
}
.data-table tr:nth-child(even) td { background: var(--grey); }
.badge {
    display: inline-block;
    padding: 3px 10px;
    border-radius: 12px;
    font-size: 11px;
    font-weight: 700;
}
.badge-green { background: #EAF3DE; color: #27500A; }
.badge-amber { background: #FAEEDA; color: #854F0B; }
.badge-red { background: #FCEBEB; color: #A32D2D; }
.badge-blue { background: #E6F1FB; color: #2E5B8A; }

/* ── TEAM ── */
.team-grid {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 20px;
    margin-top: 40px;
}
.team-card {
    background: rgba(255,255,255,0.05);
    border-radius: 8px;
    padding: 24px 16px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.08);
    transition: border-color 0.2s;
}
.team-card:hover {
    border-color: rgba(15,110,86,0.4);
}
.team-avatar {
    width: 64px;
    height: 64px;
    border-radius: 50%;
    background: linear-gradient(135deg, var(--teal), #0a4f3d);
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 16px;
    font-family: 'Playfair Display', serif;
    font-size: 22px;
    font-weight: 700;
    color: white;
}
.team-name {
    font-size: 14px;
    font-weight: 600;
    color: var(--white);
    margin-bottom: 4px;
}
.team-role {
    font-size: 11px;
    color: var(--teal);
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 10px;
}
.team-bio {
    font-size: 12px;
    color: rgba(202,220,252,0.6);
    line-height: 1.5;
}

/* ── MENTOR ── */
.mentor-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
    margin-top: 32px;
}
.mentor-card {
    background: rgba(255,255,255,0.04);
    border-radius: 8px;
    padding: 28px;
    border-left: 4px solid var(--teal);
}
.mentor-name {
    font-size: 16px;
    font-weight: 600;
    color: var(--white);
    margin-bottom: 4px;
}
.mentor-title {
    font-size: 12px;
    color: var(--teal);
    margin-bottom: 12px;
    font-style: italic;
}
.mentor-body {
    font-size: 13px;
    color: rgba(202,220,252,0.7);
    line-height: 1.6;
}

/* ── PROCESS STEPS ── */
.process-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 0;
    margin-top: 40px;
    position: relative;
}
.process-step {
    padding: 32px 24px;
    position: relative;
    text-align: center;
}
.process-step::after {
    content: '→';
    position: absolute;
    right: -8px;
    top: 50%;
    transform: translateY(-50%);
    font-size: 20px;
    color: rgba(15,110,86,0.4);
}
.process-step:last-child::after { display: none; }
.process-num {
    width: 48px;
    height: 48px;
    border-radius: 50%;
    background: var(--teal);
    color: white;
    font-family: 'Playfair Display', serif;
    font-size: 22px;
    font-weight: 700;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 16px;
}
.process-title {
    font-size: 14px;
    font-weight: 600;
    color: var(--navy);
    margin-bottom: 8px;
}
.process-body {
    font-size: 13px;
    color: var(--dkgrey);
    line-height: 1.5;
}

/* ── QUOTE ── */
.quote-block {
    background: var(--navy);
    border-left: 6px solid var(--teal);
    border-radius: 0 8px 8px 0;
    padding: 28px 32px;
    margin: 32px 0;
}
.quote-text {
    font-family: 'Playfair Display', serif;
    font-size: 20px;
    font-style: italic;
    color: var(--white);
    line-height: 1.5;
    margin-bottom: 10px;
}
.quote-attr {
    font-size: 13px;
    color: rgba(202,220,252,0.6);
}

/* ── RETURNS ── */
.returns-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 32px;
    margin-top: 40px;
}
.returns-box {
    background: rgba(255,255,255,0.05);
    border-radius: 8px;
    padding: 32px;
    border: 1px solid rgba(255,255,255,0.08);
}
.returns-box-title {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
    color: var(--teal);
    text-transform: uppercase;
    margin-bottom: 20px;
}
.returns-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 0;
    border-bottom: 1px solid rgba(255,255,255,0.06);
}
.returns-row:last-child { border-bottom: none; }
.returns-key {
    font-size: 13px;
    color: rgba(202,220,252,0.7);
}
.returns-val {
    font-size: 14px;
    font-weight: 600;
    color: var(--white);
}
.returns-val-highlight {
    font-size: 16px;
    font-weight: 700;
    color: var(--teal);
}

/* ── CONTACT ── */
.contact-box {
    background: rgba(255,255,255,0.05);
    border-radius: 8px;
    padding: 48px;
    border: 1px solid rgba(255,255,255,0.1);
    text-align: center;
    max-width: 600px;
    margin: 0 auto;
}

/* ── NAV ── */
.nav {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 100;
    background: rgba(31,45,61,0.95);
    backdrop-filter: blur(10px);
    padding: 16px 10%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-bottom: 1px solid rgba(255,255,255,0.08);
}
.nav-logo {
    font-family: 'Playfair Display', serif;
    font-size: 20px;
    font-weight: 700;
    color: var(--white);
    letter-spacing: 1px;
}
.nav-logo span { color: var(--teal); }
.nav-links {
    display: flex;
    gap: 32px;
    list-style: none;
    margin: 0;
    padding: 0;
}
.nav-links a {
    color: rgba(202,220,252,0.7);
    text-decoration: none;
    font-size: 13px;
    font-weight: 500;
    letter-spacing: 0.5px;
    transition: color 0.2s;
}
.nav-links a:hover { color: var(--white); }

/* ── FOOTER ── */
.footer {
    background: #0d1e2e;
    padding: 40px 10%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-top: 1px solid rgba(255,255,255,0.06);
}
.footer-copy {
    font-size: 12px;
    color: rgba(202,220,252,0.35);
}
.footer-right {
    font-size: 12px;
    color: rgba(202,220,252,0.35);
}

/* ── HIGHLIGHT BOX ── */
.highlight-box {
    background: linear-gradient(135deg, var(--teal), #0a4f3d);
    border-radius: 8px;
    padding: 48px;
    color: white;
    margin: 40px 0;
}
.hl-title {
    font-family: 'Playfair Display', serif;
    font-size: 32px;
    font-weight: 700;
    margin-bottom: 12px;
}
.hl-body {
    font-size: 16px;
    opacity: 0.85;
    line-height: 1.7;
    max-width: 640px;
}

/* Risk row */
.risk-row {
    display: flex;
    gap: 16px;
    align-items: flex-start;
    padding: 16px 0;
    border-bottom: 1px solid #F0F0F0;
}
.risk-row:last-child { border-bottom: none; }
.risk-dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    margin-top: 5px;
    flex-shrink: 0;
}
.risk-title { font-weight: 600; color: var(--navy); font-size: 14px; }
.risk-body { font-size: 13px; color: var(--dkgrey); margin-top: 4px; line-height: 1.5; }

/* Responsive */
@media (max-width: 900px) {
    .card-grid-3, .card-grid-2, .team-grid, .mentor-grid, .process-row, .stat-row { grid-template-columns: 1fr; }
    .returns-grid { grid-template-columns: 1fr; }
    .hero { padding: 100px 6% 60px; }
    .section-light, .section-dark, .section-teal, .section-mid { padding: 60px 6%; }
    .nav { padding: 16px 6%; }
    .footer { padding: 32px 6%; flex-direction: column; gap: 12px; text-align: center; }
}
</style>
""", unsafe_allow_html=True)

# ── NAV ────────────────────────────────────────────────────────────────
st.markdown("""
<nav class="nav">
  <div class="nav-logo">GRAND <span>VENTURES</span></div>
  <ul class="nav-links">
    <li><a href="#thesis">Thesis</a></li>
    <li><a href="#opportunity">Opportunity</a></li>
    <li><a href="#process">Process</a></li>
    <li><a href="#team">Team</a></li>
    <li><a href="#invest">Invest</a></li>
  </ul>
</nav>
""", unsafe_allow_html=True)

# ── HERO ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero" style="margin-top:53px;">
  <div class="hero-tag">🔥 Fire & Life Safety · Southern California · 2026</div>
  <h1 class="hero-title">We Buy Fire Inspection<br>Businesses. We <span>Build</span><br>Platforms. We Exit.</h1>
  <p class="hero-sub">Grand Ventures acquires service-heavy fire and life safety operators in Southern California, builds recurring revenue to 70%+, and exits to national consolidators at 8–12x earnings.</p>
  <div class="hero-stats">
    <div class="hero-stat">
      <span class="hero-stat-num">$22B</span>
      <span class="hero-stat-label">US Market</span>
    </div>
    <div class="hero-divider"></div>
    <div class="hero-stat">
      <span class="hero-stat-num">4–6x</span>
      <span class="hero-stat-label">Entry Multiple</span>
    </div>
    <div class="hero-divider"></div>
    <div class="hero-stat">
      <span class="hero-stat-num">8–12x</span>
      <span class="hero-stat-label">Exit Multiple</span>
    </div>
    <div class="hero-divider"></div>
    <div class="hero-stat">
      <span class="hero-stat-num">~2.3x</span>
      <span class="hero-stat-label">Target MOIC</span>
    </div>
  </div>
  <div class="hero-cta">
    <a href="#invest" class="btn-primary">Co-invest with us →</a>
    <a href="#thesis" class="btn-secondary">Read the thesis</a>
  </div>
</div>
""", unsafe_allow_html=True)

# ── THESIS ─────────────────────────────────────────────────────────────
st.markdown('<div id="thesis"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-light">
  <div class="section-tag">The Thesis</div>
  <div class="section-title">A Simple Arbitrage. An Obvious Gap. A Timed Window.</div>
  <div class="section-sub">Fire inspections are legally mandated. The revenue never goes away. The industry is full of small owner-run businesses where the founder is ready to retire but has no one to sell to. We buy them small and sell them big.</div>

  <div class="quote-block">
    <div class="quote-text">"We want to buy a great business at a good price — not a bad business at what seemingly is a great price."</div>
    <div class="quote-attr">— Prof. Peter Cowen, UCLA Anderson · Our north star across every deal we evaluate</div>
  </div>

  <div class="card-grid-3">
    <div class="card">
      <div class="card-num">01</div>
      <div class="card-title">Non-Discretionary Demand</div>
      <div class="card-body">Annual fire inspections are required by law. Commercial building owners cannot cancel. Revenue is compliance-driven, not preference-driven. Customers renew because they have to.</div>
      <span class="card-source">NFPA building code compliance</span>
    </div>
    <div class="card" style="--teal:#854F0B">
      <div class="card-num" style="color:#854F0B">02</div>
      <div class="card-title">Fragmented and Ageing Owner Pool</div>
      <div class="card-body">19,845 US operators. Most under $2M revenue. Baby boomer founders hitting retirement age with no succession plan and no exit. The supply of motivated sellers is structural, not cyclical.</div>
      <span class="card-source">IBIS World 2025 · Primary research</span>
    </div>
    <div class="card" style="--teal:#2E5B8A">
      <div class="card-num" style="color:#2E5B8A">03</div>
      <div class="card-title">Multiple Arbitrage — The Return</div>
      <div class="card-body">Small operators sell at 4–6x EBITDA. Regional platforms with demonstrated recurring revenue exit to national buyers at 8–12x. The gap between those two numbers is the entire business.</div>
      <span class="card-source">Essential.com 2026 · Lincoln International 2025</span>
    </div>
  </div>

  <div class="process-row" style="margin-top:48px; background:#fff; border-radius:8px; border:1px solid #E2E8F0;">
    <div class="process-step">
      <div class="process-num">1</div>
      <div class="process-title">Acquire</div>
      <div class="process-body">SoCal operator, 50%+ recurring revenue, 4–6x EBITDA entry, motivated retiring seller</div>
    </div>
    <div class="process-step">
      <div class="process-num">2</div>
      <div class="process-title">Stabilise</div>
      <div class="process-body">90-day transition, retain all customers and technicians, no changes the customer sees</div>
    </div>
    <div class="process-step">
      <div class="process-num">3</div>
      <div class="process-title">Build</div>
      <div class="process-body">Deficiency programme, service contract conversion, tuck-in route density, monitoring contracts</div>
    </div>
    <div class="process-step">
      <div class="process-num">4</div>
      <div class="process-title">Exit</div>
      <div class="process-body">5-year hold, 70%+ recurring, professional management, national consolidator buyer at 8–12x</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── OPPORTUNITY ────────────────────────────────────────────────────────
st.markdown('<div id="opportunity"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-dark">
  <div class="section-tag" style="color:#0F6E56">The Opportunity</div>
  <div class="section-title-light">Why Fire & Life Safety.<br>Why SoCal. Why Now.</div>
  <div class="section-sub-light">The window for entry at reasonable multiples is open. It will not stay open. National platforms are already paying 8–12x for exactly the asset we are building.</div>

  <div class="stat-row">
    <div class="stat-cell">
      <div class="stat-big">$22.1B</div>
      <div class="stat-label">US Market Revenue</div>
      <div class="stat-source">IBIS World 2025</div>
    </div>
    <div class="stat-cell">
      <div class="stat-big">11.45%</div>
      <div class="stat-label">Projected CAGR</div>
      <div class="stat-source">Hyde Park Capital 2024–2029</div>
    </div>
    <div class="stat-cell">
      <div class="stat-big">~50</div>
      <div class="stat-label">PE Deals / Quarter</div>
      <div class="stat-source">Lincoln International 2025</div>
    </div>
    <div class="stat-cell">
      <div class="stat-big">19,845</div>
      <div class="stat-label">US Operators</div>
      <div class="stat-source">Mostly under $2M revenue</div>
    </div>
  </div>

  <div class="card-grid-2" style="margin-top:40px;">
    <div class="card-dark">
      <div class="card-title-light">🌴 Why Southern California</div>
      <div class="card-body-light">Largest commercial real estate market on the West Coast. National platforms underweight in the LA, OC, Inland Empire mid-market. AI data center construction boom creating new fire suppression demand. Wildfire adjacency and lithium battery risk expanding mandatory compliance.</div>
    </div>
    <div class="card-dark">
      <div class="card-title-light">⏱️ Why Right Now</div>
      <div class="card-body-light">Aging owner pool is peaking — baby boomers hitting retirement with no succession plan. PE consolidation wave validating the thesis — Pye-Barker alone has done ~180 acquisitions. Entry multiples still reasonable in mid-market before national platforms arrive at scale.</div>
    </div>
    <div class="card-dark">
      <div class="card-title-light">🔒 The C-16 License Moat</div>
      <div class="card-body-light">To operate a fire sprinkler business in California you need a C-16 contractor license. This takes years and demonstrated experience to obtain. A competitor cannot just show up and underbid. The license comes with the acquisition — it is a structural barrier that protects the business.</div>
    </div>
    <div class="card-dark">
      <div class="card-title-light">🚪 The Exit Is Already There</div>
      <div class="card-body-light">Pye-Barker, APi Group, CertaSite, and AI Fire (Blackstone) are all actively acquiring. They pay 8–12x EBITDA for regional platforms with strong recurring revenue. The exit buyer is not hypothetical. They are paying these prices right now.</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── PROCESS / RESEARCH ─────────────────────────────────────────────────
st.markdown('<div id="process"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-light">
  <div class="section-tag">Our Process</div>
  <div class="section-title">We Have Done the Work.<br>Here Is What We Found.</div>
  <div class="section-sub">8 primary research conversations. 8 companies evaluated. A 15-criterion acquisition scorecard built from 180 acquisitions of practitioner experience. We know what good looks like — and what bad looks like wearing good clothes.</div>

  <div class="card-grid-3">
    <div class="card">
      <div class="card-num">8</div>
      <div class="card-title">Primary Research Conversations</div>
      <div class="card-body">Jeremy Berger (Pye-Barker, 180 acquisitions) · Prof. Jim Milke (University of Maryland) · 3 Apex Capital partners · Jason Leopoldo (UCLA alum, AZ operator) · Tony at Triton Concepts (SoCal, in-person) · Macy's facility manager</div>
    </div>
    <div class="card">
      <div class="card-num">8</div>
      <div class="card-title">Companies Evaluated</div>
      <div class="card-body">Full CIM analysis on 8 targets across SoCal, New York, Colorado, and Indiana. Three distinct types of deal risk identified: accounting irregularities, contingent government contracts, and wrong business model.</div>
    </div>
    <div class="card">
      <div class="card-num">15</div>
      <div class="card-title">Point Acquisition Scorecard</div>
      <div class="card-body">Built directly from Jeremy Berger's diligence checklist across 180 acquisitions. Three sections: recurring revenue quality (40pts), operational and workforce quality (35pts), qualitative and culture signals (25pts).</div>
    </div>
  </div>

  <div style="margin-top:48px;">
    <div class="section-tag">What We Found</div>
    <h3 style="font-family:'Playfair Display',serif;font-size:24px;color:#1F2D3D;margin-bottom:24px;">Three Types of Risk — Each Requires a Different Lens</h3>
    <table class="data-table">
      <thead>
        <tr>
          <th>Company</th>
          <th>Location</th>
          <th>Revenue</th>
          <th>Recurring</th>
          <th>Risk Found</th>
          <th>Verdict</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Superior Fire Sherpas</strong></td>
          <td>SoCal</td>
          <td>$2.66M</td>
          <td>N/A</td>
          <td>LBO loan reclassified as add-back — true multiple 9.9x not 4.7x</td>
          <td><span class="badge badge-red">WALK AWAY</span></td>
        </tr>
        <tr>
          <td><strong>Spectrum Systems</strong></td>
          <td>La Mirada, SoCal</td>
          <td>$1.8M</td>
          <td>TBD</td>
          <td>Customer concentration, unaudited 2025, A/R quality</td>
          <td><span class="badge badge-amber">CONDITIONAL</span></td>
        </tr>
        <tr>
          <td><strong>Oprandy's Fire & Safety</strong></td>
          <td>New York</td>
          <td>$969K</td>
          <td>95%</td>
          <td>2023 revenue decline unexplained — LOI condition</td>
          <td><span class="badge badge-amber">CONDITIONAL</span></td>
        </tr>
        <tr>
          <td><strong>Kubed Fire Suppression</strong></td>
          <td>Colorado</td>
          <td>$3.48M</td>
          <td>20%</td>
          <td>Wrong mix today — 80% installation work</td>
          <td><span class="badge badge-blue">MONITOR</span></td>
        </tr>
        <tr>
          <td><strong>Mid-America Fire & Safety</strong></td>
          <td>Indiana</td>
          <td>$2.9M</td>
          <td>~0%</td>
          <td>Distributor not service operator — wrong model</td>
          <td><span class="badge badge-red">PASS</span></td>
        </tr>
        <tr>
          <td><strong>Govt Contract Operator</strong></td>
          <td>SoCal</td>
          <td>TBD</td>
          <td>TBD</td>
          <td>Veteran status — contracts may not transfer on sale</td>
          <td><span class="badge badge-red">PASS</span></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
""", unsafe_allow_html=True)

# ── TEAM ───────────────────────────────────────────────────────────────
st.markdown('<div id="team"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-mid">
  <div class="section-tag" style="color:#0F6E56">The Team</div>
  <div class="section-title-light">People With Skin in the Game.<br>Advisors Who Have Done It.</div>
  <div class="section-sub-light">Each founding partner commits ~$200,000 of personal equity. We are not studying this — we are buying it. Our money goes in first.</div>

  <div class="team-grid">
    <div class="team-card">
      <div class="team-avatar">PG</div>
      <div class="team-name">Praveen Gangaraju</div>
      <div class="team-role">Operating Partner</div>
      <div class="team-bio">15+ years in FLSS. Grew a fire safety business $1M→$9M by shifting from project to recurring service revenue. This is the playbook.</div>
    </div>
    <div class="team-card">
      <div class="team-avatar">NG</div>
      <div class="team-name">Nieman Gougerchian</div>
      <div class="team-role">Deal Flow & Capital</div>
      <div class="team-bio">Led NDA pipeline and broker outreach. 8 CIMs secured. Coordinating SBA lender pre-qualification and capital structure.</div>
    </div>
    <div class="team-card">
      <div class="team-avatar">SA</div>
      <div class="team-name">Sekhar Attaluri</div>
      <div class="team-role">Relationships</div>
      <div class="team-bio">Sourced Jeremy Berger (Pye-Barker, 180 acquisitions). Led primary research programme. SoCal operator introduction pipeline.</div>
    </div>
    <div class="team-card">
      <div class="team-avatar">AA</div>
      <div class="team-name">Anthony Alonzo</div>
      <div class="team-role">Market Intelligence</div>
      <div class="team-bio">Market sizing, competitor mapping, SoCal target shortlist. Industry benchmark research and secondary data.</div>
    </div>
    <div class="team-card">
      <div class="team-avatar">MD</div>
      <div class="team-name">Mark Dixon</div>
      <div class="team-role">Network & Operations</div>
      <div class="team-bio">Operator network outreach. Flagged Superior Fire accounting irregularities. Building automation adjacency research.</div>
    </div>
  </div>

  <div style="margin-top:48px;">
    <div class="section-tag" style="color:#0F6E56">Mentor Network</div>
    <h3 style="font-family:'Playfair Display',serif;font-size:28px;color:#fff;margin-bottom:8px;">People Who Built and Sold Businesses in This Space</h3>
    <p style="color:rgba(202,220,252,0.6);margin-bottom:0;font-size:15px;">They advise and partner with us when needed — not just as references but as active guides.</p>
    <div class="mentor-grid">
      <div class="mentor-card">
        <div class="mentor-name">Jeremy Berger</div>
        <div class="mentor-title">President, Pye-Barker Fire & Safety | Founded Next Protection (~$5.8M, sold)</div>
        <div class="mentor-body">Provided 15-item acquisition checklist — foundation of our scorecard. 180 acquisitions of direct experience. Agreed to mentor and make SoCal operator introductions. Deals come from relationships he says — not cold calls.</div>
      </div>
      <div class="mentor-card">
        <div class="mentor-name">Prof. Jim Milke</div>
        <div class="mentor-title">Fire Protection Engineering, University of Maryland</div>
        <div class="mentor-body">Leading academic authority in FLSS. Validated industry structure, facility manager as customer lens, and confirmed no regulatory barrier to vertical integration. Offered contractor and facility manager introductions.</div>
      </div>
      <div class="mentor-card">
        <div class="mentor-name">Tony — Triton Concepts</div>
        <div class="mentor-title">Founder, Building Automation, Southern California</div>
        <div class="mentor-body">In-person site visit. Current at 30% recurring, wants 65%. Confirmed the gap is management attention not market demand. Same customer base as FLSS — building automation and fire systems are converging on the same buyer.</div>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── INVEST ─────────────────────────────────────────────────────────────
st.markdown('<div id="invest"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-teal">
  <div class="section-tag" style="color:rgba(255,255,255,0.7)">For Investors</div>
  <div class="section-title-light">We Are Raising $1,000,000</div>
  <div class="section-sub-light">Co-investor equity alongside SBA debt to acquire a 20-year-old Southern California fire and life safety business. You invest alongside five partners who each commit $200K of personal capital.</div>

  <div class="returns-grid">
    <div class="returns-box">
      <div class="returns-box-title">Deal Structure</div>
      <div class="returns-row"><span class="returns-key">Total acquisition price</span><span class="returns-val">~$2.3M</span></div>
      <div class="returns-row"><span class="returns-key">SBA 7(a) loan</span><span class="returns-val">~$1.4M @ ~7.5%</span></div>
      <div class="returns-row"><span class="returns-key">Co-investor equity</span><span class="returns-val-highlight">$1,000,000</span></div>
      <div class="returns-row"><span class="returns-key">Founder equity</span><span class="returns-val">~$1.0M (5 × $200K)</span></div>
      <div class="returns-row"><span class="returns-key">Investor structure</span><span class="returns-val">Preferred equity</span></div>
      <div class="returns-row"><span class="returns-key">Hold period</span><span class="returns-val">5 years</span></div>
      <div class="returns-row"><span class="returns-key">Target exit</span><span class="returns-val">National consolidator</span></div>
    </div>
    <div class="returns-box">
      <div class="returns-box-title">What You Get Back</div>
      <div class="returns-row"><span class="returns-key">Your investment</span><span class="returns-val">$1,000,000</span></div>
      <div class="returns-row"><span class="returns-key">Base case return</span><span class="returns-val-highlight">~$2.3M over 5 years</span></div>
      <div class="returns-row"><span class="returns-key">MOIC</span><span class="returns-val-highlight">~2.3x</span></div>
      <div class="returns-row"><span class="returns-key">IRR</span><span class="returns-val-highlight">~18%</span></div>
      <div class="returns-row"><span class="returns-key">Downside (6x exit)</span><span class="returns-val">~1.8x MOIC | ~14% IRR</span></div>
      <div class="returns-row"><span class="returns-key">Upside (9x exit)</span><span class="returns-val">~3.1x MOIC | ~25% IRR</span></div>
      <div class="returns-row"><span class="returns-key">How you get paid</span><span class="returns-val">Preferred — before founders</span></div>
    </div>
  </div>

  <div style="background:rgba(0,0,0,0.15);border-radius:8px;padding:24px 32px;margin-top:32px;text-align:center;">
    <p style="color:rgba(255,255,255,0.9);font-size:16px;margin:0;font-style:italic;">
      "We are not asking you to believe in an idea. We are asking you to co-invest in a specific deal we have analysed, valued, and are personally committed to."
    </p>
  </div>
</div>
""", unsafe_allow_html=True)

# ── CONTACT / QR ───────────────────────────────────────────────────────
st.markdown("""
<div class="section-dark" style="text-align:center;">
  <div class="section-tag" style="color:#0F6E56;text-align:center;">Get In Touch</div>
  <div class="section-title-light" style="text-align:center;">Ready to Talk?</div>
  <p style="color:rgba(202,220,252,0.7);font-size:16px;max-width:500px;margin:0 auto 40px;line-height:1.7;">
    Whether you are interested in co-investing, know a SoCal FLSS operator looking to exit, or want to learn more about the thesis — we want to hear from you.
  </p>
</div>
""", unsafe_allow_html=True)

# QR code section
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
    <div style="background:rgba(255,255,255,0.05);border-radius:12px;padding:40px;text-align:center;border:1px solid rgba(255,255,255,0.1);">
      <p style="color:rgba(202,220,252,0.7);font-size:14px;margin-bottom:20px;letter-spacing:1px;text-transform:uppercase;font-weight:600;">Scan to connect with Grand Ventures</p>
    </div>
    """, unsafe_allow_html=True)

    qr_url = "https://grand-ventures.streamlit.app"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=2,
    )
    qr.add_data(qr_url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="#1F2D3D", back_color="white")
    buf = BytesIO()
    qr_img.save(buf, format="PNG")
    buf.seek(0)
    st.image(buf, width=220, caption="grand-ventures.streamlit.app")
    st.markdown("""
    <div style="text-align:center;margin-top:16px;">
      <p style="color:rgba(202,220,252,0.5);font-size:12px;">UCLA Anderson EMBA 2026 · Grand Ventures</p>
      <p style="color:rgba(202,220,252,0.5);font-size:12px;">Praveen Gangaraju · Nieman Gougerchian · Sekhar Attaluri · Anthony Alonzo · Mark Dixon</p>
    </div>
    """, unsafe_allow_html=True)

# ── FOOTER ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
  <div class="footer-copy">© 2026 Grand Ventures. All rights reserved. Confidential — for qualified investors only.</div>
  <div class="footer-right">UCLA Anderson EMBA 2026 · MGMT 428B</div>
</div>
""", unsafe_allow_html=True)
