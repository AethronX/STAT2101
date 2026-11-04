"""Exam-style questions for STAT 2101 sections 4-3, 4-4 and 4-5. Every numeric answer is computed here."""
from math import comb as C, perm as P, factorial as F
from fractions import Fraction as Fr

def p(n, d=None, dp=4):
    f = Fr(n, d) if d is not None else Fr(n)
    dv = f"{float(f):.{dp}f}".rstrip("0").rstrip(".")
    if f.denominator == 1: return dv
    raw = f"{n}/{d}" if d is not None else ""
    pre = f"{raw} = " if raw and raw != f"{f.numerator}/{f.denominator}" else ""
    return f"{pre}{f.numerator}/{f.denominator} ≈ {dv}"
def dec(x, dp=4): return f"{x:.{dp}f}".rstrip("0").rstrip(".")
def n_(x): return f"{x:,}"
def tbl(h, rows):
    hh = "".join(f"<th>{c}</th>" for c in h)
    b = "".join("<tr>" + "".join(f'<td class="num">{c}</td>' for c in r) + "</tr>" for r in rows)
    return f'<div class="tbl-wrap"><table><thead><tr>{hh}</tr></thead><tbody>{b}</tbody></table></div>'
def mcq(o): return '<ul class="opts">' + "".join(f"<li>({k}) {v}</li>" for k, v in zip("abcd", o)) + "</ul>"

dice = [(a, b) for a in range(1, 7) for b in range(1, 7)]
Q = []
def add(id, part, tags, q, a, marks=None): Q.append(dict(id=id, part=part, tags=tags, q=q, a=a, marks=marks))

