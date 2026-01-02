import subprocess
from abc import ABC, abstractmethod
from shutil import which


class BaseInstaller(ABC):
    """Base class for all installers"""

    def __init__(self, cmd: str) -> None:
        self.cmd = cmd

    def is_installed(self) -> bool:
        """Checks is installer installed (wtf, too confused :D)"""
        return which(self.cmd) is not None

    @abstractmethod
    def install(self, package: str) -> subprocess.CompletedProcess:
        """Installing package, returns - subprocess result"""
        pass

    @abstractmethod
    def get_command(self, package: str) -> list[str]:
        """Return command for subprocess"""
        pass

    def run(self, package: str) -> subprocess.CompletedProcess:
        if not self.is_installed():
            raise RuntimeError(f"{self.cmd} not found in PATH!")

        return subprocess.run(
            self.get_command(package), capture_output=True, text=True, check=True
        )
