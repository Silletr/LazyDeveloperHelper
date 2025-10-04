import pytest
from unittest.mock import patch, MagicMock


@pytest.fixture
def mock_subprocess_run():
    with patch("subprocess.run") as m:
        yield m


@pytest.fixture
def mock_os_chdir():
    with patch("os.chdir") as m:
        yield m


@pytest.fixture
def mock_shutil_which():
    with patch("shutil.which") as m:
        yield m


@pytest.fixture
def mock_os_path_exists():
    with patch("os.path.exists") as m:
        yield m


@pytest.fixture
def mock_os_path_abspath():
    with patch("os.path.abspath") as m:
        yield m
