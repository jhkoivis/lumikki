
from config import conf
from lumilib import *
from json import loads
from json import dumps
import device

def start():
    '''
    Excecute on run click.
    '''
    c = conf()
    keyList = c.getAllKeys()
    keyList.sort()
    data = {}
    
    for key in keyList:
        sys.stderr.write(str(key[0:5])+ '\n')
        if (key[0:2] == 'g_') or (key[0:4] == 'cam_'):
            # lists and objects are not implemented in labview part
            # ',' and ':' are thus forbidden
            value = str(c.get(key))
            if ',' in dumps(value): continue
            if ':' in dumps(value): continue
            if value.__class__ == [].__class__: continue
            data[key] = value

    return device.labViewCommandPostJson(c.get('cam_global_ip'),
                                        c.get('cam_global_port'),
                                        c.get('cam_global_service'),
                                        'cam_start',
                                        data=data)

def stop():
    c = conf()
    return device.labViewCommandGeneral(c.get('cam_global_ip'), 
                    c.get('cam_global_port'), 
                    c.get('cam_global_service'),
                    'cam_stop')

def status():
    c = conf()
    return device.labViewCommandGeneral(c.get('cam_global_ip'), 
                                        c.get('cam_global_port'),
                                        c.get('cam_global_service'), 
                                        'cam_status')

