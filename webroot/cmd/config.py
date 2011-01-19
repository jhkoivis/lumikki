## configuration file for controlling the machine



class machines: 
    # target values
    ttm = 0
    ae = 1
    cam = 2
    ir = 3
    # true means that machine is measuring
    # access is through indexing of machine id
    active = (False, False, True, False)


class camera_conf: 
    #defaults 
    PacketSize = '9144'
    XOffset = '0'
    YOffset = '0'
    Width = '1024'
    Height = '768'
    IP = '130.233.203.154'
    Port = '6423'

    # 1024*768*8 bit = 786 432 kilobytes
    # (4+20+8+4+786 432)*9145 = 85.9997813
    # 9145 not possible => 9144
    RawFPS = '117000'

    def __init__(self):
        pass
