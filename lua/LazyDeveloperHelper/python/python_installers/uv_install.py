from base_class import BaseInstaller
import subprocess


class UvInstaller(BaseInstaller):
    def __init__(self):
        super().__init__("uv")

    def get_command(self, package: str) -> list[str]:
        return ["uv", "pip", "install", package]
        # I will check ["uv", "add", package] later — and add ->
        # only if "uv add" supporting dependencies from pyproject.toml

    def install(self, package: str) -> subprocess.CompletedProcess:
        return self.run_install(package)


if __name__ == "__main__":
    installer = UvInstaller()
    if installer.is_installed():
        print("uv знайдено в PATH!")
        # Тест установки (обережно — реально встановить!)
        # result = installer.install("requests")
        # print(result.stdout)
        # print(result.stderr)
    else:
        print(
            "uv не встановлено.Встанови:curl -LsSf https://astral.sh/uv/install.sh | sh"
        )
