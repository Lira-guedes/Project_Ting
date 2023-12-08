from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    file = False

    for file in instance.data:
        if file["nome_do_arquivo"] == path_file:
            file = True

    if not file:
        lines = txt_importer(path_file)
        dict_file = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(lines),
            "linhas_do_arquivo": lines,
        }
        instance.enqueue(dict_file)
        return print(dict_file)


def remove(instance):
    try:
        r = instance.dequeue()
        print(f"Arquivo {r['nome_do_arquivo']} removido com sucesso")
    except IndexError:
        print("Não há elementos", file=sys.stdout)


def file_metadata(instance, position):
    try:
        print(instance.search(position), file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
