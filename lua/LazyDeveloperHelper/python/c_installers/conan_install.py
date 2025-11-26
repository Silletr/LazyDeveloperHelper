import shutil as sh
from loguru import logger
import sys

# --- VARIABLES ---
CONAN = sh.which("conan")


# --- CHECK CONAN EXIST ---
def conan_exist():
    if CONAN:
        logger.info("✅ Conan exist, starting download!")
    else:
        logger.critical("❌ Conan not exist, try: pip install conan")


def install_package(): ...


# --- MAIN FUNCTION ---
def main() -> None:
    conan_exist()
    if len(sys.argv) < 2:
        logger.error("Provide at least one library name")
        sys.exit(1)
    """
    for lib in libs_to_install:
        install_package(lib, libs_list)
    """


# --- POINT OF ENTER ---
if __name__ == "__main__":
    main()
