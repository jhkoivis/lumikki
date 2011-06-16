#!/usr/bin/env python

from lib.lumilib import *
from lib.config import conf, configurationMap

command_id = 1
try: 
    c = conf()
    jsonMessage = get_json()
    command_id = jsonMessage['id']
    
    outFile = open('/tmp/lumikki.log', 'a')
    for key, value in jsonMessage.items():
    	outFile.write(str(key) + str(value))
    outFile.close()
    
    del jsonMessage['id']
    put_json(c.getAndSetCurrent(jsonMessage))

except Exception as e:
    raise
    put_json({'id':command_id, 'st':1, 'msg':'State.cgi failed [' + str(e) + ']'})
