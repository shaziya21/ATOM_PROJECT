# FUNCTION ARGUMENTS:
def update(x,y):
    x=8
    print(x)

update('x','y')

# QUES1
def add_numbers(x,y,z):#(ARGUMENTS)
   sum = x + y
   return sum

num1 = int(input('enter 1st number'))
num2 = int(input('enter 2nd number'))

print("The sum is", add_numbers(num1,num2,'num3')) #(parameters)

###########################################################

def update(lst):
    print(id(lst))

    lst[1] = 25
    print(id(lst))
    print('x: ',lst)


lst=[10,20,30]
print(id(lst))
update(lst)
print('lst: ',lst)


# in Python, we don't have the concept of 'pass by value' or 'pass by reference'.
# Instead, we have immutable or mutable arguments passed to the function.
# If we pass immutable objects like integer or string to function and
#try to update their value, their original value will not be updated
# instead a new variable will be created with updated value at new memory address.
#If we pass mutable objects like list or dictionary and try to update them,
# their original value will be updated at the same memory address
