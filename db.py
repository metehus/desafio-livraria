import sqlite3
from pathlib import Path

path = Path("data")
if not path.exists():
    path.mkdir()


conn = sqlite3.connect('data/banco.db')
cursor = conn.cursor()

def sync_db():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            ano_publicacao INTEGER NOT NULL,
            preco REAL NOT NULL
        );
    """)
    conn.commit()