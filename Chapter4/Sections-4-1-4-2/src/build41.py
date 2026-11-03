"""Exam-style question set for STAT 2101 sections 4-1 and 4-2 only. Every numeric answer is computed here."""
import os, sys, json, itertools
from fractions import Fraction as Fr
sys.path.insert(0, "/tmp/claude-0/-home-user-STAT2101/521e5d47-fbd3-5206-8b60-93d1c3cc1629/scratchpad/ch3")
from ch3lib import head, markup

def p(n, d=None, dp=4):
    f = Fr(n, d) if d is not None else Fr(n)
    dec = f"{float(f):.{dp}f}".rstrip("0").rstrip(".")
    if f.denominator == 1: return dec
    raw = f"{n}/{d}" if d is not None and Fr(n, d) != Fr(n, d).limit_denominator(1) else ""
    s = f"{raw} = " if raw and raw != f"{f.numerator}/{f.denominator}" else ""
    return f"{s}{f.numerator}/{f.denominator} ≈ {dec}"
def dec(x, dp=4): return f"{x:.{dp}f}".rstrip("0").rstrip(".")
def tbl(head_, rows):
    h = "".join(f"<th>{c}</th>" for c in head_)
    b = "".join("<tr>" + "".join(f'<td class="num">{c}</td>' for c in r) + "</tr>" for r in rows)
    return f'<div class="tbl-wrap"><table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'
def mcq(o): return '<ul class="opts">' + "".join(f"<li>({k}) {v}</li>" for k, v in zip("abcd", o)) + "</ul>"

dice = [(a, b) for a in range(1, 7) for b in range(1, 7)]
def dcount(f): return sum(1 for a, b in dice if f(a, b))
coins3 = ["".join(t) for t in itertools.product("HT", repeat=3)]
kids4 = ["".join(t) for t in itertools.product("BG", repeat=4)]

Q = []
def add(id, part, tags, q, a, marks=None): Q.append(dict(id=id, part=part, tags=tags, q=q, a=a, marks=marks))

