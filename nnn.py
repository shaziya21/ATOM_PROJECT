 # in numpy we dont need to mention type.

# Different ways of creating an array in numpy
# array()
# linspace()
# logspace()
# arange()
# zeros()
# ones()


from numpy import *

arr = array([1,2,3,4,5])
print(arr.dtype)
print(arr)


from numpy import *

arr = linspace(0,15,16) # start,end,the no of paths you wat to go for
#it will divide the range(0,15) in 16 parts

print(arr)

from numpy import *
arr=arange(1,15,2)

print(arr)


from numpy import *
arr=logspace(1,40,5) #divide into 5 parts starting from 10^1 to 10^40


print('%.2f' %arr[2])


from numpy import *
arr = ones(5,int) #using int for getting int value

print(arr)
