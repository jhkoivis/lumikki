#!/usr/bin/python

from lumilib import *
import camera
from config import camera_conf, machines

try: 
    ## send to all active devices
    msg = ''
    json_message = get_json()
    command_id = json_message['id']
    if machines.active[machines.cam]:
        ret = camera.connectAndSend(jsonMessage)
        msg = msg + "Cam: " + ret
    put_json({'st':0, 'msg':'Success: ' + msg})
except Exception as e:
    put_json({'st':1, 'msg':'run.cgi raised an exception with value: ' + e.value+ ' Msg: ' + msg})
    
