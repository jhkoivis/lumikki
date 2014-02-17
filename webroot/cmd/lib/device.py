from urllib2 import urlopen, URLError
from urllib import urlencode
import httplib, urllib
from config import conf
from lumilib import *
from json import loads
from json import dumps
from base64 import b64encode
import sys

def labViewCommandGeneral(ip, port, service, command, data=None):
    '''
        General connection command for labview devices.

        Connects to a certain ip, port, labview service and 
        labview service command. These variables depend on 
        the device installation (taken from uidefaults.conf).

        Data includes the command (stringyfied to json format)
        posted via http-post.
    '''
    #sys.stderr.write("cam from device.py")
    #sys.stderr.flush()
    c = conf()
    url = "http://%s:%s/%s/%s" % (  ip,
                                    port,
                                    service,
                                    command)
    if data != None:
        url += "?%s" % urlencode(data)
    sys.stderr.write(url)
    sys.stderr.write('\n')
    sys.stderr.flush()
    try:
        connection = urlopen(url, timeout=int(c.get('g_timeout')))
    except:
        sys.stderr.write(url)
        sys.stderr.write('\n')
	sys.stderr.flush()
	raise
    
    # connection must be a string, 
    # urlopen may return a request object if device is not present
    ccn = connection.__class__.__name__
    if ccn == "addinfourl":
	connRead = connection.read()
        try:
		connection = loads(connRead)['statusOut']
	except:
		#print connection
		# no JSON
		sys.stderr.write('\nwarning in device.py -> labviewCommandGeneral: no JSON with statusOut key\n')
                sys.stderr.flush()
		connection = connRead
        	
    elif not (ccn == "str" or ccn == "unicode"):
        connection = '240' # not ready

    return connection

def labViewCommandPostJson(ip, port, service, command, data=None):
    '''
        General connection command for labview devices.

        Connects to a certain ip, port, labview service and 
        labview service command. These variables depend on 
        the device installation (taken from uidefaults.conf).

        Data includes the command (stringyfied to json format)
        posted via http-post.
    '''
    c = conf()
    #url = "http://%s:%s/%s/%s/" % (  ip,
    #                                port,
    #                                service,
    #                                command)
    #if data != None:
    #    url += "?postdata=%s" % b64encode(dumps(data))
    #sys.stderr.write(url)
    ipPort = "%s:%s" % (ip, port)
    serviceCommand = "/%s/%s/" % (service, command)
    sys.stderr.write(ipPort + ' ' + serviceCommand + ' \n')
    sys.stderr.flush()   
 
    #h = urlopen(ipPort)
    params = urllib.urlencode({'postdata': dumps(data)})
    headers = {"Content-type": "application/x-www-form-urlencoded",
               "Accept": "text/plain"}
    conn = httplib.HTTPConnection(ipPort)
    conn.request("POST", serviceCommand, params, headers)
    connection = conn.getresponse().read()

    #connection = h.request('POST', serviceCommand, data)
    
#    try:
#        connection = urlopen(url, timeout=int(c.get('g_timeout')))
#    except:
#        sys.stderr.write(url)
#        raise
     
    # connection must be a string, 
    # urlopen may return a request object if device is not present
#    ccn = connection.__class__.__name__
#    if not (ccn == "str" or ccn == "unicode"):
#        connection = '240' # not ready
    
    sys.stderr.write(connection + '\n')
    sys.stderr.flush()
    return connection

#def labViewCommand(service, command, data=None):
#    '''
#        General connection command for labview devices.
#
#        Connects to a certain ip, port, labview service and 
#        labview service command. These variables depend on 
#        the device installation (taken from uidefaults.conf).
#
#        Data includes the command (stringyfied to json format)
#        posted via http-post.
#    '''
#    c = conf()
#    url = "http://%s:%s/%s/%s" % (  c.get(service + '_ip'),
#                                    c.get(service + '_port'),
#                                    service,
#                                    command)
#    if data != None:
#        url += "?%s" % urlencode(data)
#    sys.stderr.write(url)
#    try:
#        connection = urlopen(url, timeout=int(c.get('g_timeout')))
#    except:
#        sys.stderr.write(url)
#        raise
#     
#    # connection must be a string, 
#    # urlopen may return a request object if device is not present
#    ccn = connection.__class__.__name__
#    if not (ccn == "str" or ccn == "unicode"):
#        connection = '240' # not ready
#    
#    return connection
