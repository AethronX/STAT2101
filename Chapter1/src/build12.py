import os, sys, json, re
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "ch3"))
from ch3lib import head, markup
import figs12, qb12

QA_CSS = """<style>
.q{background:var(--surface);border:1px solid var(--rule);border-radius:4px;padding:10px 13px;margin:0 0 9px;display:flex;gap:11px;align-items:flex-start;break-inside:avoid}
.q .id,.a .id{font-family:var(--mono);font-size:.74rem;font-weight:600;color:#fff;background:var(--sec,var(--fg));padding:3px 7px;border-radius:3px;flex:none;min-width:2.6em;text-align:center}
.q .bd{min-width:0;flex:1}.q .bd p{margin:6px 0 0}
.tag{font-family:var(--mono);font-size:.64rem;letter-spacing:.06em;text-transform:uppercase;color:var(--sec,var(--fg));border:1px solid currentColor;border-radius:20px;padding:0 7px;display:inline-block;font-weight:600}
.opts{list-style:none;margin:6px 0 0;padding:0;display:grid;grid-template-columns:1fr 1fr;gap:3px 16px}.opts li{margin:0;font-size:.9rem}
.subs{margin:6px 0 0;padding-left:1.3em}.subs li{margin-bottom:3px}
.a{background:var(--surface);border:1px solid var(--rule);border-left:4px solid var(--sec,var(--fg));border-radius:4px;padding:10px 13px;margin:0 0 9px}
.a:not(.long){break-inside:avoid}
.a .ahead{display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin-bottom:6px}
.a p{margin:0 0 6px}.a p:last-child{margin-bottom:0}
.why{font-size:.88rem;color:var(--fg-soft);border-top:1px dashed var(--rule);padding-top:6px;margin-top:6px}
.lead{color:var(--fg-soft);font-size:.92rem;margin:0 0 10px}
@media (max-width:640px){.opts{grid-template-columns:1fr}}
</style>"""

