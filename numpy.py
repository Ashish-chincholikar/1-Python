
#------------------------------------------------------------------
#numpy module
import numpy as np
arr1 = np.array([7 , 20 , 13])
arr2 = np.array([3 , 5 , 2])
arr1
arr1.dtype

#creating multi-dimensional array

arr = np.array([[7 , 8 , 9],[10 ,11 ,12]])
print(arr)
"""
[[ 7  8  9]
 [10 11 12]] 
 """
# represent the minimum dimensions
# use ndmin parameter to specify how many minimum dimesions 
#you wanted to create with an array with minimum dimensions
arr = np.array([10 ,11 ,12 ,13],ndmin = 2)
print(arr)
# [[10 11 12 13]] -->2D array

arr = np.array([10 ,11 ,12 ,13],ndmin = 3)
print(arr)
# [[[10 11 12 13]]] -->3D array

#changing the Datatype of array
arr = np.array([10 ,11 ,12 ,13],dtype = complex)
print(arr)
# [[10 11 12 13]] -->2D array
#get the dimensions of the Array
arr = np.array([[1,2,3,4] , [7,8,6,7] , [9,10,11,12]])
print(arr.ndim)
print(arr)

#finding the size of each item in the array
arr = np.array([10.25 ,20.00 ,30.25 , 40.2])
print("Each item contains in bytes : " , arr.itemsize)
#each line contains in 4 bytes

#checking the datatype of each item in array
arr = np.array([10 ,20 ,30])
print("each item is of the type" , arr.dtype)

#array shape and size

arr = np.array([[10,20,30,40] , [60,70,80,90]])
arr
print("Array size : " , arr.size)
print("Array shape : " , arr.shape)

#creating array from list with type float

arr = np.array([[10 ,20 ,30 ,40] , [60,70,80,90]]  ,dtype = 'float')
print("Array created using the list : \n" , arr)

#create a sequence of integers using arange() function
arr = np.arange(0 , 20 ,3)
print("the sequential array with step of 3 : \n" , arr)
#the sequential array with step of 3 : 
 #[ 0  3  6  9 12 15 18]

#sequential array
arr = np.arange(11)
print(arr)
#[ 0  1  2  3  4  5  6  7  8  9 10]

#accessing the array elements: 
arr[2]
#2
arr[-2]
#9

#Multidimensional Array indexing

arr = np.array([[10 ,20 ,30 ,40 ,50 ] , [20 ,30 ,50 ,10 ,30]])
print(arr)
#[[10 20 30 40 50]
 #[20 30 50 10 30]]
arr.shape
print(arr[1,1]) #-->30

print(arr[0 ,4]) #-->50

print(arr[1,-1]) #-->30
#rows start from 0, we need 1st row and last element : -->30

#Accessing array elements using slicing 

arr = np.array([0 ,1, 2,3,4,5,6,7,8,9])
x = arr[1:8:2] #--> [1  3  5  7]
print(x)

arr = np.arange(10)
x = arr[::1]
print(x)#[0 1 2 3 4 5 6 7 8 9]

x = arr[-2:3:-1] #[8 7 6 5 4]
print(x)

x = arr[-2 : 10]
print(x) # [8 9]

#Indexing in numpy
arr = np.array([[10 ,20 ,30 ,40],
                [40 , 50 , 70 ,90],
                [60 , 10 ,70 ,80],
                [30 , 90 , 40 , 30]])
arr
"""
multi_arr [1,2]# to access the value at row 1 and column2
multi_arr [1,:]#to get all the columns and 1st row
multi_arr [:, 1]#to get all the rows and 1st column
"""
x = arr[:3 , ::2]
print(x)

#reshaping the array

arr = np.arange(35).reshape(5 , 7)
arr.shape
arr.size
print(arr)
"""
[[ 0  1  2  3  4  5  6]
 [ 7  8  9 10 11 12 13]
 [14 15 16 17 18 19 20]
 [21 22 23 24 25 26 27]
 [28 29 30 31 32 33 34]] 
"""

# -*- coding: utf-8 -*-
"""
Created on Thu May 11 08:15:30 2023

@author: 91721
"""

