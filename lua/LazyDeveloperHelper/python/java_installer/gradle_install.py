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
    current_dir = Path.cwd()
    for depth in range(5):
        build_gradle = current_dir / "build.gradle"
        build_gradle_kts = current_dir / "build.gradle.kts"

        if build_gradle.exists():
            log_message(f"Found Gradle Groovy project: {build_gradle}")
            return build_gradle
        elif build_gradle_kts.exists():
            log_message(f"Found Gradle Kotlin DSL project: {build_gradle_kts}")
            return build_gradle_kts

        current_dir = current_dir.parent
    return None


# --- ADD DEPENDENCY TO BUILD.GRADLE ---
def add_dependency_to_build(build_dir: Path, lib: str) -> bool:
    """Add dependency line to build.gradle dependencies block"""
    build_file = build_dir / "build.gradle"

    # Simple lib parsing: group:artifact:version or just artifact
    if "::" in lib:
        group, artifact_version = lib.split("::", 1)
        artifact, version = artifact_version.rsplit(":", 1)
        dep_line = f"    implementation '{group}:{artifact}:{version}'"
    else:
        # Fallback: assume org.example:lib:1.0.0 pattern
        dep_line = f"    implementation '{lib}:1.0.0'"

    content = build_file.read_text()

    # Find dependencies block and add line
    if "dependencies {" in content:
        # Insert before closing brace
        new_content = content.replace("dependencies {", f"dependencies {{\n{dep_line}")
        build_file.write_text(new_content)
        log_message(f"Added '{lib}' to build.gradle", "success")
        return True
    else:
        log_message("No dependencies block found in build.gradle", "error")
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
            ["gradle", "build", "--refresh-dependencies"],
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
