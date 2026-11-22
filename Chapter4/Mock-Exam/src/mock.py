"""Chapter 4 mock exam in SQU midterm format, with answers + marking scheme. Every number is computed here."""
import sys, json, os
from fractions import Fraction as Fr
from math import comb as C, perm as P, factorial as F
sys.path.insert(0, "/tmp/claude-0/-home-user-STAT2101/521e5d47-fbd3-5206-8b60-93d1c3cc1629/scratchpad/ch3")
from ch3lib import head

OUT = "/home/user/STAT2101/Chapter4/Mock-Exam"; os.makedirs(OUT + "/html", exist_ok=True)

def fr(n, d=1):
    f = Fr(n, d); v = float(f)
    s = f"{v:.4f}".rstrip("0").rstrip(".")
    if f.denominator == 1: return s
    raw = f"{n}/{d}"
    simp = f"{f.numerator}/{f.denominator}"
    return (f"{raw} = " if raw != simp and d != 1 else "") + f"{simp} ≈ {s}"
def dv(x, k=4): return f"{x:.{k}f}".rstrip("0").rstrip(".")
def tb(h, rows, cls=""):
    hh = "".join(f"<th>{c}</th>" for c in h)
    b = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="xt {cls}"><thead><tr>{hh}</tr></thead><tbody>{b}</tbody></table>'

# ------------------------------------------------------------------ data
dice = [(a, b) for a in range(1, 7) for b in range(1, 7)]
cnt = lambda f: sum(1 for a, b in dice if f(a, b))
T1 = {"Science": (24, 30, 6), "Engineering": (21, 35, 14), "Economics": (15, 35, 20)}
row = {k: sum(v) for k, v in T1.items()}; col = [sum(v[i] for v in T1.values()) for i in range(3)]; N1 = sum(row.values())
assert N1 == 200 and Fr(row["Engineering"], N1) * Fr(col[1], N1) == Fr(T1["Engineering"][1], N1)
ph = {"Samsung": 10, "Apple": 7, "Huawei": 5, "Xiaomi": 3}; N2 = sum(ph.values()); S2 = C(N2, 4)
ab = [("0", 22), ("1", 25), ("2", 18), ("3", 10), ("4 or more", 5)]; N3 = sum(f for _, f in ab)

# Each part: (label, pts, question, answer, working-list, explanation-ar, trap)
QS = []
def Qn(num, part, pts, title, stem, parts): QS.append(dict(num=num, part=part, pts=pts, title=title, stem=stem, parts=parts))

# ================================================================ Q1
E, Hc, L = row["Engineering"], col[1], col[0]
Qn(1, "A", 7, "4-1 · 4-2 · 4-3",
   "A researcher surveyed <b>200 SQU students</b> from three colleges about where they prefer to study. The results are shown below.",
   [])
QS[-1]["table"] = tb(["College", "Library (L)", "Home (H)", "Café (F)"], [[f"{k} ({k[0] if k!='Economics' else 'C'})", *v] for k, v in T1.items()])
QS[-1]["lead"] = "A student is picked at random. Find the probability that the student:"
QS[-1]["parts"] = [
 ("a", 2, "is from the College of Engineering <b>or</b> prefers to study at home.",
  fr(E + Hc - 35, N1),
  [f"Engineering and Home are <b>not</b> mutually exclusive (35 students are both), so use addition rule 2.",
   f"P(E ∪ H) = P(E) + P(H) − P(E ∩ H) = 70/200 + 100/200 − 35/200 = 135/200 = 0.675"],
  "«أو» تعني الجمع، ولأن بينهما تداخلًا (35 طالبًا) نطرح التقاطع مرة واحدة.",
  "Adding 70 + 100 without subtracting 35 gives 170/200, which counts 35 students twice."),
 ("b", 1, "is from the College of Science <b>and</b> does not prefer the library.",
  fr(36, N1),
  ["\"And\" in a table means cells inside the Science row: Home + Café = 30 + 6 = 36.", "P = 36/200 = 0.18"],
  "«و» في الجدول = خلايا داخل صف العلوم فقط، والمقام هو المجموع الكلي.",
  "Using 1 − 24/60: that answers a conditional question (given Science), not \"and\"."),
 ("c", 1, "prefers the library, <b>given that</b> the student is from the College of Economics.",
  fr(15, 70),
  ["\"Given Economics\" shrinks the sample space to the Economics row (70 students).", "P(L | C) = 15/70 = 3/14 ≈ 0.2143"],
  "«بشرط» تجعل المقام مجموع صف الشرط (70) وليس 200.",
  "Dividing by 200 (that is P(L and C)) or by 60 (that is P(C | L))."),
 ("d", 1, "is from the College of Science, <b>given that</b> the student prefers the café.",
  fr(6, 40),
  ["Condition: Café column, total 40.", "P(S | F) = 6/40 = 0.15"],
  "الشرط هنا العمود (المقهى) فالمقام 40.",
  "Reversing the condition: P(F | S) = 6/60 = 0.1 is a different question."),
 ("e", 1, "Are the events \"Engineering\" and \"Home\" independent? Justify.",
  "Independent",
  ["P(E) · P(H) = (70/200)(100/200) = 0.35 × 0.5 = 0.175", "P(E ∩ H) = 35/200 = 0.175. They are equal, so E and H are independent.",
   "Equivalently, P(H | E) = 35/70 = 0.5 = P(H)."],
  "الاستقلال: نقارن P(E∩H) مع حاصل ضرب P(E)·P(H). إذا تساويا فهما مستقلان.",
  "Answering with \"they overlap, so they are dependent\": overlap is about mutual exclusivity, not independence."),
 ("f", 1, "Are the events \"Science\" and \"Café\" mutually exclusive? Justify.",
  "No",
  ["P(S ∩ F) = 6/200 ≠ 0: six students are both, so they can occur together."],
  "المتنافيان لا يقعان معًا؛ هنا 6 طلاب في الخليتين معًا، إذن ليسا متنافيين.",
  "Mixing up mutually exclusive with independent."),
]

