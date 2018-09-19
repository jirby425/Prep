import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    n = len(arr)
    if n < 2:
        return 0

    swaps = 0
    i = 0
    while i < n:
        if int(arr[i]) == i + 1:
            i += 1
            #print arr[i], "in correct spot", i
        else:
            val = int(arr[i])-1
            tmp = arr[val]
            arr[val] = arr[i]
            arr[i] = tmp
            swaps +=1
            #print "Swap", arr[val], arr[i]
        #print arr


    return swaps

if __name__ == '__main__':

    arr = []
    fptr = open("C:\Users\Jackson\Desktop\ComputerScienceProjects\Prep\HackerRank\input07.txt", "r")



    for line in fptr:
        for word in line.split():
            arr.append(word)



    print len(arr)

    res = minimumSwaps(arr)
    print res

    #fptr.write(str(res) + '\n')

    #fptr.close()

    # 7 1 3 5 2 4 6 8
    # 6 1 3 5 2 4 7 8
    # 4 1 3 5 2 6 7 8
    # 5 1 3 4 2 6 7 8
    # 2 1 3 4 5 6 7 8
    # 1 2 3 4 5 6 7 8
