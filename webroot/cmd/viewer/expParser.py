
import numpy

class ExpParser:
    
    def __init__(self):
        self.startEndDiv = 0.5
        pass
    
    def getStartTimeAndStrainRate(self, time, strainrate, timeStart = 5, timeEnd = 20):
        """
            timeStart: startTime has to be after this (in sec)
            timeEnd : startTime has to be before this time (in sec)
        """
        indices = time < timeEnd
        indices *= time > timeStart
        t = time[indices]
        sr = strainrate[indices]
        index = numpy.argmax(sr)
        return t[index], sr[index]
    
    
    def getEndTimeAndEndStrainRate(self, time, strainrate):
        
        startTime, startStrainRate = self.getStartTimeAndStrainRate(time, strainrate)
        try:    
            t = time[len(time)*self.startEndDiv:]
            sr = strainrate[len(strainrate)*self.startEndDiv:]
            endTime = t[sr > startStrainRate][0]
            endStrainRate = sr[sr > startStrainRate][0]
        except:
            return startTime, 0 
        return endTime, endStrainRate
    
    def getAndradeFit(self, time, strainRate):
        startTime, startStrainRate = self.getStartTimeAndStrainRate(time, strainRate)
        
        x = time - startTime
        y = numpy.power(x,-0.666)
        y2 = strainRate
        y2At0 = numpy.interp([1], x, y2, 1)
        y *= y2At0
        
        return x + startTime,y
    
     
    def getTransientTime(self, time, strainRate):
        andradeTime, andradeStrainRate = self.getAndradeFit(time, strainRate)
        startTime, startStrainRate = self.getStartTimeAndStrainRate(time, strainRate)
        
        error = strainRate/andradeStrainRate - 1.0
        
        error2 = numpy.zeros(error.shape)
        error2[numpy.abs(error) >= 0] = error[numpy.abs(error) >= 0] 
        errorTime = time
        
        index = range(len(error2)) 
        index = numpy.array(index)
        boolean1 = errorTime > (startTime + 1.0)
        boolean2 = numpy.abs(error2) > 0.1
        index = index[boolean1 * boolean2][0]
        
        return time[index], strainRate[index], errorTime, error2
        
      
    def getTimeStrainRate(self, time, displacement, lag = 0.1, sampleLength = 1.0):
        """
            Lag is given in seconds.
            derivate with backward lag.
        """
        x = numpy.arange(time[0], time[-1], lag)
        y = numpy.interp(x, time, displacement, 2) # 2 means average
        
        strainRatePre = ((y[1:] - y[:-1])/1.0)/sampleLength
        newTime = x[:-1]
        
        x = numpy.arange(newTime[0], newTime[-1], 0.01)
        strainRate = numpy.interp(x, newTime, strainRatePre, 2)
        
        newTime = x - x[0]

        return newTime, strainRate
    
    def getLifeTime(self, time, strainRate):
        startTime, startStrainRate  = self.getStartTimeAndStrainRate(time, strainRate)
        transientTime, transientStrainRate, errorTime, error2 = self.getTransientTime(time, strainRate)
        lifeTime = 6.7*numpy.exp(transientTime - startTime)
        return lifeTime
            
    














