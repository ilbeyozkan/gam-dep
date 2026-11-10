// PWA Service Worker Kaydı
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/sw.js')
      .then(registration => {
        console.log('✅ Service Worker kaydedildi. Kapsam:', registration.scope);
      })
      .catch(error => {
        console.log('❌ Service Worker hatası:', error);
      });
  });
}