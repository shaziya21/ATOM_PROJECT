def topten():

    n = 1

    while n <= 10:
        sq = n*n
        yield sq     # yield is a special keyword which will make ur function as a generator
                     # yield will return the value in the format of iterator.
        n += 1

values = topten()

for i in values:
    print(i)
