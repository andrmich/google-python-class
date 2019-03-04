#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Basic list exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# It's ok if you do not complete all the functions, and there
# are some additional functions to try in list2.py.

# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.
def match_ends(words):
    return len([word for word in words if len(word)>=2 and word[0]==word[-1]])

#print(match_ends(['aaa', 'be', 'abc', 'hello']))
  # test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
  # test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
  # test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
def front_x(words):
    strings_with_x = sorted([word for word in words if word[0] == 'x'])
    other_strings = sorted([word for word in words if word[0]!= 'x'])
    return strings_with_x + other_strings

#print(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']))
# test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
#        ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
#   test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
#        ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
#   test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
#        ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])


# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.
def sort_last(tuples):
  def last_element(tuples):
      return tuples[-1]
  return sorted(tuples, key=last_element)

#print(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]))

  # test(sort_last([(1, 3), (3, 2), (2, 1)]),
  #      [(2, 1), (3, 2), (1, 3)])
  # test(sort_last([(2, 3), (1, 2), (3, 1)]),
  #      [(3, 1), (1, 2), (2, 3)])
  # test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
  #      [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


#list2
# Additional basic list exercises

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
    result = []
    if len(nums) > 0:
        for number in nums:
            if len(result) == 0:
                result.append(number)
            if number != result[-1]:
                result.append(number)

    return result

print(remove_adjacent([2, 2, 3, 3, 3, 4, 3]))
  # test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
  # test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
  # test(remove_adjacent([]), [])

# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(list1, list2):
  return sorted((list1+list2))

print(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']))
# test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
#        ['aa', 'bb', 'cc', 'xx', 'zz'])
#   test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
#        ['aa', 'bb', 'cc', 'xx', 'zz'])
#   test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
#        ['aa', 'aa', 'aa', 'bb', 'bb'])
