## configuration file for controlling the machine
import memcache

class conf:
    def __init__(self):
        self.mc = memcache.Client(['127.0.0.1:11211'], debug=0)

    def getCurrent(self):
        retDict = dict()
        for key in configurationMap: 
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

## static global configuration, which should not change ever
class staticglobals: 
    # target values
    ttm = 0
    ae = 1
    cam = 2
    ir = 3

configurationMap = {
    'g:active':[False, False, True, False]
    , 'g:measurement_id'     : 'default'
    , 'cam:packetsize' : '9144'
    , 'cam:xoffset' : '0'
    , 'cam:yoffset' : '0'
    , 'cam:width' : '1024'
    , 'cam:height' : '768'
    , 'cam:ip': '130.233.203.154'
    , 'cam:port' : 6423
    , 'cam:exposure' : '300'
    , 'cam:rawfps' : '117000'
}
