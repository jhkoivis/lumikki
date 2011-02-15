from urllib2 import urlopen
from urllib import urlencode
from httplib import responses
from config import conf
from lumilib import *

timeout = 3

statusResponses = dict({ "000":"Cannot connect to anything"
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
})

def connectAndSendStart():
    c = conf()
    command = "http://%s:%s/ttmStart" % (c.get('ttm_ip'),c.get('ttm_port'))
    response = connect(command)
    return getResponseString(response)
    
def connectAndSendStop():
    c = conf()
    command = "http://%s:%s/ttmStop" % (c.get('ttm_ip'),c.get('ttm_port'))
    response = connect(command)
    return getResponseString(response)

def connectAndGetStatus():
    c = conf()
    command = "http://%s:%s" %(c.get('ttm_ip'),c.get('ttm_port'))
    response = connect(command)
    return statusResponses[response]
    
def connectAndSetRamp():
    c = conf()
    command = "http://%s:%s/ttmRamp" % (c.get('ttm_ip'),c.get('ttm_port'))
    data = { rampRate:      c.get('ttm_ramprate')
            ,rampHeight:    c.get('ttm_rampheight')
            ,channel:       c.get('ttm_channel')
            }
    response = connect(command, data)
    return getResponseString(response)

def getResponseString(response):
    return responses[response]
    
def connect(command, data=None):
    connection = urlopen(command, data=data,timeout=3)
    response = connection.getcode()
    return response