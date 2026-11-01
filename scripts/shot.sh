#!/usr/bin/env bash
# Screenshot the landing page and the app with headless Chromium.
#
#   scripts/shot.sh                        # landing page -> docs/assets/landing-*.png
#   scripts/shot.sh app                    # the app      -> docs/assets/app-*.png
#   scripts/shot.sh app app '?q=thirst%20fever&pick=4&tab=chart'
#
# Always shoot a page with content on it: a shot of an empty search box sells
# nothing. Look at the files before committing them.
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
KIND="${1:-landing}"
NAME="${2:-$KIND}"
QUERY="${3:-}"

if [ "$KIND" = "app" ]; then PAGE="$REPO/docs/play/index.html"; else PAGE="$REPO/docs/index.html"; fi
[ -f "$PAGE" ] || { echo "no page at $PAGE" >&2; exit 1; }

CHROME="$(command -v chromium || command -v chromium-browser || command -v google-chrome)"
mkdir -p "$REPO/docs/assets"

shot () { # width, height, outfile
  "$CHROME" --headless --no-sandbox --disable-gpu --hide-scrollbars \
    --force-device-scale-factor=1 --window-size="$1,$2" \
    --virtual-time-budget=9000 --screenshot="$3" "file://$PAGE$QUERY" >/dev/null 2>&1
  echo "wrote ${3#$REPO/} ($(stat -c%s "$3") bytes)"
}

case "$KIND" in
  app)     shot 1280 1180 "$REPO/docs/assets/${NAME}-desktop.png"
           shot 430   900 "$REPO/docs/assets/${NAME}-mobile.png" ;;
  landing) shot 1280 2400 "$REPO/docs/assets/${NAME}-desktop.png"
           shot 430  2000 "$REPO/docs/assets/${NAME}-mobile.png" ;;
  *) echo "kind must be landing or app" >&2; exit 1 ;;
esac
