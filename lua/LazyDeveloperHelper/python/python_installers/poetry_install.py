from base_class import BaseInstaller
import subprocess


class PoetryInstaller(BaseInstaller):
    cmd = "poetry"

    def get_command(self, package: str) -> list[str]:
        return [self.cmd, "add", package]

    def install(self, package: str) -> subprocess.CompletedProcess:
        return self.run(package)
