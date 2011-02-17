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
    
def connectAndSend(c,message):
    log(message);
    ret = connectAndSendMessage(c, message)
    return ret

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
    mid = c.get('g_measurementid')
    message += "T(" + 'F:\data\\' + mid + '\\' + mid + ")"
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

