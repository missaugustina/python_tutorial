#!/usr/bin/python2.4 -tt
# -*- coding: utf-8 -*-
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import math

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
  if not (isinstance(s, str) or isinstance(s, unicode)):
    raise TypeError("Please provide a string")

  if len(s) < 3:
    return s
  else:
    # check if the string ends in ing
    if re.search(r'ing$', s):
      return s + 'ly'
    else: # if no replace then return s + ing
      return s + 'ing'
  return


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
  if not (isinstance(s, str) or isinstance(s, unicode)):
    raise TypeError("Please provide a string")
  return re.sub(r'not.*bad', 'good', s)

# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def split_at(s):
  halfLen = int(math.ceil(float(len(s)) / 2))
  return (s[0:halfLen], s[halfLen:])

def front_back(a, b):
  if not (isinstance(a, str) or isinstance(s, unicode)):
    raise TypeError("Please provide a string")

  if not (isinstance(b, str) or isinstance(s, unicode)):
    raise TypeError("Please provide a string")

  words = split_at(a) + split_at(b)
  return "".join([words[0], words[2], words[1], words[3]])


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print 'verbing'
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')
  test(verbing('mingling'), 'minglingly')
  try:
    verbing(123)
  except TypeError:
    print '%s %s throws exception' % (" OK", "\"123\" as s")

  print
  print 'not_bad'
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print
  print 'front_back'
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()
