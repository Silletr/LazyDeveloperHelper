import shutil as sh
from loguru import logger
import sys
from subprocess import run


# --- VARIABLES ---
CONAN = sh.which("conan")


# --- CHECK CONAN EXIST ---
def conan_exist():
    if CONAN:
        logger.info("✅ Conan exist, downloading may start!")
    else:
        logger.critical("❌ Conan not exist, try: pip install conan")


def install_package(lib: list):
    run(
        ["conan", "install", "."]
        + ["--build=missing", "-pr", "default"]
        + ["--output-folder=build"],
        check=True,
        text=True,
        capture_output=True,
    )


# --- MAIN FUNCTION ---
def main() -> None:
    conan_exist()
    if len(sys.argv) < 2:
        logger.error("Provide at least one library name")
        sys.exit(1)

    libs_to_install = []

    for arg in sys.argv[1:]:
        libs_to_install.append(arg)

    for _ in libs_to_install:
        logger.info(f"Starting downloading {libs_to_install}... ")
        install_package(libs_to_install)


# --- POINT OF ENTER ---
if __name__ == "__main__":
    main()
