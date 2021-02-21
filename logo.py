a = 10

def something():
    a = 15
    print('local variable', a)  # we cant access local variable outside the fn

something()

print('global variable', a) # we can use global variable inside a fn as well.

############################################################

a = 10

def something():
     global a
     a = 15 # if we want to specify that this "a" which we are using here
     #is not a local variable but a  global variable. in his case we have to mention here explicitly "global a".
     print('local variable', a)

something()

print('global variable', a)
