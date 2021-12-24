import numpy as np
#2d array
M = np.array([[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]])

#1d array
v = np.array([[1],
 [2],
 [3]])

#Shape of matrix or 2d array
print M.shape

#Shape of Vector or 1d array
print v.shape

v_single_dim = np.array([1, 2, 3])
print v_single_dim.shape

print v + v

print 3*v

#zeros matrix
a = np.zeros((2,2))

#ones matrix
b = np.ones((2,2))

#constant matrix
c = np.full((2,2), 5)

#identity matrix
d = np.eye(2)

#random matrix
e = np.random.random((2,2))

v1 = np.arange(3)
v2 = np.array([4,5,6])
v3 = np.array((1,6,8))
#vertical concatenation
Matrix = np.vstact([v1,v2,v3])

import numpy as np
M1 = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
M2 = 2*np.array([[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]) + np.full((3,3),6)
np.cross(M1, M2, axisa=0, axisb=1).T

