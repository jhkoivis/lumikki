#!/usr/bin/python

from lumilib import * 
from config import camera_conf, machines
import sys

try: 
    jso = get_json()
    target = jso['target']
    id = jso['id']
except: 
    put_json({'status':'120', 'msg':'status: malformed command, could no parse JSON'})
    sys.exit(0)
    

log('status.cgi::' + str(target) + '::' + str(id))

if not machines.active[target]:
    put_json({'status':'100', 'id':id, 'target':target})
elif target == machines.ttm: 
    #TODO
    put_json({'status':'122', 'id':id, 'target':target})
elif target == machines.ae: 
    #TODO
    put_json({'status':'122', 'id':id, 'target':target})
elif target == machines.cam: 
    #TODO
    put_json({'status':'122', 'id':id, 'target':target})
elif target == machines.ir:     
    #TODO
    put_json({'status':'122', 'id':id, 'target':target})
else: 
    put_json({'status':'120', 'id':id, 'target':target})



