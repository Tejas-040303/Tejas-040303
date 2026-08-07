#!/usr/bin/env python3
"""Generate the glassmorphism SVG cards used by README.md.

Why files instead of inline SVG: GitHub's markdown sanitizer strips <svg> and
every child element, so inline SVG in a README renders as nothing. SVG served
as an image (<img src="assets/....svg">) is proxied by camo and renders fine,
including declarative animation and embedded CSS.

Each card is a single file that themes itself via `prefers-color-scheme`, so
one asset covers both GitHub light and dark. Backgrounds stay transparent so
the cards sit on whatever canvas the viewer's theme provides.

Usage:  python3 scripts/generate_glass_assets.py
"""

from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets"
W = 900
FONT = "'Segoe UI',Ubuntu,'Helvetica Neue',Helvetica,Arial,sans-serif"

# --------------------------------------------------------------------------
# Shared stylesheet. Light is the default; dark overrides via media query.
# CSS custom properties are used through classes because SVG presentation
# attributes (fill="...") cannot resolve var().
# --------------------------------------------------------------------------
STYLE = """
  <style>
    :root {
      --panel:      rgba(255,255,255,0.58);
      --panel-2:    rgba(255,255,255,0.34);
      --edge:       rgba(255,255,255,0.95);
      --edge-soft:  rgba(15,23,42,0.10);
      --scrim:      rgba(13,17,23,0);
      --txt:        #0f172a;
      --muted:      #475569;
      --faint:      #64748b;
      --cyan:       #0e7490;
      --violet:     #6d28d9;
      --blue:       #1d4ed8;
      --chip:       rgba(255,255,255,0.55);
      --chip-edge:  rgba(15,23,42,0.12);
      --rule:       rgba(15,23,42,0.10);
      --orb-a:      #22d3ee;
      --orb-b:      #a78bfa;
      --orb-c:      #60a5fa;
      --orb-op:     0.55;
      --grain:      0.05;
    }
    @media (prefers-color-scheme: dark) {
      :root {
        --panel:      rgba(255,255,255,0.07);
        --panel-2:    rgba(255,255,255,0.03);
        --edge:       rgba(255,255,255,0.18);
        --edge-soft:  rgba(255,255,255,0.06);
        --scrim:      rgba(9,13,21,0.46);
        --txt:        #e8eefc;
        --muted:      #b3c2da;
        --faint:      #91a4c2;
        --cyan:       #7ee8fa;
        --violet:     #b490ff;
        --blue:       #60a5fa;
        --chip:       rgba(255,255,255,0.05);
        --chip-edge:  rgba(255,255,255,0.13);
        --rule:       rgba(255,255,255,0.08);
        --orb-a:      #22d3ee;
        --orb-b:      #a78bfa;
        --orb-c:      #3b82f6;
        --orb-op:     0.40;
        --grain:      0.07;
      }
    }
    .scrim   { fill: var(--scrim); }
    .panel   { fill: var(--panel);   stroke: var(--edge-soft); stroke-width: 1; }
    .sheen   { fill: var(--panel-2); }
    .rim     { fill: none; stroke: var(--edge); stroke-width: 1.1; }
    .rule    { stroke: var(--rule);  stroke-width: 1; }
    .chip    { fill: var(--chip);    stroke: var(--chip-edge); stroke-width: 1; }
    .orb     { opacity: var(--orb-op); }
    .oa      { fill: var(--orb-a); }
    .ob      { fill: var(--orb-b); }
    .oc      { fill: var(--orb-c); }
    .grain   { opacity: var(--grain); }
    text     { font-family: %s; }
    .h1      { fill: var(--txt);    font-size: 46px; font-weight: 700; letter-spacing: -0.5px; }
    .h2      { fill: var(--txt);    font-size: 19px; font-weight: 650; }
    .title   { fill: var(--cyan);   font-size: 16px; font-weight: 650; letter-spacing: 1.6px; }
    .lead    { fill: var(--violet); font-size: 15px; font-style: italic; }
    .body    { fill: var(--muted);  font-size: 13.5px; }
    .strong  { fill: var(--txt);    font-size: 13.5px; font-weight: 600; }
    .meta    { fill: var(--cyan);   font-size: 13px; }
    .small   { fill: var(--faint);  font-size: 11.5px; }
    .tag     { fill: var(--muted);  font-size: 11.5px; }
    .accent  { fill: var(--cyan); }
    .kicker  { fill: var(--faint);  font-size: 12px; letter-spacing: 2.6px; }
  </style>
""" % FONT


