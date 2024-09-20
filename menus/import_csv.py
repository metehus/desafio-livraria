from pathlib import Path

import pandas

from db import cursor, conn
from menus.menu_utils import do_backup


def menu_import_csv():
    do_backup()
    print("* Importar csv")

    while True:
        file_path = input("Digite o caminho do arquivo csv para importar: ")
        path = Path(file_path)
        if not path.exists():
            print("\n [!] Arquivo não encontrado!")
            continue
        elif path.is_dir():
            print("\n [!] Selecione um arquivo para importar!")
            continue

        df = pandas.read_csv(path)

        cursor.execute("DELETE FROM livros")

        to_insert = []
        for row in df.itertuples():
            to_insert.append((
                row.id,
                row.titulo,
                row.autor,
                row.ano_publicacao,
                row.preco
            ))

        cursor.executemany("""
            INSERT INTO livros (id, titulo, autor, ano_publicacao, preco) 
            VALUES (?, ?, ?, ?, ?)
        """, to_insert)

        conn.commit()

        print("\n\n * Arquivo importado!")
        break
