#!/usr/bin/env python

from lib.lumilib import *
from lib import ir
from lib.config import conf
from lib.config import staticglobals as mg

try:
    c = conf()
    jsonMessage = get_json()
    commandId = jsonMessage['id']
    active = c.get('g_active')
    msg = ''
    if active[mg.ir]:
        ret = ir.connectAndConnectIR()
        msg = "IR: " + str(ret)
        put_json({'st':0, 'id':commandId, 'msg':'Success: ' + msg})
except Exception as e:
    put_json({'id':commandId, 'st':1, 
              'msg':'Run failed [' + str(e) + ']'})
