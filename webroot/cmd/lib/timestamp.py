import time
from config import conf

def stampID():
    c = conf()
    measurement_id = c.get('g_measurementid')
    timestamp_id = measurement_id + time.strftime("%Y%m%d%H%M")
    c.set('g_measurementidunique', timestamp_id)

