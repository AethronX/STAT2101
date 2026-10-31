"""Chapter 3 exam-style question bank. Every numeric answer is computed here, never typed by hand."""
import math
from statistics import mean, median, stdev, variance, multimode
from ch3lib import *

def fm(x, d=2):
    s = f"{x:.{d}f}".rstrip("0").rstrip(".")
    return s if s != "-0" else "0"

def quart(x):
    x = sorted(x); n = len(x); h = n // 2
    lo, hi = x[:h], (x[h + 1:] if n % 2 else x[h:])
    return median(lo), median(x), median(hi)

def pval(x, p):
    x = sorted(x); n = len(x); c = n * p / 100
    if abs(c - round(c)) < 1e-9:
        c = int(round(c)); return (x[c - 1] + x[c]) / 2, c, True
    return x[math.ceil(c) - 1], c, False

Q = []   # dicts: id, part, tags, clo, marks, q, a
def add(id, part, tags, clo, q, a, marks=None):
    Q.append(dict(id=id, part=part, tags=tags, clo=clo, q=q, a=a, marks=marks))

def mcq(opts):
    return '<ul class="opts">' + "".join(f"<li>({k}) {v}</li>" for k, v in zip("abcd", opts)) + "</ul>"

# ======================================================================== PART A
A = [
 ("3-1", "CLO1-A", "A hospital records the mean waiting time of <strong>all</strong> 1,240 patients who visited its emergency department in 2025: 47 minutes. The value 47 is:",
  ["a statistic, because it is a mean", "a parameter, because it describes the entire population of interest", "a statistic, because it was computed from recorded data", "a parameter only if the data are normally distributed"],
  "b", "The question defines the population as all 2025 emergency patients, and every one of them was measured. A measure of the whole population is a <strong>parameter</strong> (μ). Option (a) is the classic trap: being a mean doesn't make it a statistic."),
 ("3-1", "CLO3-C", "In a company the mean monthly salary is OMR 1,450 and the median is OMR 820. Which conclusion is best justified?",
  ["the salary distribution is symmetric", "a few very high salaries pull the mean up, so the median better represents a typical employee", "most employees earn more than OMR 1,450", "the mode must be greater than OMR 1,450"],
  "b", "The mean is far above the median, so the distribution is <strong>right-skewed</strong> by a few large salaries (the Example 3-11 pattern). At least half earn OMR 820 or less, which rules out (c). In right-skewed data the mode is usually the smallest of the three, which rules out (d)."),
 ("3-1", "CLO2-A", "A frequency table of household incomes has a last class \"OMR 3,000 and above\". Which measure <strong>cannot</strong> be computed from the table?",
  ["the modal class", "the median class", "the mean", "the total number of households"],
  "c", "The mean needs Σf·Xₘ, and an <strong>open-ended class has no midpoint</strong>. The median class and modal class need only frequencies and cumulative frequencies, so both can still be found."),
 ("3-1", "CLO3-B", "A distribution has mean 63, median 70 and mode 74. Its shape is:",
  ["positively skewed", "negatively skewed", "symmetric", "impossible to tell without a graph"],
  "b", "Mean &lt; median &lt; mode: the mean has been pulled toward a long <strong>left</strong> tail, so the distribution is negatively skewed."),
 ("3-1", "CLO2-A", "All 20 values in a data set equal 12. Which statement is <strong>false</strong>?",
  ["mean = median = 12", "the mode is 12", "the standard deviation is 0", "the data set has no mode because no value differs from the others"],
  "d", "12 occurs 20 times, so it is the mode. \"No mode\" means no value repeats, which is the opposite situation. Every deviation is 0, so s = 0."),
 ("3-2", "CLO3-C", "Two machines fill 250 g packs. Both have mean 250 g. Machine A has s = 1.8 g and machine B has s = 4.1 g. Which is correct?",
  ["A is more consistent", "B is more consistent", "they are equally consistent because the means are equal", "consistency cannot be compared without the CV"],
  "a", "With <strong>equal means</strong>, the smaller SD means less variation. The CV would give the same ranking: 0.72% vs 1.64%. The CV is essential only when the means or units differ, so (d) is wrong here."),
 ("3-2", "CLO1-A", "Which statement about the variance is <strong>false</strong>?",
  ["it can equal zero", "it can be negative when most values are below the mean", "its units are the square of the data units", "dividing by n − 1 instead of n makes the sample variance slightly larger"],
  "b", "The variance is an average of <strong>squared</strong> deviations, so it is never negative, however the values sit relative to the mean."),
 ("3-2", "CLO2-A", "Without knowing the shape of a distribution, the smallest percentage of values guaranteed within 2.5 standard deviations of the mean is:",
  ["68%", "84%", "95%", "75%"],
  "b", "Shape unknown, so use Chebyshev: 1 − 1/2.5² = 1 − 0.16 = 0.84 = <strong>84%</strong>. 68% and 95% are empirical-rule values and need a bell shape."),
 ("3-2", "CLO2-A", "Bell-shaped data have mean 60 and SD 5. Approximately what percentage of values are <strong>above 70</strong>?",
  ["5%", "2.5%", "16%", "0.15%"],
  "b", "70 = 60 + 2(5). About 95% lie within 50–70, so 5% lie outside, split equally between the two tails: <strong>2.5%</strong> above 70."),
 ("3-2", "CLO3-C", "Every employee in a company receives a raise of OMR 50 per month. What happens to the standard deviation and the coefficient of variation of salaries?",
  ["both unchanged", "SD unchanged, CV decreases", "SD increases by 50, CV unchanged", "both increase"],
  "b", "Adding a constant shifts every salary equally, so the spread (SD) is unchanged. The mean rises by 50, so CV = s/x̄ gets <strong>smaller</strong>."),
 ("3-2", "CLO2-A", "Every value in a data set with variance 6.5 is multiplied by 3. The new variance is:",
  ["6.5", "19.5", "58.5", "9.5"],
  "c", "Multiplying by c multiplies the SD by c and the <strong>variance by c²</strong>: 6.5 × 9 = 58.5."),
 ("3-3", "CLO3-C", "Salma's z-score on a test is −0.8. This means:",
  ["she answered 80% of the questions wrongly", "her score is 0.8 standard deviations below the class mean", "80% of the class scored above her", "her score is 0.8 marks below the mean"],
  "b", "A z-score counts <strong>standard deviations</strong> from the mean; the sign says below. It says nothing about percentages correct (a) or marks (d)."),
 ("3-3", "CLO3-C", "Ali's score is at the 70th percentile of his class. Which statement is correct?",
  ["Ali answered 70% of the questions correctly", "about 70% of the class scored lower than Ali", "Ali's score is 70", "Ali scored 70% above the mean"],
  "b", "A <strong>percentile</strong> is a relative position, not a percentage of marks. This is Dr. Amani's percentile vs percentage distinction."),
 ("3-3", "CLO1-A", "Which of these is <strong>not</strong> equal to the median?",
  ["P₅₀", "Q₂", "D₅", "P₅"],
  "d", "Median = P₅₀ = Q₂ = D₅. P₅ is the 5th percentile."),
 ("3-3", "CLO3-C", "An extremely large value is added to a data set. Which measure changes the <strong>most</strong>?",
  ["the median", "the IQR", "the standard deviation", "Q₁"],
  "c", "The SD is built from squared distances from the mean, so one extreme value inflates it dramatically. The median, Q₁ and IQR depend on positions and move very little."),
 ("3-4", "CLO3-B", "In a boxplot, the median is close to Q₃ and the left whisker is three times as long as the right whisker. The distribution is:",
  ["symmetric", "positively skewed", "negatively skewed", "bimodal"],
  "c", "Median right of centre and left whisker longer both point to a long <strong>left</strong> tail: negatively skewed."),
 ("3-4", "CLO1-A", "In exploratory data analysis, the measures of centre and of variation are respectively:",
  ["mean and standard deviation", "median and IQR", "mode and range", "median and standard deviation"],
  "b", "EDA uses the <strong>median</strong> and the <strong>IQR</strong>, because neither is distorted by the outliers EDA is trying to find."),
 ("3-4", "CLO3-B", "In a boxplot, the right whisker (Q₃ to max) is twice as long as the left half of the box (Q₁ to median). This tells you that:",
  ["more values lie above Q₃ than between Q₁ and the median", "the top 25% of values are more spread out than the second quarter", "the data contain an outlier", "the mean is above Q₃"],
  "b", "Each of the four pieces holds <strong>25%</strong> of the data. A longer piece means the same number of values spread over a wider interval, not more values."),
]
for i, (tag, clo, q, opts, ans, why) in enumerate(A, 1):
    add(f"A{i}", "A", [tag], clo, f"<p>{q}</p>{mcq(opts)}", f"<p>⦃({ans})⦄</p><p class=\"why\">{why}</p>")

