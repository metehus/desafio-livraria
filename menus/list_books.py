from db import cursor

def menu_list_books():
    print("\n\n* Listar livros")
    cursor.execute("SELECT * FROM livros")
    results = cursor.fetchall()

    print("ID | Titulo | Autor | Ano de publicação | Preço")
    for row in results:
        print(f"{row[0]}. {row[1]} | {row[2]} | {row[3]} | {row[4]}")
