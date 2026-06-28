const { chromium } = require('playwright-chromium');
const path = require('path');

(async () => {
  const browser = await chromium.launch({ channel: 'chrome' });
  const context = await browser.newContext({
    viewport: { width: 1336, height: 5000 },
    deviceScaleFactor: 2,
  });
  const page = await context.newPage();
  const fileUrl = 'file:///' + path.resolve(__dirname, 'index.html').replace(/\\/g, '/');
  await page.goto(fileUrl, { waitUntil: 'networkidle' });

  // Wait for iconify-icon web components to actually render SVG into shadow DOM.
  // Allow up to a small fraction of icons to be missing so unknown icons don't block capture.
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

  const slides = await page.$$('.slide');
  console.log(`Found ${slides.length} slides.`);
  for (let i = 0; i < slides.length; i++) {
    console.log(`Capturing slide ${i + 1}...`);
    await slides[i].screenshot({ path: path.join(__dirname, `slide-${i + 1}.png`) });
  }

  await browser.close();
  console.log('Done.');
})();
