from urllib2 import urlopen, URLError
from urllib import urlencode
from config import conf
from lumilib import *
from json import loads

timeout = 5

def connectToCommand(data=None):
    c = conf()
    # TODO: no hardcoded values
    # move ae_service to config.py as variable
    # move vi_basename to config.py as variable
    url = "http://%s:%s/%s/%s" % (c.get('ae_ip'),c.get('ae_port'),c.get('ae_service'),c.get('ae_viname'))
    if data != None:
        # this converts dict to ?key1=value1&key2=value2&...
        url += "?%s" % urlencode(data)
    connection = urlopen(url, timeout=timeout)
    return connection

def connectAndStart():
    c = conf()
    filename = "%s-%s" % (c.get('g_measurementid'), c.get('g_timestamp'))
    clockfreq = "%s" % (c.get('ae_freq')) 
    data = {"stopClock":"0","stopCollection":"0","filename": filename, "ClockFrequency" : clockfreq,"startClock":"1","startCollection":"1"}
    connection = connectToCommand(data)
    #return connectAndGetStatus()

def connectAndStop():
    data = {"startClock":"0","startCollection":"0","stopClock":"1","stopCollection":"1"} # temporary
    connection = connectToCommand(data)
    #return connectAndGetStatus()

def connectAndGetStatus():
    try:
        connection = connectToCommand("status")
        response = loads(connection.read())
        print response
    except URLError:
        return "110"
    return response['status']
