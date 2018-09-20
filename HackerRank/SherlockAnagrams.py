

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    d = {}
    count = 0
    anag = ""
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            ls = list(s[i:j])
            ls.sort()
            anag = anag.join(ls)
            if anag not in d:
                d[anag] = 0
            else:
                d[anag] +=1
                count = count + d[anag]
    return count




if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = "abcd"



    result = sherlockAndAnagrams(s)
    print result

    #fptr.write(str(result) + '\n')

    #fptr.close()
