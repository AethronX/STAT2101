BODY = """<div class="wrap">
<div class="top"><h1>Probability · 4-3, 4-4 &amp; 4-5 · One-Page Sheet</h1>
<div class="sub">STAT 2101 · SQU · CLO4-A<br>ورقة القوانين — الدروس 4-3 و 4-4 و 4-5</div></div>
<div class="cols">

<div class="box s41"><h2>4-3 · Independent vs dependent</h2>
<ul><li><b>Independent</b>: A occurring does <u>not</u> change P(B). <b>Dependent</b>: it does.</li>
<li><b>With replacement</b>, separate devices (coin + die), people from a large population → independent.</li>
<li><b>Without replacement</b>, "of those who…", "of these…" → dependent / conditional.</li>
<li>Independent ≠ mutually exclusive. ME events with P &gt; 0 are always <b>dependent</b>.</li></ul>
<span class="ar">المستقلان: وقوع أحدهما لا يغيّر احتمال الآخر. السحب مع الإرجاع يعطي أحداثًا مستقلة، والسحب بدون إرجاع يعطي أحداثًا تابعة.</span></div>

<div class="box s41"><h2>4-3 · Multiplication rules ("AND")</h2>
<p><b>Rule 1</b> (independent): <span class="fb">P(A ∩ B) = P(A) · P(B)</span></p>
<p><b>Rule 2</b> (dependent): <span class="fb">P(A ∩ B) = P(A) · P(B | A) = P(B) · P(A | B)</span></p>
<p>n independent trials: <span class="f">P(all) = p · p ⋯ p = pⁿ</span></p>
<p>Without replacement, chain it: 2 aces = (4/52)(3/51) = 1/221; each next fraction drops by 1 on top (same kind) and bottom.</p></div>

<div class="box s41"><h2>4-3 · Conditional probability</h2>
<span class="fb">P(B | A) = P(A ∩ B) / P(A)     P(A) ≠ 0</span>
<p><b>The condition goes in the denominator.</b> "Given that", "if", "of those who", or a fact stated as already true ("he has to park in a no-parking zone").</p>
<p><b>Independence tests</b> (any one): <span class="f">P(B | A) = P(B)</span> · <span class="f">P(A | B) = P(A)</span> · <span class="f">P(A ∩ B) = P(A)P(B)</span></p>
<span class="ar">الشرط دائمًا في المقام. والاستقلال يعني أن الاحتمال الشرطي يساوي الاحتمال العادي.</span></div>

<div class="box s41"><h2>4-3 · Two-way tables</h2>
<table><tbody>
<tr><td>P(A and B)</td><td>cell ÷ <b>grand total</b></td></tr>
<tr><td>P(A | B)</td><td>cell ÷ <b>total of B's row or column</b></td></tr>
<tr><td>independent?</td><td>compare P(A | B) with P(A)</td></tr>
<tr><td>ME?</td><td>is the shared cell 0?</td></tr></tbody></table>
<p>P(yes | female) ≠ P(female | yes): different denominators.</p></div>

<div class="box s41"><h2>4-3 · Tree diagrams</h2>
<p><b>Multiply along</b> a branch (P of a path) · <b>add across</b> the paths that give the event · branches from each point sum to 1 · all end paths sum to 1.</p>
<span class="fb">P(B) = P(A)·P(B | A) + P(Aᶜ)·P(B | Aᶜ)</span>
<p>Reverse question: <span class="f">P(A | B) = P(A ∩ B) / P(B)</span></p></div>

<div class="box s41"><h2>4-3 · "At least one"</h2>
<span class="fb">P(at least one) = 1 − P(none)</span>
<p>n independent tries, success p: <span class="f">1 − (1 − p)ⁿ</span>. Die 3 rolls, at least one 5: 1 − (5/6)³ = 91/216.</p></div>

<div class="box s42"><h2>4-4 · Fundamental counting rule</h2>
<span class="fb">k₁ × k₂ × ⋯ × kₙ</span>
<ul><li>Repetition <b>allowed</b>: same count each slot (10 × 10 × 10 × 10).</li>
<li><b>Not allowed</b>: drop by 1 each slot (10 × 9 × 8 × 7).</li>
<li>Restricted slot first (first digit ≠ 0: 9 × 9 × 8 × 7).</li>
<li><b>and → ×</b> · <b>or → +</b> (cases)</li></ul></div>

<div class="box s42"><h2>4-4 · Factorial</h2>
<p><span class="f">n! = n(n − 1)⋯2·1</span>  <span class="f">0! = 1</span>  n! = ways to arrange n different objects in a row.</p>
<table><thead><tr><th>n</th><th>0</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th><th>8</th></tr></thead>
<tbody><tr><td>n!</td><td>1</td><td>1</td><td>2</td><td>6</td><td>24</td><td>120</td><td>720</td><td>5040</td><td>40320</td></tr></tbody></table>
<p>Cancel: 8!/5! = 8·7·6 = 336.</p></div>

<div class="box s42"><h2>4-4 · Permutations (order matters)</h2>
<p><b>Rule 1</b>: <span class="fb">ₙPᵣ = n! / (n − r)!</span> ₙPₙ = n!</p>
<p><b>Rule 2</b> (identical objects): <span class="fb">n! / (r₁! r₂! ⋯ rₚ!)</span></p>
<p>STATISTICS: 10!/(3! 3! 2!) = 50,400 · LEVEL: 5!/(2! 2!) = 30. Tally the letters first; the counts must sum to n.</p></div>

<div class="box s42"><h2>4-4 · Combinations (order doesn't matter)</h2>
<span class="fb">ₙCᵣ = n! / [(n − r)! · r!] = ₙPᵣ / r!</span>
<p><span class="f">ₙCᵣ = ₙCₙ₋ᵣ</span> · <span class="f">ₙC₀ = ₙCₙ = 1</span> · <span class="f">ₙC₁ = n</span> · C ≤ P always.</p>
<p>Two groups: 3 of 7 women <b>and</b> 2 of 5 men = ₇C₃ × ₅C₂ = 35 × 10 = 350.</p>
<p>Must include a person: fix them, then ₙ₋₁Cᵣ₋₁. Must exclude: ₙ₋₁Cᵣ.</p></div>

<div class="box s42"><h2>4-4 · P or C? (does order change the result?)</h2>
<table><tbody>
<tr><td><b>Permutation</b></td><td>rank, arrange, seat, line up, 1st/2nd/3rd, distinct offices, codes, PINs, plates, order of appearance</td></tr>
<tr><td><b>Combination</b></td><td>choose, select, committee or team (no titles), group, sample, hand of cards, lottery numbers</td></tr></tbody></table>
<p>A "combination lock" is really a permutation. Casio: <span class="f">n SHIFT × r =</span> nPr · <span class="f">n SHIFT ÷ r =</span> nCr · <span class="f">SHIFT x⁻¹</span> x!</p>
<span class="ar">إذا تغيّر الناتج بتغيير الترتيب فهو تباديل، وإلا فهو توافيق. وكلمة «و» تعني الضرب، وكلمة «أو» تعني الجمع.</span></div>

<div class="box s43"><h2>4-5 · Probability with counting rules</h2>
<ol><li><b>n(S)</b>: all ways to select (usually ₙCᵣ).</li>
<li><b>n(E)</b>: ways that meet the condition (product of C's, one per group).</li>
<li><span class="f">P(E) = n(E) / n(S)</span>, then a sentence.</li></ol>
<span class="fb">P(k from group a, r − k from group b) = ₐCₖ · ᵦCᵣ₋ₖ / ₐ₊ᵦCᵣ</span>
<p>Defective: 24 circuits, 4 bad, pick 4. P(exactly 2 bad) = ₄C₂·₂₀C₂/₂₄C₄ = 1140/10626 ≈ 0.1073. P(at least 1 bad) = 1 − ₂₀C₄/₂₄C₄ ≈ 0.5440.</p>
<p>Count n(E) and n(S) with the <b>same</b> rule. The C-method equals the without-replacement chain: ₉C₃/₁₂C₃ = (9/12)(8/11)(7/10).</p>
<span class="ar">احسب فضاء العينة ثم الحدث بنفس طريقة العدّ، ثم اقسم. «على الأقل واحد» = 1 − الكل من المجموعة الأخرى.</span></div>

<div class="box tr"><h2>Traps that cost marks</h2>
<ol><li>Missing "without replacement": the second denominator must drop.</li>
<li>Putting P(B) under P(A ∩ B) when the question asks for P(B | A).</li>
<li>Treating "of those who…" as an unconditional probability.</li>
<li>Calling ME events independent.</li>
<li>Counting only one order in "one of each" (×2 in the chain method).</li>
<li>Permutation for a committee, or a combination for officers.</li>
<li>Adding instead of multiplying across groups.</li>
<li>0! = 0 (it is 1); forgetting the repeated letters in rule 2.</li>
<li>A permutation numerator over a combination denominator.</li></ol></div>

<div class="box ex"><h2>Write it like a marker reads</h2>
<ol><li>Define events; say "with" or "without replacement".</li>
<li>Name the rule: "dependent, so Rule 2"; "order doesn't matter, so ₙCᵣ".</li>
<li>Show n(E) and n(S) separately, then divide.</li>
<li>Simplify, give a decimal, check 0 ≤ P ≤ 1.</li></ol></div>

</div></div>"""
