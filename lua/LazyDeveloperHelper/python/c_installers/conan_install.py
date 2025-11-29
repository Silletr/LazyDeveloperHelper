#!/usr/bin/python3
# -*- coding: utf-8 -*-

import shutil as sh
import sys
from subprocess import run, CalledProcessError
import json
import os

# --- VARIABLES ---
CONAN = sh.which("conan")


# --- LOGGING MESSAGE ---
def log_message(message: str, level: str = "info") -> None:
    prefixes = {
        "info": "\U0001f4cd",  # 📍
        "success": "\U0001f4e6",  # 📦
        "error": "\u274c",  # ❌
    }

    print(f"{prefixes.get(level, '\U0001f4cd')} {message}")


# --- CHECK CONAN EXIST ---
def conan_exist():
    if CONAN:
        log_message("Conan exist, downloading may start!", "success")
    else:
        log_message("Conan not exist, try: pip install conan", "error")


# -------
# Helpers
# ---------
def resolve_package_name(package):
    """
    If only name is given (e.g. "spdlog"), resolve latest version from ConanCenter.
    If full name+version (e.g. "spdlog/1.14.1") — return as-is.
    """
    if "/" in package:
        return package

    log_message(f"Resolving latest version for {package}...", "info")
    try:
        result = run(
            ["conan", "search", package, "--remote=conancenter"],
            capture_output=True,
            text=True,
            check=False,
        )

        if result.returncode != 0:
            log_message(f"conan search returned an error for: {package}", "error")
            return package
        for line in result.stdout.splitlines():
            line = line.strip()
            if line and "/" in line and line.startswith(package + "/"):
                version = line.split()[0]
                log_message(f"Choised version → {version}", "info")
                return version
            log_message(f"Cannot find version for {package}", "error")
    except (CalledProcessError, json.JSONDecodeError, IndexError):
        log_message(
            f"Failed to resolve version, falling back to {package}/latest", "error"
        )
        return package


# --- INSTALLING FUNCTION ---
def install_package(lib: str):
    full_name = resolve_package_name(lib)
    lib_short = full_name.split("/")[0]  # pyright: ignore

    build_dir = f"build_{lib_short.lower()}"
    if not os.path.exists("conanfile.txt"):
        with open("conanfile.txt", "w") as f:
            f.write("[requires]\n")
            f.write("[generators]\nCMakeDeps\nCMakeToolchain\n\n")
            f.write("[options]\n*:shared=False\n")
            f.write("[imports]\n., * -> ./bin @ keep_path=False\n")
    log_message(f"Installing {full_name} → {build_dir}/", "info")

    with open("conanfile.txt", "r") as f:
        content = f.read()

    if full_name not in content:  # pyright: ignore
        # Paste into [requires] before first empty line or generators
        lines = content.splitlines()
        for i, line in enumerate(lines):
            if line.strip() == "[generators]":
                lines.insert(i, full_name)  # pyright: ignore
                break
        with open("conanfile.txt", "w") as f:
            f.write("\n".join(lines) + "\n")

    cmd = [
        "conan",
        "install",
        ".",
        "--build=missing",
        "--output-folder",
        build_dir,
        "-pr",
        "default",
        "--update",
        "-c",
        "tools.system.package_manager:mode=check",
    ]

    try:
        run(cmd, check=True, capture_output=True, text=True)
        log_message(f"{lib} successfully installed → {build_dir}/", "success")
        log_message(f"--- \tTo remove: rm -rf {build_dir}/ ---\t\n", "info")
    except CalledProcessError as e:
        error_text = e.stderr.lower()

        if (
            "opengl/system" in error_text
            or "xorg/system" in error_text
            or "libgl" in error_text
        ):
            log_message(
                f"{lib} requires native graphics libraries (OpenGL/X11)", "info"
            )
            print(
                """
            glfw (and some other GUI/graphics libraries)
            cannot be built without system OpenGL/X11 packages.

            Install them manually and run the command again:

        Arch / Manjaro:
            sudo pacman -S glu mesa-libgl libx11 libxinerama libxcursor libxrandr libxi

        Ubuntu / Debian / Pop!_OS:
            sudo apt install libgl1-mesa-dev xorg-dev libxrandr-dev libxinerama-dev libxcursor-dev

        Fedora:
            sudo dnf install mesa-libGL-devel libX11-devel libXinerama-devel libXcursor-devel libXrandr-devel libXi-devel

        After installation everything will work automatically.
        (I dont wanna make Neovim plugin for install libs to auto-installer all in row)
        """
            )
            log_message(f"{lib} skipped — system dependencies missing", "info")
            print(f"Temporary files left in: {build_dir}/ (you can delete them)")
            return

        elif "not found in local cache" in error_text:
            log_message(f"Package {full_name} not found on ConanCenter", "error")
        else:
            log_message(f"Conan failed on {lib}:", "error")
            print(e.stderr)


# --- MAIN FUNCTION ---
def main() -> None:
    conan_exist()
    if len(sys.argv) < 2:
        log_message("Provide at least one library name", "info")
        sys.exit(1)

    libs_to_install = []

    for arg in sys.argv[1:]:
        libs_to_install.append(arg)

    for lib in sys.argv[1:]:
        install_package(lib)


# --- POINT OF ENTER ---
if __name__ == "__main__":
    main()
