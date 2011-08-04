from urllib2 import urlopen, Request, URLError
from json import dumps, loads
from config import conf
from lumilib import *

def connectAndGetResponse(data):
    try:
        req = createRequest(data)
        timeout = int(c.get('g_timeout'))
        connection = urlopen(req,timeout=timeout)
        response_json = loads(connection.read())
        return response_json["status"]
    except URLError:
        return "110"

def createRequest(data):
    c = conf()
    ip      = c.get('ir_ip')
    port    = c.get('ir_port')
    cgipath = c.get('ir_cgipath')
    url = "http://%s:%s/%s" % (ip,port,cgipath)
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

def connectAndStart():
    c = conf()
    recordmode = int(c.get('ir_triggerexperiment'))
    connectAndSendSettings()
    response = connectAndGetResponse({"startRecording":recordmode})
    return response

def connectAndSendSettings():
    c = conf()
    # TODO: path parsing belongs to device side, remove filename and add timestamp to data -dictionary 
    path = c.get('ir_parentfolder') + '\\' + c.get('g_measurementid') + '-' + c.get('g_timestamp') 
    data ={
           "expId":c.get('g_measurementid'),
           "filename":c.get('g_measurementid') + '-',
           "path":path,
           "framerate":float(c.get('ir_framerate')),
           "recordTime":float(c.get('ir_recordtime')),
           "storeCondition":int(c.get('ir_storecondition')),
           "stopCondition":int(c.get('ir_stopcondition')),
           "startCondition":int(c.get('ir_startcondition')),
           "startValue":int(c.get('ir_startvalue')),
           "storeValue":int(c.get('ir_storevalue')),
           "recordFormat":int(c.get('ir_recordformat')),
           "trigSource":int(c.get('ir_trigsource')),
           "autoShutter":int(c.get('ir_autoshutter'))
           }
    response = connectAndGetResponse(data)
    return response

def connectAndGetImage():
    response = connectAndGetResponse({"getImage":0})
    return response

def connectAndGetImageSeries():
    response = connectAndGetResponse({"getImageSeries":0})
    return response

def connectAndSimulateTrigger():
    response = connectAndGetResponse({"simulateTrigger":0})
    return response

def connectAndStopRecording():
    response = connectAndGetResponse({"stopRecording":0})
    return response

def connectAndGetStatus():
    response = connectAndGetResponse({"status":0})
    return response
    
def connectAndGetState():
    req = createRequest({"isConnected":0})
    timeout=c.conf()
    timeout = int(c.get('g_timeout'))
    connection = urlopen(req,timeout=timeout)
    r_json = loads(connection.read())
    return r_json
