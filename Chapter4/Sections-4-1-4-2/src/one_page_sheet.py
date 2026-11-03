import sys, json
sys.path.insert(0, "/tmp/claude-0/-home-user-STAT2101/521e5d47-fbd3-5206-8b60-93d1c3cc1629/scratchpad/ch3")
from ch3lib import head, markup

CSS = """<style>
body{font-size:10.2px !important;line-height:1.4 !important}
.wrap{max-width:none;zoom:1.13}
.top{display:flex;justify-content:space-between;align-items:baseline;border-bottom:2px solid var(--fg);padding-bottom:3px;margin-bottom:5px}
.top h1{font-size:15px;margin:0;line-height:1.1}
.top .sub{font-family:var(--mono);font-size:7.5px;color:var(--fg-soft);text-align:right}
.cols{column-count:3;column-gap:9px}
.box{break-inside:avoid;border:1px solid var(--rule);border-left:3px solid var(--sec);border-radius:3px;padding:4px 6px;margin:0 0 5px;background:var(--surface)}
.box h2{font-family:var(--mono);font-size:8.8px;letter-spacing:.06em;text-transform:uppercase;color:var(--sec);margin:0 0 3px;font-weight:700}
.box p,.box li{margin:0 0 2px;max-width:none}
.box ul,.box ol{margin:0;padding-left:1.1em}
.f{font-family:var(--mono);font-size:9.6px;background:var(--wash);padding:1px 4px;border-radius:2px;white-space:nowrap}
.fb{display:block;font-family:var(--mono);font-size:9.8px;background:var(--wash);padding:2px 5px;border-radius:2px;margin:2px 0;font-weight:600}
table{font-size:9.2px !important;min-width:0 !important;width:100%;margin:2px 0}
th,td{padding:1px 4px !important}
thead th{font-size:7px !important;letter-spacing:.03em}
.ar{font-family:var(--arabic);direction:rtl;text-align:right;font-size:9.6px;color:var(--fg-soft);line-height:1.5;display:block;margin-top:2px}
.s41{--sec:var(--ink-1);--wash:var(--ink-1-wash)} .s42{--sec:var(--ink-2);--wash:var(--ink-2-wash)} .tr{--sec:var(--accent);--wash:var(--accent-wash)} .ex{--sec:var(--ink-4);--wash:var(--ink-4-wash)}
svg text{font-family:var(--mono);font-size:9px;fill:currentColor}
@page{size:A4;margin:0}
</style>"""

