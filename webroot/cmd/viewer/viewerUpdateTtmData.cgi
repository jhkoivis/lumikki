
import json
import os
import sys
webroot = os.environ['LUMIKKI_LIGHTTPD_SERVER_ROOT']
sys.path.append(webroot + '/cmd/lib')
from config import conf

def writeData(jsonData):
    """
        XXX: This has to be fixed. We need timestamped data
        with 10 Hz sample rate. Depends on labview.
    """
    
    c = conf()
                        
    outFile = open(webroot + c.get('viewer_ttmDataPath'), 'a')
    asd = jsonData['analogStrain']
    sd = jsonData['stress']
    dsd = jsonData['digitalStrain']
    time = jsonData['time']
    for i in range(len(asd)):
        outFile.write('%f %f %f %f\n' % 
                      (time[0], asd[i], sd[i], dsd[i]))
    outFile.close()
    
    
    c.set('viewer_expId', jsonData['viewer_expId'])
    c.set('viewer_realLifeTime', jsonData['viewer_realLifeTime'])
    
data = sys.stdin.read()
sys.stderr.write(data)
data = json.loads(data)
writeData(data)
