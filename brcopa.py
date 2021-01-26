
# using while loop
av = 5

x= int(input("how many candies you want?"))

i=1
while i<=x:
    if i>av:
        print("out of stock")
        break

    print("candy")
    i+=1

# using for loop
t=5
x=int(input("how many candies you want?"))
for i in range(0,x):
    if i<t:
        print('candy')
    else:
        print('out of stock')
        break


continue will not jum out of the loop it will only skip the remaining statements.
for i in range(1,101):
    if i%3==0:
        continue
    print(i)
print('bye')

# using pass will execute the statement without any condition.
for i in range(1,101):
    if i%2!=0:
        pass
    else:
        print(i)



# QUES1: Print first 50 fibonacci numbers.
#
# Ques2: Check a given number is prime or not.
