#!/usr/bin/env python

from lib.lumilib import *
from lib import cam
from lib import ttm
from lib import ir
from lib import ae
from lib.config import conf
from lib.config import staticglobals as mg
from lib.timestamp import timestamp

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
        log("CAM start")
        ret = cam.start()
        msg = msg + "Cam: " + ret
        
    if active[mg.ttm]:
        log("TTM connect and send")
        ret = ttm.connectAndInitRamp()
        ret = ttm.connectAndStartLogging()
        ret = ttm.connectAndStartRamp()
        msg = msg + "TTM: " + str(ret)
        
    if active[mg.ae]:
        log("AE connect and send")
        ret = ae.connectAndStart()
        msg = msg + "AE: " + str(ret)
        
    if active[mg.ir]:
        log("IR connect and send")
        ret = ir.connectAndStart()
        msg = "IR: " + str(ret)
        
    put_json({'st':0, 'id':commandId, 'msg':'Success: ' + msg})
    
except Exception as e:
    put_json({'id':commandId, 'st':1, 'msg':'Run failed [' + str(e) + ']'})
    raise
    
