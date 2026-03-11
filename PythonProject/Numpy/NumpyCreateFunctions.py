'''
    Using numpy.array() Function
    Using numpy.zeros() Function
    Using numpy.ones() Function
    Using numpy.arange() Function
    Using numpy.linspace() Function
    Using numpy.random.rand() Function
    Using numpy.empty() Function
    Using numpy.full() Function
    Using numpy.eye() FUnction

'''
import numpy as np

#1D array
#this function creates a numpy array

a = np.zeros(5)
print(a)

#2d array or zeros
a_2D = np.zeros((4,3))
print(a_2D)

#using numpy.ones() func
a = np.ones(5)
print(a)
#2D array of ones
a_2D = np.ones((4,3))
print(a_2D)

#Providing the start , stop and step
a =np.arange(1,10, 2)
print(a)

#Using numpy.linspace() functio
#
a = np.linspace(0,10, num =5, endpoint=False)
print(a)

#using numpy.random.rand() function
#generates an array of the specified shape with random value
#if no argument is provided,

a = np.random.rand(5)
print(a)
#2D
a = np.random.rand(2,3)
print(a)
#3d
a= np.random.rand(2,3,4)
print(a)

#using  numpy.empty() function
#2D
#THis function initializes an array
#the content of the array is
a =np.empty((2,3))
print(a)

#using numpy.full() function
a = np.full((2,3), 5)
print(a)

#Using numpy.eye()
#The numpy eye() function is used to create a 2D array with ones on the diagnol
identity_matrix = np.eye((4))
print(identity_matrix)
#using identity function is used generate square identity matrix
identity_matrix = np.identity((5))
print(identity_matrix)

#numpy diag
Matrix = np.array([[10,20,30], [40,50,60], [70,80,90]])
print("Original matrix", Matrix)
Diagonal_elements = np.diag(Matrix)
print("Diagonal elements", Diagonal_elements)