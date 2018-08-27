import requests as req


def test_server_get_home_route_status_200():
    """ Teat that home is sending a 200 status code when it works
    """
    response = req.get('http://127.0.0.1:5000')
    assert response.status_code == 200


def test_server_get_home_route_response_content():
    """ make sure the home route is sending the response
    """
    response = req.get('http://127.0.0.1:5000')
    assert '''<!DOCTYPE html>
                        <html>
                        <head>
                            <title> cowsay </title>
                        </head>
                        <body>
                            <header>
                                <nav>
                                <ul>
                                    <li><a href="/cow">cowsay</a></li>
                                </ul>
                                </nav>
                            <header>
                            <main>
                               <p> This is a funny server that can give you a
                               cow</p>
                            </main>
                        </body>
                        </html>''' == str(response.text)


def test_home_response_code():
    """ Test the home returns 200
    """
    response = req.get('http://127.0.0.1:5000')
    assert response.status_code == 200


def test_errors_for_bad_request():
    """ Test the missing route returns 404
    """
    response = req.get('http://127.0.0.1:5000/rocket_ship')
    assert response.status_code == 404


def test_cow_say_takes_message():
    """ make sure the cow can take a message
    """
    response = req.get('http://127.0.0.1:5000/cow?msg=saying this works')
    assert response.status_code == 200
