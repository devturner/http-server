import requests as req


def test_server_get_home_route_status_200():
    response = req.get('http://127.0.0.1:5000')
    assert response.status_code == 200


def test_server_get_home_route_response_content():
    response = req.get('http://127.0.0.1:5000')
    assert '<html><body><h1>Hello world</h1></body></html>' == str(response.text)
    assert 'Hello world' in str(response.text)
