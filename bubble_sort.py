def sort(nums):

    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp


nums = [5, 3, 8, 6, 7, 2]
sort(nums)

print(nums)

# ===========================================
#
# another way

def bubbleSort(list):
    n = len(list)
    print(n)

    for i in range(n):
        print("This is value of i", i)

        for j in range(0, n - i - 1):
            print("This is value for j ", j)

            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]



list = [2,6,5,4,3,7,8]

bubbleSort(list)

print("Sorted list is:")

for i in range(len(list)):
    print(list[i])
