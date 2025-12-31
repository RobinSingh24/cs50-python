import project
import pyfiglet
from unittest.mock import patch


def test_get_category():
    assert project.get_category("hello.txt") == "Documents"
    assert project.get_category("Robin.png") == "Images"
    assert project.get_category("akon.mp3") == "Music"
    assert project.get_category("unknown.crx") == "Others"


@patch("project.os.makedirs")
@patch("project.shutil.move")
@patch("project.os.path.exists")
def test_move_file(mock_exists, mock_move, mock_makedirs):
    # Arrange
    mock_exists.return_value = False

    result = project.move_file("./downloads", "photo.png", "Images")

    mock_makedirs.assert_called_once_with("./downloads/Images")

    mock_move.assert_called_once_with(
        "./downloads/photo.png", "./downloads/Images/photo.png"
    )

    assert result is True


@patch("project.os.makedirs")
@patch("project.shutil.move")
@patch("project.os.path.exists")
def test_move_file_exists(mock_exists, mock_move, mock_makedirs):
    # Arrange
    mock_exists.return_value = True

    result = project.move_file("./downloads", "photo.png", "Images")

    mock_makedirs.assert_not_called()

    mock_move.assert_called_once_with(
        "./downloads/photo.png", "./downloads/Images/photo.png"
    )

    assert result is True


def test_welcome():
    assert project.welcome() == pyfiglet.figlet_format(
        "Downloads cleaner", font="small"
    )
