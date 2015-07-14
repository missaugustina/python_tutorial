#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
# surprised they didn't add this by default!!


# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

import re
import unicodedata

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Basic string exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# It's ok if you do not complete all the functions, and there
# are some additional functions to try in string2.py.


# A. donuts
# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5'
# and donuts(23) returns 'Number of donuts: many'
def donuts(count):
  if not isinstance(count, int):
    raise TypeError("Please provide a count of type int")

  if count >= 10:
    donutsCount = "many"
  else:
    donutsCount = str(count)

  return " ".join(["Number of donuts:", donutsCount])


# B. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.
def both_ends(s):
  if not (isinstance(s, str) or isinstance(s, unicode)):
    raise TypeError("Please provide a string")

  length = len(s)
  if length < 2:
    return ""
  else:
    # originally had this but if we have less than 4 chars this won't do what the exercise requires
    # firstAndLast2 = re.compile(r"^(\w{2})(?:.*)(\w{2})$", re.UNICODE)

    frontRe = re.compile(r"^(\w{2})", re.UNICODE)
    frontResult = re.search(frontRe, s)

    backRe = re.compile(r"(\w{2})$", re.UNICODE)
    backResult = re.search(backRe, s)

    return "".join([frontResult.group(1), backResult.group(1)])


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
  if not (isinstance(s, str) or isinstance(s, unicode)):
    raise TypeError("Please provide a string")

  return s[0] + s[1:].replace(s[0], '*')


# D. MixUp
# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.
def mix_up(a, b):
  if not (isinstance(a, str) or isinstance(a, unicode)):
    raise TypeError("Please provide a string")

  if not (isinstance(b, str) or isinstance(b, unicode)):
    raise TypeError("Please provide a string")

  return " ".join([b[0:2] + a[2:], a[0:2] + b[2:]])


# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
  print 'donuts'
  # Each line calls donuts, compares its result to the expected for that call.
  test(donuts(4), 'Number of donuts: 4')
  test(donuts(9), 'Number of donuts: 9')
  test(donuts(10), 'Number of donuts: many')
  test(donuts(99), 'Number of donuts: many')

  try:
    donuts("foo")
  except TypeError:
    print '%s %s throws exception' % (" OK", "\"foo\" as count")


  print
  print 'both_ends'
  test(both_ends('spring'), 'spng')
  test(both_ends('Hello'), 'Helo')
  test(both_ends('a'), '')
  test(both_ends('xyz'), 'xyyz')
  test(both_ends(u'äpfel'), u'äpel')
  test(both_ends(u'Γαζέες καὶ μυρτιὲς δὲν θὰ βρῶ πιὰ στὸ χρυσαφὶ ξέφωτο'), u'Γατο')
  test(both_ends('123Hello'), '12lo')
  try:
    both_ends(123)
  except TypeError:
    print '%s %s throws exception' % (" OK", "\"123\" as s")

  
  print
  print 'fix_start'
  test(fix_start('babble'), 'ba**le')
  test(fix_start('aardvark'), 'a*rdv*rk')
  test(fix_start('google'), 'goo*le')
  test(fix_start('donut'), 'donut')
  test(fix_start(u'äpfeläpfel'), u'äpfel*pfel')
  try:
    fix_start(123)
  except TypeError:
    print '%s %s throws exception' % (" OK", "\"123\" as s")

  print
  print 'mix_up'
  test(mix_up('mix', 'pod'), 'pox mid')
  test(mix_up('dog', 'dinner'), 'dig donner')
  test(mix_up('gnash', 'sport'), 'spash gnort')
  test(mix_up('pezzy', 'firm'), 'fizzy perm')
  test(mix_up(u'rote', u'äpfel'), u'äpte rofel')

  try:
    mix_up(123, 456)
  except TypeError:
    print '%s %s throws exception' % (" OK", "\"123, 456\" as a, b")

  try:
    mix_up('abc', 456)
  except TypeError:
    print '%s %s throws exception' % (" OK", "\"abc, 456\" as a, b")

  try:
    mix_up(123, 'abc')
  except TypeError:
    print '%s %s throws exception' % (" OK", "\"123, abc\" as a, b")


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
