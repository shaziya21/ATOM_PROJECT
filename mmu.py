# from numpy import *
# arr1= array([
#                [1,2,3],
#                [4,5,6]
#
#            ])
#
# print(arr1.ndim) #ndim: no of dimensions
# print(arr1.shape)
# print(arr1.size)
#
# import numpy as np
# arr1 = array([
# [1,2,3],
# [4,5,6]
# ])
# arr2 = arr1.flatten() # flatten fn is used to convert 2d array in 1d
# #flatten creates a copy of thearray and make changes in the copy of array instead of original
# print(arr2)
#
# import numpy as np
# arr1 = array([
#                [1,2,3,8,5,7],
#             [4,5,6,1,2,3]
#             ])
# arr2 = arr1.flatten()
# arr3 = arr2.reshape(2,2,3) # reshape : converts 1d array into 3d array
#
# print(arr3)                #one big array which has two 2d array which has 2 one-d array
#                            #thn which has 3 values.
#
# import numpy as np
# arr1 = array([
# [1,2,3],
# [4,5,6]
# ])
#
# m=matrix(arr1)
# print(m)
#
# # using different fn in matrix:
#
# import numpy as np
# # we dont need separate array to save the values.
# m = np.matrix('1 2 3 4 ; 5 6 7 8') # using ; to differentiate btwn rows
# print(m)
#
#
# import numpy as np
#
# m = np.matrix('1 2;3 4;5 6;7 8') # 4 rows and 2 columns
#
# print(m)
#
# #when we want  to pass diagonal matrix
#
# import numpy as np
#
# m = np.matrix('1 2 3; 4 5 6;7 8 9')
#
# print(np.diagonal(m))
# print(m.min())
# print(m.max())
#
#
#
#
#
# import numpy as np
#
# m1 = matrix('1 2 3;4 5 6;7 8 9')
# m2 = matrix('5 6 7;1 3 4;9 5 2')
# m3 = m1*m2
#
# print(m3)
#

import numpy as np
x = np.arange(12).reshape(4,3)
x.ravel() #doesnt makes copy like flatten
print(x)