# ======================================================================== PART B · 3-1
known = [12, 18, 9, 16, 20]; six = 6 * 14.5 - sum(known); d6 = sorted(known + [six])
add("B1", "B", ["3-1"], "CLO2-A",
    "<p>The mean of six sample values is 14.5. Five of them are 12, 18, 9, 16 and 20. Find the sixth value, then the median and mode of all six.</p>",
    f"<p>Σx = n·x̄ = 6 × 14.5 = 87. Sixth value = 87 − {sum(known)} = ⦃{fm(six)}⦄.</p>"
    f"<p>Ordered: {', '.join(fm(v) for v in d6)}. n = 6 (even), so median = ({fm(d6[2])} + {fm(d6[3])})/2 = ⦃{fm((d6[2]+d6[3])/2)}⦄. Mode = ⦃{fm(multimode(d6)[0])}⦄.</p>"
    "<p class=\"why\">Key idea: x̄ = Σx/n can be run backwards to give Σx = n·x̄. Exam favourite: a missing value or a correction.</p>")
tot = 25 * 68; new = (tot - 48 + 84) / 25
add("B2", "B", ["3-1"], "CLO2-A",
    "<p>The mean of 25 exam scores was reported as 68. It was later found that one score had been recorded as 48 instead of 84. (a) Find the correct mean. (b) Must the median change? Explain.</p>",
    f"<p>(a) Recorded total = 25 × 68 = {tot}. Corrected total = {tot} − 48 + 84 = {fm(tot+36)}. Correct mean = {fm(tot+36)}/25 = ⦃{fm(new)}⦄.</p>"
    "<p>(b) <strong>Not necessarily.</strong> The median is the 13th ordered value. Moving one score from 48 to 84 changes it only if that score crosses the middle position, and we can't tell without the data. The mean always changes, because it uses every value.</p>")
m = (32 * 71 + 18 * 79) / 50
add("B3", "B", ["3-1"], "CLO2-A · CLO3-C",
    "<p>Section 10 of STAT 2101 has 32 students with mean 71. Section 20 has 18 students with mean 79. A student says the overall mean is (71 + 79)/2 = 75. Is this correct? Find the overall mean.</p>",
    f"<p><strong>No.</strong> The sections are different sizes, so their means must be <strong>weighted</strong> by the number of students.</p>"
    f"<p class=\"fx\">x̄ = ⟪32(71) + 18(79)‖32 + 18⟫ = ⟪2272 + 1422‖50⟫ = ⦃{fm(m)}⦄</p>"
    "<p class=\"why\">The overall mean sits closer to 71 because the larger section carries more weight.</p>")
w = [.15, .10, .05, .25]; sc = [80, 90, 100, 72]; sofar = sum(a * b for a, b in zip(w, sc))
needA = (90 - sofar) / .45; needAm = (86 - sofar) / .45
add("B4", "B", ["3-1"], "CLO2-A",
    "<p>The STAT 2101 outline weights are: In-Class Quizzes 15%, Lab Quiz 10%, Active Learning 5%, Midterm 25%, Final 45%. A student has 80, 90, 100 and 72 (out of 100) in the first four. (a) Can the student still reach an A (≥ 90)? (b) What final score secures A− (≥ 86)?</p>",
    f"<p>Weighted points so far: 0.15(80) + 0.10(90) + 0.05(100) + 0.25(72) = 12 + 9 + 5 + 18 = {fm(sofar)}.</p>"
    f"<p>(a) An A needs 0.45F ≥ 90 − {fm(sofar)} = {fm(90-sofar)}, so F ≥ {fm(needA)}. That is impossible: ⦃no⦄. The best possible total is {fm(sofar)} + 45 = {fm(sofar+45)}.</p>"
    f"<p>(b) 0.45F ≥ 86 − {fm(sofar)} = {fm(86-sofar)}, so F ≥ {fm(needAm)}: with whole-number marks the student needs at least ⦃{math.ceil(needAm)}⦄ on the final.</p>")
kids = {0: 5, 1: 9, 2: 14, 3: 8, 4: 4}; n = sum(kids.values()); mk = sum(k * f for k, f in kids.items()) / n
add("B5", "B", ["3-1"], "CLO2-A · CLO3-B",
    "<p>Number of children in 40 families: 0 children → 5 families, 1 → 9, 2 → 14, 3 → 8, 4 → 4. Find the mean, median and mode, and describe the shape.</p>",
    f"<p>Mean (each value weighted by its frequency): (0·5 + 1·9 + 2·14 + 3·8 + 4·4)/40 = 77/40 = ⦃{fm(mk,3)}⦄.</p>"
    "<p>Median: n = 40, so average the 20th and 21st values. Cumulative counts: 5, 14, 28, …, so both lie in the \"2\" group: median = ⦃2⦄. Mode = ⦃2⦄ (14 families).</p>"
    f"<p>Mean ({fm(mk,3)}) &lt; median = mode (2): ⦃slightly negatively skewed⦄.</p>")
