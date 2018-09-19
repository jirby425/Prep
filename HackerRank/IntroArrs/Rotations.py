

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    if len(a) < 2:
        return a

    for i in range (0, d):
        val = a[0]
        a.pop(0)
        a.append(val)
    return a

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #nd = raw_input().split()

    n = 5

    d = 4

    a = [1, 2, 3, 4, 5]

    result = rotLeft(a, d)
    print result

    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
