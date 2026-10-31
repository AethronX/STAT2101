"""Chapter 1 and Chapter 2 diagrams, drawn to scale from the lecture data."""
import sys, math, itertools
sys.path.insert(0, "/tmp/claude-0/-home-user-STAT2101/521e5d47-fbd3-5206-8b60-93d1c3cc1629/scratchpad/ch3")
from ch3lib import *

def build1():
    F = {}
    # ---------------------------------------------------- population, sample, census, survey
    u = "ps1"
    g = [C(130, 100, 82, "wash1 ln s1"), T(130, 12, "Population (size N)", "sm b t1")]
    import random
    rnd = random.Random(7)
    pts = []
    while len(pts) < 46:
        x, y = rnd.uniform(60, 200), rnd.uniform(36, 164)
        if (x - 130) ** 2 + (y - 100) ** 2 < 70 ** 2 and all((x - a) ** 2 + (y - b) ** 2 > 140 for a, b in pts):
            pts.append((x, y))
    pick = {3, 9, 15, 22, 30, 41}
    for i, (x, y) in enumerate(pts):
        g.append(C(x, y, 4, "f2" if i in pick else "f1", "" if i in pick else ' fill-opacity="0.45"'))
    sp = [(470 + (k % 3) * 26, 82 + (k // 3) * 26) for k in range(6)]
    g += [C(496, 95, 46, "wash2 ln s2 dash"), T(496, 40, "Sample (size n)", "sm b t2")]
    g += [C(x, y, 4, "f2") for x, y in sp]
    g += [T(130, 204, "measure every member = CENSUS", "sm b t1"), T(496, 204, "measure the sample = SURVEY", "sm b t2"),
          T(312, 70, "select", "sm soft"), AR(260, 80, 380, 80, u), AR(380, 120, 260, 120, u), T(312, 140, "infer back", "sm soft")]
    F["popsample"] = fig(640, 216, "\n".join(g),
        "A population of points with six highlighted members drawn into a sample, with census and survey labelled",
        "A sample is a subset of the population. Measuring every member of the population is a census (e.g. Oman's 2020 census by the NCSI); measuring only a sample is a survey. Inferential statistics uses the sample to say something about the population.",
        "العينة جزء من المجتمع. جمع البيانات من كل أفراد المجتمع يسمى حصرًا شاملًا (census) مثل تعداد عُمان 2020، وجمعها من عينة يسمى مسحًا (survey). الإحصاء الاستدلالي يستخدم العينة للحكم على المجتمع.",
        arrow_defs(u))

    # ---------------------------------------------------- dataset anatomy
    g = []
    cols = ["ID", "College", "Gender", "GPA"]; rows = [["10234", "Science", "Female", "3.7"], ["11234", "Medical", "Male", "3.0"], ["10771", "Arts", "Female", "3.4"]]
    x0, y0, cw, rh = 150, 40, 92, 28
    for j, c in enumerate(cols):
        g += [R(x0 + j * cw, y0, cw, rh, "wash1 ln s1"), T(x0 + j * cw + cw / 2, y0 + 19, c, "sm b t1")]
    for i, r in enumerate(rows):
        for j, v in enumerate(r):
            hit = (i, j) == (1, 3)
            g += [R(x0 + j * cw, y0 + (i + 1) * rh, cw, rh, "wash3 ln s3 thick" if hit else "bg ln-soft"), T(x0 + j * cw + cw / 2, y0 + (i + 1) * rh + 19, v, "m b t3" if hit else "m")]
    g += [R(x0 - 6, y0 - 6, 4 * cw + 12, 4 * rh + 12, "ln s2 dash", 6),
          T(18, y0 + 19, "variables →", "sm b t1", "start"), T(18, y0 + 2 * rh + 19, "one row = one", "sm", "start"), T(18, y0 + 2 * rh + 35, "individual", "sm", "start"),
          T(x0 + 4 * cw + 14, y0 + 2 * rh + 19, "← a data value", "sm b t3", "start"), T(x0 + 4 * cw + 14, y0 + 2 * rh + 35, "(datum): 3.0", "sm t3", "start"),
          T(x0 + 2 * cw, y0 + 4 * rh + 30, "the whole table = the data set", "sm b t2")]
    F["dataset"] = fig(640, 196, "\n".join(g),
        "A small table with the header row marked as variables, one cell marked as a data value, and the whole table marked as the data set",
        "Dr. Amani's dataset activity answered on the table itself: each column heading is a variable, each cell is a data value (datum), and the whole table is the data set.",
        "إجابة نشاط د. أماني على الجدول نفسه: كل عنوان عمود متغير (variable)، وكل خلية قيمة بيانات (datum)، والجدول كله مجموعة بيانات (data set).")

    # ---------------------------------------------------- descriptive vs inferential
    u = "di"
    g = [R(20, 20, 290, 168, "wash2 ln s2", 8), R(340, 20, 290, 168, "wash4 ln s4", 8),
         T(165, 44, "Descriptive statistics", "b t2"), T(485, 44, "Inferential statistics", "b t4"),
         T(165, 66, "collect · organise · summarise · present", "sm"), T(485, 66, "sample → conclusion about population", "sm"),
         T(165, 98, "tables, frequency tables", "sm soft"), T(165, 116, "graphs and charts (Ch. 2)", "sm soft"),
         T(165, 134, "mean, SD, percentiles (Ch. 3)", "sm soft"),
         T(485, 98, "probability (Ch. 4–6)", "sm soft"), T(485, 116, "estimation, hypothesis tests (Ch. 7–9)", "sm soft"),
         T(485, 134, "relationships, prediction (Ch. 10)", "sm soft"),
         T(165, 168, "\"the average age in the 2020 census was …\"", "sm b t2"),
         T(485, 168, "\"…so flu cases next November will be …\"", "sm b t4")]
    F["descinf"] = fig(650, 200, "\n".join(g),
        "Two panels comparing descriptive statistics, which summarise data, with inferential statistics, which generalise from a sample",
        "The test is the verb. Describing what was observed (an average, a percentage, a chart of the collected data) is descriptive. Predicting, generalising to a population, or claiming a relationship goes beyond the data, so it is inferential.",
        "المفتاح هو الفعل: إذا كانت الجملة تصف ما تم جمعه (متوسط، نسبة، رسم) فهي وصفية. وإذا كانت تتنبأ أو تعمّم على المجتمع أو تدّعي علاقة فهي استدلالية.")

    # ---------------------------------------------------- variable tree
    g = [R(260, 12, 130, 30, "bg ln", 5), T(325, 32, "Variable", "b"),
         L(325, 42, 160, 74, "ln"), L(325, 42, 490, 74, "ln"),
         R(70, 74, 180, 30, "wash1 ln s1", 5), T(160, 94, "Qualitative (categorical)", "sm b t1"),
         R(400, 74, 180, 30, "wash2 ln s2", 5), T(490, 94, "Quantitative (numerical)", "sm b t2"),
         T(160, 124, "labels or categories", "sm soft"), T(160, 142, "gender, blood type, colour,", "sm"), T(160, 158, "ID, nationality, letter grade", "sm"),
         L(490, 104, 410, 136, "ln"), L(490, 104, 570, 136, "ln"),
         R(350, 136, 120, 28, "wash3 ln s3", 5), T(410, 155, "Discrete", "sm b t3"),
         R(510, 136, 120, 28, "wash4 ln s4", 5), T(570, 155, "Continuous", "sm b t4"),
         T(410, 182, "counted: 0, 1, 2, …", "sm soft"), T(410, 198, "children, students, calls", "sm"),
         T(570, 182, "measured: any value", "sm soft"), T(570, 198, "height, weight, time, GPA", "sm")]
    F["vartree"] = fig(650, 208, "\n".join(g),
        "Tree splitting variables into qualitative and quantitative, and quantitative into discrete and continuous, with examples",
        "Ask two questions in order: is the value a category or a number? If a number, was it counted (discrete) or measured (continuous)? A number used as a label, like a student ID, is still qualitative.",
        "اسأل سؤالين بالترتيب: هل القيمة تصنيف أم رقم؟ وإذا كانت رقمًا: هل نحصل عليه بالعدّ (منفصل) أم بالقياس (متصل)؟ الرقم المستخدم كاسم، مثل الرقم الجامعي، يبقى متغيرًا وصفيًا.")

    # ---------------------------------------------------- levels of measurement property matrix
    props = ["Categories", "Natural order", "Equal, meaningful differences", "True zero (ratios meaningful)"]
    levels = [("Nominal", "1", "gender, blood type, ID, nationality", [1, 0, 0, 0]),
              ("Ordinal", "3", "letter grade, ranking, poor/fair/good", [1, 1, 0, 0]),
              ("Interval", "2", "°C, °F, IQ, SAT, calendar year, date", [1, 1, 1, 0]),
              ("Ratio", "4", "height, weight, age, income, time, K", [1, 1, 1, 1])]
    x0, cw = 130, 92
    g = []
    heads = [("Categories", ""), ("Natural", "order"), ("Equal", "differences"), ("True zero", "(ratios OK)")]
    for j, (h1, h2) in enumerate(heads):
        g.append(T(x0 + j * cw + cw / 2, 18, h1, "sm b"))
        if h2: g.append(T(x0 + j * cw + cw / 2, 34, h2, "sm b"))
    for i, (name, tone, ex, has) in enumerate(levels):
        y = 50 + i * 40
        g += [R(10, y, 112, 32, f"wash{tone} ln s{tone}", 4), T(66, y + 21, name, f"sm b t{tone}")]
        for j, h in enumerate(has):
            cx = x0 + j * cw + cw / 2
            g.append(C(cx, y + 16, 9, f"f{tone}" if h else "bg ln-soft"))
            if h:
                g.append(T(cx, y + 20.5, "✓", "sm b", extra=' style="fill:#fff"'))
        g.append(T(x0 + 4 * cw + 8, y + 21, ex, "sm", "start"))
    g += [T(66, 222, "↑ more information", "sm soft")]
    F["levels"] = fig(720, 230, "\n".join(g),
        "Matrix showing which of four properties each level of measurement has, from nominal with one to ratio with all four",
        "Each level keeps every property of the level below and adds one. To classify a variable, find the highest property it has: zero meaning 'none' makes it ratio; equal steps without a true zero makes it interval.",
        "كل مستوى يحتفظ بخصائص المستوى الأدنى ويضيف خاصية واحدة. لتصنيف متغير ابحث عن أعلى خاصية يملكها: إذا كان الصفر يعني «لا شيء» فهو نسبي (ratio)، وإذا كانت الفروق متساوية بلا صفر حقيقي فهو فتري (interval).")

    # ---------------------------------------------------- boundaries
    sx = scale(17.5, 17.7, 60, 600)
    g = axis(sx, 17.5, 17.7, 80, [17.5, 17.55, 17.6, 17.65, 17.7], lambda v: f"{v:g}")
    g += [R(sx(17.55), 56, sx(17.65) - sx(17.55), 24, "wash1 ln s1"), C(sx(17.6), 68, 5, "f1"),
          T(sx(17.6), 46, "recorded value 17.6 in", "sm b t1"),
          T(sx(17.55), 118, "17.6 − 0.05", "sm b"), T(sx(17.65), 118, "17.6 + 0.05", "sm b"),
          T(330, 140, "true value lies in 17.55 – 17.65 (the slide's 18.55 is a typo)", "sm tA")]
    F["boundary"] = fig(640, 150, "\n".join(g),
        "Number line showing the recorded value 17.6 and its boundaries 17.55 and 17.65",
        "A continuous value is rounded when recorded, so 17.6 stands for every true value from 17.55 to 17.65. Go half a unit of the last recorded digit each way: one decimal place means ± 0.05.",
        "القيمة المتصلة تُقرّب عند تسجيلها، فالرقم 17.6 يمثل أي قيمة حقيقية بين 17.55 و 17.65. نضيف ونطرح نصف وحدة آخر خانة: خانة عشرية واحدة تعني ± 0.05.")

    # ---------------------------------------------------- SRS from table D
    row = "06512 07836 88456 36313 30879 51323 76451 25578 15986 50845 57015 53684 57054 93261".replace(" ", "")
    chunks = [row[i:i + 4] for i in range(0, 68, 4)]
    chosen = []
    g = [T(12, 18, "Table D, row 2, read in 4-digit groups (N = 4998, n = 10)", "sm b", "start")]
    for k, c in enumerate(chunks):
        v = int(c); full = len(chosen) >= 10; ok = 1 <= v <= 4998 and v not in chosen and not full
        if ok: chosen.append(v)
        x = 12 + (k % 9) * 70; y = 32 + (k // 9) * 46
        g += [R(x, y, 62, 26, "wash2 ln s2 thick" if ok else "bg ln-soft", 3), T(x + 31, y + 18, c, "m b t2" if ok else "m soft")]
        if not ok:
            g.append(T(x + 31, y + 38, "n reached" if full else ("> N" if v > 4998 else "repeat"), "sm soft" if full else "sm tA"))
    g.append(T(12, 140, "leftover digits \"61\" are not a full group, so the read stops", "sm soft", "start"))
    F["srs"] = fig(650, 150, "\n".join(g),
        "Random-number digits split into four-digit groups with the ten accepted laptop numbers highlighted and rejected groups marked",
        "Dr. Ahmed's laptop example. Group the digits to the number of digits in N, keep groups from 1 to N, and skip anything larger than N or repeated. The first ten accepted groups are the sample.",
        "مثال الحواسيب: نقسم الأرقام إلى مجموعات بعدد خانات N، ونقبل ما بين 1 و N، ونتجاوز ما هو أكبر من N أو مكرر. أول عشرة مقبولة هي العينة.")

    # ---------------------------------------------------- systematic
    sx = scale(1, 86, 40, 620)
    g = [T(20, 16, "k = 86/6 = 14.33 → round DOWN to 14, start 6 (Dr. Amani)", "sm b t2", "start")]
    for t in range(1, 87):
        sel = t in (6, 20, 34, 48, 62, 76)
        g.append(L(sx(t), 30, sx(t), 50 if sel else 42, "ln s2 thick" if sel else "ln-soft"))
        if sel: g.append(T(sx(t), 64, str(t), "sm b t2"))
    g += [T(20, 92, "k rounded UP to 15 with start 15 → only 5 trees fit (Dr. Ahmed's rounding fails)", "sm b tA", "start")]
    for t in range(1, 87):
        sel = t in (15, 30, 45, 60, 75)
        g.append(L(sx(t), 104, sx(t), 124 if sel else 116, "ln sA thick" if sel else "ln-soft"))
        if sel: g.append(T(sx(t), 138, str(t), "sm b tA"))
    g.append(T(sx(90), 138, "90 > 86 ✗", "sm b tA", "end"))
    F["systematic"] = fig(650, 148, "\n".join(g),
        "Two rows of 86 tree ticks: every 14th from tree 6 gives six trees; every 15th from tree 15 gives only five",
        "Why round k down: with k = 14, any start from 1 to 14 still reaches six trees within 86. With k = 15, a start of 15 runs past the fence after five trees, so the sample is short.",
        "لماذا نقرّب k لأسفل؟ مع k = 14 أي بداية من 1 إلى 14 تعطي 6 أشجار ضمن 86. أما مع k = 15 فالبداية 15 تتجاوز آخر شجرة بعد 5 أشجار فقط، فتنقص العينة.")

    # ---------------------------------------------------- stratified vs cluster
    g = [T(160, 18, "Stratified: some from EVERY group", "sm b t2"), T(490, 18, "Cluster: ALL from SOME groups", "sm b t4")]
    rnd = random.Random(3)
    for side, tone in ((0, "2"), (1, "4")):
        for gi in range(4):
            gx = 30 + side * 330 + gi * 70; gy = 40
            g.append(R(gx, gy, 60, 100, f"wash{tone} ln s{tone}", 6))
            g.append(T(gx + 30, gy + 116, ["Stats", "Maths", "Physics", "Chem"][gi] if side == 0 else f"School {gi + 1}", "sm"))
            for k in range(8):
                px, py = gx + 15 + (k % 2) * 30, gy + 14 + (k // 2) * 22
                if side == 0:
                    sel = k in rnd.sample(range(8), 2)
                else:
                    sel = gi in (0, 2)
                g.append(C(px, py, 6, f"f{tone}" if sel else "bg ln-soft"))
    F["stratclust"] = fig(650, 168, "\n".join(g),
        "Two panels: stratified sampling selects a few from each of four groups; cluster sampling selects every member of two whole groups",
        "Stratified: divide by a characteristic (department), then draw a random sample from every stratum, so every group is represented; sizes need not be equal. Cluster: divide into ready-made groups (schools), randomly pick whole clusters, and include everyone in them.",
        "الطبقية: نقسم حسب خاصية (القسم) ثم نسحب عينة عشوائية من كل طبقة، فتمثَّل كل المجموعات (والأعداد لا يلزم أن تتساوى). العنقودية: نقسم إلى مجموعات جاهزة (مدارس)، نختار بعض العناقيد عشوائيًا، ونأخذ كل أفرادها.")
    return F


def build2():
    F = {}
    def hist(vals, edges, title_y, tone="2", W=640, H=230, ylab="Frequency", ymax=None, fmt=lambda v: f"{v:g}", ytick=None, rel=False, labels=True):
        ymax = ymax or max(vals) * 1.15
        sx = scale(edges[0], edges[-1], 70, W - 20); sy = scale(0, ymax, H - 40, 20)
        g = [L(70, H - 40, W - 16, H - 40, "ln"), L(70, H - 40, 70, 14, "ln"), T(18, (H - 40) / 2, ylab, "sm b", "middle", f' transform="rotate(-90 18 {(H - 40) / 2})"')]
        step = ytick or max(1, round(ymax / 5))
        t = 0
        while t <= ymax:
            g += [L(66, sy(t), 70, sy(t), "ln"), T(62, sy(t) + 4, fmt(t) if rel else f"{t:g}", "sm soft", "end"), L(70, sy(t), W - 16, sy(t), "ln-soft", ' stroke-opacity="0.35"')]
            t = round(t + step, 6)
        for i, v in enumerate(vals):
            g.append(R(sx(edges[i]), sy(v), sx(edges[i + 1]) - sx(edges[i]), sy(0) - sy(v), f"wash{tone} ln s{tone}"))
            if labels and v:
                g.append(T((sx(edges[i]) + sx(edges[i + 1])) / 2, sy(v) - 5, fmt(v) if rel else f"{v:g}", "sm b"))
        for e in edges:
            g += [L(sx(e), H - 40, sx(e), H - 35, "ln"), T(sx(e), H - 22, f"{e:g}", "sm")]
        g.append(T((70 + W) / 2, H - 4, title_y, "sm b"))
        # break mark on x axis
        g += [P([(76, H - 44), (80, H - 36), (84, H - 44), (88, H - 36)], "ln")]
        return g
    def ogive(xs, ys, title_x, W=640, H=230, ymax=None, ylab="Cumulative frequency", rel=False, tone="4"):
        ymax = ymax or ys[-1] * 1.1
        sx = scale(xs[0], xs[-1], 70, W - 30); sy = scale(0, ymax, H - 40, 16)
        g = [L(70, H - 40, W - 16, H - 40, "ln"), L(70, H - 40, 70, 12, "ln"), T(18, (H - 40) / 2, ylab, "sm b", "middle", f' transform="rotate(-90 18 {(H - 40) / 2})"')]
        step = 0.2 if rel else (10 if ymax > 30 else 5)
        t = 0
        while t <= ymax + 1e-9:
            g += [L(66, sy(t), 70, sy(t), "ln"), T(62, sy(t) + 4, f"{t:g}", "sm soft", "end"), L(70, sy(t), W - 16, sy(t), "ln-soft", ' stroke-opacity="0.35"')]
            t = round(t + step, 6)
        g.append(P([(sx(a), sy(b)) for a, b in zip(xs, ys)], f"ln thick s{tone}"))
        for a, b in zip(xs, ys):
            g += [C(sx(a), sy(b), 4, f"f{tone}"), L(sx(a), H - 40, sx(a), H - 35, "ln"), T(sx(a), H - 22, f"{a:g}", "sm")]
        if b: g.append(T(sx(a), sy(b) - 9, f"{b:g}", "sm b"))
        g.append(T((70 + W) / 2, H - 4, title_x, "sm b"))
        return g

    # ---------------------------------------------------- limits vs boundaries
    sx = scale(98, 116, 40, 620)
    g = axis(sx, 98, 116, 110, range(98, 117, 1))
    for i, (lo, hi) in enumerate(((100, 104), (105, 109), (110, 114))):
        g += [R(sx(lo), 40, sx(hi) - sx(lo), 22, "wash1 ln s1", 3), T((sx(lo) + sx(hi)) / 2, 56, f"limits {lo}–{hi}", "sm b t1")]
        g += [R(sx(lo - .5), 70, sx(hi + .5) - sx(lo - .5), 22, "wash2 ln s2"), T((sx(lo - .5) + sx(hi + .5)) / 2, 86, f"{lo - .5}–{hi + .5}", "sm b t2")]
    g += [T(sx(104.5), 28, "gap", "sm tA"), T(560, 56, "limits leave gaps", "sm t1", "start"), T(560, 86, "boundaries touch", "sm t2", "start")]
    F["limbound"] = fig(650, 146, "\n".join(g),
        "Three classes on a number line: class limits 100–104, 105–109, 110–114 leave gaps; boundaries 99.5–104.5 etc. close them",
        "Example 2-2 (record temperatures). Class limits are the smallest and largest values a class can hold, so whole-number classes leave gaps (104 to 105). Boundaries subtract and add half a unit (0.5) so the classes meet, and the histogram bars can touch.",
        "مثال 2-2: حدود الفئة (limits) أصغر وأكبر قيمة في الفئة، وبينها فجوات (من 104 إلى 105). الحدود الفعلية (boundaries) نطرح ونضيف نصف وحدة (0.5) فتتلاصق الفئات وتتلاصق أعمدة المدرج.")

    # ---------------------------------------------------- histograms
    tE = [99.5, 104.5, 109.5, 114.5, 119.5, 124.5, 129.5, 134.5]; tF = [2, 8, 18, 13, 7, 1, 1]
    F["histtemp"] = fig(640, 230, "\n".join(hist(tF, tE, "Record high temperature (°F): class boundaries", ymax=20, ytick=4)),
        "Frequency histogram of 50 record high temperatures with bars from 99.5 to 134.5",
        "Example 2-4. Class boundaries on the x-axis, frequencies on the y-axis, bars touching. The peak is the 109.5–114.5 class (18 states); the distribution is roughly bell-shaped with a slight right tail. The zig-zag marks that the axis does not start at 0.",
        "مثال 2-4: الحدود الفعلية على المحور الأفقي والتكرارات على الرأسي، والأعمدة متلاصقة. القمة في الفئة 109.5–114.5 (18 ولاية)، والشكل قريب من الجرسي مع ذيل خفيف لليمين. الخط المتعرج يعني أن المحور لا يبدأ من الصفر.")
    gE = [42.5, 47.5, 52.5, 57.5, 62.5, 67.5, 72.5, 77.5]; gR = [.08, .08, .22, .28, .18, .10, .06]
    F["histgov"] = fig(640, 230, "\n".join(hist(gR, gE, "Age of state governors: class boundaries", ylab="Relative frequency", ymax=.32, ytick=.05, rel=True, fmt=lambda v: f"{v:.2f}".rstrip('0').rstrip('.') if v else "0", tone="3")),
        "Relative frequency histogram of governors' ages peaking at 0.28 in the 57.5–62.5 class",
        "Example 2-7. Same shape as a frequency histogram; only the y-axis changes to relative frequency f/n, so the bar heights sum to 1. Use it to compare data sets of different sizes.",
        "مثال 2-7: نفس شكل المدرج التكراري، لكن المحور الرأسي هو التكرار النسبي f/n، ومجموع ارتفاعات الأعمدة = 1. نستخدمه لمقارنة مجموعات مختلفة الحجم.")
    dE = [20.5, 28.5, 36.5, 44.5, 52.5, 60.5, 68.5, 76.5]; dF = [19, 20, 16, 14, 0, 1, 1]
    F["histdrv"] = fig(640, 230, "\n".join(hist(dF, dE, "Age of drivers: class boundaries (Dr. Amani's table, n = 71)", ymax=24, ytick=4, tone="1")),
        "Frequency histogram of drivers' ages with an empty 52.5–60.5 class",
        "Dr. Amani's histogram example. The empty 52.5–60.5 class is drawn as a gap with zero height, never removed. Most drivers are 20–52; the two older drivers form a long right tail: right-skewed.",
        "مثال د. أماني: الفئة 52.5–60.5 تكرارها صفر فتظهر فراغًا ولا تُحذف. أغلب السائقين بين 20 و 52، والسائقان الأكبر سنًا يشكلان ذيلًا طويلًا لليمين: التواء موجب.")

    # ---------------------------------------------------- frequency polygon
    mids = [97, 102, 107, 112, 117, 122, 127, 132, 137]; fp = [0, 2, 8, 18, 13, 7, 1, 1, 0]
    sx = scale(95, 139, 70, 620); sy = scale(0, 20, 190, 16)
    g = [L(70, 190, 626, 190, "ln"), L(70, 190, 70, 12, "ln"), T(18, 100, "Frequency", "sm b", "middle", ' transform="rotate(-90 18 100)"')]
    for t in range(0, 21, 4):
        g += [T(62, sy(t) + 4, str(t), "sm soft", "end"), L(70, sy(t), 626, sy(t), "ln-soft", ' stroke-opacity="0.35"')]
    g.append(P([(sx(m), sy(f)) for m, f in zip(mids, fp)], "ln thick s3"))
    for m, f in zip(mids, fp):
        g += [C(sx(m), sy(f), 4, "f3" if 0 < f else "fA"), T(sx(m), 208, str(m), "sm"), L(sx(m), 190, sx(m), 195, "ln")]
        if f: g.append(T(sx(m), sy(f) - 9, str(f), "sm b"))
    g += [T(sx(97), 172, "extra class", "sm tA"), T(sx(137), 172, "extra class", "sm tA"), T(345, 226, "Class midpoints (°F)", "sm b")]
    F["polygon"] = fig(640, 232, "\n".join(g),
        "Frequency polygon of the temperature data plotted at class midpoints and closed at 97 and 137",
        "Example 2-5. Plot frequencies at the class midpoints (not boundaries) and join them with straight lines. Add one empty class at each end (midpoints 97 and 137) so the polygon starts and ends on the x-axis.",
        "مثال 2-5: نرسم التكرارات عند <b>مراكز</b> الفئات (لا الحدود) ونصل النقاط بخطوط مستقيمة، ونضيف فئة فارغة في كل طرف (97 و 137) حتى يبدأ المضلع وينتهي على المحور الأفقي.")

    # ---------------------------------------------------- ogives
    F["ogivetemp"] = fig(640, 230, "\n".join(ogive(tE, [0] + list(itertools.accumulate(tF)), "Upper class boundary (°F)", ymax=55)),
        "Ogive of cumulative frequency for the temperature data rising from 0 at 99.5 to 50 at 134.5",
        "Example 2-4 ogive. Each point is (upper boundary, cumulative frequency); the line starts at 0 on the first lower boundary. The steepest segment, 109.5–114.5, is the class with the most values. Read it like: 41 states had a record below 119.5 °F.",
        "منحنى التكرار المتجمع: كل نقطة هي (الحد الأعلى، التكرار المتجمع)، ويبدأ من الصفر عند أول حد أدنى. أشد جزء انحدارًا (109.5–114.5) هو الفئة الأكثر تكرارًا. ويُقرأ هكذا: 41 ولاية سجلت أقل من 119.5.")
    crf = [0] + [round(c / 71, 3) for c in itertools.accumulate(dF)]
    F["ogivedrv"] = fig(640, 230, "\n".join(ogive(dE, crf, "Upper class boundary (age)", ymax=1.05, ylab="Cumulative relative frequency", rel=True, tone="1")),
        "Cumulative relative frequency ogive of drivers' ages reaching 1 at 76.5",
        "Dr. Amani's second ogive: same points as the cumulative frequency ogive but divided by n = 71, so it always ends at 1. The flat segment from 52.5 to 60.5 is the empty class. About 97% of drivers were younger than 52.5.",
        "المنحنى الثاني لـ د. أماني: نفس النقاط مقسومة على n = 71، فينتهي دائمًا عند 1. الجزء الأفقي (52.5–60.5) هو الفئة الفارغة. حوالي 97% من السائقين أعمارهم أقل من 52.5.")

    # ---------------------------------------------------- shapes
    shapes = [("Bell-shaped", [1, 2, 3, 5, 6, 5, 3, 2, 1]), ("Uniform", [4, 4, 3.6, 4.3, 3.9, 3.8, 3.9, 4.1, 4]),
              ("J-shaped", [1, 1.5, 2, 2, 3, 3.6, 3.6, 4.5, 6]), ("Reverse J-shaped", [6, 4.5, 3.6, 3, 3, 2.4, 2, 1.2, 1.2]),
              ("Right-skewed", [3.5, 5.6, 6, 4.4, 3.5, 2.6, 1.8, 1, .6]), ("Left-skewed", [.6, 1, 1.8, 2.6, 3.5, 4.4, 6, 5.6, 3.5]),
              ("Bimodal", [1.5, 2.8, 5.6, 4, 2, 5.6, 4, 2.4, 1]), ("U-shaped", [5.6, 4, 4, 3.4, 1.6, 2.4, 4.6, 5.4, 6])]
    g = []
    for i, (name, hs) in enumerate(shapes):
        px, py = 12 + (i % 4) * 160, 10 + (i // 4) * 104
        for j, h in enumerate(hs):
            g.append(R(px + 8 + j * 14, py + 70 - h * 10, 14, h * 10, "wash2 ln s2"))
        g += [L(px + 4, py + 70, px + 138, py + 70, "ln"), T(px + 71, py + 88, name, "sm b")]
    F["shapes"] = fig(650, 216, "\n".join(g),
        "Eight small histograms showing bell-shaped, uniform, J, reverse J, right-skewed, left-skewed, bimodal and U-shaped distributions",
        "The eight shapes both decks list. Skew is named after the tail, not the peak: a right-skewed histogram peaks on the left and trails off to the right. Bimodal means two peaks.",
        "الأشكال الثمانية في المحاضرتين. الالتواء يُسمّى باتجاه <b>الذيل</b> لا القمة: الملتوي لليمين قمته يسارًا وذيله يمتد لليمين. ثنائي المنوال يعني قمتين.")

    # ---------------------------------------------------- bar graphs
    cats = [("Coffee", 29), ("Mocha", 24), ("Latte", 18), ("Tea", 16), ("Espresso", 13)]
    sy = scale(0, 32, 190, 16)
    g = [L(70, 190, 610, 190, "ln"), L(70, 190, 70, 12, "ln"), T(18, 100, "Number of students", "sm b", "middle", ' transform="rotate(-90 18 100)"')]
    for t in range(0, 33, 8):
        g += [T(62, sy(t) + 4, str(t), "sm soft", "end"), L(70, sy(t), 610, sy(t), "ln-soft", ' stroke-opacity="0.35"')]
    for i, (c, f) in enumerate(cats):
        x = 100 + i * 100
        g += [R(x, sy(f), 60, sy(0) - sy(f), "wash1 ln s1"), T(x + 30, sy(f) - 6, str(f), "sm b"), T(x + 30, 208, c, "sm")]
    g.append(T(340, 228, "Hot drink (gaps between bars: categories, not a scale)", "sm b"))
    F["bardrinks"] = fig(640, 234, "\n".join(g),
        "Vertical bar graph of hot drink preferences for 100 students with Coffee highest at 29",
        "Dr. Amani's hot drinks example (n = 100), ordered here from most to least popular. Bars are separated because the x-axis holds categories, not a continuous scale. Coffee is the most preferred drink (29%), espresso the least (13%).",
        "مثال المشروبات لـ د. أماني (n = 100). الأعمدة منفصلة لأن المحور الأفقي تصنيفات لا مقياس متصل. القهوة الأكثر تفضيلًا (29%) والإسبريسو الأقل (13%).")
    spend = [("Electronics", 728), ("Dorm decor", 344), ("Clothing", 141), ("Shoes", 72)]
    sx = scale(0, 800, 130, 620)
    g = []
    for i, (c, v) in enumerate(spend):
        y = 18 + i * 34
        g += [R(130, y, sx(v) - 130, 22, "wash3 ln s3"), T(122, y + 16, c, "sm", "end"), T(sx(v) + 6, y + 16, f"${v}", "sm b", "start")]
    g += axis(sx, 0, 800, 158, range(0, 801, 200), lambda v: f"${v:g}") + [T(375, 196, "Average amount spent by first-year students", "sm b")]
    F["barspend"] = fig(640, 202, "\n".join(g),
        "Horizontal bar graph of first-year college spending with electronics at 728 dollars",
        "Example 2-8 as a horizontal bar graph: identical information to a vertical one, just rotated, and handy when category names are long. Electronics take more than the other three categories combined.",
        "مثال 2-8 كأعمدة أفقية: نفس المعلومة لكن مستدارة، ومفيدة عندما تكون أسماء التصنيفات طويلة. الإلكترونيات أكثر من مجموع البنود الثلاثة الأخرى.")

    sport = [("Football", 13, 6), ("Tennis", 10, 7), ("Basketball", 12, 10), ("Cricket", 5, 14), ("Other", 4, 6)]
    sy = scale(0, 25, 180, 22)
    g = [T(160, 14, "Grouped (side-by-side)", "sm b"), T(480, 14, "Stacked", "sm b")]
    for t in range(0, 26, 5):
        g += [T(32, sy(t) + 4, str(t), "sm soft", "end"), L(36, sy(t), 300, sy(t), "ln-soft", ' stroke-opacity="0.35"'),
              T(352, sy(t) + 4, str(t), "sm soft", "end"), L(356, sy(t), 630, sy(t), "ln-soft", ' stroke-opacity="0.35"')]
    g += [L(36, 180, 300, 180, "ln"), L(356, 180, 630, 180, "ln")]
    for i, (s, m, f) in enumerate(sport):
        x = 44 + i * 52
        g += [R(x, sy(m), 20, sy(0) - sy(m), "wash1 ln s1"), R(x + 20, sy(f), 20, sy(0) - sy(f), "wash4 ln s4"), T(x + 20, 196, s, "sm")]
        x2 = 366 + i * 54
        g += [R(x2, sy(m), 34, sy(0) - sy(m), "wash1 ln s1"), R(x2, sy(m + f), 34, sy(m) - sy(m + f), "wash4 ln s4"), T(x2 + 17, sy(m + f) - 5, str(m + f), "sm b"), T(x2 + 17, 196, s, "sm")]
    g += [R(250, 26, 10, 10, "wash1 ln s1"), T(264, 35, "Males", "sm", "start"), R(250, 42, 10, 10, "wash4 ln s4"), T(264, 51, "Females", "sm", "start")]
    F["compound"] = fig(650, 206, "\n".join(g),
        "Grouped and stacked bar graphs of sport preferences by gender",
        "Dr. Amani's compound bar graph data shown both ways. Grouped bars compare males with females inside each sport (cricket is the only sport where females clearly lead). Stacked bars show each sport's total (basketball 22) while keeping the split.",
        "بيانات د. أماني بالشكلين: الأعمدة المتجاورة تقارن الذكور بالإناث داخل كل رياضة (الكريكيت الوحيدة التي تتفوق فيها الإناث بوضوح)، والأعمدة المكدسة تُظهر المجموع لكل رياضة (كرة السلة 22) مع الاحتفاظ بالتقسيم.")

    # ---------------------------------------------------- pie
    trav = [("Walking", 8), ("Bus", 4), ("Car", 9), ("Cycle", 5), ("Train", 1), ("Taxi", 3)]
    cx, cy, r = 150, 118, 96
    tones = ["1", "2", "3", "4", "A", "2"]
    g = []; a0 = -90
    for (name, f), tn in zip(trav, tones):
        a1 = a0 + f / 30 * 360
        large = 1 if a1 - a0 > 180 else 0
        x0, y0 = cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0))
        x1, y1 = cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1))
        op = ' fill-opacity="0.55"' if tn != "2" or name == "Bus" else ' fill-opacity="0.25"'
        g.append(f'<path d="M{cx},{cy} L{x0:.1f},{y0:.1f} A{r},{r} 0 {large} 1 {x1:.1f},{y1:.1f} z" class="f{tn} ln"{op}/>')
        am = math.radians((a0 + a1) / 2)
        lx, ly = cx + (r + 18) * math.cos(am), cy + (r + 18) * math.sin(am)
        g.append(T(lx, ly + 4, name, "sm b", "start" if math.cos(am) > 0.1 else ("end" if math.cos(am) < -0.1 else "middle")))
        a0 = a1
    rows = [("Walking", 8), ("Bus", 4), ("Car", 9), ("Cycle", 5), ("Train", 1), ("Taxi", 3)]
    g += [T(330, 30, "Method", "sm b", "start"), T(430, 30, "f", "sm b", "end"), T(520, 30, "%  (f/n·100)", "sm b", "end"), T(620, 30, "degrees (f/n·360)", "sm b", "end")]
    for i, (nme, f) in enumerate(rows):
        y = 52 + i * 22
        g += [T(330, y, nme, "sm", "start"), T(430, y, str(f), "m", "end"), T(520, y, f"{f / 30 * 100:.2f}", "m", "end"), T(620, y, f"{f / 30 * 360:g}°", "m", "end")]
    g += [L(330, 186, 630, 186, "ln-soft"), T(330, 204, "Total", "sm b", "start"), T(430, 204, "30", "m b", "end"), T(520, 204, "100", "m b", "end"), T(620, 204, "360°", "m b", "end")]
    F["pie"] = fig(650, 224, "\n".join(g),
        "Pie chart of how 30 children travel to school with its percentage and degree table",
        "Dr. Amani's pie example, completed. Each angle is f/n × 360°, each percentage f/n × 100; the angles must add to 360° and the percentages to 100. Car (30%) and walking (26.7%) together cover more than half the class.",
        "مثال الدائرة لـ د. أماني محلولًا: الزاوية = f/n × 360، والنسبة = f/n × 100، ومجموع الزوايا 360 ومجموع النسب 100. السيارة (30%) والمشي (26.7%) معًا أكثر من نصف الفصل.")

    # ---------------------------------------------------- time series (2 panels)
    def tseries(xs, ys, px, W, ylo, yhi, ystep, title, tone):
        sx = scale(xs[0], xs[-1], px + 46, px + W - 14); sy = scale(ylo, yhi, 170, 24)
        g = [L(px + 40, 170, px + W - 8, 170, "ln"), L(px + 40, 170, px + 40, 18, "ln"), T(px + W / 2, 12, title, "sm b")]
        t = ylo
        while t <= yhi + 1e-9:
            g += [T(px + 36, sy(t) + 4, f"{t:g}", "sm soft", "end"), L(px + 40, sy(t), px + W - 8, sy(t), "ln-soft", ' stroke-opacity="0.35"')]
            t = round(t + ystep, 6)
        g.append(P([(sx(a), sy(b)) for a, b in zip(xs, ys)], f"ln thick s{tone}"))
        for a, b in zip(xs, ys):
            g += [C(sx(a), sy(b), 3.5, f"f{tone}"), T(sx(a), 186, str(a)[2:] if len(xs) > 6 else str(a), "sm")]
        return g
    g = tseries([2010, 2011, 2012, 2013, 2014, 2015], [1.40, 1.55, 1.61, 1.65, 1.78, 1.90], 0, 320, 1.3, 2.0, .1, "Academy Awards ad cost ($ millions)", "1")
    g += tseries(list(range(2014, 2022)), [23, 61, 41, 149, 165, 375, 341, 377], 330, 320, 0, 400, 100, "Omani PhD students (year '14–'21)", "4")
    g.append(P([(76, 174), (80, 166), (84, 174), (88, 166)], "ln"))
    F["timeseries"] = fig(650, 196, "\n".join(g),
        "Two time series line graphs: steadily rising advertising cost, and Omani PhD student numbers with a jump in 2019",
        "Left, Example 2-10: a steady upward trend, the cost rising every year (the y-axis starts at 1.3, so the zig-zag marks the break). Right, Dr. Amani's activity: overall strong growth, with dips in 2016 and 2020 and the steepest rise from 2018 to 2019 (+210 students).",
        "يسار مثال 2-10: اتجاه صاعد ثابت كل سنة (المحور يبدأ من 1.3). يمين نشاط د. أماني: نمو قوي عمومًا مع انخفاض في 2016 و 2020، وأشد صعود بين 2018 و 2019 (+210 طالب).")
    return F
