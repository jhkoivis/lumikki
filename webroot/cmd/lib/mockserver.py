from BaseHTTPServer import HTTPServer
from threading import Thread
from SocketServer import ThreadingMixIn
from mockdevices import MockCamHandler, MockTTMHandler, MockIRHandler
from urllib2 import urlopen
from config import conf

class MockServer:
        
    def __init__(self):
    
        self.devicemap = {
                          MockCamHandler:('localhost',40001),
                          MockTTMHandler:('localhost',40002),
                          MockIRHandler:('localhost',40003)
                          }
        self.devices = dict()
        for handler, address in self.devicemap.items():
            device = MockDevice(address, handler)
            self.devices[device] = Thread(target=device.serve)
            
    def run(self):
        try:
            for device, thread in self.devices.items():
                thread.daemon = False
                thread.start()
        except AssertionError:
            raise Exception("Run not possible, server destroyed.")
            
    def stop(self):
        for device, thread in self.devices.items():
            if thread.isAlive:
                device.stop_server()
                device.socket.close()
                device.server_close()

class MockDevice(HTTPServer,ThreadingMixIn):

    def __init__(self, address, handler):
        self.stop = False
        self.config = dict({'measuring':False})
        HTTPServer.__init__(self, address, handler)
    
    def serve(self):
        while True:
            self.handle_request()
            if self.stop:
                break
    
    def stop_server(self):
        self.stop = True
        urlopen("http://%s:%s" % self.server_address)
        
if __name__=="__main__":
    server = MockServer()
    server.run()
    raw_input("Press enter to shutdown server...")
    server.stop()