nb = C(N2 - 7, 4); eh = C(5, 1) * C(N2 - 5, 3); sa = C(10, 2) * C(7, 2)
Qn(1, "B", 5, "4-4 · 4-5",
   f"In a phone shop, 10 customers bought Samsung, 7 bought Apple, 5 bought Huawei and 3 bought Xiaomi phones (each customer bought only one phone). If <b>4 customers are selected at random</b>,",
   [
 ("a", 1, "find how many ways that <b>none</b> of them bought an Apple phone.",
  f"{nb:,}",
  [f"Total customers = 10 + 7 + 5 + 3 = {N2}; non-Apple = {N2 - 7}.", f"Order doesn't matter, so choose 4 of the {N2 - 7}: ₁₈C₄ = {nb:,} ways."],
  "«ولا واحد اشترى Apple» يعني أن الأربعة كلهم من غير Apple، أي ₁₈C₄.",
  "Writing 18 × 17 × 16 × 15 (a permutation): the four customers form a group, so order doesn't matter."),
 ("b", 2, "find the probability that <b>one</b> of them bought a Huawei phone.",
  fr(eh, S2),
  [f"n(S) = ₂₅C₄ = {S2:,}.", f"\"One of them\" means exactly one: 1 Huawei <b>and</b> 3 non-Huawei = ₅C₁ × ₂₀C₃ = 5 × {C(20, 3):,} = {eh:,}.",
   f"P = {eh:,}/{S2:,} = 114/253 ≈ 0.4506"],
  "«واحد منهم» = واحد بالضبط: نختار 1 من 5 و 3 من الباقين (20)، ونضرب.",
  "Writing 5/25, or forgetting to choose the other 3 customers from the non-Huawei 20."),
 ("c", 1, "find the probability that <b>at least one</b> of them bought an Apple phone.",
  fr(S2 - nb, S2),
  [f"Complement of part (a): P = 1 − {nb:,}/{S2:,} = {S2 - nb:,}/{S2:,} ≈ {dv((S2 - nb) / S2)}"],
  "«على الأقل واحد» = 1 − «ولا واحد»، ونستفيد من نتيجة الفرع (a).",
  "Adding exactly 1, 2, 3, 4 Apple cases: correct but long, and easy to slip."),
 ("d", 1, "find the probability that 2 bought Samsung <b>and</b> 2 bought Apple.",
  fr(sa, S2),
  [f"₁₀C₂ × ₇C₂ = 45 × 21 = {sa}.", f"P = {sa}/{S2:,} ≈ {dv(sa / S2)}"],
  "من كل فئة نختار بالتوافيق ثم نضرب لأن الشرطين معًا («و»).",
  "Adding 45 + 21 instead of multiplying."),
])

