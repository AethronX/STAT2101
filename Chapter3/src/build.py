import os, json, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from ch3lib import *
from ch3figs import build as build_figs
import qbank

FIGS = build_figs()
HTML_DIR = os.path.join(OUT, "html"); os.makedirs(HTML_DIR, exist_ok=True)

SERIES = [
    ("00-Exam-Brief", "Chapter 3 Exam Brief", "00 · Exam brief: what the outline tests"),
    ("01-Lesson-3-1-Central-Tendency", "Lesson 3-1 Central Tendency", "01 · Lesson 3-1: Measures of Central Tendency"),
    ("02-Lesson-3-2-Variation", "Lesson 3-2 Variation", "02 · Lesson 3-2: Measures of Variation"),
    ("03-Lesson-3-3-Position", "Lesson 3-3 Position", "03 · Lesson 3-3: Measures of Position"),
    ("04-Lesson-3-4-EDA", "Lesson 3-4 Exploratory Data Analysis", "04 · Lesson 3-4: Exploratory Data Analysis"),
    ("05-Revision-Pack", "Chapter 3 Revision Pack", "05 · Revision pack: formulas, decisions, traps, R"),
    ("06-Questions", "Chapter 3 Exam Questions", "06 · Exam-style questions (no answers)"),
    ("07-Answers", "Chapter 3 Full Answers", "07 · Full worked answers"),
]
CHIPS = [
    ["<strong>Weeks</strong> 3–4", "<strong>In-Class Quiz I</strong> week 4", "<strong>Lab Quiz I</strong> week 5", "<strong>Midterm</strong> 3/11/2026"],
    ["<strong>Week</strong> 3", "<strong>CLO</strong> 1-A · 2-A · 3-B · 3-C", "<strong>Textbook</strong> p. 178 {2, 3, 10, 17}"],
    ["<strong>Week</strong> 3", "<strong>CLO</strong> 2-A · 3-C", "<strong>Textbook</strong> p. 178 {2, 3, 10, 17}"],
    ["<strong>Week</strong> 4", "<strong>CLO</strong> 2-A · 3-C · 2-D (R)", "<strong>Before</strong> In-Class Quiz I"],
    ["<strong>Week</strong> 4", "<strong>CLO</strong> 3-B · 3-C · 3-D (R)", "<strong>Before</strong> In-Class Quiz I"],
    ["<strong>Revision</strong>", "<strong>Covers</strong> 3-1 → 3-4", "<strong>R</strong> Lab Quiz I"],
    ["<strong>68</strong> questions", "<strong>~150</strong> parts", "<strong>Exam-style</strong>"],
    ["<strong>Every</strong> step shown", "<strong>Tagged</strong> by lesson + CLO"],
]

def page(k, body):
    slug, title, _ = SERIES[k]
    chips = "".join(f'<span class="chip">{c}</span>' for c in CHIPS[k]) + f'<span class="chip"><strong>File</strong> {k + 1} / {len(SERIES)}</span>'
    series = " · ".join(f'<strong style="color:var(--accent)">{s[2]}</strong>' if i == k else s[2] for i, s in enumerate(SERIES))
    doc = f"""{head(title)}
<div class="wrap">
<header class="masthead">
  <p class="eyebrow">Sultan Qaboos University · STAT 2101 · Chapter 3: Data Description</p>
  <div class="meta-strip">{chips}</div>
</header>
{body}
<footer>
  <p><strong>Chapter 3 study set: {len(SERIES)} files.</strong> One merged source built from Dr. Amani Al-Rubkhi's Fall 2026 notes (course coordinator) and Dr. Ahmed Al-Hadhrami's Spring 2024 slides, aligned to the SQU STAT 2101 course outline (Fall 2026). Textbook: Bluman, <em>Elementary Statistics</em>, 10th ed.</p>
  <p>{series}</p>
</footer>
</div>
"""
    path = os.path.join(HTML_DIR, slug + ".html")
    open(path, "w", encoding="utf-8").write(doc)
    return dict(src=path, out=os.path.join(OUT, f"STAT2101-Ch3-{slug}.pdf"), title=title)

