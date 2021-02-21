def count(lst):
    even = 0
    odd = 0

    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1

    return even,odd

lst=[20,25,14,19,16,24,28,47,26]

even,odd = count(lst)


print(even)
print(odd)
print(type(even))

######################################

def count(lst):
    even = 0
    odd = 0

    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1

    return even,odd

lst=[20,25,14,19,16,24,28,47,26]

even,odd = count(lst)
print('even : {} and odd : {}' .format(even,odd))
 # format() method formats the specified
 #value(s) and insert them inside the string's placeholder.

lst=['Gnana','Sekar','Chandra','Narayana','Gitam']
for i in lst:
    if len(i)==5:
        print(i)
