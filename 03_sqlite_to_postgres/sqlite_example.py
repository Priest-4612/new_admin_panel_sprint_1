"""Тестовый модуль."""
import os
import pprint
import sqlite3
from contextlib import contextmanager

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'db.sqlite')


@contextmanager
def conn_context(path):
    """Пример функции из теории.

    Args:
        path (str): путь к базе данных
    """
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    yield conn
    conn.close()


if __name__ == '__main__':
    with conn_context(db_path) as conn:
        curs = conn.cursor()
        curs.execute("SELECT * FROM 'film_work';")
        films = curs.fetchall()
        pprint.pprint(dict(films[0]))
