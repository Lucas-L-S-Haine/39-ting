import sys


def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index) == path_file:
            return None
    instance.enqueue(path_file)
    file_content = []
    lines = 0
    with open(path_file, mode="r") as file:
        for row in file:
            file_content.append(row.strip())
            lines += 1
    output = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": lines,
        "linhas_do_arquivo": file_content
    }
    print(output)


def remove(instance):
    try:
        file = instance.dequeue()
        message = f"Arquivo {file} removido com sucesso"
    except IndexError:
        message = "Não há elementos"
    print(message)


def file_metadata(instance, position):
    try:
        file_name = instance.search(position)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
        return None
    file_content = []
    lines = 0
    with open(file_name, mode="r") as file:
        for row in file:
            file_content.append(row.strip())
            lines += 1
    file_metadata = {
        "nome_do_arquivo": file_name,
        "qtd_linhas": lines,
        "linhas_do_arquivo": file_content
    }
    print(file_metadata)
