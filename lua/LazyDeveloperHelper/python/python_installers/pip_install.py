from base_class import BaseInstaller
import subprocess


class PipInstaller(BaseInstaller):
    cmd = "pip3"

    def get_command(self, package: str) -> list[str]:
        return [self.cmd, "install", package]

    def install(self, package: str) -> subprocess.CompletedProcess:
        return self.run(package)
