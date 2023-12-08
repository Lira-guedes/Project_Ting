from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file = False

    for file in instance.data:
        if file["nome_do_arquivo"] == path_file:
            file = True
            break

    if not file:
        lines = txt_importer(path_file)
        dict_file = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(lines),
            "linhas_do_arquivo": lines,
        }
        instance.enqueue(dict_file)
        print(dict_file)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
