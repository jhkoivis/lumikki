from urllib2 import urlopen, Request, URLError
from json import dumps, loads
from config import conf
from lumilib import *

# TODO: move constants to external configuration file
# same way as in stdic

timeout = 60
cgipath = "/cgi-bin/MessageSenderCon.exe"

def connectAndGetResponse(data):
    req = createRequest(data)
    connection = urlopen(req,timeout=timeout)
    return connectAndGetStatus()

def createRequest(data):
    
    c = conf()
    ip = c.get('ir_ip')
    port = c.get('ir_port')
    url = "http://%s:%s%s" % (ip,port,cgipath)
    json = dumps(data)
    req = Request(url, json, {'Content-Type':'application/json'})
    return req

def connectAndConnectIR():
    response = connectAndGetResponse({"connect":0})
    return response

def connectAndDisconnectIR():
    response = connectAndGetResponse({"disconnect":0})
    return response

def connectAndFocus():
    response = connectAndGetResponse({"focus":0})
    return response

def connectAndSetExpID():
    c = conf()
    response = connectAndGetResponse({"expId":c.get('g_measurementid')})
    return response

def connectAndGetImage():
    response = connectAndGetResponse({"getImage":0})
    return response

def connectAndGetImageSeries():
    response = connectAndGetResponse({"getImageSeries":0})
    return response

def connectAndGetStatusNew():
    try:
        req = createRequest({"status":0})
        connection = urlopen(req,timeout=timeout)
        response_json = loads(connection.read())
        return response_json["status"]
    except URLError:
        return "110"
    
def connectAndGetStatusLegacy():
    try:
        req = createRequest({"isConnected":0})
        connection = urlopen(req,timeout=timeout)
        response_json = loads(connection.read())
        if response_json["isConnected"] == 0:
            return "210"
        else:
            return "200"
    except URLError:
        return "110"
    
connectAndGetStatus = connectAndGetStatusLegacy
    
def connectAndGetState():
    req = createRequest({"isConnected":0})
    connection = urlopen(req,timeout=timeout)
    r_json = loads(connection.read())
    return r_json