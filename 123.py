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
