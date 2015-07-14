#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
import unittest
import sys

sys.path.append('../')
import string1

class TestStringMethods(unittest.TestCase):

  def test_donuts(self):
    self.assertEquals(string1.donuts(4), 'Number of donuts: 4', 'Check number under 10')
    self.assertEquals(string1.donuts(10), 'Number of donuts: many', 'Check number over 10')
    with self.assertRaises(TypeError): # Check TypeError exception is raised for string
        string1.donuts("foo")

  def test_both_ends(self):
    self.assertEquals(string1.both_ends('spring'), 'spng', 'Check 6 char string')
    self.assertEquals(string1.both_ends('Hello'), 'Helo', 'Check 5 char string')
    self.assertEquals(string1.both_ends('xyz'), 'xyyz', 'Check 4 char string')
    self.assertEquals(string1.both_ends('a'), '', 'Check string < 3 chars')
    self.assertEquals(string1.both_ends(u'äpfel'), u'äpel', 'Check unicode string')
    self.assertEquals(string1.both_ends(u'Γαζέες καὶ μυρτιὲς δὲν θὰ βρῶ πιὰ στὸ χρυσαφὶ ξέφωτο'), u'Γατο', 'Check unicode string with whitespace')
    self.assertEquals(string1.both_ends('123Hello'), '12lo', 'Check string containing numbers')
    with self.assertRaises(TypeError): # Check TypeError exception is raised for int
        string1.both_ends(123)

  def test_fix_start(self):
    self.assertEquals(string1.fix_start('babble'), 'ba**le', 'Check string with 2 consecutive chars to replace')
    self.assertEquals(string1.fix_start('aardvark'), 'a*rdv*rk', 'Check string with 2 distributed chars to replace')
    self.assertEquals(string1.fix_start('google'), 'goo*le', 'Check string with only 1 character to replace')
    self.assertEquals(string1.fix_start('donut'), 'donut', 'Check string with no characters to replace')
    self.assertEquals(string1.fix_start(u'äpfeläpfel'), u'äpfel*pfel', 'Check unicode string')
    with self.assertRaises(TypeError): # Check TypeError exception is raised for int
        string1.fix_start(123)

  def test_mix_up(self):
    self.assertEquals(string1.mix_up('mix', 'pod'), 'pox mid', 'Check 3 char strings')
    self.assertEquals(string1.mix_up('dog', 'dinner'), 'dig donner', 'Check first string is shorter than the second')
    self.assertEquals(string1.mix_up('gnash', 'sport'), 'spash gnort', 'Check two 5 char strings')
    self.assertEquals(string1.mix_up('pezzy', 'firm'), 'fizzy perm', 'Check first string is longer than second')
    self.assertEquals(string1.mix_up(u'rote', u'äpfel'), u'äpte rofel', 'Check unicode strings')
    with self.assertRaises(TypeError): # check 2 int args
        string1.mix_up(123, 456)
    with self.assertRaises(TypeError): # check second arg is an int
        string1.mix_up('abc', 456)
    with self.assertRaises(TypeError): # check first arg is an int
        string1.mix_up(123, 'abc')

if __name__ == '__main__':
    unittest.main(verbosity=2)
