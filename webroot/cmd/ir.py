from urllib2 import urlopen, Request, URLError
from httplib import responses
from json import dumps, loads
from config import conf
from lumilib import *

timeout = 60
cgipath = "/cgi-bin/MessageSenderCon.exe"

statusResponses = { "000":"Cannot connect to anything"
       , "010":"Server sent unknown status"
       , "020":"Server response did not contain status"
       , "100":"Disabled from server."
       , "110":"Target machine did not respond"
       , "120":"Server received malformed command."
       , 403:"122"
       , 0:"210"    #"Ready to measure"
       , 1:"200"    #"Target available, values not set"
       , 200:"210"  #"Ready to measure"
       , "220":"Measuring"
       , "230":"System is busy, please try again in a while."
}

def connectAndGetResponse(data):
    req = createRequest(data)
    connection = urlopen(req,timeout=timeout)
    response = connection.getcode()
    return response

def createRequest(data):
    
    c = conf()
    ip = c.get('ir_ip')
    port = c.get('ir_port')
    url = "http://%s:%s%s" % (ip,port,cgipath)
    json = dumps(data)
    req = Request(url, json, {'Content-Type':'application/json'})
    return req

def getResponseString(response):
    return responses[response]

def getStatusResponseString(response):
    return statusResponses[response]

def connectAndConnectIR():
    response = connectAndGetResponse({"connect":0})
    return getResponseString(response)

def connectAndDisconnectIR():
    response = connectAndGetResponse({"disconnect":0})
    return getResponseString(response)

def connectAndFocus():
    response = connectAndGetResponse({"focus":0})
    return getResponseString(response)

def connectAndSetExpID():
    c = conf()
    response = connectAndGetResponse({"expId":c.get('g_measurementid')})
    return getResponseString(response)

def connectAndGetImage():
    response = connectAndGetResponse({"getImage":0})
    return getResponseString(response)

def connectAndGetImageSeries():
    response = connectAndGetResponse({"getImageSeries":0})
    return getResponseString(response)

def connectAndGetStatus():
    req = createRequest({"isConnected":0})
    try:
        connection = urlopen(req,timeout=timeout)
        #r_json = loads(connection.read())
        #return getStatusResponseString(r_json["isConnected"])
        return getStatusResponseString(connection.getcode())
    except URLError:
        return "110"
    #except ValueError:
    #    return "110"
    
def connectAndGetState():
    req = createRequest({"isConnected":0})
    connection = urlopen(req,timeout=timeout)
    r_json = loads(connection.read())
    return r_json