import os
import sqlite3
from sqlite3 import Error

from src.api.models.requests import AddUserRequest

cur_path = os.path.dirname(os.path.realpath(__file__))
if os.environ.get('ENV') == 'testing':
    DB = os.path.join(cur_path, 'test_database.db')
else:
    DB = os.path.join(cur_path, 'database.db')


def _create_connection():
    conn = sqlite3.connect(DB)
    return conn


def _create_table(create_table_sql):
    with sqlite3.connect(DB) as conn:
        c = conn.cursor()
        c.execute(create_table_sql)


def init_db():
    user_table = ''' CREATE TABLE IF NOT EXISTS users (
                        user_id text PRIMARY KEY NOT NULL,
                        email text NOT NULL,
                        password text NOT NULL,
                        data text); '''
    
    _create_table(user_table)


def add_user_to_db(user: AddUserRequest):
    sql = ''' INSERT INTO users(user_id,email,password,data)
              VALUES(?,?,?,?) '''
    with sqlite3.connect(DB) as conn:
        cur = conn.cursor()
        cur.execute(sql, user.as_tuple)



def get_user_data(user_id):
    with sqlite3.connect(DB) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE user_id=? LIMIT 1", (user_id,))

        row = cur.fetchone()

    return row