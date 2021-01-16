a=5
b=6
a,b=b,a
#this goes into stack and thn it reverse with the concept of rotation
#ROT_TWO() which swaps the two top most stack items.
print(a,b)

#formula for swaping two no without using third variable
a=a+b
b=a-b
a=a-b
print(a,b)
