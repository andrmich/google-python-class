#!/usr/bin/python2.4 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/


# A. donuts
# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5'
# and donuts(23) returns 'Number of donuts: many'
def donuts(count):
    if count < 10:
        return f'Number of donuts: {count}'
    else:
        return 'Number of donuts: many'


#print(donuts(99))


#
# def main():
#   print (donuts)
#   # Each line calls donuts, compares its result to the expected for that call.
#   test(donuts(4), 'Number of donuts: 4')
#   test(donuts(9), 'Number of donuts: 9')
#   test(donuts(10), 'Number of donuts: many')
#   test(donuts(99), 'Number of donuts: many')


# B. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.
def both_ends(s):
    if len(s) < 2:
        return ''
    else:
        return s[0:2] + s[-2:]


#print(both_ends('xyz'))


# test(both_ends('spring'), 'spng')
#   test(both_ends('Hello'), 'Helo')
#   test(both_ends('a'), '')
#   test(both_ends('xyz'), 'xyyz')

# C. fix_start
# Given a string s, return a string
# where all occurences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.
def fix_start(s):
    return s[0] + s[1:].replace(s[0], '*')


#print(fix_start('donut'))
# test(fix_start('babble'), 'ba**le')
# test(fix_start('aardvark'), 'a*rdv*rk')
# test(fix_start('google'), 'goo*le')
# test(fix_start('donut'), 'donut')

# D. MixUp
# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.
def mix_up(a, b):
    return f'{b[0:2]+a[2:]} {a[0:2]+b[2:]}'

#print(mix_up('gnash', 'sport'))
# test(mix_up('mix', 'pod'), 'pox mid')
#   test(mix_up('dog', 'dinner'), 'dig donner')
#   test(mix_up('gnash', 'sport'), 'spash gnort')
#   test(mix_up('pezzy', 'firm'), 'fizzy perm')

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
    if len(s) <3: return s
    return s+'ing' if s[-3:] != 'ing' else s+'ly'

#print(verbing('doing'))
# test(verbing('hail'), 'hailing')
#   test(verbing('swiming'), 'swimingly')
#   test(verbing('do'), 'do')

# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
import re
def not_bad(s):
    return re.sub(r'not.{1,}bad', 'good', s)

#print(not_bad("This dinner is not that bad!"))
# test(not_bad('This movie is not so bad'), 'This movie is good')
#   test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
#   test(not_bad('This tea is not hot'), 'This tea is not hot')
#   test(not_bad("It's bad yet not"), "It's bad yet not")


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back

import math
def front_back(a, b):
    a_split = math.ceil(len(a)/2)
    b_split = math.ceil(len(b)/2)
    return a[0:a_split]+b[0:b_split]+a[a_split:]+b[b_split:]

print(front_back('Kitten', 'Donut'))

# test(front_back('abcd', 'xy'), 'abxcdy')
#   test(front_back('abcde', 'xyz'), 'abcxydez')
#   test(front_back('Kitten', 'Donut'), 'KitDontenut')
