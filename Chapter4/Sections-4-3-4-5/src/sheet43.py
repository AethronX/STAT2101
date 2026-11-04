import sys, json
sys.path.insert(0, "/tmp/claude-0/-home-user-STAT2101/521e5d47-fbd3-5206-8b60-93d1c3cc1629/scratchpad/ch3")
from ch3lib import head, markup

CSS = """<style>
body{font-size:10.2px !important;line-height:1.4 !important}
.wrap{max-width:none;zoom:ZOOM}
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
.s43{--sec:var(--ink-3);--wash:var(--ink-3-wash)} .s41{--sec:var(--ink-1);--wash:var(--ink-1-wash)} .s42{--sec:var(--ink-2);--wash:var(--ink-2-wash)} .tr{--sec:var(--accent);--wash:var(--accent-wash)} .ex{--sec:var(--ink-4);--wash:var(--ink-4-wash)}
svg text{font-family:var(--mono);font-size:9px;fill:currentColor}
@page{size:A4;margin:0}
</style>"""


import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))
from sheet43_body import BODY
import os
Z = os.environ.get("Z","1.0")
doc = head("Probability 4-3 to 4-5 Sheet") + CSS.replace("zoom:ZOOM", "zoom:"+Z) + markup(BODY, {})
src = "/home/user/STAT2101/Chapter4/Sections-4-3-4-5/html/One-Page-Sheet.html"
open(src, "w", encoding="utf-8").write(doc)
json.dump([dict(src=src, out="/home/user/STAT2101/Chapter4/Sections-4-3-4-5/STAT2101-Ch4-4-3-4-5-One-Page-Sheet.pdf", title="sheet")],
          open("/tmp/claude-0/-home-user-STAT2101/521e5d47-fbd3-5206-8b60-93d1c3cc1629/scratchpad/p41/sheet43.json", "w"))
