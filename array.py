 #Array should be of same type for ex:
 #if we are using int thn everything will be in int
 #and we have to mention that we r using int array

from array import *
vals=array('i',[5,6,8,9,10])
print(vals)

#in arrays we can use certain functions


from array import *
vals=array('i',[5,6,8,9,10])
print(vals.buffer_info()) # buffer_info will give the address and size of the array.


from array import *
vals=array('i',[5,6,8,9,10])
vals.reverse() #firstly it will reverse the array
print(vals) # then print


from array import *
vals=array('i',[5,6,8,9,10])

for i in range(5):
    print(vals[i])



from array import *
vals= array(input('how many values?'))
vals=array('i')

for i in range(len(vals)): # it will give the length and it will pass in the range
  #indirectly at runtime it will  be range 5
    print(vals[i])


from array import *
vals=array('i',[5,6,8,9,10])

for i in vals:
    print(i)


from array import *
vals=array('i',[5,6,8,9,10])

newarr = array(vals.typecode , (a*a for a in vals)) # when u dont know the value so its taking from vals ,a will represent one value at a time.
# this for loop will take one by one value at a time from vals & it will assign it to array.

for i in newarr:
    print(i)



from array import *
vals=array('i',[5,6,8,9,10])

newarr = array(vals.typecode , (a*a for a in vals))

i=0

while i<len(newarr)
    print(newarr[i])
    i+=1
