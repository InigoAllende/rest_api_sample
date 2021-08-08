from flask import Flask, request

from src.api.models.requests import AddUserRequest
from src.api.logic import add_user_to_db
from src.api.db.db_logic import init_db, add_user_to_db, get_user_data

app = Flask(__name__)
init_db()


@app.route('/')
def healthcheck():
    return 'OK', 200


@app.route('/add_user', methods=['POST'])
def add_user():
    body = request.get_json(force=True)
    user = AddUserRequest(**body)
    add_user_to_db(user)
    return 'OK', 200


@app.route('/delete_user', methods=['POST'])
def delete_user():
    raise NotImplementedError


@app.route('/user/<username>', methods=['GET'])
def get_user(username):
    data = get_user_data(username)
    return data, 200