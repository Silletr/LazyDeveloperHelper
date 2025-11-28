import shutil as sh
from loguru import logger
import sys
from subprocess import run, CalledProcessError
import json


# --- VARIABLES ---
CONAN = sh.which("conan")


# --- CHECK CONAN EXIST ---
def conan_exist():
    if CONAN:
        logger.info("✅ Conan exist, downloading may start!")
    else:
        logger.critical("❌ Conan not exist, try: pip install conan")


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #
def resolve_package_name(package: str) -> str:
    """
    If only name is given (e.g. "spdlog"), resolve latest version from ConanCenter.
    If full name+version (e.g. "spdlog/1.14.1") — return as-is.
    """
    if "/" in package:
        return package

    logger.info(f"Resolving latest version for {package}...")
    try:
        result = run(
            ["conan", "search", package, "--remote=conancenter"],
            capture_output=True,
            text=True,
            check=False,
        )

        if result.returncode != 0:
            logger.warning(f"conan search returned an error for: {package}")
            return package
        for line in result.stdout.splitlines():
            line = line.strip()
            if line and "/" in line and line.startswith(package + "/"):
                version = line.split()[0]
                logger.success(f"Choised version → {version}")
                return version
            logger.warning(f"Cannot find version for {package}")
    except (CalledProcessError, json.JSONDecodeError, IndexError):
        logger.warning(f"Failed to resolve version, falling back to {package}/latest")
        return package

    return f"{package}/latest"


# --- INSTALLING FUNCTION ---
def install_package(lib: str) -> None:
    full_name = resolve_package_name(lib)
    lib_short = full_name.split("/")[0]
    build_dir = f"build_{lib_short.lower()}"

    conanfile_content = f"""
[requires]
{full_name}

[generators]
CMakeDeps
CMakeToolchain

[options]
*:shared=False

[imports]
., * -> ./bin @ keep_path=False
    """

    with open("conanfile.txt", "w") as f:
        f.write(conanfile_content)

    logger.info(f"Installing {full_name} → {build_dir}/")

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
        logger.success(f"{lib} successfully installed → {build_dir}/")
        print(f"To remove: rm -rf {build_dir}")
    except CalledProcessError as e:
        error_text = e.stderr.lower()

        if (
            "opengl/system" in error_text
            or "xorg/system" in error_text
            or "libgl" in error_text
        ):
            logger.warning(f"{lib} requires native graphics libraries (OpenGL/X11)")
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
            logger.info(f"{lib} skipped — system dependencies missing")
            print(f"Temporary files left in: {build_dir}/ (you can delete them)")
            return

        elif "not found in local cache" in error_text:
            logger.error(f"Package {full_name} not found on ConanCenter")
        else:
            logger.error(f"Conan failed on {lib}:")
            print(e.stderr)


# --- MAIN FUNCTION ---
def main() -> None:
    conan_exist()
    if len(sys.argv) < 2:
        logger.error("Provide at least one library name")
        sys.exit(1)

    libs_to_install = []

    for arg in sys.argv[1:]:
        libs_to_install.append(arg)

    for lib in sys.argv[1:]:
        install_package(lib)


# --- POINT OF ENTER ---
if __name__ == "__main__":
    main()
