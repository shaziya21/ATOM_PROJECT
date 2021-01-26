from array import *

arr = array('i',[])

n = int(input('enter the length of the array'))

for i in range(n):
    value = int(input('enter next value'))
    arr.append(value)

print(arr)

value = int(input('enter the value for search'))

k=0
for e in arr: # doing it manually
    if e == value:
        print(k)
        break
    k+=1

print(arr.index(val))