# ================================================================== Part A
A = [
 ("4-3", "Two cards are drawn from a standard deck <strong>without replacement</strong>. P(both are aces) =",
  ["1/169", "1/221", "1/26", "2/13"], "b", f"(4/52)(3/51) = 12/2652 = 1/221. Option (a) is the <em>with</em> replacement answer (4/52)²."),
 ("4-3", "P(A) = 0.4, P(B) = 0.5 and P(A ∩ B) = 0.2. Which statement is true?",
  ["A and B are mutually exclusive", "A and B are independent", "P(A | B) = 0.5", "P(A ∪ B) = 0.9"], "b",
  "P(A)·P(B) = 0.2 = P(A ∩ B), so they are independent. They are not mutually exclusive (the intersection is not 0); P(A | B) = 0.2/0.5 = 0.4; P(A ∪ B) = 0.7."),
 ("4-3", "P(A ∩ B) = 0.12 and P(A) = 0.30. Then P(B | A) =", ["0.036", "0.40", "0.25", "0.18"], "b", "P(B | A) = P(A ∩ B)/P(A) = 0.12/0.30 = 0.40. The condition goes in the denominator."),
 ("4-3", "Two events with non-zero probabilities are mutually exclusive. They must be:", ["independent", "dependent", "complementary", "equally likely"], "b",
  "If A happens, B certainly does not: P(B | A) = 0 ≠ P(B). Knowing A changes B, so they are dependent."),
 ("4-3", "A fair coin is tossed 5 times. P(at least one head) =", ["5/32", "1/2", "31/32", "1/32"], "c", "1 − P(no heads) = 1 − (1/2)⁵ = 31/32."),
 ("4-3", "A bag has 4 red and 6 blue balls. Two are drawn <strong>with replacement</strong>. P(red first, then blue) =", ["0.24", "0.2667", "0.48", "0.10"], "a",
  "Independent draws: (4/10)(6/10) = 0.24. Option (b), (4/10)(6/9), is the without-replacement value."),
 ("4-3", "A and B are independent with P(A) = 0.3 and P(B) = 0.6. P(A ∪ B) =", ["0.90", "0.18", "0.72", "0.82"], "c",
  "P(A ∩ B) = 0.3 × 0.6 = 0.18, so P(A ∪ B) = 0.3 + 0.6 − 0.18 = 0.72. Addition rule 2 still applies; independence only gives the intersection."),
 ("4-4", "The value of 6!/4! is:", ["1.5", "2", "30", "720"], "c", "6!/4! = 6 × 5 = 30. Cancel the common 4! instead of expanding both."),
 ("4-4", "How many 4-letter codes can be made from the 26 English letters if letters may repeat?",
  ["26 × 25 × 24 × 23", f"{n_(26 ** 4)}", f"{n_(C(26, 4))}", "104"], "b", f"Repetition allowed: 26 × 26 × 26 × 26 = 26⁴ = {n_(26 ** 4)}."),
 ("4-4", "From 10 club members, a president, a vice-president and a secretary are chosen. The number of ways is:",
  [f"{C(10, 3)}", f"{P(10, 3)}", "30", f"{10 ** 3}"], "b", f"Distinct offices, so order matters: ₁₀P₃ = 10 × 9 × 8 = {P(10, 3)}. ₁₀C₃ = {C(10, 3)} would be a committee without titles."),
 ("4-4", "₁₀C₇ equals:", [f"₁₀C₃ = {C(10, 3)}", f"₁₀P₇ = {n_(P(10, 7))}", "70", "7!"], "a",
  f"Choosing 7 to take is the same as choosing 3 to leave: ₙCᵣ = ₙCₙ₋ᵣ = {C(10, 7)}."),
 ("4-4", "The number of distinct arrangements of the letters of LEVEL is:", ["120", "60", "30", "20"], "c", "5 letters with L ×2 and E ×2: 5!/(2! 2!) = 120/4 = 30."),
 ("4-4", "A student has 3 shirts, 4 trousers and 2 pairs of shoes. How many different outfits are possible?", ["9", "24", "12", "6"], "b",
  "Fundamental counting rule: 3 × 4 × 2 = 24. \"And\" across categories means multiply."),
 ("4-5", "A committee of 3 is chosen at random from 5 men and 4 women. P(all three are women) =",
  [p(C(4, 3), C(9, 3)), "4/9", "1/3", "1/126"], "a", f"₄C₃/₉C₃ = 4/84 = 1/21. Count both the event and the sample space with combinations."),
 ("4-5", "A lottery draws 3 different numbers from 1 to 10; order does not matter. The probability that one ticket wins is:",
  [f"1/{P(10, 3)}", f"1/{C(10, 3)}", "3/10", "1/1000"], "b", f"Order doesn't matter, so n(S) = ₁₀C₃ = {C(10, 3)}."),
 ("4-5", "The letters of MATH are arranged at random. P(the arrangement starts with M) =", ["1/24", "1/4", "1/6", "4/24"], "b",
  "With M fixed first, the other 3 letters arrange in 3! = 6 ways, so 6/4! = 6/24 = 1/4. Or directly: each letter is equally likely to be first."),
]
for i, (t, q, o, ans, why) in enumerate(A, 1):
    add(f"A{i}", "A", [t], f"<p>{q}</p>{mcq(o)}", f"<p>⦃({ans})⦄</p><p class=\"why\">{why}</p>")

# ================================================================== Part B
add("B1", "B", ["4-3"],
    "<p><strong>[5 marks]</strong> 200 SQU students were asked whether they use the university gym:</p>" +
    tbl(["", "Uses gym", "Does not", "Total"], [["Male", 48, 52, 100], ["Female", 32, 68, 100], ["<strong>Total</strong>", 80, 120, 200]]) +
    "<p>Find: (a) P(uses gym | male) (b) P(male | uses gym) (c) P(male and uses gym) (d) Are \"male\" and \"uses gym\" independent? Justify with numbers.</p>",
    "<p>(a) Male row: 48/100 = ⦃0.48⦄ (b) Gym column: 48/80 = ⦃0.60⦄ (c) one cell: 48/200 = ⦃0.24⦄</p>"
    "<p>(d) P(gym) = 80/200 = 0.40, but P(gym | male) = 0.48 ≠ 0.40. Equivalently P(M)·P(G) = 0.5 × 0.4 = 0.20 ≠ 0.24. ⦃Dependent⦄.</p>"
    "<p class=\"why\">(a) and (b) look alike but have different denominators. The condition chooses the row or column total.</p>")
