
from config import conf
from lumilib import *
from json import loads
import device

def start():
    '''
    Excecute on run click.
    '''
    c = conf()

    filename = "%s-%s" % (c.get('g_measurementid'), c.get('g_timestamp'))

    data = {'stopClock'         : '0',
            'stopCollection'    : '0',
            'filename'          : filename,
            'ClockFrequency'    : '%s' % (c.get('ae_freq')),
            'startClock'        : '1',
            'startCollection'   : '1'}

    return device.labViewCommand('ae', 'start', data)

def stop():
    data = {"startClock"        :"0",
            "startCollection"   :"0",
            "stopClock"         :"1",
            "stopCollection"    :"1"}
    return device.labViewCommand('ae', 'stop', data)

def status():
    return device.labViewCommand('ae', 'status')


