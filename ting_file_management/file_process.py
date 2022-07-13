def process(path_file, instance):
    name = path_file
    file_content = []
    lines = 0
    with open(path_file, mode="r") as file:
        for row in file:
            file_content.append(row.strip())
            lines += 1
    output = {
        "nome_do_arquivo": name,
        "qtd_linhas": lines,
        "linhas_do_arquivo": file_content
    }
    print(output)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