d, g, N = 5, 15, 20
both_d = Fr(d, N) * Fr(d - 1, N - 1); one_each = 2 * Fr(d, N) * Fr(g, N - 1); none_d = Fr(g, N) * Fr(g - 1, N - 1)
add("B2", "B", ["4-3"],
    "<p><strong>[5 marks]</strong> A box holds 20 phone chargers, 5 of them defective. Two are taken <strong>without replacement</strong>. Find: (a) P(both defective) (b) P(exactly one defective) (c) P(at least one defective). (d) Check that (a), (b) and P(none defective) add to 1.</p>",
    f"<p>(a) (5/20)(4/19) = ⦃{p(both_d.numerator, both_d.denominator)}⦄</p>"
    f"<p>(b) defective-good <em>or</em> good-defective: (5/20)(15/19) + (15/20)(5/19) = ⦃{p(one_each.numerator, one_each.denominator)}⦄</p>"
    f"<p>(c) 1 − P(none) = 1 − (15/20)(14/19) = 1 − {none_d} = ⦃{p((1 - none_d).numerator, (1 - none_d).denominator)}⦄</p>"
    f"<p>(d) {both_d} + {one_each} + {none_d} = {both_d + one_each + none_d} ✓</p>"
    "<p class=\"why\">The usual mistake in (b) is to count only one of the two orders.</p>")
pb, lb, lo = Fr(60, 100), Fr(10, 100), Fr(4, 100)
late = pb * lb + (1 - pb) * lo
add("B3", "B", ["4-3"],
    "<p><strong>[4 marks]</strong> 60% of students come to SQU by bus. <strong>Of the bus users</strong>, 10% arrive late; of the others, 4% arrive late. Draw a tree diagram, then find: (a) P(bus and late) (b) P(late) (c) P(not bus and on time).</p>",
    f"<p>Branches: bus 0.6 → late 0.10 / on time 0.90; not bus 0.4 → late 0.04 / on time 0.96.</p>"
    f"<p>(a) Multiplication rule 2: 0.6 × 0.10 = ⦃0.06⦄ (b) add both late paths: 0.06 + 0.4 × 0.04 = 0.06 + 0.016 = ⦃{dec(float(late))}⦄ (c) 0.4 × 0.96 = ⦃0.384⦄</p>"
    "<p class=\"why\">\"Of the bus users\" makes the 10% a conditional probability, P(late | bus).</p>")
add("B4", "B", ["4-3"],
    "<p><strong>[4 marks]</strong> P(A) = 0.5, P(B) = 0.4 and P(A ∪ B) = 0.7. Find P(A ∩ B), P(A | B) and P(B | A). Are A and B independent? Are they mutually exclusive?</p>",
    "<p>P(A ∩ B) = 0.5 + 0.4 − 0.7 = ⦃0.2⦄; P(A | B) = 0.2/0.4 = ⦃0.5⦄; P(B | A) = 0.2/0.5 = ⦃0.4⦄.</p>"
    "<p>P(A | B) = 0.5 = P(A), so ⦃independent⦄. Not mutually exclusive, since P(A ∩ B) = 0.2 ≠ 0.</p>")
add("B5", "B", ["4-3"],
    "<p><strong>[3 marks]</strong> A device has 3 components that work independently; each fails with probability 0.05. Find P(all three work) and P(at least one fails).</p>",
    f"<p>P(all work) = 0.95³ = ⦃{dec(0.95 ** 3, 6)}⦄; P(at least one fails) = 1 − 0.95³ = ⦃{dec(1 - 0.95 ** 3, 6)}⦄.</p>")
