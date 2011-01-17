#!/usr/bin/python

from lumilib import * 

jso = get_json()
target = jso['target']
id = jso['id']
log('status.cgi::' + str(target) + '::' + str(id))
if target != 2: 
    put_json({'status':'100', 'id':id, 'target':target})
else: 
    put_json({'status':'200', 'id':id, 'target':target})



