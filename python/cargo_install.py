#!/usr/bin/python3

from tomlkit import parse
import sys
import os
from subprocess import run

"""
HINTS:
example = '''
[dependecies]
serde = "1.0"
'''

subprocess.run(
    ["cargo", "add", lib_name],
    check=True,
    capture_output=True,
    text=True,
)
"""
def cargo_install(lib_name):
    try:
        doc = parse("../Cargo.toml")
    except Exception as e:
        print(e)
    result = run(
        ["cargo", "add", lib_name],
        check=True,
        capture_output=True,
        text=True,
    )

def main():
    if len(sys.argv) < 2:
        print("Provide at least one Rust package name")
        return

    for lib in sys.argv[1:]:
        cargo_install(lib)


if __name__ == "__main__":
    main()