# ================================================================ Q2
s9 = [(a, b) for a, b in dice if a + b == 9]
ge10 = cnt(lambda a, b: a + b >= 10); dbl = 6; both = cnt(lambda a, b: a + b >= 10 and a == b)
Qn(2, "A", 6, "4-1 · 4-2 · 4-3", "Two fair dice are rolled.", [
 ("a", 1, "Write the event A = \"the sum is 9\" using set notation and find P(A).",
  fr(4, 36),
  ["n(S) = 6 × 6 = 36 equally likely ordered pairs.", "A = {" + ", ".join(f"({a},{b})" for a, b in s9) + "}, n(A) = 4.", "P(A) = 4/36 = 1/9 ≈ 0.1111"],
  "اكتب الحدث بصيغة المجموعات كما يطلب الدكتور، ثم ⟦n(A)/n(S)⟧.",
  "Treating (3,6) and (6,3) as one outcome: the dice are different, so order counts."),
 ("b", 2, "Find the probability that the sum is <b>at least 10</b> or the two dice show the same number (doubles).",
  fr(ge10 + dbl - both, 36),
  [f"Sum ≥ 10: (4,6) (5,5) (6,4) (5,6) (6,5) (6,6) → {ge10} outcomes. Doubles: 6 outcomes.",
   f"Both: (5,5), (6,6) → {both}. Not mutually exclusive, so P = (6 + 6 − 2)/36 = 10/36 = 5/18 ≈ 0.2778"],
  "«على الأقل 10» تشمل 10 و 11 و 12. وبما أن (5,5) و (6,6) في الحدثين نطرحهما مرة.",
  "Taking \"at least 10\" as sums 11 and 12 only, or forgetting the overlap."),
 ("c", 1, "Find the probability that the sum is <b>not</b> 7.",
  fr(30, 36),
  ["P(sum = 7) = 6/36. Complement: 1 − 6/36 = 30/36 = 5/6 ≈ 0.8333"],
  "«ليس» = المتمّمة: ⟦1 − P(E)⟧.", "Counting the 30 outcomes one by one: correct but slow."),
 ("d", 1, "Are the events \"the sum is 7\" and \"doubles\" mutually exclusive? Justify.",
  "Yes",
  ["Doubles have even sums (2, 4, …, 12), so no double gives 7: the intersection is ∅."],
  "لا يوجد زوج متشابه مجموعه 7، فالتقاطع فارغ، إذن متنافيان.", "Saying \"independent\": that is a different idea."),
 ("e", 1, "Given that the sum is 8, find the probability that the first die shows 3.",
  fr(1, 5),
  ["Reduced sample space: sum 8 = {(2,6), (3,5), (4,4), (5,3), (6,2)}, 5 outcomes.", "Only (3,5) has first die 3: P = 1/5 = 0.2.",
   "By formula: P(first 3 ∩ sum 8)/P(sum 8) = (1/36)/(5/36) = 1/5."],
  "الشرط يصغّر فضاء العينة إلى النتائج الخمس التي مجموعها 8.", "Answering 1/6 (ignoring the condition) or 1/36."),
])
Qn(2, "B", 5, "4-1",
   f"The number of absences of <b>{N3} STAT 2101 students</b> last semester is shown below. A student is selected at random.",
   [
 ("a", 1, "Find the probability that the student had exactly 2 absences.", fr(18, N3), [f"Empirical probability f/n = 18/{N3} = 0.225"], "الاحتمال التجريبي = التكرار ÷ المجموع.", "Using n(S) = 5 classes as if they were equally likely."),
 ("b", 1, "Find the probability that the student had <b>at most</b> 1 absence.", fr(47, N3), [f"0 or 1: (22 + 25)/{N3} = 47/80 = 0.5875"], "«على الأكثر 1» تشمل 0 و 1.", "Using 1 only (exactly), or 0 only."),
 ("c", 1, "Find the probability that the student had <b>more than</b> 2 absences.", fr(15, N3), [f"3 and 4-or-more: (10 + 5)/{N3} = 0.1875"], "«أكثر من 2» لا تشمل 2.", "Including the 18 students with exactly 2."),
 ("d", 1, "Find the probability that the student had <b>at least one</b> absence.", fr(58, N3), [f"Complement of 0 absences: 1 − 22/{N3} = 58/80 = 0.725"], "على الأقل واحد = 1 − ولا مرة.", "Adding four classes: correct but slow."),
 ("e", 1, "What type of probability did you use? Give an example of a <b>subjective</b> probability.",
  "Empirical", ["Empirical: it is based on observed frequencies (f/n).",
   "Subjective example: a doctor estimates a 30% chance that a patient needs an operation."],
  "تجريبي لأنه مبني على بيانات مسجلة. الشخصي = تقدير خبير بلا عدّ ولا بيانات.", "Calling it classical: the classes are not equally likely."),
])
QS[-1]["table"] = tb(["Absences", *[a for a, _ in ab], "Total"], [["Students", *[f for _, f in ab], N3]])

