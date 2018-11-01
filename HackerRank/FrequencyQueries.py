

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    d = {}
    out = []
    for i in queries:
        if i[0] == 1:
            if i[1] not in d:
                d[i[1]] = 1
            else:
                d[i[1]] += 1

        elif i[0] == 2:
            if i[1]  in d:
                d[i[1]] -= 1

        else:
            if i[1] in d.values():
                out.append(1)
            else:
                out.append(0)
    return out

if __name__ == '__main__':

    queries = [(1, 5),
(1 ,6),
(3 ,2),
(1 ,10),
(1 ,10),
(1 ,6),
(2 ,5),
(3, 2)]
    x =freqQuery(queries)
    print x
