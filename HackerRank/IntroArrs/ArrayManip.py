import math
import os
import random
import re
import sys


def arrayManipulation(n, queries):

    maxVal = 0
    size = n+1
    l = [0] * size

    for i in queries:
        val = int(i[2])
        start = int(i[0])
        end = (int(i[1])+1)
        #print val, start, end
        l[start] += val
        if end < n+1:
            l[end] -= val
        #sprint l

    x = 0
    for i in l:
        x = x + i
        if maxVal < x:
            maxVal = x

    #print l
    return maxVal

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #nm = raw_input().split()

    n = 4

    queries = []
    fileptr= open("C:\Users\Jackson\Desktop\ComputerScienceProjects\Prep\HackerRank\input01.txt", "r")

    for line in fileptr:
        queries.append(line.split())

    #print(len(queries))

    result = arrayManipulation(n, queries)
    print result
