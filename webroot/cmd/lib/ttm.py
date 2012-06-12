from urllib2 import urlopen, URLError
from urllib import urlencode
from config import conf
from lumilib import *
from json import loads
import sys

timeout = 5


#def connectAndSendStart():
#	'''
#	TODO: this is the only function that is called 
#	from cgi.
#
#	This includes if-else for constant load, speed, etc
#	'''
#	c = conf()
#	if c.get('ttm_creep_experiment') == True:
#		data = {"load":	  c.get('ttm_load')}
#	else:
#		ret = ttm.connectAndInitRamp()
#		ret = ttm.connectAndStartLogging()
#		ret = ttm.connectAndStartRamp()

def connectAndStart():
    '''
    TODO: this is the only function that is called 
    from cgi.
    
    This includes if-else for constant load, speed, etc
    '''
    c = conf()
    data = {}
    protocol = c.get('ttm_global_protocol')
    for key in c.getAllKeys():
        if key.find('ttm_global') == 0:
            data[key] = c.get(key)
        if key.find('ttm_' + protocol + '_') == 0:
            data[key] = c.get(key)
    #data = {"ttm_global_protocol":	  c.get('ttm_global_protocol'),
	#		"ttm_tensile_channel":	  c.get('ttm_tensile_channel'),
			#"rampRateAE":	  c.get('ttm_ramprateae'),
			#"rampRateSilent":	  c.get('ttm_rampratesilent'),
			#"timeWindow":	  c.get('ttm_window'),
			#"cycleLength":	  c.get('ttm_cyclelength'),
			#"holdTime":	  c.get('ttm_holdtime'),
	#		"ttm_tensile_ramprate":	  c.get('ttm_tensile_ramprate'),
	#		"ttm_creep_load":	      c.get('ttm_creep_load'),
	#		"ttm_tensile_rampamplitude":	  c.get('ttm_tensile_rampamplitude'),
	#		"ttm_global_expid":	c.get('ttm_global_expid')

	#		}
    ret = connectToCommand("start", data)

def connectAndSendInit():
	'''
	TODO: this sends long instructions to the machine.
	This is bind to the init.cgi
	'''
	pass

def connectToCommand(command, data=None):
    c = conf()
    basic_url = "http://%s:%s/lumikki/ttm_" % (c.get('ttm_global_ip'),c.get('ttm_global_port'))
    url = basic_url + command
    if data != None:
        url += "?%s" % urlencode(data)
    sys.stderr.write('%s\n' % (url))
    connection = urlopen(url, timeout=timeout)
    return connection

def connectAndStartSwitch(data=None):
	c = conf()
	basic_url = "http://%s:%s/lumikki/ttm_run2" % (c.get('ttm_global_ip'),c.get('ttm_global_port'))
	url = basic_url
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

def connectAndStartCreep():
    c = conf()
    data = { "creepLoad": c.get('ttm_load'), "channelInt": 2}
    connecttion = connectToCommand("creep", data)
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
        sys.stderr.write('%s\n' % (connection))
        response = loads(connection.read())
        print response
    except URLError:
        raise
        return "110"
    return response['status']