CH = {
 1: dict(name="Chapter 1: The Nature of Probability and Statistics", figs=figs12.build1(), Q=qb12.Q1, lessons=["1-1", "1-2", "1-3"],
         series=[("00-Exam-Brief", "Chapter 1 Exam Brief", "00 · Exam brief"),
                 ("01-Lesson-1-1-Descriptive-Inferential", "Lesson 1-1 Descriptive and Inferential", "01 · Lesson 1-1: Descriptive and Inferential Statistics"),
                 ("02-Lesson-1-2-Variables-Data-Types", "Lesson 1-2 Variables and Data Types", "02 · Lesson 1-2: Variables and Types of Data"),
                 ("03-Lesson-1-3-Sampling", "Lesson 1-3 Sampling Techniques", "03 · Lesson 1-3: Data Collection and Sampling"),
                 ("04-Revision-Pack", "Chapter 1 Revision Pack", "04 · Revision pack"),
                 ("05-Questions", "Chapter 1 Exam Questions", "05 · Exam-style questions"),
                 ("06-Answers", "Chapter 1 Full Answers", "06 · Full worked answers")],
         chips=[["<strong>Week</strong> 1", "<strong>CLO</strong> 1-A · 1-B · 1-C", "<strong>Textbook</strong> p. 34 {6, 22, 39, 42}"],
                ["<strong>Week</strong> 1", "<strong>CLO</strong> 1-A"], ["<strong>Week</strong> 1", "<strong>CLO</strong> 1-B"], ["<strong>Week</strong> 1", "<strong>CLO</strong> 1-C"],
                ["<strong>Revision</strong>", "<strong>Covers</strong> 1-1 → 1-3"], ["<strong>Exam-style</strong>", "<strong>No answers</strong>"], ["<strong>Every</strong> step shown"]],
         parts={"A": ("Part A · Concept and interpretation (multiple choice)", "Give the letter and a one-line reason, as in a written exam.", "1"),
                "B": ("Part B · Short exam problems by lesson", "Classification with justification, Table D, systematic k, find-the-mistake.", "2"),
                "C": ("Part C · Long structured questions", "Midterm-style, multi-part. Marks in brackets.", "3"),
                "D": ("Part D · True / false with justification", "The justification is the mark.", "4"),
                "E": ("Part E · Dr. Ahmed's review self-study exercises", "The two exercises that close his deck.", "1"),
                "F": ("Part F · In-Class Quiz I simulation, Chapter 1 part (15 marks · 15 minutes)", "Closed book.", "A")}),
 2: dict(name="Chapter 2: Frequency Distributions and Graphs", figs=figs12.build2(), Q=qb12.Q2, lessons=["2-1", "2-2", "2-3"],
         series=[("00-Exam-Brief", "Chapter 2 Exam Brief", "00 · Exam brief"),
                 ("01-Lesson-2-1-Organizing-Data", "Lesson 2-1 Organizing Data", "01 · Lesson 2-1: Organizing Data"),
                 ("02-Lesson-2-2-Histograms-Polygons-Ogives", "Lesson 2-2 Histograms and Ogives", "02 · Lesson 2-2: Histograms, Frequency Polygons, Ogives"),
                 ("03-Lesson-2-3-Other-Graphs", "Lesson 2-3 Other Graphs", "03 · Lesson 2-3: Other Types of Graphs"),
                 ("04-Revision-Pack", "Chapter 2 Revision Pack", "04 · Revision pack"),
                 ("05-Questions", "Chapter 2 Exam Questions", "05 · Exam-style questions"),
                 ("06-Answers", "Chapter 2 Full Answers", "06 · Full worked answers")],
         chips=[["<strong>Week</strong> 2", "<strong>CLO</strong> 2-B · 2-C · 3-A · 3-B · 3-C", "<strong>Textbook</strong> p. 101 {5, 7, 19, 23}"],
                ["<strong>Week</strong> 2", "<strong>CLO</strong> 2-B"], ["<strong>Week</strong> 2", "<strong>CLO</strong> 2-C · 3-A · 3-B"], ["<strong>Week</strong> 2", "<strong>CLO</strong> 2-C · 3-B · 3-C"],
                ["<strong>Revision</strong>", "<strong>R</strong> Labs 2 & 4"], ["<strong>Exam-style</strong>", "<strong>No answers</strong>"], ["<strong>Every</strong> step shown"]],
         parts={"A": ("Part A · Concept and interpretation (multiple choice)", "Give the letter and a one-line reason.", "1"),
                "B": ("Part B · Short exam problems by lesson", "Construction, completing tables, reading graphs, choosing graphs, find-the-mistake.", "2"),
                "C": ("Part C · Long structured questions", "Full table-to-graph workups. Marks in brackets.", "3"),
                "D": ("Part D · True / false with justification", "The justification is the mark.", "4"),
                "F": ("Part F · In-Class Quiz I simulation, Chapter 2 part (15 marks · 15 minutes)", "Closed book, calculator allowed.", "A")}),
}

def page(c, k, body, out_dir, html_dir, extra_css=""):
    cfg = CH[c]; slug, title, _ = cfg["series"][k]; n = len(cfg["series"])
    chips = "".join(f'<span class="chip">{x}</span>' for x in cfg["chips"][k]) + f'<span class="chip"><strong>File</strong> {k + 1} / {n}</span>'
    series = " · ".join(f'<strong style="color:var(--accent)">{s[2]}</strong>' if i == k else s[2] for i, s in enumerate(cfg["series"]))
    doc = f"""{head(title)}{extra_css}
<div class="wrap">
<header class="masthead">
  <p class="eyebrow">Sultan Qaboos University · STAT 2101 · {cfg['name']}</p>
  <div class="meta-strip">{chips}</div>
</header>
{body}
<footer>
  <p><strong>Chapter {c} study set: {n} files.</strong> One merged source built from Dr. Amani Al-Rubkhi's Fall 2026 notes (course coordinator) and Dr. Ahmed Al-Hadhrami's slide pack, aligned to the SQU STAT 2101 course outline (Fall 2026). Textbook: Bluman, <em>Elementary Statistics</em>, 10th ed.</p>
  <p>{series}</p>
</footer>
</div>
"""
    p = os.path.join(html_dir, slug + ".html"); open(p, "w", encoding="utf-8").write(doc)
    return dict(src=p, out=os.path.join(out_dir, f"STAT2101-Ch{c}-{slug}.pdf"), title=title)