add("B6", "B", ["4-3"],
    "<p><strong>[2 marks] Find the mistake.</strong> Given P(A ∩ B) = 0.15 and P(B) = 0.5, a student writes \"P(A | B) = 0.15/P(A)\".</p>",
    "<p>The condition B goes in the denominator: P(A | B) = P(A ∩ B)/P(B) = 0.15/0.5 = ⦃0.30⦄. P(A) is not even given.</p>")
A_ = {(a, b) for a, b in dice if a % 2 == 0}; B_ = {(a, b) for a, b in dice if a + b == 7}
add("B7", "B", ["4-3"],
    "<p><strong>[3 marks]</strong> Two dice are rolled. A = \"the first die is even\" and B = \"the sum is 7\". Show whether A and B are independent.</p>",
    f"<p>P(A) = 18/36 = 1/2; P(B) = 6/36 = 1/6; A ∩ B = {{(2,5), (4,3), (6,1)}}, so P(A ∩ B) = 3/36 = 1/12.</p>"
    f"<p>P(A)·P(B) = 1/2 × 1/6 = 1/12 = P(A ∩ B): ⦃independent⦄.</p>")
add("B8", "B", ["4-4"],
    "<p><strong>[3 marks]</strong> How many 4-digit PINs (digits 0–9) are possible if (a) repetition is allowed (b) repetition is not allowed (c) no repetition and the first digit cannot be 0?</p>",
    f"<p>(a) 10⁴ = ⦃{n_(10 ** 4)}⦄ (b) 10 × 9 × 8 × 7 = ⦃{n_(P(10, 4))}⦄ (c) 9 × 9 × 8 × 7 = ⦃{n_(9 * 9 * 8 * 7)}⦄. The first slot has 9 choices (no 0), and the second has 9 because 0 is now allowed but one digit is used.</p>")
add("B9", "B", ["4-4"],
    "<p><strong>[4 marks]</strong> A club has 12 members, including Ahmed. In how many ways can (a) a president, vice-president and secretary be chosen (b) a committee of 3 be chosen (c) a committee of 3 that includes Ahmed be chosen (d) a committee of 3 that excludes Ahmed be chosen?</p>",
    f"<p>(a) ₁₂P₃ = ⦃{n_(P(12, 3))}⦄ (b) ₁₂C₃ = ⦃{C(12, 3)}⦄ (c) Ahmed is in, choose 2 of the other 11: ₁₁C₂ = ⦃{C(11, 2)}⦄ (d) ₁₁C₃ = ⦃{C(11, 3)}⦄</p>"
    f"<p class=\"why\">Check: (c) + (d) = {C(11, 2)} + {C(11, 3)} = {C(12, 3)} = (b) ✓. Every committee either includes Ahmed or doesn't.</p>")
add("B10", "B", ["4-4"],
    "<p><strong>[3 marks]</strong> How many distinct arrangements can be made from the letters of SULTANATE? How many of them begin with S?</p>",
    f"<p>9 letters with A ×2 and T ×2: 9!/(2! 2!) = {n_(F(9))}/4 = ⦃{n_(F(9) // 4)}⦄.</p>"
    f"<p>With S fixed first, arrange the other 8 (A ×2, T ×2): 8!/(2! 2!) = ⦃{n_(F(8) // 4)}⦄.</p>")
add("B11", "B", ["4-4"],
    "<p><strong>[3 marks]</strong> A committee of 5 is formed from 6 men and 5 women. In how many ways can it have (a) exactly 2 men (b) at least 4 women?</p>",
    f"<p>(a) 2 men <em>and</em> 3 women: ₆C₂ × ₅C₃ = {C(6, 2)} × {C(5, 3)} = ⦃{C(6, 2) * C(5, 3)}⦄</p>"
    f"<p>(b) 4 women + 1 man, or 5 women: ₅C₄·₆C₁ + ₅C₅ = {C(5, 4) * 6} + 1 = ⦃{C(5, 4) * 6 + 1}⦄. \"And\" multiplies within a case; \"or\" adds the cases.</p>")
