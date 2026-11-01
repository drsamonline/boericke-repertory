/* Boericke's Repertory — service worker.
 *
 * The one rule that matters here: the HTML is NETWORK-FIRST. A cache-first
 * worker answering the page from a stale cache is how a shipped fix becomes
 * invisible to a returning reader. Assets are cache-first with a background
 * refresh, and CACHE is bumped on every release so an old copy is dropped.
 *
 * SPDX-FileCopyrightText: 2026 Dr Sohil Momin
 */
var CACHE = "boericke-1.4.0";
var ASSETS = [
  "./",
  "./index.html",
  "./manifest.webmanifest",
  "./sw.js",
  "../icon.svg",
  "./icon.png",
  "../assets/icon-192.png",
  "../assets/icon-512.png"
];

self.addEventListener("install", function (e) {
  self.skipWaiting();
  e.waitUntil(caches.open(CACHE).then(function (c) {
    return Promise.all(ASSETS.map(function (u) {
      return c.add(new Request(u, { cache: "reload" })).catch(function () {});
    }));
  }));
});

self.addEventListener("activate", function (e) {
  e.waitUntil(caches.keys().then(function (keys) {
    return Promise.all(keys.filter(function (k) { return k !== CACHE; }).map(function (k) { return caches.delete(k); }));
  }).then(function () { return self.clients.claim(); }));
});

self.addEventListener("fetch", function (e) {
  var req = e.request;
  if (req.method !== "GET") return;
  var isDoc = req.mode === "navigate" || (req.headers.get("accept") || "").indexOf("text/html") !== -1;

  if (isDoc) {
    /* network first: a new release is picked up on the next load */
    e.respondWith(
      fetch(req).then(function (res) {
        var copy = res.clone();
        caches.open(CACHE).then(function (c) { c.put(req, copy); });
        return res;
      }).catch(function () {
        return caches.match(req).then(function (hit) { return hit || caches.match("./index.html"); });
      })
    );
    return;
  }

  /* assets: cache first, refresh in the background */
  e.respondWith(
    caches.match(req).then(function (hit) {
      var net = fetch(req).then(function (res) {
        if (res && res.status === 200 && res.type === "basic") {
          var copy = res.clone();
          caches.open(CACHE).then(function (c) { c.put(req, copy); });
        }
        return res;
      }).catch(function () { return hit; });
      return hit || net;
    })
  );
});
