#!usr/bin/python3
import sys
from subprocess import run, PIPE


def install_npm(lib):
    print(f"📦 Installing npm package: {lib} ...")
    result = run(["npm", "list", lib], stdout=PIPE, stderr=PIPE, text=True)
    if lib in result.stdout:
        print(f"✅ {lib} already installed")
        return

    # if lib not found - install
    result = run(
        ["npm", "install", lib.lower(), "--no-save"],
        stdout=PIPE,
        stderr=PIPE,
        text=True,
    )
    if result.returncode == 0:
        print(f"✅ {lib} installed successfully")
    else:
        print(f"❌ Failed to install {lib}")
        print(result.stderr)


def main():
    if len(sys.argv) < 2:
        print("Provide at least one npm package name")
        return

    for lib in sys.argv[1:]:
        install_npm(lib)


if __name__ == "__main__":
    main()
