def test_health_satus(client):
    """
    pass: Check server status
    """
    response = client.get('/')

    assert response.status_code == 200
    data = response.json

    assert data['status'] == 'ready'