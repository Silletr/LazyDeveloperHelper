from .base_class import BaseInstaller
import subprocess


class PoetryInstaller(BaseInstaller):
    def __init__(self):
        super().__init__("poetry")

    def get_command(self, package: str) -> list[str]:
        return ["poetry", "add", package]

    def install(self, package: str) -> subprocess.CompletedProcess:
        return self.run_install(package)
