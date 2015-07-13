#!/usr/bin/env python

import sys # includes operating system functionality

def Hello(name):
  return 'Hello ' + name + '!!!'

def main ():
  print Hello(sys.argv[1])

if __name__ == '__main__':
  main()
