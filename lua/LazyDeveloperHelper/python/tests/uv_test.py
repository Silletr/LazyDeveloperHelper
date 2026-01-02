from ..python_installers.uv_install import UvInstaller
from unittest.mock import MagicMock

installer = UvInstaller()


# ==== TEST IS uv INSTALLED ===
def test_uv_installed():
    test = installer.is_installed()
    if test:
        print("uv installed!")
        assert "uv is installed!"

    else:
        print("Install uv please!")
        raise AssertionError


# === TEST uv install WORKING ===
def test_uv_install():
    mock_install = MagicMock()
    mock_install.pkg = "requests"
    mock_install.result = ""
