# numpy - numerical python
# Advantage of numPy Array

# Allows several mathematical operations
# Faster operation

import numpy as np
from time import process_time
# list vs numpy


#  list time 
python_list = [i for i in range(10000)]
start_time = process_time()
python_list = [i+5 for i in range(10000)]
end_time = process_time()

print(end_time - start_time)

# numpy array time ..
np_array = np.array([i for i in range(10000)])
start_time = process_time()
np_array  += 5
end_time = process_time()
print(end_time- start_time)

# Numpy arrays

#  list
list1 = [1,2,3,4,5]
print(list1)
type(list1)

# Np aray
np_array = np.array([1,2,3,4,5])
print(np_array)
type(np_array)


# Creating a 1D array

np_array1 = np.array([1,2,3,4,5])
print(np_array1)
np_array1.shape


b = np.array([(1,2,3,4,5) , (5,4,3,2,1)])
print(b)
b.shape


c = np.array([(1,2,3,4) , (4,5,6,7)] , dtype=float)
print(c)

# initial placeholder in numpy array

# Create a numpy of zero
x = np.zeros((4,5))
# print(x)

#  create a numpy array of ones
y = np.ones((3,4))
# print(y)

#  create a numpy array of particular value
z = np.full((3,4) ,5)

print(z)


#  creating  identity matrix

a = np.eye(4,4)
print(a)

# create a numpy array with random value

#  creata a random value
b = np.random.random((3,5))
print(b)

# create a random integer value's array
c = np.random.randint(10 , 50 , (3,5))
print(c)

# create array of evenly spaced value
v = np.linspace(10, 30 , 5)
# print(v)

a = np.arange(10 , 30 , 5)
print(a)


# convert a list to a numpy array
list2 = [10, 20, 30, 40, 50]
np_array = np.asarray(list2)
print(np_array)
print(type(np_array))

# analysing to a numpy array
c = np.random.randint(10 , 50 , (5,5,))
print(c)


# arrray dimension
print(c.shape)


# number of dimension
print(c.ndim)

# checking the number of element present in an array
print(c.size)

# checking the data type of an values in the array
print(c.dtype)

# mathematical operation on a np array

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
print(list1+list2)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = np.random.randint(0 , 10 , (3,3))
print(a)
b = np.random.randint(10 , 20 , (3,3))
# print(a+b)
# print(a-b)
print(np.add(a,b))
print(np.subtract(a,b))
print(np.multiply(a,b))
print(np.divide(a,b))


# array manipulation

a = np.random.randint(0 , 10 ,(2,3))
print(a)
# print(a.shape)

# transpose of the matrix
res = np.transpose(a)
print(res)

a = np.random.randint(0 , 10 ,(2,3))
print(a)
# transpose of the matrix
res = a.T
print(res)

# reshaping array

a = np.random.randint(0 , 10 , (2, 3))
print(a)
# print(a.shape)

b = a.reshape(3,2)
print(b)

