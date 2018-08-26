from multiprocessing import Process
from src import server
import pytest
# import requests


@pytest.fixture(scope='session', autouse=True)
def server_setup():
    instance = server.create_server()

    process = Process(target=instance.serve_forever)
    process.daemon = True
    process.start()


# def test_home_sends_200_response(server_setup):
#     response = requests.get('http://127.0.0.1:5000')
#     assert response.status_code == 200
