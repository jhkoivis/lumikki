#!/usr/bin/python

from lumilib import *
import camera
from config import conf
from config import staticglobals as mg

command_id = 1
try: 
    ## send to all active devices
    c = conf()
    msg = ''
    json_message = get_json()
    command_id = json_message['id']
    active = c.get('g:active')
    log("activity" + str(active))
    if active[mg.cam]:
        log("Camera connect and send")
        ret = camera.connectAndSendStart(json_message)
        log("returned")
        msg = msg + "Cam: " + ret
    put_json({'st':0, 'id':command_id, 'msg':'Success: ' + msg})
except Exception as e:
    put_json({'id':command_id, 'st':1, 
              'msg':'Run failed [' + str(e) + ']'})
    
