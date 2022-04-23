import pprint
import sqlite3
from contextlib import contextmanager
from pathlib import Path


@contextmanager
def conn_context(db_path: str):
    """Менеджер контекста.

    Args:
        db_path (str): Путь к базе данных

    Yields:
        str: Генерирует соединения с бд
    """
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    yield conn
    conn.close()


if __name__ == '__main__':
    db_path = Path(__file__).resolve().parent.joinpath('db.sqlite')
    with conn_context(db_path) as conn:
        curs = conn.cursor()
        curs.execute('SELECT * FROM film_work;')
        films = curs.fetchall()
        pprint.pprint(dict(films[0]))
