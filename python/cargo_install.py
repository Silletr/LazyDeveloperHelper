#!/bin/env python3

import os
import sys
from subprocess import run, CalledProcessError
from shutil import which
from functools import lru_cache

CARGO_TOML = "Cargo.toml"


def log_message(message: str, level: str = "info") -> None:
    """Print a formatted message with an emoji prefix."""
    prefixes = {"info": "📍", "success": "📦", "error": "❌"}
    print(f"{prefixes.get(level, '📍')} {message}")


@lru_cache(maxsize=1)
def find_cargo_toml(start_dir: str = ".") -> str | None:
    """Search for Cargo.toml starting from the specified directory.

    Args:
        start_dir (str): Directory to start the search from. Defaults to current directory.

    Returns:
        str | None: Absolute path to Cargo.toml if found, None otherwise.
    """
    cargo_path = os.path.join(start_dir, CARGO_TOML)
    if os.path.exists(cargo_path):
        return cargo_path

    current_dir = os.path.abspath(start_dir)
    while current_dir != os.path.dirname(current_dir):
        parent_dir = os.path.dirname(current_dir)
        cargo_path = os.path.join(parent_dir, CARGO_TOML)
        if os.path.exists(cargo_path):
            return cargo_path
        current_dir = parent_dir
    return None


def check_cargo_installed() -> bool:
    """Check if cargo is installed and available in PATH."""
    if not which("cargo"):
        log_message("cargo is not installed or not found in PATH.", "error")
        return False
    return True


def validate_library_name(lib: str) -> bool:
    """Check if the library name is valid."""
    if not lib or any(c in lib for c in '<>|&;"'):
        log_message(f"Invalid library name: {lib}", "error")
        return False
    return True


def cargo_install(libs: list[str]) -> None:
    """Install Rust libraries using cargo add.

    Args:
        libs (list[str]): List of library names to install.
    """
    cargo_path = find_cargo_toml()
    if not cargo_path:
        log_message("Cargo.toml not found in current or parent directories.", "error")
        return

    abs_cargo_path = os.path.abspath(cargo_path)
    original_dir = os.getcwd()
    try:
        os.chdir(os.path.dirname(abs_cargo_path))
        log_message(f"Running cargo add {' '.join(libs)} ...")
        result = run(
            ["cargo", "add"] + libs,
            check=True,
            capture_output=True,
            text=True,
        )
        log_message("Cargo output:\n" + result.stdout, "success")
    except CalledProcessError as e:
        log_message(f"Failed to install {', '.join(libs)}", "error")
        log_message("stdout:\n" + e.stdout)
        log_message("stderr:\n" + e.stderr)
    finally:
        os.chdir(original_dir)


def main():
    if len(sys.argv) < 2:
        log_message("Provide at least one Rust package name", "error")
        sys.exit(1)

    libraries = [lib for lib in sys.argv[1:] if validate_library_name(lib)]
    if not libraries:
        log_message("No valid libraries provided", "error")
        sys.exit(1)

    if not check_cargo_installed():
        sys.exit(1)

    cargo_install(libraries)


if __name__ == "__main__":
    main()
