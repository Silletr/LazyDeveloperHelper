#!/usr/bin/python3
# -*- coding: utf-8 -*-

from shutil import which as wh
import sys
import subprocess
from pathlib import Path

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


# --- CHECK gradle EXIST ---
def gradle_exists() -> bool:
    if gradle:
        log_message(f"Used Gradle: {gradle}")
        return True
    else:
        log_message("Gradle doesnt exists, install it!", "error")
        return False


# --- FIND GRADLE PROJECT ---
def find_gradle_project() -> Path | None:
    """Find nearest Gradle project (build.gradle OR build.gradle.kts)"""
    current_dir = Path.cwd()
    for depth in range(5):
        # Check both Groovy and Kotlin DSL
        for gradle_file in ["build.gradle", "build.gradle.kts"]:
            build_gradle = current_dir / gradle_file
            if build_gradle.exists():
                log_message(
                    f"Found Gradle {
                        'Kotlin DSL' if 'kts' in gradle_file else 'Groovy'
                    } project: {build_gradle}"
                )
                return current_dir  # ✅ Return PROJECT DIR, not file parent
        current_dir = current_dir.parent
    return None


# --- ADD DEPENDENCY TO BUILD.GRADLE(.KTS) ---
def add_dependency_to_build(project_dir: Path, lib: str) -> bool:
    for gradle_file in ["build.gradle", "build.gradle.kts"]:
        build_file = project_dir / gradle_file
        if not build_file.exists():
            continue

        content = build_file.read_text()

        if "::" in lib:
            # "commons-lang3::org.apache.commons:commons-lang3:3.12.0"
            #   ↑ artifact    ↑ group:artifact:version
            # gav = "org.apache.commons:commons-lang3:3.12.0"
            artifact, gav = lib.split("::", 1)

            dep_line = f'    implementation("{gav}")'
            log_msg = gav
        else:
            dep_line = f'    implementation("{lib}:latest.release")'
            log_msg = f"{lib}:latest.release"

        if "dependencies {" not in content:
            continue

        new_content = content.replace("dependencies {", f"dependencies {{\n{dep_line}")

        build_file.write_text(new_content)
        log_message(f"✅ Added '{log_msg}' to {gradle_file}", "success")
        return True

    return False


# --- INSTALLING GRADLE PACKAGE ---
def install_package(lib: str) -> bool:
    """Add lib to build.gradle THEN run gradle build"""
    project_dir = find_gradle_project()
    if not project_dir:
        log_message("No Gradle project found nearby!", "error")
        return False

    # Step 1: Add dependency to build.gradle (like conan)
    if not add_dependency_to_build(project_dir, lib):
        return False

    # Step 2: Run gradle build (download + build)
    try:
        result = subprocess.run(
            [str(gradle), "build", "--refresh-dependencies"],
            cwd=project_dir,
            capture_output=True,
            text=True,
            check=True,
        )
        log_message(f"✅ '{lib}' added and built successfully!", "success")
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        log_message(f"Build failed for '{lib}'", "error")
        print(e.stdout)
        print(e.stderr)
        return False
    except Exception as e:
        log_message(f"Install error: {e}", "error")
        return False


# --- POINT OF ENTER ---
def main() -> None:
    if not gradle_exists():
        return

    if len(sys.argv) < 2:
        log_message("Provide at least one gradle package name", "error")
        print(f"Usage: {sys.argv[0]} group::artifact:version")
        print("Example: commons-lang3::commons-lang3:3.12.0")
        return

    for lib in sys.argv[1:]:
        install_package(lib)


if __name__ == "__main__":
    main()
