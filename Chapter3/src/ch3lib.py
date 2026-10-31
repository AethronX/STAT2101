"""Shared build library for the Chapter 3 study set: page shell, mini-markup, and to-scale SVG diagrams."""
import math, re, os

SCR = "/tmp/claude-0/-home-user-STAT2101/521e5d47-fbd3-5206-8b60-93d1c3cc1629/scratchpad/ch3"
CH4 = "/home/user/STAT2101/STAT2101-Ch4-Master-Summary.html"
OUT = "/home/user/STAT2101/Chapter3"

# ------------------------------------------------------------------ page shell (same design system as Chapter 4)
_src = open(CH4, encoding="utf-8").read()
BASE_HEAD = _src[: _src.index('<div class="wrap">')]

DENSE_CSS = """<style>
/* Chapter 3: denser setting so pages carry more per sheet */
body{font-size:14.5px;line-height:1.55}
p,ul,ol{max-width:none}
p{margin:0 0 9px}
li{margin-bottom:4px}
.masthead{padding-block:34px 18px;margin-bottom:20px}
section{margin-bottom:30px}
.sec-head{margin-bottom:16px;padding-bottom:10px}
h3{margin:22px 0 8px;font-size:1.02rem}
h4{margin:14px 0 6px}
.formula{padding:11px 14px;margin:10px 0 12px}
.formula .fx{margin:1px 0;line-height:1.9}
.ex{margin:10px 0}
.ex > .q,.ex > .a{padding:10px 14px}
.ex .steps li{margin-bottom:5px}
.callout{padding:10px 13px;margin:10px 0;font-size:.93rem}
.ar-note{padding:9px 13px;margin:9px 0;line-height:1.8;font-size:.93rem}
.tbl-wrap{margin:8px 0 12px}
th,td{padding:6px 10px}
table{font-size:.9rem;min-width:0}
figure.dg{margin:12px 0 14px;padding:10px 10px 8px}
figure.dg figcaption{margin-top:6px;font-size:.84rem}
.cols2{display:grid;grid-template-columns:1fr 1fr;gap:10px;align-items:start}
.cols2 > *{min-width:0}
.cols2 .ex{margin:0}
@media (max-width:640px){.cols2{grid-template-columns:1fr}}
/* let long formulas wrap inside narrow columns instead of being clipped */
.fx,.ex .fx,.cols2 .fx,.a .fx{white-space:normal;overflow-x:visible}
footer{margin-top:10px;padding-top:12px;font-size:.78rem}footer p{margin:0 0 4px}
/* allow tall example cards to split across pages so no half-empty pages */
@media print{.ex,.a.long{break-inside:auto!important;page-break-inside:auto!important}.a:not(.long){break-inside:avoid!important}.ex > .q{break-inside:avoid}.cols2{break-inside:auto}}
.series{list-style:none;padding:0;margin:8px 0 12px;display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:2px 22px;max-width:none}
.series li{margin:0;padding:3px 0;border-bottom:1px solid var(--rule-soft);font-size:.82rem;color:var(--fg-faint)}
.series li.here{color:var(--fg);font-weight:600}
.series li.here::after{content:"  ← this file";color:var(--accent);font-weight:500}
.src{font-family:var(--mono);font-size:.66rem;letter-spacing:.06em;text-transform:uppercase;color:var(--fg-faint);border:1px solid var(--rule);border-radius:3px;padding:0 5px;margin-left:6px;white-space:nowrap;font-weight:500}
</style>
"""

def head(title):
    return BASE_HEAD.replace("<title>Probability and Counting Rules</title>", f"<title>{title}</title>") + DENSE_CSS

# ------------------------------------------------------------------ mini-markup
_RUN = re.compile(r"[A-Za-z0-9(σμ√][A-Za-z0-9(){}|=+−×÷/!ᶜ∩∪≈.,%σμ̄√²³±·\- ]*[A-Za-z0-9(){}|!ᶜ%²³]")
def ar_iso(text):
    return _RUN.sub(lambda m: f'<span dir="ltr" style="white-space:nowrap">{m.group(0)}</span>', text)

def _frac(m):
    a, b = m.group(1).split("‖")
    return f'<span class="frac"><span class="num">{a}</span><span class="den">{b}</span></span>'

