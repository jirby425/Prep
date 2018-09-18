

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):



    a_in_str = s.count("a")
    count = 0
    mult = n // len(s)

    if mult == 0:
        count = (s[:n]).count("a")
    else:
        remainder = n % len(s)
        count = (a_in_str * mult) + ((s[:remainder]).count("a"))

    return count




if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = "a"

    n = 100000000

    result = repeatedString(s, n)

    print result

    #fptr.write(str(result) + '\n')

    #fptr.close()
