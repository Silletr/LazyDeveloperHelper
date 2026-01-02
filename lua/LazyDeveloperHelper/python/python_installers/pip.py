import subprocess
import os
from .base_class import BaseInstaller


class PipInstaller(BaseInstaller):
    def __init__(self):
        super().__init__("pip3")

    def get_command(self, package: str) -> list[str]:
        return ["pip3", "install", package]

    def install(self, package: str) -> subprocess.CompletedProcess:
        return self.run_install(package)

    def add_to_requirements(
        self, package: str, req_path: str = "requirements.txt"
    ) -> None:
        """Add package to requirements.txt"""
        if not os.path.exists(req_path):
            open(req_path, "w").close()

        with open(req_path, "r", encoding="utf-8") as f:
            existing = {
                line.strip().split("==")[0].lower() for line in f if line.strip()
            }

        if package.lower() not in existing:
            with open(req_path, "a", encoding="utf-8") as f:
                f.write(f"{package}\n")
