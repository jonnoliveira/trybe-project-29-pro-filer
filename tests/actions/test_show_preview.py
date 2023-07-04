from pro_filer.actions.main_actions import show_preview  # NOQA
import pytest

call = [
    {"all_files": ["file"], "all_dirs": []},
    "Found 1 files and 0 directories\n",
    "First 5 files: ['file']\n",
    "First 5 directories: []\n",
]


@pytest.mark.parametrize(
    "context, expected_line_1, expected_line_3, expected_line_3",
    [
        (call[0], call[1], call[2], call[3]),
    ],
)
def test_show_preview(
    context, expected_line_1, expected_line_2, expected_line_3, capsys
):
    show_preview(context)
    captured = capsys.readouterr()
    for line1, line2, line3 in captured.out.splitlines():
        assert line1 == expected_line_1
        assert line2 == expected_line_2
        assert line3 == expected_line_3


def test_show_preview_empty(capsys):
    show_preview({"all_files": [], "all_dirs": []})
    captured = capsys.readouterr()
    assert captured.out == "Found 0 files and 0 directories\n"
