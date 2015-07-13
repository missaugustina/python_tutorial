#!/usr/bin/env python

import sys # includes operating system functionality

def Hello(name):
  if not isinstance(name, str):
    raise NameError('No name provided')

  return 'Hello ' + name + '!!!'

def main ():
  args = sys.argv
  if len(args) < 2:
    raise IndexError('Please provide a name!')
  name = args[1] # set to None to trigger NameError exception in Hello()
  print Hello(name)

if __name__ == '__main__':
  main()
