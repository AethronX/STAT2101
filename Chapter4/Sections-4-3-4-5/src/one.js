const { chromium } = require('playwright'); const fs = require('fs');
(async () => {
  const j = JSON.parse(fs.readFileSync(process.argv[2]))[0];
  const raw = fs.readFileSync(j.src, 'utf8'); const i = raw.indexOf('<div class="wrap">');
  const html = `<!doctype html><html lang="en" data-theme="light"><head><meta charset="utf-8">${raw.slice(0, i)}<style>:root{padding:0!important}html,body{background:#fff!important;margin:0}.wrap{padding:0!important}*{-webkit-print-color-adjust:exact;print-color-adjust:exact}</style></head><body>${raw.slice(i)}</body></html>`;
  const tmp = j.src.replace('.html', '.print.html'); fs.writeFileSync(tmp, html);
  const b = await chromium.launch({ args: ['--no-sandbox'] }); const p = await b.newPage();
  await p.emulateMedia({ media: 'print', colorScheme: 'light' });
  await p.goto('file://' + tmp, { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(600);
  await p.pdf({ path: j.out, format: 'A4', printBackground: true, margin: { top: '7mm', bottom: '7mm', left: '7mm', right: '7mm' } });
  await b.close();
})();
