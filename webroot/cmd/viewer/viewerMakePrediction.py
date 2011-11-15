
# plotting tools
# assume that matplotlib.use('Agg') is already called
import matplotlib.pyplot as pylab
import numpy
import StringIO

# get environment variables
from os import environ as os_environ
webroot = os_environ['LUMIKKI_LIGHTTPD_SERVER_ROOT']

# get config
import sys
sys.path.append(webroot + '/cmd/lib')
from config import conf

# get experiment parser
from expParser import ExpParser

def makePredictionFigure(time, displacement):
    
    #######################################
    # Do the actual calculations
    #######################################
    x = time
    y = displacement
    
    e = ExpParser()
    c = conf()
    
    t, sr = e.getTimeStrainRate(x,y)
        
    startTime, startStrainRate = e.getStartTimeAndStrainRate(t,sr)
    endTime, endTimeStrainRate = e.getEndTimeAndEndStrainRate(t,sr)
    transientTime, transientStrainRate, err, err2 = e.getTransientTime(t,sr) 

    lifeTime = e.getLifeTime(t,sr)
  
    realLifeTime = float(c.get('viewer_realLifeTime'))
  
    ##################################################
    # plot data
    ##################################################

    pylab.plot(t,sr, '-o') # all data
    pylab.plot(startTime, startStrainRate, 'ro') # start time
    pylab.plot(transientTime, transientStrainRate, 'gs') # transient time
    pylab.plot(lifeTime + startTime, startStrainRate, 
               'kv', label = 'lifeTime: %f' % (lifeTime)) # predicted time
    pylab.plot(realLifeTime + startTime, startStrainRate, 
               'm^', label = 'realLifeTime: %f' % (realLifeTime)) # real life time (if available)
    
    pylab.gca().set_ylim([0, startStrainRate*1.2])
    pylab.xlabel('Time [s]')
    pylab.ylabel('Strainrate [mm/s]')
    pylab.legend(loc= 'upper center')
    
    # write file
    imageFile = StringIO.StringIO()
    pylab.savefig(imageFile, format= "png")
    imageFile.seek(0)
    
    ####################################################
    # save to log file what we are predicted
    ####################################################
 
    webroot = os_environ['LUMIKKI_LIGHTTPD_SERVER_ROOT']
    predLogFn = c.get('viewer_predictionLogFileName').replace("'","") # there is an extra '
    dataFile = open(webroot + predLogFn, 'a')
    dataFile.write('%s %f %f\n' % (c.get('viewer_expId'), 
                                   lifeTime,
                                   float(c.get('viewer_realLifeTime'))))
    dataFile.close()
    
    return imageFile
    
