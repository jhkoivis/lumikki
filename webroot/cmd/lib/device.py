from urllib2 import urlopen, URLError
from urllib import urlencode
from config import conf
from lumilib import *
from json import loads
import sys


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
    url = "http://%s:%s/%s/%s" % (  c.get(service + '_ip'),
                                    c.get(service + '_port'),
                                    service,
                                    command)
    if data != None:
        url += "?%s" % urlencode(data)
    try:
        connection = urlopen(url, timeout=int(c.get('g_timeout')))
    except:
        sys.stderr.write(url)
        raise
     
    # connection must be a string, 
    # urlopen may return a request object if device is not present
    ccn = connection.__class__.__name__
    if not (ccn == "str" or ccn == "unicode"):
        connection = '240' # not ready
    
    return connection

