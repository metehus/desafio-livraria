from db import cursor, conn
from menus.menu_utils import find_book, do_backup


def menu_remove_book():
    do_backup()
    print("\n\n* Remover livro")
    search_name = input("Digite um título para pesquisar um livro: ")

    book = find_book(search_name)

    if book is not None:
        cursor.execute("""
                DELETE FROM livros WHERE titulo = ?
            """, (book['titulo'],))
        conn.commit()

        print("* Livro Removido com sucesso!")
