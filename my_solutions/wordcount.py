#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/
import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
# def main():
#   if len(sys.argv) != 3:
#     print 'usage: ./wordcount.py {--count | --topcount} file'
#     sys.exit(1)
#
#   option = sys.argv[1]
#   filename = sys.argv[2]
#   if option == '--count':
#     print_words(filename)
#   elif option == '--topcount':
#     print_top(filename)
#   else:
#     print 'unknown option: ' + option
#     sys.exit(1)
#
# if __name__ == '__main__':
#   main()
import pprint
import string

alice_file = open('/home/aisim/Downloads/google-python-exercises/basic/alice.txt')
alice_content = alice_file.readlines()

text = ''.join(alice_content)
for ch in string.punctuation:
    if ch == "'":
        continue
    text = text.replace(ch, '')
text = text.lower().split()

alice_d = {}

for word in text:
    if word not in alice_d:
        alice_d[word] = 0
    alice_d[word] += 1

def alphabetical(d):
    t = []
    for k in sorted(alice_d.keys()):
         t.append((k, alice_d[k]))
    return t[:8]

def most_frequent(d):
    v = list(d.values())
    k = list(d.keys())
    return (sorted(zip(d.values(), d.keys()), reverse=True))[:3]

if __name__ == "__main__":
    pprint.pprint(most_frequent(alice_d))
    pprint.pprint(alphabetical(alice_d))