# ================================================================ Q3
pa, pb, pu = .45, .35, .62; pi = round(pa + pb - pu, 2)
Qn(3, "A", 5, "4-2 · 4-3", "For two events A and B, P(A) = 0.45, P(B) = 0.35 and P(A ∪ B) = 0.62. Find:", [
 ("a", 1, "P(A ∩ B)", dv(pi), [f"Rearrange addition rule 2: P(A ∩ B) = P(A) + P(B) − P(A ∪ B) = 0.45 + 0.35 − 0.62 = {dv(pi)}"], "نقلب قاعدة الجمع لإيجاد التقاطع.", "Multiplying 0.45 × 0.35: that assumes independence, which isn't given."),
 ("b", 1, "the probability that A occurs but B does not.", dv(pa - pi), [f"P(A ∩ Bᶜ) = P(A) − P(A ∩ B) = 0.45 − {dv(pi)} = {dv(pa - pi)}"], "A فقط = A ناقص المنطقة المشتركة.", "Writing P(A) − P(B)."),
 ("c", 1, "the probability that neither A nor B occurs.", dv(1 - pu), [f"P((A ∪ B)ᶜ) = 1 − 0.62 = {dv(1 - pu)}"], "لا هذا ولا ذاك = متمّمة الاتحاد.", "Writing 1 − P(A) − P(B) = 0.20, which ignores the overlap."),
 ("d", 1, "P(A | B)", fr(18, 35), [f"P(A | B) = P(A ∩ B)/P(B) = {dv(pi)}/0.35 = 18/35 ≈ 0.5143"], "الشرط B في المقام.", "Dividing by P(A)."),
 ("e", 1, "Are A and B independent? Are they mutually exclusive?", "Dependent; not mutually exclusive",
  [f"P(A | B) ≈ 0.5143 ≠ P(A) = 0.45 (or 0.45 × 0.35 = 0.1575 ≠ {dv(pi)}): dependent.", f"P(A ∩ B) = {dv(pi)} ≠ 0: not mutually exclusive."],
  "سؤالان مختلفان: الاستقلال بمقارنة الاحتمال الشرطي، والتنافي بالنظر إلى التقاطع.", "Using one test to answer both questions."),
])
QS[-1]["venn"] = (dv(pa - pi), dv(pi), dv(pb - pi), dv(1 - pu))
r1 = Fr(6, 10) * Fr(5, 9); mix = 2 * Fr(6, 10) * Fr(4, 9); w2 = Fr(6, 10) * Fr(4, 9) + Fr(4, 10) * Fr(3, 9)
Qn(3, "B", 5, "4-3", "A box contains 6 red and 4 white balls. Two balls are drawn one after the other <b>without replacement</b>.", [
 ("a", 1, "Find the probability that both balls are red.", fr(r1.numerator, r1.denominator), ["Dependent draws, multiplication rule 2: (6/10)(5/9) = 30/90 = 1/3 ≈ 0.3333"], "بدون إرجاع: يقل البسط والمقام في السحبة الثانية.", "(6/10)² = 0.36: that is with replacement."),
 ("b", 2, "Find the probability of getting one ball of each colour.", fr(mix.numerator, mix.denominator),
  ["Two orders: red-white or white-red.", "(6/10)(4/9) + (4/10)(6/9) = 24/90 + 24/90 = 48/90 = 8/15 ≈ 0.5333", "Check with combinations: ₆C₁·₄C₁/₁₀C₂ = 24/45 = 8/15 ✓"],
  "«واحدة من كل لون» لها ترتيبان: أحمر ثم أبيض، أو أبيض ثم أحمر.", "Counting only one order, which gives 24/90 (half the answer)."),
 ("c", 1, "Find the probability that the <b>second</b> ball is white.", fr(w2.numerator, w2.denominator),
  ["Two paths end with white: R then W, or W then W.", "(6/10)(4/9) + (4/10)(3/9) = 24/90 + 12/90 = 36/90 = 0.4"],
  "نجمع مسارات الشجرة التي تنتهي بالأبيض. والنتيجة = 4/10، وهذا ليس صدفة.", "Writing 4/9 or 3/9: both ignore what the first draw was."),
 ("d", 1, "If the balls were drawn <b>with replacement</b>, find P(both red).", "0.36", ["Independent draws, multiplication rule 1: (6/10)(6/10) = 0.36"], "مع الإرجاع: السحبتان مستقلتان، فيتكرر نفس الاحتمال.", "Keeping 5/9 from the without-replacement case."),
])
M, Ph, Ch, MP, MC, PC, MPC, NN = 65, 50, 40, 20, 15, 10, 5, 120
al = M + Ph + Ch - MP - MC - PC + MPC
Qn(3, "C", 3, "4-2", f"Of {NN} first-year students, {M} take Math, {Ph} take Physics and {Ch} take Chemistry; {MP} take Math and Physics, {MC} take Math and Chemistry, {PC} take Physics and Chemistry, and {MPC} take all three. A student is chosen at random.", [
 ("a", 2, "Find the probability that the student takes at least one of the three courses.", fr(al, NN),
  [f"Extended addition rule: (65 + 50 + 40 − 20 − 15 − 10 + 5)/120 = {al}/120 ≈ {dv(al / NN)}"],
  "نجمع الثلاثة، نطرح الأزواج، ثم نعيد إضافة الثلاثي.", "Forgetting to add back the 5 who take all three."),
 ("b", 1, "Find the probability that the student takes none of them.", fr(NN - al, NN), [f"1 − {al}/120 = {NN - al}/120 ≈ {dv((NN - al) / NN)}"], "المتمّمة.", "—"),
])

