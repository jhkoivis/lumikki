from urllib2 import urlopen, URLError
from urllib import urlencode
from config import conf
from lumilib import *
from json import loads


def labViewCommand(service, command, data=None):
    '''
        General connection command for labview devices.

        Connects to a certain ip, port, labview service and 
        labview service command. These variables depend on 
        the device installation (taken from uidefaults.conf).

        Data includes the command (stringyfied to json format)
        posted via http-post.
    '''
    c = conf()
    basic_url = "http://%s:%s/%s/%s" % (c.get(service + '_ip'),
                                        c.get(service + '_port'),
                                        service,
                                        command)
    if data != None:
        url += "?%s" % urlencode(data)
    connection = urlopen(url, timeout=c.conf())
    return connection

