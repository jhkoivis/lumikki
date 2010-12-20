import threading
import webbrowser
import BaseHTTPServer
import SimpleHTTPServer
import json


PORT = 8080


class TestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    """The test example handler."""
    def do_GET(self):
        print "Got request:" + self.path
        self.send_response(200)
        if self.path.endswith(".html") or self.path.endswith(".js"): 
            data = open(self.path[1:], 'r').read()
            if self.path.endswith(".html"): 
                self.send_header("Content-type:", "text/html")
            else:
                self.send_header("Content-type:", "text/javascript")
            self.send_header("Content-length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
        elif self.path.endswith("status"): 
            self.send_header("Content-type", "application/javascript")
            s = json.dumps({'status':100})
            self.send_header("Content-length", str(len(s)))
            self.end_headers()
            self.wfile.write(s)
        else:
            self.send_error(404)

def start_server():
    """Start the server."""
    server_address = ("", PORT)
    server = BaseHTTPServer.HTTPServer(server_address, TestHandler)
    server.serve_forever()

if __name__ == "__main__":
    start_server()
