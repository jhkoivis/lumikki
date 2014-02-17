from urllib2 import urlopen, Request, URLError
from json import dumps, loads
from config import conf
from lumilib import *
import sys

def connectAndGetResponse(data):
    c = conf()
    try:
        req = createRequest(data)
        timeout = int(c.get('g_timeout'))
        connection = urlopen(req,timeout=timeout)
        response_json = loads(connection.read())
        sys.stderr.write(str(connection) + '\n')
        sys.stderr.write(str(response_json) + '\n')
        sys.stderr.flush()
        return response_json["status"]
    except URLError:
        return "110"

def createRequest(data):
    c = conf()
    ip      = c.get('ir_global_ip')
    port    = c.get('ir_global_port')
    cgipath = c.get('ir_global_cgipath')
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
    connectAndSendSettings()
    triggerexperiment = int(c.get('ir_global_triggerexperiment'))
    response = connectAndGetResponse({"startRecording":triggerexperiment})
    return response

def connectAndSendSettings():
    c = conf()
    # TODO: path parsing belongs to device side, add timestamp to data -dictionary 
    path = c.get('ir_global_parentfolder') + '\\' + c.get('g_measurementid') + '-' + c.get('g_timestamp')
    data = {"expId":c.get('g_measurementid'),
            "path":path,
            "framerate":float(c.get('ir_global_framerate')),
            "storeCondition":int(c.get('ir_global_storecondition')),
            "storeValue":int(c.get('ir_global_storevalue')),
            "recordFormat":int(c.get('ir_global_recordformat')),
            "autoShutter":int(c.get('ir_global_autoshutter'))
            }
    if int(c.get('ir_global_triggerexperiment')) == 1: 
        trigdata = {"stopCondition":int(c.get('ir_trigger_stopcondition')),
                    "stopValue":float(c.get('ir_trigger_stopvalue')),
                    "startCondition":int(c.get('ir_trigger_startcondition')),
                    "startValue":int(c.get('ir_trigger_startvalue')),
                    "trigSource":int(c.get('ir_trigger_trigsource'))
                   }
        data.update(trigdata)
    else:
        streamdata = {"stopCondition":int(c.get('ir_stream_stopcondition')),
                      "startCondition":int(c.get('ir_stream_startcondition')),
                      "startValue":int(c.get('ir_stream_startvalue'))
                     }
        data.update(streamdata)
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
