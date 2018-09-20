#!/bin/python

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):

    d = {}
    count = 0
    for i in arr:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    print d

    for i in d.keys():
        if (i*r) in d and (i*r*r) in d:
            v1 = d[i]
            v2 = d[i*r]
            v3 = d[i*r*r]
            if r == 1:
                v1-=3
                v2-=4
                v3-=5
            print v1, i
            print v2, i*r
            print v3, i*r*r
            count += (v1 * v2 * v3)

    return count


if __name__ == '__main__':
    fptr = open("C:\Users\Jackson\Desktop\ComputerScienceProjects\Prep\HackerRank\input02.txt", "r")
    for line in fptr:
        arr= line.split()

    #arr = [1, 3, 9, 9, 27, 81]
    r = 1
    result = countTriplets(arr, r)
    print result
