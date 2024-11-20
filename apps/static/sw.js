self.addEventListener('install', (event) => {
    console.log("[Service Worker] Install");
});
  
self.addEventListener('fetch', (event) => {
    console.log("[Service Worker] Fetched resource " + event.request.url);
});

self.addEventListener('push', (event) => {
    const data = event.data.json();
    const title = data.title || "Default title";
    const options = {
        body: data.body || "Default body",
        icon: '/static/icons/icon-192x192.png'
    };

    event.waitUntil(
        self.registration.showNotification(title, options)
    );
});
