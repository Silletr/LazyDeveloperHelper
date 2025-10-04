from unittest.mock import MagicMock
import subprocess
from python.pip_install import install_lib

def test_install_lib_already_installed(tmp_path, mock_subprocess_run, capsys):
    req_file = tmp_path / "requirements.txt"
    req_file.write_text("requests\n")

    mock_subprocess_run.return_value = MagicMock(
        returncode=0,
        stdout="Requirement already satisfied: requests",
        stderr=""
    )

    install_lib("requests")

    captured = capsys.readouterr()
    assert "Installing requests ..." in captured.out
    assert "requests already installed" in captured.out

    install_lib("requests")

    captured = capsys.readouterr()
    assert "📦 Installing requests ..." in captured.out
    assert "✅ requests successfully installed" in captured.out or "already installed" in captured.out
    assert req_file.read_text() == "requests\n"

def test_install_lib_failure(tmp_path, mock_subprocess_run, capsys):
    req_file = tmp_path / "requirements.txt"
    req_file.touch()
    mock_subprocess_run.side_effect = subprocess.CalledProcessError(
        returncode=1,
        cmd=["pip", "install", "requests"],
        output="",
        stderr="Error: not found",
    )
    install_lib("requests")
    captured = capsys.readouterr()
    assert "❌ Failed to install requests" in captured.out
    assert "📍 stderr:\nError: not found" in captured.out
    assert req_file.read_text() == "requests\n"


def test_install_lib_create_requirements(tmp_path, mock_subprocess_run):
    mock_subprocess_run.return_value = MagicMock(
        returncode=0, stdout="Successfully installed requests-2.28.1", stderr=""
    )
    install_lib("requests")
    req_file = tmp_path / "requirements.txt"
    assert req_file.exists()
    assert req_file.read_text() == "requests\n"
