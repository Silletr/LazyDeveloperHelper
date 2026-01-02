# python_installers/cargo.py
import os
from python_installers.base_class import BaseInstaller


class CargoInstaller(BaseInstaller):
    CARGO_TOML = "Cargo.toml"
    cmd = "cargo"

    def find_cargo_toml(self, start_dir: str = ".") -> str | None:
        current = os.path.abspath(start_dir)
        while current != os.path.dirname(current):
            path = os.path.join(current, self.CARGO_TOML)
            if os.path.exists(path):
                return path
            current = os.path.dirname(current)
        return None

    def get_command(self, package: str) -> list[str]:
        return [self.cmd, "add", package]
