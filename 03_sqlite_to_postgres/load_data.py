import os
import sqlite3
from contextlib import contextmanager
from pathlib import Path

import psycopg2
from dotenv import load_dotenv
from psycopg2.extensions import connection as _connection
from psycopg2.extras import DictCursor

from dataclasses_models import (  # isort:skip
    Genre,
    GenreFilmwork,
    Filmwork,
    Person,
    PersonFilmWork,
)
from postgres_saver import PostgresSaver  # isort:skip
from sqlite_loader import SQLiteLoader  # isort:skip


dataclass_dict = {
    'film_work': Filmwork,
    'genre': Genre,
    'genre_film_work': GenreFilmwork,
    'person': Person,
    'person_film_work': PersonFilmWork,
}


def load_from_sqlite(
    connection: sqlite3.Connection,
    pg_conn: _connection,
    size: 100,
):
    postgres_saver = PostgresSaver(pg_conn)
    sqlite_loader = SQLiteLoader(connection)

    for table in dataclass_dict.keys():
        loader = sqlite_loader.load_data(table, dataclass_dict, size)
        for loaded_data in loader:
            postgres_saver.save_data(loaded_data, dataclass_dict, size)


@contextmanager
def conn_context(db_path: str):
    conn = sqlite3.connect(db_path)
    try:
        yield conn.cursor()
    finally:
        conn.close()


if __name__ == '__main__':
    SIZE = 500
    ENV_PATH = Path(__file__).resolve().parent.parent.joinpath('env', '.env')
    load_dotenv(dotenv_path=ENV_PATH)

    SQLITE_PATH = os.getenv('SQLITE_PATH', default=None)
    dsl = {
        'dbname': os.getenv('POSTGRES_DB', None),
        'user': os.getenv('POSTGRES_USER', None),
        'password': os.getenv('POSTGRES_PASSWORD', None),
        'host': os.getenv('DB_HOST', None),
        'port': os.getenv('DB_PORT', '5432'),
    }

    with conn_context(SQLITE_PATH) as sqlite_conn:
        with psycopg2.connect(**dsl, cursor_factory=DictCursor) as pg_conn:
            load_from_sqlite(sqlite_conn, pg_conn, SIZE)
