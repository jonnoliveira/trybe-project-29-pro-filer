"""Arquivo que estudantes devem editar"""
import os


def show_deepest_file(context):
    if not context["all_files"]:
        print("No files found")
    else:
        """A função 'lambda' é uma função anônima como as arrow
        functions em JS. Nesse caso ela recebe um caminho da
        lista de arquivos e retorna o tamanho da lista de diretórios que
        compõem o caminho. O 'max' vai retornar o caminho que tiver
        o maior tamanho."""
        deepest_file = max(
            context["all_files"], key=lambda path: len(os.path.split(path))
        )
        print(f"Deepest file: {deepest_file}")


def find_file_by_name(context, search_term, case_sensitive=True):
    if not search_term:
        return []

    found_files = []

    for path in context["all_files"]:
        file_name = path.split("/")[-1]

        if not case_sensitive:
            file_name.lower()
            search_term.lower()

        if search_term in file_name:
            found_files.append(path)

    return found_files
