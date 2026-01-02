# python_installers/factory.py
from lua.LazyDeveloperHelper.python.cargo_install import CargoInstaller
from .pip import PipInstaller
from .poetry_install import PoetryInstaller
from .uv_install import UvInstaller
import sys


print("Factory called with args:", sys.argv)


def get_installer(manager: str):
    managers = {
        "pip": PipInstaller(),
        "poetry": PoetryInstaller(),
        "uv": UvInstaller(),
        "cargo": CargoInstaller,
    }
    installer = managers.get(manager.lower())
    if not installer:
        raise ValueError(f"Unsupported manager: {manager}")
    return installer
