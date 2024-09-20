from db import cursor


def menu_list_by_author():
    print("\n\n* Buscar livros por autor")
    search_name = input("Digite o autor do livro para buscar: ")

    cursor.execute("SELECT * FROM livros WHERE autor = ?", (search_name,))
    results = cursor.fetchall()

    print("ID | Titulo | Autor | Ano de publicação | Preço")
    for row in results:
        print(f"{row[0]}. {row[1]} | {row[2]} | {row[3]} | {row[4]}")