# ================================================================ Q4
H, cH, cN = .55, .20, .70; car = H * cH + (1 - H) * cN
Qn(4, "A", 6, "4-3",
   "At SQU, 55% of students live in the university hostels. <b>Of those</b> living in the hostels, 20% own a car; of those not living in the hostels, 70% own a car. A student is selected at random.", [
 ("a", 1, "Draw a tree diagram for this situation.", "Tree", ["Hostel 0.55 → car 0.20 / no car 0.80; not hostel 0.45 → car 0.70 / no car 0.30.", "Each branch pair sums to 1."], "الفرع الأول: السكن، والثاني: السيارة بشرط السكن.", "Putting 0.20 on the first level: it is conditional, so it belongs on the second level."),
 ("b", 1, "Find the probability that the student lives in the hostel <b>and</b> owns a car.", dv(H * cH), ["Multiplication rule 2: P(H) · P(car | H) = 0.55 × 0.20 = 0.11"], "«من بين هؤلاء» تعني احتمالًا شرطيًا، فنضرب على طول الفرع.", "Answering 0.20, which is P(car | H)."),
 ("c", 2, "Find the probability that the student owns a car.", dv(car), ["Add the two paths that end in \"car\": 0.11 + 0.45 × 0.70 = 0.11 + 0.315 = 0.425"], "نجمع كل المسارات المنتهية بـ «سيارة».", "Averaging 0.20 and 0.70."),
 ("d", 1, "Given that the student owns a car, find the probability that he or she lives in the hostel.", dv(H * cH / car), [f"P(H | car) = P(H ∩ car)/P(car) = 0.11/0.425 ≈ {dv(H * cH / car)}"], "السؤال المعكوس: نقسم المسار على مجموع المسارات.", "Answering 0.20 or 0.55."),
 ("e", 1, "Are the events \"lives in hostel\" and \"owns a car\" independent? Justify.", "Dependent", ["P(car | H) = 0.20 ≠ P(car) = 0.425."], "الاحتمال الشرطي لا يساوي العادي، إذن تابعان.", "—"),
])
f4 = .92 ** 4; ex1 = .8 * .3 + .2 * .7
Qn(4, "B", 6, "4-3 · 4-5", "Answer the following.", [
 ("a", 1, "A machine has 4 components that work independently; each fails with probability 0.08. Find P(all four work).", dv(f4), ["Multiplication rule 1: 0.92⁴ ≈ 0.7164"], "المكونات مستقلة فنضرب احتمال العمل أربع مرات.", "0.08⁴: that is P(all fail)."),
 ("b", 1, "For the same machine, find P(at least one component fails).", dv(1 - f4), [f"1 − 0.92⁴ ≈ {dv(1 - f4)}"], "على الأقل واحد = 1 − ولا واحد.", "4 × 0.08 = 0.32."),
 ("c", 1, "A coin is tossed and a die is rolled. Find P(tail and a number greater than 4).", fr(1, 6), ["Independent: (1/2)(2/6) = 1/6 ≈ 0.1667"], "أداتان منفصلتان = مستقلتان.", "Adding instead of multiplying."),
 ("d", 1, "A and B are independent with P(A) = 0.3 and P(B) = 0.5. Find P(A ∪ B).", "0.65", ["P(A ∩ B) = 0.3 × 0.5 = 0.15; P(A ∪ B) = 0.3 + 0.5 − 0.15 = 0.65"], "الاستقلال يعطي التقاطع، وقاعدة الجمع ما زالت مطلوبة.", "0.3 + 0.5 = 0.8."),
 ("e", 1, "Ali passes Statistics with probability 0.8 and Math with probability 0.7, independently. Find P(he passes exactly one).", dv(ex1), ["Stat only + Math only = 0.8 × 0.3 + 0.2 × 0.7 = 0.24 + 0.14 = 0.38"], "«بالضبط واحدة» لها حالتان، نجمعهما.", "Computing only one case."),
 ("f", 1, "Two cards are drawn from a standard deck without replacement. Find P(both are aces).", fr(12, 2652), ["(4/52)(3/51) = 12/2652 = 1/221 ≈ 0.0045"], "بدون إرجاع: 3 آسات من 51 في السحبة الثانية.", "(4/52)² = 1/169 (with replacement)."),
])

