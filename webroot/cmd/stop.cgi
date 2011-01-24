#!/usr/bin/env python

from lumilib import *
import camera

commandId=1
try: 
    ## send to all active devices
    jsonMessage = get_json()
    commandId = jsonMessage['id']
    camera.connectAndSendStop()
    put_json({'st':0, 'id':commandId})
except Exception as e:
    put_json({'id':commandId, 'st':1, 
              'msg':'Stop failed [' + str(e) + ']'})

