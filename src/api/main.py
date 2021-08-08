from flask import Flask, request

from src.api.models.requests import AddUserRequest
from src.api.logic import add_user_to_db

app = Flask(__name__)


@app.route('/')
def healthcheck():
    return 'OK', 200


@app.route('/add_user', methods=['POST'])
def add_user():
    app.logger.error(request.json)
    user = AddUserRequest(**request.json)
    return 'OK', 200


@app.route('/delete_user', methods=['POST'])
def delete_user():
    raise NotImplementedError


@app.route('/user/<username>', methods=['GET'])
def get_user():
    raise NotImplementedError