add("B6", "B", ["3-1"], "CLO3-C",
    "<p>Choose the most appropriate measure of centre and justify it in one line each: (a) blood types of 200 donors; (b) customer satisfaction rated poor / fair / good / excellent; (c) house prices in Muscat, where a few villas cost over OMR 900,000; (d) heights of 500 adult women, roughly symmetric.</p>",
    "<p>(a) ⦃Mode⦄: nominal data, so no ordering or arithmetic is meaningful. (b) ⦃Median⦄: ordinal data, which can be ordered but not averaged. (c) ⦃Median⦄: ratio data, but right-skewed by outliers that would inflate the mean. (d) ⦃Mean⦄: ratio data, not skewed; the mean uses all values and varies least across samples.</p>")
stem = [32, 35, 38, 40, 41, 41, 46, 49, 52, 52, 52, 57, 60, 64, 78]
add("B7", "B", ["3-1"], "CLO2-A · CLO3-C",
    "<p>Stem-and-leaf (key 3 | 2 = 32): 3 | 2 5 8 · 4 | 0 1 1 6 9 · 5 | 2 2 2 7 · 6 | 0 4 · 7 | 8. (a) Find the mean, median, mode and midrange. (b) If 78 had been recorded as 98, which of these four would change, and by how much?</p>",
    f"<p>(a) n = 15, Σx = {sum(stem)}, so x̄ = ⦃{fm(mean(stem),3)}⦄. Median = 8th value = ⦃{median(stem)}⦄. Mode = ⦃52⦄. MR = (32 + 78)/2 = ⦃55⦄.</p>"
    f"<p>(b) The mean rises by 20/15 = ⦃1.33⦄, to {fm(mean(stem)+20/15,3)}. The midrange rises by 20/2 = ⦃10⦄, to 65. The <strong>median and mode do not change</strong>: they depend on positions and repeats, not on how far the largest value is.</p>")

# ======================================================================== PART B · 3-2
n, Sx, Sx2 = 12, 540, 25140; s2 = (n * Sx2 - Sx ** 2) / (n * (n - 1)); s = math.sqrt(s2)
add("B8", "B", ["3-2"], "CLO2-A",
    "<p>For a sample, n = 12, ΣX = 540 and ΣX² = 25,140. Find the standard deviation and the coefficient of variation.</p>",
    f"<p class=\"fx\">s² = ⟪12(25,140) − 540²‖12(11)⟫ = ⟪301,680 − 291,600‖132⟫ = ⟪10,080‖132⟫ = {fm(s2,4)}</p>"
    f"<p>s = ⦃{fm(s,3)}⦄; x̄ = 540/12 = 45; CV = {fm(s,3)}/45 × 100 = ⦃{fm(s/45*100,2)}%⦄.</p>"
    "<p class=\"why\">The raw data are not needed: the shortcut formula works directly from n, ΣX and ΣX².</p>")
d = [4, 7, 9, 12]; ss = sum((v - mean(d)) ** 2 for v in d)
add("B9", "B", ["3-2"], "CLO2-A",
    "<p><strong>Find the mistake.</strong> For the <em>sample</em> 4, 7, 9, 12 a student wrote: x̄ = 8, Σ(X − x̄)² = 34, \"s² = 34/4 = 8.5, s = 2.92\". Identify the error and correct it.</p>",
    f"<p>The student divided by n. This is a <strong>sample</strong>, so the divisor is n − 1 = 3.</p><p class=\"fx\">s² = 34/3 = ⦃{fm(ss/3,3)}⦄ &nbsp; s = ⦃{fm(math.sqrt(ss/3),3)}⦄</p>"
    "<p class=\"why\">Dividing by n underestimates the population variance; that is the reason for n − 1.</p>")
cvp, cvt = .008 / .229 * 100, 2.6 / 34 * 100
add("B10", "B", ["3-2"], "CLO2-A · CLO3-C",
    "<p>Over one summer in Muscat, the weekly petrol price had mean OMR 0.229 per litre with s = OMR 0.008, and the daily maximum temperature had mean 34 °C with s = 2.6 °C. Which variable was relatively more variable? Justify.</p>",
    f"<p>The units differ (OMR vs °C), so the raw SDs can't be compared. Use the CV:</p><p class=\"fx\">price: 0.008/0.229 × 100 = {fm(cvp,2)}% &nbsp;&nbsp; temperature: 2.6/34 × 100 = {fm(cvt,2)}%</p>"
    "<p>⦃Temperature⦄ was relatively more variable; the petrol price was more consistent.</p>")
add("B11", "B", ["3-2"], "CLO2-A",
    "<p>A data set has mean 80 and s = 3, and its shape is unknown. Find the interval, centred at the mean, that must contain <strong>at least 96%</strong> of the values.</p>",
    "<p>Set 1 − 1/k² = 0.96, so 1/k² = 0.04, k² = 25 and k = 5.</p><p class=\"fx\">80 ± 5(3) → ⦃65 to 95⦄</p>"
    "<p class=\"why\">Chebyshev run backwards: from the percentage to k, then to the interval.</p>")
add("B12", "B", ["3-2"], "CLO2-A · CLO3-C",
    "<p>A data set has mean 50 and s = 5, and its shape is unknown. A student claims that at least 84% of the values lie between 40 and 65, because the upper limit is 3 SD above the mean. Evaluate the claim and give the correct guaranteed percentage.</p>",
    "<p>Chebyshev applies to intervals <strong>symmetric</strong> about the mean. The interval 40–65 is 2 SD below and 3 SD above. The symmetric interval it is guaranteed to contain is 40–60 (k = 2), so at least ⦃75%⦄ lie between 40 and 65. The student's 84% isn't guaranteed (and 3 SD would give 88.89%, not 84%).</p>"
    "<p class=\"why\">With an asymmetric interval, use the <strong>smaller</strong> k.</p>")
add("B13", "B", ["3-2"], "CLO2-A",
    "<p>Delivery times are bell-shaped, and about 95% of them fall between 18 and 42 minutes. (a) Find the mean and SD. (b) About what percentage take longer than 36 minutes? (c) About what percentage take between 24 and 42 minutes?</p>",
    "<p>(a) 95% lies within ±2 SD, so the mean is the midpoint: (18 + 42)/2 = ⦃30⦄. Then 4s = 42 − 18 = 24, so s = ⦃6⦄.</p>"
    "<p>(b) 36 = 30 + 1·6. About 68% lie within ±1 SD, so 32% lie outside, half above: ⦃16%⦄.</p>"
    "<p>(c) 24 is −1 SD and 42 is +2 SD. Half of 68% (34%) plus half of 95% (47.5%) = ⦃81.5%⦄.</p>")
add("B14", "B", ["3-2"], "CLO2-A · CLO3-C",
    "<p>Quiz marks out of 20 have mean 12.4, median 13, SD 3.1 and IQR 4.5. The instructor converts each mark to a score out of 100 (multiplying by 5) and then adds 4 bonus points. Find the new mean, median, SD, IQR and variance. Does the coefficient of variation change?</p>",
    f"<p>For y = 5x + 4: centre ×5 + 4, spread ×5, variance ×25.</p>"
    f"<p>Mean = 5(12.4) + 4 = ⦃66⦄ · median = 5(13) + 4 = ⦃69⦄ · SD = 5(3.1) = ⦃15.5⦄ · IQR = 5(4.5) = ⦃22.5⦄ · variance = 15.5² = ⦃240.25⦄.</p>"
    f"<p>CV before = 3.1/12.4 = {fm(3.1/12.4*100,2)}%; after = 15.5/66 = {fm(15.5/66*100,2)}%. It <strong>changes</strong>: multiplying alone would leave it unchanged, but the added constant raises the mean without changing the SD.</p>")
