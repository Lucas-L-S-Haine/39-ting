def exists_word(word, instance):
    files = []
    for index in range(len(instance)):
        file_name = instance.search(index)
        ocurrences = []
        line_number = 0
        with open(file_name, mode="r") as file:
            for row in file:
                line_number += 1
                if word in row.lower():
                    ocurrences.append({"linha": line_number})
        if len(ocurrences) > 0:
            files.append({
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": ocurrences
            })
    return files


def search_by_word(word, instance):
    search = exists_word(word, instance)
    for index in range(len(search)):
        file_name = search[index]["arquivo"]
        lines = [item["linha"] for item in search[index]["ocorrencias"]]
        ocurrences = []
        with open(file_name, mode="r") as file:
            content = file.read().split("\n")
        for line_number in lines:
            ocurrences.append({
                "linha": line_number,
                "conteudo": content[line_number - 1]
            })
        search[index]["ocorrencias"] = ocurrences
    return search
