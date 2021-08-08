from flask import Flask

app = Flask(__name__)

@app.route('/')
def healthcheck():
    return 'OK', 200


@app.route('/add_user', methods=['POST'])
def add_user():
    raise NotImplementedError


@app.route('/delete_user', methods=['POST'])
def delete_user():
    raise NotImplementedError


@app.route('/user/<username>', methods=['GET'])
def get_user():
    raise NotImplementedError