dev = [-3, 5, -1, None, 2]; x4 = -sum(v for v in dev if v is not None); full = [-3, 5, -1, x4, 2]
add("B15", "B", ["3-2"], "CLO2-A",
    "<p>The deviations of five sample values from their mean are −3, 5, −1, d and 2. Find d and the sample variance.</p>",
    f"<p>Deviations from the mean always sum to zero: −3 + 5 − 1 + d + 2 = 0, so d = ⦃{x4}⦄.</p>"
    f"<p class=\"fx\">s² = ⟪9 + 25 + 1 + 9 + 4‖5 − 1⟫ = ⟪48‖4⟫ = ⦃12⦄</p>")

# ======================================================================== PART B · 3-3
add("B16", "B", ["3-3"], "CLO2-A · CLO3-C",
    "<p>A scholarship requires a z-score of at least 1.75 on an entrance exam with mean 64 and s = 8. (a) What is the minimum qualifying score? (b) Hamad scored 75. Does he qualify?</p>",
    "<p>(a) X = x̄ + z·s = 64 + 1.75(8) = ⦃78⦄. (b) z = (75 − 64)/8 = 1.375 &lt; 1.75: ⦃no⦄, he is 3 marks short.</p>")
zA, zB = (52 - 55) / 2, (49 - 50) / .8
add("B17", "B", ["3-3"], "CLO3-C",
    "<p>In a 400 m race, Runner A ran 52 s in a group with mean 55 s and s = 2 s. Runner B ran 49 s in a group with mean 50 s and s = 0.8 s. Which runner performed better relative to their own group?</p>",
    f"<p>z<sub>A</sub> = (52 − 55)/2 = {fm(zA)} and z<sub>B</sub> = (49 − 50)/0.8 = {fm(zB)}.</p><p>For running times <strong>lower is better</strong>, so the more negative z is the stronger performance: ⦃Runner A⦄. A has the slower raw time but is 1.5 SD faster than his group, against 1.25 SD for B.</p>"
    "<p class=\"why\">Trap: picking B because 49 &lt; 52, or picking the larger z without checking whether a high value is good.</p>")
dv = [12, 15, 18, 20, 21, 23, 25, 26, 28, 30, 31, 33, 35, 38, 41, 47]
q1, q2, q3 = quart(dv); I = q3 - q1; p25 = pval(dv, 25); p90 = pval(dv, 90); r30 = (sum(v < 30 for v in dv) + .5) / len(dv) * 100
d3 = pval(dv, 30); d7 = pval(dv, 70)
add("B18", "B", ["3-3"], "CLO2-A",
    f"<p>Daily visitors to a museum in Nizwa over 16 days (already ordered): {', '.join(map(str, dv))}. (a) Find the percentile rank of 30. (b) Find P₂₅ and P₉₀. (c) Find Q₁, Q₂, Q₃ by the median method and check for outliers. (d) Find D₃ and D₇.</p>",
    f"<p>(a) 9 values are below 30: (9 + 0.5)/16 × 100 = {fm(r30,3)} ≈ ⦃59th percentile⦄.</p>"
    f"<p>(b) P₂₅: c = 16·25/100 = 4, whole, so (4th + 5th)/2 = (20 + 21)/2 = ⦃{fm(p25[0])}⦄. P₉₀: c = 14.4, rounds up to 15, so the 15th value = ⦃{fm(p90[0])}⦄.</p>"
    f"<p>(c) Q₂ = (26 + 28)/2 = ⦃{fm(q2)}⦄; Q₁ = median of the lower 8 = (20 + 21)/2 = ⦃{fm(q1)}⦄; Q₃ = median of the upper 8 = (33 + 35)/2 = ⦃{fm(q3)}⦄. IQR = {fm(I)}; fences {fm(q1-1.5*I)} and {fm(q3+1.5*I)}. The extremes 12 and 47 are inside: ⦃no outliers⦄. Q₁ equals P₂₅, as it should.</p>"
    f"<p>(d) D₃ = P₃₀: c = 4.8, rounds up to 5, so ⦃{fm(d3[0])}⦄. D₇ = P₇₀: c = 11.2, rounds up to 12, so ⦃{fm(d7[0])}⦄.</p>")
add("B19", "B", ["3-3"], "CLO2-A",
    "<p>In a class of 40 students, Maryam's percentile rank (by the course formula) is 81.25. How many students scored below her? How many scored above her, assuming no ties?</p>",
    "<p>(r + 0.5)/40 × 100 = 81.25, so r + 0.5 = 32.5 and r = ⦃32 below⦄. Above: 40 − 32 − 1 (Maryam herself) = ⦃7⦄.</p>")
bd = [14, 18, 20, 22, 24, 26, 28, 30, 31, 45]; a1, a2, a3 = quart(bd); II = a3 - a1
add("B20", "B", ["3-3"], "CLO2-A · CLO3-C",
    f"<p>Is 45 an outlier in the data {', '.join(map(str, bd))}? Show the procedure.</p>",
    f"<p>Median = (24 + 26)/2 = {fm(a2)}. Q₁ = median of 14 18 20 22 24 = {fm(a1)}. Q₃ = median of 26 28 30 31 45 = {fm(a3)}. IQR = {fm(II)} and 1.5·IQR = {fm(1.5*II)}.</p>"
    f"<p>Fences: {fm(a1-1.5*II)} and {fm(a3+1.5*II)}. 45 <strong>equals</strong> the upper fence, and an outlier must be strictly greater, so ⦃45 is not an outlier⦄.</p>")

# ======================================================================== PART B · 3-4
add("B21", "B", ["3-4"], "CLO3-B · CLO3-C",
    "<p>The five-number summary of waiting times (minutes) for 120 patients is 4, 11, 15, 22, 49. (a) Describe the shape. (b) Is 49 an outlier? (c) About how many patients waited at least 15 minutes? (d) What percentage waited between 11 and 49 minutes?</p>",
    "<p>(a) The median is nearer Q₁ (15 − 11 = 4) than Q₃ (22 − 15 = 7), and the right whisker (27) is much longer than the left (7): ⦃positively skewed⦄.</p>"
    "<p>(b) IQR = 11, 1.5·IQR = 16.5, upper fence = 38.5. Since 49 &gt; 38.5, ⦃49 is an outlier⦄.</p>"
    "<p>(c) Half the patients are at or above the median: about ⦃60⦄. (d) From Q₁ to the maximum is three quarters of the data: ⦃75%⦄.</p>")
