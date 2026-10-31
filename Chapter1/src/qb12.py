"""Chapter 1 and Chapter 2 exam-style question banks. Numeric answers are computed, never typed by hand."""
import math, itertools, sys
sys.path.insert(0, "/tmp/claude-0/-home-user-STAT2101/521e5d47-fbd3-5206-8b60-93d1c3cc1629/scratchpad/ch3")
from ch3lib import *

Q1, Q2 = [], []
def add(Q, id, part, tags, clo, q, a, marks=None):
    Q.append(dict(id=id, part=part, tags=tags, clo=clo, q=q, a=a, marks=marks))
def mcq(opts):
    return '<ul class="opts">' + "".join(f"<li>({k}) {v}</li>" for k, v in zip("abcd", opts)) + "</ul>"
def fm(x, d=2):
    s = f"{x:.{d}f}".rstrip("0").rstrip("."); return s
def tbl(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    b = "".join("<tr>" + "".join(f'<td class="num">{c}</td>' for c in r) + "</tr>" for r in rows)
    return f'<div class="tbl-wrap"><table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'

ROW = "06512 07836 88456 36313 30879 51323 76451 25578 15986 50845 57015 53684 57054 93261"
def srs(dig, N, n):
    r = ROW.replace(" ", ""); out = []; log = []
    for i in range(0, len(r) - dig + 1, dig):
        if len(out) == n: break
        c = r[i:i + dig]; v = int(c)
        if v < 1 or v > N: log.append(f"<s>{c}</s>")
        elif v in out: log.append(f"<s>{c}</s>")
        else: out.append(v); log.append(c)
    return out, log

# =============================================================== CHAPTER 1
A1 = [
 ("1-1", "CLO1-A", "A researcher asked 400 Muscat households about car ownership and reports: \"62% of the households surveyed own two or more cars.\" This statement is:",
  ["inferential, because it comes from a sample", "descriptive, because it only describes the 400 households surveyed", "inferential, because it is a percentage", "neither, because no graph is used"], "b",
  "It reports what was observed in the people actually asked. Being from a sample doesn't make a statement inferential; <strong>generalising</strong> beyond the sample does."),
 ("1-1", "CLO1-A", "From the same 400 households the researcher writes: \"About 62% of <strong>all</strong> Muscat households own two or more cars.\" This statement is:",
  ["descriptive", "inferential", "a census result", "a parameter computed from the population"], "b",
  "The claim moves from the sample to all Muscat households, so it is a generalisation from sample to population: inferential."),
 ("1-1", "CLO1-A", "The SQU registrar computes the mean GPA of <strong>every</strong> 2025 graduate. Which description is correct?",
  ["a survey producing a statistic", "a census producing a parameter, summarised with descriptive statistics", "inferential statistics, because a mean was calculated", "a biased sample"], "b",
  "Every member of the defined population was measured: a census. A measure of a whole population is a parameter, and reporting it is descriptive."),
 ("1-2", "CLO1-B", "Which variable is <strong>qualitative</strong>?",
  ["number of absences in a semester", "student ID number", "waiting time at a clinic", "annual rainfall in Salalah"], "b",
  "An ID is a number used only as a label: arithmetic on it is meaningless, so it is qualitative (nominal)."),
 ("1-2", "CLO1-B", "The <strong>year</strong> a car was manufactured is measured at the:",
  ["nominal level", "ordinal level", "interval level", "ratio level"], "c",
  "Differences between years are meaningful (2020 is 5 years after 2015), but year 0 does not mean \"no time\", so there is no true zero."),
 ("1-2", "CLO1-B", "Which statement is meaningful <strong>only</strong> because the variable is at the ratio level?",
  ["30 °C is twice as hot as 15 °C", "a 6-hour flight lasts twice as long as a 3-hour flight", "an IQ of 140 is twice as intelligent as 70", "grade A is twice as good as grade C"], "b",
  "Time <em>duration</em> has a true zero, so ratios are valid. °C and IQ are interval; grades are ordinal."),
 ("1-2", "CLO1-B", "Customers rate a service 1 = very poor, 2 = poor, 3 = fair, 4 = good, 5 = excellent. The level of measurement is:",
  ["nominal", "ordinal", "interval", "ratio"], "b",
  "The numbers only code an order. The gap from poor to fair is not known to equal the gap from good to excellent."),
 ("1-2", "CLO1-B", "The number of patients visiting a clinic each day is:",
  ["qualitative, nominal", "quantitative, continuous, interval", "quantitative, discrete, ratio", "quantitative, discrete, interval"], "c",
  "It is counted (discrete), and 0 patients means none (true zero), so it is ratio."),
 ("1-3", "CLO1-C", "A traffic officer checks every 20th car leaving a mall car park, starting with a randomly chosen car among the first 20. The method is:",
  ["simple random", "systematic", "stratified", "cluster"], "b", "Every k-th member, k = 20, from a random start."),
 ("1-3", "CLO1-C", "SQU randomly selects 3 of its colleges and surveys <strong>every</strong> student in those colleges. The method is:",
  ["stratified, because colleges are groups", "cluster", "systematic", "convenience"], "b",
  "Some groups are chosen and all their members included: cluster. Stratified would take students from <em>every</em> college."),
 ("1-3", "CLO1-C", "A TV programme asks viewers to send an SMS to vote on a new law. The sample is:",
  ["simple random, because anyone can vote", "a volunteer (self-selected) sample, likely biased", "cluster", "a census of viewers"], "b",
  "The respondents decide for themselves whether to take part, so those with strong opinions are over-represented."),
 ("1-3", "CLO1-C", "In a random sample of 200 students, 48% support a policy; the true figure for all students is 51%. The 3% difference is best described as:",
  ["nonsampling error", "sampling error", "a biased sample", "a recording error"], "b",
  "A random sample differs from the population purely by chance: sampling error."),
 ("1-3", "CLO1-C", "A clinic's scale is miscalibrated and adds 0.5 kg to every weight. This produces:",
  ["sampling error", "nonsampling error", "no error, because it is the same for everyone", "a cluster effect"], "b",
  "An instrument error is a nonsampling error. Taking a larger sample would not remove it."),
 ("1-3", "CLO1-C", "Which feature is <strong>essential</strong> to a stratified sample?",
  ["equal numbers from each stratum", "a random sample drawn from every stratum", "only some strata are sampled", "every member of a stratum is included"], "b",
  "Every stratum must be represented by a random sample. Sizes do not have to be equal (Dr. Amani's note)."),
]
for i, (tag, clo, q, opts, ans, why) in enumerate(A1, 1):
    add(Q1, f"A{i}", "A", [tag], clo, f"<p>{q}</p>{mcq(opts)}", f"<p>⦃({ans})⦄</p><p class=\"why\">{why}</p>")

add(Q1, "B1", "B", ["1-1"], "CLO1-A",
    "<p>To study daily study hours of all 3,500 first-year SQU students, a researcher asks 150 randomly chosen first-year students; their mean is 2.4 hours. Identify (a) the population and N, (b) the sample and n, (c) the variable with its type and level, (d) whether 2.4 is a parameter or a statistic, (e) the branch of statistics if the researcher concludes \"first-year students study about 2.4 hours a day\".</p>",
    "<p>(a) ⦃all 3,500 first-year SQU students, N = 3500⦄. (b) ⦃the 150 students asked, n = 150⦄. (c) ⦃daily study hours: quantitative, continuous, ratio⦄. (d) ⦃statistic⦄: it comes from the sample. (e) ⦃inferential⦄: the conclusion is about all first-year students.</p>")
add(Q1, "B2", "B", ["1-1"], "CLO1-A",
    "<p>Census or survey? Justify each. (a) The NCSI collects data on every person, household and building in Oman. (b) SQU emails a questionnaire to 300 randomly chosen students. (c) A teacher records the marks of every student in her class in order to describe that class.</p>",
    "<p>(a) ⦃census⦄: every member of the population. (b) ⦃survey⦄: a sample. (c) ⦃census⦄: the population is defined as <em>her class</em>, and all of it is measured. Whether something is a census depends on how the population is defined.</p>")
add(Q1, "B3", "B", ["1-2"], "CLO1-B",
    "<p>Give the type (qualitative or quantitative, discrete or continuous) and the level of measurement of each: (a) governorate of residence (b) number of siblings (c) body temperature in °C (d) customer rating poor / fair / good / excellent (e) time to finish an exam, in minutes (f) Oman Air flight number WY101.</p>",
    "<p>(a) ⦃qualitative, nominal⦄ (b) ⦃quantitative, discrete, ratio⦄ (c) ⦃quantitative, continuous, interval⦄ (d) ⦃qualitative, ordinal⦄ (e) ⦃quantitative, continuous, ratio⦄: a duration (f) ⦃qualitative, nominal⦄: a label, even though it contains digits.</p>")
add(Q1, "B4", "B", ["1-2"], "CLO1-B",
    "<p>Find the boundaries of each recorded value: (a) 48 kg (b) GPA 3.7 (c) 0.125 s.</p>",
    "<p>(a) ⦃47.5–48.5 kg⦄ (±0.5) (b) ⦃3.65–3.75⦄ (±0.05) (c) ⦃0.1245–0.1255 s⦄ (±0.0005)</p><p class=\"why\">Half of one unit of the <em>last recorded digit</em>, each way.</p>")
add(Q1, "B5", "B", ["1-2"], "CLO1-B · CLO3-C",
    "<p>\"Muscat's temperature rose from 20 °C in January to 40 °C in June, so June is twice as hot.\" Evaluate the claim.</p>",
    "<p>⦃Invalid.⦄ Temperature in °C is <strong>interval</strong>: 0 °C is not an absence of heat, so ratios are meaningless. Only the difference (+20 °C) is meaningful. On the Kelvin scale, a ratio scale, the temperatures are 293.15 K and 313.15 K, a ratio of only about 1.07.</p>")
add(Q1, "B6", "B", ["1-2"], "CLO1-B",
    "<p>Two students describe \"number of goals scored in a match\". Student A: \"quantitative, continuous, because it can be large.\" Student B: \"quantitative, discrete, ratio.\" Who is right, and what is wrong with the other answer?</p>",
    "<p>⦃Student B.⦄ Goals are <strong>counted</strong>, so the variable is discrete however large the counts get; 0 goals means none, so it is ratio. Continuous means <em>measured</em>, with infinitely many values between any two, which is not the same as \"can be large\".</p>")
o, log = srs(3, 750, 6)
add(Q1, "B7", "B", ["1-3"], "CLO1-C",
    f"<p>A company has N = 750 employees numbered 001–750. Select a simple random sample of n = 6 using Table D, starting at row 2, column 1 ({ROW}).</p>",
    f"<p>N has 3 digits, so read 3-digit groups: {' '.join(log)}.</p><p>Sample: ⦃{', '.join(f'{v:03d}' for v in o)}⦄. 783 is skipped because it is greater than 750.</p>")
add(Q1, "B8", "B", ["1-3"], "CLO1-C",
    "<p>A list of 250 patients is to be sampled systematically, n = 12. (a) Find k and list the sample if the random start is 7. (b) A student rounds k up to 21 and the random start happens to be 21. What goes wrong?</p>",
    f"<p>(a) k = 250/12 = 20.83, rounded <strong>down</strong> to ⦃20⦄. Sample: ⦃{', '.join(str(7 + 20 * i) for i in range(12))}⦄.</p><p>(b) 21, 42, …, 231, then the 12th would be 252 &gt; 250: only ⦃11 patients⦄. Rounding up can leave the sample short, which is why the rule rounds down.</p>")
add(Q1, "B9", "B", ["1-3"], "CLO1-C · CLO3-C",
    "<p>A researcher wants to compare study habits of male and female SQU students, but females are about two-thirds of the students. Explain why a stratified sample is better than a simple random sample here, and describe how to take it.</p>",
    "<p>An SRS might, by chance, contain too few of one gender to compare reliably. ⦃Stratify by gender⦄: list males and females separately, then draw a random sample (for example by Table D or a computer) from <strong>each</strong> stratum. This guarantees both genders are represented; the two sample sizes may be equal or different.</p>")
add(Q1, "B10", "B", ["1-3"], "CLO1-C",
    "<p>Name the sampling method and say whether it is likely to be biased: (a) the first 30 shoppers to enter Lulu on Saturday morning (b) an online poll on a news website that anyone can answer (c) the names of all 2,000 employees are placed in a box and 40 are drawn.</p>",
    "<p>(a) ⦃convenience, biased⦄: early Saturday shoppers are not typical. (b) ⦃volunteer, biased⦄: self-selected respondents with strong views. (c) ⦃simple random (lottery method), unbiased⦄, provided the slips are well mixed.</p>")
add(Q1, "B11", "B", ["1-3"], "CLO1-C",
    "<p>The Ministry of Education wants grade-10 maths scores. Plan P: randomly pick 10 of the 120 schools and test every grade-10 student in them. Plan Q: in every one of the 120 schools, randomly pick 5 grade-10 students. Name each plan and give one advantage of each.</p>",
    "<p>P is ⦃cluster⦄: cheaper and faster, with only 10 sites to visit. Q is ⦃stratified⦄ (schools as strata): every school is represented, but all 120 schools must be visited.</p>")
add(Q1, "B12", "B", ["1-3"], "CLO1-C",
    "<p><strong>Find the mistake.</strong> For 86 trees and n = 6, a student used k = 15 and a random start of 13: \"13, 28, 43, 58, 73, 88\".</p>",
    "<p>Tree 88 does not exist (N = 86). k should be 86/6 = 14.33, rounded <strong>down</strong> to 14. With start 13: ⦃13, 27, 41, 55, 69, 83⦄.</p>")
add(Q1, "B13", "B", ["1-3"], "CLO1-C",
    "<p><strong>Find the mistake.</strong> For N = 4998 laptops, a student read Table D row 2 in 5-digit groups and chose laptops 06512 and 07836 first.</p>",
    "<p>The groups must have the same number of digits as N, which is <strong>4</strong>. 06512 = 6512 &gt; 4998 would be rejected anyway. The correct start is ⦃0651, 2078, 3688, 4563, …⦄.</p>")
add(Q1, "B14", "B", ["1-1", "1-3"], "CLO1-A · CLO1-C · CLO3-C",
    "<p>A website surveys 50 members of a \"sleep well\" club, who volunteered, and concludes: \"Students who sleep more get higher GPAs.\" (a) Which branch of statistics is the conclusion? (b) Which sampling method was used? (c) Give two reasons to doubt the conclusion.</p>",
    "<p>(a) ⦃inferential⦄: a general claim about a relationship. (b) ⦃volunteer (self-selected)⦄. (c) The sample is biased (club members who chose to answer are not typical students), and 50 people is small. A survey can also only show an association: it doesn't prove that sleeping more <em>causes</em> a higher GPA.</p>")

add(Q1, "C1", "C", ["1-2"], "CLO1-B",
    "<p>An SQU hospital record contains: (a) name (b) age in years (c) weight in kg (d) condition: critical / serious / fair / good (e) date of admission (f) number of previous visits (g) ward number (h) body temperature in °C (i) blood type. For each, state qualitative or quantitative (and discrete or continuous) and the level of measurement.</p>",
    "<p>(a) ⦃qualitative, nominal⦄ (b) ⦃quantitative, continuous, ratio⦄ (c) ⦃quantitative, continuous, ratio⦄ (d) ⦃qualitative, ordinal⦄ (e) ⦃quantitative, interval⦄: a date has no true zero (f) ⦃quantitative, discrete, ratio⦄ (g) ⦃qualitative, nominal⦄: a label (h) ⦃quantitative, continuous, interval⦄ (i) ⦃qualitative, nominal⦄</p>", marks=9)
add(Q1, "C2", "C", ["1-1", "1-2", "1-3"], "CLO1-A · B · C",
    "<p>The Oman Traffic Authority wants to know the average daily driving time of licensed drivers in Oman. It plans to ask a sample of 1,200 drivers.</p><ol class=\"subs\"><li>State the population, the sample and the variable, with the variable's type and level.</li><li>Describe a stratified design and a cluster design for this study.</li><li>Give one possible nonsampling error.</li><li>Classify: (i) \"The 1,200 drivers averaged 74 minutes a day.\" (ii) \"Omani drivers spend between 70 and 78 minutes a day driving.\"</li></ol>",
    "<p><strong>1.</strong> Population ⦃all licensed drivers in Oman⦄; sample ⦃the 1,200 drivers asked⦄; variable ⦃daily driving time: quantitative, continuous, ratio⦄.</p><p><strong>2.</strong> Stratified: divide drivers by governorate (or by experience: under 5, 5–10, over 10 years) and take a random sample from <strong>each</strong> group. Cluster: treat, say, licensing centres or wilayats as clusters, randomly choose some, and survey <strong>all</strong> drivers registered there.</p><p><strong>3.</strong> Drivers misremember or exaggerate their time; data-entry errors; a badly worded question.</p><p><strong>4.</strong> (i) ⦃descriptive⦄ (ii) ⦃inferential⦄: an estimate for all Omani drivers.</p>", marks=10)
o2, log2 = srs(3, 480, 8)
add(Q1, "C3", "C", ["1-3"], "CLO1-C",
    f"<p>A college lists its 480 students, numbered 001–480. Table D row 2: {ROW}.</p><ol class=\"subs\"><li>Select a simple random sample of 8 students starting at row 2, column 1.</li><li>Select a systematic sample of 8: find k, and take the random start as the first 2-digit number in row 2 that is between 01 and k.</li><li>The college wants both male and female students represented. Which method should it use, and how?</li></ol>",
    f"<p><strong>1.</strong> 3-digit groups: {' '.join(log2)}. Sample: ⦃{', '.join(f'{v:03d}' for v in o2)}⦄.</p><p><strong>2.</strong> k = 480/8 = ⦃60⦄. The first 2-digit group is 06, which lies in 01–60, so the start is 6: ⦃6, 66, 126, 186, 246, 306, 366, 426⦄.</p><p><strong>3.</strong> ⦃Stratified by gender⦄: a random sample from the male list and one from the female list.</p>", marks=10)
add(Q1, "C4", "C", ["1-2"], "CLO1-B · CLO3-C",
    "<p>A survey records: (i) gender, (ii) satisfaction coded 1–5, (iii) room temperature in °C, (iv) monthly income in OMR. For each variable, state the level and say whether each comparison is meaningful: \"is different from\", \"is greater than\", \"is 10 units more than\", \"is twice\".</p>",
    "<p>(i) ⦃nominal⦄: only \"different from\". (ii) ⦃ordinal⦄: \"different\" and \"greater than\"; a 10-unit difference has no fixed meaning. (iii) ⦃interval⦄: different, greater, 10 units more; <strong>not</strong> twice. (iv) ⦃ratio⦄: all four, so OMR 800 is twice OMR 400.</p>", marks=8)

TF1 = [
 ("1-2", "Every quantitative variable is measured at either the interval or the ratio level.", "True", "Nominal and ordinal data are categories (qualitative); numerical data with meaningful differences are interval or ratio."),
 ("1-2", "A discrete variable cannot be at the ratio level.", "False", "The number of children is discrete and ratio: 0 means none, and 4 is twice 2."),
 ("1-3", "A census has no sampling error.", "True", "Sampling error comes from measuring only part of the population. A census can still have nonsampling errors such as recording mistakes."),
 ("1-3", "Taking a larger sample removes nonsampling error.", "False", "A defective instrument or a biased question gives wrong data at any sample size."),
 ("1-3", "In cluster sampling, every cluster contributes some members to the sample.", "False", "Only the randomly chosen clusters do, with all their members. \"Some from every group\" describes stratified sampling."),
 ("1-3", "In stratified sampling, the same number must be taken from each stratum.", "False", "Dr. Amani's note: the sizes need not be equal, e.g. 12 from Statistics and 24 from Mathematics."),
 ("1-2", "Postal codes are quantitative because they are numbers.", "False", "They are labels; averaging them is meaningless. Qualitative, nominal."),
 ("1-3", "A convenience sample becomes unbiased if it is large enough.", "False", "Size does not fix how subjects were chosen. A large biased sample is still biased."),
]
for i, (tag, st, ans, why) in enumerate(TF1, 1):
    add(Q1, f"D{i}", "D", [tag], "CLO1-B · CLO1-C", f"<p><strong>True or false? Justify.</strong> {st}</p>", f"<p>⦃{ans}⦄. {why}</p>")

add(Q1, "E1", "E", ["1-2"], "CLO1-B",
    "<p><strong>Review exercise (Dr. Ahmed).</strong> Name the level of measurement: (a) ranking of data, a precise difference between units of measure, and a true zero; (b) mutually exclusive categories that can be ranked, but without precise differences between ranks; (c) mutually exclusive categories with no order or ranking; (d) ranking and precise differences, but no true zero.</p>",
    "<p>(a) ⦃ratio⦄ (b) ⦃ordinal⦄ (c) ⦃nominal⦄ (d) ⦃interval⦄</p>")
add(Q1, "E2", "E", ["1-2"], "CLO1-B",
    "<p><strong>Review exercise (Dr. Ahmed).</strong> An SQU hospital patient record shows: (a) Name: Ibrahim Ahmed (b) Age: 35 years (c) Condition: Fair (d) Date of admission: May 15 2019. State the type of data and the level of measurement of each.</p>",
    "<p>(a) ⦃qualitative, nominal⦄ (b) ⦃quantitative (continuous), ratio⦄ (c) ⦃qualitative, ordinal⦄ (d) ⦃quantitative, interval⦄: dates have meaningful differences but no true zero (Dr. Ahmed's interval list).</p>")

add(Q1, "F1", "F", ["1-1"], "CLO1-A", "<p><strong>[2 marks]</strong> Define <em>inferential statistics</em> and give an example from Oman.</p>",
    "<p>Generalising from samples to populations, performing estimations and hypothesis tests, determining relationships among variables, and making predictions. Example: ⦃the Ministry of Health surveys a sample of hospitals in November to predict next November's national flu cases⦄.</p>")
add(Q1, "F2", "F", ["1-2"], "CLO1-B", "<p><strong>[4 marks]</strong> Type and level: (a) number of credit hours registered (b) Likert response \"agree\" (c) graduation year (d) distance from home to SQU in km.</p>",
    "<p>(a) ⦃quantitative, discrete, ratio⦄ (b) ⦃qualitative, ordinal⦄ (c) ⦃quantitative, interval⦄ (d) ⦃quantitative, continuous, ratio⦄</p>")
add(Q1, "F3", "F", ["1-3"], "CLO1-C", "<p><strong>[4 marks]</strong> Name the method: (a) every 15th invoice is audited (b) 4 of 11 governorates are chosen at random and all hospitals in them are surveyed (c) 10 nurses are randomly chosen from each department (d) a lottery draws 25 student IDs.</p>",
    "<p>(a) ⦃systematic⦄ (b) ⦃cluster⦄ (c) ⦃stratified⦄ (d) ⦃simple random⦄</p>")
add(Q1, "F4", "F", ["1-3"], "CLO1-C", "<p><strong>[3 marks]</strong> N = 92 and n = 7 for a systematic sample. Find k and the sample if the random start is 9.</p>",
    f"<p>k = 92/7 = 13.14, rounded down to ⦃13⦄. Sample: ⦃{', '.join(str(9 + 13 * i) for i in range(7))}⦄.</p>")
add(Q1, "F5", "F", ["1-2"], "CLO1-B", "<p><strong>[2 marks]</strong> Find the boundaries of 7.25 g and of 120 cm.</p>",
    "<p>⦃7.245–7.255 g⦄ and ⦃119.5–120.5 cm⦄</p>")

# =============================================================== CHAPTER 2
A2 = [
 ("2-1", "CLO2-B", "A grouped distribution of whole-number ages has classes 35–44, 45–54, 55–64. The class width is:", ["9", "9.5", "10", "11"], "c",
  "Width = UCL − LCL + 1 = 44 − 35 + 1 = 10 (or the next LCL − this LCL = 45 − 35). The value 9 is the classic trap."),
 ("2-1", "CLO2-B", "Data range from 18 to 60 and 6 classes are required. The class width should be:", ["7", "7.5", "8", "6"], "c",
  "42/6 = 7 exactly, but the width is rounded <strong>up</strong> even from a whole number. With width 7, six classes cover only 18–59 and miss the value 60."),
 ("2-1", "CLO2-B", "Which is <strong>not</strong> a requirement of a grouped frequency distribution?", ["classes are mutually exclusive", "classes are continuous", "all classes have the same width", "every class contains at least one value"], "d",
  "A class with no values stays in the table with f = 0."),
 ("2-1", "CLO2-B", "A class has relative frequency 0.15 in a data set of 60 values. Its frequency is:", ["6", "9", "15", "0.25"], "b", "f = RF × n = 0.15 × 60 = 9."),
 ("2-2", "CLO3-A", "On a frequency polygon, the points are plotted against the:", ["class limits", "lower class boundaries", "class midpoints", "upper class boundaries"], "c",
  "Midpoints for polygons; boundaries for histograms; upper boundaries for ogives."),
 ("2-2", "CLO3-A", "The first point of an ogive is plotted at:", ["(first midpoint, first frequency)", "(first lower boundary, 0)", "(first upper boundary, 0)", "(0, 0)"], "b",
  "The line starts at zero on the first lower class boundary."),
 ("2-2", "CLO3-B", "Part of an ogive is perfectly horizontal. This means:", ["that class contains the most values", "that class has frequency 0", "the data are uniform", "the graph is drawn incorrectly"], "b",
  "The cumulative frequency does not increase across the class, so no values fall in it (the 52.5–60.5 drivers class)."),
 ("2-2", "CLO3-B", "A histogram's tallest bar is near the left and the bars trail off to the right. The distribution is:", ["left-skewed", "right-skewed", "J-shaped", "uniform"], "b", "Skew is named after the long tail, here on the right."),
 ("2-3", "CLO2-C", "The nationality of 200 tourists is best displayed with a:", ["histogram", "ogive", "bar graph", "time series graph"], "c",
  "Nationality is qualitative (nominal), so a bar graph or pie chart. Histograms and ogives need quantitative classes."),
 ("2-3", "CLO2-C", "In a pie chart, a category holding 15% of the data has a sector of:", ["15°", "36°", "54°", "150°"], "c", "0.15 × 360° = 54°."),
 ("2-3", "CLO3-B", "In a stacked bar, the \"female\" section runs from 20 up to 35 on the y-axis. The number of females is:", ["35", "20", "15", "55"], "c",
  "A section's frequency is its top minus its bottom: 35 − 20."),
 ("2-3", "CLO3-A", "A stem-and-leaf plot's key reads 4 | 7 = 0.47. The row \"3 | 2 8\" represents:", ["3.2 and 3.8", "32 and 38", "0.32 and 0.38", "0.032 and 0.038"], "c", "Same place values as the key: stem tenths, leaf hundredths."),
]
for i, (tag, clo, q, opts, ans, why) in enumerate(A2, 1):
    add(Q2, f"A{i}", "A", [tag], clo, f"<p>{q}</p>{mcq(opts)}", f"<p>⦃({ans})⦄</p><p class=\"why\">{why}</p>")

# B1 grouped construction with whole-number width trap
wait = [12, 25, 31, 18, 44, 27, 35, 22, 15, 29, 38, 41, 20, 33, 26, 19, 47, 30, 24, 36, 28, 16, 39, 21, 32, 45, 23, 34, 27, 30]
L, H = min(wait), max(wait); k = 5; w = (H - L) / k; W = math.floor(w) + 1
rows = []; cf = 0
for i in range(k):
    lo = L + i * W; hi = lo + W - 1; f = sum(lo <= v <= hi for v in wait); cf += f
    rows.append((f"{lo}–{hi}", f"{lo - .5}–{hi + .5}", f, fm(f / len(wait), 3), cf))
add(Q2, "B1", "B", ["2-1"], "CLO2-B",
    f"<p>Waiting times (minutes) of 30 patients: {', '.join(map(str, wait))}. Construct a grouped frequency distribution with <strong>5 classes</strong>, including boundaries, f, RF and CF.</p>",
    f"<p>R = {H} − {L} = {H - L}; width = {H - L}/5 = {fm(w)}, a whole number, but still rounded <strong>up</strong> to ⦃{W}⦄. With width 7, the five classes would end at {L + 5 * 7 - 1} and miss {H}.</p>"
    + tbl(["Limits", "Boundaries", "f", "RF", "CF"], rows) +
    f"<p>Check: Σf = {sum(r[2] for r in rows)} = n ✓. The last class reaches {L + 5 * W - 1} ≥ {H} ✓.</p>")
add(Q2, "B2", "B", ["2-1"], "CLO2-B",
    "<p>Complete the table (n = 40):</p>" + tbl(["Class", "f", "RF", "CF"], [["10–19", "3", "", "3"], ["20–29", "?", "", "11"], ["30–39", "12", "", "?"], ["40–49", "?", "", "36"], ["50–59", "?", "", "40"]]) + "<p>Then find the percentage of values below 39.5.</p>",
    "<p>f₂ = 11 − 3 = ⦃8⦄; CF₃ = 11 + 12 = ⦃23⦄; f₄ = 36 − 23 = ⦃13⦄; f₅ = 40 − 36 = ⦃4⦄. RF: 0.075, 0.2, 0.3, 0.325, 0.1 (sum 1).</p><p>Below 39.5 = CF of the third class: 23/40 = ⦃57.5%⦄.</p>")
add(Q2, "B3", "B", ["2-1"], "CLO2-B",
    "<p>A distribution has class boundaries 15.5–20.5, 20.5–25.5, 25.5–30.5, 30.5–35.5. Find the class limits, the class width and the midpoints.</p>",
    "<p>Limits: ⦃16–20, 21–25, 26–30, 31–35⦄ (add and subtract 0.5). Width ⦃5⦄ (= 20.5 − 15.5). Midpoints ⦃18, 23, 28, 33⦄.</p>")
majors = {"Statistics": 9, "Mathematics": 12, "Physics": 6, "Chemistry": 8, "Biology": 5}
add(Q2, "B4", "B", ["2-1", "2-3"], "CLO2-B · CLO3-B",
    "<p>The majors of 40 College of Science students: Statistics 9, Mathematics 12, Physics 6, Chemistry 8, Biology 5. Build the categorical distribution with percentages and pie angles, and write one sentence of interpretation.</p>",
    tbl(["Major", "f", "%", "degrees"], [[m, f, fm(f / 40 * 100, 1), f"{f / 40 * 360:g}°"] for m, f in majors.items()] + [["<strong>Total</strong>", 40, 100, "360°"]]) +
    "<p>⦃Mathematics is the most common major (30%)⦄, while Biology is the least (12.5%).</p>")
add(Q2, "B5", "B", ["2-2"], "CLO3-B",
    "<p>Use the cumulative frequencies of the record-temperature ogive (Example 2-4): less than 99.5 → 0, 104.5 → 2, 109.5 → 10, 114.5 → 28, 119.5 → 41, 124.5 → 48, 129.5 → 49, 134.5 → 50. (a) How many states had a record of at least 114.5 °F? (b) What percentage had records between 109.5 and 124.5 °F? (c) Which class has the most states, and how can you tell from the ogive?</p>",
    "<p>(a) 50 − 28 = ⦃22 states⦄. (b) (48 − 10)/50 = ⦃76%⦄. (c) ⦃109.5–114.5⦄ (18 states): the ogive's steepest segment.</p>")
add(Q2, "B6", "B", ["2-2"], "CLO2-C",
    "<p>For the classes 20–29 (f 4), 30–39 (f 9), 40–49 (f 15), 50–59 (f 7), 60–69 (f 5), list every point you would plot for (a) the frequency polygon and (b) the ogive.</p>",
    "<p>(a) Midpoints with the extra empty classes: ⦃(14.5, 0), (24.5, 4), (34.5, 9), (44.5, 15), (54.5, 7), (64.5, 5), (74.5, 0)⦄.</p><p>(b) Upper boundaries with CF, starting at the first lower boundary: ⦃(19.5, 0), (29.5, 4), (39.5, 13), (49.5, 28), (59.5, 35), (69.5, 40)⦄.</p>")
add(Q2, "B7", "B", ["2-2"], "CLO3-B",
    "<p>Name the shape of each histogram, read left to right: (a) 2, 5, 9, 14, 10, 6, 3 (b) 15, 10, 6, 4, 2, 1 (c) 8, 3, 2, 3, 9 (d) 3, 9, 4, 3, 8, 3 (e) 6, 6, 7, 6, 6, 7</p>",
    "<p>(a) ⦃bell-shaped⦄ (b) ⦃reverse J-shaped⦄: highest at the left and falling steadily (c) ⦃U-shaped⦄ (d) ⦃bimodal⦄ (e) ⦃uniform⦄</p>")
add(Q2, "B8", "B", ["2-2"], "CLO2-C · CLO3-A",
    "<p><strong>Find the mistakes.</strong> A student drew a histogram of the temperature data with bars centred on 100–104, 105–109, …, a gap between bars, no axis labels, and the y-axis starting at 2.</p>",
    "<p>(1) The x-axis must show <strong>boundaries</strong> (99.5, 104.5, …), not limits. (2) Histogram bars must <strong>touch</strong>. (3) Title and axis labels are required. (4) A frequency axis should start at 0. If an axis doesn't start at 0, mark the break with a zig-zag.</p>")
trans = {"Bus": 14, "Car": 18, "Walk": 5, "Taxi": 3}
add(Q2, "B9", "B", ["2-3"], "CLO2-C",
    "<p>40 students travel to SQU by bus 14, car 18, walk 5, taxi 3. Find each pie angle and percentage. Which two categories together make up more than three-quarters of the circle?</p>",
    tbl(["Mode", "f", "%", "degrees"], [[m, f, fm(f / 40 * 100, 1), f"{f / 40 * 360:g}°"] for m, f in trans.items()]) + "<p>⦃Car and bus: 32/40 = 80%, i.e. 288°⦄.</p>")
add(Q2, "B10", "B", ["2-3"], "CLO3-B",
    "<p>A stacked bar graph of Year 1 to Year 3 STAT 2101 enrolments has male sections from 0 to 14, 0 to 18 and 0 to 22, and female sections on top reaching 25, 34 and 40. Build the frequency table and state one insight.</p>",
    tbl(["Year", "Males", "Females", "Total"], [["1", 14, "25 − 14 = 11", 25], ["2", 18, "34 − 18 = 16", 34], ["3", 22, "40 − 22 = 18", 40]]) +
    "<p>⦃Enrolment grows every year (25 → 40)⦄, and males outnumber females each year.</p>")
dec = [1.3, 1.5, 1.8, 2.0, 2.2, 2.2, 2.4, 2.7, 2.9, 3.1, 3.3, 3.4, 3.4, 3.6, 3.8, 4.1, 4.5]
from collections import defaultdict
stems = defaultdict(list)
for v in dec: stems[int(v)].append(str(round(v * 10) % 10))
plot = "\n".join(f"{s} | {' '.join(stems[s])}" for s in range(1, 5))
add(Q2, "B11", "B", ["2-3"], "CLO2-C · CLO3-B",
    f"<p>Draw a stem-and-leaf plot with a key for the reaction times (s): {', '.join(map(str, dec))}. Then give the shape and the peak.</p>",
    f'<p class="fx" style="white-space:pre;line-height:1.5">{plot}      key: 1 | 3 = 1.3 s</p><p>Leaf counts 3, 6, 6, 2: ⦃roughly symmetric (mound-shaped)⦄, with the peak of ⦃6⦄ values at stems 2 and 3.</p>')
add(Q2, "B12", "B", ["2-3"], "CLO3-B",
    "<p>Monthly sales (OMR thousands) of a Muscat shop: Jan 42, Feb 45, Mar 51, Apr 49, May 58, Jun 66, Jul 71. Describe the trend, and say between which two consecutive months the change was fastest.</p>",
    "<p>⦃Upward trend⦄: sales rose from 42 to 71 (+29), with a single dip in April. The fastest change was ⦃May to June (+8)⦄, the steepest segment.</p>")
add(Q2, "B13", "B", ["2-2", "2-3"], "CLO2-C",
    "<p>Choose the most suitable graph and justify it: (a) the daily number of COVID cases in Oman over a year (b) favourite mobile brand of 150 students (c) the ages of 500 patients, to see the shape (d) the percentage of the national budget spent on each sector (e) how many of 500 patients are younger than 40</p>",
    "<p>(a) ⦃time series⦄: change over time (b) ⦃bar graph⦄: categorical (c) ⦃histogram⦄ (or frequency polygon): quantitative shape (d) ⦃pie⦄: parts of a whole (e) ⦃ogive⦄: counts below a value</p>")

# C1 full grouped workup
temps = [29, 33, 35, 31, 38, 41, 36, 34, 30, 37, 39, 42, 35, 33, 36, 40, 44, 38, 32, 37, 35, 34, 39, 36, 41, 37, 33, 38, 36, 35, 27, 40, 34, 37, 36, 38, 43, 35, 39, 36]
L, H, k = min(temps), max(temps), 6; w = (H - L) / k; W = math.ceil(w) if w != int(w) else int(w) + 1
rows = []; cf = 0; fs = []
for i in range(k):
    lo = L + i * W; hi = lo + W - 1; f = sum(lo <= v <= hi for v in temps); cf += f; fs.append(f)
    rows.append((f"{lo}–{hi}", f"{lo - .5}–{hi + .5}", fm((lo + hi) / 2, 1), f, fm(f / 40, 3), cf, fm(cf / 40, 3)))
peak = max(range(k), key=lambda i: fs[i])
below = rows[2][5]
add(Q2, "C1", "C", ["2-1", "2-2"], "CLO2-B · CLO2-C · CLO3-B",
    f"<p>Maximum temperatures (°C) in Muscat on 40 days: {', '.join(map(str, temps))}.</p><ol class=\"subs\"><li>Construct a grouped distribution with <strong>6 classes</strong>: limits, boundaries, midpoints, f, RF, CF, CRF.</li><li>Which class is modal? Describe the shape.</li><li>On how many days was the maximum below {L + 3 * W - .5}? What percentage is that?</li><li>List the x-values you would use for the histogram, the frequency polygon and the ogive.</li></ol>",
    f"<p><strong>1.</strong> R = {H} − {L} = {H - L}; width = {fm(w, 3)} → ⦃{W}⦄.</p>" +
    tbl(["Limits", "Boundaries", "Midpoint", "f", "RF", "CF", "CRF"], rows) +
    f"<p><strong>2.</strong> Modal class ⦃{rows[peak][0]}⦄ (f = {fs[peak]}). The frequencies {', '.join(map(str, fs))} rise to one central peak and fall away: ⦃roughly bell-shaped⦄.</p>"
    f"<p><strong>3.</strong> CF at {L + 3 * W - .5} = ⦃{below} days⦄, i.e. {fm(below / 40 * 100, 1)}%.</p>"
    f"<p><strong>4.</strong> Histogram: boundaries {L - .5}, {L + W - .5}, …, {L + k * W - .5}. Polygon: midpoints {fm(L + (W - 1) / 2 - W, 1)} (extra), {', '.join(r[2] for r in rows)}, {fm(L + (W - 1) / 2 + k * W, 1)} (extra). Ogive: {L - .5} (CF 0), then each upper boundary.</p>", marks=16)
add(Q2, "C2", "C", ["2-1", "2-2"], "CLO2-B · CLO3-B",
    "<p>Read this distribution of exam times (minutes):</p>" + tbl(["Boundaries", "f"], [["29.5–39.5", 4], ["39.5–49.5", 7], ["49.5–59.5", 13], ["59.5–69.5", 10], ["69.5–79.5", 6]]) +
    "<ol class=\"subs\"><li>Find the class width, the class limits and n.</li><li>Find the midpoints and the relative frequencies.</li><li>What percentage of students took less than 59.5 minutes?</li><li>Between which two boundaries does the ogive rise most steeply? Why?</li></ol>",
    "<p><strong>1.</strong> Width ⦃10⦄; limits ⦃30–39, 40–49, 50–59, 60–69, 70–79⦄; n = ⦃40⦄.</p><p><strong>2.</strong> Midpoints 34.5, 44.5, 54.5, 64.5, 74.5; RF 0.10, 0.175, 0.325, 0.25, 0.15.</p><p><strong>3.</strong> (4 + 7 + 13)/40 = ⦃60%⦄.</p><p><strong>4.</strong> ⦃49.5–59.5⦄: it holds the largest frequency (13), so the CF climbs fastest there.</p>", marks=10)
add(Q2, "C3", "C", ["2-1", "2-3"], "CLO2-B · CLO2-C · CLO3-C",
    "<p>60 SQU students named their preferred study place: library 21, home 18, café 9, lab 12. Among them, males chose library 9, home 11, café 4, lab 6.</p><ol class=\"subs\"><li>Build the frequency distribution with percentages.</li><li>Find the pie-chart angles.</li><li>Build the male/female table and describe how a grouped and a stacked bar graph would display it.</li><li>Give two insights.</li></ol>",
    tbl(["Place", "f", "%", "degrees", "Males", "Females"], [["Library", 21, 35, "126°", 9, 12], ["Home", 18, 30, "108°", 11, 7], ["Café", 9, 15, "54°", 4, 5], ["Lab", 12, 20, "72°", 6, 6], ["<strong>Total</strong>", 60, 100, "360°", 30, 30]]) +
    "<p><strong>3.</strong> Grouped: two bars side by side (male, female) for each place. Stacked: one bar per place of total height f, split into a male section and a female section on top.</p><p><strong>4.</strong> ⦃The library is the most popular place (35%)⦄; ⦃home is preferred more by males (11 vs 7), the library more by females (12 vs 9)⦄.</p>", marks=12)

TF2 = [
 ("2-1", "A class with frequency 0 may be left out of a grouped distribution.", "False", "Classes must be continuous, so the empty class stays with f = 0."),
 ("2-1", "If range ÷ number of classes is exactly 6, the class width is 6.", "False", "Round up even from a whole number, to 7. Otherwise the largest value falls outside the last class."),
 ("2-2", "An ogive can go down.", "False", "Cumulative frequency never decreases. It is flat when a class is empty."),
 ("2-2", "A histogram and a bar graph differ only in colour.", "False", "A histogram shows quantitative classes on a number line with touching bars; a bar graph shows categories with separated bars."),
 ("2-3", "A stem-and-leaf plot keeps the original data values.", "True", "Every value can be read back from its stem and leaf, which a histogram cannot do."),
 ("2-3", "The angles in a correctly drawn pie chart must add to 360°.", "True", "The parts must make up the whole circle."),
 ("2-2", "A relative frequency histogram has a different shape from the frequency histogram of the same data.", "False", "Every bar is divided by the same n, so only the y-scale changes."),
 ("2-1", "The class width can be found as (upper boundary − lower boundary) + 1.", "False", "That gives 9 for the class 20.5–28.5, whose width is 8. Use UCB − LCB, or UCL − LCL + 1."),
]
for i, (tag, st, ans, why) in enumerate(TF2, 1):
    add(Q2, f"D{i}", "D", [tag], "CLO2-B · CLO3-A", f"<p><strong>True or false? Justify.</strong> {st}</p>", f"<p>⦃{ans}⦄. {why}</p>")

add(Q2, "F1", "F", ["2-1"], "CLO2-B", "<p><strong>[3 marks]</strong> Data range from 47 to 92 and 5 classes are required. Find the width and the first two classes (limits and boundaries).</p>",
    "<p>45/5 = 9, a whole number, so rounded up to ⦃10⦄. Classes ⦃47–56 (46.5–56.5)⦄ and ⦃57–66 (56.5–66.5)⦄.</p>")
add(Q2, "F2", "F", ["2-1"], "CLO2-B", "<p><strong>[3 marks]</strong> Frequencies 6, 11, 15, 8 (n = 40). Find the CF and CRF of the third class, and the RF of the fourth class.</p>",
    "<p>CF₃ = ⦃32⦄; CRF₃ = ⦃0.8⦄; RF₄ = 8/40 = ⦃0.2⦄.</p>")
add(Q2, "F3", "F", ["2-2"], "CLO3-A", "<p><strong>[3 marks]</strong> For the class 120–129, give the value used on the x-axis of a histogram, a frequency polygon and an ogive.</p>",
    "<p>Histogram: boundaries ⦃119.5–129.5⦄; polygon: midpoint ⦃124.5⦄; ogive: upper boundary ⦃129.5⦄.</p>")
add(Q2, "F4", "F", ["2-3"], "CLO2-C", "<p><strong>[3 marks]</strong> A category has 27 of 120 observations. Find its percentage and its pie angle.</p>",
    "<p>27/120 = ⦃22.5%⦄; 0.225 × 360 = ⦃81°⦄.</p>")
add(Q2, "F5", "F", ["2-3"], "CLO3-B", "<p><strong>[3 marks]</strong> Stem-and-leaf (key 5 | 2 = 52): 4 | 1 3 · 5 | 0 2 4 7 · 6 | 1 3 3 5 6 8 9 · 7 | 0 2 4 5 · 8 | 1. How many values? What is the peak? What is the shape?</p>",
    "<p>n = 2 + 4 + 7 + 4 + 1 = ⦃18⦄; peak ⦃7 values in the 60s⦄; ⦃roughly bell-shaped (symmetric)⦄.</p>")
