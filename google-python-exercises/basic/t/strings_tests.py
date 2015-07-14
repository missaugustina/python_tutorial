import unittest
import sys

sys.path.append('../')
import string1

class TestStringMethods(unittest.TestCase):

  #def test_upper(self):
  #    self.assertEqual('foo'.upper(), 'FOO')
  #
  #def test_isupper(self):
  #    self.assertTrue('FOO'.isupper())
  #    self.assertFalse('Foo'.isupper())
  #
  #def test_split(self):
  #    s = 'hello world'
  #    self.assertEqual(s.split(), ['hello', 'world'])
  #    # check that s.split fails when the separator is not a string
  #    with self.assertRaises(TypeError):
  #        s.split(2)

  def test_donuts(self):
    count = 4
    self.assertEquals(string1.donuts(4), 'Number of donuts: 4')

if __name__ == '__main__':
    unittest.main()