add("B22", "B", ["3-4"], "CLO3-C",
    "<p>Five-number summaries of waiting times (minutes) at two bank branches: Muscat 3, 8, 12, 15, 21; Sohar 5, 7, 9, 18, 30. Compare the branches on centre, spread, range and shape.</p>",
    "<p><strong>Centre:</strong> Muscat's median (12) is higher than Sohar's (9). <strong>Spread:</strong> Sohar's IQR (11) is larger than Muscat's (7). <strong>Range:</strong> Sohar 25 vs Muscat 18, so Sohar varies more. "
    "<strong>Shape:</strong> Muscat is roughly symmetric (median 4 above Q₁ and 3 below Q₃; whiskers 5 and 6). Sohar is ⦃positively skewed⦄ (median only 2 above Q₁; right whisker 12 vs left 2).</p>"
    "<p class=\"why\">Sohar has the shorter typical wait but the longer, less predictable worst cases.</p>")
s1, s2_, s3 = quart(stem); IS = s3 - s1
add("B23", "B", ["3-4"], "CLO2-A · CLO3-B",
    "<p>Using the stem-and-leaf data of B7, find the five-number summary, check for outliers, and describe the shape from the boxplot.</p>",
    f"<p>n = 15, median = 8th = ⦃{fm(s2_)}⦄. Lower seven 32 35 38 <strong>40</strong> 41 41 46, so Q₁ = ⦃{fm(s1)}⦄. Upper seven 52 52 52 <strong>57</strong> 60 64 78, so Q₃ = ⦃{fm(s3)}⦄.</p>"
    f"<p>Five-number summary: 32, {fm(s1)}, {fm(s2_)}, {fm(s3)}, 78. IQR = {fm(IS)}; fences {fm(s1-1.5*IS)} and {fm(s3+1.5*IS)}, so 78 is not an outlier.</p>"
    f"<p>Shape: the median is almost centred in the box (9 vs 8), but the right whisker (21) is much longer than the left (8): ⦃slightly positively skewed⦄. The tail comes from 64 and 78.</p>")

# boxplot figure question
sx = scale(20, 100, 120, 630)
g = axis(sx, 20, 100, 150, range(20, 101, 10))
g += [T(20, 54, "Section A", "sm b t2", "start")] + boxplot(sx, 50, (30, 56, 70, 76, 84), "2", h=26, labels=False)
g += [T(20, 114, "Section B", "sm b t4", "start")] + boxplot(sx, 110, (50, 58, 64, 70, 78), "4", h=26, labels=False)
FIGQ = fig(660, 176, "\n".join(g), "Side-by-side boxplots of midterm scores for two sections on a common scale from 20 to 100",
           "Midterm scores (out of 100) for two STAT 2101 sections. Read values from the scale.",
           "درجات الميدتيرم لشعبتين. اقرأ القيم من المحور.")
add("B24", "B", ["3-4"], "CLO3-B · CLO3-C",
    f"{FIGQ}<p>(a) Read the five-number summary of each section. (b) Which section has the higher median? (c) Which is more variable in its middle 50%? (d) Describe each shape. (e) In which section did at least half the students score above 65?</p>",
    "<p>(a) A: ⦃30, 56, 70, 76, 84⦄ · B: ⦃50, 58, 64, 70, 78⦄.</p><p>(b) ⦃Section A⦄ (70 vs 64). (c) IQR A = 20, IQR B = 12, so ⦃Section A⦄.</p>"
    "<p>(d) A: the median is right of the box centre (14 above Q₁, 6 below Q₃) and the left whisker (26) is far longer than the right (8): ⦃negatively skewed⦄. B: median centred (6 and 6), whiskers equal (8 and 8): ⦃symmetric⦄.</p>"
    "<p>(e) A's median is 70 &gt; 65, so at least half of section A scored above 65. In B the median is 64, so fewer than half did: ⦃Section A⦄.</p>")

# ======================================================================== PART C · long exam questions
c1 = [23, 27, 18, 31, 25, 29, 35, 22, 27, 40, 26, 21]; c1s = sorted(c1); n1 = len(c1)
m1 = mean(c1); md1 = median(c1); s1_ = stdev(c1); S1, S2 = sum(c1), sum(v * v for v in c1)
cq1, cq2, cq3 = quart(c1); ci = cq3 - cq1; lo2, hi2 = m1 - 2 * s1_, m1 + 2 * s1_; inside = sum(lo2 < v < hi2 for v in c1)
add("C1", "C", ["3-1", "3-2", "3-3", "3-4"], "CLO2-A · CLO3-B · CLO3-C",
    f"<p>A health centre in Seeb recorded the number of patients on 12 randomly selected days: {', '.join(map(str, c1))}.</p>"
    "<ol class=\"subs\"><li>Find the mean, median, mode and midrange.</li><li>Find the sample standard deviation using the shortcut formula, and the coefficient of variation.</li>"
    "<li>Find Q₁, Q₂, Q₃ (median method), the IQR, and check for outliers.</li><li>Give the five-number summary and describe the shape of the boxplot. Is this consistent with your answer to part 1?</li>"
    "<li>By Chebyshev's theorem, at least what percentage of days lie within x̄ ± 2s? What percentage actually do?</li><li>Find the z-score of the busiest day and interpret it.</li></ol>",
    f"<p><strong>1.</strong> Ordered: {', '.join(map(str, c1s))}. x̄ = {S1}/12 = ⦃{fm(m1,3)}⦄; median = (26 + 27)/2 = ⦃{fm(md1)}⦄; mode = ⦃27⦄; MR = (18 + 40)/2 = ⦃29⦄.</p>"
    f"<p><strong>2.</strong> ΣX = {S1}, ΣX² = {S2}. s² = [12({S2}) − {S1}²]/(12·11) = ({12*S2} − {S1**2})/132 = {fm((12*S2-S1**2)/132,4)}, so s = ⦃{fm(s1_,3)}⦄. CV = {fm(s1_,3)}/{fm(m1,3)} × 100 = ⦃{fm(s1_/m1*100,2)}%⦄.</p>"
    f"<p><strong>3.</strong> Lower six 18 21 22 | 23 25 26, so Q₁ = (22 + 23)/2 = ⦃{fm(cq1)}⦄. Q₂ = {fm(cq2)}. Upper six 27 27 29 | 31 35 40, so Q₃ = (29 + 31)/2 = ⦃{fm(cq3)}⦄. IQR = ⦃{fm(ci)}⦄; fences {fm(cq1-1.5*ci)} and {fm(cq3+1.5*ci)}, so ⦃no outliers⦄ (40 &lt; {fm(cq3+1.5*ci)}).</p>"
    f"<p><strong>4.</strong> 18, {fm(cq1)}, {fm(cq2)}, {fm(cq3)}, 40. The median sits 4 above Q₁ and 3.5 below Q₃ (near the centre), but the right whisker (10) is longer than the left (4.5): mildly ⦃positively skewed⦄. This agrees with part 1: mean ({fm(m1,2)}) &gt; median ({fm(md1)}).</p>"
    f"<p><strong>5.</strong> At least ⦃75%⦄. The interval is {fm(lo2,2)} to {fm(hi2,2)}, and {inside} of 12 days lie inside: ⦃{fm(inside/12*100,1)}%⦄. Chebyshev's bound is a <em>minimum</em> and is usually beaten.</p>"
    f"<p><strong>6.</strong> z = (40 − {fm(m1,3)})/{fm(s1_,3)} = ⦃{fm((40-m1)/s1_,2)}⦄. The busiest day was about {fm((40-m1)/s1_,1)} standard deviations above the mean number of patients.</p>", marks=18)
