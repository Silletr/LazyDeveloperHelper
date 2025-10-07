#!/usr/bin/env python3
import os
import sys
from subprocess import run, CalledProcessError
from shutil import which
from typing import Set


# Logging function
def log_message(message: str, level: str = "info") -> None:
    """Print a formatted message with an emoji prefix."""
    prefixes = {"info": "📦", "success": "✅", "error": "❌"}
    print(f"{prefixes.get(level, '📦')} {message}")


# Check if pip3 is installed
def check_pip_installed() -> bool:
    """Check if pip3 is installed and available in PATH."""
    pip_path = which("pip3")
    if pip_path is None:
        log_message("pip3 is not installed or not found in PATH.", "error")
        return False
    return True


# Validate library name
def validate_library_name(lib_name: str) -> bool:
    """Check if the library name is valid."""
    if not lib_name or any(c in lib_name for c in '<>|&;"'):
        log_message(f"Invalid library name: {lib_name}", "error")
        return False
    return True


def install_lib(
    lib_name: str, libs_list: Set[str], req_path: str = "requirements.txt"
) -> None:
    """Install a Python library using pip if not already installed."""
    if not check_pip_installed():
        return
    if not validate_library_name(lib_name):
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
        stdout_lower = result.stdout.lower()
        if "requirement already satisfied" in stdout_lower:
            log_message(f"{lib_name} already installed", "success")
            log_message(result.stdout, "info")
        elif "successfully installed" in stdout_lower:
            log_message(f"{lib_name} successfully installed", "success")
            log_message(result.stdout, "info")
    except CalledProcessError as e:
        log_message(f"Failed to install {lib_name}", "error")
        log_message(f"stdout: {e.stdout}", "error")
        log_message(f"stderr: {e.stderr}", "error")
        log_message(f"Return code: {e.returncode}", "error")


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
