import subprocess
from abc import ABC, abstractmethod


class BaseInstaller(ABC):
    """Base class for all installers"""

    def __init__(self, cmd_name: str):
        self.cmd_name = cmd_name

    def is_installed(self, installer: str = "pip3") -> bool:
        """Checks is installer installed (wtf, too confused :D)"""
        self.installer = installer
        result = subprocess.run(
            ["which", self.installer], capture_output=True, text=True
        )
        return result.returncode == 0

    @abstractmethod
    def install(self, package: str) -> subprocess.CompletedProcess:
        """Installing package, returns - subprocess result"""
        pass

    @abstractmethod
    def get_command(self, package: str) -> list[str]:
        """Return command for subprocess"""
        pass

    def run_install(self, package: str) -> subprocess.CompletedProcess:
        """Unique installer with logging"""
        if not self.is_installed():
            raise RuntimeError(f"{self.cmd_name} not found in PATH")

        cmd = self.get_command(package)
        return subprocess.run(cmd, capture_output=True, text=True)
