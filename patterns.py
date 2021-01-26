# #print the perfect square pattern.

for i in range(4):
    for j in range(4):
        print(" # ",end="")
    print()

# print the pattern
#
# #
# # #
# # # #
print()
for i in range(4):
    for j in range(i+1):
        print(" # ",end="")
    print()


print()
for i in range(4):
    for j in range(4-i):
        print(" # ",end="")
    print()


# QUES:

# 1 2 3 4
# 2 3 4
# 3 4
# 4

i=4
for i in range(1,i+1):
    for j in range(i,4-i):
        print(i,end="")

    print()
