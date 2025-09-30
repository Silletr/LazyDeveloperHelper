from unittest.mock import MagicMock
from ..python.cargo_install import (
    find_cargo_toml,
    check_cargo_installed,
    cargo_install,
    validate_library_name,
)
import subprocess


def test_find_cargo_toml_exists(tmp_path, mock_os_path_exists, mock_os_path_abspath):
    (tmp_path / "Cargo.toml").touch()
    result = find_cargo_toml(str(tmp_path))
    if result != str(tmp_path / "Cargo.toml"):
        raise AssertionError


def test_find_cargo_toml_not_found(mock_os_path_exists):
    result = find_cargo_toml()
    assert result is None


def test_validate_library_name_valid():
    if validate_library_name("serde") is not True:
        raise AssertionError


def test_validate_library_name_invalid(capsys):
    if validate_library_name("serde;malicious") is not False:
        raise AssertionError
    captured = capsys.readouterr()
    if "Invalid library name: serde;malicious" not in captured.out:
        raise AssertionError


def test_check_cargo_installed(mock_shutil_which, capsys):
    mock_shutil_which.return_value = "/usr/bin/cargo"
    if check_cargo_installed() is not True:
        raise AssertionError

    mock_shutil_which.return_value = None
    if check_cargo_installed() is not False:
        raise AssertionError
    captured = capsys.readouterr()
    if "cargo is not installed or not found in PATH" not in captured.out:
        raise AssertionError


def test_cargo_install_success(
    tmp_path,
    mock_subprocess_run,
    mock_os_path_exists,
    mock_os_path_abspath,
    mock_os_getcwd,
    mock_os_chdir,
    capsys,
):
    (tmp_path / "Cargo.toml").touch()
    mock_subprocess_run.return_value = MagicMock(
        returncode=0, stdout="Added serde", stderr=""
    )
    cargo_install(["serde"])
    captured = capsys.readouterr()
    if "Running cargo add serde ..." not in captured.out:
        raise AssertionError
    if "Cargo output:\nAdded serde" not in captured.out:
        raise AssertionError
    mock_os_chdir.assert_called()


def test_cargo_install_failure(
    tmp_path,
    mock_subprocess_run,
    mock_os_path_exists,
    mock_os_path_abspath,
    mock_os_getcwd,
    mock_os_chdir,
    capsys,
):
    (tmp_path / "Cargo.toml").touch()
    mock_subprocess_run.side_effect = subprocess.CalledProcessError(
        returncode=1,
        cmd=["cargo", "add", "serde"],
        stdout="",
        stderr="Error: invalid crate",
    )
    cargo_install(["serde"])
    captured = capsys.readouterr()
    if "Failed to install serde" not in captured.out:
        raise AssertionError
    if "stderr:\nError: invalid crate" not in captured.out:
        raise AssertionError