# ------------------------------------------------------------------ Part A · MCQ
primes = {2, 3, 5, 7, 11}; npr = dcount(lambda a, b: a + b in primes)
A = [
 ("4-1", f"Two fair dice are rolled. The probability that the sum is a <strong>prime number</strong> is:", ["1/3", "5/12", "4/11", "1/2"], "b",
  f"Primes 2, 3, 5, 7, 11 occur 1 + 2 + 4 + 6 + 2 = {npr} times out of 36: {p(npr, 36)}. Option (c) uses 11 possible sums as if they were equally likely, which they are not."),
 ("4-1", "Three fair coins are tossed. P(at least two heads) =", ["3/8", "1/2", "1/4", "7/8"], "b",
  f"At least two = exactly two or three: {{HHT, HTH, THH, HHH}}, 4 of 8 outcomes = 0.5. (a) counts only <em>exactly</em> two."),
 ("4-1", "Which value <strong>cannot</strong> be the probability of an event?", ["0", "1", "−0.02", "0.999"], "c", "0 ≤ P(E) ≤ 1, so a negative value is impossible."),
 ("4-1", "The outcomes of an experiment have probabilities 0.20, 0.35, k and 0.15. The value of k is:", ["0.25", "0.30", "0.70", "cannot be found"], "b",
  "The probabilities of all outcomes in S add to 1: k = 1 − 0.70 = 0.30."),
 ("4-1", "Of 1,200 SQU students surveyed, 360 said they use the bus, so P(bus) = 0.30. This is:", ["classical probability", "empirical probability", "subjective probability", "a compound event"], "b",
  "It is computed from observed frequencies, f/n, so it is empirical."),
 ("4-1", "A physician says there is a 25% chance a patient will need surgery, based on her experience. This is:", ["classical", "empirical", "subjective", "impossible to classify"], "c",
  "An expert's educated estimate, with no sample space counted and no data table: subjective."),
 ("4-1", "If P(E) = 0.27, then P(Ē) is:", ["0.27", "0.73", "−0.27", "1.27"], "b", "P(Ē) = 1 − P(E) = 0.73."),
 ("4-1", "Five students sit a quiz. The complement of \"<strong>at least 2</strong> students pass\" is:", ["at most 2 pass", "fewer than 2 pass", "exactly 2 pass", "more than 2 fail"], "b",
  "\"At least 2\" means 2, 3, 4 or 5 pass, so its complement is 0 or 1 pass: fewer than 2 (that is, at most 1)."),
 ("4-1", "A card is drawn from a standard 52-card deck. P(red face card) =", ["3/26", "3/13", "1/2", "6/13"], "a",
  "There are 6 red face cards (J, Q, K of hearts and of diamonds): 6/52 = 3/26."),
 ("4-1", "When a single die is rolled, which event has probability 1?", ["a number greater than 0", "an even number", "a 6", "a number greater than 6"], "a",
  "Every face is greater than 0, so the event is certain. A number greater than 6 is impossible (probability 0)."),
 ("4-2", "On one die, A = {2, 4, 6} and B = {1, 2, 3}. P(A or B) =", ["1", "5/6", "2/3", "1/2"], "b",
  "A ∩ B = {2}, so the events are not mutually exclusive: 3/6 + 3/6 − 1/6 = 5/6. Option (a) forgets to subtract the overlap."),
 ("4-2", "A and B are mutually exclusive with P(A) = 0.45 and P(B) = 0.30. Then P(A ∪ B) and P(A ∩ B) are:", ["0.75 and 0.135", "0.75 and 0", "0.615 and 0", "0.75 and 0.75"], "b",
  "Mutually exclusive: P(A ∩ B) = 0, and P(A ∪ B) = P(A) + P(B) = 0.75. Option (a) multiplies, as if the events were independent."),
 ("4-2", "P(A) = 0.6 and P(B) = 0.5. Which statement is <strong>certainly true</strong>?", ["A and B are mutually exclusive", "A and B cannot be mutually exclusive", "P(A ∪ B) = 1.1", "P(A ∩ B) = 0"], "b",
  "If they were mutually exclusive, P(A ∪ B) would be 1.1 > 1, which is impossible. So they must overlap, with P(A ∩ B) ≥ 0.1."),
 ("4-2", "P(A ∪ B) = 0.7, P(A) = 0.4 and P(B) = 0.5. Then P(A ∩ B) =", ["0.2", "0.1", "0.3", "0.9"], "a", "P(A ∩ B) = P(A) + P(B) − P(A ∪ B) = 0.9 − 0.7 = 0.2."),
 ("4-2", "A card is drawn from a standard deck. P(queen or club) =", ["17/52", "4/13", "1/52", "1/4"], "b",
  "4/52 + 13/52 − 1/52 = 16/52 = 4/13. The queen of clubs is counted in both events, so subtract it once."),
 ("4-2", "P(A) = 0.5 and P(A ∩ B) = 0.2. The probability that A occurs but B does not is:", ["0.7", "0.3", "0.1", "0.25"], "b", "A only = P(A) − P(A ∩ B) = 0.3."),
]
for i, (t, q, o, ans, why) in enumerate(A, 1):
    add(f"A{i}", "A", [t], f"<p>{q}</p>{mcq(o)}", f"<p>⦃({ans})⦄</p><p class=\"why\">{why}</p>")

# ------------------------------------------------------------------ Part B · short structured
g2 = [s for s in kids4 if s.count("G") == 2]
add("B1", "B", ["4-1"],
    "<p><strong>[4 marks]</strong> A family has four children. (a) Write the sample space S and state n(S). (b) Find P(exactly two girls). (c) Find P(at least one boy). (d) Find P(the first and last child are of the same gender).</p>",
    f"<p>(a) S = {{{', '.join(kids4)}}}, ⦃n(S) = 16⦄.</p><p>(b) E = {{{', '.join(g2)}}}, n(E) = 6, so P = 6/16 = ⦃0.375⦄.</p>"
    f"<p>(c) Complement of \"no boys\" = {{GGGG}}: 1 − 1/16 = ⦃15/16 ≈ 0.9375⦄.</p>"
    f"<p>(d) {sum(1 for s in kids4 if s[0] == s[3])} outcomes have matching first and last letters: 8/16 = ⦃0.5⦄.</p>")
