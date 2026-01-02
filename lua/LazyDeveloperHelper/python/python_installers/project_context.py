from enum import Enum
from pathlib import Path


class PythonProjectType(Enum):
    REQUIREMENTS = "requirements"
    POETRY = "poetry"
    UV = "uv"


class PythonProjectContext:
    def __init__(self, cwd: str):
        self.cwd = cwd

    def detect(self) -> PythonProjectType:
        if (Path(self.cwd) / "pyproject.toml").exists():
            return PythonProjectType.POETRY
        if (Path(self.cwd) / "requirements.txt").exists():
            return PythonProjectType.REQUIREMENTS
        return PythonProjectType.REQUIREMENTS
