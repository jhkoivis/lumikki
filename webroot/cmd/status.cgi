#!/usr/bin/python

from lumilib import * 
from config import camera_conf, machines
import sys

try: 
    jso = get_json()
    target = jso['target']
    id = jso['id']
    log('status.cgi::' + str(target) + '::' + str(id))
    ## TODO, clean
    if not machines.active[target]:
        put_json({'status':'100', 'id':id, 'target':target})
    elif target == machines.ttm: 
        put_json({'status':'122', 'id':id, 'target':target})
    elif target == machines.ae: 
        put_json({'status':'122', 'id':id, 'target':target})
    elif target == machines.cam: 
        put_json({'status':'122', 'id':id, 'target':target})
    elif target == machines.ir:     
        put_json({'status':'122', 'id':id, 'target':target})
    else: 
        put_json({'status':'120', 'id':id, 'target':target})

except Exception as e: 
    put_json({'status':'120', 'msg':'status.cgi failed: ' + e.value})




