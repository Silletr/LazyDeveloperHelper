#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List
import sys
import argparse
from subprocess import run, CalledProcessError
from shutil import which

# --- VARIABLES ---
LUAROCKS_FLAG = "--local"
luarocks_path = which("luarocks")


# --- LOGGING MESSAGE ---
def log_message(message: str, level: str = "info") -> None:
    prefixes = {
        "info": "\U0001f4cd",  # 📍
        "success": "\U0001f4e6",  # 📦
        "error": "\u274c",  # ❌
    }

    print(f"{prefixes.get(level, '\U0001f4cd')} {message}")


# --- CHECKING LIBRARY NAME ---
def validate_library_name(lib: str) -> bool:
    if not lib or any(c in lib for c in '<>|&;"'):
        log_message(f"Invalid library name: {lib}", "error")
        return False
    return True


# --- INSTALLING BY LUAROCKS ---
def install_luarocks(libs: List[str], quiet: bool = False) -> None:
    for lib in libs:
        if not validate_library_name(lib):
            continue

        luarocks_path = which("luarocks")
        if not luarocks_path:
            log_message("luarocks is not found in PATH", "error")
            return

        log_message(f"Installing LuaRocks package {lib} ...", "info")

        # Build arguments
        flags = [LUAROCKS_FLAG]
        if quiet:
            flags.append("-q")

        luarocks_args = [luarocks_path, "install", lib] + flags

        try:
            result = run(
                luarocks_args,
                check=True,
                text=True,
                capture_output=True,
            )
            stdout_lower = result.stdout.lower()
            if "installed" in stdout_lower or "already installed" in stdout_lower:
                log_message(f"{lib} installed or already present", "success")

            if result.stdout and not quiet:
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


# --- MAIN ---
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("libs", nargs="*", help="LuaRocks packages to install")
    parser.add_argument("--quiet", action="store_true", help="Suppress output")

    args, unknown = parser.parse_known_args()

    # unknown contains anything argparse didn’t understand
    # remove any optional flags accidentally included in libs
    libs = [lib for lib in args.libs if not lib.startswith("--")]

    if not args.libs:
        log_message("No valid libraries provided", "error")
        sys.exit(1)
    install_luarocks(libs, quiet=args.quiet)


if __name__ == "__main__":
    main()