cls = [(24.5, 5), (34.5, 12), (44.5, 18), (54.5, 10), (64.5, 5)]; nn = sum(f for _, f in cls)
fx = sum(m * f for m, f in cls); fx2 = sum(f * m * m for m, f in cls); gm = fx / nn; gs2 = (nn * fx2 - fx ** 2) / (nn * (nn - 1)); gs = math.sqrt(gs2)
cf = []; t = 0
for _, f in cls:
    t += f; cf.append(t)
add("C2", "C", ["3-1", "3-2"], "CLO2-A · CLO3-C",
    "<p>Ages of a sample of 50 SQU staff members:</p><div class=\"tbl-wrap\"><table><thead><tr><th>Age</th><th class=\"num\">20–29</th><th class=\"num\">30–39</th><th class=\"num\">40–49</th><th class=\"num\">50–59</th><th class=\"num\">60–69</th></tr></thead>"
    "<tbody><tr><td>f</td><td class=\"num\">5</td><td class=\"num\">12</td><td class=\"num\">18</td><td class=\"num\">10</td><td class=\"num\">5</td></tr></tbody></table></div>"
    "<ol class=\"subs\"><li>Find the mean, the sample standard deviation and the CV.</li><li>Find the modal class and the median class.</li><li>If the last class were \"60 and over\", which of your answers could still be found? Explain.</li></ol>",
    f"<p><strong>1.</strong> Midpoints 24.5, 34.5, 44.5, 54.5, 64.5. Σf·Xₘ = {fm(fx)}, Σf·Xₘ² = {fm(fx2)}.</p>"
    f"<p class=\"fx\">x̄ = {fm(fx)}/50 = {fm(gm,2)} &nbsp; s² = ⟪50({fm(fx2)}) − {fm(fx)}²‖50(49)⟫ = {fm(gs2,3)} &nbsp; s = {fm(gs,3)}</p>"
    f"<p>⦃x̄ = {fm(gm,2)} years, s = {fm(gs,2)} years⦄, CV = ⦃{fm(gs/gm*100,2)}%⦄.</p>"
    f"<p><strong>2.</strong> Modal class ⦃40–49⦄ (f = 18). N/2 = 25; CF = {', '.join(map(str, cf))}, and 35 is the first CF above 25, so the median class is ⦃40–49⦄.</p>"
    "<p><strong>3.</strong> The mean, s and CV <strong>could not</strong> be found: the open-ended class has no midpoint. The modal class and median class <strong>could</strong>: they use only frequencies, and neither falls in the last class.</p>", marks=12)
add("C3", "C", ["3-2"], "CLO2-A · CLO3-C",
    "<p>Two factories fill 500 ml bottles. Factory A: mean 502 ml, s = 4 ml. Factory B: mean 498 ml, s = 2.5 ml.</p>"
    "<ol class=\"subs\"><li>Which factory is more consistent? Justify with a calculation.</li><li>Nothing is known about A's distribution. At least what percentage of A's bottles hold between 494 and 510 ml?</li>"
    "<li>Out of 2,000 bottles from A, at most how many hold less than 490 or more than 514 ml?</li><li>B's fills are bell-shaped. About what percentage of B's bottles hold between 493 and 503 ml? About what percentage hold less than 495.5 ml?</li></ol>",
    f"<p><strong>1.</strong> CV<sub>A</sub> = 4/502 = {fm(4/502*100,2)}% and CV<sub>B</sub> = 2.5/498 = {fm(2.5/498*100,2)}%: ⦃B⦄ is more consistent (the means are close, so the SDs agree too).</p>"
    "<p><strong>2.</strong> k = (510 − 502)/4 = 2, so at least ⦃75%⦄.</p>"
    f"<p><strong>3.</strong> 490 and 514 are 502 ± 3(4), so k = 3. At most 1/9 lie outside: 2000/9 = {fm(2000/9,1)}, so at most ⦃222⦄ bottles. Round <strong>down</strong> for \"at most\".</p>"
    "<p><strong>4.</strong> 493 and 503 are 498 ± 2(2.5): about ⦃95%⦄. 495.5 = 498 − 1(2.5); 68% lie within ±1 SD, so half of the remaining 32% is below: about ⦃16%⦄.</p>", marks=12)
md = [18, 22, 25, 27, 29, 30, 31, 33, 34, 35, 36, 36, 38, 39, 40, 41, 43, 44, 46, 49]
mm, ms = mean(md), stdev(md); p80 = pval(md, 80); r35 = (sum(v < 35 for v in md) + .5) / 20 * 100; z41 = (41 - mm) / ms
add("C4", "C", ["3-2", "3-3"], "CLO2-A · CLO3-C",
    f"<p>Midterm marks (out of 50) for 20 students, ordered: {', '.join(map(str, md))}. Here x̄ = {fm(mm,2)} and s = {fm(ms,3)}.</p>"
    "<ol class=\"subs\"><li>Find the percentile rank of 35 and the value at P₈₀.</li><li>Khalid scored 41. Find his z-score.</li>"
    "<li>The instructor converts each mark to a score out of 100 (× 2) and adds 3 bonus points. Find the new mean and SD.</li><li>Does Khalid's z-score change after the conversion? Does his percentile rank? Explain.</li></ol>",
    f"<p><strong>1.</strong> 9 values are below 35: (9.5/20) × 100 = ⦃{fm(r35,1)}th⦄ percentile. P₈₀: c = 20·80/100 = 16, whole, so (16th + 17th)/2 = (41 + 43)/2 = ⦃{fm(p80[0])}⦄.</p>"
    f"<p><strong>2.</strong> z = (41 − {fm(mm,2)})/{fm(ms,3)} = ⦃{fm(z41,2)}⦄.</p>"
    f"<p><strong>3.</strong> New mean = 2({fm(mm,2)}) + 3 = ⦃{fm(2*mm+3,2)}⦄; new SD = 2({fm(ms,3)}) = ⦃{fm(2*ms,3)}⦄. The +3 does not affect the SD.</p>"
    f"<p><strong>4.</strong> <strong>Neither changes.</strong> New z = (85 − {fm(2*mm+3,2)})/{fm(2*ms,3)} = {fm((85-2*mm-3)/(2*ms),2)}: the shift cancels in the numerator and the ×2 cancels between numerator and denominator. The order of the students is unchanged, so every percentile rank is unchanged too. Position measures don't change under a positive linear transformation.</p>", marks=12)
