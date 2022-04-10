import sqlite3
import os

from contextlib import contextmanager

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'db.sqlite')

@contextmanager
def conn_context(db_path):
  conn = sqlite3.connect(db_path)
  conn.row_factory = sqlite3.Row
  yield conn
  conn.close()

with conn_context(db_path) as conn:
  curs = conn.cursor()
  curs.execute("SELECT * FROM 'film_work';")
  data = curs.fetchall()
  print(dict(data[0]))
