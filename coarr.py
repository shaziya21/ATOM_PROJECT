# adding number to array

from numpy import *
arr = array([1,2,3,4,5])

arr= arr+5
print(arr)

# adding two array
from numpy import *
arr1 = array([1,2,3,4,5])
arr2 = array([6,7,8,9,4])
arr3 = arr1+arr2
print(arr3)
VECTORIZED OPERATION : ADDING OF ARRAY

from numpy import *
arr=array([1,2,3,4,5])
x=[]
for i in arr:
    y=i+5
    x.append(y)
print(x)

from numpy import *
arr1 = array([1,2,3,4,5])
print(sin(arr1))

from numpy import *
arr1 = array([1,2,3,4,5])
print(sqrt(arr1))
#we any math fn in this like this

from numpy import *
arr1 = array([8,5,3,7,5])
print(sort(arr1))

ALIASING  creating a new allies for the new array

from numpy import *

arr1 = array([2,4,6,8,9])
arr2 = arr1

print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))

from numpy import *

arr1 = array([2,4,6,8,9])
arr2 = arr1.view() # view() is used to create two diff array add

print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))

# there are two types of copy
# SHALLOW COPY: A shallow copy creates a new object
# which stores the reference of the original elements.

#DEEP COPY:A deep copy creates a new object and recursively
#adds the copies of nested objects present in
#the original elements.

from numpy import *

arr1 = array([2,4,6,8,9])
arr2 = arr1.view()

arr1[1]=5

print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))
# in shallow copy when we change some value in arr1 it will automatically change the value in arr2.

from numpy import *

arr1 = array([2,4,6,8,9])
arr2 = arr1.view() # view() is used to create two diff array add

print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))

#QUES:WRITE A CODE TO ADD 2 ARRAYS USING FOR LOOP:

import numpy as np
arr1=np.array([1,2,3,4,5])
arr2=np.array([6,7,8,9,2,3,5,6,7])
arr3=np.array([])
for i in range(len(arr1)):
     arr3 = arr1+arr2
print(arr3)

# write a code to find the max value from an array
# without using in built fn.
