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
    pass
