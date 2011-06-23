#!/usr/bin/env python


from lib.lumilib import *
from lib.timestamp import timestamp
from lib.config import conf
from lib.config import staticglobals as mg

try:
    c = conf()
    jsonMessage = get_json()
    commandId = jsonMessage['id']
    msg = ''
    ret = timestamp()
    msg = "Timestamp: " + ret
    put_json({'st':0, 'id':commandId, 'msg':msg})
except Exception as e:
    put_json({'id':commandId, 'st':1, 
              'msg':'Timestamp failed [' + str(e) + ']'})
