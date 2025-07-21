#!/usr/bin/env python3

import sys
import os
from subprocess import run


def cargo_install(lib_name):
    cargo_path = "Cargo.toml"
    if not os.path.exists(cargo_path):
        print("❌ Cargo.toml not found in expected location.")
        return

    # Start installing from Cargo
    print(f"🔧 Running cargo add {lib_name} ...")
    try:
        result = run(
            ["cargo", "add", lib_name],
            check=True,
            capture_output=True,
            text=True,
        )
        print("📦 Cargo output:\n", result.stdout)
    except Exception as e:
        print("❌ cargo add failed:", e)
        return


def main():
    if len(sys.argv) < 2:
        print("Provide at least one Rust package name")
        return

    for lib in sys.argv[1:]:
        cargo_install(lib)


if __name__ == "__main__":
    main()
