#!/usr/bin/env python3
from subprocess import CalledProcessError, run
import sys


def install_luarocks(lib_name):
    print(f"📦 Installing LuaRocks package {lib_name} ...\n")
    try:
        result = run(
            ["luarocks", "install", lib_name, "--local"],
            check=True,
            text=True,
            capture_output=True,
        )
        stdout_lower = result.stdout.lower()
        if "installed" in stdout_lower or "already installed" in stdout_lower:
            print(result.stdout)
            print(f"✅ {lib_name} installed or already present")
        else:
            print(result.stdout)
            print(f"✅ {lib_name} installation output above")

    except CalledProcessError as e:
        print(f"❌ Failed to install {lib_name}")
        print("🔻 stdout:\n", e.stdout)
        print("🔻 stderr:\n", e.stderr)
        print("🔚 Return code:", e.returncode)


def main():
    if len(sys.argv) < 2:
        print("Provide at least one LuaRocks package name")
        return

    for lib in sys.argv[1:]:
        install_luarocks(lib)


if __name__ == "__main__":
    main()
