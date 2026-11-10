// OYUN-DEP Service Worker
const CACHE_NAME = 'oyun-dep-v1';
const URLS_TO_CACHE = [
  '/',
  '/giris-sayfasi',
  '/static/css/stil.css',
  '/static/js/oyun.js',
  '/static/img/maskot.svg',
  '/static/img/liman.svg',
  '/static/img/orman.svg',
  '/static/img/dag.svg',
  '/static/img/gol.svg',
  '/static/img/kale.svg'
];

// Kurulum: Dosyaları önbelleğe al
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('Önbellek açıldı');
        return cache.addAll(URLS_TO_CACHE);
      })
  );
  self.skipWaiting();
});

// Aktifleştirme: Eski önbellekleri temizle
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          if (cacheName !== CACHE_NAME) {
            console.log('Eski önbellek silindi:', cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
  self.clients.claim();
});

// Fetch: Önce ağdan dene, olmazsa önbellekten getir
self.addEventListener('fetch', event => {
  // Sadece GET isteklerini önbelleğe al
  if (event.request.method !== 'GET') return;

  // API çağrılarını önbelleğe alma
  if (event.request.url.includes('/oyun/kaydet') || 
      event.request.url.includes('/avatar-guncelle')) {
    return;
  }

  event.respondWith(
    fetch(event.request)
      .then(response => {
        // Dinamik önbellekleme (sadece static dosyalar)
        if (event.request.url.includes('/static/')) {
          const responseClone = response.clone();
          caches.open(CACHE_NAME).then(cache => {
            cache.put(event.request, responseClone);
          });
        }
        return response;
      })
      .catch(() => {
        // Ağ yoksa önbellekten getir
        return caches.match(event.request);
      })
  );
});