#!usr/bin/python3
import sys
from subprocess import run, PIPE, CalledProcessError


def install_npm(lib):
    print(f"📦 Installing npm package: {lib} ...")
    result = run(["npm", "list", lib], stdout=PIPE, stderr=PIPE, text=True, check=True)
    if lib in result.stdout:
        print(f"✅ {lib} already installed")
        return
    try:
        # if lib not found - install
        result = run(
            ["npm", "install", lib.lower(), "--no-save"],
            stdout=PIPE,
            stderr=PIPE,
            text=True,
            check=True,
        )
        if result.returncode == 0:
            print(f"✅ {lib} installed successfully")
        else:
            print(f"❌ Failed to install {lib}")
            print(result.stderr)

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
