import sys
from os.path import exists as file_exists


def txt_importer(path_file):
    if not file_exists(path_file):
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return None
    file_content = []
    with open(path_file, mode="r") as file:
        for row in file:
            file_content.append(row.strip())
    return file_content
