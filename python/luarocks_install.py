#!/usr/bin/env python3
from typing import List
import sys
from subprocess import run, CalledProcessError
from shutil import which

# --- VARIABLES ---

LUAROCKS_FLAG = "--local"
luarocks_path = which("luarocks")


# -- LOGGING MESSAGE
def log_message(message: str, level: str = "info") -> None:
    prefixes = {"info": "📍", "success": "📦", "error": "❌"}
    print(f"{prefixes.get(level, '📍')} {message}")


# --- CHECKING LUAROCKS INSTALLED
def check_luarocks_installed() -> bool:
    """Check if luarocks is installed and available in PATH."""
    if luarocks_path is None:
        log_message("luarocks is not installed or not found in PATH.", "error")
        return False
    return True


# --- CHECKING LIBRARY NAME
def validate_library_name(lib: str) -> bool:
    """Simple validation to avoid injection / weird names."""
    if not lib or any(c in lib for c in '<>|&;"'):
        log_message(f"Invalid library name: {lib}", "error")
        return False
    return True


# --- INSTALLING BY LUAROCKS
def install_luarocks(libs: List[str]) -> None:
    for lib in libs:
        if not validate_library_name(lib):
            continue

        luarocks_path = which("luarocks")
        if not luarocks_path:
            log_message("luarocks is not found in PATH", "error")
            return

        log_message(f"Installing LuaRocks package {lib} ...", "info")
        try:
            assert luarocks_path is not None, "luarocks_path should not be None"
            result = run(
                [luarocks_path, "install", lib, LUAROCKS_FLAG],
                check=True,
                text=True,
                stdout=None,
                stderr=None,
                capture_output=True,
            )
            stdout_lower = result.stdout.lower()
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


# --- START DOWNLOADING
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
