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
