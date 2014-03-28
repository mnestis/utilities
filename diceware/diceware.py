#!/usr/bin/python

"""
diceware.py -- Darren Richardson -- 2014-03-26 -- v1.0

This script generates diceware passwords from the std.edu common word list.

It takes two parameters:

    1. An integer: this is the number of words in the password;
    2. A path: this is the path to the std.edu wordlist file.

It uses the random.SystemRandom class, meaning that it should use your system's
source of entropy, and should be more than adequate for this purpose.
"""

def import_wordlist(filepath, indexLength):
    """Takes a path and returns a dictionary of words."""
    import re

    wordfile = open(filepath, "r")

    wordlist = {}
    # This is the regex that works for the std.edu wordlist. It may need to be changed to accommodate others.
    word_re = re.compile("^([1-6]{"+str(indexLength)+"})\s([A-Za-z0-9!'\"#\$%&\(\)\*\+\-:;=\?@\.]+)$")

    for line in wordfile.readlines():
        match = word_re.match(line)
        if match:
            wordlist[match.groups()[0]] = match.groups()[1]

    # Check that there are the right number of words. An incomplete dictionary would potentially cause problems.
    if len(wordlist) != 6**indexLength:
        raise ValueError("The number of elements of the word dictionary is not right. Actual value: %s, Expected value: %s" % (len(wordlist),6**indexLength))

    return wordlist

def generate_password(wordcount, words):
    """Takes a dictionary of words, and selects a password.
    The password has the number of words equal to 'wordcount'.
    The words are separated by spaces."""

    from random import SystemRandom
    rand = SystemRandom()

    return reduce(lambda a, b: a + " " + b,
                  map(lambda key: words[key],
                      rand.sample(words, wordcount)))

if __name__=="__main__":
    import sys

    wordcount = int(sys.argv[1])
    indexLength = 5 # This is fixed to 5 for the std.edu wordlist, but there's no reason it couldn't be longer.
    filepath = sys.argv[2]

    if wordcount <= 1:
        raise Exception("The second parameter to this program needs to be greater or equal to 1.")

    print generate_password(wordcount, import_wordlist(filepath, indexLength))
