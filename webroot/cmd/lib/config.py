import memcache
import os
import sys
from xml.sax import make_parser
from variableXmlContentHandler import variableXmlContentHandler

def loadConfigurationMap():
    """
        loads configuration map from 
        os.environ['LUMIKKI_PYTHON_UIDEFAULTS']
    """
    configurationMap = {}
    fn = os.environ['LUMIKKI_PYTHON_UIDEFAULTS']
    #fn = '../../html/variables.xml'
    
    parser = make_parser() 
    curHandler = variableXmlContentHandler(configurationMap)
    parser.setContentHandler(curHandler) 
    parser.parse(open(fn,'r'))
    #print configDict

    configurationMap['g_active'] = [False, False, False, False, False]

    return configurationMap

configurationMap = loadConfigurationMap()

class conf:
    def __init__(self):
        ip = os.environ['LUMIKKI_MEMCACHE_IP']
        port = os.environ['LUMIKKI_MEMCACHE_PORT']
        memcacheAddr = ['%s:%s' % (ip, port)]
        try:
            self.mc = memcache.Client(memcacheAddr, debug=0)
        except TypeError:
            sys.stderr.write('Memcache init failed with: %s' % (memcacheAddr))  
            raise

    def getAndSetCurrent(self, inputMap):
        retDict = dict()
        for key in configurationMap: 
            inKeys = inputMap.keys()
            if key in inKeys:
                self.set(key, inputMap[key])
            retDict[key] = self.get(key)
        return retDict

    def get(self, key):
        value = self.mc.get(key)
        if not value: 
            svalue = configurationMap[key]
            if svalue:
                self.mc.set(key,svalue)
            return svalue
        else:
            return value

    def set(self, key, value):
        self.mc.set(key,value)

    def getAllKeys(self):
        keys = configurationMap.keys()
        return keys

class staticglobals: 
    ttm = 0
    ae = 1
    cam = 2
    ir = 3
    temperature = 4


