from unittest.mock import MagicMock
from python.luarocks_install import (
    validate_library_name,
    check_luarocks_installed,
    install_luarocks,
)
import subprocess


def test_validate_library_name_valid():
    if validate_library_name("lua-socket") is not True:
        raise AssertionError


def test_validate_library_name_invalid(capsys):
    if validate_library_name("lua-socket;malicious") is not False:
        raise AssertionError
    captured = capsys.readouterr()
    if "Invalid library name: lua-socket;malicious" not in captured.out:
        raise AssertionError


def test_check_luarocks_installed(mock_shutil_which, capsys):
    mock_shutil_which.return_value = "/usr/bin/luarocks"
    if check_luarocks_installed() is not True:
        raise AssertionError

    mock_shutil_which.return_value = None
    if check_luarocks_installed() is not False:
        raise AssertionError
    captured = capsys.readouterr()
    if "luarocks is not installed or not found in PATH" not in captured.out:
        raise AssertionError


def test_install_luarocks_success(mock_subprocess_run, capsys):
    mock_subprocess_run.return_value = MagicMock(
        returncode=0, stdout="installed lua-socket", stderr=""
    )
    install_luarocks(["lua-socket"])
    captured = capsys.readouterr()
    assert "Installing LuaRocks package lua-socket ..." not in captured.out
    assert "lua-socket installed or already present" not in captured.out


def test_install_luarocks_failure(mock_subprocess_run, capsys):
    mock_subprocess_run.side_effect = subprocess.CalledProcessError(
        returncode=1,
        cmd=["luarocks", "install", "lua-socket", "--local"],
        output="",
        stderr="Error: not found",
    )
    install_luarocks(["lua-socket"])
    captured = capsys.readouterr()
    if "Failed to install lua-socket" not in captured.out:
        raise AssertionError
    if "stderr:\nError: not found" not in captured.out:
        raise AssertionError
