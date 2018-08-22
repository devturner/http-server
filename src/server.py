from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import os
from cowpy import cow
import json
import html.parser


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        parsed_qs = parse_qs(parsed_path.query)
        raw_html = '''<!DOCTYPE html>
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
                        </html>'''

        # set a status code
        # set any headers
        # set any body data on the response
        # end headers

        if parsed_path.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(raw_html.encode())
            return

        elif parsed_path.path == '/cow':
            try:
                if len(parsed_qs['msg'][0]) < 1:
                    self.send_response(400)
                    self.send_header('Content-Type', 'text/html')
                    self.end_headers()
                    self.wfile.write(b'400 Bad Request')
                    return
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()
                cowpyy = cow.Kitty()
                msg = cowpyy.milk(parsed_qs['msg'][0])
                self.wfile.write(f'''<html><body>{msg}</body></html>'''.encode("utf-8"))
                return

            except KeyError:
                self.send_response(400)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()
                self.wfile.write(b'400 bad request')
                return

        else:
            self.send_response(404)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(b'404 content not found')
            return

        self.send_response(404)
        self.end_headers()

    def do_POST(self):
        parsed_path = urlparse(self.path)
        parsed_qs = parse_qs(parsed_path.query)

        if parsed_path.path == '/cow':
            try:
                cowpyy = cow.Kitty()
                msg = cowpyy.milk(parsed_qs['msg'][0])
                jcow = json.dumps(msg)
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(f'''{jcow}'''.encode())
                return
            except KeyError:
                send.response(400)
                send.header('Content-Type', 'text/html')
                self.end_headers()
                self.write(b'400, bad request')
                return
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(b'404 content not found')
            return

def create_server():
    return HTTPServer(
        ('127.0.0.1', int(os.environ['PORT'])),
        SimpleHTTPRequestHandler
    )


def run_forever():
    server = create_server()

    try:
        server.serve_forever()
        print(f'Server running on {os.environ["PORT"]}')

    except KeyboardInterrupt:
        server.shutdown()
        server.server_close()


if __name__ == '__main__':
    run_forever()
