# Numpy Intro
"""
Numpy - "Numerical Python". Foundation for Pandas and high performance scientific computing / data analysis
1. Numpy Arrays
2. Basic Operations
3. Indexing
4. Universal Functions
5. Array Methods for Data Analysis
6. Linear Algebra
"""

import numpy as np
# use np.some_numpy_method to use numpy
# numpy is python package that allows for doing data analysis
# different ways of importing
from numpy import array, dot, sign
from numpy import *

# Print the absolute value of -1
# Absolute refers to the distance of a number to the zero line
print()
print("The absolute number of '-1' is : ", np.abs(-1))
print()


# Numpy Arrays
print("*************************Numpy Arrays*************************")
print()
# 1D array
list1 = [1,1.1,-5.45,3.2]
arr1 = np.array(list1)
print("The 1D array contents of 'arr1' : ", arr1)
print()

# 2D array
list2 = [[1, 1.1, -5.45, 3.2], [-0.5, 0.33, 10.12, -5]]
arr2 = np.array(list2)
print("The 2D array contents of 'arr2' : ", arr2)
print()

print("The shape of array1 : ", arr1.shape)
print("The shape of array2 : ", arr2.shape)
print()

# Numpy Basic Operation's - What are arrays actually good for??
# Operation's between equal-size arrays or arrays and scalars element-wise
# Boolean operations on arrays also act element-wise
# No loops needed
print("*************************Numpy Basic Operations*************************")
print()

# Numpy makes array - scalar operations easier

# clunky loop
new_list1 = []
print("The values in the list before '-5' subtraction : ", list1)
for x in list1:
    # for each element subtract 5 from the value
    new_list1.append(x-5)
print("The values in the list after '-5' subtraction : ", new_list1)
print()

# It is NOT possible to square the 'the non-int values of type int'  from the list
# but is possible with an array

# numpy makes array operations easier
print("The values in arr2 before squaring : ", arr2)
print("Squaring the values of arr2 : ", arr2*arr2)
print()


# numpy makes array - scalar boolean logic easier
# print the elements in arr1 that are greater than 0
#
#This is NOT possible!
# print("list1 is > 0 : ", list1>0)

in_pos=[]
for x in list1:
    in_pos.append(x>0)
print("Listing if 'list1' value is greater than 0 : ", in_pos)
print()


print("Listing if 'arr1' values are greater than 0 : ", arr1>0)
print()

#
arr3 = np.array([1,2,3,4])
arr4 = np.array([0,3,5,6])
print("The values of arr3 : ", arr3)
print("The values of arr4 : ", arr4)
print("The output of arr3 > arr4 : ", arr3>arr4)
print()

# Bool1 -> is arr1 > 0
bool1 = arr1 > 0
print("Array1 is > 0 : ", bool1)
bool2 = arr1 > 1
print("Array1 is > 1 : ", bool2)
print()

# In which cases are both bool1 and bool2 True
print("The values in which both values of bool1 & bool2 are True : ", bool1&bool2)
print()

# In which cases are both bool1 and bool2 are NOT True
print("The values in which any value of bool1 '|' bool2 are True : ", bool1|bool2)
print()
print()

# Array Indexing
print("*************************Array Indexing*************************")
print()
# Id arrays are similar to python lists
print("The contents of arr1 : ", arr1)
print()
print("The value of arr1[0] : ", arr1[0])
print()
print("The values from arr1[1:3] : ", arr1[1:3])
print()
print("The values from arr1[-2:1 : ", arr1[-2:1])
print()

# 2D array indexing
print("The contents of arr2 : ", arr2)
print()
print("The contents of arr2[0] : ", arr2[0])
print()
print("The value from arr2[0][1] : ", arr2[0][1])
print()
print("The value printed from arr2[0,1] : ", arr2[0,1])
print()
print("The contents of arr2[0] : ", arr2[0])
print("The values from arr2[0] from pos[0] up to pos[3] - arr2[0, :3] : ", arr2[0, :3])
print()
print("The contents of arr2 : ", arr2)
print("The contents of arr2[0] & arr[1] up to pos[3]  -arr2[:, :3] : ", arr2[:, :3])
print()
print("This can NOT be done with a list. 'list2' : ")
print()
print("The contents of arr2 : ", arr2)
print("Print specific values of an array arr2[:, [1,3,-1]] : ", arr2[:, [1,3,-1]])
print()

