import urllib2 as url
from urllib import urlencode
from config import conf
from lumilib import *

timeout = 3

def connectAndSendStart():
    c = conf()
    url = "%s:%s/ttmStart" % (c.get('ttm_ip'),c.get('ttm_port'))
    connect(url)
    
def connectAndSendStop():
    c = conf()
    url = "%s:%s/ttmStop" % (c.get('ttm_ip'),c.get('ttm_port'))
    connect(url)
    
def connectAndSetRamp():
    c = conf()
    url = "%s:%s/ttmStop" % (c.get('ttm_ip'),c.get('ttm_port'))
    data = { rampRate:      c.get('ttm_ramprate')
            ,rampHeight:    c.get('ttm_rampheight')
            ,channel:       c.get('ttm_channel')
            }
    connectAndSendData(url, data)
    
def connect(url):
    try:
        return "%s" % url.urlopen(url,timeout=3).getcode()
    except IOError:
        return "110"
    
def connectAndSendData(url, data):
    urldata = urlencode(data)
    try:
        return "%s" % url.urlopen(url,data=data,timeout=3).getcode()
    except IOError:
        return "110"
        