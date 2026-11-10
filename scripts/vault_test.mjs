/* Test the vault's crypto exactly as the app implements it.
   WebCrypto promises never settle under Chromium's virtual clock, so this runs
   in Node (which has the same webcrypto API) against functions lifted verbatim
   out of the app file. */
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

/* Relative to this file, not to whatever machine wrote it. This carried an
   absolute path into somebody's home directory, so the crypto suite only ever
   ran where it was written. */
const here = dirname(fileURLToPath(import.meta.url));
const html = readFileSync(join(here, "..", "docs", "play", "index.html"), "utf8");

function grab(name) {
  const i = html.indexOf("  function " + name + "(");
  if (i < 0) throw new Error("not found: " + name);
  let depth = 0, started = false, j = i;
  for (; j < html.length; j++) {
    const c = html[j];
    if (c === "{") { depth++; started = true; }
    else if (c === "}") { depth--; if (started && depth === 0) { j++; break; } }
  }
  return html.slice(i, j);
}

const src = ["b64", "unb64", "deriveKey", "sealCases", "openCases"].map(grab).join("\n");
const crypto = globalThis.crypto;
const btoa_ = (s) => Buffer.from(s, "binary").toString("base64");
const atob_ = (s) => Buffer.from(s, "base64").toString("binary");
const fn = new Function("crypto", "btoa", "atob", src + "\nreturn { b64, unb64, deriveKey, sealCases, openCases };");
const { deriveKey, sealCases, openCases } = fn(crypto, btoa_, atob_);

const cases = [{ id: 1, name: "Test patient", notes: "burning headache", selection: [{ idx: 4, path: "Head › Headache" }] }];
const pass = "correct horse battery";
const salt = crypto.getRandomValues(new Uint8Array(16));

const results = [];
const ok = (n, c, d) => results.push((c ? "PASS " : "FAIL ") + n + (c ? "" : "  — " + d));

const key = await deriveKey(pass, salt);
const rec = await sealCases(cases, key, salt);

ok("sealed record has the expected fields", rec.v === 1 && rec.salt && rec.iv && rec.ct, JSON.stringify(Object.keys(rec)));
ok("ciphertext does not contain the plaintext", rec.ct.indexOf("Test") === -1 && Buffer.from(rec.ct, "base64").toString("binary").indexOf("patient") === -1);

const key2 = await deriveKey(pass, Buffer.from(rec.salt, "base64"));
const back = await openCases(rec, key2);
ok("right passphrase round-trips", JSON.stringify(back) === JSON.stringify(cases), JSON.stringify(back));

const wrong = await deriveKey("wrong passphrase", Buffer.from(rec.salt, "base64"));
let rejected = false;
try { await openCases(rec, wrong); } catch (e) { rejected = true; }
ok("wrong passphrase fails to decrypt", rejected);

const tampered = JSON.parse(JSON.stringify(rec));
const raw = Buffer.from(tampered.ct, "base64");
raw[3] = raw[3] ^ 0xff;
tampered.ct = raw.toString("base64");
let tamperRejected = false;
try { await openCases(tampered, key2); } catch (e) { tamperRejected = true; }
ok("tampered ciphertext is rejected (GCM tag)", tamperRejected);

const t0 = Date.now();
await deriveKey(pass, salt);
ok("key derivation is slow enough to be worth having", Date.now() - t0 > 40, (Date.now() - t0) + " ms");

console.log(results.join("\n"));
console.log(results.some(r => r.startsWith("FAIL")) ? "FAILED" : "ALL PASS (" + results.length + ")");
