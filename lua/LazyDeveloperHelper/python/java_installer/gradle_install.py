#!/usr/bin/python3
# -*- coding: utf-8 -*-

# from subprocess import CalledProcessError, run <- Ruff dont agree un-used import


from shutil import which as wh
import sys

# --- CHECK GRADLE ---
gradle = wh("gradle")


# --- LOGGING MESSAGE ---
def log_message(message: str, level: str = "info") -> None:
    prefixes = {
        "info": "\U0001f4cd",  # 📍
        "success": "\U0001f4e6",  # 📦
        "error": "\u274c",  # ❌
    }

    print(f"{prefixes.get(level, '\U0001f4cd')} {message}")


def gradle_exists() -> bool:
    if gradle:
        log_message(f"Used Gradle: {gradle}")
        log_message("Gradle exist, downloading", "success")
        return True
    else:
        log_message("Gradle doesnt exists, install it!", "error")
        return False


# --- INSTALLING gradle PACKAGE ---
def install_package(lib: str):
    # command = [gradle, "install"], lib   <- My pre-commit config angry on this
    pass


# --- POINT OF ENTER ---
def main() -> None:
    # Check if gradle exists first
    if not gradle_exists():
        return

    # Check if arguments were provided
    if len(sys.argv) < 2:
        log_message("Provide at least one gradle package name", "error")
        print(f"Usage: {sys.argv[0]} <package1> <package2> ...")
        return

    # Install each package
    for lib in sys.argv[1:]:
        install_package(lib)


if __name__ == "__main__":
    main()
