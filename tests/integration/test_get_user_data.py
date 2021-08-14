def test_fetch_data_not_stored_user(client):
    response = client.get(f'/user/newuser')
    assert response.status_code == 200
    assert response.json == {}
