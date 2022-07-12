import sys
from os.path import exists as file_exists


def is_txt(path_file):
    try:
        file_extension = path_file.split(".")[1]
    except IndexError:
        file_extension = ""
    return file_extension == "txt"


def txt_importer(path_file):
    if not file_exists(path_file):
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return None
    if not is_txt(path_file):
        print("Formato inválido", file=sys.stderr)
        return None
    file_content = []
    with open(path_file, mode="r") as file:
        for row in file:
            file_content.append(row.strip())
    return file_content
