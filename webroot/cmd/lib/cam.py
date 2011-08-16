from config import conf
import device

def start():
    '''
    Excecute on run click.
    '''
    c = conf()
    
    data = {'measurementid':    c.get('g_measurementid')}
    variables =  [  'fps', 'exposure', 'offsetx', 'offsety',
                    'packetsize', 'width', 'height',
                    'parentfolder', 'index']
    for var in variables:
        key = var
        configKey = 'cam_' + key
        data[key] = c.get(configKey)

    return device.labViewCommand('cam', 'start', data)

def stop():
    return device.labViewCommand('cam', 'stop')

def status():
    return device.labViewCommand('cam', 'status')
