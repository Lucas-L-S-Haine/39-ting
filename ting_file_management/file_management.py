from sys import stderr
from subprocess import check_output, CalledProcessError


def file_exists(path_file):
    command = f"ls {path_file} &> /dev/null"
    try:
        check_output(command, shell=True)
        return True
    except CalledProcessError:
        return False


def txt_importer(path_file):
    if not file_exists(path_file):
        stderr.write(f"Arquivo {path_file} não encontrado")
        return None
    file_content = []
    with open(path_file, mode="r") as file:
        for row in file:
            file_content.append(row.strip())
    return file_content
