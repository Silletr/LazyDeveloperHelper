#!/usr/bin/env python3
import sys
import subprocess
import os


def install_lib(lib_name):
    print(f"📦 Installing LuaRocks package {lib_name} ...\n")
    result = subprocess.run("luarocks", "install", lib_name,
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

    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install {lib_name}")
        print(e.output)

def main():
    if len(sys.argv) < 2:
        print("Provide at least one LuaRocks package name")
        return

    for lib in sys.argv[1:]:
        install_luarock(lib)

if __name__ == "__main__":
    main()

