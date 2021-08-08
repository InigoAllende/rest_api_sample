import os
import sqlite3
from sqlite3 import Error

from src.api.models.requests import AddUserRequest

DB = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'database.db')


def _create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn


def _create_table(conn, create_table_sql):
    c = conn.cursor()
    c.execute(create_table_sql)



def init_db():
    user_table = ''' CREATE TABLE IF NOT EXISTS users (
                        user_id text PRIMARY KEY NOT NULL,
                        email text NOT NULL,
                        password text NOT NULL,
                        data text); '''
    
    # create a database connection
    conn = _create_connection(DB)

    # create tables
    if conn is not None:
        _create_table(conn, user_table)


def add_user_to_db(user: AddUserRequest):
    conn = _create_connection(DB)

    sql = ''' INSERT INTO users(user_id,email,password,data)
              VALUES(?,?,?,?) '''

    cur = conn.cursor()
    cur.execute(sql, user.as_tuple)
    conn.commit()


def get_user_data(user_id):
    conn = _create_connection(DB)
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE user_id=? LIMIT 1", (user_id,))

    row = cur.fetchone()

    return row