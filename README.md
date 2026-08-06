<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                    GLASSMORPHISM PROFILE README               -->
<!--         Frosted glass aesthetic · Cool tones · Depth layers   -->
<!-- ═══════════════════════════════════════════════════════════════ -->
<!-- ═══════ BACKDROP AMBIENT GLOW (Subtle base layer) ═══════ -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=0:0f172a,50:1e293b,100:0f172a&height=2&section=header&reversal=false" width="100%"/>
</p>
<!-- ═══════ HEADER GLASS PANEL ═══════ -->
<p align="center">
  <svg width="100%" height="220" viewBox="0 0 900 220" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <!-- Frosted glass gradient -->
      <linearGradient id="headerGlass" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="rgba(126,232,250,0.12)"/>
        <stop offset="50%" stop-color="rgba(180,144,255,0.06)"/>
        <stop offset="100%" stop-color="rgba(96,165,250,0.12)"/>
      </linearGradient>
      <!-- Glow filter for text -->
      <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="3" result="blur"/>
        <feMerge>
          <feMergeNode in="blur"/>
          <feMergeNode in="SourceGraphic"/>
        </feMerge>
      </filter>
      <!-- Soft shadow -->
      <filter id="shadow" x="-10%" y="-10%" width="120%" height="130%">
        <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="rgba(126,232,250,0.15)"/>
      </filter>
    </defs>
    <!-- Glass card background -->
    <rect x="20" y="15" width="860" height="190" rx="24" fill="url(#headerGlass)" 
          stroke="rgba(255,255,255,0.12)" stroke-width="1.5" filter="url(#shadow)"/>

    <!-- Decorative blurred orbs (glassmorphism depth) -->
    <circle cx="150" cy="80" r="60" fill="rgba(126,232,250,0.08)" filter="url(#glow)"/>
    <circle cx="750" cy="140" r="50" fill="rgba(180,144,255,0.08)" filter="url(#glow)"/>

    <!-- Name -->
    <text x="450" y="95" font-family="system-ui, -apple-system, sans-serif" font-size="52" 
          font-weight="700" fill="#e2e8f0" text-anchor="middle" filter="url(#glow)">Tejas Pawar</text>

    <!-- Tagline -->
    <text x="450" y="140" font-family="system-ui, -apple-system, sans-serif" font-size="18" 
          fill="#94a3b8" text-anchor="middle" letter-spacing="2">FULL-STACK DEVELOPER  ·  IAM PROFESSIONAL</text>

    <!-- Accent line -->
    <line x1="350" y1="165" x2="550" y2="165" stroke="rgba(126,232,250,0.4)" stroke-width="1.5" stroke-linecap="round"/>
</svg>
</p>
<!-- ═══════ TYPING ANIMATION (Glass cyan tone) ═══════ -->
<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Inter&weight=500&size=22&pause=1200&color=7EE8FA&center=true&vCenter=true&width=650&lines=MERN+Stack+Developer;SailPoint+IdentityIQ+Professional;Building+secure+%26+scalable+products" alt="Typing Animation"/>
</p>
<!-- ═══════ FLOATING BADGE PILLS ═══════ -->
<p align="center">
  <img src="https://img.shields.io/badge/👁️_Profile_Views-7ee8fa?style=flat-square&labelColor=rgba(255,255,255,0.05)&color=0f172a&logoColor=7ee8fa" />
  &nbsp;
  <img src="https://img.shields.io/badge/Open_to-Collaboration-7ee8fa?style=flat-square&labelColor=0f172a&color=0f172a&logoColor=7ee8fa" />
  &nbsp;
  <img src="https://img.shields.io/badge/📍_Pune-India-b490ff?style=flat-square&labelColor=0f172a&color=0f172a" />
</p>
<br>
<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                         ABOUT ME                              -->
<!-- ═══════════════════════════════════════════════════════════════ -->
<p align="center">
  <svg width="100%" height="70" viewBox="0 0 900 70" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <linearGradient id="sectionGlass" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="rgba(126,232,250,0.08)"/>
        <stop offset="50%" stop-color="rgba(180,144,255,0.04)"/>
        <stop offset="100%" stop-color="rgba(126,232,250,0.08)"/>
      </linearGradient>
      <filter id="sectionGlow" x="-10%" y="-10%" width="120%" height="130%">
        <feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="rgba(126,232,250,0.1)"/>
      </filter>
    </defs>
    <rect x="30" y="10" width="840" height="50" rx="16" fill="url(#sectionGlass)" 
          stroke="rgba(255,255,255,0.08)" stroke-width="1" filter="url(#sectionGlow)"/>
    <text x="450" y="43" font-family="system-ui, sans-serif" font-size="20" 
          font-weight="600" fill="#7ee8fa" text-anchor="middle" letter-spacing="1">👋 ABOUT ME</text>
  </svg>
