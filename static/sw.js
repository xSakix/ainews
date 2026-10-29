// Service worker for AI News Daily: makes the site installable as an app
// and keeps recently read pages available offline (see docs/pwa-plan.md).
// Bump VERSION only when this file's caching logic changes; new articles
// and new CSS/JS need no bump (pages are network-first, assets fingerprinted).
const VERSION = 'v1';
const PAGES = `ainews-pages-${VERSION}`;
const ASSETS = `ainews-assets-${VERSION}`;
const IMAGES = `ainews-images-${VERSION}`;
const CORE = `ainews-core-${VERSION}`;
const OFFLINE_URL = '/offline/';
const CORE_URLS = [OFFLINE_URL, '/icons/icon-192.png'];
const LIMITS = { [PAGES]: 60, [ASSETS]: 30, [IMAGES]: 80 };
const NETWORK_TIMEOUT_MS = 4000;
const writes = new Map();

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CORE).then((cache) => cache.addAll(CORE_URLS)).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil((async () => {
    const keep = new Set([PAGES, ASSETS, IMAGES, CORE]);
    for (const name of await caches.keys()) {
      if (name.startsWith('ainews-') && !keep.has(name)) await caches.delete(name);
    }
    await self.clients.claim();
    // The page that registered the worker loaded before it existed;
    // cache it now so the start page also opens offline.
    for (const client of await self.clients.matchAll({ type: 'window' })) {
      if (!isPage(new URL(client.url))) continue;
      try {
        const response = await fetch(client.url);
        if (response.ok && response.type === 'basic') {
          await remember(PAGES, new Request(client.url), response);
        }
      } catch (e) { /* offline or redirected */ }
    }
  })());
});

self.addEventListener('fetch', (event) => {
  const { request } = event;
  if (request.method !== 'GET') return;
  const url = new URL(request.url);
  if (url.origin !== self.location.origin) return;

  if (request.mode === 'navigate') {
    if (isPage(url)) event.respondWith(pageResponse(event));
  } else if (url.pathname.startsWith('/assets/')) {
    event.respondWith(cacheFirst(request, ASSETS));
  } else if (url.pathname.endsWith('/index.json')) {
    // Search index, so search keeps working offline.
    event.respondWith(networkFirst(request, PAGES));
  } else if (request.destination === 'image' || request.destination === 'font') {
    event.respondWith(staleWhileRevalidate(event, IMAGES));
  }
  // Everything else (RSS, Markdown copies, llms.txt, ...) goes straight to the network.
});

async function pageResponse(event) {
  const { request } = event;
  const cache = await caches.open(PAGES);
  try {
    const response = await withTimeout(fetch(request), NETWORK_TIMEOUT_MS);
    if (response.ok && response.type === 'basic') {
      event.waitUntil(remember(PAGES, request, response.clone()));
    }
    return response;
  } catch (e) {
    const cached = await cache.match(request, { ignoreSearch: true });
    if (cached) {
      event.waitUntil(remember(PAGES, request, cached.clone()));
      return clean(cached);
    }
    const offline = await caches.match(OFFLINE_URL);
    return offline ? clean(offline) : Response.error();
  }
}

async function networkFirst(request, cacheName) {
  const cache = await caches.open(cacheName);
  try {
    const response = await fetch(request);
    if (response.ok) await remember(cacheName, request, response.clone());
    return response;
  } catch (e) {
    return (await cache.match(request)) || Response.error();
  }
}

async function cacheFirst(request, cacheName) {
  const cache = await caches.open(cacheName);
  const cached = await cache.match(request);
  if (cached) return cached;
  const response = await fetch(request);
  if (response.ok) await remember(cacheName, request, response.clone());
  return response;
}

async function staleWhileRevalidate(event, cacheName) {
  const cache = await caches.open(cacheName);
  const cached = await cache.match(event.request);
  const update = fetch(event.request).then((response) => {
    if (response.ok) return remember(cacheName, event.request, response.clone()).then(() => response);
    return response;
  });
  if (cached) { event.waitUntil(update.catch(() => {})); return cached; }
  return update;
}

// A response that came through a redirect cannot answer a navigation.
function clean(response) {
  if (!response.redirected) return response;
  return new Response(response.body, { status: response.status, statusText: response.statusText, headers: response.headers });
}

function withTimeout(promise, ms) {
  return new Promise((resolve, reject) => {
    const timer = setTimeout(() => reject(new Error('timeout')), ms);
    promise.then((r) => { clearTimeout(timer); resolve(r); }, (e) => { clearTimeout(timer); reject(e); });
  });
}

// RSS, Markdown, manifests and other file downloads are not HTML pages,
// even when opened directly in a browser tab.
function isPage(url) {
  return url.origin === self.location.origin && !/\.[^/]+$/.test(url.pathname);
}

// Serialize writes so concurrent requests cannot exceed the limits. Moving
// an existing entry to the end keeps recently read pages, not just new ones.
// Storage failures must never prevent a successful network response.
function remember(cacheName, request, response) {
  const write = (writes.get(cacheName) || Promise.resolve()).then(async () => {
    const cache = await caches.open(cacheName);
    await cache.delete(request);
    await cache.put(request, response);
    await trim(cacheName);
  }).catch(() => {});
  writes.set(cacheName, write);
  return write;
}

async function trim(cacheName) {
  const max = LIMITS[cacheName];
  if (!max) return;
  const cache = await caches.open(cacheName);
  const keys = await cache.keys();
  for (const key of keys.slice(0, Math.max(0, keys.length - max))) await cache.delete(key);
}
