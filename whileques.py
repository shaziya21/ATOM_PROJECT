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


#Ques 2: write a code to print below pattern.
# # # # #
# # # # #
# # # # #
# # # # #

i=1
while i<=5:
    print("*",end="")
    j=1
    while j<=5:
        print("*",end="")
        j=j+1
i=i+1

rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        # Check condition if value of j is smaller or equal than
        # the j then print i otherwise print j
        if j <= i:
            print('*', end=' ')
        else:
            print('*', end=' ')
    print()  
