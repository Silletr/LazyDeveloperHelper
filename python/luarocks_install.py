#!/usr/bin/env python3
from typing import List
import sys
import os
from subprocess import run, CalledProcessError
from shutil import which

LUAROCKS_FLAG = "--local"

def log_message(message: str, level: str = "info") -> None:
    prefixes = {"info": "📍", "success": "📦", "error": "❌"}
    print(f"{prefixes.get(level, '📍')} {message}")

def check_luarocks_installed() -> bool:
    """Return True if luarocks binary is present in PATH."""
    if not which("luarocks"):
        log_message("luarocks is not installed or not found in PATH.", "error")
        return False
    return True

def validate_library_name(lib: str) -> bool:
    """Simple validation to avoid injection / weird names."""
    if not lib or any(c in lib for c in '<>|&;"'):
        log_message(f"Invalid library name: {lib}", "error")
        return False
    return True

def install_luarocks(libs: List[str]) -> None:
    """Install one or more luarocks packages."""
    if not check_luarocks_installed():
        return

    for lib in libs:
        if not validate_library_name(lib):
            continue

        log_message(f"Installing LuaRocks package {lib} ...", "info")
        try:
            result = run(
                ["luarocks", "install", lib, LUAROCKS_FLAG],
                check=True,
                text=True,
                capture_output=True,
            )
            stdout_lower = result.stdout.lower()
            # success messages can vary; be permissive
            if "installed" in stdout_lower or "already installed" in stdout_lower:
                log_message(f"{lib} installed or already present", "success")
                if result.stdout:
                    log_message(result.stdout, "info")
            else:
                log_message(f"{lib} installation output above", "success")
                if result.stdout:
                    log_message(result.stdout, "info")
        except CalledProcessError as e:
            log_message(f"Failed to install {lib}", "error")
            log_message(f"stdout:\n{e.stdout}")
            log_message(f"stderr:\n{e.stderr}")
            log_message(f"Return code: {e.returncode}", "error")
        except FileNotFoundError as e:
            log_message(f"File error: {e}", "error")
        except PermissionError as e:
            log_message(f"Permission error: {e}", "error")

def main() -> None:
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

