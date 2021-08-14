from _pytest.mark import param
import pytest

@pytest.mark.parametrize('user, email, password, data', [
    ('user1', 'user1@mail.com', 'password1', None),
    ('user1', 'user1@mail.com', 'password1', {'foo': 'bar'}),
])
def test_add_user_happy_path(client, user, email, password, data):
    body = {'user_id': user, 'email': email, 'password': password, 'data': data}
    response = client.post('/add_user', json=body)
    assert response.status_code == 200
    assert response.data == b'OK'

    response = client.get(f'/user/{user}')
    assert response.status_code == 200
    assert response.json['user_id'] == user
    assert response.json['email'] == email 
    assert response.json['password'] == password 
    assert response.json['data'] == data 


@pytest.mark.parametrize('user, email, password, data', [
    (None, 'user1@mail.com', 'password1', None),
    ('', 'user1@mail.com', 'password1', None),
    ('user1', None, 'password1', None),
    ('user1', '', 'password1', None),
    ('user1', 'user1@mail.com', None, None),
    ('user1', 'user1@mail.com', '', None),
    ('user1', 'user1@mail.com', 'short', None),
])
def test_add_user_empty_field_raises_exception(client, user, email, password, data):
    body = {'user_id': user, 'email': email, 'password': password, 'data': data}
    response = client.post('/add_user', json=body)
    assert response.status_code == 422


def test_add_user_duplicated_ids(client):
    # Add first user
    body = {'user_id': 'user1', 'email': 'user1@mail.com', 
            'password': 'password1', 'data': None}
    response = client.post('/add_user', json=body)
    assert response.status_code == 200
    assert response.data == b'OK'

    # Try to add him again error should be handled
    response = client.post('/add_user', json=body)
    assert response.status_code == 200
    assert response.data == b'OK'