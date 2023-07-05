from pro_filer.actions.main_actions import show_details  # NOQA
from unittest.mock import Mock, patch
import pytest
import time
import datetime

date = "2023-06-13"
ts = time.mktime(datetime.datetime.strptime(date, "%Y-%m-%d").timetuple())


@pytest.mark.parametrize(
    "context, line_one, line_two, line_three, line_four, line_five",
    [
        (
            {
                "base_path": "/home/trybe/Downloads",
            },
            "File name: Downloads\n",
            "File size in bytes: 2356\n",
            "File type: directory\n",
            "File extension: [no extension]\n",
            f"Last modified date: {date}\n",
        ),
    ],
)
def test_show_details_dir(
    context, line_one, line_two, line_three, line_four, line_five, capsys
):
    mock_exists = Mock(return_value=True)
    mock_getsize = Mock(return_value=2356)
    mock_isdir = Mock(return_value=True)
    mock_splitext = Mock(return_value=("Downloads", ""))
    mock_getmtime = Mock(return_value=ts)
    with (
        patch("os.path.exists", mock_exists),
        patch("os.path.getsize", mock_getsize),
        patch("os.path.isdir", mock_isdir),
        patch("os.path.splitext", mock_splitext),
        patch("os.path.getmtime", mock_getmtime),
    ):
        show_details(context)

        captured = capsys.readouterr()
        assert line_one in captured.out
        assert line_two in captured.out
        assert line_three in captured.out
        assert line_four in captured.out
        assert line_five in captured.out


@pytest.mark.parametrize(
    "context, line_one, line_two, line_three, line_four, line_five",
    [
        (
            {
                "base_path": "/home/trybe/Downloads/Trybe_logo.png",
            },
            "File name: Trybe_logo.png\n",
            "File size in bytes: 698\n",
            "File type: file\n",
            "File extension: .png\n",
            f"Last modified date: {date}\n",
        ),
    ],
)
def test_show_details_file(
    capsys, context, line_one, line_two, line_three, line_four, line_five
):
    mock_exists = Mock(return_value=True)
    mock_getsize = Mock(return_value=698)
    mock_isdir = Mock(return_value=False)
    mock_splitext = Mock(return_value=("Trybe_logo", ".png"))
    mock_getmtime = Mock(return_value=ts)

    with (
        patch("os.path.exists", mock_exists),
        patch("os.path.getsize", mock_getsize),
        patch("os.path.isdir", mock_isdir),
        patch("os.path.splitext", mock_splitext),
        patch("os.path.getmtime", mock_getmtime),
    ):
        show_details(context)

        captured = capsys.readouterr()
        assert line_one in captured.out
        assert line_two in captured.out
        assert line_three in captured.out
        assert line_four in captured.out
        assert line_five in captured.out


def test_show_details_not_exist(capsys):
    mock_exists = Mock(return_value=False)

    with patch("os.path.exists", mock_exists):
        show_details({"base_path": "/home/trybe/????"})

        captured = capsys.readouterr()
        assert "File '????' does not exist" in captured.out
