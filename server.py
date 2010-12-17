import threading
import webbrowser
import BaseHTTPServer
import SimpleHTTPServer
import json


PORT = 8080


class TestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    """The test example handler."""
    def do_GET(self):
        self.wfile.write(json.dumps({'status':100}))

def start_server():
    """Start the server."""
    server_address = ("", PORT)
    server = BaseHTTPServer.HTTPServer(server_address, TestHandler)
    server.serve_forever()

if __name__ == "__main__":
    start_server()
