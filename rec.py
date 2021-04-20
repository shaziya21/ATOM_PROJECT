import sys

sys.setrecursionlimit(20)
# for setting rec limit manually

print(sys.getrecursionlimit()) # it will give the limit.

i = 0

def greet():
    global i # for using global variable inside func.
    i +=1
    print("hello", i)
    greet()

greet()
