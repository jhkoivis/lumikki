from urllib2 import urlopen
from urllib import urlencode
from httplib import responses
from config import conf
from lumilib import *

timeout = 3

statusResponses = { "000":"Cannot connect to anything"
       , "010":"Server sent unknown status"
       , "020":"Server response did not contain status"
       , "100":"Disabled from server."
       , "110":"Target machine did not respond"
       , "120":"Server received malformed command."
       , 403:"122"
       , "200":"Target available, values not set"
       , 200:"210"
       , "220":"Measuring"
       , "230":"System is busy, please try again in a while." 
}


def connectToCommand(command, data=None):
    
    command_root = "/lumikki/csm_lumikki_instron_"

    return createUrlAndConnect(command_root, data)

def createUrlAndConnect(command, data=None):
    c = conf()
    basic_url = "http://%s:%s" % (c.get('ttm_ip'),c.get('ttm_port'))
    url = basic_url + command
    if data != None:
        url += "?%s" % urlencode(data)
    return connect(url)
    
def connect(url):
    connection = urlopen(url, timeout=timeout)
    response = connection.getcode()
    return response

def getResponseString(response):
    return responses[response]

def connectAndStartLogging():
    c = conf()
    data = {"expId": c.get('g_measurementid')}
    response = connectToCommand("startLogging", data)
    return getResponseString(response)

def connectAndStopLogging():
    response = connectToCommand("stopLogging")
    return getResponseString(response)
    
def connectAndInitRamp():
    c = conf()
    data = { "rampRate":      c.get('ttm_ramprate')
            ,"rampAmplitude": c.get('ttm_rampamplitude')
            }
    response = connectToCommand("initRamp", data)
    return getResponseString(response)

def connectAndStartRamp():
    response = connectToCommand("startRamp")
    return getResponseString(response)

def connectAndMoveToSetPoint():
    c = conf()
    data = { "setpoint":     c.get('ttm_setpoint')
            ,"setpointTime": c.get('ttm_setpointtime')
            }
    response = connectToCommand("moveToSetpoint", data)
    return getResponseString(response)

def connectAndGetStatus():
    # This needs more sophisticated ideas in order to recognize the measuring
    response = createUrlAndConnect("")
    return statusResponses[response]