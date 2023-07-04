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
    for line1, line2, line3 in captured.out.splitlines():
        assert line1 == call[1]
        assert line2 == call[2]
        assert line3 == call[3]


def test_show_preview_empty(capsys):
    show_preview({"all_files": [], "all_dirs": []})
    captured = capsys.readouterr()
    assert captured.out == "Found 0 files and 0 directories\n"
