import memcache

# TODO: load configuration map from a file

configurationMap = {'g_logdir'        : '~'
    , 'g_memcacheAddr'	: '127.0.0.1:38339'
    , 'g_active':[False, False, False, False]
    , 'g_measurementid'     : 'default'
    , 'g_timestamp'     : ''
    , 'cam_parentfolder' : r'F:\data'
    , 'cam_packetsize' : '9144'
    , 'cam_xoffset' : '0'
    , 'cam_yoffset' : '0'
    , 'cam_width' : '1024'
    , 'cam_height' : '768'
    , 'cam_ip': '130.233.203.154'
    , 'cam_port' : "6423"
    , 'cam_exposure' : '300'
    , 'cam_rawfps' : '1000'
    , 'cam_index' : '0'
    , 'ttm_ramprate' : '0.2'
    , 'ttm_rampamplitude' : '2'
    , 'ttm_setpoint' : '1'
    , 'ttm_setpointtime' : '1'
    , 'ttm_ip' : '10.0.0.10'
    , 'ttm_port' : '80'
    , 'ttm_load' : '0.0'
    , 'ttm_creep_experiment' : False
    , 'ttm_protocol' : 'aecontrol'
    , 'ttm_ramprateae' : '0'
    , 'ttm_rampratesilent' : '0.01'
    , 'ttm_window' : '50'
    , 'ttm_channel' : '1'
    , 'ttm_cyclelength' : '10'
    , 'ttm_holdtime' : '10'
    , 'ir_framerate' : '30'
    , 'ir_recordtime' : '1.0'
    , 'ir_filename' : 'irpicture'
    , 'ir_ip' : '10.0.0.30'
    , 'ir_port' : '81'
    , 'ir_parentfolder' : r'D:\irimages'
    , 'ir_storecondition' : '1'
    , 'ir_stopcondition' : '2'
    , 'ir_startcondition' : '2'
    , 'ir_startvalue' : '0'
    , 'ir_storevalue' : '0'
    , 'ir_recordformat' : '2'
    , 'ir_trigsource' : '0'
    , 'ir_autoshutter' : '0'
    , 'ir_triggerexperiment' : '1'
    , 'ae_ip' : '10.0.0.40'
    , 'ae_port' : '80'
    , 'ae_freq' : '2000000'
    , 'ae_service' : 'aewebservice'
    , 'ae_viname' : 'gateway'
}

class conf:
    def __init__(self):
        self.mc = memcache.Client([configurationMap['g_memcacheAddr']], debug=0)

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


