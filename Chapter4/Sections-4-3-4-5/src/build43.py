import os, sys, json
sys.path.insert(0, "/tmp/claude-0/-home-user-STAT2101/521e5d47-fbd3-5206-8b60-93d1c3cc1629/scratchpad/ch3")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ch3lib import head, markup
from q43 import Q
# ------------------------------------------------------------------ build
QA_CSS = open("/home/user/STAT2101/Chapter1/html/05-Questions.html", encoding="utf-8").read()
QA_CSS = QA_CSS[QA_CSS.index("<style>\n.q{"):]; QA_CSS = QA_CSS[:QA_CSS.index("</style>") + 8]
PARTS = {"A": ("Part A · Multiple choice (16)", "Give the letter and a one-line reason, as in a written exam.", "1"),
         "B": ("Part B · Short structured questions (16)", "Typical 2–6 mark midterm items. Write S and E in set notation.", "2"),
         "C": ("Part C · Long questions (5)", "Midterm-style, multi-part. Marks in brackets.", "3"),
         "D": ("Part D · 20-minute mini-quiz (16 marks)", "Time yourself, closed book, before opening the answers.", "A")}
OUT = "/home/user/STAT2101/Chapter4/Sections-4-3-4-5"; os.makedirs(OUT + "/html", exist_ok=True)
def page(title, slug, body):
    doc = f"""{head(title)}{QA_CSS}
<div class="wrap"><header class="masthead"><p class="eyebrow">Sultan Qaboos University · STAT 2101 · Chapter 4 · Sections 4-3, 4-4 and 4-5 only</p>
<div class="meta-strip"><span class="chip"><strong>{len(Q)}</strong> questions</span><span class="chip"><strong>CLO</strong> 4-A</span><span class="chip"><strong>Final</strong> 29/12/2026</span></div></header>
{body}
<footer><p>Built to the STAT 2101 Fall 2026 course outline (CLO4-A: calculate probabilities using counting rules and basic probability principles). Sections 4-3 Multiplication Rules and Conditional Probability, 4-4 Counting Rules and 4-5 Probability and Counting Rules only. Every numeric answer was computed by code from the question data.</p></footer></div>"""
    path = f"{OUT}/html/{slug}.html"; open(path, "w", encoding="utf-8").write(doc)
    return dict(src=path, out=f"{OUT}/STAT2101-Ch4-4-3-4-5-{slug}.pdf", title=title)
def body(ans):
    tg = lambda q: "".join(f'<span class="tag">{t}</span> ' for t in q["tags"])
    out = [f"""<section style="--sec:var(--accent);--wash:var(--accent-wash)"><div class="sec-head"><span class="sec-num">{'ANS' if ans else 'Q'}</span><h2>{'Full worked answers' if ans else 'Exam-style questions'}: Sections 4-3, 4-4 and 4-5
<span class="ar">{'الإجابات الكاملة — افتحه بعد حل ملف الأسئلة' if ans else 'أسئلة بمعايير اختبارات جامعة السلطان قابوس — الاحتمالات 4-3 و 4-4 و 4-5'}</span></h2></div>
{'<p>Each answer shows the set or the rule, the substitution and the value. The <span class="v">why</span> lines name the trap the question was built on.</p>' if ans else
 '<p>Covers sections 4-3 (independent and dependent events, multiplication rules 1 and 2, conditional probability, independence tests, two-way tables, tree diagrams, at least one), 4-4 (fundamental counting rule, factorial, permutation rules 1 and 2, combinations) and 4-5 (probability with counting rules). Every question is tagged with its section.</p>'
 '<ar t="طريقة الاستخدام">حل الجزء D أولًا (20 دقيقة) لتعرف مستواك، ثم الأجزاء A و B و C، ثم صحّح من ملف الإجابات. حدّد دائمًا: مع إرجاع أم بدون؟ الترتيب مهم أم لا؟ واكتب القاعدة التي تستخدمها، فعليها درجات.</ar>'}
</section>"""]
    for pt, (title, lead, tone) in PARTS.items():
        sec = "var(--accent)" if tone == "A" else f"var(--ink-{tone})"; wash = "var(--accent-wash)" if tone == "A" else f"var(--ink-{tone}-wash)"
        cards = []
        for q in [q for q in Q if q["part"] == pt]:
            mk = f' <strong>[{q["marks"]} marks]</strong>' if q["marks"] else ""
            cards.append(f'<div class="a{" long" if q["marks"] else ""}"><div class="ahead"><span class="id">{q["id"]}</span>{tg(q)}{mk}</div>{q["a"]}</div>' if ans
                         else f'<div class="q"><span class="id">{q["id"]}</span><div class="bd">{tg(q)}{mk}{q["q"]}</div></div>')
        out.append(f'<section style="--sec:{sec};--wash:{wash}"><h3 class="grp">{title}</h3><p class="lead">{lead}</p>{"".join(cards)}</section>')
    return markup("\n".join(out), {})
man = [page("Probability 4-3 to 4-5 Questions", "Questions", body(False)), page("Probability 4-3 to 4-5 Answers", "Answers", body(True))]
json.dump(man, open(os.path.join(os.path.dirname(__file__), "manifest43.json"), "w"))
print(len(Q), "questions", {k: sum(q["part"] == k for q in Q) for k in "ABCD"})
