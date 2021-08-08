import pytest

@pytest.mark.parametrize('user, email, password, data', [
    ('user1', 'user1@mail.com', 'password1', None),
])
def test_add_user_happy_path(client, user, email, password, data):
    body = {'user_id': user, 'email': email, 'password': password, 'data': data}
    response = client.post('/add_user', json=body)
    assert response.status_code == 200
    assert response.data == b'OK'
