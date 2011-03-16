

#!/usr/bin/env python

from lumilib import *
import ttm
import ir
from config import conf
from config import staticglobals as mg
import sys

try:
    c = conf()
    jso = get_json()
    target = jso['target']
    id = jso['id']
    log('status.cgi::' + str(target) + '::' + str(id))
    active = c.get('g_active')
    if not active[target]:
        put_json({'status':'100', 'id':id, 'target':target})
    elif target == mg.ttm: 
    	status = ttm.connectAndGetStatus()
        put_json({'status':status, 'id':id, 'target':target})
    elif target == mg.ae: 
        put_json({'status':'122', 'id':id, 'target':target})
    elif target == mg.cam: 
        put_json({'status':'122', 'id':id, 'target':target})
    elif target == mg.ir:
        status, jsonmsg = ir.connectAndGetStatus()
        put_json({'status':status, 'id':id, 'target':target})
    else: 
        put_json({'status':'120', 'id':id, 'target':target})

except Exception as e: 
    put_json({'status':'120', 'msg':'status.cgi failed: ' + str(e)})




