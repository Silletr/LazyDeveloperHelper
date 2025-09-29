#!/usr/bin/env python3

import sys
from subprocess import run, CalledProcessError
from shutil import which
from typing import List

LUAROCKS_FLAG = "--local"


def log_message(message: str, level: str = "info") -> None:
    """Print a formatted message with an emoji prefix.

    Args:
        message (str): Message to print.
        level (str): Message level ('info', 'success', 'error'). Defaults to 'info'.
    """
    prefixes = {"info": "📍", "success": "✅", "error": "❌"}
    print(f"{prefixes.get(level, '📍')} {message}")


# --- CHECKING LUAROCKS INSTALLED
def check_luarocks_installed() -> bool:
    """Check if luarocks is installed and available in PATH."""
    if not which("luarocks"):
        log_message("luarocks is not installed or not found in PATH.", "error")
        return False
    return True


# --- CHECKING LIBRARY NAME
def validate_library_name(lib: str) -> bool:
    """Check if the library name is valid.

    Args:
        lib (str): Library name to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    if not lib or any(c in lib for c in '<>|&;"'):
        log_message(f"Invalid library name: {lib}", "error")
        return False
    return True


# --- INSTALLING BY LUAROCKS
def install_luarocks(libs: List[str]) -> None:
    """Install LuaRocks packages.

    Args:
        libs (List[str]): List of package names to install.
    """
    if not check_luarocks_installed():
        return

    for lib in libs:
        if not validate_library_name(lib):
            continue

        log_message(f"Installing LuaRocks package {lib} ...")
        try:
            result = run(
                ["luarocks", "install", lib, LUAROCKS_FLAG],
                check=True,
                text=True,
                capture_output=True,
            )
            stdout_lower = result.stdout.lower()
            if "installed" in stdout_lower or "already installed" in stdout_lower:
                log_message(f"{lib} installed or already present", "success")
                log_message(result.stdout)
            else:
                log_message(f"{lib} installation output above", "success")
                log_message(result.stdout)
        except CalledProcessError as e:
            log_message(f"Failed to install {lib}", "error")
            log_message(f"stdout:\n{e.stdout}")
            log_message(f"stderr:\n{e.stderr}")
            log_message(f"Return code: {e.returncode}")


# --- START DOWNLOADING
def main():
    if len(sys.argv) < 2:
        log_message("Provide at least one LuaRocks package name", "error")
        sys.exit(1)

    libraries = [lib for lib in sys.argv[1:] if validate_library_name(lib)]
    if not libraries:
        log_message("No valid libraries provided", "error")
        sys.exit(1)

    install_luarocks(libraries)


if __name__ == "__main__":
    main()
