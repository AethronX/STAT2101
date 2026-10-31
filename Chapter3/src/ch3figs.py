"""All Chapter 3 diagrams, drawn to scale from the lecture data."""
import math
from ch3lib import *

def build():
    F = {}

    # ---------------------------------------------------------- 3-1 population / sample
    u = "ps"
    g = [R(20, 34, 250, 120, "wash1 ln s1", 6), T(145, 60, "Population", "b t1"),
         T(145, 80, "all individuals or items of interest", "sm soft"),
         T(145, 112, "parameters", "sm b"), T(145, 134, "μ · σ² · σ · p", "m b t1"),
         R(390, 34, 250, 120, "wash2 ln s2", 6), T(515, 60, "Sample", "b t2"),
         T(515, 80, "a subset of the population", "sm soft"),
         T(515, 112, "statistics", "sm b"), T(515, 134, "x̄ · s² · s · p̂", "m b t2"),
         AR(272, 66, 386, 66, u), T(329, 56, "random selection", "sm"),
         AR(386, 124, 272, 124, u), T(329, 146, "inference", "sm")]
    F["popsample"] = fig(660, 170, "\n".join(g),
        "Population with parameters and sample with statistics, linked by random selection and inference",
        "Parameters describe the whole population and use Greek letters; statistics describe a sample and use Latin letters. We select a sample at random, compute a statistic, and use it to infer the parameter.",
        "المعلمة (parameter) تصف المجتمع كله وتُكتب بحروف يونانية، والإحصاءة (statistic) تصف العينة. نسحب عينة عشوائية، نحسب الإحصاءة، ثم نستدل بها على المعلمة.",
        arrow_defs(u))

    # ---------------------------------------------------------- 3-1 median position
    g = []
    d1 = [17.6, 69.8, 108.2, 159.8, 222.6]
    for i, v in enumerate(d1):
        x = 40 + i * 84
        hit = i == 2
        g += [R(x, 30, 76, 30, "wash1 ln s1 thick" if hit else "bg ln-soft", 3), T(x + 38, 50, f"{v:g}", "m b t1" if hit else "m"),
              T(x + 38, 76, f"{i+1}", "sm soft")]
    g += [T(40, 20, "n = 5 (odd): median at position (n + 1)/2 = 3", "sm b", "start"), T(470, 50, "MD = 108.2", "m b t1", "start")]
    d2 = [656, 684, 702, 764, 856, 1132, 1133, 1303]
    for i, v in enumerate(d2):
        x = 40 + i * 54
        hit = i in (3, 4)
        g += [R(x, 118, 50, 30, "wash1 ln s1 thick" if hit else "bg ln-soft", 3), T(x + 25, 138, f"{v}", "m b t1" if hit else "m"),
              T(x + 25, 164, f"{i+1}", "sm soft")]
    g += [T(40, 108, "n = 8 (even): average positions n/2 = 4 and n/2 + 1 = 5", "sm b", "start"),
          T(484, 138, "MD = (764 + 856)/2 = 810", "m b t1", "start")]
    F["median"] = fig(700, 174, "\n".join(g),
        "Ordered data with the middle value highlighted for an odd count and the two middle values for an even count",
        "Order the data first. Odd n: the median is the single middle value (Example 3-4). Even n: it is the mean of the two middle values (Example 3-5). The number under each box is its position.",
        "رتّب البيانات أولًا. إذا كان n فرديًا فالوسيط هو القيمة الوسطى (مثال 3-4)، وإذا كان زوجيًا فهو متوسط القيمتين الوسطيين (مثال 3-5). الرقم تحت كل مربع هو ترتيبه.")

    # ---------------------------------------------------------- 3-1 outlier pulls the mean
    sx = scale(0, 110, 40, 620)
    g = axis(sx, 0, 110, 78, range(0, 111, 10), lambda v: f"{v:g}k")
    for v, k in ((18, 0), (18, 1), (24, 0), (40, 0), (100, 0)):
        g.append(C(sx(v), 64 - k * 13, 5.5, "f1"))
    g += [T(sx(100), 46, "owner", "sm soft"), T(sx(18), 34, "2 technicians", "sm soft")]
    for v, lab, row, cls in ((18, "Mode = 18k", 0, "t3"), (24, "Median = 24k", 1, "t2"), (40, "Mean = 40k", 2, "tA")):
        y = 116 + row * 18
        g += [L(sx(v), 96, sx(v), y - 11, "ln-soft dash"), T(sx(v) + 4, y, lab, f"sm b {cls}", "start")]
    g += [T(sx(70), 24, "one 100k salary drags the mean to the right →", "sm b tA")]
    F["outlier"] = fig(660, 158, "\n".join(g),
        "Five salaries on a number line: the mean of 40 thousand sits far right of the median and mode because of one 100 thousand salary",
        "Example 3-11. One extreme salary pulls the mean up to 40k while the median (24k) and mode (18k) stay with the typical workers. With outliers or skew, report the median.",
        "مثال 3-11: راتب واحد كبير (100 ألف) يسحب المتوسط إلى 40 ألفًا، بينما يبقى الوسيط (24 ألفًا) والمنوال (18 ألفًا) قريبين من رواتب أغلب العاملين. مع القيم المتطرفة أو الالتواء نستخدم الوسيط.")

    # ---------------------------------------------------------- 3-1 distribution shapes
    def lognorm(x, mu=1.0, s=0.62):
        return 0 if x <= 0 else math.exp(-(math.log(x) - mu) ** 2 / (2 * s * s)) / (x * s * math.sqrt(2 * math.pi))
    mode, med, mean = math.exp(1 - .62 ** 2), math.exp(1), math.exp(1 + .62 ** 2 / 2)
    peak = lognorm(mode)
    def panel(px, kind):
        out = [L(px + 8, 150, px + 202, 150, "ln")]
        dom = 8.0
        def X(t): return px + 10 + t / dom * 190
        def f(t):
            if kind == "pos": return lognorm(t) / peak
            if kind == "neg": return lognorm(dom - t) / peak
            return math.exp(-((t - 4) ** 2) / (2 * 1.15 ** 2))
        pts = [(X(i * dom / 200), 150 - 92 * f(i * dom / 200)) for i in range(201)]
        out.append(P(pts, "ln thick"))
        if kind == "sym":
            out += [L(X(4), 150, X(4), 58, "ln-soft dash"), T(X(4), 50, "mean = median = mode", "sm b")]
        else:
            marks = [("Mode", mode, "t3"), ("Median", med, "t2"), ("Mean", mean, "tA")]
            if kind == "neg":
                marks = [(n, dom - v, c) for n, v, c in marks]
            for i, (n, v, c) in enumerate(marks):
                ytop = 150 - 92 * f(v)
                ly = 22 + i * 16
                out += [L(X(v), 150, X(v), ytop, "ln-soft dash"), L(X(v), ytop, X(v), ly + 3, "ln-soft"),
                        T(X(v) + (4 if kind == "pos" else -4), ly, n, f"sm b {c}", "start" if kind == "pos" else "end")]
        title, order = {"neg": ("Negatively (left) skewed", "mean < median < mode"),
                        "sym": ("Symmetric", "mean = median = mode"),
                        "pos": ("Positively (right) skewed", "mode < median < mean")}[kind]
        out += [T(px + 105, 170, title, "sm b"), T(px + 105, 187, order, "m")]
        return out
    g = panel(10, "neg") + panel(235, "sym") + panel(460, "pos")
    F["shapes"] = fig(680, 196, "\n".join(g),
        "Three distribution curves showing where the mean, median and mode fall for left-skewed, symmetric and right-skewed data",
        "The mean is pulled toward the long tail; the mode stays at the peak; the median sits between them. Read the shape from the order of the three measures.",
        "المتوسط ينسحب نحو الذيل الطويل، والمنوال يبقى عند القمة، والوسيط بينهما. من ترتيب المقاييس الثلاثة نعرف شكل التوزيع.")

    # ---------------------------------------------------------- 3-2 clinics
    sx = scale(4, 10.5, 70, 640)
    A = [6.5, 6.6, 6.7, 6.8, 7.1, 7.3, 7.4, 7.7, 7.7, 7.7]
    B = [4.2, 5.4, 5.8, 6.2, 6.7, 7.7, 7.7, 8.5, 9.3, 10.0]
    g = axis(sx, 4, 10.5, 150, [4, 5, 6, 7, 8, 9, 10])
    for row, (name, d, tone, y) in enumerate((("Clinic A", A, "2", 56), ("Clinic B", B, "3", 116))):
        seen = {}
        for v in d:
            k = seen.get(v, 0); seen[v] = k + 1
            g.append(C(sx(v), y - k * 10, 4, f"f{tone}"))
        g.append(T(20, y + 4, name, f"sm b t{tone}", "start"))
        g += bracket(sx(min(d)), sx(max(d)), y + 14, "", "sm b", up=False)[:3]
        g.append(T(sx(max(d)) + 8, y + 18, f"range = {max(d) - min(d):.1f}", "sm b", "start"))
    g += [L(sx(7.15), 22, sx(7.15), 150, "ln sA dash"), T(sx(7.15), 16, "mean = 7.15 for both", "sm b tA")]
    F["clinics"] = fig(660, 176, "\n".join(g),
        "Dot plots of waiting times at two clinics with the same mean of 7.15 minutes but very different spreads",
        "Same mean, median, mode and midrange, but clinic B's waiting times are spread almost five times wider. The centre alone cannot tell the clinics apart; a measure of variation can.",
        "نفس المتوسط والوسيط والمنوال ومنتصف المدى للعيادتين، لكن أوقات الانتظار في العيادة B مشتّتة أكثر بكثير. مقاييس النزعة المركزية وحدها لا تكفي، ونحتاج مقاييس التشتت.")

    # ---------------------------------------------------------- 3-2 deviations
    sx = scale(0, 70, 60, 440)
    data = [10, 60, 50, 30, 40, 20]
    g = axis(sx, 0, 70, 176, range(0, 71, 10))
    g += [L(sx(35), 14, sx(35), 176, "ln sA dash"), T(sx(35), 10, "μ = 35", "sm b tA")]
    for i, v in enumerate(data):
        y = 30 + i * 23
        dv = v - 35
        g += [L(sx(35), y, sx(v), y, f"ln thick s{'2' if dv > 0 else '3'}"), C(sx(v), y, 4.5, "f2" if dv > 0 else "f3"),
              T(sx(v) + (10 if dv > 0 else -10), y + 4, f"{dv:+d}", "m b", "start" if dv > 0 else "end"),
              T(30, y + 4, str(v), "m", "end")]
    g += [T(470, 46, "Σ(X − μ) = 0", "m b", "start"), T(470, 70, "squares:", "sm soft", "start"),
          T(470, 88, "625+625+225+25+25+225", "m", "start"), T(470, 108, "Σ(X − μ)² = 1750", "m b", "start"),
          T(470, 136, "σ² = 1750 / 6 ≈ 291.7", "m b t2", "start"), T(470, 158, "σ = √291.7 ≈ 17.1", "m b t2", "start")]
    F["deviations"] = fig(660, 200, "\n".join(g),
        "Each paint lifetime drawn as a bar from the mean of 35 to its value, with positive and negative deviations",
        "Example 3-18 (brand A paint). Each bar is a deviation X − μ. They cancel to zero, which is why we square them before averaging; the average squared deviation is the variance.",
        "مثال 3-18: كل خط يمثل انحراف القيمة عن المتوسط. مجموع الانحرافات = صفر دائمًا، لذلك نربّعها قبل أخذ المتوسط، ومتوسط مربعات الانحرافات هو التباين.")

    # ---------------------------------------------------------- 3-2 Chebyshev
    sx = scale(16, 40, 50, 620)
    g = axis(sx, 16, 40, 120, [19, 22, 25, 28, 31, 34, 37])
    for t, lab in zip([19, 22, 25, 28, 31, 34, 37], ["x̄−3s", "x̄−2s", "x̄−s", "x̄", "x̄+s", "x̄+2s", "x̄+3s"]):
        g.append(T(sx(t), 156, lab, "sm soft"))
    g += [R(sx(22), 82, sx(34) - sx(22), 30, "wash2"), R(sx(19), 92, sx(22) - sx(19), 20, "wash3"),
          R(sx(34), 92, sx(37) - sx(34), 20, "wash3")]
    g += bracket(sx(22), sx(34), 70, "k = 2: at least 1 − 1/4 = 75%  (≥ 38 of 50)", "sm b t2")
    g += bracket(sx(19), sx(37), 36, "k = 3: at least 1 − 1/9 ≈ 88.89%", "sm b t3")
    F["cheb"] = fig(660, 166, "\n".join(g),
        "Number line around a mean of 28 with standard deviation 3, showing nested intervals for k equal to 2 and 3",
        "Dr. Amani's activity: n = 50, x̄ = 28, s = 3. The interval (22, 34) is x̄ ± 2s, so at least 75% (37.5, so at least 38 observations) lie inside, whatever the shape of the data.",
        "نشاط د. أماني: n = 50 و x̄ = 28 و s = 3. الفترة (22, 34) هي x̄ ± 2s، إذن 75% على الأقل من البيانات داخلها (أي 38 مشاهدة على الأقل) مهما كان شكل التوزيع.")

    # ---------------------------------------------------------- 3-2 empirical rule
    sx = scale(165, 795, 40, 640)
    pdf = lambda v: math.exp(-((v - 480) / 90) ** 2 / 2)
    def band(a, b, op):
        pts = [(sx(a), 170)] + [(sx(a + (b - a) * i / 80), 170 - 110 * pdf(a + (b - a) * i / 80)) for i in range(81)] + [(sx(b), 170)]
        return PG(pts, "f2", f' fill-opacity="{op}"')
    g = [band(210, 750, .12), band(300, 660, .22), band(390, 570, .38),
         P([(sx(165 + i * 630 / 200), 170 - 110 * pdf(165 + i * 630 / 200)) for i in range(201)], "ln thick")]
    g += axis(sx, 165, 795, 170, [210, 300, 390, 480, 570, 660, 750])
    g += bracket(sx(390), sx(570), 52, "≈ 68%", "sm b t2")
    g += bracket(sx(300), sx(660), 34, "≈ 95%", "sm b t2")
    g += bracket(sx(210), sx(750), 16, "≈ 99.7%", "sm b t2")
    g = [x.replace('y="10.0"', 'y="11.0"') for x in g]
    F["empirical"] = fig(680, 198, "\n".join(g),
        "Bell curve of exam scores with mean 480 and standard deviation 90, shaded within one, two and three standard deviations",
        "The empirical rule holds only for bell-shaped (normal) data. Exam scores with mean 480 and SD 90: about 68% fall in 390–570, 95% in 300–660, 99.7% in 210–750.",
        "القاعدة التجريبية تصلح فقط للبيانات الجرسية (الطبيعية). درجات بمتوسط 480 وانحراف 90: حوالي 68% بين 390 و 570، و95% بين 300 و 660، و99.7% بين 210 و 750.")

    # ---------------------------------------------------------- 3-2 linear transformation
    sx = scale(0, 10, 90, 470)
    g = axis(sx, 0, 10, 176, range(0, 11))
    rows = (("x", [1, 2, 3, 4], 2.5, 1.29, "1"), ("x + 5", [6, 7, 8, 9], 7.5, 1.29, "2"), ("2x", [2, 4, 6, 8], 5, 2.58, "4"))
    for i, (lab, d, m, s, tone) in enumerate(rows):
        y = 34 + i * 50
        g += [T(20, y + 4, lab, f"m b t{tone}", "start")]
        g += [L(sx(m - s), y + 14, sx(m + s), y + 14, f"ln s{tone} thick")]
        g += [C(sx(v), y, 5, f"f{tone}") for v in d]
        g += [PG([(sx(m), y + 9), (sx(m) - 5, y + 19), (sx(m) + 5, y + 19)], f"f{tone}")]
        g += [T(500, y + 4, f"mean {m:g}  ·  SD {s:g}", "m", "start")]
    g += [T(500, 18, "IQR: 2 → 2 → 4", "sm soft", "start")]
    F["lintrans"] = fig(680, 200, "\n".join(g),
        "Three rows of dots: the original data, the data shifted by 5, and the data doubled, with mean and spread marked",
        "Adding 5 slides every point (and the mean, median) right by 5 but leaves the spread (SD, IQR) unchanged. Multiplying by 2 doubles both the centre and the spread. Triangle = mean; bar = mean ± 1 SD.",
        "إضافة 5 تُزيح كل القيم (والمتوسط والوسيط) بمقدار 5 لكن التشتت (SD و IQR) لا يتغير. الضرب في 2 يضاعف مقاييس المركز والتشتت معًا. المثلث = المتوسط، والخط = المتوسط ± انحراف معياري واحد.")

    # ---------------------------------------------------------- 3-3 z-scores
    sz = scale(-3, 3, 110, 610)
    g = []
    for i, (name, mu, sd, x, tone) in enumerate((("English", 76, 4, 85, "1"), ("French", 36, 3, 42, "3"))):
        y = 40 + i * 62
        g += [L(sz(-3), y, sz(3), y, "ln-soft"), T(20, y + 4, name, f"sm b t{tone}", "start")]
        for k in range(-3, 4):
            g += [L(sz(k), y - 4, sz(k), y + 4, "ln-soft"), T(sz(k), y - 9, f"{mu + k * sd:g}", "sm soft")]
        z = (x - mu) / sd
        g += [C(sz(z), y, 6, f"f{tone}"), T(sz(z) + 12, y + 20, f"{x} → z = {z:.2f}", f"m b t{tone}", "start")]
    g += axis(sz, -3, 3, 150, range(-3, 4), lambda v: f"{v:+d}" if v else "0")
    g += [T(sz(0), 184, "z (standard deviations from the mean)", "sm b")]
    F["zscore"] = fig(660, 192, "\n".join(g),
        "Two test scores placed on a common z-score scale: English 85 at z 2.25 and French 42 at z 2.00",
        "Example 3-27. Raw scores 85 and 42 cannot be compared directly. On the common z scale, English (z = 2.25) sits further above its class mean than French (z = 2.00), so English is her better relative position.",
        "مثال 3-27: لا يمكن مقارنة 85 و 42 مباشرة. على مقياس z الموحد، الإنجليزي (z = 2.25) أبعد فوق متوسط فصله من الفرنسي (z = 2.00)، إذن موقعها النسبي في الإنجليزي أفضل.")

    # ---------------------------------------------------------- 3-3 percentile / decile / quartile rulers
    sp = scale(0, 100, 120, 620)
    g = []
    rows = (("Percentiles", 30, [1, 25, 50, 75, 99], lambda p: f"P{p}", range(1, 100), "3"),
            ("Deciles", 80, list(range(10, 100, 10)), lambda p: f"D{p // 10}", range(10, 100, 10), "2"),
            ("Quartiles", 130, [25, 50, 75], lambda p: f"Q{p // 25}", [25, 50, 75], "4"))
    for name, y, labs, fmt, ticks, tone in rows:
        g += [L(sp(0), y, sp(100), y, "ln"), T(20, y + 4, name, f"sm b t{tone}", "start"),
              T(sp(0), y + 18, "min", "sm soft"), T(sp(100), y + 18, "max", "sm soft")]
        for t in ticks:
            g.append(L(sp(t), y - (3 if name == "Percentiles" else 6), sp(t), y + (3 if name == "Percentiles" else 6), "ln"))
        for p in labs:
            g.append(T(sp(p), y - 10, fmt(p), f"sm b t{tone}"))
    for p, lab in ((25, "P25 = Q1"), (50, "P50 = D5 = Q2 = MD"), (75, "P75 = Q3")):
        g += [L(sp(p), y0, sp(p), y1, "ln sA dash") for y0, y1 in ((34, 64), (86, 114), (136, 156))]
        g.append(T(sp(p), 170, lab, "sm b tA"))
    F["rulers"] = fig(660, 178, "\n".join(g),
        "Three aligned rulers dividing ordered data into 100 percentiles, 10 deciles and 4 quartiles, with matching positions linked",
        "Percentiles cut ordered data into 100 parts, deciles into 10, quartiles into 4. They are the same scale: Q1 = P25, the median = P50 = D5 = Q2, Q3 = P75, and each Dk = P(10k).",
        "المئينات تقسم البيانات المرتبة إلى 100 جزء، والعشيرات إلى 10، والربيعات إلى 4. وكلها على نفس المقياس: Q1 = P25، والوسيط = P50 = D5 = Q2، و Q3 = P75.")

    # ---------------------------------------------------------- 3-3 percentile rank and value (Jim's class)
    sc = [34, 37, 48, 59, 62, 75, 76, 78, 79, 80, 82, 85, 90, 91, 92, 92, 94, 97, 99, 100]
    g = [T(30, 20, "Percentile rank of Jim's 78: 7 values below → (7 + 0.5)/20 × 100 = 37.5", "sm b", "start")]
    for i, v in enumerate(sc):
        x = 30 + i * 30
        cls, tcls = ("wash3 ln s3", "m") if i < 7 else (("washA ln sA thick", "m b tA") if i == 7 else ("bg ln-soft", "m soft"))
        g += [R(x, 30, 27, 24, cls, 2), T(x + 13.5, 47, str(v), tcls)]
    g += [T(30, 80, "Value at P74: c = 20 × 74/100 = 14.8 → round up to 15 → 15th value = 92", "sm b", "start"),
          T(30, 98, "Value at P50: c = 10 (whole) → mean of 10th and 11th = (80 + 82)/2 = 81", "sm b", "start")]
    for i, v in enumerate(sc):
        x = 30 + i * 30
        cls = "wash4 ln s4 thick" if i == 14 else ("wash2 ln s2 thick" if i in (9, 10) else "bg ln-soft")
        g += [R(x, 108, 27, 24, cls, 2), T(x + 13.5, 125, str(v), "m"), T(x + 13.5, 146, str(i + 1), "sm soft")]
    F["pctjim"] = fig(640, 154, "\n".join(g),
        "Twenty ordered exam scores with the seven below Jim's 78 shaded, and the 10th, 11th and 15th positions highlighted",
        "Top: count the values strictly below X, add 0.5, divide by n. Bottom: c = n·p/100 gives a position. A decimal c rounds up to one position; a whole c means averaging positions c and c + 1.",
        "أعلى: عُدّ القيم الأقل من X، أضف 0.5، واقسم على n. أسفل: c = n·p/100 يعطي الترتيب؛ إذا كان c عشريًا نقرّبه لأعلى، وإذا كان عددًا صحيحًا نأخذ متوسط القيمتين c و c + 1.")

    # ---------------------------------------------------------- 3-3 outlier fences
    sx = scale(20, 140, 50, 630)
    g = axis(sx, 20, 140, 120, range(20, 141, 20))
    for v in sc:
        g.append(C(sx(v), 96, 3.2, "f3"))
    g += boxplot(sx, 60, (34, 68.5, 81, 92, 100), "3", labels=False)
    g += [T(sx(68.5), 38, "Q1 = 68.5", "sm b"), T(sx(92), 38, "Q3 = 92", "sm b")]
    for v, lab in ((33.25, "Q1 − 1.5·IQR = 33.25"), (127.25, "Q3 + 1.5·IQR = 127.25")):
        g += [L(sx(v), 22, sx(v), 120, "ln sA dash"), T(sx(v), 16, lab, "sm b tA")]
    g += [T(sx(34) + 8, 112, "34 is just inside → not an outlier", "sm tA", "start")]
    F["fences"] = fig(660, 146, "\n".join(g),
        "Twenty scores with their box from Q1 68.5 to Q3 92 and outlier fences at 33.25 and 127.25",
        "IQR = 92 − 68.5 = 23.5, so 1.5·IQR = 35.25. Anything below 33.25 or above 127.25 would be an outlier. The lowest score, 34, misses the fence by 0.75, so there are no outliers.",
        "المدى الربيعي = 23.5، و 1.5 × 23.5 = 35.25. أي قيمة أقل من 33.25 أو أكبر من 127.25 تعتبر قيمة شاذة. أقل درجة 34 داخل الحد بفارق 0.75 فقط، إذن لا توجد قيم شاذة.")

    # ---------------------------------------------------------- 3-4 boxplot anatomy (Dr. Amani's example)
    sx = scale(0, 100, 50, 620)
    five = (7, 39, 49, 61, 90)
    g = axis(sx, 0, 100, 118, range(0, 101, 10)) + boxplot(sx, 72, five, "4", h=34)
    for v, n in zip(five, ("Minimum", "Q1", "Median Q2", "Q3", "Maximum")):
        g.append(T(sx(v), 30, n, "sm b soft"))
    for a, b in zip(five, five[1:]):
        g.append(T((sx(a) + sx(b)) / 2, 100, "25%", "sm t4"))
    g += bracket(sx(39), sx(61), 148, "IQR = Q3 − Q1 = 22", "sm b t4", up=False)
    F["boxanat"] = fig(660, 172, "\n".join(g),
        "Boxplot of Dr. Amani's fifteen values with minimum 7, Q1 39, median 49, Q3 61 and maximum 90, each section holding 25 percent",
        "Five-number summary 7, 39, 49, 61, 90. Each of the four pieces (left whisker, two halves of the box, right whisker) holds 25% of the data, however long it looks.",
        "الملخص الخماسي 7، 39، 49، 61، 90. كل جزء من الأجزاء الأربعة (الخط الأيسر، نصفا الصندوق، الخط الأيمن) يحتوي 25% من البيانات مهما كان طوله.")

    # ---------------------------------------------------------- 3-4 activity boxplot
    sx = scale(0, 60, 50, 620)
    g = axis(sx, 0, 60, 92, range(0, 61, 10)) + boxplot(sx, 52, (5, 12, 22, 36, 53), "4", h=30)
    g += [T(sx(17), 84, "10", "sm soft"), T(sx(29), 84, "14", "sm soft")]
    F["boxact"] = fig(660, 120, "\n".join(g),
        "Boxplot with minimum 5, Q1 12, median 22, Q3 36 and maximum 53",
        "Activity solution. The median sits left of the box centre (10 vs 14 on each side) and the right whisker (17) is longer than the left (7): the data are positively (right) skewed.",
        "حل النشاط: الوسيط يقع يسار منتصف الصندوق (10 مقابل 14)، والخط الأيمن (17) أطول من الأيسر (7)، إذن التوزيع ملتوٍ نحو اليمين (موجب).")

    # ---------------------------------------------------------- 3-4 skewness from boxplots
    g = []
    for i, (title, five, rule) in enumerate((("Left (negatively) skewed", (5, 45, 72, 82, 92), "median right · left whisker longer"),
                                            ("Symmetric", (8, 35, 50, 65, 92), "median centred · whiskers equal"),
                                            ("Right (positively) skewed", (8, 18, 28, 55, 95), "median left · right whisker longer"))):
        px = 15 + i * 222
        sxp = scale(0, 100, px + 8, px + 200)
        g += boxplot(sxp, 44, five, "4", h=28, labels=False)
        g += [T(px + 104, 90, title, "sm b"), T(px + 104, 108, rule, "sm soft")]
    F["skewbox"] = fig(680, 116, "\n".join(g),
        "Three boxplots illustrating left-skewed, symmetric and right-skewed data",
        "Read skewness from two clues: where the median sits inside the box, and which whisker is longer. Both point toward the long tail.",
        "نقرأ الالتواء من دليلين: موقع الوسيط داخل الصندوق، وأي الخطين أطول. وكلاهما يشير إلى جهة الذيل الطويل.")

    # ---------------------------------------------------------- 3-4 meteorites
    sx = scale(0, 300, 50, 620)
    g = axis(sx, 0, 300, 92, range(0, 301, 50)) + boxplot(sx, 52, (30, 47, 83.5, 164, 296), "4", h=30)
    F["meteor"] = fig(660, 120, "\n".join(g),
        "Boxplot of meteorites found with minimum 30, Q1 47, median 83.5, Q3 164, maximum 296",
        "Example 3-37. The median is close to Q1 and the right whisker is far longer than the left: positively (right) skewed.",
        "مثال 3-37: الوسيط قريب من Q1 والخط الأيمن أطول بكثير من الأيسر، إذن التوزيع ملتوٍ نحو اليمين.")

    # ---------------------------------------------------------- 3-4 wood vs steel
    sx = scale(20, 130, 110, 630)
    g = axis(sx, 20, 130, 158, range(20, 131, 10))
    g += [T(20, 54, "Wooden", "sm b t2", "start")] + boxplot(sx, 50, (35, 49, 58, 67.5, 72), "2", h=28)
    g += [T(20, 124, "Steel", "sm b t4", "start")] + boxplot(sx, 120, (28, 51.5, 85, 104, 120), "4", h=28)
    F["woodsteel"] = fig(660, 186, "\n".join(g),
        "Side-by-side boxplots of wooden and steel roller coaster speeds on a shared scale",
        "Example 3-38 on one scale. Steel coasters have a much higher median (85 vs 58), a much larger IQR (52.5 vs 18.5) and range, and are negatively skewed; wooden coasters are about symmetric.",
        "مثال 3-38 على مقياس واحد: الوسيط للحديدية أعلى بكثير (85 مقابل 58)، ومداها الربيعي ومداها أكبر بكثير، وتوزيعها ملتوٍ لليسار، بينما الخشبية متماثلة تقريبًا.")

    return F
