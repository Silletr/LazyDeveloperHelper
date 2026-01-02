# python_installers/cargo.py
import os
import subprocess
from python_installers.base_class import BaseInstaller


class CargoInstaller(BaseInstaller):
    CARGO_TOML = "Cargo.toml"

    def __init__(self):
        super().__init__("cargo")

    def find_cargo_toml(self, start_dir: str = ".") -> str | None:
        current = os.path.abspath(start_dir)
        while current != os.path.dirname(current):
            path = os.path.join(current, self.CARGO_TOML)
            if os.path.exists(path):
                return path
            current = os.path.dirname(current)
        return None

    def get_command(self, package: str) -> list[str]:
        return ["cargo", "add", package]

<<<<<<< HEAD
    def install(self, package: str) -> subprocess.CompletedProcess:
        cargo_toml = self.find_cargo_toml()
        if not cargo_toml:
            raise RuntimeError("Cargo.toml not found in current or parent directories")
=======
        Returns:
        str | None: Absolute path to Cargo.toml if found, None otherwise.
    """
    cargo_path = os.path.join(start_dir, CARGO_TOML)
    if os.path.exists(cargo_path):
        abs_path = os.path.abspath(cargo_path)
        log_message(f"Found Cargo.toml at: {abs_path}", "info")
        return abs_path
    # --- IF Cargo.toml IS FOUND
    current_dir = os.path.abspath(start_dir)
    while current_dir != os.path.dirname(current_dir):
        parent_dir = os.path.dirname(current_dir)
        cargo_path = os.path.join(parent_dir, CARGO_TOML)
        if os.path.exists(cargo_path):
            abs_path = os.path.abspath(cargo_path)
            log_message(f"Found Cargo.toml at: {abs_path}", "info")
            return abs_path
        current_dir = parent_dir
    log_message("Cargo.toml not found in current or parent directories.", "error")
    return None
>>>>>>> f0e6ead ([NEW FILE/DIR: lua/LazyDeveloperHelper/python/python_installers/test_of_poetry/*, test_files/test_conan/main.c, lua/LazyDeveloperHelper/python/python_installers/factory.py | MOVED FILE/DIR: lua/LazyDeveloperHelper/python/pip_install.py -> lua/LazyDeveloperHelper/python/python_installers/pip_install.py, !!! TOO MUCH MORE !!!] Completed Python architecture changes, tomorrow i`ll be busy with Lua rework)

        project_dir = os.path.dirname(cargo_toml)
        original_dir = os.getcwd()

        try:
            os.chdir(project_dir)
            return self.run_install(package)
        finally:
            os.chdir(original_dir)
