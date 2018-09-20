
import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):

    d = {}
    for i in magazine:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    for i in note:
        if i not in d or d[i]==0:
            print "No"
            return
        else:
            d[i] -= 1

    print "Yes"

if __name__ == '__main__':
    #mn = raw_input().split()


    #m = int(mn[0])

    #n = int(mn[1])

    magazine = "give me one grand today night".split()

    note = "give one grand today".split()

    print magazine, note


    checkMagazine(magazine, note)
