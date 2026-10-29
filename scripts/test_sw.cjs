// Exercise the worker's observable fetch/lifecycle behavior using Node built-ins.
const assert = require('node:assert/strict');
const { test } = require('node:test');
const { readFileSync } = require('node:fs');
const { runInNewContext } = require('node:vm');
const source = readFileSync(require('node:path').join(__dirname, '../static/sw.js'), 'utf8');
const origin = 'https://example.test';

function harness() {
  const listeners = {}, stores = new Map();
  let network = async () => response('fresh');
  let failWrites = false;
  const key = r => new URL(typeof r === 'string' ? r : r.url, origin).href;
  const cacheStorage = {
    async keys() { return [...stores.keys()]; },
    async delete(name) { return stores.delete(name); },
    async open(name) {
      if (!stores.has(name)) stores.set(name, new Map());
      const entries = stores.get(name);
      return {
        async keys() { return [...entries.keys()].map(u => new Request(u)); },
        async delete(r) { return entries.delete(key(r)); },
        async put(r, value) {
          if (failWrites) throw new Error('quota');
          entries.set(key(r), value.clone());
        },
        async match(r, options = {}) {
          const url = key(r);
          const found = options.ignoreSearch
            ? [...entries].find(([u]) => u.split('?')[0] === url.split('?')[0])?.[1]
            : entries.get(url);
          return found?.clone();
        },
        async addAll(urls) { for (const u of urls) await this.put(u, await network(u)); },
      };
    },
    async match(r) {
      for (const name of stores.keys()) {
        const value = await (await this.open(name)).match(r);
        if (value) return value;
      }
    },
  };
  runInNewContext(source, {
    self: {
      location: { origin },
      addEventListener: (name, fn) => { listeners[name] = fn; },
      skipWaiting: async () => {},
      clients: { claim: async () => {}, matchAll: async () => [{ url: origin + '/sk/' }] },
    },
    caches: cacheStorage, fetch: (...args) => network(...args),
    Request, Response, URL, setTimeout, clearTimeout,
  });
  return {
    caches: cacheStorage,
    setNetwork(fn) { network = fn; },
    failWrites() { failWrites = true; },
    async lifecycle(name) {
      const pending = [];
      listeners[name]({ waitUntil: p => pending.push(p) });
      await Promise.all(pending);
    },
    async get(path, { mode = 'navigate', method = 'GET', destination = '' } = {}) {
      const pending = [];
      let result;
      const request = { url: new URL(path, origin).href, method, mode, destination };
      listeners.fetch({ request, waitUntil: p => pending.push(p), respondWith: p => { result = p; } });
      const value = await result;
      await Promise.all(pending);
      return value;
    },
  };
}
function response(text, status = 200) {
  const r = new Response(text, { status });
  Object.defineProperty(r, 'type', { value: 'basic' });
  return r;
}

test('install precaches only the shell; activate preserves unrelated caches and saves the first page', async () => {
  const h = harness();
  await h.caches.open('ainews-pages-old');
  await h.caches.open('another-app');
  await h.lifecycle('install');
  assert.deepEqual((await (await h.caches.open('ainews-core-v1')).keys()).map(r => new URL(r.url).pathname), ['/offline/', '/icons/icon-192.png']);
  await h.lifecycle('activate');
  assert(!(await h.caches.keys()).includes('ainews-pages-old'));
  assert((await h.caches.keys()).includes('another-app'));
  assert(await (await h.caches.open('ainews-pages-v1')).match('/sk/'));
});

test('pages are fresh online, saved offline; unread pages use the shell and 404s are not saved', async () => {
  const h = harness();
  await h.lifecycle('install');
  assert.equal(await (await h.get('/sk/read/')).text(), 'fresh');
  h.setNetwork(async () => response('updated'));
  assert.equal(await (await h.get('/sk/read/')).text(), 'updated');
  h.setNetwork(async () => response('missing', 404));
  assert.equal((await h.get('/sk/missing/')).status, 404);
  assert.equal(await (await h.caches.open('ainews-pages-v1')).match('/sk/missing/'), undefined);
  h.setNetwork(async () => { throw new Error('offline'); });
  assert.equal(await (await h.get('/sk/read/')).text(), 'updated');
  assert.equal(await (await h.get('/sk/unread/')).text(), 'fresh');
});

test('concurrent writes are bounded and revisited pages survive eviction', async () => {
  const h = harness();
  await Promise.all(Array.from({ length: 60 }, (_, i) => h.get(`/posts/${i}/`)));
  await h.get('/posts/0/');
  await h.get('/posts/new/');
  const cache = await h.caches.open('ainews-pages-v1');
  assert.equal((await cache.keys()).length, 60);
  assert(await cache.match('/posts/0/'));
  assert.equal(await cache.match('/posts/1/'), undefined);
  await h.get('/sk/index.json', { mode: 'cors' });
  assert.equal((await cache.keys()).length, 60);
  for (const [cacheName, prefix, count, destination] of [
    ['ainews-assets-v1', '/assets/', 30, 'script'],
    ['ainews-images-v1', '/images/', 80, 'image'],
  ]) {
    await Promise.all(Array.from({ length: count + 5 }, (_, i) => h.get(`${prefix}${i}`, { mode: 'cors', destination })));
    assert.equal((await (await h.caches.open(cacheName)).keys()).length, count);
  }
});

test('RSS, Markdown, text, external and non-GET requests pass through', async () => {
  const h = harness();
  for (const path of ['/index.xml', '/sk/posts/a/index.md', '/llms.txt', '/manifest.webmanifest', 'https://external.test/']) {
    assert.equal(await h.get(path), undefined);
  }
  assert.equal(await h.get('/sk/', { method: 'POST' }), undefined);
});

test('cache storage failures do not discard successful network responses', async () => {
  const h = harness();
  h.failWrites();
  for (const [path, options] of [
    ['/sk/', {}], ['/sk/index.json', { mode: 'cors' }],
    ['/assets/a.js', { mode: 'cors' }], ['/images/a.png', { mode: 'cors', destination: 'image' }],
  ]) assert.equal(await (await h.get(path, options)).text(), 'fresh');
});

test('slow navigation falls back after four seconds and cleans a cached redirect', async () => {
  const h = harness();
  const cached = new Response('saved redirect');
  // Response.clone in the shim cannot preserve redirected, so exercise clean
  // separately through a cache match override on the real response instance.
  const open = h.caches.open.bind(h.caches);
  h.caches.open = async name => {
    const cache = await open(name);
    if (name === 'ainews-pages-v1') cache.match = async () => {
      Object.defineProperty(cached, 'redirected', { value: true, configurable: true });
      return cached;
    };
    return cache;
  };
  h.setNetwork(() => new Promise(() => {}));
  const start = Date.now();
  const result = await h.get('/slow/');
  assert(Date.now() - start >= 3900);
  assert.equal(result.redirected, false);
  assert.equal(await result.text(), 'saved redirect');
});

test('fingerprinted assets are cache-first and images revalidate in the background', async () => {
  const h = harness();
  await h.get('/assets/a.js', { mode: 'cors' });
  await h.get('/images/a.png', { mode: 'cors', destination: 'image' });
  h.setNetwork(async () => response('updated'));
  assert.equal(await (await h.get('/assets/a.js', { mode: 'cors' })).text(), 'fresh');
  assert.equal(await (await h.get('/images/a.png', { mode: 'cors', destination: 'image' })).text(), 'fresh');
  h.setNetwork(async () => { throw new Error('offline'); });
  assert.equal(await (await h.get('/images/a.png', { mode: 'cors', destination: 'image' })).text(), 'updated');
});