</p>
<p align="center">
  <svg width="100%" height="280" viewBox="0 0 900 280" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <linearGradient id="cardGlass" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="rgba(255,255,255,0.05)"/>
        <stop offset="100%" stop-color="rgba(255,255,255,0.02)"/>
      </linearGradient>
      <filter id="cardShadow" x="-5%" y="-5%" width="110%" height="115%">
        <feDropShadow dx="0" dy="6" stdDeviation="10" flood-color="rgba(0,0,0,0.3)"/>
      </filter>
    </defs>
    <rect x="30" y="5" width="840" height="270" rx="20" fill="url(#cardGlass)" 
          stroke="rgba(255,255,255,0.08)" stroke-width="1" filter="url(#cardShadow)"/>
    <!-- Content as SVG text for glass aesthetic -->
    <text x="70" y="50" font-family="system-ui, sans-serif" font-size="15" fill="#e2e8f0">
      <tspan font-style="italic" fill="#b490ff">"I build full-stack apps and secure the identities behind them."</tspan>
    </text>

    <text x="70" y="90" font-family="system-ui, sans-serif" font-size="14" fill="#94a3b8">MERN developer turned IAM professional.</text>

    <text x="70" y="125" font-family="system-ui, sans-serif" font-size="13" fill="#cbd5e1">💼  Today: IAM professional — SailPoint IdentityIQ · identity governance · access certifications</text>
    <text x="70" y="155" font-family="system-ui, sans-serif" font-size="13" fill="#cbd5e1">🌱  Learning: Enterprise IAM architecture &amp; IdentityIQ deep dives</text>
    <text x="70" y="185" font-family="system-ui, sans-serif" font-size="13" fill="#cbd5e1">🛠️  Building: MERN side projects, iterated daily</text>
    <text x="70" y="215" font-family="system-ui, sans-serif" font-size="13" fill="#cbd5e1">🧠  Practicing: Daily DSA in Java &amp; Python</text>
    <text x="70" y="245" font-family="system-ui, sans-serif" font-size="13" fill="#cbd5e1">🎓  BE Computer Science — DYPCOE Akurdi, Pune</text>
</svg>
</p>
<br>
<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                         EXPERIENCE                            -->
<!-- ═══════════════════════════════════════════════════════════════ -->
<p align="center">
  <svg width="100%" height="70" viewBox="0 0 900 70" xmlns="http://www.w3.org/2000/svg">
    <rect x="30" y="10" width="840" height="50" rx="16" fill="url(#sectionGlass)" 
          stroke="rgba(255,255,255,0.08)" stroke-width="1" filter="url(#sectionGlow)"/>
    <text x="450" y="43" font-family="system-ui, sans-serif" font-size="20" 
          font-weight="600" fill="#7ee8fa" text-anchor="middle" letter-spacing="1">💼 EXPERIENCE</text>
  </svg>
</p>
<p align="center">
  <svg width="100%" height="200" viewBox="0 0 900 200" xmlns="http://www.w3.org/2000/svg">
    <rect x="30" y="5" width="840" height="190" rx="20" fill="url(#cardGlass)" 
          stroke="rgba(255,255,255,0.08)" stroke-width="1" filter="url(#cardShadow)"/>
    <!-- Role title -->
    <text x="70" y="50" font-family="system-ui, sans-serif" font-size="18" font-weight="600" fill="#e2e8f0">Junior SailPoint Developer</text>
    <text x="70" y="75" font-family="system-ui, sans-serif" font-size="14" fill="#7ee8fa">_VOIS  ·  Pune, India  ·  [MONTH_YEAR] – Present</text>

    <!-- Divider -->
    <line x1="70" y1="95" x2="830" y2="95" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>

    <!-- Bullets -->
    <text x="70" y="125" font-family="system-ui, sans-serif" font-size="13" fill="#94a3b8">▸  Hands-on with SailPoint IdentityIQ in the [RIO] team — access governance &amp; certifications</text>
    <text x="70" y="150" font-family="system-ui, sans-serif" font-size="13" fill="#94a3b8">▸  Enterprise-scale IAM policy design, deployment &amp; workflow maintenance</text>
    <text x="70" y="175" font-family="system-ui, sans-serif" font-size="13" fill="#94a3b8">▸  Cross-functional collaboration on secure identity lifecycle management</text>