manifest = []
for k in range(6):
    frag = open(os.path.join(SCR, "frag", f"{k:02d}.html"), encoding="utf-8").read()
    manifest.append(page(k, markup(frag, FIGS)))

# ---------------------------------------------------------------- questions / answers
PARTS = {
    "A": ("Part A · Concept and interpretation (multiple choice)", "Each item needs a reason, not a recalled fact. Give the letter <em>and</em> one line of justification, as in a written exam.", "1"),
    "B": ("Part B · Short exam problems by lesson", "Inverse problems, corrections, comparisons and interpretation, the way quiz and midterm questions are actually built.", "2"),
    "C": ("Part C · Long structured questions", "Midterm-style, multi-part, mixing lessons. Marks shown in brackets.", "3"),
    "D": ("Part D · True / false with justification, and find the mistake", "A one-word answer earns nothing. The justification is the mark.", "4"),
    "E": ("Part E · Dr. Ahmed's review self-study exercises", "The three exercises that close Dr. Ahmed's deck, fully solved in the answers file.", "1"),
    "F": ("Part F · In-Class Quiz I simulation (20 marks · 30 minutes)", "Closed book, calculator allowed. Time yourself before opening the answers file.", "A"),
}
def tags(q):
    t = "".join(f'<span class="tag">{x}</span> ' for x in q["tags"])
    return t + f'<span class="tag" style="--sec:var(--fg-faint)">{q["clo"]}</span>'

def qa_page(k, answers):
    out = []
    if not answers:
        cover = {}
        for q in qbank.Q:
            for t in q["tags"]:
                cover[t] = cover.get(t, 0) + 1
        out.append(f"""<section style="--sec:var(--accent);--wash:var(--accent-wash)">
<div class="sec-head"><span class="sec-num">Q</span><h2>Chapter 3 exam-style questions<span class="ar">أسئلة امتحانية حقيقية: تفسير، مسائل عكسية، مقارنة، كشف أخطاء. ليست أسئلة مباشرة</span></h2></div>
<p>Built from the course outline's assessment criteria: <strong>CLO2-A</strong> (calculate central tendency, variability and position), <strong>CLO3-B, C</strong> (extract and reason from graphs and summary statistics) and <strong>CLO1-A</strong> (parameters vs statistics). Every question carries its lesson and outcome tags. If you miss a question, the lesson tag tells you which file to reopen. Answers are in a <strong>separate file</strong> (07); work closed-book first.</p>
<div class="tbl-wrap"><table><thead><tr><th>Lesson</th><th class="num">3-1</th><th class="num">3-2</th><th class="num">3-3</th><th class="num">3-4</th></tr></thead>
<tbody><tr><td>Questions touching the lesson</td>{"".join(f'<td class="num">{cover.get(x,0)}</td>' for x in ("3-1","3-2","3-3","3-4"))}</tr></tbody></table></div>
<ar t="طريقة الاستخدام">الأسئلة هنا <b>ليست مباشرة</b>، بل على نمط أسئلة الكويز والميدتيرم: قيمة مفقودة، تصحيح خطأ في التسجيل، مقارنة بين مجموعتين، قراءة مخطط صندوقي، اكتشاف خطأ طالب، وتبرير صح أو خطأ. حلّها <b>مغلق الكتاب</b>، ثم صحّح من ملف الإجابات (07). الجزء <b>F</b> محاكاة للكويز الصفي الأول: 30 دقيقة لـ 20 درجة.</ar>
</section>""")
    tone = {"A": "1", "B": "2", "C": "3", "D": "4", "E": "1", "F": "A"}
    for p in "ABCDEF":
        title, lead, _ = PARTS[p]
        sec = f'var(--ink-{tone[p]})' if tone[p] != "A" else "var(--accent)"
        wash = f'var(--ink-{tone[p]}-wash)' if tone[p] != "A" else "var(--accent-wash)"
        cards = []
        for q in [q for q in qbank.Q if q["part"] == p]:
            mk = f' <strong>[{q["marks"]} marks]</strong>' if q["marks"] else ""
            if answers:
                cards.append(f'<div class="a{" long" if q["marks"] else ""}" id="a{q["id"]}"><div class="ahead"><span class="id">{q["id"]}</span>{tags(q)}{mk}</div>{q["a"]}</div>')
            else:
                cards.append(f'<div class="q" id="q{q["id"]}"><span class="id">{q["id"]}</span><div class="bd">{tags(q)}{mk}{q["q"]}</div></div>')
        out.append(f'<section style="--sec:{sec};--wash:{wash}"><h3 class="grp">{title}</h3><p class="lead">{lead}</p>{"".join(cards)}</section>')
    if answers:
        out.insert(0, """<section style="--sec:var(--accent);--wash:var(--accent-wash)">
<div class="sec-head"><span class="sec-num">ANS</span><h2>Chapter 3 full worked answers<span class="ar">الإجابات الكاملة بالخطوات: افتحه بعد حل ملف الأسئلة</span></h2></div>
<p>Each answer shows the rule, the substitution, the number, and the interpretation sentence a marker looks for. The <span class="v">why</span> lines name the trap the question was built around. All values were computed by code from the question data, not typed by hand.</p></section>""")
    return markup("\n".join(out), FIGS)