def defs(px, py, pw, ph, r):
    """Filters, sheen gradient, and a clip matching the panel's rounded rect.

    The orbs are clipped to the panel itself rather than to the SVG viewport, so
    no colour spills past the glass and gets hard-cut at the image bounds. That
    cut is very visible on GitHub's light theme.
    """
    return f"""
  <defs>
    <filter id="blur" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="30"/>
    </filter>
    <filter id="shadow" x="-25%" y="-45%" width="150%" height="200%">
      <feDropShadow dx="0" dy="6" stdDeviation="10" flood-color="#0b1020" flood-opacity="0.18"/>
    </filter>
    <filter id="noise" x="0%" y="0%" width="100%" height="100%">
      <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="3" stitchTiles="stitch"/>
      <feColorMatrix type="saturate" values="0"/>
    </filter>
    <linearGradient id="sheenGrad" x1="0" y1="0" x2="0.35" y2="1">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.32"/>
      <stop offset="55%" stop-color="#ffffff" stop-opacity="0.02"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>
    </linearGradient>
    <clipPath id="pane">
      <rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="{r}"/>
    </clipPath>
  </defs>
"""


def orbs(px, py, pw, ph, seed=0):
    """Slow-drifting blurred orbs, confined to the glass. SMIL animates fine
    inside an <img>-loaded SVG (scripts do not run, declarative animation does)."""
    rad = max(ph * 0.62, 58)
    a = [
        (px + 0.14 * pw, py + 0.34 * ph, rad * 1.15, "oa", 0),
        (px + 0.86 * pw, py + 0.66 * ph, rad * 1.05, "ob", -4),
        (px + 0.50 * pw, py + 0.10 * ph, rad * 0.80, "oc", -8),
    ]
    out = ['<g class="orb" filter="url(#blur)" clip-path="url(#pane)">']
    for i, (cx, cy, r, cls, delay) in enumerate(a):
        dur = 16 + i * 5 + seed
        dx = 30 if i % 2 == 0 else -26
        dy = -16 if i % 2 == 0 else 18
        out.append(
            f'<circle class="{cls}" cx="{cx:.0f}" cy="{cy:.0f}" r="{r:.0f}">'
            f'<animateTransform attributeName="transform" type="translate" '
            f'values="0 0; {dx} {dy}; 0 0" dur="{dur}s" begin="{delay}s" '
            f'repeatCount="indefinite" calcMode="spline" '
            f'keyTimes="0;0.5;1" keySplines="0.4 0 0.2 1;0.4 0 0.2 1"/></circle>'
        )
    out.append("</g>")
    return "\n    ".join(out)


def glass(px, py, pw, ph, r):
    """Frosted pane laid over the orbs: scrim, translucent fill, sheen, grain, rim.

    The scrim is fully transparent in light mode and a soft dark wash in dark
    mode — it holds the orbs back just enough to keep muted text legible without
    draining the colour out of the glass.
    """
    return f"""
    <rect class="scrim" x="{px}" y="{py}" width="{pw}" height="{ph}" rx="{r}"/>
    <rect class="panel" x="{px}" y="{py}" width="{pw}" height="{ph}" rx="{r}"/>
    <rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="{r}" fill="url(#sheenGrad)"/>
    <rect class="grain" x="{px}" y="{py}" width="{pw}" height="{ph}" rx="{r}" filter="url(#noise)"/>
    <rect class="rim" x="{px}" y="{py}" width="{pw}" height="{ph}" rx="{r}"/>
"""


