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


def gradle_exists():
    if gradle:
        log_message(f"Used Gradle: {gradle}")
        log_message("Gradle exist, downloading", "success")
    else:
        log_message("Gradle doesnt exists, install it!", "error")


# --- INSTALLING gradle PACKAGE ---
def install_package(lib: str):
    print(lib)


# --- POINT OF ENTER ---
def main() -> None:
    gradle_exists()
    if len(sys.argv) < 2:
        print("Provide at least one npm package name")
        return
    for lib in sys.argv[1:]:
        install_package(lib)