s8 = dcount(lambda a, b: a + b == 8); s4 = dcount(lambda a, b: a + b <= 4); dbl = dcount(lambda a, b: a == b)
d_or_8 = dcount(lambda a, b: a == b or a + b == 8); diff2 = dcount(lambda a, b: abs(a - b) == 2)
add("B2", "B", ["4-1", "4-2"],
    "<p><strong>[5 marks]</strong> Two fair dice are rolled. Find: (a) P(sum is 8) (b) P(sum is at most 4) (c) P(doubles or a sum of 8) (d) P(the two numbers differ by exactly 2) (e) P(sum is greater than 12).</p>",
    f"<p>n(S) = 36.</p><p>(a) {{(2,6), (3,5), (4,4), (5,3), (6,2)}}: ⦃{p(s8, 36)}⦄.</p>"
    f"<p>(b) Sums 2, 3, 4 → 1 + 2 + 3 = {s4}: ⦃{p(s4, 36)}⦄. \"At most 4\" includes 4.</p>"
    f"<p>(c) Doubles 6, sum 8 five, and (4,4) is in both: (6 + 5 − 1)/36 = ⦃{p(d_or_8, 36)}⦄.</p>"
    f"<p>(d) (1,3), (3,1), (2,4), (4,2), (3,5), (5,3), (4,6), (6,4): ⦃{p(diff2, 36)}⦄.</p><p>(e) ⦃0⦄: impossible, because the largest sum is 12.</p>")
vis = [("0", 12), ("1", 30), ("2", 25), ("3", 18), ("4 or more", 15)]; n = 100
add("B3", "B", ["4-1"],
    "<p><strong>[4 marks]</strong> The number of visits 100 students made to the SQU clinic last semester:</p>" + tbl(["Visits", "Students"], vis) +
    "<p>For a student chosen at random, find: (a) P(exactly 2 visits) (b) P(at most 1 visit) (c) P(at least 3 visits) (d) P(more than 1 but fewer than 4 visits).</p>",
    "<p>Empirical probability, f/n with n = 100.</p><p>(a) 25/100 = ⦃0.25⦄ (b) 0 and 1: (12 + 30)/100 = ⦃0.42⦄ (c) 3 and \"4 or more\": (18 + 15)/100 = ⦃0.33⦄ (d) only 2 and 3: (25 + 18)/100 = ⦃0.43⦄</p>"
    "<p class=\"why\">Check: at most 1, exactly 2 and at least 3 cover every student once: 0.42 + 0.25 + 0.33 = 1 ✓.</p>")
S = set(range(1, 16)); A3 = {x for x in S if x % 3 == 0}; Bo = {x for x in S if x % 2}
U = A3 | Bo; I = A3 & Bo
fmt = lambda s: "{" + ", ".join(map(str, sorted(s))) + "}"
add("B4", "B", ["4-1", "4-2"],
    "<p><strong>[5 marks]</strong> A number is chosen at random from S = {1, 2, …, 15}. Let A = \"a multiple of 3\" and B = \"an odd number\". (a) Write A, B, A ∩ B, A ∪ B, Ā and (A ∪ B)ᶜ. (b) Find P(A ∪ B) using the addition rule and check it by counting. (c) Are A and B mutually exclusive? Explain.</p>",
    f"<p>(a) A = {fmt(A3)}; B = {fmt(Bo)}; A ∩ B = {fmt(I)}; A ∪ B = {fmt(U)}; Ā = {fmt(S - A3)}; (A ∪ B)ᶜ = {fmt(S - U)}.</p>"
    f"<p>(b) {len(A3)}/15 + {len(Bo)}/15 − {len(I)}/15 = ⦃{p(len(U), 15)}⦄ ✓ (n(A ∪ B) = {len(U)}).</p>"
    f"<p>(c) ⦃No⦄: A ∩ B = {fmt(I)} ≠ ∅.</p>")
