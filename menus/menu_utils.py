from datetime import datetime

from db import cursor
import pandas as pd
from pathlib import Path


def find_book(name):
    cursor.execute("SELECT * FROM livros WHERE titulo = ?", (name,))
    result = cursor.fetchone()

    if result is not None:
        return {
            'id': result[0],
            'titulo': result[1],
            'autor': result[2],
            'ano_publicacao': result[3],
            'preco': result[4],
        }
    else:
        print("[!] Livro não encontrado!")
        return None

def export_all_to_csv(folder, file_name):
    cursor.execute("SELECT * FROM livros")
    result = cursor.fetchall()
    items = []
    for row in result:
        items.append({
            'id': row[0],
            'titulo': row[1],
            'autor': row[2],
            'ano_publicacao': row[3],
            'preco': row[4]
        })

    df = pd.DataFrame(items)

    df.to_csv(f"{folder}/{file_name}", index=False)

def do_backup():
    path = Path("backups")
    if not path.exists():
        path.mkdir()

    # save
    now_str = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    file_name = f"backup_livraria_{now_str}.csv"
    export_all_to_csv(path, file_name)

    files = list(path.glob("*"))
    files.sort(key=lambda x: x.stat().st_mtime)

    for file in files[:-5]:
        file.unlink()
