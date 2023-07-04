from pro_filer.actions.main_actions import show_preview  # NOQA
import pytest


# call = [
#     {"all_files": ["file"], "all_dirs": []},
#     "Found 1 files and 0 directories",
#     "First 5 files: ['file']",
#     "First 5 directories: []",
# ]


@pytest.mark.parametrize(
    "context",
    "line_one",
    "line_two",
    "line_three",
    [
        (
            {"all_files": ["file"], "all_dirs": []},
            "Found 1 files and 0 directories",
            "First 5 files: ['file']",
            "First 5 directories: []",
        ),
    ],
)
def test_show_preview(context, line_one, line_two, line_three, capsys):
    show_preview(context)  # <<<<<<<< passar o dicionário como argumento
    captured = capsys.readouterr()
    assert line_one in captured.out
    assert line_two in captured.out
    assert line_three in captured.out


def test_show_preview_empty(capsys):
    show_preview({"all_files": [], "all_dirs": []})
    captured = capsys.readouterr()
    assert captured.out == "Found 0 files and 0 directories\n"
