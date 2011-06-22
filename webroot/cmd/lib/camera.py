import LabVIEW
import getpass
from config import conf
from lumilib import *

def connectAndSendStart():
    c = conf()
    return connectAndSend(c, createStartMessage(c))

def connectAndSendStop():
    c = conf()
    return connectAndSend(c, createStopMessage(c))

def connectAndGetStatus():
	c = conf()
	responce = connectAndSend(c, createStatusMessage(c))
	# TODO: this is a hack that will be fixed on 
	# device side during summer 2011
	rDict = {}
	splittedResponce = responce.split('\n')
	for item in splittedResponce:
		splittedItem = item.split(':',1)
		rDict[splittedItem[0].strip()] = splittedItem[1].strip()
	if not rDict.has_key('Errors'):
		return 240
	if not rDict['Errors'] == '':
		return 240
	if not rDict.has_key('Satus'):
		return 240
	if rDict['Satus'].find('CAMERA IS STOPPED') >= 0:
		return 210
	if rDict['Satus'].find('CAMERA IS ON') >= 0:
		return 220
	if len(responce) == 0:
		return 240 
	return responce    

def connectAndSend(c,message):
    log(message);
    ret = connectAndSendMessage(c, message)
    return ret

def createStatusMessage(c):
    return "status?"

def createStopMessage(c):
    return "M(2)"

def createStartMessage(c):
    """
    return start message
    """
    message =  "M(1)"
    message += "S(" + c.get('cam_packetsize') + ")"
    message += "F(" + c.get('cam_rawfps')     + ")"
    message += "U(" + getpass.getuser()     + ")"
    message += "W(" + c.get('cam_width')      + ")"
    message += "H(" + c.get('cam_height')     + ")"
    message += "X(" + c.get('cam_xoffset')    + ")"
    message += "Y(" + c.get('cam_yoffset')    + ")"
    message += "E(" + c.get('cam_exposure')   + ")"
    mid = "%s-%s" % (c.get('g_measurementid'), c.get('g_timestamp'))
    message += "T(" + c.get('cam_parentfolder') + '\\' + mid + '\\' + mid + ")"
    message += "I(" + "0"                   + ")"
    print message
    return message

def connectAndSendMessage(c,message):
    """
    Connects to labview and sends message
    returns returnmessage. Passes throw e.g. ValueError
    and other expceptions, which are handled by the upper level.
    """
    LabVIEW.connect(c.get('cam_ip'), int(c.get('cam_port')))
    messageout = LabVIEW._passCommand(message)
    LabVIEW.disconnect()
    return messageout

