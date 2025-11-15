github_release() {
  echo "[*] Preparing clean release…"

  rm -rf /tmp/ldh_release
  mkdir -p /tmp/ldh_release/LazyDeveloperHelper

  echo "[*] Copying required files:"

  cp -r plugin /tmp/ldh_release/LazyDeveloperHelper/
  cp -r lua /tmp/ldh_release/LazyDeveloperHelper/
  echo "[*] Copying README.md, LICENSE files"
  cp README.md /tmp/ldh_release/LazyDeveloperHelper/
  cp LICENSE /tmp/ldh_release/LazyDeveloperHelper/

  echo "[*] Zipping to /tmp/ldh_release:"
  cd /tmp/ldh_release
  zip -r LazyDeveloperHelper.zip LazyDeveloperHelper >/dev/null

  echo "[*] Moving archive to LazyDeveloperHelper/dist:"
  mkdir -p ./dist
  mv LazyDeveloperHelper.zip ./dist/

  echo "[✓] Done. Clean .zip is in dist/, size:"
  du -h dist/LazyDeveloperHelper.zip
}
