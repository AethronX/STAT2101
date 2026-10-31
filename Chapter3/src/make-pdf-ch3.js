const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

// Print-tuning layer. Forces the light palette, removes the artifact-skeleton
// safe-area padding, and keeps cards from being split across pages.
const PRINT_CSS = `
:root{
  padding:0 !important;
  color-scheme:light !important;
}
html,body{background:#ffffff !important}
body{font-size:15px !important}
.wrap{
  max-width:none !important;
  padding-left:0 !important;
  padding-right:0 !important;
  padding-block:0 0 !important;
}
.masthead{padding-block:0 28px !important}

/* keep navigation links usable inside the PDF */
.gobtn{display:inline-block !important}

/* pagination control */
.formula,.callout,.card,.ar-note,.howto,.timerbox,.flow li,.q,figure{
  break-inside:avoid; page-break-inside:avoid;
}
tr{break-inside:avoid; page-break-inside:avoid}
thead{display:table-header-group}
.sec-head,.part-head,h3,h3.grp,h4{break-after:avoid; page-break-after:avoid}
section{break-before:auto}
nav.toc{break-inside:avoid; page-break-inside:avoid}
footer{break-before:auto}

/* colour fidelity */
*{-webkit-print-color-adjust:exact !important; print-color-adjust:exact !important}
`;

function buildDocument(artifactHtml, title) {
  const marker = '<div class="wrap">';
  const i = artifactHtml.indexOf(marker);
  if (i === -1) throw new Error('could not locate <div class="wrap"> in ' + title);
  const head = artifactHtml.slice(0, i);
  const body = artifactHtml.slice(i);
  return `<!doctype html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
${head}
<style>${PRINT_CSS}</style>
</head>
<body>
${body}
</body>
</html>`;
}


const SCRATCH='/tmp/claude-0/-home-user-STAT2101/521e5d47-fbd3-5206-8b60-93d1c3cc1629/scratchpad';
const jobs = JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
const footerFor = (t) => `
<div style="width:100%;font-family:Georgia,serif;font-size:8px;color:#78828f;
            padding:0 11mm;display:flex;justify-content:space-between;align-items:center;">
  <span style="font-size:8px;">STAT 2101 · ${t}</span>
  <span style="font-size:8px;"><span class="pageNumber"></span> / <span class="totalPages"></span></span>
</div>`;
(async () => {
  const browser = await chromium.launch({ args: ['--no-sandbox'] });
  for (const job of jobs) {
    const doc = buildDocument(fs.readFileSync(job.src,'utf8'), job.title);
    const tmp = path.join(SCRATCH, path.basename(job.out, '.pdf') + '.print.html');
    fs.writeFileSync(tmp, doc, 'utf8');
    const page = await browser.newPage({ viewport: { width: 820, height: 1160 } });
    await page.emulateMedia({ media: 'screen', colorScheme: 'light' });
    await page.goto('file://' + tmp, { waitUntil: 'networkidle', timeout: 90000 });
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(800);
    const theme = await page.evaluate(() => getComputedStyle(document.body).backgroundColor);
    await page.emulateMedia({ media: 'print', colorScheme: 'light' });
    await page.pdf({ path: job.out, format: 'A4', printBackground: true,
      displayHeaderFooter: true, headerTemplate: '<div></div>', footerTemplate: footerFor(job.title),
      margin: { top: '10mm', bottom: '12mm', left: '10mm', right: '10mm' } });
    await page.close();
    console.log(path.basename(job.out).padEnd(62), 'bg', theme, (fs.statSync(job.out).size/1024|0)+' KB');
  }
  await browser.close();
})().catch(e => { console.error('FAILED:', e.message); process.exit(1); });
