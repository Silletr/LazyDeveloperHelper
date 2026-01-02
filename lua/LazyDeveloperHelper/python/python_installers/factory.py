from pip_install import PipInstaller
from uv_install import UvInstaller
from poetry_install import PoetryInstaller

from project_context import PythonProjectType


def get_python_installer(kind: PythonProjectType):
    if kind == PythonProjectType.UV:
        return UvInstaller("uv")

    if kind == PythonProjectType.REQUIREMENTS:
        return PipInstaller("pip3")

    if kind == PythonProjectType.POETRY:
        return PoetryInstaller("poetry")
