

# import graph generators
# this has to be first
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as pylab
import StringIO
import numpy

# import predicter
# This has to be after viewer matplotlib.use()
from viewerMakePrediction import makePredictionFigure

# imports for creating image string with base64 encoding
from urllib import quote        as urllib_quote
from base64 import b64encode    as base64_b64encode

# import environment variables
from os import environ as os_environ
webroot = os_environ['LUMIKKI_LIGHTTPD_SERVER_ROOT']

# add config to pythonpath
import sys
sys.path.append(webroot + '/cmd/lib')

# import configuration
from config import conf

c = conf()

def getTtmOnlineDataAsNumpyArray():
    '''
        Load ttm data as numpy array
    '''
    ttmDataPath = c.get('viewer_ttmDataPath')
    return numpy.loadtxt(webroot + ttmDataPath)

def makeFigure(ttmOnlineData):
    '''
        Make simple figure
    '''
    pylab.figure()

    pylab.subplot(3,1,1)
    pylab.plot(ttmOnlineData[:,0], ttmOnlineData[:,1])
    pylab.xlabel('Time in samples [1/500 s]')
    pylab.ylabel('Analog disp. [mm]')

    pylab.subplot(3,1,2)
    pylab.plot(ttmOnlineData[:,0], ttmOnlineData[:,1])
    pylab.xlabel('Time in samples [1/500 s]')
    pylab.ylabel('Force [kN]')

    pylab.subplot(3,1,3)
    pylab.plot(ttmOnlineData[:,0], ttmOnlineData[:,2])
    pylab.xlabel('Time in samples [1/500 s]')
    pylab.ylabel('Digital disp. [mm]')

    imageFile = StringIO.StringIO()
    pylab.savefig(imageFile, format= "png")
    imageFile.seek(0)
    
    return imageFile

def printFigure(file):
    """
    print png figure as html to stdout
    """
    uri = 'data:image/png;base64,' 
    uri += urllib_quote(base64_b64encode(imageFile.buf))
    print '<img src = "%s"/>' % uri

ttmOnlineData = getTtmOnlineDataAsNumpyArray()
#imageFile = makeFigure(ttmOnlineData)
imageFile = makePredictionFigure(ttmOnlineData[:,0],  
                                 ttmOnlineData[:,-1])
printFigure(imageFile)





