
from BaseHTTPServer import BaseHTTPRequestHandler
from SocketServer import StreamRequestHandler

#import mockserver; a = mockserver.MockServer(); a.run()

class MockCamHandler(StreamRequestHandler):

    def handle(self):
        
        self.raw_requestline = self.rfile.readline()
        print "REQUEST: %s" % self.raw_requestline
        if self.raw_requestline.split()[0] == 'GET':
            self.wfile.write("HTTP/1.1 200 \r\nContent-Type: text/html\r\n\r\ncam")
        elif self.raw_requestline.find("status") != -1:
            self.wfile.write('Satus:CAMERA IS ON\r\n')
            print self.__dict__
            self.finish()
            #self.connection.close()
        
    
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", r"text/html")
        self.end_headers()
        self.wfile.write("cam")
        return
        
class MockTTMHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", r"text/html")
        self.end_headers()
        self.wfile.write("ttm")
        return
