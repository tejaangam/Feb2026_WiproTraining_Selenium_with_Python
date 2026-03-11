import numpy as np

#Changing shape
#reshape

a = np.arange(1,7)
print("Original array:", a)
#reshape the array
reshaped = a.reshape(2,3)
print("Reshaped array:", reshaped)

#flat = return 1D iterator over the array
arr = np.array([[1,2], [3,4]])
for x in arr.flat:
    print(x)

#FLatten = Return a copy of the array collapsed into 1 dimension
arr = np.array([[1,2], [3,4]])
print(arr)
at_arr = arr.flatten()
print(at_arr)

#ravel () - Returns a flattened array
arr = np.array([[1,2], [3,4]])
print(arr)
at_arr = arr.ravel()
print(at_arr)


#pad() - Returns a padded array with shape increased according to pad-width()
arr = np.array([1,2,3])
padded = np.pad(arr, 3, mode = 'constant')
print(padded)


''' Transpose operations
1   transpose
Permutes the dimensions of an array
2   ndarray.T
 as self.transpose()
3   rollaxis
Rolls the specified axis backwards
4   swapaxes
Interchanges the two axes of an array
5   moveaxis()
Move axes of an array to new positions
'''

#1  transpose
# reorders the dimensions of an array.
# rows will become the columns

arr = np.array([[1,2,3],[4,5,6]])
print(arr)
transpose = arr.transpose()
print(transpose)

#2 ndarray.T
arr = np.array([[1,2,3],[4,5,6]])
print(arr)
transpose = arr.T
print(transpose)

#rollaxis - Rolls the specified axis backwards

arr = np.zeros((2,3,4))
print(arr)

# 2 is the blocks - axis 0
# 3 - rows - axis 1
# 4 columns - axis 2

#(0,1 ,2) - (2,3,4)
#(2,0,1) - (4,2,3)

#arr[block][row][column]

new_arr = np.rollaxis(arr, 2)
print(new_arr)

#swapaxes() - Interchanges two axes of an array.
#$Axis 0 and Axis 2 swapped.
arr = np.zeros((2,3,4))
print(arr)

new_arr = np.swapaxes(arr, 0 , 2)
print(new_arr)
# (4 3, 2)

#moveaxis() - Moves specified axes to new positions.
arr = np.zeros((2,3,4))
print(arr)
new_arr = np.moveaxis(arr, 0, -1)
print(new_arr)

# (3 ,4 2)
#Transepose operations
# reorders the dimensions of an array
arr = np.array([[1,2,3], [4,5,6]])
print("Normal Array", arr)
transpose = arr.transpose()
print("Transposed array", transpose)

#ndarray.T
arr = np.array([[1,2,3], [4,5,6]])
print(arr)
transpose = arr.T
print(transpose)

#rollaxis - Rolls the specified axis backwards
arr = np.zeros((2,3,4))
print(arr)

# 2 is the blocks - axis 0
# 3 - rows - axis 1
# 4 - columns - axis 2

#(0,1,2) - (2,3,4)
#(2,0,1) - (4,2,3)

#arr[block][row][column]
new_arr= np.rollaxis(arr, 2)
print(new_arr)
#4,3,2

#moveaxis() - Moves specified axes to new positions
arr = np.zeros((2,3,4))
print(arr)

#new_arr = np.swapaxes(arr, )


#concatenate - joining 2 arrays
a = np.array([[1,2], [3,4]])
b = np.array([[5,6], [7,8]])

print(np.concatenate((a,b), axis = 0))
print(np.concatenate((a,b), axis = 1))


#Stack - join the arrays along new axis
#adds new dimension
# all arrays must have the same shape

a=np.array([1,2,3])
b=np.array([4,5,6])
print(np.stack((a,b), axis = 0))
print(np.stack((a,b), axis = 1))

# hstack() - Stacks arrays vertically (row-wise)
a = np.array([[1,2], [3,4]])
b = np.array([[5,6], [7,8]])

print((np.hstack(a)))
print(np.concatenate((a,b), axis = 1))

#vstack() - stacks arrays vertically (row-wise)
print(np.vstack((a,b)))
print(np.concatenate((a,b), axis = 0))

#column stack()
a=np.array([1,2,3])
b=np.array([4,5,6])
print(np.column_stack((a,b)))


# row-stack() -Stacks arrays row wise
print(np.vstack((a,b)))



#Splitting Arrays
#split arrays intp multiple sub arrays based on axis
arr = np.array([1,2,3,4,5,6])
result = np.split(arr, 2)
print(result)

# hsplit() - splits array horizontally (column - wise)
#works on 2D arrays

arr2 = np.array([[1,2,3,4],
                [5,6,7,8]])
print(np.hsplit(arr2, 2))

#vsplit() Splits array vertically

arr3 = np.array([[1,2],
                 [3,4],
                 [5,6],
                 [7,8]])
print(np.vsplit(arr3, 2))


# Adding/ Remove elements
#resize() - Returns a new array with a specified path
arr = np.array([1,2,3,4])
new_arr = np.resize(arr, (2,3))
print(new_arr)

#the elements will repeat in the new array
#returns new array

#append () - Appends values at the end of an array
arr = np.array([1,2,3])
new_arr = np.append(arr, [4,5])
print(new_arr)

#2D array
a = np.array([[1,2], [3,4]])
b = np.array([[5,6]])
np.append(a, b, axis = 0)

#Insert values before given index
arr = np.array([10,20,30])
new_arr = np.insert(arr, 2, 15)
print(new_arr)

#Deletes elements along a specified axis.
arr = np.array([10,20,30])
new_arr = np.delete(arr, 2)

#Unique()
arr = np.array([1,2,2,3,4,5,5])
print(np.unique(arr))

#Repeating
#repeat () is used to repeat each element of an array
#Each element is repeated twice
arr = np.array([1,2,3])
print(np.repeat(arr,3))

#Different repeats for each element
arr = np.array([10,20,30])
print(np.repeat(arr, [1,2,3]))

#Repeat in 2D array
arr2 = np.array([[1,2],
                [3,4]])
print(np.repeat(arr2, 2, axis = 0))

# tile() the input array that will be repeated.

my_array = np.array([1,2,3])
tiled_array = np.tile(my_array, 2)
print("original array:", my_array)
print("tiled array:", tiled_array)


#Rearranging Elements
#flip() Reverse the order

arr = np.array([1,2,3,4])
print(np.flip(arr))

#2D
arr2 = np.array([[1,2],
                 [3,4]])
print(np.flip(arr2,axis = 0))
print(np.flip(arr2,axis = 1))

#flipr() - Flip left-right
arr2 = np.array([[1,2,3],
                 [4,5,6]])
print(np.fliplr(arr2))

#flipud - Flip Up- down (axis=0)
print(np.flipud(arr2))

#roll  - Rolls (rotates) element along a given axis
arr2 = np.array([[1,2,3],
                [4,5,6]])
np.roll(arr2, 2, axis=None)

#Sorting and Searching
arr  =np.array([5, 2, 9, 1])
indices = np.argsort(arr)
print(indices)

#lexsort() - Used for sorting with multiple columns (like sorting by start name,
#Then by b (secondary key)
#Sorting happens from right to left

a = np.array([1,1,0,0])
b = np.array([1,0,1,0])

result = np.lexsort()

#Changing Dimensions