add("C5", "C", ["3-1", "3-2", "3-3", "3-4"], "CLO3-B · CLO3-C",
    "<p>Monthly electricity bills (OMR) for samples of 40 homes in two Muscat neighbourhoods:</p>"
    "<div class=\"tbl-wrap\"><table><thead><tr><th></th><th class=\"num\">x̄</th><th class=\"num\">median</th><th class=\"num\">s</th><th class=\"num\">min</th><th class=\"num\">Q₁</th><th class=\"num\">Q₃</th><th class=\"num\">max</th></tr></thead><tbody>"
    "<tr><td>Al Khuwair</td><td class=\"num\">38.2</td><td class=\"num\">31.5</td><td class=\"num\">14.6</td><td class=\"num\">12</td><td class=\"num\">24</td><td class=\"num\">47</td><td class=\"num\">96</td></tr>"
    "<tr><td>Al Amerat</td><td class=\"num\">29.4</td><td class=\"num\">29.0</td><td class=\"num\">6.1</td><td class=\"num\">15</td><td class=\"num\">25</td><td class=\"num\">34</td><td class=\"num\">44</td></tr></tbody></table></div>"
    "<ol class=\"subs\"><li>Describe the shape of each distribution using two pieces of evidence.</li><li>Which neighbourhood's bills are more consistent? Justify.</li>"
    "<li>Check each data set for outliers.</li><li>Which measure of centre should be reported for each neighbourhood? Why?</li><li>At least how many Al Amerat homes have bills between 17.2 and 41.6 OMR?</li></ol>",
    f"<p><strong>1.</strong> Al Khuwair: mean 38.2 well above median 31.5; the right whisker (49) is much longer than the left (12): ⦃positively skewed⦄. Al Amerat: mean ≈ median (29.4 vs 29.0), the median is nearly centred in the box (4 above Q₁, 5 below Q₃) and the whiskers are equal (10 and 10): ⦃roughly symmetric⦄.</p>"
    f"<p><strong>2.</strong> CV: Al Khuwair 14.6/38.2 = {fm(14.6/38.2*100,1)}%; Al Amerat 6.1/29.4 = {fm(6.1/29.4*100,1)}%. ⦃Al Amerat⦄ is more consistent.</p>"
    "<p><strong>3.</strong> Al Khuwair: IQR 23, fences 24 − 34.5 = −10.5 and 47 + 34.5 = 81.5, so ⦃96 is an outlier⦄. Al Amerat: IQR 9, fences 11.5 and 47.5, so ⦃no outliers⦄.</p>"
    "<p><strong>4.</strong> Al Khuwair: the ⦃median⦄, because the data are skewed and contain an outlier that inflates the mean. Al Amerat: the ⦃mean⦄ (or either), because the data are roughly symmetric with no outliers.</p>"
    "<p><strong>5.</strong> 29.4 ± 2(6.1) = 17.2 to 41.6, so k = 2 and at least 75%: 0.75 × 40 = ⦃30 homes⦄.</p>", marks=14)

# ======================================================================== PART D · true/false with justification, find the mistake
TF = [
 ("3-2", "If the standard deviation of a data set is 0, all its values are equal.", "True", "s = 0 means Σ(X − x̄)² = 0, so every deviation is 0 and every value equals the mean."),
 ("3-1", "The median is always one of the data values.", "False", "For even n it is the mean of the two middle values: the median of 2, 4, 6, 8 is 5."),
 ("3-2", "Adding the same constant to every value changes the coefficient of variation.", "True", "The SD is unchanged but the mean shifts, so s/x̄ changes."),
 ("3-2", "Chebyshev's theorem says exactly 75% of values lie within 2 SD of the mean.", "False", "It guarantees at least 75%; the actual percentage is often higher."),
 ("3-4", "If Q₂ − Q₁ = Q₃ − Q₂, the distribution must be symmetric.", "False", "The whiskers can still differ: 1, 10, 11, 12, 13, 14, 15 has Q₁ = 10, Q₂ = 12, Q₃ = 14 (equal gaps of 2), but the left whisker is 9 and the right is 1, so it is left-skewed."),
 ("3-3", "The IQR can never be larger than the range.", "True", "Q₁ ≥ min and Q₃ ≤ max, so Q₃ − Q₁ ≤ max − min."),
 ("3-1", "In a negatively skewed distribution the mean is usually greater than the median.", "False", "The long left tail pulls the mean below the median."),
 ("3-2", "The variance of 5, 5, 5, 6 is larger than the variance of 1, 1, 1, 2.", "False", "The second set is the first minus 4. Shifting does not change the spread, so the variances are equal (0.25)."),
]
for i, (tag, st, ans, why) in enumerate(TF, 1):
    add(f"D{i}", "D", [tag], "CLO1-A · CLO3-C", f"<p><strong>True or false? Justify.</strong> {st}</p>", f"<p>⦃{ans}⦄. {why}</p>")
add("D9", "D", ["3-1"], "CLO2-A",
    "<p><strong>Find the mistake.</strong> \"The median of 9, 2, 7, 4, 6 is 7, the middle number.\"</p>",
    "<p>The data were not <strong>ordered</strong>. Ordered: 2, 4, 6, 7, 9, so the median is ⦃6⦄.</p>")
add("D10", "D", ["3-3"], "CLO2-A",
    "<p><strong>Find the mistake.</strong> For 20 ordered values a student found P₃₅ as follows: c = 20·35/100 = 7, \"so P₃₅ is the 7th value\".</p>",
    "<p>c = 7 is a <strong>whole number</strong>, so step 3B applies: P₃₅ is ⦃the mean of the 7th and 8th values⦄. Rounding up and taking a single value is step 3A, used only when c is a decimal.</p>")
add("D11", "D", ["3-3"], "CLO2-A",
    "<p><strong>Find the mistake.</strong> For the data 10, 12, 15, 15, 18, 20, 25, 30 a student found the percentile rank of 15 as (4 + 0.5)/8 × 100 = 56.25.</p>",
    "<p>The student counted the values <em>up to and including</em> 15 (four of them). The formula counts values strictly <strong>below</strong> X: only 10 and 12, so 2. Correct: (2 + 0.5)/8 × 100 = ⦃31.25th percentile⦄.</p>")
add("D12", "D", ["3-2"], "CLO3-C",
    "<p><strong>Find the mistake.</strong> A student says data set B (mean 200, s = 20) is more variable than data set A (mean 10, s = 3) \"because 20 &gt; 3\".</p>",
    "<p>The means differ hugely, so comparing raw SDs is invalid. CV<sub>A</sub> = 30% and CV<sub>B</sub> = 10%: ⦃A is relatively more variable⦄.</p>")

