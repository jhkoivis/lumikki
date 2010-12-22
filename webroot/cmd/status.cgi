#!/usr/bin/python

from lumilib import * 

jso = getjson()
target = jso['target']
id = jso['id']
log('status.cgi::' + str(target) + '::' + str(id))
putjson({'status':'200', 'id':id, 'target':target})

