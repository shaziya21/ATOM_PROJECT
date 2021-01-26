# PRIME NUMBER: It is divisible by 1 and itself only.
num=int(input("which number you want to check?"))
for i in range(1,num):
    if num % i == 0:
        print('prime number')
        break
else:
    print('not prime')
