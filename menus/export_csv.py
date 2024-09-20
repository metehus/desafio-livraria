from menus.menu_utils import export_all_to_csv
from pathlib import Path


def menu_export_csv():
    print("* Exportação csv")

    path = Path("exports")
    if not path.exists():
        path.mkdir()

    export_all_to_csv("exports", "livros_exportados.csv")

    print("\n Exportado com sucesso para exports/livros_exportados.csv!")