# ======================================================================== PART E · review self-study exercises (Hadhrami)
bb = [5.4, 5.5, 5.7, 5.8, 5.9, 6.1, 6.1, 6.4, 6.4, 6.5, 6.6, 6.7, 6.7, 6.7, 7.0, 7.0, 7.0, 7.1, 7.2, 7.2, 7.4, 7.5, 7.7, 7.7, 7.8, 8.0, 8.1, 8.1, 8.3, 8.7]
bm, bs = mean(bb), stdev(bb); b1, b2, b3 = quart(bb); kk = 1 / math.sqrt(.36); blo, bhi = bm - kk * bs, bm + kk * bs; bin_ = sum(blo < v < bhi for v in bb)
k = (40 - 26) / 3
add("E1", "E", ["3-2"], "CLO2-A · CLO3-C",
    "<p><strong>Review exercise (Dr. Ahmed).</strong> The average cost of a Talabat delivery is 26 OMR, and the <strong>variance</strong> of the cost is 9. One Thursday evening Talabat served only customers whose orders were <strong>outside</strong> the range 12 to 40 OMR. What is the maximum percentage of customers served that evening?</p>",
    f"<p>Variance 9, so s = 3. The interval is symmetric: 26 ± 14, so k = 14/3 = {fm(k,3)}. Chebyshev: at least 1 − 1/k² = 1 − 9/196 = {fm((1-1/k**2)*100,2)}% lie <em>inside</em>.</p>"
    f"<p>So at most 9/196 = ⦃{fm(100/k**2,2)}%⦄ lie outside: that is the maximum percentage served.</p>"
    "<p class=\"why\">Two traps: taking s = 9 (it is the variance), and answering with the \"inside\" percentage.</p>")
add("E2", "E", ["3-1", "3-2", "3-3"], "CLO2-A",
    f"<p><strong>Review exercise (Dr. Ahmed).</strong> Weights (pounds) of 30 newborn babies: {', '.join(fm(v) for v in bb)}.</p>"
    "<ol class=\"subs\"><li>Find the mode, median, mean and standard deviation.</li><li>Find the five-number summary and the interquartile range.</li><li>Find an interval centred at the mean that contains at least 64% of the data.</li><li>What percentage of the 30 weights actually lies in that interval?</li></ol>",
    f"<p><strong>(a)</strong> 6.7 and 7.0 each occur 3 times: ⦃bimodal, 6.7 and 7.0⦄. Median = (15th + 16th)/2 = (7.0 + 7.0)/2 = ⦃{fm(median(bb))}⦄. x̄ = {fm(sum(bb),1)}/30 = ⦃{fm(bm,3)}⦄. s = ⦃{fm(bs,3)}⦄ (sample).</p>"
    f"<p><strong>(b)</strong> Q₁ = median of the lower 15 = 8th value = {fm(b1)}; Q₃ = 23rd value = {fm(b3)}. Five-number summary: ⦃5.4, {fm(b1)}, {fm(b2)}, {fm(b3)}, 8.7⦄; IQR = ⦃{fm(b3-b1,2)}⦄.</p>"
    f"<p><strong>(c)</strong> 1 − 1/k² = 0.64, so k² = 1/0.36 and k = 5/3 ≈ 1.667. Interval: {fm(bm,3)} ± 1.667({fm(bs,3)}) = ⦃{fm(blo,3)} to {fm(bhi,3)}⦄.</p>"
    f"<p><strong>(d)</strong> Only 5.4 and 8.7 fall outside, so {bin_} of 30 = ⦃{fm(bin_/30*100,2)}%⦄, well above the guaranteed 64%.</p>", marks=14)
add("E3", "E", ["3-1"], "CLO3-B · CLO3-C",
    "<p><strong>Review exercise (Dr. Ahmed).</strong> STAT 2101 students collected the annual maximum temperature (°C) in Muscat for ten years from 2011: mean = 51.3, mode = 46.5, median = 52. What is the shape of the distribution?</p>",
    "<p>The decisive comparison is mean vs median: 51.3 &lt; 52, so the mean is pulled toward a left tail: ⦃negatively (left) skewed⦄.</p>"
    "<p class=\"why\">The mode (46.5) does not fit the textbook ordering mean &lt; median &lt; mode. With only ten values the mode is unstable (any repeated value becomes the mode), so base the conclusion on mean vs median and say why.</p>")

# ======================================================================== PART F · In-Class Quiz I simulation
f2 = [8, 12, 15, 15, 17, 21, 24, 40]; f3 = [6, 9, 10, 13, 17]; S3, S32 = sum(f3), sum(v * v for v in f3); f3s2 = (5 * S32 - S3 ** 2) / 20
add("F1", "F", ["3-1"], "CLO1-A", "<p><strong>[3 marks]</strong> Parameter or statistic? (a) The mean GPA of all 2025 SQU graduates. (b) The SD of travel time for 60 students surveyed at the library. (c) The proportion of 500 sampled Omani households owning an electric car.</p>",
    "<p>(a) ⦃parameter⦄: all graduates form the population. (b) ⦃statistic⦄: a sample of 60. (c) ⦃statistic⦄: a sample proportion, p̂.</p>")
add("F2", "F", ["3-1"], "CLO2-A · CLO3-C", f"<p><strong>[4 marks]</strong> The number of emails received on 8 days: {', '.join(map(str, f2))}. Find the mean, median and mode. Which best describes a typical day? Why?</p>",
    f"<p>x̄ = {sum(f2)}/8 = ⦃{fm(mean(f2))}⦄; median = (15 + 17)/2 = ⦃{fm(median(f2))}⦄; mode = ⦃15⦄. The ⦃median⦄ best describes a typical day: the single 40-email day pulls the mean up, and the data are right-skewed (mode &lt; median &lt; mean).</p>")
add("F3", "F", ["3-2"], "CLO2-A", f"<p><strong>[4 marks]</strong> A sample of five values: {', '.join(map(str, f3))}. Using the shortcut formula, find the standard deviation and the coefficient of variation.</p>",
    f"<p>ΣX = {S3}, ΣX² = {S32}. s² = [5({S32}) − {S3}²]/(5·4) = ({5*S32} − {S3**2})/20 = {fm(f3s2,3)}, so s = ⦃{fm(math.sqrt(f3s2),3)}⦄. x̄ = 11, so CV = ⦃{fm(math.sqrt(f3s2)/11*100,2)}%⦄.</p>")
add("F4", "F", ["3-2"], "CLO2-A", "<p><strong>[3 marks]</strong> A sample of 80 commute times has mean 120 minutes and s = 15. Without assuming any shape, at least how many commutes lie between 82.5 and 157.5 minutes?</p>",
    f"<p>k = (157.5 − 120)/15 = 2.5, so at least 1 − 1/6.25 = 84%. 0.84 × 80 = 67.2, rounded up: at least ⦃68 commutes⦄.</p>")
add("F5", "F", ["3-3"], "CLO3-C", "<p><strong>[3 marks]</strong> Aisha scored 72 in Statistics (class mean 64, s = 5) and 81 in Calculus (class mean 75, s = 4). In which subject is her relative position better?</p>",
    "<p>z<sub>Stat</sub> = (72 − 64)/5 = 1.6 and z<sub>Calc</sub> = (81 − 75)/4 = 1.5: ⦃Statistics⦄, though the margin is small.</p>")
add("F6", "F", ["3-4"], "CLO3-B", "<p><strong>[3 marks]</strong> The five-number summary of a data set is 20, 45, 70, 75, 80. Describe the shape and give two pieces of evidence. What percentage of values are at most 45?</p>",
    "<p>The median (70) is much closer to Q₃ (5 below) than to Q₁ (25 above), and the left whisker (25) is far longer than the right (5): ⦃negatively skewed⦄. At most 45 is at or below Q₁: ⦃25%⦄.</p>")