def card(h, body, seed=0, w=W, pad=18, top=12, r=24, bottom=None):
    """Assemble one card: shadow -> orbs -> frosted glass -> content."""
    px, py = pad, top
    pw = w - pad * 2
    ph = h - top - (top if bottom is None else bottom)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
        f'viewBox="0 0 {w} {h}" fill="none" role="img">'
        + STYLE
        + defs(px, py, pw, ph, r)
        + f'  <g filter="url(#shadow)"><rect x="{px}" y="{py}" width="{pw}" '
          f'height="{ph}" rx="{r}" fill="#94a3b8" fill-opacity="0.28"/></g>\n  '
        + orbs(px, py, pw, ph, seed)
        + glass(px, py, pw, ph, r)
        + body
        + "\n</svg>\n"
    )


def t(x, y, s, cls="body", anchor=None, extra=""):
    a = f' text-anchor="{anchor}"' if anchor else ""
    return f'  <text class="{cls}" x="{x}" y="{y}"{a}{extra}>{escape(s)}</text>\n'


# --------------------------------------------------------------------------
# Cards
# --------------------------------------------------------------------------

def head(label, y=54):
    """Card title + hairline rule."""
    return t(46, y, label, "title") + f'  <line class="rule" x1="46" y1="{y+16}" x2="{W-46}" y2="{y+16}"/>\n'


def rows(items, y0, gap, key_w):
    """▸ Key    Value  — the repeated list pattern."""
    b, y = "", y0
    for k, v in items:
        b += t(46, y, "▸", "meta")
        b += t(66, y, k, "strong")
        b += t(66 + key_w, y, v, "body")
        y += gap
    return b


def hero():
    h = 244
    b = t(W / 2, 96, "Tejas Pawar", "h1", "middle")
    b += (
        f'  <line x1="{W/2-96:.0f}" y1="118" x2="{W/2+96:.0f}" y2="118" '
        f'style="stroke:var(--cyan);opacity:.55" stroke-width="2" stroke-linecap="round"/>\n'
    )
    b += t(W / 2, 150, "FULL-STACK DEVELOPER  ·  IAM PROFESSIONAL", "title", "middle")
    b += t(W / 2, 180, "Building products by day, securing the identities behind them.", "body", "middle")
    b += (
        '  <circle cx="386" cy="204" r="4" style="fill:var(--cyan)">'
        '<animate attributeName="opacity" values="1;0.25;1" dur="2.4s" repeatCount="indefinite"/>'
        "</circle>\n"
    )
    b += t(400, 209, "Pune, India  ·  Open to collaboration", "small")
    return card(h, b, seed=0, top=14, r=26)


def section(label, filename):
    """Slim glass title strip used above badge and stat rows."""
    h = 60
    b = t(W / 2, 36, label, "title", "middle")
    write(filename, card(h, b, seed=3, top=7, r=16))


def about():
    h = 306
    b = head("ABOUT")
    b += t(46, 102, "“I build full-stack apps — and secure the identities behind them.”", "lead")
    b += rows(
        [
            ("Today", "IAM professional — SailPoint IdentityIQ, identity governance, access certifications"),
            ("Learning", "Enterprise IAM architecture and IdentityIQ internals"),
            ("Building", "MERN side projects, iterated on daily"),
            ("Practicing", "Daily DSA in Java and Python"),
            ("Studied", "BE Computer Science — DYPCOE Akurdi, Pune"),
        ],
        y0=142, gap=29, key_w=86,
    )
    return card(h, b, seed=1)


