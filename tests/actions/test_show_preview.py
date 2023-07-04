from pro_filer.actions.main_actions import show_preview  # NOQA
import pytest

call_one = [
    {"all_files": [], "all_dirs": []},
    "Found 0 files and 0 directories",
]


@pytest.mark.parametrize(
    "context, expected_output",
    [
        (call_one[0], call_one[1]),
    ],
)
def test_show_preview(context, expected_output, capsys):
    show_preview(context)
    captured = capsys.readouterr()
    assert captured.out == expected_output