import numpy as np
"""
arr = np.array([[1,3,4,5] , [5,6,4,3]])
arr.shape
arr.size
arr.ndim
print(arr.dtype)
arr = np.array([[1,3,4,5] , [5,6,4,3]] , dtype = "float")
arr
"""
#BOOLEAN ARRAY INDEXING
import numpy as np

arr = np.arange(12).reshape(3,4)
print(arr)
rows = np.array([False , True , True])
wanted_rows = arr[rows, : ]
print(wanted_rows)

#Numpy array to python list using tolist() method
arr = np.array([10,20,30,40])
print("Array : ",arr)
print(type(arr))

#converting to list
lst = arr.tolist()
print("list : ",lst)
print(type(lst))

#converting multidimensional array to list

arr1 = np.array([[10,20,30,40],
                [10,30,50,70],
                [50 ,80,30 ,20]])

print("Array \n" , arr1)

#converting array to list using tolist() method

lst1 = arr1.tolist()
print("list : \n" , lst1)

#converting list to array
#numpy.array()
#numpy.asarray()

lst = [10,20,30,40]
print(type(lst))
#convert list to arrray
arr2 = np.array(lst)
print(arr2)
print(type(arr2))

#using numpy.asarray()
lst1 = [10,20,30,40]
print(type(lst1))
arr3 = np.asarray(lst)
print("Array : ", arr3)
print(type(arr3))

#numpy Array properties
#in case of properties paranthiesis () are not give

#1) arr.shape
arr4 = np.array([[1,2,3] , [3,4,5]])
print(arr4)
arr4.shape

#resizing of array 
arr4 = np.array([[1,2,3] , [3,4,5]])
print(arr4)
#[[1 2 3]
# [3 4 5]]
arr4.shape = (3,2)
print(arr4)
#[[1 2]
# [3 3]
# [4 5]]

#using reshape
arr4 = np.array([[1,2,3] , [3,4,5]])
print(arr4)
new_arr = arr4.reshape(3,2)
print(new_arr)

#usage of ndim
arr4 = np.array([[1,2,3] , [3,4,5]])
print(arr4.ndim)

#performing arithemtic operations on arrays
arr1 = np.arange(16).reshape(4,4)
print(arr1)
"""
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]] 
"""
arr2 = np.array([1,3,2,4])
print(arr2)
#[1 3 2 4]
#add()
add_arr = np.add(arr1 , arr2)
print(f"Adding two array : \n{add_arr}")
""" 
[[ 1  4  4  7]
 [ 5  8  8 11]
 [ 9 12 12 15]
 [13 16 16 19]]
"""

#Substract()
sub_arr = np.subtract(arr1 , arr2)
print(f"Substracting two array : \n{sub_arr}")
"""
[[ 0  1  2  3]       [1 3 2 4]      
 [ 4  5  6  7] 
 [ 8  9 10 11]
 [12 13 14 15]] 

result

[[-1 -2  0 -1]
 [ 3  2  4  3]
 [ 7  6  8  7]
 [11 10 12 11]]

"""
#Multiply()

mul_arr = np.multiply(arr1 , arr2)
print(f"Multiplication of array is  : \n{mul_arr}")
""" 
each row to column 
[[ 0  3  4 12]
 [ 4 15 12 28]
 [ 8 27 20 44]
 [12 39 28 60]]
"""

#divide()

div_arr = np.divide(arr1, arr2)
print(f"Division of array is \n :{div_arr}")

#numpy.reciprocal()
# this function returns the reciprocal of arguments element-wise

#to perform Reciprocal opertaion
arr1 = np.array([50 , 10 , 3 , 1 , 200])
rep_arr1 = np.reciprocal(arr1)
print(f"After applying the reciprocal() function : \n {rep_arr1}")

#To perform the power operation
arr1 = np.array([3,10,5])
pow_arr1 = np.power(arr1 , 3)
print(f"after applying the power function to array : \n {pow_arr1}")

#apply elements of one array as the power values of the second
#array elements

