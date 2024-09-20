from db import sync_db
from menus.add_book import menu_add_book
from menus.export_csv import menu_export_csv
from menus.import_csv import menu_import_csv
from menus.list_books import menu_list_books
from menus.list_by_author import menu_list_by_author
from menus.menu_utils import do_backup
from menus.remove_book import menu_remove_book
from menus.update_book_price import menu_update_book

def menu_backup():
    do_backup()
    print("* Backupo feito!")

def menu_exit():
    exit()

menus = [
    (1, menu_add_book),
    (2, menu_list_books),
    (3, menu_update_book),
    (4, menu_remove_book),
    (5, menu_list_by_author),
    (6, menu_export_csv),
    (7, menu_import_csv),
    (8, menu_backup),
    (9, menu_exit)
]

def main_menu():
    sync_db()
    print("* Sistema livrinho *")
    print("1. Adicionar novo livro")
    print("2. Exibir todos os livros")
    print("3. Atualizar preço de um livro")
    print("4. Remover um livro")
    print("5. Buscar livros por autor")
    print("6. Exportar dados para CSV")
    print("7. Importar dados de CSV")
    print("8. Fazer backup do banco de dados")
    print("9. Sair")
    print("")

    option = int(input("Digite a opção desejada: "))

    for menu_option in menus:
        if option == menu_option[0]:
            menu_option[1]()
            print("\n\n")

            return main_menu()
    print("[!] Digite uma opção válida (1-9)\n")
    main_menu()

main_menu()