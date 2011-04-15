from BaseHTTPServer import HTTPServer
from threading import Thread
from SocketServer import ThreadingMixIn
from mockdevices import MockCamHandler, MockTTMHandler, MockIRHandler
from urllib2 import urlopen
from config import conf
from itertools import izip

class MockServer:
        
    def __init__(self):
    
        self.devicemap = {
                          'cam':(MockCamHandler,('localhost',40001)),
                          'ttm':(MockTTMHandler,('localhost',40002)),
                          'ir' :( MockIRHandler,('localhost',40003))
                          }
        self.devices = dict()
        self.threads = dict()
        for name, config in self.devicemap.items():
            handler, address = config
            self.devices[name] = MockDevice(address, handler)
            self.threads[name] = Thread(target=self.devices[name].serve)
            
    def run(self):
        try:
            for device, thread in izip(self.devices.values(), self.threads.values()):
                thread.daemon = False
                thread.start()
        except AssertionError:
            raise Exception("Run not possible, server destroyed.")
            
    def stop(self):
        for device, thread  in izip(self.devices.values(), self.threads.values()):
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
