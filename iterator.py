# nums = [1,2,3,4]
#
# it = iter(nums)
#
# print(it.next()) # for getting the value we'll a use an inbuilt fn .
# print(next(it)) # another way.

# it will print the obj of iterator, but  we want value.
# it = iter(nums)
# print(it)

# ---------------------------------------------------

# creating own class and giving my own object

class topten:

    def __init__(self):
        self.num = 1

    def __iter__(self):  # iter mthod will give object of iterator
        return self

    def __next__(self):   # next will give the next object.

        if self.num <= 10:

            val = self.num
            self.num += 1

            return val
        else :
            raise StopIteration # or exit()



values = topten()

for i in values:
    print(i)
