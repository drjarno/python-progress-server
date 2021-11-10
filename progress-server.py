#!/usr/bin/env python3

from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl
import json

statistics = {
    "chap1ex1": 0,
    "chap1ex2": 0,
    "chap1ex3": 0,
    "chap2ex1": 0,
    "chap2ex2": 0,
    "chap2ex3": 0,
    "chap2ex4": 0,
    "chap3ex1": 0,
    "chap3ex2": 0,
    "chap3ex3": 0,
    "chap3ex4": 0,
    "chap3ex5": 0,
    "chap3ex6": 0,
    "chap3ex7": 0,
    "chap3ex8": 0,
    "chap3ex9": 0,
    "chap3ex10": 0,
    "chap4ex1": 0,
    "chap4ex2": 0,
    "chap4ex3": 0,
    "chap4ex4": 0,
    "chap4ex5": 0,
}

class ProgressServer(BaseHTTPRequestHandler):
    """docstring for ProgressServer."""

    def do_GET(self):
        path = self.path.split('?')
        if len(path) > 1:
            values = path[1]
        path = path[0]

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        if path == "/admin" or path == "/admin/" or path == "/admin/index.html":
            self.wfile.write(('{"status":"ok","counts":' + json.dumps(statistics) + '}').encode('utf8'))
        elif path[:10] == "/done_chap":
            print(path[6:])
            try:
                statistics[path[6:]] += 1
                self.wfile.write(b'{"status":"ok"}')
            except Exception as e:
                self.wfile.write(b'{"status":"error","message":"bad exercise"}')

        else:
            self.wfile.write(b'{"status":"error","message":"bad path"}')


def serve():
    server = HTTPServer(("0.0.0.0", 8080), ProgressServer)
    server.socket = ssl.wrap_socket(server.socket, certfile='./server.pem', server_side=True)
    server.serve_forever()

if __name__ == "__main__":
    serve()
