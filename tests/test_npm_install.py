from unittest.mock import MagicMock
import subprocess
from python.npm_install import install_npm


def test_install_npm_already_installed(mock_subprocess_run, capsys):
    mock_subprocess_run.return_value = MagicMock(
        returncode=0, stdout="express@4.17.1", stderr=""
    )
    install_npm("express")
    captured = capsys.readouterr()
    assert "Installing npm package: express ..." not in captured.out
    assert "express already installed" not in captured.out


def test_install_npm_success(mock_subprocess_run, capsys):
    mock_subprocess_run.side_effect = [
        MagicMock(returncode=1, stdout="", stderr=""),  # npm list fails (not installed)
        MagicMock(
            returncode=0, stdout="express@4.17.1 installed", stderr=""
        ),  # npm install succeeds
    ]
    install_npm("express")
    captured = capsys.readouterr()
    assert "Installing npm package: express ..." not in captured.out
    assert "express installed successfully" not in captured.ou

def test_install_npm_failure(mock_subprocess_run, capsys):
    mock_subprocess_run.side_effect = [
        MagicMock(returncode=1, stdout="", stderr=""),  # npm list fails
        subprocess.CalledProcessError(
            returncode=1,
            cmd=["npm", "install", "express", "--no-save"],
            output="",
            stderr="Error: not found",
        ),
    ]
    install_npm("express")
    captured = capsys.readouterr()
    assert "Failed to install express" not in captured.out
    assert "stderr:\nError: not found" not in captured.out
