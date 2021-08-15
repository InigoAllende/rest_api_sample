import json

from flask import Flask, request
from src.api.logic import add_user_to_db, get_user_data, init_db, delete_user
from src.api.models.requests import AddUserRequest, DeleteUserRequest
from pydantic import ValidationError

app = Flask(__name__)
init_db()


@app.errorhandler(ValidationError)
def handle_exception(error):
    """Return JSON instead of HTML for HTTP errors."""
    return error.json(), 422


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
def delete_user_data():
    body = request.get_json(force=True)
    user = DeleteUserRequest(**body)
    delete_user(user)
    return 'OK', 200


@app.route('/user/<username>', methods=['GET'])
def get_user(username):
    data = get_user_data(username)
    if data:
        response = {'user_id': data[0], 'email': data[1], 'password': data[2], 'data': json.loads(data[3])}
        return response, 200
    return {}, 200