# Boolean Indexing
print("Boolean Indexing")
print()
mask1 = arr1>0
print("The contents of arr1 : ", arr1)
print("Listing what values from arr1 are True/False : ", mask1)
print()
print("Passing mask1(arr1>0) into arr1 - creates a new array of only +ve values : arr1[mask1] : ", arr1[mask1])
print()
print("The contents of arr2 : ", arr2)
print("Using Boolean Indexing of 2D Array elements arr1[True, False], :2 and printing up to pos[2] : ", arr2[[True, False], :2])
print()
print("The contents of arr2 : ", arr2)
mask2 = arr2 < 0
print("The contents of arr2 < 0 : ", mask2)
print()
print("Passing in the 2D boolean mask 'mask2' into arr2 - arr2[mask2]  will create a new array that only has -ve values: ", arr2[mask2])
print("The contents of arr2 : ", arr2)
print()
print()


# Numpy Functions
# Functions that perform elementwise operations on data in arrays
print("Numpy Functions")
print()

# Many Universal Funcs operate on a single array
# Universal functions apply to each element in the array, which allows faster performance
# Can do many UFuncs ... abs, fabs, exp, sign, tan...
arr = np.array([1,4,9,16])
print("The values in 'arr' before square root. : ", arr)
print("The values in 'arr' after square root. : ", np.sqrt(arr))
print("The values in 'arr' after logarithm of arr", np.log(arr))
print()

# some U Funcs on multiple arrays
arr_new1 = np.array([1,-1,3,5])
arr_new2 = np.array([2,1,4,1])
print("The values of arr_new1 : ", arr_new1)
print("The values of arr_new2 : ", arr_new2)
print("The maximum values elementwise between 'arr_new1' and 'arr_new2' : ", np.maximum(arr_new1, arr_new2))

# Data Analysis
# 1. Math/Stat Methods
# 2. Boolean Array Operations
# 3. Sorting/Unique Values

# Math/Stat Methods
print("**********Math/Stat Methods**********")
list1_new = [1,1.1,-5.45,3.2]
arr1_new = np.array([list1_new])
list2_new = [[1,1.1,-5.45,3.2], [-0.5, 0.33, 10.12, -5]]
arr2_new = np.array(list2_new)
print("The contents of 'arr1_new' : ", arr1_new)
print("The contents of 'arr2_new' : ", arr2_new)

# arrays have many built-in functions that aggregate the data
print("The average of all the elements of arr1_new using built i n mean() function : ", arr1_new.mean())
print()
print("Taking the average across the 2D array.")
print("Finding arr2_new.mean() : ", arr2_new.mean())
print("Finding the arr2_new.mean(0)  across the rows : ", arr2_new.mean(0))
print("Finding the arr2_new.mean(1) across the columns : ", arr2_new.mean(1))
print()
print("Can also do np.mean(arr2_new) : ", np.mean(arr2_new))
print()

# Some functions dont aggregate but instead produce an array
print("Takes the cumulative sum across each of the columns : ", arr2_new.cumsum(0))

# Boolean array operations
print()
print("**********Boolean array operations***********")
mask3=(arr1_new>0)
print("Mask3 values are : ", mask3)
print()

# Taking True = 1 and False = 0  do the sum()
print("The sum of the boolean array 'arr1_new' True = 1 False = 0 : ", mask3.sum())
print("The average of the boolean array 'arr1_new' True = 1 False = 0 : ", mask3.mean())
print()

# Mask.any() will loop through the array and tell if 'any' of the values is 'True'
print("'mask3'  any() of the values == True : ", mask3.any())
print()
# Mask.all() will loop through the array and tell if 'all' of the values is 'True'
print("'mask3' all() of the values == True : ", mask3.all())

# Sorting/Unique Values
print()
print("**********Sorting**********")
print()

print("The values in 'arr1_new' : ", arr1_new)
print()
# sorting the array in place
arr1_new.sort()
print("Sorting 'arr1_new' : ", arr1_new)
print()
# Get Unique values in sorted order
tickers = np.array(['Tech', 'Tech', 'Cons', 'Energy', 'Financials', 'Financials'])
print("The contents of 'tickers array : ", tickers)
print()
print("Sorted Unique values only : ", np.unique(tickers))
print()

# Numpy Linear algebra
print("**********Numpy Linear algebra**********")
print("linear Algebra is better done in Numpy than Pandas....")

x = np.array([[1., 2., 3.],[4., 5., 6.]])
print("The 'x' array : ", x)
print()

y = np.array([[6., 23.], [-1, 7], [8,9]])
print("the 'y' array : ", y)

# multiple matrices
print("multiple matrices - x.dot(y) : ", x.dot(y))
print()
print("Or can do it np.dot(x, y) : ", np.dot(x, y))
print()
print("or can do 'x @ y' : ", x @ y)
print()
print("The Transpose - 'x.T' : ", x.T)
print()

# Inverse
print("The Linear Algebra inverse is : ", np.linalg.inv(x @ y))
print()
print()