def experience():
    h = 330
    b = head("EXPERIENCE")
    b += t(46, 104, "Junior SailPoint Developer", "h2")
    b += t(46, 128, "_VOIS  ·  Pune, India  ·  Oct 2025 – Present", "meta")
    y = 162
    for line in (
        "Hands-on with SailPoint IdentityIQ on the RIO team — access governance and certifications",
        "Enterprise-scale IAM policy design, deployment and workflow maintenance",
        "Cross-functional collaboration on secure identity lifecycle management",
    ):
        b += t(46, y, "▸", "meta") + t(66, y, line, "body")
        y += 25
    # ---- timeline rail ----
    ty = 274
    b += f'  <line class="rule" x1="46" y1="{ty-38}" x2="{W-46}" y2="{ty-38}"/>\n'
    stops = [("Jul 2025", "Offer"), ("Oct 2025", "Joined _VOIS"), ("Now", "SailPoint · RIO")]
    x0, x1 = 108, W - 108
    b += (
        f'  <line x1="{x0}" y1="{ty}" x2="{x1}" y2="{ty}" '
        f'style="stroke:var(--cyan);opacity:.30" stroke-width="2" stroke-linecap="round"/>\n'
    )
    for i, (when, what) in enumerate(stops):
        cx = x0 + (x1 - x0) * i / (len(stops) - 1)
        last = i == len(stops) - 1
        tone = "cyan" if last else "violet"
        b += (
            f'  <circle cx="{cx:.0f}" cy="{ty}" r="{6 if last else 5}" '
            f'style="fill:var(--{tone})" opacity="{1 if last else .75}"/>\n'
        )
        if last:
            b += (
                f'  <circle cx="{cx:.0f}" cy="{ty}" r="6" style="fill:none;stroke:var(--cyan)" stroke-width="1.5">'
                f'<animate attributeName="r" values="6;13;6" dur="2.6s" repeatCount="indefinite"/>'
                f'<animate attributeName="opacity" values="0.8;0;0.8" dur="2.6s" repeatCount="indefinite"/>'
                "</circle>\n"
            )
        b += t(cx, ty - 16, when, "strong", "middle")
        b += t(cx, ty + 26, what, "small", "middle")
    return card(h, b, seed=2)


def certifications():
    h = 196
    b = head("CERTIFICATIONS")
    x = 46
    for label, tone in (("SailPoint — General", "cyan"), ("Generative AI", "violet")):
        w = 14 + len(label) * 7.6
        b += (
            f'  <rect x="{x:.0f}" y="94" width="{w:.0f}" height="34" rx="10" '
            f'style="fill:var(--{tone});opacity:.12"/>\n'
            f'  <rect x="{x:.0f}" y="94" width="{w:.0f}" height="34" rx="10" '
            f'style="fill:none;stroke:var(--{tone});opacity:.35" stroke-width="1"/>\n'
        )
        b += t(x + w / 2, 116, label, "tag", "middle",
               extra=f' style="fill:var(--{tone});font-size:12.5px"')
        x += w + 14
    b += t(46, 160, "Foundational", "small")
    x = 136
    for label in ("Python", "MERN Stack", "DSA"):
        w = 14 + len(label) * 7.0
        b += f'  <rect class="chip" x="{x:.0f}" y="146" width="{w:.0f}" height="22" rx="7"/>\n'
        b += t(x + w / 2, 161, label, "tag", "middle")
        x += w + 10
    return card(h, b, seed=4)


def exploring():
    h = 212
    b = head("CURRENTLY EXPLORING")
    b += rows(
        [
            ("Deep-diving", "SailPoint IdentityIQ internals — workflows, rules, connectors"),
            ("Studying", "Enterprise IAM architecture and access-governance patterns"),
            ("Shipping", "MERN side projects, plus daily DSA in Java and Python"),
        ],
        y0=108, gap=32, key_w=94,
    )
    return card(h, b, seed=5)


def timeline(points):
    """Build a valid SMIL (keyTimes, values) pair from (fraction, value) points.

    keyTimes must be strictly increasing, start at 0 and end at 1. A duplicate
    key — easy to produce when a phase lands exactly on a cycle boundary —
    silently invalidates the whole animation, so collapse them here.
    """
    eps = 1e-4
    out = []
    for frac, val in points:
        frac = min(max(float(frac), 0.0), 1.0)
        if out and frac <= out[-1][0]:
            frac = out[-1][0] + eps
            if frac > 1.0:                     # no room left: replace instead
                out[-1] = (out[-1][0], val)
                continue
        out.append((frac, val))
    if out[0][0] > 0:
        out.insert(0, (0.0, out[0][1]))
    if out[-1][0] < 1.0:
        out.append((1.0, out[-1][1]))
    else:
        out[-1] = (1.0, out[-1][1])
    return (";".join(f"{f:.5f}" for f, _ in out),
            ";".join(f"{v}" for _, v in out))


