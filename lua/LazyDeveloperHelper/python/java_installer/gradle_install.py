#!/usr/bin/python3

# from subprocess import CalledProcessError, run <- Ruff dont agree un-used import
from shutil import which as wh
import sys


from logger import log_message

# --- CHECK GRADLE ---
gradle = wh("gradle")


def gradle_exists():
    if gradle:
        log_message(f"Used Gradle: {gradle}")
        log_message("Gradle exist, downloading", "success")
    else:
        log_message("Gradle doesnt exists, install it!", "error")


# --- INSTALLING gradle PACKAGE ---
def install_package(lib: str):
    pass


# --- POINT OF ENTER ---
def main() -> None:
    gradle_exists()
    if len(sys.argv) < 2:
        print("Provide at least one npm package name")
        return
    for lib in sys.argv[1:]:
        install_package(lib)