car = {"Science": 30, "Engineering": 45, "Arts": 25}; bus = {"Science": 40, "Engineering": 20, "Arts": 40}
add("B5", "B", ["4-1", "4-2"],
    "<p><strong>[6 marks]</strong> 200 SQU students were classified by college and transport:</p>" +
    tbl(["", "Car", "Bus", "Total"], [["Science", 30, 40, 70], ["Engineering", 45, 20, 65], ["Arts", 25, 40, 65], ["<strong>Total</strong>", 100, 100, 200]]) +
    "<p>A student is selected at random. Find: (a) P(Engineering) (b) P(Engineering and bus) (c) P(Engineering or bus) (d) P(Science or Arts) (e) P(neither Engineering nor car). (f) Are \"Engineering\" and \"bus\" mutually exclusive? Justify.</p>",
    "<p>(a) 65/200 = ⦃0.325⦄ (b) one cell: 20/200 = ⦃0.10⦄ (c) (65 + 100 − 20)/200 = 145/200 = ⦃0.725⦄ (d) mutually exclusive colleges: (70 + 65)/200 = ⦃0.675⦄ "
    "(e) not Engineering and not car = Science-bus + Arts-bus = (40 + 40)/200 = ⦃0.40⦄ (f) ⦃No⦄: 20 students are both, so P(E ∩ Bus) = 0.10 ≠ 0.</p>")
pa, pb, pu = .35, .45, .62; pi = pa + pb - pu
add("B6", "B", ["4-2"],
    "<p><strong>[4 marks]</strong> P(A) = 0.35, P(B) = 0.45 and P(A ∪ B) = 0.62. Find: (a) P(A ∩ B) (b) P(A but not B) (c) P(neither A nor B) (d) P(exactly one of A and B).</p>",
    f"<p>(a) 0.35 + 0.45 − 0.62 = ⦃{dec(pi)}⦄ (b) 0.35 − {dec(pi)} = ⦃{dec(pa - pi)}⦄ (c) 1 − 0.62 = ⦃{dec(1 - pu)}⦄ "
    f"(d) A only + B only = {dec(pa - pi)} + {dec(pb - pi)} = ⦃{dec(pu - pi)}⦄ (or P(A ∪ B) − P(A ∩ B)).</p>"
    f"<p class=\"why\">Draw the Venn diagram first: {dec(pa - pi)} | {dec(pi)} | {dec(pb - pi)} | outside {dec(1 - pu)}. The four regions add to 1 ✓.</p>")
add("B7", "B", ["4-2"],
    "<p><strong>[3 marks]</strong> In a phone shop, 32% of buyers choose Samsung, 41% Apple and 15% Huawei; each buyer buys one phone. Find: (a) P(Samsung or Apple) (b) P(another brand) (c) P(not Apple).</p>",
    "<p>The brands are mutually exclusive. (a) 0.32 + 0.41 = ⦃0.73⦄ (b) 1 − (0.32 + 0.41 + 0.15) = ⦃0.12⦄ (c) 1 − 0.41 = ⦃0.59⦄</p>")
M, Ph, Ch, MP, MC, PC, MPC, N = 50, 40, 30, 15, 10, 8, 5, 100
atl = M + Ph + Ch - MP - MC - PC + MPC; onlyM = M - MP - MC + MPC
add("B8", "B", ["4-2"],
    "<p><strong>[4 marks]</strong> Of 100 first-year students, 50 take Math, 40 Physics and 30 Chemistry; 15 take Math and Physics, 10 Math and Chemistry, 8 Physics and Chemistry, and 5 take all three. For a student chosen at random, find: (a) P(at least one of the three) (b) P(none) (c) P(Math only).</p>",
    f"<p>(a) Extended addition rule: (50 + 40 + 30 − 15 − 10 − 8 + 5)/100 = ⦃{dec(atl / N)}⦄ (b) 1 − {dec(atl / N)} = ⦃{dec(1 - atl / N)}⦄ "
    f"(c) 50 − 15 − 10 + 5 = {onlyM}, so ⦃{dec(onlyM / N)}⦄. Add 5 back because the triple overlap was subtracted twice.</p>")