</svg>
</p>
<p align="center">
  <svg width="100%" height="50" viewBox="0 0 900 50" xmlns="http://www.w3.org/2000/svg">
    <rect x="30" y="5" width="840" height="40" rx="12" fill="rgba(126,232,250,0.04)" 
          stroke="rgba(126,232,250,0.15)" stroke-width="1"/>
    <text x="450" y="30" font-family="system-ui, sans-serif" font-size="13" fill="#7ee8fa" text-anchor="middle">
      ⏱️ Total: ~1 year at _VOIS (including 4 months in SailPoint [RIO] team)
    </text>
  </svg>
</p>
<br>
<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                        TECH STACK                             -->
<!-- ═══════════════════════════════════════════════════════════════ -->
<p align="center">
  <svg width="100%" height="70" viewBox="0 0 900 70" xmlns="http://www.w3.org/2000/svg">
    <rect x="30" y="10" width="840" height="50" rx="16" fill="url(#sectionGlass)" 
          stroke="rgba(255,255,255,0.08)" stroke-width="1" filter="url(#sectionGlow)"/>
    <text x="450" y="43" font-family="system-ui, sans-serif" font-size="20" 
          font-weight="600" fill="#7ee8fa" text-anchor="middle" letter-spacing="1">🛠 TECH STACK</text>
  </svg>
</p>
<p align="center">
  <img src="https://img.shields.io/badge/JavaScript-0f172a?style=for-the-badge&logo=javascript&logoColor=7ee8fa&labelColor=rgba(255,255,255,0.05)"/>
  <img src="https://img.shields.io/badge/Java-0f172a?style=for-the-badge&logo=openjdk&logoColor=7ee8fa&labelColor=rgba(255,255,255,0.05)"/>
  <img src="https://img.shields.io/badge/Python-0f172a?style=for-the-badge&logo=python&logoColor=7ee8fa&labelColor=rgba(255,255,255,0.05)"/>
  <img src="https://img.shields.io/badge/SQL-0f172a?style=for-the-badge&logo=mysql&logoColor=7ee8fa&labelColor=rgba(255,255,255,0.05)"/>
</p>
<p align="center">
  <img src="https://img.shields.io/badge/React-0f172a?style=for-the-badge&logo=react&logoColor=b490ff&labelColor=rgba(255,255,255,0.05)"/>
  <img src="https://img.shields.io/badge/Node.js-0f172a?style=for-the-badge&logo=nodedotjs&logoColor=b490ff&labelColor=rgba(255,255,255,0.05)"/>
  <img src="https://img.shields.io/badge/Express-0f172a?style=for-the-badge&logo=express&logoColor=b490ff&labelColor=rgba(255,255,255,0.05)"/>
  <img src="https://img.shields.io/badge/MongoDB-0f172a?style=for-the-badge&logo=mongodb&logoColor=b490ff&labelColor=rgba(255,255,255,0.05)"/>
</p>
<p align="center">
  <img src="https://img.shields.io/badge/SailPoint-0f172a?style=for-the-badge&logo=sailpoint&logoColor=60a5fa&labelColor=rgba(255,255,255,0.05)"/>
  <img src="https://img.shields.io/badge/IdentityIQ-0f172a?style=for-the-badge&logo=sailpoint&logoColor=60a5fa&labelColor=rgba(255,255,255,0.05)"/>
  <img src="https://img.shields.io/badge/Git-0f172a?style=for-the-badge&logo=git&logoColor=60a5fa&labelColor=rgba(255,255,255,0.05)"/>
  <img src="https://img.shields.io/badge/VS_Code-0f172a?style=for-the-badge&logo=visual-studio-code&logoColor=60a5fa&labelColor=rgba(255,255,255,0.05)"/>
