
import os
import time

webroot = os.environ['LUMIKKI_LIGHTTPD_SERVER_ROOT']

os.rename(webroot + '/html/viewer/ttmData.csv', 
          webroot + '/html/viewer/ttmData-%f.csv' % (time.time()))