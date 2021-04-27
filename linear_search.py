pos = -1

def search(list,n):
    i = 0
    while i < len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i = i + 1
    return False


list = [2,3,4,5,6,7,9]
n = 2

if search(list,n):
    print('found at', pos)

else:
    print('not found')

# -------------------------------------------------------
# using for loop

list=[4,3,12,34,56,77,89]
n=int(input('enter a number'))
for i in range(len(list)):
    if list[i]==n:
        print('found at pos',i+1)
        break
else:
        print('not found')

# ---------------------------------------------------------
# Using for loop code:

pos = -1
def search(list, n):
 for i in range(len(list)):
  if list[i]==n:
   globals()['pos'] = i
   return True
 return False

list = [5,8,4,6,9,2]
n = 9

if search(list, n):
 print("Found at ",pos+1)
else:
 print("Not Found")
