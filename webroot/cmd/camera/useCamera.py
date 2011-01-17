# Use the camera through Labview
# 
# Jani Saarenpaa. TKK summer 2009.
# 
# Self taught python user. So, don't except the right rutines or good coding
# habits.
# TODO: make this a class and define a use camera function or something
#
# import the LabVIEW.py which you must have
import LabVIEW
import sys
import string
import os
import getpass # to get the user name
import datetime # to get the date
import ConfigParser
import time # to get some sleep

# python + \ = HELL
# import ntpath
# Labview makes the file path now


if len(sys.argv) == 1 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
# Not enough minera... arguments
    print "1) Usage: python " + sys.argv[0] + " start [test number] (optional: test name)"
    print "To start the camera. Note: you have less problems if you do not use characters " \
            + "like \'%\' or \'.\' in the test name."
    print "2) Usage: python " + sys.argv[0] + " stop"
    print "To stop the camera and lifts the lift"
    print "3) Usage: python " + sys.argv[0] + " status"
    print "To have it print the status of Windows machine"
    print "4) Usage: python " + sys.argv[0] + " change"
    print "Changes the camera's parameters to CHANGE parameters"
    print "5) Usage: python " + sys.argv[0] + " cycle up/down"
    print "You can raise the lift and stop taking photos."
    print "You should see " + sys.argv[0] + ".conf file for any need for change."
else:
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

    config.add_section('CHANGE')

    config.set('CHANGE', 'RawFPS'    , '1000') # 1000 = 1 sec
    config.set('CHANGE', 'PacketSize', '9144')
    config.set('CHANGE', 'XOffset'   , '0')
    config.set('CHANGE', 'YOffset'   , '0')
    config.set('CHANGE', 'Width'     , '1024')
    config.set('CHANGE', 'Height'    , '768')
    config.set('CHANGE', 'IP'        , '130.233.203.154')
    config.set('CHANGE', 'Port'      , '6423')


    if not config.read(os.path.abspath(sys.argv[0]) + '.conf'): 
#
# Oh, the default gets written to the configuration file. So, this is not needed
#
#        config.add_section('Settings') 
#        i = 0
#        while i < len(config.items('DEFAULT')):
#            config.set('Settings', \
#                    config.items('DEFAULT')[i][0], \
#                    config.get('DEFAULT', config.items('DEFAULT')[i][0],1))
#            i += 1
#
# .... python 2.4 doesn't "with" statement...
# with open('example.cfg', 'wb') as configfile:
        try:
            fileHandle = open(os.path.abspath(sys.argv[0]) + ".conf", 'w')
        except IOError:
            print "Error while opening conf file " \
                   + os.path.abspath(sys.argv[0]) + ".conf."
            # fileHandle.close()
            os._exit(2)
        config.write(fileHandle)
        fileHandle.close()



# Make the string to send
# START
    if sys.argv[1] == "start":
# It seems to be simpler to have predetermined locations for the data
    # Turn that slash
        #realPath = ntpath.normpath(sys.argv[9])
    # For some reason normpath forgots the last backslash
        #if (1 + string.rfind(sys.argv[9],'/')) == len(sys.argv[9]):
        #    realPath = realPath + "\\"
        try:
            testName = sys.argv[3] #+ datetime.date.today().strftime("%y%m%d")
        except IndexError:
            testName = "" #datetime.date.today().strftime("%y%m%d")

        try:
            string.atoi(sys.argv[2])
            if len(sys.argv[2]) > 2: # this might be more elegant
                testName = testName + "0"     # with string.size()
        except ValueError:
            print "ERROR: check that the test number is a number"
            os._exit(2)
        testName = testName + sys.argv[2]
        testName = testName + datetime.date.today().strftime("%y%m%d")

        message = "M(1)S(" + config.get('DEFAULT', "PacketSize") + \
                     ")F(" + config.get('DEFAULT', "RawFPS"    ) + \
                     ")U(" + getpass.getuser()                   + \
                     ")W(" + config.get('DEFAULT', "Width"     ) + \
                     ")H(" + config.get('DEFAULT', "Height"    ) + \
                     ")X(" + config.get('DEFAULT', "XOffset"   ) + \
                     ")Y(" + config.get('DEFAULT', "YOffset"   ) + \
                     ")T(" + testName                            + \
                     ")I(" + "0"                                 +")"
# I = index
# Barack Obama
    elif sys.argv[1] == "change":

        message = "M(3)S(" + config.get('CHANGE', "PacketSize" ) + \
                     ")F(" + config.get('CHANGE', "RawFPS"     ) + \
                     ")U(" + getpass.getuser()                   + \
                     ")W(" + config.get('CHANGE', "Width"      ) + \
                     ")H(" + config.get('CHANGE', "Height"     ) + \
                     ")X(" + config.get('CHANGE', "XOffset"    ) + \
                     ")Y(" + config.get('CHANGE', "YOffset"    ) +")"
# Cycle = lift up:
    elif sys.argv[1] == "cycle":
        if len(sys.argv) < 3:
            print 'cycle needs an argument that states either up or down.'
        else:
            if sys.argv[2] == "up":
                message = "M(4)"
            elif sys.argv[2] == "down":
                message = "M(5)"
# STOP
    elif sys.argv[1] == "stop":
        message = "M(2)"
# STATUS REPORT
    elif sys.argv[1] == "status":
        # seems that it doesn't work for some reason if there is no text. There is no end
        # to the sending phase and timeout cuts the connection.
        message = "status?"
    else:
        print "ERROR: Invalid command"
        os._exit(2)

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
    if sys.argv[1] == "status":
        print messageout

# Where "M(1)" tells that this the Message that the machine waiting
# "S()"  is packet Size that the camera sends the images
# "F()" is the FPS
# "P()" is the file path where the pictures should be saved in the camera computer. You need to
# have "\\" insted of "\" to get the python send the right command. In our example  the files will be
# saved at "F:\test\newTest1002253174873.tiff". The number indicates the time it is taken. Read
# more in CameraShoot.vi
# "W()" is the Width of the picture
# "H()" is the Height of the picture
# "X()" is the offset in widht
# "Y()" is the offset in height
# "U()" is the curren user
# "T()" is the test name

# To be fair disconnect:
    LabVIEW.disconnect()
    

