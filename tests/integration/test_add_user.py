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