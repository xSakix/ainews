// Run with Playwright installed outside the repo; CI supplies NODE_PATH.
const { chromium } = require('playwright');
const assert = require('node:assert/strict');
const { spawn } = require('node:child_process');
const { once } = require('node:events');
const [,, root, port = '8765'] = process.argv;
assert(root, 'Usage: node scripts/test_pwa_browser.cjs PUBLIC_DIR [PORT]');
const base = `http://localhost:${port}`;
const editions = ['', 'sk', 'nl', 'fr', 'de', 'es', 'zh'];
const headings = ["You're offline", 'Ste offline', 'Je bent offline', 'Vous êtes hors ligne', 'Sie sind offline', 'Sin conexión', '您已离线'];
const wait = ms => new Promise(resolve => setTimeout(resolve, ms));
(async () => {
  const server = spawn('python3', ['-m', 'http.server', port, '-d', root], { stdio: 'ignore' });
  let browser;
  try {
    for (let i = 0; i < 40; i++) { try { await fetch(base); break; } catch { await wait(100); } }
    browser = await chromium.launch({ args: ['--no-sandbox'] });
    const context = await browser.newContext();
    const page = await context.newPage();
    const jsErrors = [];
    page.on('pageerror', e => jsErrors.push(e.message));
    const cdp = await context.newCDPSession(page);
    const articles = [];
    for (const edition of editions) {
      const home = edition ? `/${edition}/` : '/';
      await page.goto(base + home);
      await page.evaluate(() => navigator.serviceWorker.ready);
      await page.waitForFunction(() => !!navigator.serviceWorker.controller);
      await page.waitForFunction(async () => !!await caches.match(location.href));
      const errors = (await cdp.send('Page.getInstallabilityErrors')).installabilityErrors;
      assert.deepEqual(errors, []);
      const mf = await cdp.send('Page.getAppManifest');
      assert.deepEqual(mf.errors, []);
      assert.equal(JSON.parse(mf.data).start_url, home);
      const article = await page.locator('.post-entry a.entry-link').first().getAttribute('href');
      await page.goto(article);
      const title = await page.locator('h1').first().textContent();
      await page.waitForFunction(async () => !!await caches.match(location.href));
      articles.push({url: article, title});
      console.log('INSTALLABLE', edition || 'en', 'article cached');
    }
    await page.goto(base + '/sk/search/', { waitUntil: 'networkidle' });
    await page.locator('#searchInput').fill('AI');
    // PaperMod searches on keyup, whereas Playwright.fill only fires input.
    await page.locator('#searchInput').press('End');
    await page.waitForFunction(async () => !!await caches.match(new URL('/sk/index.json', location.origin).href));
    await page.waitForFunction(() => document.querySelectorAll('#searchResults li').length > 0);
    server.kill(); await once(server, 'exit');
    for (const [i, edition] of editions.entries()) {
      const home = edition ? `/${edition}/` : '/';
      assert.equal((await page.goto(base + home)).status(), 200);
      assert.equal(await page.locator('#saved').count(), 0);
      assert.equal((await page.goto(articles[i].url)).status(), 200);
      assert.equal(await page.locator('h1').first().textContent(), articles[i].title);
      const computedStyle = await page.locator('body').evaluate(el => getComputedStyle(el).fontFamily);
      assert(!computedStyle.includes('Times New Roman'));
      await page.goto(base + home + 'never-read/');
      assert.equal(await page.locator('h1').textContent(), headings[i]);
      await page.waitForFunction(() => document.querySelectorAll('#saved li').length >= 14);
      console.log('OFFLINE', edition || 'en', 'home/article/localized fallback OK');
    }
    await page.goto(base + '/sk/search/', { waitUntil: 'networkidle' });
    await page.locator('#searchInput').fill('AI');
    await page.locator('#searchInput').press('End');
    await page.waitForFunction(() => document.querySelectorAll('#searchResults li').length > 0);
    console.log('OFFLINE SEARCH OK');
    assert.deepEqual(jsErrors, []);
    console.log('Browser checks passed with no JavaScript errors.');
  } finally {
    if (browser) await browser.close();
    if (server.exitCode === null && server.signalCode === null) server.kill();
  }
})().catch(e => { console.error(e); process.exitCode = 1; });
