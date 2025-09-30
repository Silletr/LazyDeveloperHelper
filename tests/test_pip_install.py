from unittest.mock import MagicMock
import subprocess
from ..python.pip_install import install_lib


def test_install_lib_already_installed(tmp_path, mock_subprocess_run, capsys):
    req_file = tmp_path / "requirements.txt"
    req_file.write_text("requests\n")
    mock_subprocess_run.return_value = MagicMock(
        returncode=0, stdout="Requirement already satisfied: requests", stderr=""
    )
    install_lib("requests")
    captured = capsys.readouterr()
    if "Installing requests ..." not in captured.out:
        raise AssertionError
    if "requests already installed" not in captured.out:
        raise AssertionError


def test_install_lib_success(tmp_path, mock_subprocess_run, capsys):
    req_file = tmp_path / "requirements.txt"
    req_file.touch()
    mock_subprocess_run.return_value = MagicMock(
        returncode=0, stdout="Successfully installed requests-2.28.1", stderr=""
    )
    install_lib("requests")
    captured = capsys.readouterr()
    if "Installing requests ..." not in captured.out:
        raise AssertionError
    if "requests successfully installed" not in captured.out:
        raise AssertionError
    if req_file.read_text() != "requests\n":
        raise AssertionError


def test_install_lib_failure(tmp_path, mock_subprocess_run, capsys):
    req_file = tmp_path / "requirements.txt"
    req_file.touch()
    mock_subprocess_run.side_effect = subprocess.CalledProcessError(
        returncode=1,
        cmd=["pip", "install", "requests"],
        stdout="",
        stderr="Error: not found",
    )
    install_lib("requests")
    captured = capsys.readouterr()
    if "Failed to install requests" not in captured.out:
        raise AssertionError
    if "stderr:\nError: not found" not in captured.out:
        raise AssertionError
    if req_file.read_text() != "requests\n":
        raise AssertionError


def test_install_lib_create_requirements(tmp_path, mock_subprocess_run, capsys):
    mock_subprocess_run.return_value = MagicMock(
        returncode=0, stdout="Successfully installed requests-2.28.1", stderr=""
    )
    install_lib("requests")
    req_file = tmp_path / "requirements.txt"
    if not req_file.exists():
        raise AssertionError
    if req_file.read_text() != "requests\n":
        raise AssertionError
