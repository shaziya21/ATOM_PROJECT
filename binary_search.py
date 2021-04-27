# lower bound <= upper bound
# always use // for int division
# 1. (L + U)/ 2 = mid Value

# 2. mid value = search

# 3. mid value != search
#        3.1  for new iteration change upper and lower bound
#
# 5. if search value is smaller then change upper bound.
# & mid becomes new upper bound.
#
# 6. if search value is greater then change lower bound.
# & mid becomes new lower bound.
#
# 7. again same thing from step 1.


pos = 0

def search(list,n):

    l = 0
    u = len(list)-1

    while l <= u:
        mid = (l+u) // 2

        if list[mid] == n:
            globals() ['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid+1;
            else:
                u = mid-1;
    return False

list = [2,3,4,5,6,7,9]
n = 10

if search(list,n):
    print('found at', pos)

else:
    print('not found')