add("B12", "B", ["4-4"],
    "<p><strong>[2 marks]</strong> Find n if ₙC₂ = 45.</p>",
    "<p>n(n − 1)/2 = 45, so n(n − 1) = 90 = 10 × 9, giving ⦃n = 10⦄.</p>")
r, w, k = 6, 4, 4
add("B13", "B", ["4-5"],
    "<p><strong>[3 marks]</strong> A bag holds 6 red and 4 white balls. Four are drawn at random. Find P(exactly 2 red) and P(at least 1 white).</p>",
    f"<p>n(S) = ₁₀C₄ = {C(10, 4)}. Exactly 2 red: ₆C₂ × ₄C₂ = {C(6, 2)} × {C(4, 2)} = {C(6, 2) * C(4, 2)}, so P = ⦃{p(C(6, 2) * C(4, 2), C(10, 4))}⦄.</p>"
    f"<p>At least 1 white = 1 − P(all red) = 1 − ₆C₄/₁₀C₄ = 1 − {C(6, 4)}/{C(10, 4)} = ⦃{p(C(10, 4) - C(6, 4), C(10, 4))}⦄.</p>")
tot = F(6) // (F(3) * F(2)); ends = F(4) // F(2)
add("B14", "B", ["4-5"],
    "<p><strong>[3 marks]</strong> The letters of BANANA are arranged at random. Find P(the arrangement begins and ends with A).</p>",
    f"<p>n(S) = 6!/(3! 2!) = {tot}. Fix A at both ends; arrange B, N, A, N: 4!/2! = {ends}.</p><p>P = ⦃{p(ends, tot)}⦄</p>")
add("B15", "B", ["4-5"],
    "<p><strong>[2 marks]</strong> A 3-digit code is formed with no repeated digits (0–9). Find P(all three digits are odd).</p>",
    f"<p>n(S) = ₁₀P₃ = {P(10, 3)}; n(E) = ₅P₃ = {P(5, 3)} (odd digits 1, 3, 5, 7, 9). P = ⦃{p(P(5, 3), P(10, 3))}⦄.</p>")
add("B16", "B", ["4-3", "4-5"],
    "<p><strong>[3 marks]</strong> 12 bulbs include 3 that are defective. Three are chosen at random. Find P(none defective) in two ways: with combinations, and with the multiplication rule. Then find P(at least one defective).</p>",
    f"<p>Combinations: ₉C₃/₁₂C₃ = {C(9, 3)}/{C(12, 3)} = {Fr(C(9, 3), C(12, 3))}.</p>"
    f"<p>Multiplication rule (without replacement): (9/12)(8/11)(7/10) = {Fr(9 * 8 * 7, 12 * 11 * 10)}. Same answer ✓.</p>"
    f"<p>P(none) = ⦃{p(C(9, 3), C(12, 3))}⦄; P(at least one) = ⦃{p(C(12, 3) - C(9, 3), C(12, 3))}⦄</p>")

