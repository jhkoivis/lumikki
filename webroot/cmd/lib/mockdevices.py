
from BaseHTTPServer import BaseHTTPRequestHandler
from SocketServer import StreamRequestHandler
from json import loads, dumps
from time import time
        
class MockTTMHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.checkStatus()
        raw_command = self.path.split('_')[-1]
        command = self.parseCommand(raw_command)
        
        try:
            function = getattr(self, command)
            response = function()
            print "COMMAND: %s" % command
        except AttributeError:
            response = ''

        self.send_response(200)
        self.send_header('Content-Type','application/json')
        self.end_headers()
        self.wfile.write(response)
        self.wfile.close()
        print "SERVER CONFIG: %s" % self.server.config
        
    def parseCommand(self, command):
        self.data = dict()
        try:
            command, raw_data = command.split('?')
            keyvalues = raw_data.split('&')
            for keyvalue in keyvalues:
                key, value = keyvalue.split('=')
                self.data[key] = value
        except ValueError:
            pass
        return command
        
    def checkStatus(self):
        conf = self.server.config
        if conf['measuring'] == True:
            try:
                measurementtime = time() - conf['startTime']
                if measurementtime >= float(conf['setpointTime']):
                    conf['measuring'] = False
                    del conf['startTime']
            except KeyError:
                return
                
    def status(self):
        conf = self.server.config
        if conf['measuring'] == True:
            statuscode = '220'
        else:
            statuscode = '200'
        return dumps(dict({'status':statuscode}))
    
    def initRamp(self):
        conf = self.server.config
        conf.update(self.data)
        conf['measuring'] = True
        return ''
    
    def stop(self):
        conf = self.server.config
        conf['measuring'] = False
        return ''
    
    def startLogging(self):
        conf = self.server.config
        conf['logging'] = True
        return ''
    
    def stopLogging(self):
        conf = self.server.config
        conf['logging'] = False
        return ''
    
    def moveToSetpoint(self):
        conf = self.server.config
        conf.update(self.data)
        conf['measuring'] = True
        conf['startTime'] = time()
        return ''
            
class MockIRHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        self.checkStatus()
        conf = self.server.config
        
        if self.headers['content-type'] == "application/json":
            clength = int(self.headers['content-length'])
            data = self.rfile.read(clength)
            loaded = loads(data)
            for key in loaded.keys():
                try:
                    function = getattr(self, key)
                    response = function()
                    print "COMMAND: %s" % key
                except (AttributeError, TypeError):
                    conf[key] = loaded[key]
                    response = self.status()
                    
        self.writeResponse(response)
        print "SERVER CONFIG: %s" % self.server.config
                    
    def do_GET(self):
        self.writeResponse(self.status())
        
    def writeResponse(self, response):
        self.send_response(200)
        self.send_header('Content-Type','application/json')
        self.end_headers()
        self.wfile.write(response)
        print "RESPONSE: %s" % response
        
    def status(self):
        conf = self.server.config
        if conf['measuring']:
            statuscode = "220"
        else:
            statuscode = "210"
        return dumps(dict({'status':statuscode}))
        
    def connect(self):
        conf = self.server.config
        if not conf['measuring']:
            conf['isConnected'] = True
        return self.status()
    
    def disconnect(self):
        conf = self.server.config
        if not conf['measuring']:
            conf['isConnected'] = False
        return self.status()
    
    def focus(self):
        conf = self.server.config
        if not conf['measuring']:
            conf['focused'] = True
        return self.status()
        
    def getImage(self):
        return self.status()
        
    def getImageSeries(self):
        conf = self.server.config
        conf['measuring'] = True
        conf['startTime'] = time()
        return self.status()

    def stopRecording(self):
        conf = self.server.config
        conf['measuring'] = False
        try:
            del conf['startTime']
        except KeyError:
            pass
        return self.status()
        
    def checkStatus(self):
        conf = self.server.config
        if conf['measuring']:
            try:
                currenttime = time()
                if (currenttime - conf['startTime']) >= conf['recordTime']:
                    conf['measuring'] = False
                    del conf['startTime']
            except KeyError:
                pass

class MockCAMHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", r"text/html")
        self.end_headers()
        self.wfile.write("cam")
        return
    
class MockAEHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", r"text/html")
        self.end_headers()
        self.wfile.write("ae")
        return
    
