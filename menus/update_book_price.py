from db import cursor, conn
from menus.menu_utils import find_book, do_backup


def menu_update_book():
    do_backup()
    print("\n\n* Atualizar preço de livro")
    search_name = input("Digite um título para pesquisar um livro: ")

    book = find_book(search_name)

    if book is not None:
        print(f"Livro {book['titulo']} encontrado com preço {book['preco']}\n")
        price = float(input("Digite o novo preço do livro: "))

        cursor.execute("""
            UPDATE livros SET preco = ? WHERE titulo = ?
        """, (price, book['titulo']))
        conn.commit()

        print("* Livro atualizado com sucesso!")
