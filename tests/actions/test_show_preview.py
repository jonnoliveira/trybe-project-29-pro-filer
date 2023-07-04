from pro_filer.actions.main_actions import show_preview  # NOQA

call = [
    {"all_files": ["file"], "all_dirs": []},
    "Found 1 files and 0 directories\n",
    "First 5 files: ['file']\n",
    "First 5 directories: []\n",
]


def test_show_preview(capsys):
    show_preview(call[0])  # <<<<<<<< passar o dicionário como argumento
    captured = capsys.readouterr()
    assert call[1] in captured.out
    assert call[2] in captured.out
    assert call[3] in captured.out


def test_show_preview_empty(capsys):
    show_preview({"all_files": [], "all_dirs": []})
    captured = capsys.readouterr()
    assert captured.out == "Found 0 files and 0 directories\n"
