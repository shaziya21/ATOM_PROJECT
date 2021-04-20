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

# QUES : Take 10 names from the user and then count and display the no of users who has len more thn 5 letters

names= int(input('enter the names of users'))
count+=1
for i in names:
    if length>=5
        print(names)

else:
    print('not found')
