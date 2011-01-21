#!/usr/bin/env python

from lumilib import *
from config import conf, configurationMap

command_id = 1
try: 
    c = conf()
    json_message = get_json()
    command_id = json_message['id']
    put_json(c.getCurrent())
except Exception as e:
    put_json({'id':command_id, 'st':1, 
              'msg':'Run failed [' + str(e) + ']'})