def markup(html, figs):
    def ar(m):
        label, body = m.group(1), m.group(2)
        body = re.sub(r"\{\{(.+?)\}\}", r'<span class="v" dir="ltr">\1</span>', body)
        body = re.sub(r"\[\[(.+?)\]\]", r'<b dir="ltr">\1</b>', body)
        body = re.sub(r"⟦(.+?)⟧", r'<span class="v" dir="ltr">\1</span>', body)
        return f'<div class="ar-note"><span class="lbl">{label}</span>{body}</div>'
    html = re.sub(r'<ar t="([^"]*)">(.*?)</ar>', ar, html, flags=re.S)
    html = re.sub(r"⟪(.+?)⟫", _frac, html)
    html = re.sub(r"⟦(.+?)⟧", r'<span class="v">\1</span>', html)
    html = re.sub(r"⦃(.+?)⦄", r'<span class="ans">\1</span>', html)
    html = re.sub(r"<arn>(.*?)</arn>", r'<span class="arn">\1</span>', html)
    def fg(m):
        k = m.group(1)
        if k not in figs:
            raise SystemExit("missing figure " + k)
        return figs[k]
    html = re.sub(r'<fig id="([a-z0-9_]+)"\s*/>', fg, html)
    left = re.findall(r"⟦|⟧|⦃|⦄|⟪|⟫|<ar |<fig ", html)
    if left:
        raise SystemExit("unprocessed markup: " + str(left[:5]))
    return html

# ------------------------------------------------------------------ SVG primitives
def T(x, y, txt, cls="", anchor="middle", extra=""):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" class="{cls}"{extra}>{txt}</text>'
def L(x1, y1, x2, y2, cls="ln", extra=""):
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" class="{cls}"{extra}/>'
def C(cx, cy, r, cls, extra=""):
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" class="{cls}"{extra}/>'
def R(x, y, w, h, cls, rx=0, extra=""):
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" class="{cls}"{extra}/>'
def P(pts, cls, extra=""):
    return f'<polyline points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in pts)}" class="{cls}"{extra}/>'
def PG(pts, cls, extra=""):
    return f'<polygon points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in pts)}" class="{cls}"{extra}/>'
def arrow_defs(uid):
    return (f'<marker id="{uid}-arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
            f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="currentColor"/></marker>')
def AR(x1, y1, x2, y2, uid, cls="ln"):
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" class="{cls}" marker-end="url(#{uid}-arr)"/>'

def fig(W, H, inner, aria, cap_en, cap_ar, defs=""):
    d = f"<defs>{defs}</defs>" if defs else ""
    return (f'<figure class="dg"><svg viewBox="0 0 {W} {H}" style="max-width:{W}px" role="img" aria-label="{aria}" '
            f'xmlns="http://www.w3.org/2000/svg">{d}\n{inner}\n</svg><figcaption>{cap_en}'
            f'<span class="ar">{ar_iso(cap_ar)}</span></figcaption></figure>')

def scale(v0, v1, x0, x1):
    return lambda v: x0 + (v - v0) * (x1 - x0) / (v1 - v0)

def axis(sx, v0, v1, y, ticks, fmt=lambda v: f"{v:g}", cls="m soft"):
    out = [L(sx(v0), y, sx(v1), y, "ln")]
    for t in ticks:
        out += [L(sx(t), y, sx(t), y + 5, "ln"), T(sx(t), y + 18, fmt(t), cls)]
    return out

def boxplot(sx, y, five, tone="4", h=26, labels=True, lab_cls="m b"):
    mn, q1, md, q3, mx = five
    g = [L(sx(mn), y, sx(q1), y, "ln"), L(sx(q3), y, sx(mx), y, "ln"),
         L(sx(mn), y - 8, sx(mn), y + 8, "ln"), L(sx(mx), y - 8, sx(mx), y + 8, "ln"),
         R(sx(q1), y - h / 2, sx(q3) - sx(q1), h, f"wash{tone} ln s{tone}"),
         L(sx(md), y - h / 2, sx(md), y + h / 2, f"ln s{tone} thick")]
    if labels:
        prev, lift = -99, 0
        for v in five:
            lift = 13 if (sx(v) - prev < 30 and lift == 0) else 0
            g.append(T(sx(v), y - h / 2 - 7 - lift, f"{v:g}", lab_cls))
            prev = sx(v)
    return g

def bracket(x1, x2, y, label, cls="sm b", up=True, tick=6):
    d = tick if up else -tick
    return [L(x1, y, x2, y, "ln"), L(x1, y, x1, y + d, "ln"), L(x2, y, x2, y + d, "ln"),
            T((x1 + x2) / 2, y - 6 if up else y + 16, label, cls)]
