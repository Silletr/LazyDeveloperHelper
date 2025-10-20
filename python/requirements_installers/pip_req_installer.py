#!/bin/env python3

# --- IMPORTS ---
import os

# --- VARIABLES ---
REQUIREMENTS_FILE = "requirements.txt"


# --- LOGGING MESSAGE ---
def log_message(message: str, level: str = "info") -> None:
    prefixes = {"info": "📍", "success": "📦", "error": "❌"}
    print(f"{prefixes.get(level, '📍')} {message}")


# --- INSTALL REQUIREMENTS FROM FILE ---
def install_requirements():
    search_path = "."
    for dirpath, _, filenames in os.walk(search_path):
        if REQUIREMENTS_FILE in filenames:
            log_message("requirements.txt is found!", "success")
            return os.path.join(dirpath, REQUIREMENTS_FILE)
        else:
            log_message(
                "requirements.txt is not exist! Try to `touch requirements.txt`", "info"
            )
            break


install_requirements()