def qa(c, answers):
    cfg = CH[c]; Q = cfg["Q"]; out = []
    tags = lambda q: "".join(f'<span class="tag">{t}</span> ' for t in q["tags"]) + f'<span class="tag" style="--sec:var(--fg-faint)">{q["clo"]}</span>'
    if answers:
        out.append(f"""<section style="--sec:var(--accent);--wash:var(--accent-wash)"><div class="sec-head"><span class="sec-num">ANS</span><h2>Chapter {c} full worked answers<span class="ar">الإجابات الكاملة: افتحه بعد حل ملف الأسئلة</span></h2></div>
<p>Each answer gives the result, the reason a marker looks for, and in the <span class="v">why</span> lines the trap the question was built on. Numeric answers were computed by code from the question data.</p></section>""")
    else:
        cover = {}
        for q in Q:
            for t in q["tags"]: cover[t] = cover.get(t, 0) + 1
        out.append(f"""<section style="--sec:var(--accent);--wash:var(--accent-wash)"><div class="sec-head"><span class="sec-num">Q</span><h2>Chapter {c} exam-style questions<span class="ar">أسئلة امتحانية حقيقية: تصنيف مع تبرير، بناء وقراءة، اكتشاف أخطاء. ليست أسئلة مباشرة</span></h2></div>
<p>Built from the outline's assessment criteria for this chapter. Every question carries its lesson tag and outcome tag; a wrong answer points to the lesson file to reopen. Answers are in a <strong>separate file</strong>.</p>
<div class="tbl-wrap"><table><thead><tr><th>Lesson</th>{''.join(f'<th class="num">{l}</th>' for l in cfg['lessons'])}</tr></thead><tbody><tr><td>Questions touching the lesson</td>{''.join(f'<td class="num">{cover.get(l,0)}</td>' for l in cfg['lessons'])}</tr></tbody></table></div>
<ar t="طريقة الاستخدام">الأسئلة على نمط الكويز والميدتيرم: <b>تصنيف مع تبرير</b>، <b>بناء جدول أو رسم</b>، <b>قراءة رسم واستخراج قيمة</b>، و<b>اكتشاف خطأ طالب</b>. حلّها مغلق الكتاب ثم صحّح من ملف الإجابات. الجزء F محاكاة لجزء هذا الفصل في الكويز الصفي الأول.</ar></section>""")
    for p, (title, lead, tone) in cfg["parts"].items():
        sec = "var(--accent)" if tone == "A" else f"var(--ink-{tone})"; wash = "var(--accent-wash)" if tone == "A" else f"var(--ink-{tone}-wash)"
        cards = []
        for q in [q for q in Q if q["part"] == p]:
            mk = f' <strong>[{q["marks"]} marks]</strong>' if q["marks"] else ""
            if answers:
                cards.append(f'<div class="a{" long" if q["marks"] else ""}"><div class="ahead"><span class="id">{q["id"]}</span>{tags(q)}{mk}</div>{q["a"]}</div>')
            else:
                cards.append(f'<div class="q"><span class="id">{q["id"]}</span><div class="bd">{tags(q)}{mk}{q["q"]}</div></div>')
        out.append(f'<section style="--sec:{sec};--wash:{wash}"><h3 class="grp">{title}</h3><p class="lead">{lead}</p>{"".join(cards)}</section>')
    return markup("\n".join(out), cfg["figs"])

manifest = []
for c in (1, 2):
    out_dir = f"/home/user/STAT2101/Chapter{c}"; html_dir = os.path.join(out_dir, "html"); os.makedirs(html_dir, exist_ok=True)
    for k in range(5):
        frag = open(os.path.join(HERE, f"frag{c}", f"{k:02d}.html"), encoding="utf-8").read()
        manifest.append(page(c, k, markup(frag, CH[c]["figs"]), out_dir, html_dir))
    manifest.append(page(c, 5, qa(c, False), out_dir, html_dir, QA_CSS))
    manifest.append(page(c, 6, qa(c, True), out_dir, html_dir, QA_CSS))
    used = set(); src = "".join(open(os.path.join(HERE, f"frag{c}", f"{k:02d}.html"), encoding="utf-8").read() for k in range(5))
    used = set(re.findall(r'<fig id="([a-z0-9_]+)"', src)); unused = set(CH[c]["figs"]) - used
    print(f"Ch{c}: questions {len(CH[c]['Q'])}, figures used {len(used)}, unused {sorted(unused) or 'none'}")
json.dump(manifest, open(os.path.join(HERE, "manifest.json"), "w"), indent=1)
for m in manifest: print(os.path.basename(m["src"]), os.path.getsize(m["src"]) // 1024, "KB")
