

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):

    count = 0
    iters = 0
    swapped = False

    for i in range (0, len(q)):
        if q[i] - 3 > i:
            print "Too chaotic"
            return

    for i in range(0,len(q)-1):
        for j in range (0, len(q)-1):
            iters = iters +1
            if q[j] > q[j+1]:
                count = count + 1
                q[j], q[j+1] = q[j+1], q[j]
                swapped = True
                print "swapped:", q[j+1], q[j]
        if swapped:
            swapped = False
        else:
            break

    print count


if __name__ == '__main__':
    # t = int(raw_input())
    #
    # for t_itr in xrange(t):
    #     n = int(raw_input())
    #
    #     q = map(int, raw_input().rstrip().split())

    n = 8
    q = [1, 2, 5, 3, 7, 8, 6, 4]
    #
    # 1 2 3 4 5 6 7 8
    # 1 2 3 5 4 6 7 8
    # 1 2 5 3 4 6 7 8  5 two swaps
    # 1 2 5 3 4 7 6 8
    # 1 2 5 3 7 4 6 8  7 two swaps
    # 1 2 5 3 7 6 4 8  6 one swap
    # 1 2 5 3 7 6 8 4
    #
    # 1 2 5 3 7 8 6 4  8 two swaps
    # 0 1 2 3 4 5 6 7
    # 0+0+2+0+2+2+0+0



    print minimumBribes(q)
