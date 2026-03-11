#Creating of arrays

# 1D, 2D, 3D

import numpy as np

#1D array
a = np.array([1,2,3])
print(a)

#2D array
a = np.array([[1,2], [3,4]])
print(a)

#3D array
a = np.array([[1,2],[3,4],[5,6]])
print(a)

#Create a array with specific data ttype
a = np.array([1,2,3], dtype=complex)
print(a)

a = np.array([1,2,3], dtype=float)
print(a)

a = np.array([1,2,3], dtype=int)
print(a)