QA_CSS = """<style>
.q{background:var(--surface);border:1px solid var(--rule);border-radius:4px;padding:10px 13px;margin:0 0 9px;display:flex;gap:11px;align-items:flex-start;break-inside:avoid}
.q .id,.a .id{font-family:var(--mono);font-size:.74rem;font-weight:600;color:#fff;background:var(--sec,var(--fg));padding:3px 7px;border-radius:3px;flex:none;min-width:2.6em;text-align:center}
.q .bd{min-width:0;flex:1}.q .bd p{margin:6px 0 0}
.tag{font-family:var(--mono);font-size:.64rem;letter-spacing:.06em;text-transform:uppercase;color:var(--sec,var(--fg));border:1px solid currentColor;border-radius:20px;padding:0 7px;display:inline-block;font-weight:600}
.opts{list-style:none;margin:6px 0 0;padding:0;display:grid;grid-template-columns:1fr 1fr;gap:3px 16px}.opts li{margin:0;font-size:.9rem}
.subs{margin:6px 0 0;padding-left:1.3em}.subs li{margin-bottom:3px}
.a{background:var(--surface);border:1px solid var(--rule);border-left:4px solid var(--sec,var(--fg));border-radius:4px;padding:10px 13px;margin:0 0 9px;break-inside:avoid}
.a .ahead{display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin-bottom:6px}
.a p{margin:0 0 6px}.a p:last-child{margin-bottom:0}
.why{font-size:.88rem;color:var(--fg-soft);border-top:1px dashed var(--rule);padding-top:6px;margin-top:6px}
.lead{color:var(--fg-soft);font-size:.92rem;margin:0 0 10px}
h3.grp{display:flex}
@media (max-width:640px){.opts{grid-template-columns:1fr}}
</style>"""
for k, ans in ((6, False), (7, True)):
    body = qa_page(k, ans)
    m = page(k, body)
    t = open(m["src"], encoding="utf-8").read().replace("</style>\n\n<div class=\"wrap\">", "</style>" + QA_CSS + "\n<div class=\"wrap\">", 1)
    if QA_CSS not in t:
        t = t.replace('<div class="wrap">', QA_CSS + '\n<div class="wrap">', 1)
    open(m["src"], "w", encoding="utf-8").write(t)
    manifest.append(m)

json.dump(manifest, open(os.path.join(SCR, "manifest.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for m in manifest:
    print(os.path.basename(m["src"]), os.path.getsize(m["src"]) // 1024, "KB")
