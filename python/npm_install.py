#!/usr/bin/python3
import sys
from subprocess import run, PIPE, CalledProcessError


def install_npm(lib):
    print(f"📦 Checking npm package: {lib} ...")
    # Check if package is installed, without raising an error on failure
    result = run(["npm", "list", lib], stdout=PIPE, stderr=PIPE, text=True, check=False)
    if result.returncode == 0 and lib in result.stdout:
        print(f"✅ {lib} already installed")
        return

    # Package not found, attempt to install
    print(f"📦 Installing npm package: {lib} ...")
    try:
        result = run(
            ["npm", "install", lib.lower(), "--no-save"],
            stdout=PIPE,
            stderr=PIPE,
            text=True,
            check=True,
        )
        print(f"✅ {lib} installed successfully")
    except CalledProcessError as e:
        print(f"❌ Failed to install {lib}")
        print("🔻 stdout:\n", e.stdout)
        print("🔻 stderr:\n", e.stderr)
        print("🔚 Return code:", e.returncode)


def main():
    if len(sys.argv) < 2:
        print("Provide at least one npm package name")
        return
    for lib in sys.argv[1:]:
        install_npm(lib)


if __name__ == "__main__":
    main()
