
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

    return device.labViewCommandGeneral(c.get('ae_ip'), 
					c.get('ae_port'), 
					c.get('ae_service'),
					'ae_start',
					data=data)

def stop():
    c = conf()
    data = {"startClock"        :"0",
            "startCollection"   :"0",
            "stopClock"         :"1",
            "stopCollection"    :"1"}
    return device.labViewCommandGeneral(c.get('ae_ip'), 
					c.get('ae_port'), 
					c.get('ae_service'),
					'ae_stop',
					data=data)

def status():
    c = conf()
    sys.stderr.write("status from ae.py\n")
    sys.stderr.write("ae_ip: %s\n" % (c.get('ae_ip')))
    sys.stderr.write("ae_port: %s\n" % (c.get('ae_port')))
    sys.stderr.write("ae_service: %s\n" % (c.get('ae_service')))
#    try:
#	from urllib2 import urlopen
#        connection = urlopen('http://10.0.0.40/ae/ae_status', timeout=int(c.get('g_timeout')))
#        sys.stderr.write('status from ae.py: %s' % (connection))
#    except:
#        sys.stderr.write('error')
#        raise

    return device.labViewCommandGeneral(c.get('ae_ip'), 
					c.get('ae_port'), 
					c.get('ae_service'), 
					'ae_status')


