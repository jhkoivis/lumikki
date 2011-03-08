###########################
# Labview command line interface
#
# usage: python useCamera_jko.py 1 \\\\disco.hut.fi\\work\\jko\\test5\\test5-
#
############################
#
# Juha Koivisto. 100504 
# Jani Saarenpaa. TKK summer 2009.
#
# TODO:
# - change test name to path
# - change single letters to words (make it more dictionary style, or xml style)
# - change the labview side to match these
#
# 
#
import LabVIEW
import sys
import string
import os
import getpass # to get the user name
import datetime # to get the date
import ConfigParser
import time # to get some sleep


def printUsage():
    """
    Prints usage information
    """
    print ""
    print "1) Usage: "
    print "             python " + sys.argv[0] + " start $testNo $path"
    print ""	
    print "   $testNo : number of the test (this will be removed in the future)"
    print "   $path   : path in camera computer, note that after last '\\' is the file prefix"
    print "             remember to protect the '\\' in linux side"
    print ""
    print "   example : python " + sys.argv[0],
    print " start 1 \\\\\\\\disco.hut.fi\\\\work\\\\jko\\\\test5\\\\test5-"  
    print ""
    print "2) Usage: python " + sys.argv[0] + " stop"
    print "   To stop the camera and lifts the lift"
    print "3) Usage: python " + sys.argv[0] + " status"
    print "   To have it print the status of Windows machine"
    print "4) Usage: python " + sys.argv[0] + " change"
    print "   Changes the camera's parameters to CHANGE parameters"
    print "5) Usage: python " + sys.argv[0] + " cycle up/down"
    print "   You can raise the lift and stop taking photos."
    print "   You should see " + sys.argv[0] + ".conf file for any need for change."

def makeDefaultConfig():
    """
    Set deafult config. Write it to file. 
    
    returns ConfigParser instance with default config
    """ 
    # Make the config:
    config = ConfigParser.SafeConfigParser()
    # default configuration if the configuration file doesn't exist.
    config.set('', 'RawFPS'    , '117000')
    # 1024*768*8 bit = 786 432 kilobytes
    # (4+20+8+4+786 432)*9145 = 85.9997813
    # 9145 not possible => 9144
    config.set('', 'PacketSize', '9144')
    config.set('', 'XOffset'   , '0')
    config.set('', 'YOffset'   , '0')
    config.set('', 'Width'     , '1024')
    config.set('', 'Height'    , '768')
    config.set('', 'IP'        , '130.233.203.154')
    config.set('', 'Port'      , '6423')
    config.set('', 'exposure'  , '500')

    config.add_section('CHANGE')

    config.set('CHANGE', 'RawFPS'    , '1000') # 1000 = 1 sec
    config.set('CHANGE', 'PacketSize', '9144')
    config.set('CHANGE', 'XOffset'   , '0')
    config.set('CHANGE', 'YOffset'   , '0')
    config.set('CHANGE', 'Width'     , '1024')
    config.set('CHANGE', 'Height'    , '768')
    config.set('CHANGE', 'IP'        , '130.233.203.154')
    config.set('CHANGE', 'Port'      , '6423')
    config.set('CHANGE', 'exposure'  , '500')     

    if not config.read(os.path.abspath(sys.argv[0]) + '.conf'): 
        try:
            fileHandle = open(os.path.abspath(sys.argv[0]) + ".conf", 'w')
        except IOError:
            print "Error while opening conf file " \
                   + os.path.abspath(sys.argv[0]) + ".conf."
            os._exit(2)
        config.write(fileHandle)
        fileHandle.close()
    
    return config

def createStartMessage(config):
    """
    return start message
    """
    try:
        testName = sys.argv[3] 
    except IndexError:
        testName = "" 
    try:
        string.atoi(sys.argv[2])
        # TODO fix above and below
        if len(sys.argv[2]) > 2: # this might be more elegant 
            testName = testName + "0"     # with string.size()
    except ValueError:
        print "ERROR: check that the test number is a number"
        os._exit(2)
    except IndexError:
        print "ERROR: give at least test number e.g."
        print "   " + sys.argv[0] + " start 0" 
        exit(2)
    testName = testName + sys.argv[2]
    testName = testName + datetime.date.today().strftime("%y%m%d")

    message =  "M(1)"
    message += "S(" + config.get('DEFAULT', "PacketSize") + ")"
    message += "F(" + config.get('DEFAULT', "RawFPS"    ) + ")"
    message += "U(" + getpass.getuser()                   + ")"
    message += "W(" + config.get('DEFAULT', "Width"     ) + ")"
    message += "H(" + config.get('DEFAULT', "Height"    ) + ")"
    message += "X(" + config.get('DEFAULT', "XOffset"   ) + ")"
    message += "Y(" + config.get('DEFAULT', "YOffset"   ) + ")"
    message += "E(" + config.get('DEFAULT', "exposure"  ) + ")"
    message += "T(" + testName                            + ")"
    message += "I(" + "0"                                 + ")"
    
    return message

def createChangeMessage(config):
    """
    return change message
    """
    message  = "M(3)"
    message += "S(" + config.get('CHANGE', "PacketSize") + ")"
    message += "F(" + config.get('CHANGE', "RawFPS") + ")"
    message += "U(" + getpass.getuser() + ")"
    message += "W(" + config.get('CHANGE', "Width") + ")"
    message += "H(" + config.get('CHANGE', "Height") + ")"
    message += "X(" + config.get('CHANGE', "XOffset") + ")"
    message += "Y(" + config.get('CHANGE', "YOffset") +")"
    message += "E(" + config.get('CHANGE', "exposure") + ")"
             
    return message

def createCycleMessage():
    """
    return cycle up/down message
    """
    if len(sys.argv) < 3:
        print 'cycle needs an argument that states either up or down.'
    else:
        if sys.argv[2] == "up":
            message = "M(4)"
        elif sys.argv[2] == "down":
            message = "M(5)"
    return message

def connectAndSendMessage(config,message):
    """
    Connects to labview and sends message
    returns returnmessage
    """
    # Try to connect to Labview
    try:
        if LabVIEW.connect(config.get('DEFAULT', "IP"), \
                config.getint('DEFAULT', "Port")):
            os._exit(1)
    except ValueError:
        print "ERROR: Check that the port is number."
        os._exit(2)
    # Send the message to this vi. For example:
    #    print LabVIEW._passCommand(message)
    messageout = LabVIEW._passCommand(message)
    LabVIEW.disconnect()
    return messageout

def createMessage(config):
    """
    Creates a message based on sys.argv
    TODO pass sys.argv as a parameter
    returns message
    """
    # create start message
    if sys.argv[1] == "start":
        message = createStartMessage(config)
    # create change message
    elif sys.argv[1] == "change":
        message = createChangeMessage(config)
    # Cycle = lift up:
    elif sys.argv[1] == "cycle":
        message = createCycleMessage()
    # STOP
    elif sys.argv[1] == "stop":
        message = "M(2)"
    # STATUS REPORT
    elif sys.argv[1] == "status":
        message = "status?"
    else:
        print "ERROR: Invalid command"
        os._exit(2)
    return message

########################################################################

# no parameters => print usage
if len(sys.argv) == 1 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
    printUsage()
else:
    config = makeDefaultConfig()
    message = createMessage(config)
    messageout = connectAndSendMessage(config,message)
    if sys.argv[1] == "status":
        print messageout

