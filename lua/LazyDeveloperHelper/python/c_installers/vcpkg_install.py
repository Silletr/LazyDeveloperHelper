#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import subprocess
import shutil


# --- LOGGING MESSAGE ---
def log_message(message: str, level: str = "info") -> None:
    prefixes = {
        "info": "\U0001f4cd",  # 📍
        "success": "\U0001f4e6",  # 📦
        "error": "\u274c",  # ❌
    }

    print(f"{prefixes.get(level, '\U0001f4cd')} {message}")


# --- FIND vcpkg IN PATH ---
def find_vcpkg():
    """Find vcpkg executable cross-platform."""
    vcpkg_path = shutil.which("vcpkg")
    if not vcpkg_path:
        log_message("vcpkg not found in PATH. Install it first!", "critical")
        print(
            "Linux: git clone https://github.com/Microsoft/vcpkg && ./vcpkg/bootstrap-vcpkg.sh"
        )
        sys.exit(1)

    log_message(f"Found vcpkg: {vcpkg_path}", "info")
    return vcpkg_path


# --- INSTALL PACKAGE BY vcpkg install ---
def install_package(pkg: str):
    vcpkg_path = find_vcpkg()
    command = [vcpkg_path, "install", pkg]
    try:
        subprocess.run(command, check=True, text=True, capture_output=True)
        log_message(f"Installing: {pkg}")
        return True
    except subprocess.CalledProcessError as e:
        log_message(f"Failed: {e.stderr}")
        return False


if __name__ == "__main__":
    if len(sys.argv) != 2:
        log_message("Usage: :LazyDevInstall {package} (NeoVim Version)")
        log_message("Or: python3 vcpkg_install.py {package} (CLI Version)")
        sys.exit(1)
    package = sys.argv[1]
    install_package(package)
