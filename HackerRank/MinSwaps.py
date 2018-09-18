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
        if arr[i] == i + 1:
            i += 1
        else:
            tmp = arr[arr[i]-1]
            arr[arr[i]-1] = arr[i]
            arr[i] = tmp

            swaps +=1
        #print arr


    return swaps

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = 7

    arr = [7, 1, 3, 5, 2, 4, 6, 8]

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
