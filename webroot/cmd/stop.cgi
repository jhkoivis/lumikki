#!/usr/bin/env python

from lib.lumilib import *
from lib import camera
from lib import ttm
from lib.config import conf
from lib.config import staticglobals as mg

commandId=1
try: 
    ## send to all active devices
    jsonMessage = get_json()
    commandId = jsonMessage['id']
    c = conf()
    active = c.get('g_active')
    if active[mg.cam]:
        camera.connectAndSendStop()
    if active[mg.ttm]:
        ttm.connectAndStopLogging()
        ttm.connectAndStop()
    put_json({'st':0, 'id':commandId})
except Exception as e:
    put_json({'id':commandId, 'st':1, 
              'msg':'Stop failed [' + str(e) + ']'})