# ================================================================ Q5
Qn(5, "A", 6, "4-4", "Answer the following counting questions.", [
 ("a", 1, "A car plate has 3 letters (A–Z) followed by 3 digits (0–9), repetition allowed. How many plates are possible?", f"{26 ** 3 * 10 ** 3:,}", ["Fundamental counting rule: 26³ × 10³ = 17,576 × 1,000 = 17,576,000"], "مع التكرار: نفس العدد في كل خانة.", "Using 26 + 10."),
 ("b", 1, "How many plates are possible if no letter and no digit may repeat?", f"{26 * 25 * 24 * 10 * 9 * 8:,}", ["26 × 25 × 24 × 10 × 9 × 8 = 15,600 × 720 = 11,232,000"], "بدون تكرار: ينقص العدد واحدًا في كل خانة.", "—"),
 ("c", 1, "In how many ways can a president, a vice-president and a secretary be chosen from 12 club members?", f"{P(12, 3):,}", ["Distinct offices, order matters: ₁₂P₃ = 12 × 11 × 10 = 1,320"], "مناصب مختلفة = تباديل.", "₁₂C₃ = 220 is a committee without titles."),
 ("d", 1, "In how many ways can a committee of 4 be chosen from the 12 members?", f"{C(12, 4)}", ["No titles, order doesn't matter: ₁₂C₄ = 495"], "لجنة بلا مناصب = توافيق.", "₁₂P₄ = 11,880."),
 ("e", 2, "How many different arrangements of the letters of the word SALALAH are there? How many of them begin with H?", f"{F(7) // (F(3) * F(2))}; {F(6) // (F(3) * F(2))}",
  ["7 letters: A ×3, L ×2, S, H. Permutation rule 2: 7!/(3! 2!) = 5040/12 = 420", "Fix H first; arrange S, A, L, A, L, A: 6!/(3! 2!) = 720/12 = 60"],
  "نقسم على مضروب عدد التكرار لكل حرف متكرر.", "Forgetting to divide by 2! for the two L's."),
])
nS = C(14, 5)
Qn(5, "B", 6, "4-5", "A committee of 5 people is to be chosen at random from 8 men and 6 women.", [
 ("a", 2, "Find the probability that exactly 3 women are chosen.", fr(C(6, 3) * C(8, 2), nS), [f"n(S) = ₁₄C₅ = {nS:,}.", f"n(E) = ₆C₃ × ₈C₂ = 20 × 28 = 560.", f"P = 560/{nS:,} = 40/143 ≈ 0.2797"], "3 نساء و 2 رجال: نضرب التوافيق ثم نقسم على الكل.", "Using ₆C₃/₁₄C₅, which forgets to choose the 2 men."),
 ("b", 1, "Find the probability that at least one man is chosen.", fr(nS - C(6, 5), nS), [f"1 − P(all women) = 1 − ₆C₅/₁₄C₅ = 1 − 6/{nS:,} ≈ {dv(1 - 6 / nS)}"], "المتمّمة: كلهم نساء.", "—"),
 ("c", 1, "Find the probability that a particular man, Salim, is on the committee.", fr(C(13, 4), nS), [f"Salim is in; choose 4 of the other 13: ₁₃C₄ = {C(13, 4)}. P = {C(13, 4)}/{nS:,} = 5/14 ≈ 0.3571", "Check: 5 seats among 14 people = 5/14 ✓"], "نثبّت سالم ثم نختار الباقين.", "—"),
 ("d", 1, "The letters of the word OMAN are arranged at random. Find P(the arrangement starts with a vowel).", fr(12, 24), ["n(S) = 4! = 24. Start with O or A: 2 × 3! = 12. P = 12/24 = 0.5"], "الحرف الأول من حرفين علّة من أصل 4.", "—"),
 ("e", 1, "A 3-digit lottery number (000–999) is drawn at random. Find P(all three digits are different).", "0.72", ["n(S) = 10³ = 1000; n(E) = 10 × 9 × 8 = 720; P = 0.72"], "الكل مع التكرار، والحدث بدون تكرار.", "Using ₁₀C₃: order matters in a number."),
])

assert sum(p[1] for q in QS for p in q["parts"]) == 60, sum(p[1] for q in QS for p in q["parts"])
for q in QS: assert sum(p[1] for p in q["parts"]) == q["pts"], (q["num"], q["part"])
TOT = {n: sum(q["pts"] for q in QS if q["num"] == n) for n in range(1, 6)}

# ================================================================ HTML
CSS = """<style>
body{font-size:12.2px;line-height:1.5}
.paper{max-width:none}
.uni{text-align:center;border-bottom:2px solid var(--fg);padding-bottom:6px;margin-bottom:12px}
.uni .l1{font-family:var(--display);font-size:17px;font-weight:700}
.uni .l2{font-size:12.5px}.uni .l3{font-size:11.5px;color:var(--fg-soft)}
.mock{font-family:var(--mono);font-size:9.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--accent);text-align:center;margin:0 0 10px}
.cover{display:flex;justify-content:space-between;gap:20px;align-items:flex-start;margin:28px 0}
.who p{margin:16px 0}.who span{display:inline-block;border-bottom:1px dotted var(--fg-soft);min-width:220px}
.score{border-collapse:collapse;min-width:200px}.score thead th{background:var(--surface-2)!important;color:var(--fg)!important;text-transform:none;letter-spacing:0}.score td,.score th{border:1px solid var(--fg);padding:5px 12px;font-size:12px;text-align:left}
.center{text-align:center;font-size:14px;margin:30px 0 8px}
.rules{font-size:11.5px;color:var(--fg-soft);border:1px solid var(--rule);border-radius:4px;padding:8px 12px;margin-top:22px}
.rules li{margin:2px 0}
.qh{font-weight:700;margin:0 0 4px}.qh .tag{font-family:var(--mono);font-size:9px;color:var(--fg-faint);font-weight:500;margin-left:8px}
.qblock{margin:0 0 10px}
.xt{border-collapse:collapse;margin:6px auto 8px;font-size:11.5px}.xt th,.xt td{border:1px solid var(--fg);padding:3px 12px;text-align:center}
.xt thead th{background:var(--surface-2);color:var(--fg);font-weight:600;text-transform:none;letter-spacing:0;font-size:11.5px}
.part{margin:6px 0 0;break-inside:avoid}
.space{height:var(--h,92px);border-bottom:1px dotted var(--rule);margin:2px 0 6px}
.pb{break-before:page}
.sol{border:1px solid var(--rule);border-left:4px solid var(--sec,var(--ink-2));border-radius:4px;padding:7px 10px;margin:6px 0;break-inside:avoid;background:var(--surface)}
.sol .shead{display:flex;justify-content:space-between;gap:8px;align-items:baseline}
.sol .fin{font-family:var(--mono);font-weight:700;background:var(--ink-2-wash);padding:1px 6px;border-radius:3px}
.sol ol{margin:4px 0 2px;padding-left:1.3em}.sol li{margin:1px 0}
.sol .ar{font-family:var(--arabic);direction:rtl;text-align:right;color:var(--fg-soft);font-size:11.5px;margin-top:3px}
.sol .trap{font-size:10.8px;color:var(--accent);margin-top:2px}
.pts{font-family:var(--mono);font-size:9.5px;color:var(--fg-faint)}
.sec{border:1px solid var(--rule);border-radius:4px;padding:8px 12px;margin:0 0 10px;background:var(--surface)}
.sec h3{margin:0 0 6px;font-size:13px}
.sec .arx{font-family:var(--arabic);direction:rtl;text-align:right;color:var(--fg-soft)}
.cov td,.cov th{border:1px solid var(--rule);padding:2px 8px;font-size:10.5px}.cov{border-collapse:collapse;width:100%}
.cov thead th{background:var(--surface-2);color:var(--fg);text-transform:none;letter-spacing:0}
</style>"""
HDR = """<div class="uni"><div class="l1">Sultan Qaboos University · College of Science</div>
<div class="l2">Department of Mathematics · STAT 2101 – Introduction to Statistics</div>
<div class="l3">Chapter 4 Review Test: Probability and Counting Rules · Time: 90 minutes</div></div>
<p class="mock">Mock review test in the format of the SQU midterm · for practice only, not an official exam</p>"""

