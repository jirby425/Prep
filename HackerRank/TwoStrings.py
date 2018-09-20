#!/bin/python

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    d = {}
    for i in range(len(s1)):
        d[s1[i]] = 0

    print d
    for i in range(len(s2)):
        if s[i] in d:
            return "YES"
    return "NO"

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #q = int(raw_input())

    s1 = "hello"
    s2 = "world"

    output = twoStrings(s1, s2)
    print output
