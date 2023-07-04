from pro_filer.actions.main_actions import show_preview  # NOQA
import pytest

call = [
    {"all_files": ["file"], "all_dirs": []},
    [
        "Found 1 files and 0 directories\n",
        "First 5 files: ['file']\n",
        "First 5 directories: []\n",
    ],
]

call_empty = [
    {"all_files": [], "all_dirs": []},
    "Found 0 files and 0 directories\n",
]


@pytest.mark.parametrize(
    "context, expected_output",
    [
        (call[0], call[1]),
    ],
)
def test_show_preview(context, expected_output, capsys):
    show_preview(context)
    captured = capsys.readouterr()
    assert (
        captured.out
        == expected_output[0] + expected_output[1] + expected_output[2]
    )


def test_show_preview_empty(call_empty, capsys):
    show_preview(call_empty[0])
    captured = capsys.readouterr()
    assert captured.out == call_empty[1]
