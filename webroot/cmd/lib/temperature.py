
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

    data = {'temperature_filename'          : filename,
            'temperature_protocol_name'     : '%s' % (c.get('temperature_global_protocol')),
            'temperature_setpoint'          : '%f' % (c.get('temperature_constant_setpoint')),}

    return device.labViewCommandGeneral(c.get('temperature_global_ip'), 
					c.get('temperature_global_port'), 
					c.get('temperature_global_service'),
					'temperature_start',
					data=data)

def stop():
    c = conf()
    return device.labViewCommandGeneral(c.get('temperature_global_ip'), 
					c.get('temperature_global_port'), 
					c.get('temperature_global_service'),
					'temperature_stop')

def status():
    c = conf()
    return device.labViewCommandGeneral(c.get('temperature_global_ip'), 
					c.get('temperature_global_port'), 
					c.get('temperature_global_service'), 
					'temperature_status')


