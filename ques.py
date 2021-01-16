# QUES1: Take three values from user and find the greatest number from them..

num1=float(input('enter 1st number'))
num2=float(input('enter 2nd number'))
num3=float(input('enter 3rd number'))

if (num1>num2) and (num1>num3):
 print('num1')

if(num2>num3) and (num2>num1):
 print('num2')

else:
    print('the greatest number is num3')

#QUES 2:Write a code to chck a given number is positive or negative.


x=int(input('enter a number:'))

if x>0:
    print('positive number')

else:
    print('negative number')
