# def square(a):
#     return a*a
#
# result = square(5)
# print(result)

# a : a*a
# so we got this fn which is anonymous which accepts value a and what it returns is a*a.
f = lambda a : a*a
result  = f(5)
print(result)

f = lambda a,b : a+b
result  = f(5,6)
print(result)
