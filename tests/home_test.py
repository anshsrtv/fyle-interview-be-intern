def test_validate_request(client):
    """
    fail case: Method not allowed
    """
    response = client.post('/')

    assert response.status_code == 405

        
def test_health_satus(client):
    """
    pass: Check server status
    """
    response = client.get('/')

    assert response.status_code == 200
    data = response.json

    assert data['status'] == 'ready'