</p>
<br>
<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                      FEATURED PROJECTS                        -->
<!-- ═══════════════════════════════════════════════════════════════ -->
<p align="center">
  <svg width="100%" height="70" viewBox="0 0 900 70" xmlns="http://www.w3.org/2000/svg">
    <rect x="30" y="10" width="840" height="50" rx="16" fill="url(#sectionGlass)" 
          stroke="rgba(255,255,255,0.08)" stroke-width="1" filter="url(#sectionGlow)"/>
    <text x="450" y="43" font-family="system-ui, sans-serif" font-size="20" 
          font-weight="600" fill="#7ee8fa" text-anchor="middle" letter-spacing="1">📌 FEATURED PROJECTS</text>
  </svg>
</p>
<p align="center">
  <a href="https://github.com/Tejas-040303/REPO_NAME_1">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=Tejas-040303&repo=REPO_NAME_1&theme=transparent&hide_border=true&title_color=7ee8fa&text_color=e2e8f0&icon_color=b490ff&bg_color=0f172a" />
  </a>
  &nbsp;&nbsp;
  <a href="https://github.com/Tejas-040303/REPO_NAME_2">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=Tejas-040303&repo=REPO_NAME_2&theme=transparent&hide_border=true&title_color=7ee8fa&text_color=e2e8f0&icon_color=b490ff&bg_color=0f172a" />
  </a>
</p>
<p align="center">
  <a href="YOUR_PORTFOLIO_LINK">
    <svg width="220" height="50" viewBox="0 0 220 50" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="btnGrad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="rgba(126,232,250,0.2)"/>
          <stop offset="100%" stop-color="rgba(180,144,255,0.2)"/>
        </linearGradient>
      </defs>
      <rect x="5" y="5" width="210" height="40" rx="20" fill="url(#btnGrad)" 
            stroke="rgba(126,232,250,0.3)" stroke-width="1.5"/>
      <text x="110" y="30" font-family="system-ui, sans-serif" font-size="14" 
            font-weight="500" fill="#7ee8fa" text-anchor="middle">🌐  View Full Portfolio</text>
    </svg>
  </a>
</p>
<br>
<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                       CERTIFICATIONS                          -->
<!-- ═══════════════════════════════════════════════════════════════ -->
<p align="center">
  <svg width="100%" height="70" viewBox="0 0 900 70" xmlns="http://www.w3.org/2000/svg">
    <rect x="30" y="10" width="840" height="50" rx="16" fill="url(#sectionGlass)" 
          stroke="rgba(255,255,255,0.08)" stroke-width="1" filter="url(#sectionGlow)"/>
    <text x="450" y="43" font-family="system-ui, sans-serif" font-size="20" 
          font-weight="600" fill="#7ee8fa" text-anchor="middle" letter-spacing="1">🏆 CERTIFICATIONS</text>
  </svg>
</p>
<p align="center">
  <svg width="100%" height="130" viewBox="0 0 900 130" xmlns="http://www.w3.org/2000/svg">
    <rect x="30" y="5" width="840" height="120" rx="20" fill="url(#cardGlass)" 
          stroke="rgba(255,255,255,0.08)" stroke-width="1" filter="url(#cardShadow)"/>
    <!-- Primary certs -->
    <rect x="70" y="30" width="180" height="35" rx="10" fill="rgba(126,232,250,0.08)" stroke="rgba(126,232,250,0.2)" stroke-width="1"/>
    <text x="160" y="53" font-family="system-ui, sans-serif" font-size="13" fill="#7ee8fa" text-anchor="middle">🏅 SailPoint — General</text>

    <rect x="280" y="30" width="180" height="35" rx="10" fill="rgba(180,144,255,0.08)" stroke="rgba(180,144,255,0.2)" stroke-width="1"/>
    <text x="370" y="53" font-family="system-ui, sans-serif" font-size="13" fill="#b490ff" text-anchor="middle">🤖 Generative AI</text>

    <!-- Foundational label -->
    <text x="70" y="95" font-family="system-ui, sans-serif" font-size="12" fill="#64748b">📜 Foundational:</text>
    <rect x="180" y="78" width="80" height="22" rx="6" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
    <text x="220" y="93" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">Python</text>
    <rect x="270" y="78" width="90" height="22" rx="6" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
    <text x="315" y="93" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">MERN Stack</text>
