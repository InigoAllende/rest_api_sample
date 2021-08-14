import pytest


def _populate_db(client, user_data):
    response = client.post('/add_user', json=user_data)
    assert response.status_code == 200
    user_data['user_id']
    response = client.get(f'/user/{user_data["user_id"]}')
    assert response.status_code == 200
    assert response.json['user_id'] == user_data['user_id']
    assert response.json['email'] == user_data['email'] 
    assert response.json['password'] == user_data['password'] 
    assert response.json['data'] == user_data['data'] 


@pytest.mark.parametrize('user, email, password, data', [
    ('user1', 'user1@mail.com', 'password1', None),
    ('user1', 'user1@mail.com', 'password1', {'foo': 'bar'}),
])
def test_delete_user_happy_path(client, user, email, password, data):
    user_data = {'user_id': user, 'email': email, 'password': password, 'data': data}
    _populate_db(client, user_data)

    response = client.post('/delete_user', json={'user_id': user, 'password': password})
    assert response.status_code == 200

    response = client.get(f'/user/{user}')
    assert response.status_code == 200
    assert not response.json


def test_delete_user_not_in_db(client):
    response = client.post('/delete_user', 
                           json={'user_id': 'user1', 
                                 'password': 'password'})
    assert response.status_code == 200