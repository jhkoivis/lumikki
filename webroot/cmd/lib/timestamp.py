import time
from config import conf

def timestamp():
    c = conf()
    timestamp = time.strftime("%Y%m%d%H%M")
    c.set('g_timestamp', timestamp)

