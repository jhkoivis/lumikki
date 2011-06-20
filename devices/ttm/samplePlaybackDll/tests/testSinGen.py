

import unittest
import ctypes
import numpy

class TestSinGen(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.sinGen = ctypes.cdll.LoadLibrary("./singen.so")
    
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def sinGenHelper(self, start, step, vectLen):
        outVectClass =  ctypes.c_double * vectLen
        
        outVect = outVectClass()
        pOutVect = ctypes.pointer(outVect)
        pTest = self.sinGen.singen(ctypes.c_double(start),
                           ctypes.c_double(step), 
                           pOutVect, 
                           ctypes.c_int(vectLen))
        
        for i in range(len(outVect)):
            tCurr = i*step - start
            self.assertAlmostEqual(outVect[i], 
                                  numpy.sin(2*3.14159265*tCurr), places=5)
            
    
    def testSinGen(self):
        
        vectLen = 10
        start = 0.0
        step = 0.1
        
        outVectClass =  ctypes.c_double * vectLen
        
        outVect = outVectClass()
        pOutVect = ctypes.pointer(outVect)
        pTest = self.sinGen.singen(ctypes.c_double(start),
                           ctypes.c_double(step), 
                           pOutVect, 
                           ctypes.c_int(vectLen))
        
        
        for i in range(len(outVect)):
            tCurr = i*step - start
            self.assertAlmostEqual(outVect[i], 
                                  numpy.sin(2*3.14159265*tCurr), places=5)
        
        
    def testMultiplePositions(self):
        self.sinGenHelper(0, 0.01, 900)
        
if __name__ == '__main__':
    unittest.main()
