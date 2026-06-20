const { chromium } = require('playwright-chromium');
const path = require('path');

(async () => {
  const browser = await chromium.launch({ channel: 'chrome' });
  const context = await browser.newContext({
    viewport: { width: 1280, height: 720 },
    deviceScaleFactor: 2,
  });
  const page = await context.newPage();
  const fileUrl = 'file:///' + path.resolve(__dirname, 'index.html').replace(/\\/g, '/');

  await page.goto(fileUrl, { waitUntil: 'networkidle' });

  // Wait for iconify-icon shadow DOMs to render SVG
  try {
    await page.waitForFunction(() => {
      const icons = Array.from(document.querySelectorAll('iconify-icon'));
      if (icons.length === 0) return true;
      const ready = icons.filter(el => el.shadowRoot && el.shadowRoot.querySelector('svg')).length;
      return ready / icons.length >= 0.98;
    }, { timeout: 60000 });
  } catch (e) {
    console.log('Icon wait threshold not fully met, proceeding anyway.');
  }

  await page.waitForTimeout(1500);

  // Force print media so @media print rules apply
  await page.emulateMedia({ media: 'print' });

  await page.pdf({
    path: path.join(__dirname, 'slides.pdf'),
    width: '1280px',
    height: '720px',
    printBackground: true,
    margin: { top: 0, bottom: 0, left: 0, right: 0 },
    preferCSSPageSize: false,
  });

  await browser.close();
  console.log('PDF saved: slides.pdf');
})();