def space(pts): return f'<div class="space" style="--h:{70 + 34 * pts}px"></div>'
def venn_svg():
    return ""

def questions():
    rows = "".join(f"<tr><td>Q{n}. [{TOT[n]} pts.]</td><td style='min-width:70px'></td></tr>" for n in range(1, 6))
    h = [HDR, f"""<div class="cover"><div class="who"><p>Student's Name: <span></span></p><p>ID Number: <span></span></p><p>Section: <span style="min-width:80px"></span></p></div>
<table class="score"><thead><tr><th>Qu. No</th><th>Score</th></tr></thead><tbody>{rows}<tr><td><b>Total: 60</b></td><td></td></tr></tbody></table></div>
<p class="center">Questions start from the next page</p><p class="center" style="margin-top:0">Answer <b>all</b> questions. Show <b>all</b> your work.</p>
<div class="rules"><b>Instructions.</b><ul><li>Give each probability as a fraction and as a decimal to 4 places.</li>
<li>Write sample spaces and events in set notation where asked, and name the rule you use. Method marks are given for both.</li>
<li>Calculators allowed. Sections covered: 4-1 to 4-5.</li></ul></div>"""]
    for q in QS:
        h.append('<div class="pb"></div>' if q["part"] == "A" else "")
        h.append(f'<div class="qblock"><p class="qh">Q{q["num"]}. [{q["part"]}]. [{q["pts"]} pts.] <span class="tag">§ {q["title"]}</span></p><p>{q["stem"]}</p>')
        if q.get("table"): h.append(q["table"])
        if q.get("lead"): h.append(f"<p>{q['lead']}</p>")
        for lab, pts, txt, *_ in q["parts"]:
            h.append(f'<div class="part"><p>({lab}) {txt} <span class="pts">[{pts}]</span></p>{space(pts)}</div>')
        h.append("</div>")
    return "\n".join(h)

