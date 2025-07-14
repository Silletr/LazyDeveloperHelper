#!/bin/bash
set -e

echo "[*] Preparing clean release…"

rm -f dist/LazyDeveloperHelper.zip
rm -rf /tmp/ldh_release

mkdir -p /tmp/ldh_release/LazyDeveloperHelper
cp -r plugin /tmp/ldh_release/LazyDeveloperHelper/
cp -r python /tmp/ldh_release/LazyDeveloperHelper/
cp README.md LICENSE contributing.md requirements.txt /tmp/ldh_release/LazyDeveloperHelper/

echo "[*] Zipping..."
cd /tmp/ldh_release
zip -r LazyDeveloperHelper.zip LazyDeveloperHelper > /dev/null

echo "[*] Moving..."
mkdir -p ~/Projects/LazyDeveloperHelper/dist
mv LazyDeveloperHelper.zip ~/Projects/LazyDeveloperHelper/dist/

echo "[✓] Done. Clean .zip is in dist/, size:"
du -h ~/Projects/LazyDeveloperHelper/dist/LazyDeveloperHelper.zip
