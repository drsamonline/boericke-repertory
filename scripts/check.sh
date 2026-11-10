#!/usr/bin/env bash
# Guard against the one failure a 900 kB single-file app hides well: a syntax
# error that silently kills the whole script, leaving a page that renders and
# does nothing. Extracts the app's script and hands it to node --check.
set -euo pipefail
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

for f in "$REPO/docs/play/index.html"; do
  python3 - "$f" "$TMP/app.js" <<'PY'
import io, re, sys
src, out = sys.argv[1], sys.argv[2]
s = io.open(src, encoding="utf-8").read()
m = re.search(r"<script>\n/\* =+\n   Boericke.*?</script>", s, re.S)
if not m:
    sys.exit("could not find the app script in " + src)
io.open(out, "w", encoding="utf-8").write(m.group(0)[len("<script>"):-len("</script>")])
PY
  node --check "$TMP/app.js"
  echo "syntax ok: ${f#$REPO/}"
done

echo "--- self-test (headless Chromium) ---"
CHROME="$(command -v chromium || command -v chromium-browser || command -v google-chrome)"
PROFILE="$(mktemp -d)"
"$CHROME" --headless --no-sandbox --disable-gpu --allow-file-access-from-files \
  --user-data-dir="$PROFILE" --virtual-time-budget=15000 --dump-dom \
  "file://$REPO/tools/selftest.html" 2>/dev/null |
  python3 -c "import sys,re,html; d=sys.stdin.read(); m=re.search(r'<pre id=\"out\">(.*?)</pre>', d, re.S); print(html.unescape(m.group(1)) if m else 'NO OUTPUT')"
rm -rf "$PROFILE"

echo "--- vault crypto (node) ---"
node "$REPO/scripts/vault_test.mjs"