def answers():
    h = [HDR.replace("Chapter 4 Review Test", "Chapter 4 Review Test · ANSWERS, MARKING SCHEME AND EXPLANATIONS")]
    h.append("""<div class="sec"><h3>1 · How SQU midterm questions are built (from the Fall 2014 STAT 1001 Midterm II)</h3>
<ul><li><b>Format</b>: a cover page with a score table, 4 main questions each split into [A] and [B] with points (40 pts, 1 hour), long real-life scenarios in (a), (b), (c) parts, and "show all your work". This mock copies it: 5 questions, 60 pts, 90 minutes.</li>
<li><b>Q1[A] style</b>, a two-way table from an SQU survey: one <b>or</b> question across rows, one <b>and not</b> question in a single row, and one <b>given that</b> question. This mock's Q1[A] has the same three, plus independence and mutually-exclusive checks.</li>
<li><b>Q1[B] style</b>, counting with categories: "how many ways that <b>none</b> of them…" (a combination from the other categories) and "the probability that <b>one</b> of them…" (exactly one: ₖC₁ × ₒₜₕₑᵣC₂ ÷ ₙC₃).</li>
<li>Points are about 1 per step; the final number alone rarely earns full marks.</li></ul>
<p class="arx">الأسئلة طويلة وقصصية من بيئة الجامعة، وكل سؤال يختبر قاعدتين أو ثلاثًا بالترتيب. الدرجة على الخطوات: اسم القاعدة، والتعويض، ثم الناتج.</p></div>""")
    # sample midterm ch4 parts solved
    S = {"S": (15, 10), "M": (20, 18), "E": (22, 15)}; n = 100
    tot = 12 + 8 + 4 + 7
    h.append(f"""<div class="sec"><h3>2 · The Chapter 4 questions of that midterm, solved</h3>
<p><b>Q1[A]</b> (100 students; Science 25, Medicine 38, Engineering 37). (a) P(M or E): colleges are mutually exclusive, so (38 + 37)/100 = <b>0.75</b>. (b) P(M and N) = 18/100 = <b>0.18</b>. (c) P(Y | S) = 15/25 = <b>0.6</b>.</p>
<p><b>Q1[B]</b> ({tot} customers: blue 12, green 8, gray 4, black 7; 3 selected). (a) None black: ₂₄C₃ = <b>{C(24, 3):,}</b> ways. (b) Exactly one green: ₈C₁ × ₂₃C₂ / ₃₁C₃ = 8 × {C(23, 2)} / {C(31, 3):,} = {fr(8 * C(23, 2), C(31, 3))}.</p>
<p class="arx">بقية أسئلة ذلك الامتحان (القيمة المتوقعة، ذات الحدين، الطبيعي، فترات الثقة) من الفصول 5 إلى 7، وليست من الفصل الرابع.</p></div>""")
    cov = [("Sample space, set notation, classical probability", "Q2[A] a, e"), ("Empirical probability, frequency table", "Q2[B]"), ("Subjective probability", "Q2[B] e"),
           ("Complement, at least / at most / more than", "Q1[B] c · Q2[A] c · Q2[B] · Q3[A] c"), ("Mutually exclusive events", "Q1[A] f · Q2[A] d · Q3[A] e"),
           ("Addition rules 1 and 2", "Q1[A] a · Q2[A] b · Q3[A] a"), ("Extended addition rule (3 events)", "Q3[C]"),
           ("Two-way table: and, or, given", "Q1[A]"), ("Conditional probability", "Q1[A] c, d · Q2[A] e · Q3[A] d · Q4[A] d"),
           ("Independence test", "Q1[A] e · Q3[A] e · Q4[A] e"), ("Multiplication rule 1 (independent)", "Q3[B] d · Q4[B] a–e"),
           ("Multiplication rule 2 (dependent, without replacement, \"of those\")", "Q3[B] a–c · Q4[A] b · Q4[B] f"), ("Tree diagram", "Q3[B] c · Q4[A]"),
           ("At least one = 1 − none", "Q1[B] c · Q4[B] b · Q5[B] b"), ("Fundamental counting rule, with and without repetition", "Q5[A] a, b"),
           ("Permutation rule 1", "Q5[A] c"), ("Permutation rule 2 (identical letters)", "Q5[A] e"), ("Combinations", "Q1[B] a · Q5[A] d"),
           ("Probability with counting rules", "Q1[B] b–d · Q5[B]")]
    h.append('<div class="sec"><h3>3 · Coverage: every Chapter 4 point and where it is tested</h3><table class="cov"><thead><tr><th>Point</th><th>Question</th></tr></thead><tbody>' +
             "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in cov) + "</tbody></table></div>")
    tones = {1: "1", 2: "2", 3: "3", 4: "4", 5: "1"}
    for q in QS:
        h.append(f'<p class="qh" style="margin-top:12px">Q{q["num"]}. [{q["part"]}]. [{q["pts"]} pts.] <span class="tag">§ {q["title"]}</span></p>')
        if q.get("venn"):
            a, b_, c_, d_ = q["venn"]
            h.append(f'<p style="font-size:11px">Venn regions: A only {a} · A ∩ B {b_} · B only {c_} · neither {d_} (sum 1 ✓).</p>')
        for lab, pts, txt, fin, work, ar, trap in q["parts"]:
            steps = "".join(f"<li>{w}</li>" for w in work)
            ar = ar.replace("⟦", '<span dir="ltr">').replace("⟧", "</span>")
            h.append(f'<div class="sol" style="--sec:var(--ink-{tones[q["num"]]})"><div class="shead"><span><b>({lab})</b> <span class="pts">[{pts} pt{"s" if pts > 1 else ""}]</span></span><span class="fin">{fin}</span></div>'
                     f'<ol>{steps}</ol><div class="ar">الشرح: {ar}</div>' + (f'<div class="trap">Common mistake: {trap}</div>' if trap and trap != "—" else "") + "</div>")
    return "\n".join(h)

docs = [("Questions", "Chapter 4 Review Test", questions()), ("Answers", "Chapter 4 Review Test Answers", answers())]
man = []
for slug, title, body in docs:
    src = f"{OUT}/html/{slug}.html"
    open(src, "w", encoding="utf-8").write(head(title) + CSS + f'<div class="wrap"><div class="paper">{body}</div></div>')
    man.append(dict(src=src, out=f"{OUT}/STAT2101-Ch4-Mock-Exam-{slug}.pdf", title=title))
json.dump(man, open("/tmp/claude-0/-home-user-STAT2101/521e5d47-fbd3-5206-8b60-93d1c3cc1629/scratchpad/mock/man.json", "w"))
print("parts", sum(len(q["parts"]) for q in QS), "points", sum(TOT.values()), TOT)
