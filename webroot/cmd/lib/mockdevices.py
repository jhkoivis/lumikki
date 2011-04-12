
from BaseHTTPServer import BaseHTTPRequestHandler
from SocketServer import StreamRequestHandler
from json import loads, dumps
from time import time

#import mockserver; s = mockserver.MockServer(); s.run()

class MockHTTPHandler(StreamRequestHandler):
    
    def respond(self):
        
        print "REQUEST: %s" % self.request
        print "COMMAND: %s" % self.command
        print "DATA: %s" % self.data
        print "DEVICE CONF: %s" % self.server.config
        
        if self.request == 'GET':
            self.wfile.write("HTTP/1.1 200 \r\nContent-Type: text/html\r\n\r\n")
            try:
                function = getattr(self, self.command)
                response = function()
                self.wfile.write(response)
            except AttributeError as e:
                response = "COMMAND: %s, DATA: %s" % (self.command, dumps(self.data))
                self.wfile.write(response)     
    
    def HTTPGetData(self):
        self.data = dict()
        try:
            self.command, raw_data = self.command.split('?')
            keyvalues = raw_data.split('&')
            for keyvalue in keyvalues:
                key, value = keyvalue.split('=')
                self.data[key] = value
        except ValueError:
            self.command = self.command
            
    def HTTPGetJSON(self):
        pass
        
class MockTTMHandler(MockHTTPHandler):

    def handle(self):
        
        requestline = self.rfile.readline()
        self.request, raw_command = requestline.split()[0:2]
        self.command = raw_command.split('_')[-1]
        self.checkSetPointTime()
        MockHTTPHandler.HTTPGetData(self)
        MockHTTPHandler.respond(self)
        
    def checkSetPointTime(self):
        conf = self.server.config
        if conf['measuring'] == True:
            try:
                measurementtime = time() - conf['starttime']
                if measurementtime >= float(conf['setpointTime']):
                    conf['measuring'] = False
                    del conf['starttime']
            except KeyError:
                return
            
    def status(self):
        conf = self.server.config
        if conf['measuring'] == True:
            status = dumps({'status':'220'})
        else:
            status = dumps({'status':'200'})
        return status
    
    def initRamp(self):
        conf = self.server.config
        conf.update(self.data)
        conf['measuring'] = True
        return 'initRamp'
    
    def stop(self):
        conf = self.server.config
        conf['measuring'] = False
        return 'stop' 
    
    def startLogging(self):
        conf = self.server.config
        conf['logging'] = True
        return 'startLogging.'
    
    def stopLogging(self):
        conf = self.server.config
        conf['logging'] = False
        return 'stopLogging'
    
    def moveToSetpoint(self):
        conf = self.server.config
        conf.update(self.data)
        conf['measuring'] = True
        conf['starttime'] = time()
        return 'moveToSetpoint'
            
class MockIRHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", r"text/html")
        self.end_headers()
        self.wfile.write("ir")
        return

class MockCamHandler(StreamRequestHandler):

    def handle(self):
        
        self.raw_requestline = self.rfile.readline()
        print "REQUEST: %s" % self.raw_requestline
        if self.raw_requestline.split()[0] == 'GET':
            self.wfile.write("HTTP/1.1 200 \r\nContent-Type: text/html\r\n\r\ncam")
        elif self.raw_requestline.find("status") != -1:
            self.wfile.write('Satus:CAMERA IS ON\r\n')
            self.connection.shutdown()
        
    
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", r"text/html")
        self.end_headers()
        self.wfile.write("cam")
        return
    