add("B9", "B", ["4-1"],
    "<p><strong>[2 marks] Find the mistake.</strong> \"Two coins are tossed. S = {two heads, one head, no heads}, so P(exactly one head) = 1/3.\"</p>",
    "<p>Those three outcomes are not equally likely, so classical probability does not apply to them. The equally likely sample space is S = {HH, HT, TH, TT}, and P(exactly one head) = 2/4 = ⦃0.5⦄.</p>")
add("B10", "B", ["4-2"],
    "<p><strong>[2 marks] Find the mistake.</strong> \"P(king or heart) = 4/52 + 13/52 = 17/52.\"</p>",
    "<p>The king of hearts is counted twice; the events are not mutually exclusive. Correct: 4/52 + 13/52 − 1/52 = ⦃16/52 = 4/13⦄.</p>")
add("B11", "B", ["4-1"],
    "<p><strong>[2 marks]</strong> An event E is three times as likely to occur as not to occur. Find P(E).</p>",
    "<p>P(E) = 3P(Ē) = 3(1 − P(E)), so 4P(E) = 3 and P(E) = ⦃0.75⦄.</p>")
Eg, Fr_, nei, tot = 70, 45, 25, 120; both = Eg + Fr_ - (tot - nei)
add("B12", "B", ["4-2"],
    "<p><strong>[4 marks]</strong> In a company of 120 employees, 70 speak English, 45 speak French and 25 speak neither. An employee is chosen at random. Find: (a) P(speaks both) (b) P(speaks exactly one of the two) (c) P(speaks French only).</p>",
    f"<p>English or French = 120 − 25 = 95, so both = 70 + 45 − 95 = {both}.</p>"
    f"<p>(a) ⦃{p(both, 120)}⦄ (b) (95 − {both})/120 = ⦃{p(95 - both, 120)}⦄ (c) (45 − {both})/120 = ⦃{p(45 - both, 120)}⦄</p>")
ev = dcount(lambda a, b: a * b % 2 == 0)
add("B13", "B", ["4-1"],
    "<p><strong>[2 marks]</strong> Two dice are rolled. Find P(the product of the two numbers is even).</p>",
    f"<p>The product is odd only when both numbers are odd: 3 × 3 = 9 outcomes. P(even) = 1 − 9/36 = ⦃{p(ev, 36)}⦄.</p>")
add("B14", "B", ["4-2"],
    "<p><strong>[3 marks]</strong> Are the two events mutually exclusive? Explain. (a) A student is a STAT 2101 student; the student is a Science student. (b) Rolling one die: an odd number; a number greater than 5. (c) A card is a spade; the card is red.</p>",
    "<p>(a) ⦃Not mutually exclusive⦄: a Science student can be taking STAT 2101. (b) ⦃Mutually exclusive⦄: odd = {1, 3, 5} and greater than 5 = {6}, so the intersection is empty. (c) ⦃Mutually exclusive⦄: spades are black.</p>")

# ------------------------------------------------------------------ Part C · long questions
bt = {"O+": 70, "O−": 14, "A+": 56, "A−": 10, "B+": 24, "B−": 6, "AB+": 16, "AB−": 4}; nb = 200
neg = sum(v for k, v in bt.items() if k.endswith("−")); Aty = bt["A+"] + bt["A−"]
add("C1", "C", ["4-1", "4-2"],
    "<p>Blood types of 200 donors at the SQU Hospital blood bank:</p>" +
    tbl(["", "O", "A", "B", "AB", "Total"], [["Rh+", 70, 56, 24, 16, 166], ["Rh−", 14, 10, 6, 4, 34], ["<strong>Total</strong>", 84, 66, 30, 20, 200]]) +
    "<ol class=\"subs\"><li>What type of probability is used here, and why?</li><li>P(Rh−)</li><li>P(type A or Rh−)</li><li>P(neither type O nor Rh+)</li><li>P(type A or type B); name the rule you used.</li><li>P(not AB)</li><li>Are \"type O\" and \"Rh−\" mutually exclusive?</li></ol>",
    f"<p><strong>1.</strong> ⦃Empirical⦄: it comes from observed frequencies (f/n).</p><p><strong>2.</strong> {neg}/200 = ⦃{dec(neg / nb)}⦄</p>"
    f"<p><strong>3.</strong> Not mutually exclusive (A− = 10): (66 + 34 − 10)/200 = ⦃{dec((Aty + neg - 10) / nb)}⦄</p>"
    "<p><strong>4.</strong> Not O and not Rh+, i.e. A−, B− or AB−: (10 + 6 + 4)/200 = ⦃0.10⦄</p>"
    "<p><strong>5.</strong> Addition rule 1 (a donor has one type): (66 + 30)/200 = ⦃0.48⦄</p><p><strong>6.</strong> 1 − 20/200 = ⦃0.90⦄</p>"
    "<p><strong>7.</strong> ⦃No⦄: 14 donors are O−.</p>", marks=12)
