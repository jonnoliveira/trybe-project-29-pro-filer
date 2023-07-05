from pro_filer.actions.main_actions import find_duplicate_files  # NOQA
import pytest


def test_finder_duplicate_files_error(tmp_path):
    path_one = tmp_path / "apples"
    path_one.mkdir()

    py_one = path_one / "shinigamis.py"
    py_one.touch()

    # um arquivo não existe
    context = {"all_files": ["apples.py", str(py_one)]}

    with pytest.raises(ValueError):
        find_duplicate_files(context)


def test_finder_duplicate_files_equals(tmp_path):
    # cria arquivos temporarios
    path_one = tmp_path / "books"
    path_one.mkdir()

    path_two = tmp_path / "apples"
    path_two.mkdir()

    pdf_three = tmp_path / "smiles.pdf"
    pdf_three.touch()
    pdf_three.write_text("of death")  # <<<< diff: necessário possuir conteúdo

    py_one = path_one / "shinigamis.py"  # equal
    py_one.touch()

    py_two = path_two / "shinigamis.py"  # equal
    py_two.touch()

    context = {"all_files": [str(py_one), str(py_two), str(pdf_three)]}
    output = [(str(py_one), str(py_two))]

    data = find_duplicate_files(context)
    assert data == output
