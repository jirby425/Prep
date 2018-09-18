import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = jumper(c, 0, 0)
    return jumps

def jumper(c, i, jumps):
    if i >= len(c)-1:
        return jumps
    if i == len(c)-2:
        return jumps+1

    if i < len(c):
        j1 = j2 = float('inf')
        if(c[i+1]  != 1):
            j1 = jumper(c, i+1, jumps+1)
        if(c[i+2] != 1):
            j2 = jumper (c, i+2, jumps+1)

        return min(j1, j2)





if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = 6
    c = [0, 0, 0, 1, 0, 0]


    result = jumpingOnClouds(c)
    print result
    ##fptr.write(str(result) + '\n')

    #fptr.close()
