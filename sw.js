// iborygame.com/sw.js: a clean-up worker, not the game's.
// On Oct 25, 2026 the game's files were briefly uploaded to the site root, so visitors' browsers installed the game's offline worker for
// the whole site and kept showing the cached game on the home page. A browser checks this file for changes on every visit; when it finds
// this version, it clears what the old worker cached, removes the worker, and reloads open pages so they show the real site.
// The game has its own worker at /play/sw.js, which is not affected. Keep this file at the root for a few months.
self.addEventListener("install", function () { self.skipWaiting(); });
self.addEventListener("activate", function (e) {
  e.waitUntil(
    caches.keys()
      .then(function (keys) { return Promise.all(keys.map(function (k) { return caches.delete(k); })); }) // the game re-caches its own files on its next start
      .then(function () { return self.registration.unregister(); })
      .then(function () { return self.clients.matchAll({ type: "window" }); })
      .then(function (cs) { cs.forEach(function (c) { if (!/\/play\//.test(new URL(c.url).pathname)) c.navigate(c.url); }); })
  );
});
