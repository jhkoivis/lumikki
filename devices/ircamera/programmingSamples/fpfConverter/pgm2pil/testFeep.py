
import pgm2pil
import pylab

try:
    pylab.imread('feep_false.pgm')
except IOError:
    pass
else:
    raise ValueError("feep_false should fail")

pylab.subplot(2,1,1)
a = pylab.imread('feep.pgm')
pylab.imshow(a)

pylab.subplot(2,1,2)
b = pylab.imread('lena.png')
pylab.imshow(b)

pylab.show()
