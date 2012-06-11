

#!/usr/bin/env python

from lib.lumilib import *
from lib import ir
from lib import ttm
from lib import cam
from lib import ae
from lib import temperature
from lib.config import conf
from lib.config import staticglobals as mg
import sys

try:
    c = conf()
    jso = get_json()
    target = jso['target']
    id = jso['id']
    log('status.cgi::' + str(target) + '::' + str(id))
    active = c.get('g_active')
    
    if not active[target]: 	status = '100'
    elif target == mg.ttm: 	status = ttm.connectAndGetStatus()
    elif target == mg.ae:  	status = ae.status()
    elif target == mg.cam: 	status = cam.status()
    elif target == mg.ir:  	status = ir.connectAndGetStatus()
    elif target == mg.temperature:  status = temperature.status()
    else: 					status = '120'
    
    put_json({'status':status, 'id':id, 'target':target})

except Exception as e: 
    put_json({'status':'120', 'msg':'status.cgi failed: ' + str(e)})
    raise



