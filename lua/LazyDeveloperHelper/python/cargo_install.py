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

    def install(self, package: str) -> subprocess.CompletedProcess:
        cargo_toml = self.find_cargo_toml()
        if not cargo_toml:
            raise RuntimeError("Cargo.toml not found in current or parent directories")

        project_dir = os.path.dirname(cargo_toml)
        original_dir = os.getcwd()

        try:
            os.chdir(project_dir)
            return self.run_install(package)
        finally:
            os.chdir(original_dir)