# ================================================================== Part C
yy, yn, my, mn, oy, on = 90, 60, 70, 80, 40, 60; T = 400
both_old = Fr(100, 400) * Fr(99, 399)
add("C1", "C", ["4-3"],
    "<p>400 adults in Muscat were asked whether they exercise regularly:</p>" +
    tbl(["Age group", "Yes", "No", "Total"], [["18–30", yy, yn, yy + yn], ["31–50", my, mn, my + mn], ["over 50", oy, on, oy + on], ["<strong>Total</strong>", 200, 200, 400]]) +
    "<ol class=\"subs\"><li>P(exercises)</li><li>P(exercises | 18–30)</li><li>P(over 50 | does not exercise)</li><li>P(18–30 and exercises)</li><li>Are \"18–30\" and \"exercises\" independent? Justify.</li><li>Two adults are chosen without replacement. Find P(both are over 50).</li></ol>",
    "<p><strong>1.</strong> 200/400 = ⦃0.5⦄ <strong>2.</strong> 90/150 = ⦃0.6⦄ <strong>3.</strong> 60/200 = ⦃0.3⦄ <strong>4.</strong> 90/400 = ⦃0.225⦄</p>"
    "<p><strong>5.</strong> P(yes | 18–30) = 0.6 ≠ P(yes) = 0.5 (or 0.225 ≠ 0.375 × 0.5 = 0.1875): ⦃dependent⦄. Young adults are more likely to exercise.</p>"
    f"<p><strong>6.</strong> (100/400)(99/399) = ⦃{p(both_old.numerator, both_old.denominator)}⦄</p>", marks=12)
pr = Fr(1, 3) * Fr(3, 5) + Fr(2, 3) * Fr(1, 5)
add("C2", "C", ["4-3"],
    "<p>Box A has 3 red and 2 blue balls; box B has 1 red and 4 blue. A die is rolled: 1 or 2 → a ball is drawn from box A; otherwise from box B.</p><ol class=\"subs\"><li>Draw the tree diagram with all branch probabilities.</li><li>P(box A and red)</li><li>P(red)</li><li>Given that the ball is red, find the probability it came from box A.</li><li>Are \"box A\" and \"red\" independent?</li></ol>",
    f"<p><strong>1.</strong> A 1/3 → red 3/5, blue 2/5; B 2/3 → red 1/5, blue 4/5.</p><p><strong>2.</strong> (1/3)(3/5) = ⦃1/5⦄</p>"
    f"<p><strong>3.</strong> 1/5 + (2/3)(1/5) = 1/5 + 2/15 = ⦃{p(pr.numerator, pr.denominator)}⦄</p>"
    f"<p><strong>4.</strong> P(A | red) = P(A ∩ red)/P(red) = (1/5)/(1/3) = ⦃3/5 = 0.6⦄</p>"
    "<p><strong>5.</strong> P(A | red) = 0.6 ≠ P(A) = 1/3: ⦃dependent⦄.</p>", marks=10)
nS = C(12, 5)
add("C3", "C", ["4-4", "4-5"],
    "<p>A committee of 5 is chosen at random from 7 engineers and 5 doctors.</p><ol class=\"subs\"><li>Find n(S).</li><li>P(exactly 3 engineers)</li><li>P(all members have the same profession)</li><li>P(at least one doctor)</li><li>P(a particular engineer, Salim, is on the committee)</li></ol>",
    f"<p><strong>1.</strong> ₁₂C₅ = ⦃{nS}⦄</p><p><strong>2.</strong> ₇C₃ × ₅C₂ = {C(7, 3)} × {C(5, 2)} = {C(7, 3) * C(5, 2)}, so P = ⦃{p(C(7, 3) * C(5, 2), nS)}⦄</p>"
    f"<p><strong>3.</strong> all engineers ₇C₅ = {C(7, 5)} or all doctors ₅C₅ = 1: ({C(7, 5)} + 1)/{nS} = ⦃{p(C(7, 5) + 1, nS)}⦄</p>"
    f"<p><strong>4.</strong> 1 − ₇C₅/{nS} = ⦃{p(nS - C(7, 5), nS)}⦄</p><p><strong>5.</strong> Salim in, choose 4 of the other 11: ₁₁C₄ = {C(11, 4)}, so P = ⦃{p(C(11, 4), nS)}⦄. Check: 5 of 12 seats, 5/12 ✓.</p>", marks=12)
