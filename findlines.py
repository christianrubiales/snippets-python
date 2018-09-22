#!/usr/bin/env python

# Takes in the lines from stdin
# prints lines containing any of the supplied arguments
#
# Example: cat findlines-test.txt | findlines.py a b c
# Result: the above command will print only those lines containing "a" or "b" or "c"

import sys

linenum = 0
try:
  for line in sys.stdin:
    linenum += 1
    for arg in sys.argv:
      if arg in line:
        print(line.rstrip())
        break
except:
  print("Error in line: ", linenum)
  raise
