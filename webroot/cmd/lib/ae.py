from urllib2 import urlopen, URLError
from urllib import urlencode
from config import conf
from lumilib import *
from json import loads

timeout = 5

def connectToCommand(command, data=None):
    c = conf()
    # TODO: no hardcoded values
    # move ae_service to config.py as variable
    # move vi_basename to config.py as variable
    basic_url = "http://%s:%s/ae_service/vi_basename" % (c.get('ae_ip'),c.get('ae_port'))
    url = basic_url + command
    if data != None:
        # this converts dict to ?key1=value1&key2=value2&...
        url += "?%s" % urlencode(data)
    connection = urlopen(url, timeout=timeout)
    return connection

def connectAndStart():
    c = conf()
    aeValue = "%s" % (c.get('ae_example')) # this is the variable name defined in html
    data = {"ae_server_key_example": aeValue} # this is the variable name defined in device side
    connection = connectToCommand("vi_name_end", data)
    return connectAndGetStatus()

def connectAndGetStatus():
    try:
        connection = connectToCommand("status")
        response = loads(connection.read())
        print response
    except URLError:
        return "110"
    return response['status']
