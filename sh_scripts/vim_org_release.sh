vim_org_release() {
	echo "[*] Preparing clean release…"

	rm -f dist/LazyDeveloperHelper.zip
	rm -rf /tmp/ldh_release

	echo "[*] Copying folders"
	mkdir -p /tmp/ldh_release/LazyDeveloperHelper
	cp -r lua/LazyDeveloperHelper/commands/ /tmp/ldh_release/LazyDeveloperHelper/
	cp -r lua/LazyDeveloperHelper/init.lua /tmp/ldh_release/LazyDeveloperHelper/

	echo "[*] Copying files for test workability"
	cp -r test_files/test.* /tmp/ldh_release/LazyDeveloperHelper/

	cp -r lua/LazyDeveloperHelper/python/c_installers /tmp/ldh_release/LazyDeveloperHelper/
	cp -r lua/LazyDeveloperHelper/python/requirements_installers /tmp/ldh_release/LazyDeveloperHelper/
	find lua/LazyDeveloperHelper/python/java_installer -name 'gradle_install.py' -exec cp --parents {} /tmp/ldh_release/LazyDeveloperHelper/ \;
	find lua/LazyDeveloperHelper/python/java_installer -name 'build.kotlin.kts' -exec cp --parents {} /tmp/ldh_release/LazyDeveloperHelper/ \;

	echo "[*] Copying License, commit-generator.py, changelog.md"
	cp LICENSE commit_generation.py CHANGELOG.md /tmp/ldh_release/LazyDeveloperHelper/

	echo "[*] Zipping..."
	cd /tmp/ldh_release
	zip -r LazyDeveloperHelper.zip LazyDeveloperHelper >/dev/null

	echo "[*] Moving..."
	mkdir -p ~/Projects/LazyDeveloperHelper/dist
	mv LazyDeveloperHelper.zip ~/Projects/LazyDeveloperHelper/dist/

	echo "[✓] Done. Clean .zip is in dist/, size:"
	du -h ~/Projects/LazyDeveloperHelper/dist/LazyDeveloperHelper.zip
}
