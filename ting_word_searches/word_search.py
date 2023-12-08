def exists_word(word, instance):
    exist = []

    for i in range(0, len(instance)):
        file = instance.search(i)
        data = {
            'palavra': word,
            'arquivo': file['nome_do_arquivo'],
            'ocorrencias': list()
        }

        for line, content in enumerate(file['linhas_do_arquivo']):
            if word.casefold() in content.casefold():
                data['ocorrencias'].append({'linha': line + 1})

        if len(data['ocorrencias']) > 0:
            exist.append(data)

    return exist


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
