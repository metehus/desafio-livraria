from db import cursor, conn
from menus.menu_utils import do_backup


def menu_add_book():
    do_backup()
    print("\n\n* Adicionar livro")
    try:
        titulo = input("Digite o título: ")
        autor = input("Digite o autor: ")
        ano = int(input("Digite o ano: "))
        preco = float(input("Digite o preço: "))

        cursor.execute("""
            INSERT INTO livros (titulo, autor, ano_publicacao, preco)
            VALUES (?, ?, ?, ?)
        """, (titulo, autor, ano, preco))
        conn.commit()

        print("* Livro adicionado com sucesso!")
    except ValueError:
        print("[!] Valor inválido!")
        menu_add_book()