def typing():
    """Terminal-style typewriter strip, animated with SMIL so it works as an <img>.

    One shared caret walks the whole cycle rather than one caret per line, which
    keeps a single blinking cursor on screen at any moment.
    """
    lines = [
        "MERN Stack Developer",
        "SailPoint IdentityIQ Professional",
        "Building secure & scalable products",
    ]
    h, fs = 60, 15.0
    cw = fs * 0.60                      # monospace advance width
    per = 4.0                           # seconds per line
    total = per * len(lines)
    longest = max(len(s) for s in lines) * cw
    tx = (W - longest) / 2 + 18         # leave room for the prompt
    mono = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"

    b = t(tx - 26, 36, "❯", "meta", extra=f' style="font-family:{mono};font-size:{fs}px"')

    defs_extra, texts = [], ""
    caret_pts = [(0.0, f"{tx:.1f}")]

    for i, line in enumerate(lines):
        w = len(line) * cw
        base = i * per / total
        t_end = base + 1.6 / total      # finished typing
        h_end = base + 3.4 / total      # end of hold
        w_end = base + per / total      # window end (erased)

        ks, vs = timeline([
            (0.0, 0), (base, 0), (t_end, f"{w:.1f}"),
            (h_end, f"{w:.1f}"), (w_end, 0), (1.0, 0),
        ])
        defs_extra.append(
            f'    <clipPath id="clip{i}">\n'
            f'      <rect x="{tx:.1f}" y="18" height="26" width="0">\n'
            f'        <animate attributeName="width" dur="{total}s" repeatCount="indefinite"\n'
            f'          keyTimes="{ks}" values="{vs}"/>\n'
            f'      </rect>\n'
            f'    </clipPath>\n'
        )
        texts += (
            f'  <g clip-path="url(#clip{i})">\n'
            f'    <text class="meta" x="{tx:.1f}" y="36" '
            f'style="font-family:{mono};font-size:{fs}px">{escape(line)}</text>\n'
            f'  </g>\n'
        )
        caret_pts += [
            (base, f"{tx:.1f}"), (t_end, f"{tx + w:.1f}"),
            (h_end, f"{tx + w:.1f}"), (w_end, f"{tx:.1f}"),
        ]

    caret_pts.append((1.0, f"{tx:.1f}"))
    cks, cvs = timeline(caret_pts)
    b += texts
    b += (
        f'  <rect y="22" width="2.5" height="19" rx="1" style="fill:var(--cyan)" x="{tx:.1f}">\n'
        f'    <animate attributeName="x" dur="{total}s" repeatCount="indefinite"\n'
        f'      keyTimes="{cks}" values="{cvs}"/>\n'
        f'    <animate attributeName="opacity" values="1;1;0;0;1" dur="1s" repeatCount="indefinite"/>\n'
        f'  </rect>\n'
    )

    out = card(h, b, seed=7, top=7, r=16)
    return out.replace("  </defs>", "".join(defs_extra) + "  </defs>")


def footer():
    h = 98
    b = t(W / 2, 44, "Always happy to talk web dev, IAM, or a project idea.", "body", "middle")
    b += t(W / 2, 68, "Let’s build something.", "meta", "middle")
    return card(h, b, seed=6, top=12, r=18)


def write(name, content):
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text(content, encoding="utf-8")
    print(f"  assets/{name}  ({len(content):,} bytes)")


def main():
    print("Generating glassmorphism cards ->", OUT)
    write("hero.svg", hero())
    write("typing.svg", typing())
    write("about.svg", about())
    write("experience.svg", experience())
    write("certifications.svg", certifications())
    write("exploring.svg", exploring())
    write("footer.svg", footer())
    section("🛠  TECH STACK", "section-stack.svg")
    section("📌  FEATURED PROJECTS", "section-projects.svg")
    section("📊  GITHUB ANALYTICS", "section-analytics.svg")
    section("🐍  CONTRIBUTION SNAKE", "section-snake.svg")
    section("🧊  3D CONTRIBUTION GRAPH", "section-3d.svg")
    section("🤝  CONNECT WITH ME", "section-connect.svg")
    print("Done.")


if __name__ == "__main__":
    main()
