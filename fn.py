def greet(): #defining the fn
    print('hello')
    print('good morning')

greet() #fn will be called only when we'll explicitly call it.

def greet():
    print('hello')
    print('good morning')

def add(x,y):
    c=x+y
    print(c)
add(2,2)

# another type of fn which will return you the value.
def greet():
    print('hello')
    print('good morning')

def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d

greet()
result1,result2 = add_sub(6,4)
print(result1,result2)