BODY = """<div class="wrap">
<div class="top"><h1>Probability · 4-1 &amp; 4-2 · One-Page Sheet</h1>
<div class="sub">STAT 2101 · SQU · CLO4-A<br>ورقة القوانين — الدرسان 4-1 و 4-2</div></div>
<div class="cols">

<div class="box s41"><h2>4-1 · Key terms (define as sentences)</h2>
<ul><li><b>Probability experiment</b>: a chance process with well-defined results (outcomes).</li>
<li><b>Outcome</b>: the result of a <u>single</u> trial.</li>
<li><b>Sample space S</b>: the set of <u>all</u> possible outcomes; size n(S).</li>
<li><b>Event</b>: a set of outcomes (a subset of S).</li>
<li><b>Simple</b> event = 1 outcome · <b>compound</b> = 2 or more.</li></ul>
<span class="ar">النتيجة لمحاولة واحدة، وفضاء العينة كل النتائج، والحدث مجموعة جزئية منه.</span></div>

<div class="box s41"><h2>4-1 · Sample spaces to know</h2>
<ul><li>1 die: n = 6 · 2 dice: n = <b>36</b> (ordered pairs)</li>
<li>n coins / n children: n(S) = <b>2ⁿ</b> (2 → 4, 3 → 8, 4 → 16)</li>
<li>3 children: {BBB, BBG, BGB, GBB, BGG, GBG, GGB, GGG}</li>
<li>Coin + die: 2 × 6 = 12 (H1…H6, T1…T6)</li>
<li>Tools: <b>list</b> in a fixed order · <b>tree diagram</b> · <b>grid</b> (dice)</li></ul>
<table><thead><tr><th>Sum of 2 dice</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th><th>8</th><th>9</th><th>10</th><th>11</th><th>12</th></tr></thead>
<tbody><tr><td><b>ways /36</b></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td><b>6</b></td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td></tr></tbody></table>
<p>Doubles: 6 · sum odd: 18 · sum even: 18 · product odd: 9 (both odd)</p></div>

<div class="box s41"><h2>4-1 · Deck of 52 cards</h2>
<p>4 suits × 13: ♥ ♦ red (26), ♣ ♠ black (26). Each rank (A, 2…10, J, Q, K) appears 4 times. <b>Face cards</b> J, Q, K = 12 (6 red). Ace is not a face card.</p></div>

<div class="box s41"><h2>4-1 · Three types of probability</h2>
<table><tbody>
<tr><td><b>Classical</b></td><td>equally likely outcomes; count S</td><td><span class="f">P(E) = n(E)/n(S)</span></td></tr>
<tr><td><b>Empirical</b></td><td>observed data / frequency table</td><td><span class="f">P(E) = f/n</span></td></tr>
<tr><td><b>Subjective</b></td><td>expert's educated guess or opinion</td><td>no formula</td></tr></tbody></table>
<p>Tell: count S → classical · "of 500 surveyed…" → empirical · "a doctor estimates…" → subjective.</p>
<span class="ar">كلاسيكي = عدّ نتائج متساوية الفرص. تجريبي = من بيانات مجموعة f/n. شخصي = تقدير خبير.</span></div>

<div class="box s41"><h2>4-1 · Probability rules</h2>
<ol><li><span class="f">0 ≤ P(E) ≤ 1</span> (negative or &gt; 1 means an error)</li>
<li>P(E) = 0 → E is <b>impossible</b> (a 9 on one die)</li>
<li>P(E) = 1 → E is <b>certain</b> (a number &lt; 7 on one die)</li>
<li>The probabilities of all outcomes in S add to <b>1</b></li></ol>
<p>Scale: 0 impossible · 0.25 unlikely · 0.5 50–50 · 0.75 likely · 1 certain</p></div>

<div class="box s41"><h2>4-1 · Complement</h2>
<span class="fb">P(Ē) = 1 − P(E)   ·   P(E) + P(Ē) = 1</span>
<p>Ē = everything in S that is <b>not</b> in E (stay inside S!). Use it for: <b>not · none · neither · at least one</b>.</p>
<p><span class="f">P(at least one) = 1 − P(none)</span></p>
<span class="ar">المتمّمة: كل ما في فضاء العينة وليس في الحدث. استخدمها مع: ليس، ولا واحد، واحد على الأقل.</span></div>

<div class="box s41"><h2>4-1 · The five phrases (values 3, 4, 5, 6, 7)</h2>
<table><thead><tr><th>Phrase</th><th>Values</th><th>Symbol</th><th>Complement</th></tr></thead><tbody>
<tr><td>exactly 5</td><td>5</td><td>X = 5</td><td>X ≠ 5</td></tr>
<tr><td>less / fewer than 5</td><td>3, 4</td><td>X &lt; 5</td><td>at least 5</td></tr>
<tr><td><b>at most</b> 5</td><td>3, 4, 5</td><td>X ≤ 5</td><td>more than 5</td></tr>
<tr><td>more than 5</td><td>6, 7</td><td>X &gt; 5</td><td>at most 5</td></tr>
<tr><td><b>at least</b> 5</td><td>5, 6, 7</td><td>X ≥ 5</td><td>fewer than 5</td></tr></tbody></table>
<span class="ar">كلمة <b dir="ltr">at</b> تعني أن الرقم داخل الحساب، وكلمة <b dir="ltr">than</b> تعني أنه خارجه. ومتمّمة «على الأقل <span dir="ltr">k</span>» هي «أقل من <span dir="ltr">k</span>».</span></div>

<div class="box s41"><h2>4-1 · Set operations (Venn)</h2>
<ul><li><b>A ∪ B</b> "A <u>or</u> B": in A, in B, <u>or both</u> (inclusive)</li>
<li><b>A ∩ B</b> "A <u>and</u> B": in both</li>
<li><b>Ā = Aᶜ</b> "not A": in S but not in A</li>
<li>Check: n(A ∪ B) + n((A ∪ B)ᶜ) = n(S)</li></ul></div>

<div class="box s42"><h2>4-2 · Mutually exclusive (disjoint)</h2>
<p>A and B <b>cannot occur at the same time</b>: no common outcomes.</p>
<span class="fb">A ∩ B = ∅   ⇔   P(A ∩ B) = 0</span>
<p>Write the intersection, then decide. Die: even {2,4,6} &amp; odd {1,3,5} → ME. Even &amp; {1,2,4} share {2,4} → <b>not</b> ME.</p>
<p>If <span class="f">P(A) + P(B) &gt; 1</span>, A and B <b>cannot</b> be ME.</p>
<span class="ar">المتنافيان لا يقعان معًا (لا تقاطع بينهما). اكتب التقاطع أولًا ثم احكم.</span></div>

<div class="box s42"><h2>4-2 · Addition rules ("OR")</h2>
<p><b>Rule 1</b> (ME): <span class="fb">P(A ∪ B) = P(A) + P(B)</span></p>
<p><b>Rule 2</b> (not ME, always safe): <span class="fb">P(A ∪ B) = P(A) + P(B) − P(A ∩ B)</span></p>
<p>Rearranged: <span class="f">P(A ∩ B) = P(A) + P(B) − P(A ∪ B)</span></p>
<p><b>3 ME events</b>: <span class="f">P(A∪B∪C) = P(A)+P(B)+P(C)</span></p>
<p><b>3 events, general</b>:</p>
<span class="fb">P(A∪B∪C) = ΣP(single) − [P(A∩B)+P(A∩C)+P(B∩C)] + P(A∩B∩C)</span>
<span class="ar">«أو» = جمع. إذا كان بينهما تداخل نطرح التقاطع مرة لأنه حُسب مرتين.</span></div>

<div class="box s42"><h2>4-2 · Venn: the four regions</h2>
<svg viewBox="0 0 230 74" style="width:100%;max-width:230px;display:block;margin:0 auto">
<rect x="1" y="1" width="228" height="72" rx="3" fill="none" stroke="currentColor" stroke-width=".8"/>
<circle cx="85" cy="37" r="30" fill="var(--ink-2-wash)" stroke="var(--ink-2)"/><circle cx="130" cy="37" r="30" fill="var(--ink-2-wash)" fill-opacity=".6" stroke="var(--ink-2)"/>
<text x="72" y="40" text-anchor="middle">A only</text><text x="107.5" y="40" text-anchor="middle" style="font-size:8px">A∩B</text><text x="144" y="40" text-anchor="middle">B only</text><text x="200" y="66" text-anchor="middle">neither</text></svg>
<table><tbody>
<tr><td>A only = A ∩ Bᶜ</td><td>P(A) − P(A∩B)</td></tr>
<tr><td>B only = Aᶜ ∩ B</td><td>P(B) − P(A∩B)</td></tr>
<tr><td>neither = (A ∪ B)ᶜ</td><td>1 − P(A ∪ B)</td></tr>
<tr><td>exactly one</td><td>P(A) + P(B) − 2P(A∩B)</td></tr>
<tr><td>Aᶜ ∪ B</td><td>1 − P(A only)</td></tr>
<tr><td>P(A∩B) limit</td><td>≤ smaller of P(A), P(B)</td></tr></tbody></table>
<p>Fill the overlap first, then the "only" parts; the four regions must add to 1.</p></div>

<div class="box s42"><h2>4-2 · Two-way tables</h2>
<table><tbody>
<tr><td>P(A)</td><td>row/col total ÷ grand total</td></tr>
<tr><td>P(A and B)</td><td><b>one cell</b> ÷ grand total</td></tr>
<tr><td>P(A or B)</td><td>(row + col − shared cell) ÷ total</td></tr>
<tr><td>P(neither A nor B)</td><td>1 − P(A or B), or sum the other cells</td></tr>
<tr><td>ME?</td><td>the shared cell = 0?</td></tr></tbody></table>
<p>Two categories of the <u>same</u> variable (two colleges, two blood types) are always ME.</p></div>

<div class="box tr"><h2>Traps that cost marks</h2>
<ol><li>"or" read as exclusive: it means <b>or both</b>.</li>
<li>Rule 1 used when events overlap: double counts (king or heart = 16/52, not 17/52).</li>
<li>Multiplying instead of adding for ME events: P(A∪B) = P(A)+P(B), and P(A∩B) = 0.</li>
<li>Unequal outcomes treated as equally likely ({2 heads, 1 head, 0 heads} is wrong; use HH, HT, TH, TT).</li>
<li>11 dice sums are <b>not</b> equally likely: always divide by 36.</li>
<li>"at least 2" ≠ "exactly 2"; "at most" includes the number.</li>
<li>Ā forgetting elements of S that lie in B.</li>
<li>Empirical: dividing by the wrong total; check Σf = n.</li></ol></div>

<div class="box ex"><h2>Write it like a marker reads</h2>
<ol><li>Define events: "Let A = …".</li>
<li>Write S and E in <b>set notation</b> (the lecturer requires it).</li>
<li>Name the rule: "not ME, so Rule 2".</li>
<li>Substitute, simplify the fraction, give a decimal.</li>
<li>Check 0 ≤ P ≤ 1 and that complements add to 1.</li></ol>
<span class="ar">عرّف الأحداث، اكتب فضاء العينة بصيغة المجموعات، سمِّ القاعدة، ثم عوّض، وتأكد أن الناتج بين 0 و 1.</span></div>

</div></div>"""

doc = head("Probability 4-1 and 4-2 Sheet") + CSS + markup(BODY, {})
src = "/home/user/STAT2101/Chapter4/Sections-4-1-4-2/html/One-Page-Sheet.html"
open(src, "w", encoding="utf-8").write(doc)
json.dump([dict(src=src, out="/home/user/STAT2101/Chapter4/Sections-4-1-4-2/STAT2101-Ch4-4-1-4-2-One-Page-Sheet.pdf", title="4-1 and 4-2 sheet")],
          open("/tmp/claude-0/-home-user-STAT2101/521e5d47-fbd3-5206-8b60-93d1c3cc1629/scratchpad/p41/sheet.json", "w"))
print("ok")
