# with numpy
import numpy
def numpysum(n):
  a = np.arange(n) ** 2
  b = np.arange(n) ** 3
  c = a + b
return c

#without numpy
def pythonsum(n):
a = range(n)
b = range(n)
c = []
for i in range(len(a)):
a[i] = i ** 2
b[i] = i ** 3
c.append(a[i] + b[i])
return c

# with numpy for either list, tuple or array object, return list
import numpy as np
def numpySquare(x):
    return list(np.array(x)**2)
b= numpySquare(np.array([4,8,4,8,8,8]))
print(b)

#basic numpy

a = numpy.arange(5)
print(a)
a.dtype

b= numpy.zeros(5)
a=numpy.array([1,2,3,4,5])
a.shape
a.size
a.ndim
newArray = numpy.array(aList)

a = numpy.array([1,2,3],[6,7,8],[11,51,53])
print(a)
