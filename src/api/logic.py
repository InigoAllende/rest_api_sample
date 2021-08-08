import os
import sqlite3
from sqlite3 import Error

from src.api.models.requests import AddUserRequest

if os.environ.get('ENV') == 'testing':
    file = 'test_database.db'
else:
    file = 'database.db'

DB = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'db', file)


def create_connection():
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


def delete_user(user):
    with sqlite3.connect(DB) as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM users WHERE user_id=? AND password=? LIMIT 1", user.as_tuple)
        if not cur.rowcount:
            print('Failed to delete, user and password do not match')