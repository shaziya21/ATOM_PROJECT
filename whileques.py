#Ques: Write a code to print all the values from 1 to 100 .
#skip the numbers which are divisible by 3 or 5.
i=1
a=1
while i<=100:
    if ((a%3 and a%5)==0) :
           a=a+1
          
    else:
        print(a)
        a=a+1
    i=i+1
