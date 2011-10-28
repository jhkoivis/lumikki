from config import conf
import device

def start():
    '''
    Excecute on run click.
    '''
    c = conf()
    
    data = {'testname':    "%s-%s" % (c.get('g_timestamp'), c.get('g_measurementid'))}
    variables =  [  'rawfps', 'exposure', 'offsetx', 'offsety',
                    'packetsize', 'width', 'height',
                    'parentfolder', 'index']
    for var in variables:
        key = var
        configKey = 'cam_' + key
        data[key] = c.get(configKey)

    return device.labViewCommand('cam', 'cam_start', data)

def stop():
    return device.labViewCommand('cam', 'cam_stop')

def status():
    return device.labViewCommand('cam', 'cam_status')