arr2 = np.array([3,2,1])
print("Second array \n ",arr2)
pow_arr2 = np.power(arr1 , arr2)
print(f"After applying the power function to array : \n{pow_arr2}")

# After applying the power function to array : 
# [ 27 100   5]

#to perform mod function on numpy array
import numpy as np
arr1 = np.array([7 , 20 ,13])
arr2 = np.array([3,5,2])
arr1
arr1.dtype
#mod()
mod_arr = np.mod(arr1 , arr2)
print(f"after applying mod function to the array : \n{mod_arr}")

#-------------------------slot2--------------------------------
#linear Algebra using numpy array

#create empty array
from numpy import empty

a = empty([3,3])
print(a)
#contains exponent values as elements


#create zero arrays
from numpy import zeros
a = zeros([3 , 5])
print(a)

#create one array
from numpy import ones

a = ones([3,5])
print(a)

#vertical stack
from numpy import array
from numpy import vstack
from numpy import hstack
a1 = array([1,2,3])
print(a1)
a2 = array([4,5,6])
print(a2)
a3 = vstack((a1,a2))
print(a3)
print(a3.shape)

#create array with hstack -->horizontal
a1 = array([1,2,3])
print(a1)
a2 = array([4,5,6])
print(a2)
a3 = hstack((a1,a2))
print(a3)

#two dimensional list of lists to Array
#create two-dimenstional array
from numpy import array
#list of data
data = [[11,22], 
        [33,44],
        [55,66]]
#array of data
data = array(data)
print(data)
print(type(data))

#index array out of bound
data = array([11,22,33,44,55])
#index data
print(data[5])
#index 5 is out of bounds for axis 0 with size 5

#accessing elements using negative indexing
data[-1]
data[-2]

from numpy import array
data = [ [11,22] ,
        [33,44] ,
        [55,66]]
print(type(data))
data = array(data)
print(type(data))
print(data[0][0])
print(data[0,])#0th row and all columns


# -*- coding: utf-8 -*-
"""
Created on Fri May 12 08:09:55 2023

@author: 91721
"""
#split input and output Data
from numpy import array

data = array([[11,22,33],
        [44,55,66],
        [77,88,99]])

#spliting the data
X , y = data[:,:-1] , data[:,-1]
print(X)
print(y)

#broadcast scalar to one-dimensional array
#inorder to increase the pixel values
a = array([1,2,3,4])
print(a)
#define scalar
b = 2
print(b)
#broadcast
c = a + b
print(c)
print(type(c))

#vector addition
#define first arrray
a = array([1,2,3,4])
print(a)
#define second array
b = array([1,5,6,4])
print(b)
#add vectors
c = a + b
print(c)

#vector Substraction
#define first arrray
a = array([1,2,3,4])
print(a)
#define second array
b = array([1,5,6,4])
print(b)
#add vectors
c = a - b
print(c)

#vector l1 norms and vector l2 norms
from numpy import array
from numpy.linalg import norm

a = array([1,2,3])
print(a)

l1 = norm(a , 1)
print(l1)

#vector l2 norm
l2 = norm(a , 2)
print(l2)

#to find the upper or lower triangular matrices
from numpy import array
from numpy import tril
from numpy import triu

#define square matrix
M = array([
    [1,2,3],
    [4,5,6],
    [7,8,9]])
    
print(M)
#lower triangular
lower = tril(M)
print(lower)

#upper triangular
upper = triu(M)
print(upper)

#to find the diagonal matrix 
from numpy import array
from numpy import diag
M = array([
    [1,2,3],
    [4,5,6],
    [7,8,9]])
    
print(M)
#extract diagonal vector
d = diag(M)
print(d)

#created diagonal matrix from vector
D = diag(d)
print(D)

#===========================slot2================================
#identity matrix
from numpy import identity
I = identity(3)
print(I)

#orthogonal matrix
from numpy import array
from numpy.linalg import inv
#define orthogonal matrix
Q = array([[1 , 0],
           [0 , -1]])
print(Q)

#inverse equivalence
v = inv(Q)
print(Q.T)
print(v)

#identity equivalence

I = Q.dot(Q.T)
print(I)

