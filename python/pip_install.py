#!/usr/bin/env python3

import os
import sys
from subprocess import run, CalledProcessError
from shutil import which
from typing import Set


# LOGGING MESSAGE ---
def check_pip_installed() -> bool:
    """Check if pip3 is installed and available in PATH."""
    pip_path = which("pip3")
    if pip_path is None:
        log_message("pip3 is not installed or not found in PATH.", "error")
        return False
    return True


def log_message(message: str, level: str = "info") -> None:
    prefixes = {"info": "📍", "success": "📦", "error": "❌"}
    print(f"{prefixes.get(level, '📍')} {message}")


# --- VALIDATE LIB NAME
def validate_library_name(lib_name: str) -> bool:
    """Check if the library name is valid."""
    if not lib_name or any(c in lib_name for c in '<>|&;"'):
        log_message(f"Invalid library name: {lib_name}", "error")
        return False
    return True


# --- INSTALLING LIBS ---
def install_lib(
    lib_name: str, libs_list: Set[str], req_path: str = "requirements.txt"
) -> None:
    """
    Install a Python package via pip. Accepts optional requirements file path.
    Keeps behavior deterministic and prints unified messages (emoji prefixes).
    """
    if not check_pip_installed():
        return
    if not validate_library_name(lib_name):
        return

    log_message(f"Installing {lib_name} ...", "info")

    # Ensure requirements file exists
    if not os.path.exists(req_path):
        try:
            with open(req_path, "w", encoding="utf-8") as f:
                f.write("")  # create empty file
        except OSError as e:
            log_message(f"Could not create {req_path}: {e}", "error")
            return
    log_message(f"Installing {lib_name} ...")

    # Update requirements.txt
    if not os.path.exists(req_path):
        with open(req_path, "w", encoding="utf-8") as f:
            f.write("")  # Create empty file

    with open(req_path, "r", encoding="utf-8") as file:
        all_libs = file.readlines()
        libs_list.update(line.strip().split("==")[0].lower() for line in all_libs)

    if lib_name.lower() not in libs_list:
        with open(req_path, "a", encoding="utf-8") as file:
            file.write(f"{lib_name}\n")
        libs_list.add(lib_name.lower())

    # Read existing libs (case-insensitive)
    libs_set: Set[str] = set()
    try:
        with open(req_path, "r", encoding="utf-8") as file:
            for line in file:
                name = line.strip().split("==")[0].lower()
                if name:
                    libs_set.add(name)
    except OSError as e:
        log_message(f"Could not read {req_path}: {e}", "error")
        return

    # Append to requirements if missing
    if lib_name.lower() not in libs_set:
        try:
            with open(req_path, "a", encoding="utf-8") as file:
                file.write(f"{lib_name}\n")
        except OSError as e:
            log_message(f"Could not write to {req_path}: {e}", "error")
            return

    # Run pip install
    try:
        result = run(
            [
                sys.executable,
                "-m",
                "pip",
                "install",
                "--upgrade",
                lib_name,
                "--break-system-packages",
            ],
            check=True,
            text=True,
            capture_output=True,
        )
        stdout_lower = (result.stdout or "").lower()
        if "requirement already satisfied" in stdout_lower:
            log_message(f"{lib_name} already installed", "success")
            if result.stdout:
                log_message(result.stdout, "info")
        elif "successfully installed" in stdout_lower:
            log_message(f"{lib_name} successfully installed", "success")
            if result.stdout:
                log_message(result.stdout, "info")
        else:
            # some pip outputs may differ — still show stdout for debugging
            log_message(f"{lib_name} installation output:", "info")
            if result.stdout:
                log_message(result.stdout, "info")

    except CalledProcessError as e:
        log_message(f"Failed to install {lib_name}", "error")
        log_message(f"stdout:\n{e.stdout}")
        log_message(f"stderr:\n{e.stderr}")
        log_message(
            f"Return code: {getattr(e, 'returncode', 'unknown')}",
            "error",
        )
    except Exception as e:
        log_message(
            f"Unexpected error while installing {lib_name}: {e}",
            "error",
        )


def main() -> None:
    """Main function to process command-line arguments."""
    print(">>> pip_install started <<<")
    if len(sys.argv) < 2:
        log_message("Provide at least one library name", "error")
        sys.exit(1)

    libs_list: Set[str] = set()
    for lib in sys.argv[1:]:
        install_lib(lib, libs_list)


if __name__ == "__main__":
    main()
