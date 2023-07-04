from pro_filer.actions.main_actions import show_preview  # NOQA
import pytest


# call = [
#     {"all_files": ["file"], "all_dirs": []},
#     "Found 1 files and 0 directories",
#     "First 5 files: ['file']",
#     "First 5 directories: []",
# ]


@pytest.mark.parametrize(
    "context, line_one, line_two, line_three",
    [
        (
            {
                "all_files": ["file1", "file2"],
                "all_dirs": [],
            },
            "Found 2 files and 0 directories",
            "First 5 files: ['file1', 'file2']",
            "First 5 directories: []",
        ),
        (
            {
                "all_files": [],
                "all_dirs": ["dir1", "dir2"],
            },
            "Found 0 files and 2 directories",
            "First 5 files: []",
            "First 5 directories: ['dir1', 'dir2']",
        ),
        (
            {
                "all_files": [
                    "file1",
                    "file2",
                    "file3",
                    "file4",
                    "file5",
                    "file6",
                ],
                "all_dirs": ["dir1", "dir2", "dir3", "dir4", "dir5", "dir6"],
            },
            "Found 6 files and 6 directories",
            "First 5 files: ['file1', 'file2', 'file3', 'file4', 'file5']",
            "First 5 directories: ['dir1', 'dir2', 'dir3', 'dir4', 'dir5']",
        ),
    ],
)
def test_show_preview(capsys, context, line_one, line_two, line_three):
    show_preview(context)
    captured = capsys.readouterr()
    assert line_one in captured.out
    assert line_two in captured.out
    assert line_three in captured.out


def test_show_preview_empty(capsys):
    show_preview({"all_files": [], "all_dirs": []})
    captured = capsys.readouterr()
    assert captured.out == "Found 0 files and 0 directories\n"