</svg>
</p>
<br>
<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                    CURRENTLY EXPLORING                        -->
<!-- ═══════════════════════════════════════════════════════════════ -->
<p align="center">
  <svg width="100%" height="70" viewBox="0 0 900 70" xmlns="http://www.w3.org/2000/svg">
    <rect x="30" y="10" width="840" height="50" rx="16" fill="url(#sectionGlass)" 
          stroke="rgba(255,255,255,0.08)" stroke-width="1" filter="url(#sectionGlow)"/>
    <text x="450" y="43" font-family="system-ui, sans-serif" font-size="20" 
          font-weight="600" fill="#7ee8fa" text-anchor="middle" letter-spacing="1">📚 CURRENTLY EXPLORING</text>
  </svg>
</p>
<p align="center">
  <svg width="100%" height="160" viewBox="0 0 900 160" xmlns="http://www.w3.org/2000/svg">
    <rect x="30" y="5" width="840" height="150" rx="20" fill="url(#cardGlass)" 
          stroke="rgba(255,255,255,0.08)" stroke-width="1" filter="url(#cardShadow)"/>
    <text x="70" y="50" font-family="system-ui, sans-serif" font-size="14" fill="#94a3b8">📖 <tspan fill="#e2e8f0">Book:</tspan> ...........................................................................................</text>
    <text x="70" y="90" font-family="system-ui, sans-serif" font-size="14" fill="#94a3b8">💡 <tspan fill="#e2e8f0">Concept:</tspan> ......................................................................................</text>
    <text x="70" y="130" font-family="system-ui, sans-serif" font-size="14" fill="#94a3b8">🔨 <tspan fill="#e2e8f0">Side Project:</tspan> ...............................................................................</text>
</svg>
</p>
<br>
<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                      GITHUB ANALYTICS                         -->
<!-- ═══════════════════════════════════════════════════════════════ -->
<p align="center">
  <svg width="100%" height="70" viewBox="0 0 900 70" xmlns="http://www.w3.org/2000/svg">
    <rect x="30" y="10" width="840" height="50" rx="16" fill="url(#sectionGlass)" 
          stroke="rgba(255,255,255,0.08)" stroke-width="1" filter="url(#sectionGlow)"/>
    <text x="450" y="43" font-family="system-ui, sans-serif" font-size="20" 
          font-weight="600" fill="#7ee8fa" text-anchor="middle" letter-spacing="1">📊 GITHUB ANALYTICS</text>
  </svg>
</p>
<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=Tejas-040303&show_icons=true&theme=transparent&hide_border=true&title_color=7ee8fa&text_color=e2e8f0&icon_color=b490ff&bg_color=0f172a&cache_seconds=86400" alt="GitHub Stats"/>
  &nbsp;&nbsp;
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Tejas-040303&layout=compact&theme=transparent&hide_border=true&title_color=7ee8fa&text_color=e2e8f0&bg_color=0f172a&cache_seconds=86400" alt="Top Languages"/>
</p>
<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=Tejas-040303&theme=transparent&hide_border=true&stroke=7ee8fa&ring=b490ff&fire=60a5fa&currStreakNum=e2e8f0&sideNums=e2e8f0&currStreakLabel=94a3b8&sideLabels=94a3b8&dates=64748b&background=0f172a" alt="GitHub Streak"/>
</p>
<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=Tejas-040303&theme=react-dark&hide_border=true&bg_color=0f172a&color=7ee8fa&line=b490ff&point=60a5fa" alt="Contribution Graph"/>
</p>
<br>
<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                    CONTRIBUTION SNAKE                         -->
<!-- ═══════════════════════════════════════════════════════════════ -->
<p align="center">
  <svg width="100%" height="70" viewBox="0 0 900 70" xmlns="http://www.w3.org/2000/svg">
    <rect x="30" y="10" width="840" height="50" rx="16" fill="url(#sectionGlass)" 
          stroke="rgba(255,255,255,0.08)" stroke-width="1" filter="url(#sectionGlow)"/>
    <text x="450" y="43" font-family="system-ui, sans-serif" font-size="20" 
          font-weight="600" fill="#7ee8fa" text-anchor="middle" letter-spacing="1">🐍 CONTRIBUTION SNAKE</text>
  </svg>
