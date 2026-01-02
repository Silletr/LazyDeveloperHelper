from base_class import BaseInstaller


class UvInstaller(BaseInstaller):
    cmd = "uv"

    def get_command(self, package: str) -> list[str]:
        return [self.cmd, "install", package]

    def install(self, package):
        return self.run(package)
