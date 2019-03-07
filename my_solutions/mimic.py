#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""
import random
import sys
import string
import re
import pprint
from collections import defaultdict
from itertools import chain

def get_text_from_file(file_path):
    file = open(file_path, 'r')
    text = file.read().strip().lower()
    file.close()
    return text


def remove_punctuation(text):
    for ch in string.punctuation:
        if ch == "'":
            continue
        text = text.replace(ch, '')

    new = re.sub(r"[\s']", r' ', text)
    without_apostrophe = re.sub(r"'\s+", r' ', new)
    words = without_apostrophe.split()
    return words


def dict_word_with_words_after_it(words):
    #  Returns mimic dict mapping each word to list of words which follow it.
    pairs = []
    for i in range(len(words) - 2):
        pairs.append((words[i], words[i + 1]))

    unique_pairs = set(pairs)
    mimic_dict = defaultdict(list)
    for k, *v in unique_pairs:
        mimic_dict[k].append(v)

    for k,v in mimic_dict.items():
        mimic_dict[k] = list(chain(*v))

    return mimic_dict

#
def get_random_text(file_path, word):
    text = get_text_from_file(file_path)
    words = remove_punctuation(text)
    mimic_dict = dict_word_with_words_after_it(words)
    random_text = [word, ]
    while len(random_text) < 200:
        word = random.choice(mimic_dict[word])
        random_text.append(word)
    result = ' '.join(random_text)
    return result


if __name__ == '__main__':
    pprint.pprint(get_random_text('/home/aisim/Downloads/google-python-exercises/basic/alice.txt', 'milk'))
# '/home/aisim/Downloads/google-python-exercises/basic/alice.txt