add("C2", "C", ["4-1", "4-2"],
    "<p>A coin is tossed and then a die is rolled.</p><ol class=\"subs\"><li>Draw a tree diagram and list the sample space. What is n(S)?</li><li>P(a head and an even number)</li><li>P(a head or an even number)</li><li>P(a tail and a number greater than 4)</li><li>Are \"head\" and \"6\" mutually exclusive?</li></ol>",
    "<p><strong>1.</strong> S = {H1, H2, H3, H4, H5, H6, T1, T2, T3, T4, T5, T6}, ⦃n(S) = 12⦄.</p><p><strong>2.</strong> {H2, H4, H6}: 3/12 = ⦃0.25⦄</p>"
    "<p><strong>3.</strong> 6/12 + 6/12 − 3/12 = ⦃9/12 = 0.75⦄</p><p><strong>4.</strong> {T5, T6}: ⦃2/12 ≈ 0.1667⦄</p><p><strong>5.</strong> ⦃No⦄: H6 belongs to both.</p>", marks=8)
odd = dcount(lambda a, b: (a + b) % 2); gt9 = dcount(lambda a, b: a + b > 9); oddgt9 = dcount(lambda a, b: (a + b) % 2 and a + b > 9)
f6or7 = dcount(lambda a, b: a == 6 or a + b == 7); s7or11 = dcount(lambda a, b: a + b in (7, 11))
add("C3", "C", ["4-1", "4-2"],
    "<p>Two fair dice, one red and one green, are rolled.</p><ol class=\"subs\"><li>State n(S) and explain why the outcomes are equally likely.</li><li>P(the sum is odd)</li><li>P(the sum is odd or greater than 9)</li><li>P(the red die shows 6 or the sum is 7)</li><li>A player wins with a sum of 7 or 11. Find P(win) and P(lose).</li></ol>",
    "<p><strong>1.</strong> ⦃36⦄ ordered pairs (red, green); the dice are fair, so each pair has probability 1/36.</p>"
    f"<p><strong>2.</strong> ⦃{p(odd, 36)}⦄</p><p><strong>3.</strong> sum &gt; 9 has {gt9} outcomes and odd-and-&gt;9 (sum 11) has {oddgt9}: (18 + {gt9} − {oddgt9})/36 = ⦃{p(odd + gt9 - oddgt9, 36)}⦄</p>"
    f"<p><strong>4.</strong> red 6: 6 outcomes; sum 7: 6 outcomes; (6, 1) is in both: (6 + 6 − 1)/36 = ⦃{p(f6or7, 36)}⦄</p>"
    f"<p><strong>5.</strong> Mutually exclusive sums: (6 + 2)/36 = ⦃{p(s7or11, 36)}⦄; P(lose) = ⦃{p(36 - s7or11, 36)}⦄</p>", marks=10)
ages = [("18–25", 9), ("26–33", 14), ("34–41", 12), ("42–49", 10), ("50–57", 5)]; na = 50
add("C4", "C", ["4-1", "4-2"],
    "<p>Ages of 50 customers at a Muscat bank branch:</p>" + tbl(["Age", "Customers"], ages) +
    "<ol class=\"subs\"><li>P(a customer is 34–41)</li><li>P(a customer is at least 42)</li><li>P(a customer is younger than 34 or older than 49)</li><li>P(a customer is not in the 26–33 class)</li><li>Can you find P(a customer is younger than 30) from this table? Explain.</li></ol>",
    "<p><strong>1.</strong> 12/50 = ⦃0.24⦄ <strong>2.</strong> (10 + 5)/50 = ⦃0.30⦄ <strong>3.</strong> (9 + 14 + 5)/50 = ⦃0.56⦄ (mutually exclusive classes) <strong>4.</strong> 1 − 14/50 = ⦃0.72⦄</p>"
    "<p><strong>5.</strong> ⦃No⦄: 30 falls inside the 26–33 class, and the table doesn't show how those 14 ages split around 30.</p>", marks=8)
