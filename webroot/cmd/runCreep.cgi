#!/usr/bin/env python

from lib.lumilib import *
from lib import camera
from lib import ttm
from lib.config import conf
from lib.config import staticglobals as mg
from lib.timestamp import timestamp
from lib import ir

commandId = 1
try: 
    ## send to all active devices
    c = conf()
    msg = ''
    jsonMessage = get_json()
    commandId = jsonMessage['id']
    measurementid = jsonMessage['g_measurementid']
    if measurementid: 
        c.set('g_measurementid', measurementid)
    else: 
        raise ValueError("No measurement ID set.")
    active = c.get('g_active')
    log("active array: " + str(active))
    if active[mg.cam]:
        log("Camera connect and send")
        ret = camera.connectAndSendStart()
        msg = msg + "Cam: " + ret
    if active[mg.ttm]:
        log("TTM connect and send")
        #ret = ttm.connectAndInitRamp()
        ret = ttm.connectAndStartLogging()
        #ret = ttm.connectAndStartRamp()
        ttm.connectAndStartCreep()
	msg = msg + "TTM: " + str(ret)
    if active[mg.ir]:
        ir.connectAndSendSettings()
        ret = ir.connectAndGetImageSeries()
        msg = "IR: " + ret
        put_json({'st':0, 'id':commandId, 'msg':'Success: ' + msg})
    put_json({'st':0, 'id':commandId, 'msg':'Success: ' + msg})
except Exception as e:
    put_json({'id':commandId, 'st':1, 
              'msg':'Run failed [' + str(e) + ']'})
    
