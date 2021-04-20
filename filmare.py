# def is_even(n):
#     return n%2==0
# # the fn used here is only to be used here but normally fn are reuseable.
#
# nums = (3,2,6,8,4,6,2,9)
# # (list)
# evens = list(filter(is_even, nums))
#
# print(evens)
# (take list from you and filter it)

# Using lambda for this
from functools import reduce

nums = (3,2,6,8,4,6,2,9)

evens = list(filter(lambda n : n%2==0, nums))
print(evens)

doubles = list(map(lambda n : n*2, evens))
print(doubles)s

sum = reduce(lambda a,b : a+b, doubles)
print(sum)

# MAP() : The map() function applies a given function to each item of an iterable (list, tuple etc.) and returns a list of the results.
# map() is a built-in function that allows you to process and transform all the items in an iterable without using an explicit for loop, a technique commonly known as mapping

# map: Takes a function f, and a list L1, and returns a list L2 obtained by applying f to every element of L1. Say f is a function that takes x and returns 2x. Then, map(f, [1,2,3,4]) returns [2,4,6,8].
#
# reduce: Takes a binary operator f, a list L and a seed value (or identity element). It returns the seed value if the list is empty. Otherwise, it applies the binary operator f to the seed and first element of L, then applies f to the result of this and the 2nd element of L, and so on till L is exhausted. The result is returned. This can be seen as a generalization of factorial function.
#
# filter: Takes a boolean function f and a list L1. It applies the function to each element of L1, and list of those elements that give true is returned.
