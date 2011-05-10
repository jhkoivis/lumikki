from urllib2 import urlopen, URLError
from urllib import urlencode
from config import conf
from lumilib import *
from json import loads

timeout = 5


def connectAndSendStart():
	'''
	TODO: this is the only function that is called 
	from cgi.

	This includes if-else for constant load, speed, etc
	'''
	c = conf()
	if c.get('ttm_creep_experiment') == True:
		data = {"load":	  c.get('ttm_load')}
	else:
		ret = ttm.connectAndInitRamp()
		ret = ttm.connectAndStartLogging()
		ret = ttm.connectAndStartRamp()

def connectAndSendInit():
	'''
	TODO: this sends long instructions to the machine.
	This is bind to the init.cgi
	'''
	pass

def connectToCommand(command, data=None):
    c = conf()
    basic_url = "http://%s:%s/lumikki/csm_lumikki_instron_" % (c.get('ttm_ip'),c.get('ttm_port'))
    url = basic_url + command
    if data != None:
        url += "?%s" % urlencode(data)
    connection = urlopen(url, timeout=timeout)
    return connection

def connectAndStartLogging():
    c = conf()
    data = {"expId": "%s-%s" % (c.get('g_measurementid'), c.get('g_timestamp'))}
    connection = connectToCommand("startLogging", data)
    return connectAndGetStatus()

def connectAndStopLogging():
    connection = connectToCommand("stopLogging")
    return connectAndGetStatus()
    
def connectAndInitRamp():
    c = conf()
    data = { "rampRate":      c.get('ttm_ramprate')
            ,"rampAmplitude": c.get('ttm_rampamplitude')
            }
    connection = connectToCommand("initRamp", data)
    return connectAndGetStatus()

def connectAndStartRamp():
    connection = connectToCommand("startRamp")
    return connectAndGetStatus()

def connectAndStop():
    connection = connectToCommand("stop")
    return connectAndGetStatus()

def connectAndMoveToSetPoint():
    c = conf()
    data = { "setpoint":     c.get('ttm_setpoint')
            ,"setpointTime": c.get('ttm_setpointtime')
            }
    response = connectToCommand("moveToSetpoint", data)
    return connectAndGetStatus()

def connectAndStartCreepExperiment():
	c = conf()
	data = {"load":	  c.get('ttm_load')}
	connectToCommand('creep', data)

def connectAndGetStatus():

    try:
        connection = connectToCommand("status")
	response = loads(connection.read())
	print response
    except URLError:
        return "110"
    return response['status']
