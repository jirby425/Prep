

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):

    if n == 0:
        return 0

    i = 0
    seaLevel = 0
    numValleys = 0
    while i < n:
        if s[i] == 'D':
            seaLevel = seaLevel - 1
        if s[i] == 'U':
            seaLevel = seaLevel + 1
            if seaLevel == 0:
                numValleys = numValleys+1
        i = i+1
        #print "SeaLevel: ", seaLevel, "after: ", i


    return numValleys




if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = 8

    s = "UDDDUDUU"

    result = countingValleys(n, s)

    print result
