#!/usr/bin/env python

from lib.lumilib import *
from lib.config import conf, configurationMap

command_id = 1
try: 
    c = conf()
    jsonMessage = get_json()
    command_id = jsonMessage['id']
    del jsonMessage['id']
    put_json(c.getAndSetCurrent(jsonMessage))
except Exception as e:
    raise
    put_json({'id':command_id, 'st':1, 'msg':'State.cgi failed [' + str(e) + ']'})
