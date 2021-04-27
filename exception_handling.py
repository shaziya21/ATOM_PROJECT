a = 5
b = 2

try:  # it'll try to divide otherwise jump to except and execute.
    print('resource open')
    print(a/b)
    k = int(input("enter a number"))
    print(k)

# except block will get executed only when there's error.
# for different type of errors we have different except block.

except ZeroDivisionError as e :   # if we want to print message error as well or print what is the error thn well use 'e' as a representation of exception.
    print('hey , you cannot divide a number by zero' , e)

except ValueError as e:
    print('invalid input')

except Exception as e:  # this Exception can handle all the exception.
    print('something went wrong')
finally:
    print('resource closed')


# finally block will executed if we get error as well as if we don't get error.
