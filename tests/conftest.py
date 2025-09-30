import pytest
from unittest.mock import patch, MagicMock


@pytest.fixture
def mock_subprocess_run():
    with patch("subprocess.run") as mock_run:
        yield mock_run


@pytest.fixture
def mock_os_path_exists(tmp_path):
    def _exists(path):
        return (tmp_path / path).exists()

    with patch("os.path.exists", side_effect=_exists) as mock_exists:
        yield mock_exists


@pytest.fixture
def mock_os_path_abspath(tmp_path):
    def _abspath(path):
        return str(tmp_path / path)

    with patch("os.path.abspath", side_effect=_abspath) as mock_abspath:
        yield mock_abspath


@pytest.fixture
def mock_os_getcwd(tmp_path):
    with patch("os.getcwd", return_value=str(tmp_path)) as mock_getcwd:
        yield mock_getcwd


@pytest.fixture
def mock_os_chdir():
    with patch("os.chdir") as mock_chdir:
        yield mock_chdir


@pytest.fixture
def mock_shutil_which():
    with patch("shutil.which") as mock_which:
        yield mock_which
