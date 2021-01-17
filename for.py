# in while loop we need to specify a condition
# but in for loop it uses sequence
# unlike while loop which depends on condition true or false.
# "For Loop" depends on the elements it has to iterate.
# For Loop iterates with number declared in the range.
# unlike while here we dont initialise variable,check condn and incree or decr.
# by ourself

x=('shaziya',21,13)
for i in x:
    print(i)


for i in ['shaz',21,0.6]:  # [] is list
    print(i)

for i in range(10): # it means start from 0 and end at 9
    print(i)

for i in range(11,21,1): # start point,end point and iteration
    print(i)
