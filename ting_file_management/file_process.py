def process(path_file, instance):
    name = path_file
    file_content = []
    with open(path_file, mode="r") as file:
        for row in file:
            instance.enqueue(row)
    for index in range(len(instance)):
        file_content.append(instance.search(index).strip())
    output = {
        "nome_do_arquivo": name,
        "qtd_linhas": len(file_content),
        "linhas_do_arquivo": file_content
    }
    print(output)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