pa, pb, pab = .40, .35, .12
add("C5", "C", ["4-2"],
    "<p>P(A) = 0.40, P(B) = 0.35 and P(A ∩ B) = 0.12.</p><ol class=\"subs\"><li>Draw a Venn diagram showing the probability of each of the four regions.</li><li>P(A ∪ B)</li><li>P(Aᶜ ∩ Bᶜ)</li><li>P(Aᶜ ∪ B)</li><li>P(exactly one of A, B)</li><li>Could P(A ∩ B) be 0.45 instead? Why not?</li></ol>",
    f"<p><strong>1.</strong> A only {dec(pa - pab)} · both {dec(pab)} · B only {dec(pb - pab)} · outside {dec(1 - pa - pb + pab)} (sum = 1 ✓).</p>"
    f"<p><strong>2.</strong> ⦃{dec(pa + pb - pab)}⦄ <strong>3.</strong> ⦃{dec(1 - pa - pb + pab)}⦄ <strong>4.</strong> everything except A only: 1 − {dec(pa - pab)} = ⦃{dec(1 - pa + pab)}⦄ "
    f"<strong>5.</strong> {dec(pa - pab)} + {dec(pb - pab)} = ⦃{dec(pa + pb - 2 * pab)}⦄</p>"
    "<p><strong>6.</strong> ⦃No⦄: A ∩ B is part of B, so P(A ∩ B) ≤ P(B) = 0.35.</p>", marks=10)

# ------------------------------------------------------------------ Part D · 20-minute quiz
add("D1", "D", ["4-1"], "<p><strong>[2 marks]</strong> Define <em>sample space</em> and <em>compound event</em>, with one example each.</p>",
    "<p>The ⦃set of all possible outcomes⦄ of a probability experiment (one die: {1, …, 6}). An event with ⦃two or more outcomes⦄ (an even number: {2, 4, 6}).</p>")
add("D2", "D", ["4-1"], "<p><strong>[3 marks]</strong> Three coins are tossed. Find P(exactly one tail), P(at most one tail) and P(no tails).</p>",
    "<p>Exactly one: {HHT, HTH, THH}, ⦃3/8⦄. At most one: no tails or one tail, ⦃4/8 = 0.5⦄. No tails: {HHH}, ⦃1/8⦄.</p>")
add("D3", "D", ["4-2"], "<p><strong>[3 marks]</strong> P(A) = 0.25 and P(B) = 0.40. Find P(A ∪ B) if (a) A and B are mutually exclusive (b) P(A ∩ B) = 0.10.</p>",
    "<p>(a) ⦃0.65⦄ (b) 0.25 + 0.40 − 0.10 = ⦃0.55⦄</p>")
add("D4", "D", ["4-1", "4-2"], "<p><strong>[4 marks]</strong> In a class, 18 of 30 students are female; 12 students wear glasses, 7 of them female. One student is chosen at random. Find P(female or wears glasses) and P(male without glasses).</p>",
    "<p>(18 + 12 − 7)/30 = ⦃23/30 ≈ 0.7667⦄. Male without glasses = the complement of (female or glasses) = ⦃7/30 ≈ 0.2333⦄. Check: 12 males, 5 with glasses, so 7 without ✓.</p>")
add("D5", "D", ["4-1"], "<p><strong>[2 marks]</strong> Two dice are rolled. Find P(the sum is at least 10).</p>", f"<p>Sums 10, 11, 12: 3 + 2 + 1 = 6, ⦃{p(6, 36)}⦄.</p>")
add("D6", "D", ["4-2"], "<p><strong>[2 marks]</strong> Explain, with an example, why mutually exclusive events cannot both occur, and write the addition rule they use.</p>",
    "<p>They share ⦃no outcomes⦄ (A ∩ B = ∅), e.g. \"even\" and \"odd\" on one die. Rule: ⦃P(A ∪ B) = P(A) + P(B)⦄.</p>")

