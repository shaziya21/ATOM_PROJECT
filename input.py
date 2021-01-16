#by default input gives you string format
x=input('enter 1st number ')
a=int(x)
y=input('enter 2nd number ')
b=int(y)
z=a+b
print(z)
#instead of using two variables a and b we can directly convert innto integer
x=float(input('enter 1st number'))
y=int(input('enter 2nd number'))
z=x+y
print(z);

ch=input('enter a char')
print(ch[0])

ch=input('enter a char')[2]
print(ch)

result=eval(input('enter an expression'))
print(result)

x =int(input('enter a number'))
y =int(input('enter second number'))
z=x//y
print(z)
