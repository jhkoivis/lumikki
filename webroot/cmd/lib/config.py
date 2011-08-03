import memcache
import os
import sys

def loadConfigurationMap():
    """
        loads configuration map from 
        os.environ['LUMIKKI_PYTHON_UIDEFAULTS']
    """
    configurationMap = {}
    fn = os.environ['LUMIKKI_PYTHON_UIDEFAULTS']
    for line in open(fn, 'r'): 
        line = line.strip() 
        if len(line) <= 1: continue
        if line[0] == '#': continue

        key = eval(line.split('=')[0].strip())
        #print key
        value = eval(line.split('=')[1].strip())
        #print value

        configurationMap[key] = value

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

class staticglobals: 
    ttm = 0
    ae = 1
    cam = 2
    ir = 3