# ------------------------------------------------------------------ build
QA_CSS = open("/home/user/STAT2101/Chapter1/html/05-Questions.html", encoding="utf-8").read()
QA_CSS = QA_CSS[QA_CSS.index("<style>\n.q{"):]; QA_CSS = QA_CSS[:QA_CSS.index("</style>") + 8]
PARTS = {"A": ("Part A · Multiple choice (16)", "Give the letter and a one-line reason, as in a written exam.", "1"),
         "B": ("Part B · Short structured questions (14)", "Typical 2–6 mark midterm items. Write S and E in set notation.", "2"),
         "C": ("Part C · Long questions (5)", "Midterm-style, multi-part. Marks in brackets.", "3"),
         "D": ("Part D · 20-minute mini-quiz (16 marks)", "Time yourself, closed book, before opening the answers.", "A")}
OUT = "/home/user/STAT2101/Chapter4/Sections-4-1-4-2"; os.makedirs(OUT + "/html", exist_ok=True)
def page(title, slug, body):
    doc = f"""{head(title)}{QA_CSS}
<div class="wrap"><header class="masthead"><p class="eyebrow">Sultan Qaboos University · STAT 2101 · Chapter 4 · Sections 4-1 and 4-2 only</p>
<div class="meta-strip"><span class="chip"><strong>{len(Q)}</strong> questions</span><span class="chip"><strong>CLO</strong> 4-A</span><span class="chip"><strong>Midterm</strong> 3/11/2026 · 6:15 pm</span></div></header>
{body}
<footer><p>Built to the STAT 2101 Fall 2026 course outline (CLO4-A: calculate probabilities using basic probability principles). Sections 4-1 Sample Spaces and Probability and 4-2 The Addition Rules only. Every numeric answer was computed by code from the question data.</p></footer></div>"""
    path = f"{OUT}/html/{slug}.html"; open(path, "w", encoding="utf-8").write(doc)
    return dict(src=path, out=f"{OUT}/STAT2101-Ch4-4-1-4-2-{slug}.pdf", title=title)
def body(ans):
    tg = lambda q: "".join(f'<span class="tag">{t}</span> ' for t in q["tags"])
    out = [f"""<section style="--sec:var(--accent);--wash:var(--accent-wash)"><div class="sec-head"><span class="sec-num">{'ANS' if ans else 'Q'}</span><h2>{'Full worked answers' if ans else 'Exam-style questions'}: Sections 4-1 and 4-2
<span class="ar">{'الإجابات الكاملة — افتحه بعد حل ملف الأسئلة' if ans else 'أسئلة بمعايير اختبارات جامعة السلطان قابوس — الاحتمالات 4-1 و 4-2 فقط'}</span></h2></div>
{'<p>Each answer shows the set or the rule, the substitution and the value. The <span class="v">why</span> lines name the trap the question was built on.</p>' if ans else
 '<p>Covers only what sections 4-1 and 4-2 teach: sample spaces (lists, trees, dice tables), classical, empirical and subjective probability, the probability rules, complements, the phrases at least / at most / fewer than, mutually exclusive events, and addition rules 1, 2 and the three-event version. No conditional probability, multiplication rule or counting rules. Every question is tagged with its section.</p>'
 '<ar t="طريقة الاستخدام">حل الجزء D أولًا (20 دقيقة) لتعرف مستواك، ثم الأجزاء A و B و C، ثم صحّح من ملف الإجابات. اكتب فضاء العينة والحدث <b>بصيغة المجموعات</b> دائمًا، وسمِّ القاعدة التي تستخدمها، فعليها درجات.</ar>'}
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
man = [page("Probability 4-1 and 4-2 Questions", "Questions", body(False)), page("Probability 4-1 and 4-2 Answers", "Answers", body(True))]
json.dump(man, open(os.path.join(os.path.dirname(__file__), "manifest.json"), "w"))
print(len(Q), "questions", {k: sum(q["part"] == k for q in Q) for k in "ABCD"})