</p>
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Tejas-040303/Tejas-040303/output/github-contribution-grid-snake-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Tejas-040303/Tejas-040303/output/github-contribution-grid-snake.svg">
    <img alt="github contribution grid snake animation" src="https://raw.githubusercontent.com/Tejas-040303/Tejas-040303/output/github-contribution-grid-snake.svg">
  </picture>
</p>
<br>
<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                        DEV QUOTE                              -->
<!-- ═══════════════════════════════════════════════════════════════ -->
<p align="center">
  <svg width="100%" height="70" viewBox="0 0 900 70" xmlns="http://www.w3.org/2000/svg">
    <rect x="30" y="10" width="840" height="50" rx="16" fill="url(#sectionGlass)" 
          stroke="rgba(255,255,255,0.08)" stroke-width="1" filter="url(#sectionGlow)"/>
    <text x="450" y="43" font-family="system-ui, sans-serif" font-size="20" 
          font-weight="600" fill="#7ee8fa" text-anchor="middle" letter-spacing="1">✍️ DEV QUOTE</text>
  </svg>
</p>
<p align="center">
  <img src="https://quotes-github-readme.vercel.app/api?type=horizontal&theme=radical" alt="Dev Quote"/>
</p>
<br>
<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                       CONNECT WITH ME                         -->
<!-- ═══════════════════════════════════════════════════════════════ -->
<p align="center">
  <svg width="100%" height="70" viewBox="0 0 900 70" xmlns="http://www.w3.org/2000/svg">
    <rect x="30" y="10" width="840" height="50" rx="16" fill="url(#sectionGlass)" 
          stroke="rgba(255,255,255,0.08)" stroke-width="1" filter="url(#sectionGlow)"/>
    <text x="450" y="43" font-family="system-ui, sans-serif" font-size="20" 
          font-weight="600" fill="#7ee8fa" text-anchor="middle" letter-spacing="1">🤝 CONNECT WITH ME</text>
  </svg>
</p>
<p align="center">
  <a href="https://linkedin.com/in/YOUR_LINKEDIN_USERNAME">
    <svg width="140" height="45" viewBox="0 0 140 45" xmlns="http://www.w3.org/2000/svg">
      <rect x="5" y="5" width="130" height="35" rx="12" fill="rgba(10,102,194,0.1)" stroke="rgba(10,102,194,0.3)" stroke-width="1"/>
      <text x="70" y="28" font-family="system-ui, sans-serif" font-size="13" fill="#60a5fa" text-anchor="middle">LinkedIn</text>
    </svg>
  </a>
  &nbsp;&nbsp;
  <a href="mailto:tej.pawar04@gmail.com">
    <svg width="140" height="45" viewBox="0 0 140 45" xmlns="http://www.w3.org/2000/svg">
      <rect x="5" y="5" width="130" height="35" rx="12" fill="rgba(234,67,53,0.1)" stroke="rgba(234,67,53,0.3)" stroke-width="1"/>
      <text x="70" y="28" font-family="system-ui, sans-serif" font-size="13" fill="#f87171" text-anchor="middle">Gmail</text>
    </svg>
  </a>
  &nbsp;&nbsp;
  <a href="YOUR_PORTFOLIO_LINK">
    <svg width="140" height="45" viewBox="0 0 140 45" xmlns="http://www.w3.org/2000/svg">
      <rect x="5" y="5" width="130" height="35" rx="12" fill="rgba(126,232,250,0.08)" stroke="rgba(126,232,250,0.25)" stroke-width="1"/>
      <text x="70" y="28" font-family="system-ui, sans-serif" font-size="13" fill="#7ee8fa" text-anchor="middle">Portfolio</text>
    </svg>
  </a>
</p>
<p align="center">
  <svg width="100%" height="60" viewBox="0 0 900 60" xmlns="http://www.w3.org/2000/svg">
    <text x="450" y="35" font-family="system-ui, sans-serif" font-size="14" fill="#64748b" text-anchor="middle" font-style="italic">
      Always happy to talk web dev, IAM, or a project idea — let's build something. 🚀
    </text>
  </svg>
</p>
<!-- ═══════ FOOTER GLASS WAVE ═══════ -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,6&height=120&section=footer&animation=twinkling&fontColor=7ee8fa"/>
</p>