add("C4", "C", ["4-4", "4-5"],
    "<p>SQU student IDs have 6 digits, and the first digit must be 1 or 2.</p><ol class=\"subs\"><li>How many IDs are possible if repetition is allowed?</li><li>How many if no digit may repeat?</li><li>With repetition allowed, find P(a randomly issued ID ends in 0).</li><li>With repetition allowed, find P(all six digits are the same).</li></ol>",
    f"<p><strong>1.</strong> 2 × 10⁵ = ⦃{n_(2 * 10 ** 5)}⦄ <strong>2.</strong> 2 × 9 × 8 × 7 × 6 × 5 = ⦃{n_(2 * 9 * 8 * 7 * 6 * 5)}⦄</p>"
    f"<p><strong>3.</strong> 2 × 10⁴ × 1 / (2 × 10⁵) = ⦃0.1⦄ <strong>4.</strong> only 111111 and 222222: 2/{n_(2 * 10 ** 5)} = ⦃0.00001⦄</p>", marks=8)
add("C5", "C", ["4-3", "4-4"],
    "<p>A multiple-choice quiz has 5 questions, each with 4 options. A student guesses every answer independently.</p><ol class=\"subs\"><li>How many different answer sheets are possible?</li><li>P(all five correct)</li><li>P(none correct)</li><li>P(at least one correct)</li></ol>",
    f"<p><strong>1.</strong> 4⁵ = ⦃{4 ** 5}⦄ <strong>2.</strong> (1/4)⁵ = ⦃1/1024 ≈ 0.000977⦄ <strong>3.</strong> (3/4)⁵ = ⦃{p(3 ** 5, 4 ** 5)}⦄ <strong>4.</strong> 1 − 243/1024 = ⦃{p(4 ** 5 - 3 ** 5, 4 ** 5)}⦄</p>", marks=8)

# ================================================================== Part D
add("D1", "D", ["4-3"], "<p><strong>[2 marks]</strong> Define independent and dependent events, with one example each.</p>",
    "<p>Independent: the occurrence of one ⦃does not change⦄ the probability of the other (two coin tosses). Dependent: it ⦃does change⦄ it (two cards drawn without replacement).</p>")
add("D2", "D", ["4-3"], "<p><strong>[3 marks]</strong> 30% of a city's residents own a car; of the car owners, 45% also own a motorbike. Find P(car and motorbike). Is 0.45 a conditional probability?</p>",
    "<p>⦃Yes⦄: 0.45 = P(motorbike | car). P(car ∩ motorbike) = 0.30 × 0.45 = ⦃0.135⦄.</p>")
add("D3", "D", ["4-4"], "<p><strong>[3 marks]</strong> Evaluate ₈P₃, ₈C₃ and 7!/(5! 2!).</p>",
    f"<p>₈P₃ = ⦃{P(8, 3)}⦄; ₈C₃ = ⦃{C(8, 3)}⦄; 7!/(5! 2!) = ⦃{F(7) // (F(5) * 2)}⦄</p>")
add("D4", "D", ["4-4"], "<p><strong>[2 marks]</strong> In how many ways can 7 different books be arranged on a shelf if a particular book must be in the middle?</p>",
    f"<p>The middle place is fixed; arrange the other 6: 6! = ⦃{F(6)}⦄.</p>")
add("D5", "D", ["4-5"], "<p><strong>[3 marks]</strong> 4 students are chosen at random from 8 males and 6 females. Find P(2 males and 2 females).</p>",
    f"<p>₈C₂ × ₆C₂ / ₁₄C₄ = {C(8, 2)} × {C(6, 2)} / {C(14, 4)} = ⦃{p(C(8, 2) * C(6, 2), C(14, 4))}⦄</p>")
add("D6", "D", ["4-3"], "<p><strong>[3 marks]</strong> P(A) = 0.6, P(B | A) = 0.5 and P(B | Aᶜ) = 0.2. Find P(A ∩ B) and P(B).</p>",
    "<p>P(A ∩ B) = 0.6 × 0.5 = ⦃0.30⦄; P(B) = 0.30 + 0.4 × 0.2 = ⦃0.38⦄ (add the two tree paths that end in B).</p>")
